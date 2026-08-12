# CEREBRO — Research Agent with Citations

Intelligent RAG (Retrieval-Augmented Generation) Research Agent with a React frontend and Flask backend.

CEREBRO retrieves evidence passages from a localized knowledge base, applies relevance filtering, and synthesizes answers using strictly retrieved evidence, mapping inline citation markers directly to the source passages.

---

## Overview

CEREBRO is a specialized cited research assistant designed to navigate corporate or domain-specific documents, extract relevant passages, rank them using a hybrid search mechanism, filter out low-confidence evidence, and generate synthetically grounded answers. It is built to operate fully locally if necessary, with a structured fallback mode when OpenAI API keys are not supplied.

---

## Problem

Generic search engines retrieve documents but require users to read and synthesize answers. Standard LLMs synthesize answers but suffer from hallucinations, fabrication, and lack of auditability. CEREBRO resolves this by implementing a closed-loop Retrieval-Augmented Generation pipeline where every claim must correspond to a verified, retrieved source chunk that is easily auditable by the user via interactive citation cards in the frontend.

---

## Features

- **Document Ingestion:** Processes `.txt`, `.pdf`, and `.docx` files dynamically.
- **Hybrid Retrieval:** Blends semantic context with exact keyword indices.
- **Evidence Threshold Gate:** Rejects off-topic queries to prevent hallucination.
- **Interactive Passage Citations:** Features clickable citations displaying source, section, relevance, and exact chunk passage in the UI.
- **Local Fallback Mode:** Pre-configured to extract key evidence statements locally when no OpenAI key is configured.
- **Upcoming Events & Voice Integrations:** Preserves original scheduling, calendar, and voice metrics features.

---

## Architecture

```
User Query
    │
    ▼
Query Processor
    │
    ▼
Retriever (Hybrid BM25 + Semantic)
    │
    ▼
Evidence Filter (EVIDENCE_THRESHOLD Gate)
    │
    ├─► [Below Threshold] ──► Return "Insufficient Evidence" Refusal
    │
    └─► [Above Threshold] ──► Grounded LLM Synthesis ──► Cited Answer + Supporting Evidence
```

For more details, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

---

## Tech Stack

- **Backend:** Flask REST API (Python 3.12+), SQLite
- **Semantic Model:** Local `sentence-transformers/all-MiniLM-L6-v2` dense vectors
- **Keyword Search:** Custom Okapi BM25 engine
- **LLM Synthesis:** OpenAI GPT-3.5-turbo
- **Frontend:** React 18 with hooks, Lucide icons, and modern responsive CSS

---

## Project Structure

```
CEREBRO-Research-Agent/
│
├── backend/
│   ├── app.py                 # Flask REST API entry point
│   ├── config.py              # Configuration management
│   ├── models/
│   │   ├── __init__.py
│   │   └── embeddings.py      # Legacy embedding utilities (preserved)
│   └── services/
│       ├── __init__.py
│       ├── document_service.py # Doc parsing, loading, chunking
│       ├── embedding_service.py # Local ST embeddings + TF-IDF fallback
│       ├── retrieval_service.py # Hybrid BM25 + Semantic search & gating
│       ├── llm_service.py     # Grounded OpenAI synthesis & local fallback
│       ├── citation_service.py # Citation mapping and context formatting
│       ├── db_service.py      # SQLite database service
│       └── calendar_service.py # Google calendar service (preserved)
│
├── frontend/                  # React Frontend Single Page App
│
├── data/
│   └── knowledge_base/        # Store fictional documents here (.txt, .pdf, .docx)
│
├── docs/                      # Architectural & design documentation
│   ├── ARCHITECTURE.md
│   ├── RETRIEVAL_METHOD.md
│   ├── TRADEOFFS.md
│   └── TESTING.md
│
├── examples/                  # Question lists and real cited answers
│   ├── questions.json
│   ├── sample_output.md
│   └── cited_answers.md
│
├── tests/                     # 26 automated tests
│   └── test_cerebro.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation

### Windows

From the REPOSITORY ROOT:

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Then:

```bash
cd backend
python app.py
```

### macOS/Linux

From the REPOSITORY ROOT:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Then:

```bash
cd backend
python app.py
```

---

## Environment Variables

Edit the created `.env` file with the following variables:

```ini
# Flask Setup
FLASK_ENV=development
FLASK_DEBUG=true
FLASK_HOST=0.0.0.0
FLASK_PORT=5000

