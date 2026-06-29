"""Manual LLM enrichment command helpers."""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

from .agent_core_trace import emit_enrich_cost
from .llm import LLMConfig, LLMError, call_openrouter
from .models import Concept, EnrichmentMetadata, SourceRef
from .okf_writer import dump_concept, slugify
from .source_pack import build_source_pack, sha256_text


def enrich_target(
    bundle_root: Path,
    target: str,
    provider: str = "openrouter",
    model: str = "anthropic/claude-sonnet-4.6",
    max_input_chars: int = 120_000,
    temperature: float = 0.2,
    dry_run: bool = False,
) -> Path:
    source_pack = build_source_pack(bundle_root, target, max_input_chars)
    generated_at = datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    usage: dict[str, Any] | None = None
    if dry_run:
        output = _dry_run_output(source_pack)
    else:
        if provider != "openrouter":
            raise LLMError(f"unsupported provider for this tranche: {provider}")
        output, usage = call_openrouter(
            source_pack, LLMConfig(provider=provider, model=model, temperature=temperature)
        )
    body = _body_from_output(output)
    output_hash = sha256_text(json.dumps(output, sort_keys=True, ensure_ascii=False))
    source_refs = _source_refs_from_pack(source_pack)
    concept = Concept(
        concept_id=f"generated/enriched/{slugify(target)}",
        concept_type="Reference",
        title=str(output.get("title") or f"LLM enrichment: {target}"),
        description=str(output.get("description") or f"LLM-drafted source-cited enrichment for `{target}`."),
        tags=["enriched", "llm", target],
        truth_owner="derived",
        authority="advisory",
        source_refs=source_refs,
        last_verified_at=generated_at,
        confidence="medium",
        dispute_policy="repo_wins",
        review_status="proposed",
        enrichment=EnrichmentMetadata(
            provider=provider,
            model=model,
            input_hash=str(source_pack["input_hash"]),
            output_hash=output_hash,
            generated_at=generated_at,
        ),
        body=body,
    )
    path = bundle_root.parent / concept.path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump_concept(concept), encoding="utf-8")
    _write_run_record(bundle_root.parent / "exports/enrichment-runs.jsonl", concept, source_pack, output)
    if not dry_run:
        emit_enrich_cost(provider, model, target, usage=usage)
    return path


def _dry_run_output(source_pack: dict[str, object]) -> dict[str, object]:
    target = str(source_pack.get("target", "unknown"))
    concepts = source_pack.get("concepts", [])
    citations: list[str] = []
    if isinstance(concepts, list):
        citations = [str(item.get("id")) for item in concepts if isinstance(item, dict) and item.get("id")][:3]
    if not citations:
        citations = ["Unknown from indexed sources"]
    return {
        "title": f"Dry-run enrichment for {target}",
        "description": "Dry-run output used to validate enrichment plumbing without calling OpenRouter.",
        "sections": [
            {
                "heading": "Dry-run summary",
                "body": "This dry-run proves the enrichment writer, frontmatter, validation, and export paths without spending model tokens.",
                "citations": citations,
            }
        ],
        "claims": [],
    }


def _body_from_output(output: dict[str, object]) -> str:
    sections = output.get("sections", [])
    lines = ["# LLM enrichment", "", "Review status: proposed. Treat this as advisory until human-reviewed.", ""]
    if isinstance(sections, list):
        for section in sections:
            if not isinstance(section, dict):
                continue
            lines.append(f"# {section.get('heading', 'Section')}")
            lines.append("")
            lines.append(str(section.get("body", "")))
            lines.append("")
            citations = section.get("citations", [])
            if isinstance(citations, list) and citations:
                lines.append("Citations: " + ", ".join(f"`{citation}`" for citation in citations))
                lines.append("")
    claims = output.get("claims", [])
    if isinstance(claims, list) and claims:
        lines.append("# Claims")
        lines.append("")
        for claim in claims:
            if isinstance(claim, dict):
                lines.append(f"* {claim.get('text')} — citations: `{claim.get('citations')}`")
    return "\n".join(lines).strip() + "\n"


def _source_refs_from_pack(source_pack: dict[str, object]) -> list[SourceRef]:
    refs: list[SourceRef] = []
    concepts = source_pack.get("concepts", [])
    if isinstance(concepts, list):
        for concept in concepts[:20]:
            if not isinstance(concept, dict):
                continue
            raw_refs = concept.get("source_refs", [])
            if not isinstance(raw_refs, list):
                continue
            for raw in raw_refs:
                if not isinstance(raw, dict):
                    continue
                refs.append(
                    SourceRef(
                        repo=str(raw.get("repo")) if raw.get("repo") else None,
                        path=str(raw.get("path")) if raw.get("path") else None,
                        commit=str(raw.get("commit")) if raw.get("commit") else None,
                        lines=str(raw.get("lines")) if raw.get("lines") else None,
                        url=str(raw.get("url")) if raw.get("url") else None,
                    )
                )
                if len(refs) >= 30:
                    return refs
    return refs


def _write_run_record(path: Path, concept: Concept, source_pack: dict[str, object], output: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "concept_id": concept.concept_id,
        "provider": concept.enrichment.provider if concept.enrichment else None,
        "model": concept.enrichment.model if concept.enrichment else None,
        "prompt_version": concept.enrichment.prompt_version if concept.enrichment else None,
        "input_hash": source_pack.get("input_hash"),
        "output_hash": sha256_text(json.dumps(output, sort_keys=True, ensure_ascii=False)),
        "created_at": concept.last_verified_at,
    }
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")


def load_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    _, raw, _ = text.split("---\n", 2)
    data = yaml.safe_load(raw)
    return data if isinstance(data, dict) else {}
