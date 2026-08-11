# Testing Guide & Results — CEREBRO Research Agent

This document explains the testing strategy, frameworks, and results for the CEREBRO Research Agent.

---

## 1. Testing Framework

We use **`pytest`** for unit testing and integration testing of the backend services, retrieval pipeline, API endpoints, and hallucination prevention gates.

**Dependencies:**
- `pytest` (v9.1.1+)
- `pytest-cov` (v4.0.0+) for coverage tracking

---

## 2. Test Suite Architecture (`tests/test_cerebro.py`)

The test suite contains **21 robust test cases** structured into five major category blocks:

### A. Document Ingestion & Chunking (`TestDocumentIngestion`)
- **`test_chunk_text_splits_correctly`**: Verifies that large documents are split into overlapping passages according to `chunk_size` and `overlap` configurations.
- **`test_chunk_preserves_metadata`**: Ensures metadata fields (e.g., `source`, `doc_id`, `chunk_index`) are preserved in every chunk.
- **`test_load_txt_file`**: Verifies that the loader reads plain-text files and extracts coherent contents.
- **`test_empty_directory_returns_no_chunks`**: Validates edge-case behavior when indexing directories with no supported documents.

### B. Hybrid Retrieval & Ranking (`TestRetrieval`)
- **`test_leave_query_ranks_leave_chunk_first`**: Verifies that leave-related queries rank the leave policy passage first.
- **`test_password_query_ranks_password_chunk_first`**: Verifies that security-related queries rank the password complexity requirements passage first.
- **`test_remote_work_query`**: Ensures queries regarding remote eligibility return remote work passages.
- **`test_results_sorted_by_score`**: Validates that candidate chunks are strictly returned in descending order of combined score.
- **`test_result_contains_required_fields`**: Confirms retrieved chunks are enriched with scores (semantic, BM25, combined) and relevance labels.
- **`test_unrelated_query_below_threshold`**: Tests that completely unrelated queries (e.g., stock price) return candidate scores below the sufficient evidence gate.

### C. Citation Generation (`TestCitations`)
- **`test_build_assigns_sequential_ids`**: Ensures citation IDs are sequential 1-indexed integers matching the retrieved passage rank.
- **`test_context_contains_citation_headers`**: Verifies the formatting of the evidence context block sent to the LLM.
- **`test_citation_has_source_and_section`**: Confirms that citation tags map directly back to source documents, page numbers (if available), and section headings.

### D. Grounding & Hallucination Prevention (`TestGrounding`)
- **`test_insufficient_evidence_response`**: Confirms that when no evidence meets the threshold (`has_evidence=False`), the LLM/fallback returns a clean refusal rather than generating a response.
- **`test_keyword_fallback_includes_sources`**: Checks the keyword-fallback path (used when no API key is provided) to ensure it labels itself as an evidence-only fallback and lists sources.

### E. Flask REST API Endpoints (`TestAPI`)
- **`test_health_endpoint`**: Verifies `GET /api/health` returns status, retrieval mode, and count.
- **`test_documents_endpoint`**: Verifies `GET /api/documents` returns the summarized list of indexed documents.
- **`test_stats_endpoint`**: Verifies `GET /api/stats` returns system statistics.
- **`test_research_endpoint_returns_answer`**: Sends queries to `POST /api/research` and checks the response schema (answer, citations, retrieval_info).
- **`test_research_endpoint_insufficient`**: Verifies that out-of-scope queries return `insufficient_evidence: true` in the JSON response.
- **`test_research_rejects_empty_query`**: Ensures bad requests return a `400` status.

---

## 3. Running the Test Suite

1. Activate your virtual environment and navigate to the backend folder:
   ```bash
   cd backend
   .\venv\Scripts\activate   # Windows
   # or: source venv/bin/activate  # macOS/Linux
   ```
2. Run pytest:
   ```bash
   pytest ../tests/test_cerebro.py -v
   ```

---

## 4. Test Verification Results

All 21 test cases passed successfully in a fresh environment:

```text
============================= test session starts =============================
platform win32 -- Python 3.12.6, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\sanja\OneDrive\Desktop\Cerebro\CEREBRO-Research-Agent
collected 21 items

..\tests\test_cerebro.py::TestRetrieval::test_leave_query_ranks_leave_chunk_first PASSED
..\tests\test_cerebro.py::TestRetrieval::test_password_query_ranks_password_chunk_first PASSED
..\tests\test_cerebro.py::TestRetrieval::test_unrelated_query_below_threshold PASSED
..\tests\test_cerebro.py::TestRetrieval::test_results_sorted_by_score PASSED
..\tests\test_cerebro.py::TestRetrieval::test_result_contains_required_fields PASSED
..\tests\test_cerebro.py::TestRetrieval::test_remote_work_query PASSED
..\tests\test_Citations::test_build_assigns_sequential_ids PASSED
..\tests\test_Citations::test_context_contains_citation_headers PASSED
..\tests\test_Citations::test_citation_has_source_and_section PASSED
..\tests\test_Grounding::test_insufficient_evidence_response PASSED
..\tests\test_Grounding::test_keyword_fallback_includes_sources PASSED
..\tests\test_DocumentIngestion::test_chunk_text_splits_correctly PASSED
..\tests\test_DocumentIngestion::test_chunk_preserves_metadata PASSED
..\tests\test_DocumentIngestion::test_load_txt_file PASSED
..\tests\test_DocumentIngestion::test_empty_directory_returns_no_chunks PASSED
..\tests\test_API::test_health_endpoint PASSED
..\tests\test_API::test_research_endpoint_returns_answer PASSED
..\tests\test_API::test_research_endpoint_insufficient PASSED
..\tests\test_API::test_research_rejects_empty_query PASSED
..\tests\test_API::test_documents_endpoint PASSED
..\tests\test_API::test_stats_endpoint PASSED

======================== 21 passed in 88.87s (0:01:28) ========================
```

---

## 5. UI Verification Results

Manual frontend verification confirms that:
- **Answers** are displayed clearly in Markdown format.
- **Inline Citation numbers** (e.g., `[1]`) are highlighted.
- **Clicking a source card** collapses or expands the exact supporting chunk text.
- **Insufficient Evidence state** displays a custom UI block containing a red warning icon indicating the query was unanswerable with the current knowledge base.
