"""OpenRouter LLM client and enrichment validation."""

from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any


class LLMError(RuntimeError):
    """Raised when enrichment cannot be produced or validated."""


@dataclass(frozen=True)
class LLMConfig:
    provider: str = "openrouter"
    model: str = "anthropic/claude-sonnet-4.6"
    temperature: float = 0.2
    api_key_env: str = "OPENROUTER_API_KEY"


FORBIDDEN_OUTPUT_RE = re.compile(
    r"(?i)(BEGIN [A-Z ]*PRIVATE KEY|api[_-]?key\s*[:=]|auth[_-]?token\s*[:=]|password\s*[:=]|secret\s*[:=]|sk-[A-Za-z0-9_-]{16,})"
)


SYSTEM_PROMPT = """You enrich an OKF knowledge base for AS215932.
Use only the supplied source pack. Return strict JSON only.
Every factual claim must include at least one citation to a supplied concept id
or source_ref. If unsupported, write exactly: Unknown from indexed sources.
Never include secrets, credential values, cookies, private keys, wallet data, or raw tokens.
Generated content is advisory/proposed unless the source explicitly says otherwise.
"""


def build_user_prompt(source_pack: dict[str, Any]) -> str:
    return (
        "Create useful source-cited OKF enrichment from this source pack.\n"
        "Return JSON with keys: title, description, sections, claims.\n"
        "sections must be a list of {heading, body, citations}.\n"
        "claims must be a list of {text, citations}.\n\n"
        + json.dumps(source_pack, sort_keys=True, ensure_ascii=False)
    )


def call_openrouter(
    source_pack: dict[str, Any], config: LLMConfig
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    api_key = os.environ.get(config.api_key_env)
    if not api_key:
        raise LLMError(f"missing {config.api_key_env}; LLM enrichment is manual/opt-in")
    payload = {
        "model": config.model,
        "temperature": config.temperature,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(source_pack)},
        ],
        "response_format": {"type": "json_object"},
        "usage": {"include": True},
    }
    request = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "authorization": f"Bearer {api_key}",
            "content-type": "application/json",
            "http-referer": "https://github.com/AS215932/knowledge",
            "x-title": "AS215932 Knowledge Enrichment",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise LLMError(f"OpenRouter request failed: {exc}") from exc
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise LLMError("OpenRouter response was not valid JSON") from exc
    content = data["choices"][0]["message"]["content"]
    result = parse_json_object_response(content)
    validate_enrichment_json(result, _allowed_citations(source_pack))
    usage: dict[str, Any] | None = data.get("usage") if isinstance(data, dict) else None
    return result, usage


def parse_json_object_response(content: Any) -> dict[str, Any]:
    if not isinstance(content, str):
        raise LLMError("OpenRouter message content was not text")
    text = content.strip()
    if text.startswith("```json") or text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as exc:
        raise LLMError("OpenRouter message content was not a JSON object") from exc
    if not isinstance(parsed, dict):
        raise LLMError("OpenRouter content was not a JSON object")
    return parsed


def _allowed_citations(source_pack: dict[str, Any]) -> set[str]:
    allowed: set[str] = set()
    concepts = source_pack.get("concepts", [])
    if isinstance(concepts, list):
        for concept in concepts:
            if isinstance(concept, dict) and concept.get("id"):
                allowed.add(str(concept["id"]))
            refs = concept.get("source_refs") if isinstance(concept, dict) else None
            if isinstance(refs, list):
                for ref in refs:
                    if isinstance(ref, dict):
                        repo = ref.get("repo")
                        path = ref.get("path")
                        if repo and path:
                            allowed.add(f"{repo}:{path}")
                        elif repo:
                            allowed.add(str(repo))
                        if ref.get("url"):
                            allowed.add(str(ref["url"]))
    return allowed


def validate_enrichment_json(data: dict[str, Any], allowed_citations: set[str]) -> None:
    if FORBIDDEN_OUTPUT_RE.search(json.dumps(data, sort_keys=True, ensure_ascii=False)):
        raise LLMError("enrichment JSON contains forbidden secret-like output")
    if _claims_canonicality(data):
        raise LLMError("enrichment JSON makes unsupported canonicality claims")
    if not isinstance(data.get("sections"), list) or not data["sections"]:
        raise LLMError("enrichment JSON missing non-empty sections")
    for section in data["sections"]:
        if not isinstance(section, dict):
            raise LLMError("section must be an object")
        if not section.get("heading") or not section.get("body"):
            raise LLMError("section missing heading/body")
        _validate_citations(section.get("citations"), allowed_citations, f"section {section.get('heading')}")
    claims = data.get("claims", [])
    if claims is not None and not isinstance(claims, list):
        raise LLMError("claims must be a list")
    for claim in claims or []:
        if not isinstance(claim, dict):
            raise LLMError("claim must be an object")
        if claim.get("text"):
            _validate_citations(claim.get("citations"), allowed_citations, "claim")


def _validate_citations(raw: Any, allowed_citations: set[str], label: str) -> None:
    if not isinstance(raw, list) or not raw:
        raise LLMError(f"{label} missing citations")
    for citation in raw:
        if str(citation) not in allowed_citations:
            raise LLMError(f"unknown citation: {citation}")


def _claims_canonicality(data: dict[str, Any]) -> bool:
    text = json.dumps(data, sort_keys=True, ensure_ascii=False).lower()
    forbidden_phrases = [
        "this enrichment is canonical",
        "authority: canonical",
        "authority is canonical",
        "truth_owner: okf",
        "truth owner is okf",
    ]
    return any(phrase in text for phrase in forbidden_phrases)
