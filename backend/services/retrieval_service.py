"""
Retrieval Service — CEREBRO Research Agent
Hybrid BM25 + Semantic retrieval with configurable relevance threshold.

Scoring methodology:
  combined_score = α * semantic_score + (1 - α) * bm25_score
  Default α = 0.6 (semantic-dominant when model is available; falls back to BM25-only).

Relevance threshold: chunks scoring below MIN_SCORE are excluded from the evidence
context passed to the LLM.  This prevents hallucination from weakly-related passages.
"""

import math
import re
from typing import List, Dict, Any, Tuple

from services.embedding_service import EmbeddingService


# ── BM25 Implementation ────────────────────────────────────────────────────────

class BM25:
    """Okapi BM25 over a corpus of tokenized documents."""

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self._corpus_tokens: List[List[str]] = []
        self._idf: Dict[str, float] = {}
        self._avgdl: float = 0.0
        self._N: int = 0

    def fit(self, texts: List[str]) -> None:
        """Index a list of text strings."""
        self._corpus_tokens = [self._tokenize(t) for t in texts]
        self._N = len(self._corpus_tokens)
        self._avgdl = (
            sum(len(d) for d in self._corpus_tokens) / self._N if self._N else 1.0
        )
        # Build IDF
        df: Dict[str, int] = {}
        for doc_tokens in self._corpus_tokens:
            for tok in set(doc_tokens):
                df[tok] = df.get(tok, 0) + 1
        self._idf = {
            tok: math.log((self._N - n + 0.5) / (n + 0.5) + 1.0)
            for tok, n in df.items()
        }

    def score(self, query: str) -> List[float]:
        """Return BM25 score for every indexed document."""
        q_tokens = self._tokenize(query)
        scores = []
        for doc_tokens in self._corpus_tokens:
            dl = len(doc_tokens)
            doc_freq: Dict[str, int] = {}
            for tok in doc_tokens:
                doc_freq[tok] = doc_freq.get(tok, 0) + 1

            s = 0.0
            for tok in q_tokens:
                if tok not in self._idf:
                    continue
                tf = doc_freq.get(tok, 0)
                numerator = tf * (self.k1 + 1)
                denominator = tf + self.k1 * (1 - self.b + self.b * dl / self._avgdl)
                s += self._idf[tok] * numerator / denominator
            scores.append(s)
        return scores

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        return [t for t in text.split() if len(t) > 2]


# ── Retrieval Service ──────────────────────────────────────────────────────────

class RetrievalService:
    """
    Hybrid retrieval: BM25 keyword ranking + semantic embedding similarity.

    Configuration (via constructor or env):
        top_k      — number of chunks to return (default 5)
        min_score  — relevance threshold [0,1]; chunks below this are excluded (default 0.30)
        alpha      — weight for semantic score (default 0.6); BM25 gets (1 - alpha)
    """

    def __init__(
        self,
        embedding_service: EmbeddingService,
        top_k: int = 5,
        min_score: float = 0.30,
        alpha: float = 0.60,
        evidence_threshold: float = 0.68,
        keyword_weight: float = 0.40,
    ):
        self._emb = embedding_service
        self.top_k = top_k
        self.min_score = min_score
        self.alpha = alpha
        self.evidence_threshold = evidence_threshold
        self.keyword_weight = keyword_weight
        self._bm25 = BM25()
        self._chunks: List[Dict[str, Any]] = []
        self._indexed = False


    # ── Indexing ───────────────────────────────────────────────────────────────

    def index(self, chunks: List[Dict[str, Any]]) -> None:
        """Index chunks for retrieval."""
        self._chunks = chunks
        texts = [c["text"] for c in chunks]

        # Build BM25 index
        self._bm25.fit(texts)

        # Build semantic embeddings index
        self._emb.index_chunks(chunks)

        self._indexed = True
        print(
            f"[RetrievalService] Indexed {len(chunks)} chunks "
            f"(mode={self._emb.mode}, alpha={self.alpha}, min_score={self.min_score})"
        )

    # ── Retrieval ──────────────────────────────────────────────────────────────

    def retrieve(self, query: str) -> List[Dict[str, Any]]:
        """
        Retrieve the top-k most relevant chunks for a query.

        Returns:
            List of chunk dicts augmented with:
                semantic_score  — raw semantic similarity [0, 1]
                bm25_score      — normalized BM25 score [0, 1]
                combined_score  — weighted combination [0, 1]
                relevance_label — human-readable relevance tier
        """
        if not self._indexed or not self._chunks:
            return []

        # Semantic scores [0, 1]
        sem_scores = self._emb.score_query(query)

        # BM25 raw scores (unbounded positive float) → normalize to [0, 1]
        bm25_raw = self._bm25.score(query)
        bm25_max = max(bm25_raw) if bm25_raw else 1.0
        bm25_norm = [s / (bm25_max + 1e-9) for s in bm25_raw]

        # Combine
        results = []
        for i, chunk in enumerate(self._chunks):
            sem = sem_scores[i] if i < len(sem_scores) else 0.0
            bm25 = bm25_norm[i] if i < len(bm25_norm) else 0.0

            # If semantic mode is unavailable, fall back to BM25-only
            if self._emb.mode == "tfidf":
                combined = bm25
            else:
                combined = self.alpha * sem + self.keyword_weight * bm25

            if combined >= self.min_score:
                enriched = dict(chunk)
                enriched["semantic_score"] = round(sem, 4)
                enriched["bm25_score"] = round(bm25, 4)
                enriched["combined_score"] = round(combined, 4)
                enriched["relevance_label"] = self._relevance_label(combined)
                results.append(enriched)

        # Sort by combined score descending
        results.sort(key=lambda x: x["combined_score"], reverse=True)
        return results[: self.top_k]

    def has_sufficient_evidence(self, results: List[Dict[str, Any]]) -> bool:
        """
        Return True if ANY retrieved chunk has a high enough SEMANTIC score.

        We check the maximum semantic score across all results because:
        - BM25 may rank a chunk with lower semantic similarity first due to keyword overlap
        - A high-semantic-score chunk deeper in the list still provides valid evidence
        - Threshold determines if the evidence actually supports the query topic
        """
        if not results:
            return False
        # For semantic mode: check best semantic score across all results
        if self._emb.mode == "semantic":
            max_sem = max(r.get("semantic_score", 0.0) for r in results)
            return max_sem >= self.evidence_threshold
        # For TF-IDF fallback: gate on top combined score
        return results[0]["combined_score"] >= (self.min_score + 0.15)


    # ── Helpers ────────────────────────────────────────────────────────────────

    @staticmethod
    def _relevance_label(score: float) -> str:
        if score >= 0.75:
            return "Very High"
        elif score >= 0.55:
            return "High"
        elif score >= 0.40:
            return "Medium"
        else:
            return "Low"