# API Endpoint URL for Frontend
REACT_APP_API_URL=http://localhost:5000

# OpenAI Integration (Optional)
OPENAI_API_KEY=your-openai-api-key-here
LLM_MODEL=gpt-3.5-turbo

# Retrieval Configurations
TOP_K=5
RETRIEVAL_MIN_SCORE=0.30
EVIDENCE_THRESHOLD=0.68
SEMANTIC_WEIGHT=0.60
KEYWORD_WEIGHT=0.40
EMBEDDING_MODEL=all-MiniLM-L6-v2

# Persistence & Logs
LOG_LEVEL=INFO
LOG_FILE=./logs/cerebro.log
SECRET_KEY=dev-secret-key
```

---

## Running the Backend

With the virtual environment activated, change directory to `backend` and run the app:
```bash
cd backend
python app.py
```
Backend will start on `http://localhost:5000`.

---

## Running the Frontend

1. Navigate to the `frontend` directory in a new terminal:
   ```bash
   cd frontend
   ```
2. Install package dependencies:
   ```bash
   npm install
   ```
3. Start the dev server:
   ```bash
   npm start
   ```
The frontend opens on `http://localhost:3000`.

---

## Running the Real LLM Synthesis

To run the system in LLM Synthesis Mode instead of the Local Fallback Mode:

1. Open the `.env` file at the repository root (created from `.env.example`).
2. Set your OpenAI API key:
   ```ini
   OPENAI_API_KEY=sk-proj-yourActualKeyHere...
   ```
3. Restart the backend server:
   ```bash
   python app.py
   ```
4. Once restarted, all research queries will be answered using the actual LLM with strict grounding constraints.
5. To regenerate the example outputs using your key:
   ```bash
   python examples/generate_answers.py
   ```

---

## Adding Knowledge Base Documents

Simply place your `.txt`, `.pdf`, or `.docx` documents in:
`data/knowledge_base/`

To index the new documents dynamically, click the **Reload Knowledge Base** button in the **Documents** tab of the React UI or trigger a reload via:
`POST http://localhost:5000/api/reload`

---

## How Retrieval Works

Retrieval in CEREBRO operates in two phases:
1. **Indexing:** At startup, files in the knowledge base are parsed, split into paragraph chunks, indexed into a local BM25 keyword search cache, and mapped to dense vector embeddings.
2. **Retrieval:** For any query, candidates are retrieved, combined scores are calculated, and weak candidates are filtered before the final evidence gate evaluates topical relevance.

For more details, see [docs/RETRIEVAL_METHOD.md](docs/RETRIEVAL_METHOD.md).

---

## Hybrid Retrieval Method

Scores from keyword search (BM25) and vector semantics are combined using:
`combined_score = SEMANTIC_WEIGHT * semantic_score + KEYWORD_WEIGHT * bm25_norm`

Semantic weights are set to `0.60` and keyword weights to `0.40` by default. This ensures conceptual semantic matching takes precedence while preserving exact terminology matches.

---

## Chunking Strategy

Documents are chunked using paragraph-boundary division:
- Target chunk size: **250 words**
- Overlap size: **50 words**
- Splitting on double newlines ensures that natural context structures remain intact.

---

## Relevance Scoring

BM25 scores are normalized by dividing by the highest BM25 score obtained for the query. Semantic similarity scores are computed using the cosine similarity of the query embedding against the chunk embedding, shifted to a range of `[0.0, 1.0]`. Chunks scoring below `RETRIEVAL_MIN_SCORE` (default `0.30`) are excluded.

---

## Evidence Threshold

The evidence gate evaluates the maximum raw semantic similarity score across all candidate chunks:
- If the maximum raw semantic similarity is below `EVIDENCE_THRESHOLD` (default `0.68`), the query is flagged as unanswerable.
- This prevents the LLM from synthesizing answers based on weakly related passages that happen to share minor keywords.

