"""
CEREBRO — Research Agent with Citations
Main Flask application entry point.
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
import json
import os
import uuid
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ── Service Imports ────────────────────────────────────────────────────────────
from services.document_service import DocumentService
from services.embedding_service import EmbeddingService
from services.retrieval_service import RetrievalService
from services.citation_service import CitationService
from services.llm_service import LLMService
from services.calendar_service import CalendarService

# ── Preserve legacy services ──────────────────────────────────────────────────
from services.db_service import DBService
from services.logger_service import LoggerService

# ── App Bootstrap ──────────────────────────────────────────────────────────────
app = Flask(__name__)
CORS(app)

# Paths
BASE_DIR = Path(__file__).parent
KB_DIR = str(BASE_DIR.parent / "data" / "knowledge_base")
DB_PATH = str(BASE_DIR / "data" / "kb_agent.db")
os.makedirs(str(BASE_DIR / "data"), exist_ok=True)
os.makedirs(str(BASE_DIR.parent / "logs"), exist_ok=True)

# ── Service Initialization ─────────────────────────────────────────────────────
from config import get_config
config_obj = get_config()
print("[CEREBRO] Initializing services...")

document_service = DocumentService(knowledge_base_dir=KB_DIR)
embedding_service = EmbeddingService()
retrieval_service = RetrievalService(
    embedding_service=embedding_service,
    top_k=config_obj.TOP_K,
    min_score=config_obj.RETRIEVAL_MIN_SCORE,
    alpha=config_obj.SEMANTIC_WEIGHT,
    evidence_threshold=config_obj.EVIDENCE_THRESHOLD,
    keyword_weight=config_obj.KEYWORD_WEIGHT,
)
citation_service = CitationService()
llm_service = LLMService(
    model=os.getenv("LLM_MODEL", "gpt-3.5-turbo")
)
calendar_service = CalendarService()

db_service = DBService(db_path=DB_PATH)
logger_service = LoggerService(db_service=db_service)


def _build_index():
    """Load documents and build the retrieval index."""
    try:
        chunks = document_service.load_all(chunk_size=250, overlap=50)
        if chunks:
            retrieval_service.index(chunks)
            print(f"[CEREBRO] Index ready: {len(chunks)} chunks from {KB_DIR}")
        else:
            print("[CEREBRO] WARNING: No chunks loaded from knowledge base.")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"[CEREBRO] Index build failed: {e}")


# Build index at startup
_build_index()
print("[CEREBRO] Backend ready.")


# ── API Routes ─────────────────────────────────────────────────────────────────

@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    chunks = document_service.get_chunks()
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "chunks_indexed": len(chunks),
        "retrieval_mode": embedding_service.mode,
        "llm_enabled": llm_service.enabled,
    }), 200


@app.route("/api/documents", methods=["GET"])
def get_documents():
    """Return summary of indexed documents."""
    try:
        doc_list = document_service.get_document_list()
        chunks = document_service.get_chunks()
        return jsonify({
            "success": True,
            "count": len(doc_list),
            "total_chunks": len(chunks),
            "documents": doc_list,
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/reload", methods=["POST"])
def reload_documents():
    """Force reload of knowledge base documents."""
    try:
        chunks = document_service.reload()
        if chunks:
            retrieval_service.index(chunks)
        return jsonify({
            "success": True,
            "message": f"Reloaded {len(chunks)} chunks from knowledge base.",
            "chunks": len(chunks),
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/research", methods=["POST"])
def research():
    """
    Main research endpoint.
    Accepts a question, retrieves evidence, and returns a cited answer.

    Request body:
        { "query": "What is the annual leave policy?" }

    Response:
        {
          "success": true,
          "query": "...",
          "answer": "Employees are entitled to 20 days... [1]",
          "citations": [...],
          "retrieval_info": { "chunks_retrieved": 3, "top_score": 0.82, ... },
          "insufficient_evidence": false,
          "timestamp": "..."
        }
    """
    try:
        data = request.get_json(silent=True) or {}
        query = (data.get("query") or "").strip()

        if not query:
            return jsonify({"success": False, "error": "Query cannot be empty"}), 400

        # ── Step 1: Retrieve evidence ──────────────────────────────────────────
        evidence = retrieval_service.retrieve(query)
        has_evidence = retrieval_service.has_sufficient_evidence(evidence)

        # ── Step 2: Build citations and context ───────────────────────────────
        citations, evidence_context = citation_service.build(evidence)

        # ── Step 3: Generate grounded answer ──────────────────────────────────
        llm_result = llm_service.generate_grounded_answer(
            query=query,
            evidence_context=evidence_context,
            citations=citations,
            has_evidence=has_evidence,
        )

        answer = llm_result.get("response", "")
        insufficient = llm_result.get("insufficient_evidence", False)

        # ── Step 3.5: Citation Validation ──────────────────────────────────────
        grounded = not insufficient
        if not insufficient and citations:
            validation = citation_service.validate_citations(
                answer=answer,
                citations=citations,
                has_evidence=has_evidence
            )
            if not validation["valid"]:
                # Try safely regenerating once with a stricter prompt if LLM is enabled
                if llm_service.enabled and llm_service.client:
                    stricter_context = (
                        evidence_context + 
                        "\n\nWARNING: Your previous answer was rejected because you either included invalid citation numbers "
                        "or forgot to cite your claims altogether. You MUST cite every claim using ONLY the numbers: " + 
                        ", ".join(f"[{c['id']}]" for c in citations) + "."
                    )
                    llm_result = llm_service.generate_grounded_answer(
                        query=query,
                        evidence_context=stricter_context,
                        citations=citations,
                        has_evidence=has_evidence,
                    )
                    answer = llm_result.get("response", "")
                    validation = citation_service.validate_citations(
                        answer=answer,
                        citations=citations,
                        has_evidence=has_evidence
                    )
                
                # Check validation result again
                if not validation["valid"]:
                    grounded = False
                    answer = f"Grounded citation error: {validation['error_message']} [Citation validation failed]"

        # ── Step 4: Log ───────────────────────────────────────────────────────
        sources_for_log = [
            {"title": c["source"], "section": c["section"]}
            for c in citations
        ]
        logger_service.log_query(query, not insufficient and grounded, sources_for_log)

        # ── Step 5: Build response ────────────────────────────────────────────
        retrieval_info = {
            "chunks_retrieved": len(evidence),
            "sources_used": len(set(c["source"] for c in citations)),
            "top_score": evidence[0]["combined_score"] if evidence else 0.0,
            "retrieval_mode": embedding_service.mode,
            "min_threshold": retrieval_service.min_score,
        }

        return jsonify({
            "success": True,
            "query": query,
            "answer": answer,
            "citations": citations,
            "retrieval_info": retrieval_info,
            "insufficient_evidence": insufficient,
            "grounded": grounded,
            "model_used": llm_result.get("model", "unknown"),
            "tokens_used": llm_result.get("tokens_used", 0),
            "timestamp": datetime.now().isoformat(),
        }), 200

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/search", methods=["POST"])
def search():
    """Raw retrieval endpoint — returns ranked chunks without LLM synthesis."""
    try:
        data = request.get_json(silent=True) or {}
        query = (data.get("query") or "").strip()
        if not query:
            return jsonify({"success": False, "error": "Query cannot be empty"}), 400

        results = retrieval_service.retrieve(query)
        return jsonify({
            "success": True,
            "query": query,
            "results": results,
            "count": len(results),
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/logs", methods=["GET"])
def get_logs():
    """Return query logs."""
    try:
        logs = logger_service.get_logs()
        return jsonify({"success": True, "count": len(logs), "logs": logs}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/stats", methods=["GET"])
def get_stats():
    """Return system statistics."""
    try:
        logs = logger_service.get_logs()
        answered = sum(1 for l in logs if l.get("answered"))
        chunks = document_service.get_chunks()
        docs = document_service.get_document_list()
        return jsonify({
            "success": True,
            "stats": {
                "total_documents": len(docs),
                "total_chunks": len(chunks),
                "total_queries": len(logs),
                "answered_queries": answered,
                "unanswered_queries": len(logs) - answered,
                "response_rate": f"{(answered/len(logs)*100):.1f}%" if logs else "0%",
                "retrieval_mode": embedding_service.mode,
                "llm_enabled": llm_service.enabled,
                "llm_model": llm_service.model,
                "min_score_threshold": retrieval_service.min_score,
            },
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/clear-logs", methods=["POST"])
def clear_logs():
    """Clear all query logs."""
    try:
        logger_service.clear_logs()
        return jsonify({"success": True, "message": "Logs cleared."}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/events", methods=["GET"])
def get_events():
    """Get upcoming company events"""
    try:
        result = calendar_service.get_upcoming_events()
        return jsonify({
            "success": result["success"],
            "events": result.get("events", []),
            "count": result.get("count", 0)
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "events": []
        }), 500


@app.route("/api/holidays", methods=["GET"])
def get_holidays():
    """Get company holidays"""
    try:
        result = calendar_service.get_company_holidays()
        return jsonify({
            "success": result["success"],
            "holidays": result.get("holidays", []),
            "year": result.get("year")
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "holidays": []
        }), 500


@app.route("/api/voice", methods=["POST"])
def handle_voice():
    """Handle voice input transcription"""
    try:
        data = request.json or {}
        transcribed_text = data.get("text", "")
        if not transcribed_text:
            return jsonify({"success": False, "error": "No text provided"}), 400
        return jsonify({
            "success": True,
            "transcribed": transcribed_text,
            "message": "Voice input received. Processing as regular query."
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# ── Legacy compatibility route (maps /api/query → /api/research) ───────────────
@app.route("/api/query", methods=["POST"])
def handle_query():
    """Legacy compatibility endpoint — delegates to /api/research."""
    return research()


# ── Static file serving ────────────────────────────────────────────────────────
STATIC_DIR = str(BASE_DIR.parent / "frontend" / "build")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    """Serve React build files."""
    if path and (Path(STATIC_DIR) / path).exists():
        return send_from_directory(STATIC_DIR, path)
    index_path = Path(STATIC_DIR) / "index.html"
    if index_path.exists():
        return send_from_directory(STATIC_DIR, "index.html")
    return jsonify({
        "message": "CEREBRO Research Agent API is running.",
        "docs": "See README.md for frontend setup.",
        "endpoints": ["/api/health", "/api/research", "/api/documents", "/api/stats"],
    }), 200


# ── Error Handlers ─────────────────────────────────────────────────────────────
@app.errorhandler(404)
def not_found(error):
    return jsonify({"success": False, "error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"success": False, "error": "Internal server error"}), 500


if __name__ == "__main__":
    host = os.getenv("FLASK_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "true").lower() == "true"
    app.run(debug=debug, host=host, port=port)
