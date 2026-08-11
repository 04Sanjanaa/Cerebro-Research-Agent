"""
Document Service — CEREBRO Research Agent
Handles loading, chunking, and metadata extraction from knowledge-base documents.
Supports TXT, PDF, and DOCX formats.
"""

import os
import re
import uuid
from pathlib import Path
from typing import List, Dict, Any, Optional


def _load_txt(filepath: str) -> str:
    """Read a plain-text file."""
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def _load_pdf(filepath: str) -> str:
    """Extract text from a PDF file using pypdf."""
    try:
        import pypdf
        text_parts = []
        with open(filepath, "rb") as f:
            reader = pypdf.PdfReader(f)
            for page_num, page in enumerate(reader.pages, start=1):
                page_text = page.extract_text() or ""
                if page_text.strip():
                    text_parts.append(f"[Page {page_num}]\n{page_text}")
        return "\n\n".join(text_parts)
    except ImportError:
        raise RuntimeError(
            "pypdf is required for PDF support. Install it: pip install pypdf"
        )


def _load_docx(filepath: str) -> str:
    """Extract text from a DOCX file."""
    try:
        import docx
        doc = docx.Document(filepath)
        paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]
        return "\n\n".join(paragraphs)
    except ImportError:
        raise RuntimeError(
            "python-docx is required for DOCX support. Install it: pip install python-docx"
        )


def load_document(filepath: str) -> str:
    """Load text from a supported document file."""
    suffix = Path(filepath).suffix.lower()
    if suffix == ".txt" or suffix == ".md":
        return _load_txt(filepath)
    elif suffix == ".pdf":
        return _load_pdf(filepath)
    elif suffix == ".docx":
        return _load_docx(filepath)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")


def _extract_section_titles(text: str) -> List[Dict[str, Any]]:
    """
    Try to extract section headings and their line numbers from text.
    Returns list of {'title': str, 'line': int}.
    """
    lines = text.split("\n")
    sections = []
    # Common heading patterns: all-caps lines, numbered headings, === underlines
    heading_patterns = [
        re.compile(r"^(SECTION\s+\d+[\.:]\s+.+)$", re.IGNORECASE),
        re.compile(r"^(\d+\.\d*\s+[A-Z].{3,})$"),
        re.compile(r"^[=\-]{3,}$"),  # separator lines — grab preceding line
    ]
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        # Check separator pattern — the preceding non-empty line is the title
        if re.match(r"^[=\-]{5,}$", stripped):
            for j in range(i - 1, max(i - 5, -1), -1):
                prev = lines[j].strip()
                if prev:
                    sections.append({"title": prev, "line": j})
                    break
            continue
        for pat in heading_patterns[:2]:
            if pat.match(stripped):
                sections.append({"title": stripped, "line": i})
                break
    return sections


def split_by_sections(text: str) -> List[Dict[str, Any]]:
    """
    Split document text into logical sections based on common headings.
    """
    import re
    # Match headers like "SECTION 3: ...", "3.1 Annual Leave...", or "Policy Reference: ..."
    pattern = r'(?m)^([=\-]{3,}.*|[A-Z\s]{4,60}\s+—\s+.+|SECTION\s+\d+[\.:]\s+.+|\d+\.\d+\s+[A-Z].+)$'
    matches = list(re.finditer(pattern, text))
    
    sections = []
    if not matches:
        return [{"heading": "Introduction", "body": text}]
        
    first_start = matches[0].start()
    intro_text = text[:first_start].strip()
    if intro_text:
        lines = [l.strip() for l in intro_text.split("\n") if l.strip() and not re.match(r"^[=\-]{3,}$", l.strip())]
        if lines:
            sections.append({"heading": "Introduction", "body": "\n".join(lines)})
            
    for i in range(len(matches)):
        heading = matches[i].group(1).strip()
        # Clean heading from markdown or decorative separators
        heading = re.sub(r"^[=\-\s]+|[=\-\s]+$", "", heading).strip()
        
        start_idx = matches[i].end()
        end_idx = matches[i+1].start() if i + 1 < len(matches) else len(text)
        body = text[start_idx:end_idx].strip()
        
        # Clean body from divider lines
        body_lines = [line for line in body.split("\n") if not re.match(r"^[=\-]{3,}$", line.strip())]
        cleaned_body = "\n".join(body_lines).strip()
        
        if cleaned_body:
            sections.append({"heading": heading, "body": cleaned_body})
            
    return sections


