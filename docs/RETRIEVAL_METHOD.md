# Retrieval Method — CEREBRO Research Agent

## Overview

CEREBRO uses a **Hybrid BM25 + Semantic Retrieval** approach that combines:
1. **BM25** (keyword-based, exact term matching)
2. **Sentence-Transformers** (semantic similarity, `all-MiniLM-L6-v2`)

Combined score: `combined = 0.6 * semantic + 0.4 * bm25_normalized`

---

## Document Chunking

**Method:** Paragraph-boundary chunking with word overlap.

- Split on double-newline paragraph boundaries
- Target chunk size: **250 words**
- Overlap between consecutive chunks: **50 words** (prevents information loss at boundaries)
- Each chunk retains:
  - `doc_id` — document identifier
  - `source` — filename
  - `section` — extracted section heading
  - `chunk_index` — position in document

**Why paragraphs?** Paragraph boundaries respect natural information units. A semantic embedding of a coherent paragraph is more meaningful than an arbitrary character cut.

---

## Embeddings

**Model:** `sentence-transformers/all-MiniLM-L6-v2`

- 384-dimensional dense vectors
- ~80 MB download, runs fully locally (no API key required)
- Trained on 1B+ sentence pairs
- Produces normalized embeddings suitable for cosine similarity

**Fallback:** TF-IDF cosine similarity (if sentence-transformers unavailable)

---

## BM25

Okapi BM25 parameters:
- `k1 = 1.5` (term frequency saturation)
- `b = 0.75` (document length normalization)

BM25 raw scores are normalized to [0,1] by dividing by the maximum score in each query.

---

## Relevance Scoring

```
semantic_score = cosine_similarity(query_embedding, chunk_embedding)
                 shifted to [0,1]: (raw_cosine + 1) / 2

bm25_norm      = bm25_raw_score / max(bm25_raw_scores_for_query)

combined_score = 0.6 * semantic_score + 0.4 * bm25_norm
```

**Rationale for 0.6/0.4 split:** Semantic similarity captures intent better than exact keyword matching, especially for paraphrased questions. BM25 provides exact-term recall that the embedding model may miss for rare domain terms.

---

## Relevance Threshold

**Retrieval threshold (min_score):** `0.30`
- Chunks with `combined_score < 0.30` are excluded from retrieval results.

**Evidence gate (EVIDENCE_SEMANTIC_THRESHOLD):** `0.68`
- The maximum `semantic_score` across all retrieved chunks must exceed 0.68 for the query to be considered "answerable."
- This gate uses semantic score (not combined) to prevent BM25's exact-term boost from inflating scores on off-topic queries containing common words like "company."

**Empirical calibration:**
- Relevant queries (e.g., leave entitlement): max semantic ≈ 0.78–0.89
- Borderline queries (e.g., "company revenue"): max semantic ≈ 0.65
- Off-topic queries (e.g., "stock price"): max semantic ≈ 0.54–0.60

---

## Top-K

Default: `top_k = 5` chunks per query.

5 chunks provides enough evidence context for multi-source synthesis without exceeding LLM context limits.

---

## Citation Mapping

1. Retrieved chunks are ranked by `combined_score`.
2. Citation IDs [1], [2], ... are assigned in rank order.
3. The LLM is instructed to cite each claim inline using these IDs.
4. The frontend maps citation IDs back to the original chunk metadata for display.

---

## Known Failure Cases

1. **Short documents / sparse chunks:** Very short knowledge-base files may not chunk into enough passages.
2. **Highly technical abbreviations:** BM25 handles abbreviations but semantics may miss them.
3. **Multi-hop reasoning:** Questions requiring combining information from 3+ separate chunks may produce lower-quality synthesis.
4. **Threshold calibration:** The 0.68 evidence threshold was calibrated for the provided sample KB. Different corpora may require retuning.
