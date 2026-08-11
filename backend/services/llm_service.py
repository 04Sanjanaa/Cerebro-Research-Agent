"""
LLM Service — CEREBRO Research Agent
Grounded answer generation using OpenAI GPT models.
Enforces evidence-only answering with citation instructions.
"""

import os
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

# Insufficient-evidence response template
INSUFFICIENT_EVIDENCE_RESPONSE = (
    "I couldn't find enough information in the provided knowledge-base sources "
    "to answer this question reliably.\n\n"
    "**Sources consulted:** None sufficiently relevant.\n\n"
    "Please check if the relevant document has been added to the knowledge base, "
    "or rephrase your question."
)

GROUNDED_SYSTEM_PROMPT = """You are CEREBRO, an AI research assistant that answers questions STRICTLY based on the provided evidence passages.

CRITICAL RULES — you MUST follow all of these:
1. Answer ONLY using information explicitly present in the provided evidence passages.
2. NEVER invent facts, statistics, names, policies, or any information not in the evidence.
3. NEVER use your general training knowledge to fill in gaps.
4. For every factual claim or piece of information you include in your answer, add an inline citation in square brackets [1], [2], etc., referring to the source passage number.
5. If multiple passages support the same point, cite all relevant ones: [1][2].
6. If the evidence passages do NOT contain sufficient information to answer the question, respond ONLY with: "I couldn't find enough information in the provided sources to answer this question."
7. Do NOT fabricate citations. Only cite passages that directly support the claim.
8. Be clear about when you are synthesizing across multiple sources vs. quoting a single source.
9. Use clear, professional language. Format with markdown where helpful.
10. Start your answer directly — do not repeat the question."""


class LLMService:
    """
    Generates grounded answers with citations using OpenAI GPT.
    Falls back to a template response when no API key is configured.
    """

    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY", "")
        self.model = model
        self.enabled = False
        self.client = None

        if self.api_key:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=self.api_key)
                self.enabled = True
                print(f"[LLMService] OpenAI enabled. Model: {self.model}")
            except ImportError:
                print("[LLMService] openai package not installed. LLM disabled.")
            except Exception as e:
                print(f"[LLMService] Failed to initialize OpenAI client: {e}")
        else:
            print("[LLMService] No OPENAI_API_KEY found. Running in keyword-fallback mode.")

    def generate_grounded_answer(
        self,
        query: str,
        evidence_context: str,
        citations: List[Dict[str, Any]],
        has_evidence: bool,
    ) -> Dict[str, Any]:
        """
        Generate a cited, grounded answer using the LLM.

        Args:
            query: User research question.
            evidence_context: Formatted evidence passages with citation labels.
            citations: Citation metadata list.
            has_evidence: Whether sufficient evidence was found.

        Returns:
            dict with keys: success, response, model, tokens_used (if applicable)
        """
        # ── Insufficient Evidence Branch ──────────────────────────────────────
        if not has_evidence:
            return {
                "success": True,
                "response": INSUFFICIENT_EVIDENCE_RESPONSE,
                "model": "fallback",
                "tokens_used": 0,
                "insufficient_evidence": True,
            }

        # ── LLM Branch ────────────────────────────────────────────────────────
        if self.enabled and self.client:
            return self._call_openai(query, evidence_context)

        # ── Keyword Fallback Branch ───────────────────────────────────────────
        return self._keyword_fallback(query, citations)

    def _call_openai(self, query: str, evidence_context: str) -> Dict[str, Any]:
        """Call OpenAI API with grounded prompt."""
        user_prompt = (
            f"Research Question: {query}\n\n"
            f"Evidence Passages:\n{evidence_context}\n\n"
            "Please answer the research question using ONLY the evidence passages above. "
            "Cite each claim with the passage number in square brackets."
        )

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": GROUNDED_SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.1,  # Low temperature for factual accuracy
                max_tokens=1000,
            )
            answer = response.choices[0].message.content
            return {
                "success": True,
                "response": answer,
                "model": self.model,
                "tokens_used": response.usage.total_tokens,
                "insufficient_evidence": False,
            }
        except Exception as e:
            print(f"[LLMService] OpenAI call failed: {e}")
            return {
                "success": False,
                "response": f"LLM error: {str(e)}. Falling back to extracted summary.",
                "model": self.model,
                "tokens_used": 0,
                "insufficient_evidence": False,
            }

    def _keyword_fallback(
        self, query: str, citations: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Template-based response when LLM is not available.
        Extracts key bullet points from evidence and adds citation labels.
        """
        if not citations:
            return {
                "success": True,
                "response": INSUFFICIENT_EVIDENCE_RESPONSE,
                "model": "keyword_fallback",
                "tokens_used": 0,
                "insufficient_evidence": True,
            }

        parts = []
        parts.append(
            f"*Note: LLM is not configured (no OPENAI_API_KEY). "
            f"Showing extracted evidence passages.*\n"
        )

        for c in citations:
            label = c["label"]
            source = c["source"]
            section = c.get("section", "")
            text = c.get("full_text", c.get("passage", ""))

            # Extract bullet points if present
            lines = [l.strip() for l in text.split("\n") if l.strip()]
            bullets = [l for l in lines if l.startswith(("•", "-", "*", "–"))]
            display_lines = bullets[:8] if bullets else lines[:5]
            content = "\n".join(display_lines)

            header = f"**{source}**"
            if section:
                header += f" — {section}"

            parts.append(f"{header} {label}\n\n{content}")

        response_text = "\n\n---\n\n".join(parts)
        return {
            "success": True,
            "response": response_text,
            "model": "keyword_fallback",
            "tokens_used": 0,
            "insufficient_evidence": False,
        }
