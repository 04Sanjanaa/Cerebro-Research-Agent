"""
Tests for CEREBRO Research Agent
Tests: retrieval ranking, citation generation, grounding, API endpoints, document ingestion.
Run with: pytest tests/ -v
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

import pytest

# ── Retrieval Tests ────────────────────────────────────────────────────────────

LEAVE_CHUNK = {
    "id": "doc_000_chunk_000",
    "text": "Full-time employees are entitled to 20 days of paid annual leave per calendar year. Leave accrues at 1.67 days per month.",
    "metadata": {"source": "employee_handbook.txt", "section": "Annual Leave", "doc_id": "doc_000"}
}
PASSWORD_CHUNK = {
    "id": "doc_001_chunk_000",
    "text": "All user account passwords must meet the following requirements: minimum length 12 characters, must include uppercase, lowercase, numbers, and special characters.",
    "metadata": {"source": "security_policy.txt", "section": "Password Requirements", "doc_id": "doc_001"}
}
REMOTE_CHUNK = {
    "id": "doc_000_chunk_001",
    "text": "Employees must complete 3 months probation before being eligible for remote work. Manager approval is required. Core hours are 10 AM to 3 PM.",
    "metadata": {"source": "employee_handbook.txt", "section": "Remote Work Policy", "doc_id": "doc_000"}
}
EXPENSE_CHUNK = {
    "id": "doc_002_chunk_000",
    "text": "Meal reimbursement limits: up to $50 per day for domestic travel, $75 per day for international travel. Hotel: up to $200 per night.",
    "metadata": {"source": "expense_policy.txt", "section": "Expense Limits", "doc_id": "doc_002"}
}

ALL_CHUNKS = [LEAVE_CHUNK, PASSWORD_CHUNK, REMOTE_CHUNK, EXPENSE_CHUNK]


def make_retrieval_service(chunks=None):
    from services.embedding_service import EmbeddingService
    from services.retrieval_service import RetrievalService
    emb = EmbeddingService()
    svc = RetrievalService(emb, top_k=5, min_score=0.20, alpha=0.60)
    svc.index(chunks or ALL_CHUNKS)
    return svc


class TestRetrieval:
    def test_leave_query_ranks_leave_chunk_first(self):
        """Leave-related query should rank the leave chunk above unrelated chunks."""
        svc = make_retrieval_service()
        results = svc.retrieve("How many days of annual leave am I entitled to?")
        assert len(results) > 0, "Expected at least one result"
        assert results[0]["id"] == LEAVE_CHUNK["id"], (
            f"Expected leave chunk first, got {results[0]['id']}"
        )

    def test_password_query_ranks_password_chunk_first(self):
        """Password query should rank the security policy chunk first."""
        svc = make_retrieval_service()
        results = svc.retrieve("What are the password complexity requirements?")
        assert len(results) > 0
        assert results[0]["id"] == PASSWORD_CHUNK["id"], (
            f"Expected password chunk first, got {results[0]['id']}"
        )

    def test_unrelated_query_below_threshold(self):
        """Stock price query should have no sufficient evidence."""
        svc = make_retrieval_service()
        results = svc.retrieve("What is the current stock price?")
        has_evidence = svc.has_sufficient_evidence(results)
        assert not has_evidence, "Stock price query should return insufficient evidence"

    def test_results_sorted_by_score(self):
        """Results must be sorted by combined_score descending."""
        svc = make_retrieval_service()
        results = svc.retrieve("annual leave policy")
        if len(results) > 1:
            for i in range(len(results) - 1):
                assert results[i]["combined_score"] >= results[i+1]["combined_score"], \
                    "Results are not sorted by score"

    def test_result_contains_required_fields(self):
        """Each result must have the required metadata fields."""
        svc = make_retrieval_service()
        results = svc.retrieve("leave policy")
        if results:
            r = results[0]
            assert "semantic_score" in r
            assert "bm25_score" in r
            assert "combined_score" in r
            assert "relevance_label" in r
            assert "metadata" in r

    def test_remote_work_query(self):
        """Remote work query should surface remote work chunk."""
        svc = make_retrieval_service()
        results = svc.retrieve("What are the remote work requirements?")
        ids = [r["id"] for r in results]
        assert REMOTE_CHUNK["id"] in ids, "Remote work chunk should appear in results"


# ── Citation Tests ─────────────────────────────────────────────────────────────

class TestCitations:
    def test_build_assigns_sequential_ids(self):
        from services.citation_service import CitationService
        svc = make_retrieval_service()
        results = svc.retrieve("annual leave")
        cs = CitationService()
        citations, context = cs.build(results)
        for i, c in enumerate(citations, start=1):
            assert c["id"] == i
            assert c["label"] == f"[{i}]"

    def test_context_contains_citation_headers(self):
        from services.citation_service import CitationService
        svc = make_retrieval_service()
        results = svc.retrieve("password requirements")
        cs = CitationService()
        citations, context = cs.build(results)
        if citations:
            assert "[1]" in context
            assert "Source:" in context

    def test_citation_has_source_and_section(self):
        from services.citation_service import CitationService
        svc = make_retrieval_service()
        results = svc.retrieve("leave entitlement")
        cs = CitationService()
        citations, _ = cs.build(results)
        if citations:
            c = citations[0]
            assert c["source"] != ""
            assert "chunk_id" in c
            assert "passage" in c


# ── Grounding / LLM Tests ─────────────────────────────────────────────────────

class TestGrounding:
    def test_insufficient_evidence_response(self):
        """When has_evidence=False the LLM service returns the insufficiency message."""
        from services.llm_service import LLMService, INSUFFICIENT_EVIDENCE_RESPONSE
        llm = LLMService()  # no API key
        result = llm.generate_grounded_answer(
            query="What is the stock price?",
            evidence_context="",
            citations=[],
            has_evidence=False,
        )
        assert result["success"]
        assert result["insufficient_evidence"]
        assert "couldn't find" in result["response"].lower() or "insufficient" in result["response"].lower()

    def test_keyword_fallback_includes_sources(self):
        """Keyword fallback should reference source docs in the response."""
        from services.llm_service import LLMService
        from services.citation_service import CitationService
        llm = LLMService()
        svc = make_retrieval_service()
        results = svc.retrieve("annual leave")
        cs = CitationService()
        citations, context = cs.build(results)
        result = llm.generate_grounded_answer("leave", context, citations, has_evidence=True)
        assert result["success"]
        assert "employee_handbook" in result["response"].lower() or "[1]" in result["response"]


# ── Document Ingestion Tests ───────────────────────────────────────────────────

class TestDocumentIngestion:
    def test_chunk_text_splits_correctly(self):
        from services.document_service import chunk_text
        long_text = " ".join(["word"] * 600)
        chunks = chunk_text(long_text, chunk_size=200, overlap=30, source_name="test.txt")
        assert len(chunks) >= 2, "Long text should split into multiple chunks"

    def test_chunk_preserves_metadata(self):
        from services.document_service import chunk_text
        chunks = chunk_text("Hello world. This is a test.", source_name="test.txt", doc_id="doc_x")
        assert len(chunks) >= 1
        c = chunks[0]
        assert c["metadata"]["source"] == "test.txt"
        assert c["metadata"]["doc_id"] == "doc_x"
        assert "chunk_index" in c["metadata"]

    def test_load_txt_file(self, tmp_path):
        """DocumentService should load a .txt file and return chunks."""
        import textwrap
        from services.document_service import DocumentService
        doc_dir = tmp_path / "kb"
        doc_dir.mkdir()
        sample = doc_dir / "sample.txt"
        sample.write_text(textwrap.dedent("""
            SECTION 1: LEAVE POLICY
            Employees are entitled to 20 days annual leave.
            Leave must be requested two weeks in advance.

            SECTION 2: REMOTE WORK
            Employees need manager approval for remote work.
            Core hours are 10 AM to 3 PM.
        """), encoding="utf-8")

        ds = DocumentService(knowledge_base_dir=str(doc_dir))
        chunks = ds.load_all(chunk_size=50, overlap=5)
        assert len(chunks) >= 1
        texts = " ".join(c["text"] for c in chunks)
        assert "20 days" in texts

    def test_empty_directory_returns_no_chunks(self, tmp_path):
        from services.document_service import DocumentService
        ds = DocumentService(knowledge_base_dir=str(tmp_path))
        chunks = ds.load_all()
        assert chunks == []


# ── API Endpoint Tests ─────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def client():
    """Flask test client fixture."""
    # Set env before importing app
    os.environ.setdefault("FLASK_TESTING", "1")
    from app import app
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


class TestAPI:
    def test_health_endpoint(self, client):
        resp = client.get("/api/health")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["status"] == "healthy"
        assert "chunks_indexed" in data

    def test_research_endpoint_returns_answer(self, client):
        resp = client.post("/api/research",
                           json={"query": "What is the annual leave entitlement?"},
                           content_type="application/json")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["success"]
        assert "answer" in data
        assert "citations" in data
        assert "retrieval_info" in data

    def test_research_endpoint_insufficient(self, client):
        resp = client.post("/api/research",
                           json={"query": "What is the stock market index today?"},
                           content_type="application/json")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["success"]
        assert data["insufficient_evidence"] is True

    def test_research_rejects_empty_query(self, client):
        resp = client.post("/api/research",
                           json={"query": ""},
                           content_type="application/json")
        assert resp.status_code == 400

    def test_documents_endpoint(self, client):
        resp = client.get("/api/documents")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["success"]
        assert isinstance(data["documents"], list)

    def test_stats_endpoint(self, client):
        resp = client.get("/api/stats")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["success"]
        assert "total_chunks" in data["stats"]
