# CEREBRO — Research Agent with Citations

Intelligent RAG (Retrieval-Augmented Generation) Research Agent with React frontend and Flask backend.

CEREBRO retrieves evidence passages from a localized knowledge base, applies relevance filtering, and synthesizes answers using strictly retrieved evidence, mapping inline citation markers directly to the source passage.

---

## 1. Overview

CEREBRO operates as a cited research agent. Given a research question, it reads local documents, extracts relevant passages, ranks them using a hybrid algorithm, applies strict relevance gating to prevent hallucinations on off-topic questions, and synthesizes a grounded answer with interactive, clickable sources.

---

## 2. Features

- **Ingestion & Chunking:** Processes `.txt`, `.pdf`, and `.docx` files, splitting them on paragraph boundaries with overlap.
- **Hybrid Retrieval:** BM25 term weighting + semantic similarity (`all-MiniLM-L6-v2` dense vectors).
- **Evidence Gate:** Strictly filters out low-confidence matches to prevent LLM hallucinations.
- **Grounded Answering:** Synthesizes answers using *only* the retrieved evidence.
- **Citation System:** Generates numbered citation tokens `[1]`, `[2]` inline, linking them directly to expandable source passages in the UI.
- **SQLite Persistence:** Logs all queries, status (answered/unanswered), and source metadata.
- **Keyword Fallback:** Fully operational pipeline even without an OpenAI API key configured.

---

## 3. Architecture

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
Evidence Filter (Threshold Gate: 0.68)
    │
    ├─► [Below Threshold] ──► Return "Insufficient Evidence"
    │
    └─► [Above Threshold] ──► Grounded LLM Synthesis ──► Cited Answer + Clickable Sources
```

---

## 4. Tech Stack

- **Backend:** Flask REST API (Python 3.12+), SQLite
- **Semantic Model:** Local `sentence-transformers/all-MiniLM-L6-v2` (runs locally, 80MB, no API key required)
- **Keyword Search:** Custom Okapi BM25 engine
- **LLM Synthesis:** OpenAI GPT-3.5-turbo (or custom OpenAI-compatible models)
- **Frontend:** React 18 with hooks, CSS grid/flexbox responsive dark-mode UI, Lucide icons

---

## 5. Installation

### Prerequisites
- Python 3.12+
- Node.js 18+

### Backend Setup
1. Open a terminal in the root directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy the environment template and set up your variables:
   ```bash
   cp .env.example .env
   ```
   *(Add your `OPENAI_API_KEY` to `.env` to enable GPT-based cited synthesis).*

### Frontend Setup
1. Open another terminal in the root directory:
   ```bash
   cd frontend
   ```
2. Install package dependencies:
   ```bash
   npm install
   ```

---

## 6. Running the Application

### Running the Backend
From the `backend` folder:
```bash
python app.py
```
The backend server runs on `http://localhost:5000`.

### Running the Frontend
From the `frontend` folder:
```bash
npm start
```
The React development server opens on `http://localhost:3000`.

---

## 7. Adding Documents

Place any policy documents (`.txt`, `.pdf`, or `.docx`) in:
`data/knowledge_base/`

To force a rebuild of the retrieval index after adding documents, click the **Reload Knowledge Base** button in the **Documents** tab of the UI, or send a POST request to:
`POST http://localhost:5000/api/reload`

---

## 8. Example Questions

### Answered by the Knowledge Base:
1. *What is the annual leave entitlement?* (Answers 20 days)
2. *How far in advance should leave be requested?* (Answers 2 weeks)
3. *What is the remote work policy?* (Answers hybrid 3-day split, core hours)
4. *What are the password requirements?* (Answers 12-char length, complexity)
5. *What are the expense reimbursement limits?* (Answers hotel, food limits)
6. *What are the requirements and restrictions for remote work?* (Answers hybrid schedule, equipment rules)

### Requiring Synthesis:
7. *How do leave and remote-work policies interact?* (Synthesizes probationary period constraints across sections)

### Out-of-Scope (Triggers Insufficient Evidence):
8. *What was the company's revenue last year?*
9. *Who is the CEO?*
10. *What is the company's stock price today?*

---

## 9. Hallucination Prevention & Gating

To guarantee grounding, CEREBRO measures relevance using a raw semantic score. If the maximum similarity score across all retrieved chunks is below `0.68`, the agent concludes there is no sufficient evidence and returns:

> "I couldn't find enough information in the provided knowledge-base sources to answer this question reliably."

---

## 10. Automated Tests

Run the test suite using pytest to verify retrieval, citations, grounding, and API routes:
```bash
pytest tests/ -v
```
All 21 test cases are passing.
