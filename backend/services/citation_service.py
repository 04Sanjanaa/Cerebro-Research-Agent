"""
Citation Service - CEREBRO Research Agent
Maps retrieved evidence chunks to numbered citation IDs and formats them for display.
"""

from typing import List, Dict, Any, Tuple


class CitationService:
    """
    Assigns [1], [2], ... citation IDs to retrieved evidence chunks
    and builds structured citation objects for the API response.

    Usage:
        service = CitationService()
        citations, context = service.build(evidence_chunks)
        # Pass context to LLM; LLM response will contain [1], [2], ...
    """

    def build(
        self, evidence_chunks: List[Dict[str, Any]]
    ) -> Tuple[List[Dict[str, Any]], str]:
        """
        Build citation list and formatted evidence context string.

        Args:
            evidence_chunks: Ranked list of chunk dicts from RetrievalService.

        Returns:
            (citations, context_string)
            citations - list of citation dicts with id, label, source, section, etc.
            context_string - formatted evidence block to embed in the LLM prompt
        """
        citations = []
        context_parts = []

        for idx, chunk in enumerate(evidence_chunks, start=1):
            meta = chunk.get("metadata", {})
            source = meta.get("source", "Unknown Source")
            section = meta.get("section", "")
            chunk_id = chunk.get("id", f"chunk_{idx}")
            text = chunk.get("text", "")
            score = chunk.get("combined_score", 0.0)
            relevance = chunk.get("relevance_label", "")

            # Trim passage for display (400 chars max)
            passage_preview = text[:400].strip()
            if len(text) > 400:
                passage_preview += "..."

            citation = {
                "id": idx,
                "label": f"[{idx}]",
                "source": source,
                "section": section,
                "chunk_id": chunk_id,
                "passage": passage_preview,
                "full_text": text,
                "score": score,
                "relevance": relevance,
            }
            citations.append(citation)

            # Build context block for LLM
            source_header = f"[{idx}] Source: {source}"
            if section:
                source_header += f" | Section: {section}"
            context_parts.append(f"{source_header}\n{text}")

        context_string = "\n\n---\n\n".join(context_parts)
        return citations, context_string

    def format_citation_instructions(self) -> str:
        """
        Return the citation instruction fragment to embed in the LLM system prompt.
        """
        return (
            "When you use information from a source, you MUST cite it inline using "
            "the citation number in square brackets, e.g. [1] or [2]. "
            "Place the citation immediately after the relevant sentence or clause. "
            "If multiple sources support the same statement, cite all of them, e.g. [1][2]. "
            "Do NOT cite a source that does not actually support the claim."
        )