def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 80,
    source_name: str = "unknown",
    doc_id: str = None,
) -> List[Dict[str, Any]]:
    """
    Split text into logical, section-preserving chunks.
    If a section's length exceeds chunk_size, it is sub-split into overlapping chunks.
    """
    if not text or not text.strip():
        return []

    doc_id = doc_id or str(uuid.uuid4())[:8]
    sections = split_by_sections(text)
    
    chunks: List[Dict[str, Any]] = []
    chunk_index = 0
    
    for sec in sections:
        heading = sec["heading"]
        body = sec["body"]
        words = body.split()
        if not words:
            continue
            
        # Section fits within chunk_size
        if len(words) <= chunk_size:
            chunk_id = f"{doc_id}_chunk_{chunk_index:03d}"
            chunks.append({
                "id": chunk_id,
                "text": f"{heading}\n{body}",
                "metadata": {
                    "doc_id": doc_id,
                    "source": source_name,
                    "section": heading,
                    "chunk_index": chunk_index,
                    "word_count": len(words)
                }
            })
            chunk_index += 1
        else:
            # Section is too large; split into overlapping sub-chunks
            i = 0
            part = 1
            while i < len(words):
                chunk_words = words[i : i + chunk_size]
                chunk_text_str = " ".join(chunk_words)
                chunk_id = f"{doc_id}_chunk_{chunk_index:03d}"
                chunks.append({
                    "id": chunk_id,
                    "text": f"{heading} (Part {part})\n{chunk_text_str}",
                    "metadata": {
                        "doc_id": doc_id,
                        "source": source_name,
                        "section": heading,
                        "chunk_index": chunk_index,
                        "word_count": len(chunk_words)
                    }
                })
                chunk_index += 1
                part += 1
                i += (chunk_size - overlap)
                
    return chunks


class DocumentService:
    """Loads and chunks all documents from the knowledge-base directory."""

    SUPPORTED_EXTENSIONS = {".txt", ".md", ".pdf", ".docx"}

    def __init__(self, knowledge_base_dir: str = "./data/knowledge_base"):
        self.knowledge_base_dir = knowledge_base_dir
        self._chunks: List[Dict[str, Any]] = []
        self._loaded = False

    def load_all(self, chunk_size: int = 500, overlap: int = 80) -> List[Dict[str, Any]]:
        """
        Load all supported documents from the knowledge-base directory and chunk them.
        Returns the list of chunks.
        """
        kb_path = Path(self.knowledge_base_dir)
        if not kb_path.exists():
            raise FileNotFoundError(
                f"Knowledge base directory not found: {self.knowledge_base_dir}"
            )

        all_chunks: List[Dict[str, Any]] = []
        doc_index = 0

        for file_path in sorted(kb_path.iterdir()):
            if file_path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
                continue
            try:
                text = load_document(str(file_path))
                doc_id = f"doc_{doc_index:03d}"
                file_chunks = chunk_text(
                    text,
                    chunk_size=chunk_size,
                    overlap=overlap,
                    source_name=file_path.name,
                    doc_id=doc_id,
                )
                all_chunks.extend(file_chunks)
                doc_index += 1
                print(f"[DocumentService] Loaded {file_path.name}: {len(file_chunks)} chunks")
            except Exception as e:
                print(f"[DocumentService] Error loading {file_path.name}: {e}")

        self._chunks = all_chunks
        self._loaded = True
        print(f"[DocumentService] Total chunks: {len(all_chunks)}")
        return all_chunks

    def get_chunks(self) -> List[Dict[str, Any]]:
        """Return cached chunks, loading if necessary."""
        if not self._loaded:
            self.load_all()
        return self._chunks

    def get_document_list(self) -> List[Dict[str, str]]:
        """Return a summary of loaded documents (unique sources)."""
        chunks = self.get_chunks()
        seen = {}
        for chunk in chunks:
            src = chunk["metadata"]["source"]
            if src not in seen:
                seen[src] = {
                    "source": src,
                    "chunk_count": 0,
                    "sections": set(),
                }
            seen[src]["chunk_count"] += 1
            seen[src]["sections"].add(chunk["metadata"].get("section", ""))
        result = []
        for src, info in seen.items():
            info["sections"] = sorted(info["sections"])
            result.append(info)
        return result

    def reload(self, chunk_size: int = 500, overlap: int = 80) -> List[Dict[str, Any]]:
        """Force reload all documents."""
        self._loaded = False
        return self.load_all(chunk_size=chunk_size, overlap=overlap)
