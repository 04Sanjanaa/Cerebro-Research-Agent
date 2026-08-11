# Design Tradeoffs — CEREBRO Research Agent

## 1. Model Choice: Local vs. Hosted

- **Choice:** OpenAI `gpt-3.5-turbo` for synthesis, `sentence-transformers` locally for embeddings.
- **Tradeoff:**
  - **Pros:** `gpt-3.5-turbo` is highly instruction-compliant, cheap, fast, and generates well-structured markdown and inline citations. Local embeddings run completely free, fast, and do not leak user documents to external APIs.
  - **Cons:** Requires a hosted OpenAI API key for LLM synthesis. However, the backend features a robust keyword-fallback mode that handles the pipeline offline if no key is provided.

---

## 2. Retrieval Choice: Hybrid (BM25 + Dense Semantics)

- **Choice:** Combining Okapi BM25 and `all-MiniLM-L6-v2`.
- **Tradeoff:**
  - **Pros:** Semantic search handles synonyms and conceptual matches (e.g., mapping "vacation" to "annual leave"). BM25 excels at exact keyword matching (e.g., identifying policy numbers like "IS-001" or "FIN-003"). Combining them gives high precision and recall.
  - **Cons:** Indexing is slightly slower because the model must run locally. This is mitigated by using a lightweight (80MB) model which takes less than 2 seconds to embed our knowledge base.

---

## 3. Storage Choice: SQLite

- **Choice:** Standard SQLite database instead of a heavy vector database (like Pinecone or Milvus).
- **Tradeoff:**
  - **Pros:** Zero-configuration local database. The entire project runs with no external databases or Docker containers required. Fast enough for small-to-medium datasets (thousands of documents).
  - **Cons:** Vector similarity search is computed in-memory (numpy matrix multiplication) rather than indexed with HNSW. Scaling to millions of documents would require replacing this with a dedicated vector database.

---

## 4. Ingestion Choice: Chunk Size and Overlap

- **Choice:** Paragraph chunking with a target of 250 words and 50 words overlap.
- **Tradeoff:**
  - **Pros:** A 250-word chunk size fits a single topic (like a subsection of a policy) perfectly, keeping semantic similarity high. The 50-word overlap ensures that details near a cut boundary are not lost.
  - **Cons:** Smaller chunks increase the number of vector comparisons during search. This is negligible at our scale.

---

## 5. Hallucination Prevention: Semantic-Only Gate

- **Choice:** Gating answerability strictly on a raw semantic similarity threshold of `0.68`.
- **Tradeoff:**
  - **Pros:** Prevents BM25 exact term matches from forcing answers to off-topic queries (e.g. asking about "office address" shouldn't return random paragraphs just because they contain the word "office"). Highly reliable.
  - **Cons:** Strict thresholds may reject queries that contain minor typos or are highly paraphrased. This is solved by using high-quality semantic encoders.