---

## Grounded Answer Generation

The CEREBRO backend supports two modes of answer generation:

### 1. LLM Synthesis Mode (Production / Active RAG)
- **Requires:** `OPENAI_API_KEY` configured in `.env`.
- **Process:** When the evidence threshold is passed, the LLM (`gpt-3.5-turbo`) is supplied with:
  1. A strict system instruction set forbidding outside world knowledge.
  2. The ordered list of verified evidence context paragraphs.
  3. Strict instructions to add sequential inline citation tags (e.g. `[1]`, `[2]`).
- **Settings:** The temperature is set to `0.1` to force factual compliance.

### 2. Local Evidence-Only Fallback Mode (Offline / Sandbox)
- **Requires:** Works without an API key (automatically activated if `OPENAI_API_KEY` is empty).
- **Process:** Acts as an evidence-only fallback. Rather than using an LLM to synthesize a paragraph, it displays the key statements directly from the top retrieved passages next to their citation numbers.
- **Auditability:** It clearly informs the user that LLM synthesis is inactive and presents the raw evidence.


---

## Citation Generation

- Citation IDs (`[1]`, `[2]`, ...) correspond directly to the ranked indices of retrieved passages.
- In fallback mode, the response displays these citations alongside the parsed source, section, and text excerpt.
- In the UI, the citation tags are clickable, allowing the user to reveal the supporting passage snippet.

---

## Hallucination Prevention

Hallucinations are blocked at two levels:
1. **Retrieval Gate:** Unrelated questions are filtered out by the `EVIDENCE_THRESHOLD` before reaching the model.
2. **System Prompting:** The prompt forbids the LLM from inventing policies, names, or utilizing its own general knowledge.

---

## Example Questions

Our sample questions include:
- **Direct retrieval:** *What is the annual leave entitlement?*
- **Multi-passage:** *What are the main requirements for working remotely?*
- **Multi-document:** *How do the leave and remote work policies relate to each other?*
- **Unanswerable:** *Who is the company's CEO?*

---

## Sample Outputs

Real outputs generated by querying the actual running system are saved in [examples/cited_answers.md](examples/cited_answers.md).

---

## Handling Unknown Questions

For queries with no relevant passages matching `EVIDENCE_THRESHOLD`, the agent refuses to answer, returning:
> "I couldn't find enough information in the provided knowledge-base sources to answer this question reliably."

---

## Testing

Run unit tests, API tests, and ingestion checks with:
```bash
pytest tests/ -v
```
All **26 test cases** pass successfully. For detailed descriptions of the tests, see [docs/TESTING.md](docs/TESTING.md).

---

## Tradeoffs

A detailed outline of system design tradeoffs (local vs hosted, hybrid vs semantic, SQLite vs vector DBs) is documented in [docs/TRADEOFFS.md](docs/TRADEOFFS.md).

---

## Limitations

1. **Context Window Size:** Serving large numbers of retrieved chunks can consume tokens.
2. **Local CPU Overhead:** Embeddings are generated locally which can create minor latency on lower-end CPUs.
3. **Keyword Fallback:** Without an OpenAI API key, the system falls back to evidence-only extraction.

---

## Future Improvements

- Incorporate local cited LLMs (such as Llama 3 or Mistral) for a fully private RAG pipeline.
- Implement hierarchical vector indexing (HNSW) to support millions of document chunks.
- Add support for indexing Google Drive, Slack, and Notion spaces directly.

---

## Challenge Requirements Checklist

- [x] Question set (`examples/questions.json`)
- [x] Source documents (`data/knowledge_base/`)
- [x] Cited answers (`examples/cited_answers.md`)
- [x] Retrieval method documentation (`docs/RETRIEVAL_METHOD.md`)
- [x] Design Tradeoffs (`docs/TRADEOFFS.md`)
- [x] Architecture diagrams (`docs/ARCHITECTURE.md`)
- [x] 26 automated tests (`tests/test_cerebro.py`)
- [x] Grounded cited answering & no-answer refusal

