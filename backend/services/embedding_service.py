"""
Embedding Service — CEREBRO Research Agent
Uses sentence-transformers (all-MiniLM-L6-v2) for semantic similarity.
Falls back gracefully to TF-IDF when sentence-transformers is unavailable.
"""

import os
import math
import re
from typing import List, Dict, Any, Optional


# ── Sentence-Transformers (preferred) ─────────────────────────────────────────
try:
    from sentence_transformers import SentenceTransformer
    import numpy as np

    _ST_AVAILABLE = True
except ImportError:
    _ST_AVAILABLE = False


class EmbeddingService:
    """
    Manages document embeddings for semantic search.

    Embedding strategy:
    - Primary: sentence-transformers/all-MiniLM-L6-v2
      Fast, lightweight (80 MB), runs fully locally, no API key required.
      Produces 384-dimensional dense vectors.
    - Fallback: TF-IDF-style cosine similarity computed on-the-fly.
      No additional dependencies; purely based on term frequencies.
    """

    MODEL_NAME = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

    def __init__(self):
        self._model: Optional[Any] = None
        self._chunk_embeddings: Optional[Any] = None  # np.ndarray when ST is used
        self._chunks: List[Dict[str, Any]] = []
        self._tfidf_idf: Dict[str, float] = {}
        self._mode = "tfidf"  # updated to "semantic" if ST loads

        if _ST_AVAILABLE:
            try:
                print(f"[EmbeddingService] Loading model: {self.MODEL_NAME}")
                self._model = SentenceTransformer(self.MODEL_NAME)
                self._mode = "semantic"
                print("[EmbeddingService] Semantic mode active (sentence-transformers).")
            except Exception as e:
                print(f"[EmbeddingService] Model load failed ({e}). Falling back to TF-IDF.")
        else:
            print("[EmbeddingService] sentence-transformers not installed. Using TF-IDF fallback.")

    @property
    def mode(self) -> str:
        return self._mode

    # ── Indexing ───────────────────────────────────────────────────────────────

    def index_chunks(self, chunks: List[Dict[str, Any]]) -> None:
        """
        Build the embedding index for a list of chunks.
        Each chunk dict must have 'text' and 'id' keys.
        """
        self._chunks = chunks
        texts = [c["text"] for c in chunks]

        if self._mode == "semantic" and self._model is not None:
            print(f"[EmbeddingService] Encoding {len(texts)} chunks...")
            self._chunk_embeddings = self._model.encode(
                texts, batch_size=32, show_progress_bar=False, normalize_embeddings=True
            )
            print("[EmbeddingService] Indexing complete.")
        else:
            # Build IDF table
            self._build_idf(texts)

    def _build_idf(self, texts: List[str]) -> None:
        """Build inverse-document-frequency table for TF-IDF."""
        N = len(texts)
        df: Dict[str, int] = {}
        for text in texts:
            tokens = set(self._tokenize(text))
            for tok in tokens:
                df[tok] = df.get(tok, 0) + 1
        self._tfidf_idf = {
            tok: math.log((N + 1) / (count + 1)) + 1.0
            for tok, count in df.items()
        }

    # ── Scoring ────────────────────────────────────────────────────────────────

    def score_query(self, query: str) -> List[float]:
        """
        Return a similarity score [0,1] for each indexed chunk against the query.
        """
        if not self._chunks:
            return []

        if self._mode == "semantic" and self._model is not None:
            q_emb = self._model.encode([query], normalize_embeddings=True)
            scores = (self._chunk_embeddings @ q_emb.T).flatten().tolist()
            # Scores are already in [-1, 1]; shift to [0, 1]
            return [(s + 1.0) / 2.0 for s in scores]
        else:
            return self._tfidf_scores(query)

    def _tfidf_scores(self, query: str) -> List[float]:
        """TF-IDF cosine similarity between query and each chunk."""
        q_tokens = self._tokenize(query)
        q_vec = self._tfidf_vector(q_tokens)

        scores = []
        for chunk in self._chunks:
            d_tokens = self._tokenize(chunk["text"])
            d_vec = self._tfidf_vector(d_tokens)
            scores.append(self._cosine(q_vec, d_vec))
        return scores

    def _tfidf_vector(self, tokens: List[str]) -> Dict[str, float]:
        tf: Dict[str, float] = {}
        for tok in tokens:
            tf[tok] = tf.get(tok, 0) + 1
        total = len(tokens) or 1
        return {
            tok: (count / total) * self._tfidf_idf.get(tok, 1.0)
            for tok, count in tf.items()
        }

    @staticmethod
    def _cosine(v1: Dict[str, float], v2: Dict[str, float]) -> float:
        shared = set(v1) & set(v2)
        if not shared:
            return 0.0
        dot = sum(v1[k] * v2[k] for k in shared)
        mag1 = math.sqrt(sum(x * x for x in v1.values()))
        mag2 = math.sqrt(sum(x * x for x in v2.values()))
        if mag1 == 0 or mag2 == 0:
            return 0.0
        return dot / (mag1 * mag2)

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        return [t for t in text.split() if len(t) > 2]
