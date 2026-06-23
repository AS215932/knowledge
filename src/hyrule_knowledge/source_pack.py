"""Build bounded source packs for LLM enrichment."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .exporter import load_okf_concepts


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_source_pack(bundle_root: Path, target: str, max_chars: int = 120_000) -> dict[str, Any]:
    concepts = load_okf_concepts(bundle_root)
    selected = _select_concepts(concepts, target)
    payload: dict[str, Any] = {
        "target": target,
        "rules": [
            "Use only provided concepts and source_refs.",
            "Every factual claim must cite a provided source_ref index or concept id.",
            "If the source pack does not support a fact, write 'Unknown from indexed sources'.",
            "Do not include secrets, credential values, cookies, private keys, wallet data, or raw tokens.",
        ],
        "concepts": [],
    }
    used = len(json.dumps(payload))
    for concept in selected:
        compact = {
            "id": concept["id"],
            "type": concept["type"],
            "title": concept["title"],
            "description": concept["description"],
            "tags": concept["tags"],
            "source_refs": concept["source_refs"],
            "body_excerpt": concept["body"][:3000],
        }
        size = len(json.dumps(compact, ensure_ascii=False))
        if used + size > max_chars:
            break
        payload["concepts"].append(compact)
        used += size
    payload["input_hash"] = sha256_text(json.dumps(payload, sort_keys=True, ensure_ascii=False))
    return payload


def _select_concepts(concepts: list[dict[str, Any]], target: str) -> list[dict[str, Any]]:
    if target == "all":
        preferred = {
            "Organization",
            "Service",
            "Project",
            "Domain Policy",
            "Runbook",
            "Agent Instruction",
            "Business Analysis",
            "Workflow",
        }
        return [c for c in concepts if c["type"] in preferred][:120]
    if target == "org":
        return [c for c in concepts if c["id"].startswith("generated/org/") or c["type"] in {"Repository", "Service", "Project", "Domain Policy"}]
    if target == "services":
        return [c for c in concepts if c["id"].startswith("generated/services/") or c["id"].startswith("generated/projects/")]
    if target == "architecture":
        return [c for c in concepts if c["type"] in {"Service", "Project", "Infrastructure Host", "Router", "Domain Policy", "Workflow"}]
    if target == "api":
        return [c for c in concepts if c["type"] in {"API Endpoint", "API Schema", "Service"}]
    if target == "infrastructure":
        return [
            c
            for c in concepts
            if c["type"]
            in {"Infrastructure Host", "Router", "DNS Zone", "Network Prefix", "Monitoring Inventory", "Workflow", "Deployment"}
        ]
    return [c for c in concepts if target in c["id"] or target.lower() in c["title"].lower()]
