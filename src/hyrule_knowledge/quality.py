"""Coverage and usefulness quality reports."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

from .exporter import load_edges, load_okf_concepts, read_jsonl, write_jsonl
from .models import QualityFinding

TOP_LEVEL_IDS = [
    "generated/org/as215932",
    "generated/projects/network-operations",
    "generated/projects/hyrule-business",
    "generated/services/hyrule-cloud",
    "generated/services/hyrule-web",
    "generated/services/noc-agent",
    "generated/services/hyrule-mcp",
    "generated/services/hyrule-network-proxy",
    "generated/services/engineering-loop",
    "generated/services/as215932-net",
]

REQUIRED_SERVICE_SECTIONS = [
    "# What this is",
    "# Responsibilities",
    "# Runtime/deployment shape",
    "# Interfaces",
    "# Dependencies",
    "# Source-of-truth files",
    "# Safety/security constraints",
    "# Citations",
]


def evaluate_quality(bundle_root: Path, exports_dir: Path = Path("exports")) -> tuple[dict[str, Any], list[QualityFinding]]:
    concepts = load_okf_concepts(bundle_root)
    by_id = {concept["id"]: concept for concept in concepts}
    edges = load_edges(exports_dir)
    source_rows = read_jsonl(exports_dir / "sources.jsonl")
    observation_rows = read_jsonl(exports_dir / "observations.jsonl")
    enrichment_rows = read_jsonl(exports_dir / "enrichment-runs.jsonl")
    inbound: dict[str, int] = defaultdict(int)
    outbound: dict[str, int] = defaultdict(int)
    for edge in edges:
        outbound[str(edge["source"])] += 1
        inbound[str(edge["target"])] += 1
    findings: list[QualityFinding] = []

    for concept_id in TOP_LEVEL_IDS:
        concept = by_id.get(concept_id)
        if concept is None:
            findings.append(QualityFinding(concept_id, "critical", "missing_top_level", "Required top-level concept is missing."))
            continue
        body = str(concept.get("body", ""))
        if len(body) < 800:
            findings.append(QualityFinding(concept_id, "critical", "top_level_too_short", "Top-level concept body is under 800 characters."))
        if concept_id != "generated/org/as215932":
            for section in REQUIRED_SERVICE_SECTIONS:
                if section not in body:
                    findings.append(QualityFinding(concept_id, "critical", "missing_required_section", f"Missing required section `{section}`."))

    for concept in concepts:
        concept_id = str(concept["id"])
        concept_type = str(concept["type"])
        body = str(concept.get("body", ""))
        source_refs = concept.get("source_refs")
        if concept_id.startswith("generated/") and not source_refs:
            findings.append(QualityFinding(concept_id, "critical", "missing_source_refs", "Generated concept has no source_refs."))
        if concept_id.startswith("generated/enriched/"):
            if not _frontmatter(bundle_root, concept_id).get("enrichment"):
                findings.append(QualityFinding(concept_id, "critical", "missing_enrichment_metadata", "LLM-enriched concept lacks enrichment metadata."))
            if "Citations" not in body and "citations:" not in body.lower():
                findings.append(QualityFinding(concept_id, "critical", "enrichment_missing_citations", "LLM-enriched concept lacks citations."))
        if concept_id.startswith("observed/") and concept.get("authority") == "canonical":
            findings.append(QualityFinding(concept_id, "critical", "observed_canonical", "Observed concept must not be canonical."))
        if concept_type == "API Endpoint":
            frontmatter = _frontmatter(bundle_root, concept_id)
            if (
                not concept.get("resource")
                or not frontmatter.get("method")
                or not frontmatter.get("route")
                or not source_refs
            ):
                findings.append(QualityFinding(concept_id, "critical", "endpoint_missing_fields", "Endpoint concept missing method/route/source metadata."))
        if concept_type in {"Infrastructure Host", "Router"}:
            if not source_refs or not concept.get("description"):
                findings.append(QualityFinding(concept_id, "critical", "host_missing_source", "Host concept missing source or description."))
        if concept_type == "Source Document" and len(body) < 700:
            findings.append(QualityFinding(concept_id, "warning", "shallow_source_doc", "Source document concept is shallow."))
        if inbound.get(concept_id, 0) == 0 and not concept_id.startswith("generated/org/"):
            findings.append(QualityFinding(concept_id, "warning", "no_inbound_links", "Concept has no inbound graph edges."))
        if outbound.get(concept_id, 0) == 0 and concept_type in {"Service", "Project", "Organization"}:
            findings.append(QualityFinding(concept_id, "warning", "no_outbound_links", "Top-level concept has no outbound graph edges."))

    counts_by_type = Counter(str(concept["type"]) for concept in concepts)
    counts_by_truth = Counter(str(concept.get("truth_owner")) for concept in concepts)
    counts_by_authority = Counter(str(concept.get("authority")) for concept in concepts)
    source_repos = sorted({str(row.get("repo")) for row in source_rows if row.get("repo")})
    source_files = sorted({f"{row.get('repo')}:{row.get('path')}" for row in source_rows if row.get("repo") and row.get("path")})
    report = {
        "concept_count": len(concepts),
        "edge_count": len(edges),
        "source_repo_count": len(source_repos),
        "source_repos": source_repos,
        "source_file_ref_count": len(source_files),
        "source_files_skipped": "Not enumerated in quality report; see knowledge.config.yml include/exclude patterns and ingestion logs.",
        "telemetry_source_status": _telemetry_status(observation_rows),
        "llm_enrichment_run_status": "not_run" if not enrichment_rows else "proposed_output_present",
        "llm_enrichment_run_count": len(enrichment_rows),
        "concepts_by_type": dict(sorted(counts_by_type.items())),
        "concepts_by_truth_owner": dict(sorted(counts_by_truth.items())),
        "concepts_by_authority": dict(sorted(counts_by_authority.items())),
        "critical_count": sum(1 for finding in findings if finding.severity == "critical"),
        "warning_count": sum(1 for finding in findings if finding.severity == "warning"),
        "endpoint_count": counts_by_type.get("API Endpoint", 0),
        "schema_count": counts_by_type.get("API Schema", 0),
        "host_count": counts_by_type.get("Infrastructure Host", 0) + counts_by_type.get("Router", 0),
        "observed_count": sum(1 for concept in concepts if str(concept["id"]).startswith("observed/")),
        "llm_enriched_count": sum(1 for concept in concepts if str(concept["id"]).startswith("generated/enriched/")),
    }
    return report, findings


def write_quality_reports(bundle_root: Path, reports_dir: Path = Path("reports"), exports_dir: Path = Path("exports")) -> None:
    report, findings = evaluate_quality(bundle_root, exports_dir)
    reports_dir.mkdir(parents=True, exist_ok=True)
    (reports_dir / "coverage.json").write_text(json.dumps(report, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    quality = {"summary": report, "findings": [finding.as_json() for finding in findings]}
    (reports_dir / "quality.json").write_text(json.dumps(quality, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    write_jsonl(reports_dir / "quality.jsonl", [finding.as_json() for finding in findings])
    _write_coverage_md(reports_dir / "coverage.md", report, findings)
    _write_shallow_md(reports_dir / "shallow-concepts.md", findings)


def quality_check(bundle_root: Path, reports_dir: Path = Path("reports"), exports_dir: Path = Path("exports")) -> list[QualityFinding]:
    report, findings = evaluate_quality(bundle_root, exports_dir)
    if not (reports_dir / "quality.json").exists() or not (reports_dir / "coverage.json").exists():
        return [QualityFinding("reports", "critical", "missing_reports", "Quality reports are missing; run `hyrule-knowledge quality --write`.")]
    critical = [finding for finding in findings if finding.severity == "critical"]
    stored = json.loads((reports_dir / "coverage.json").read_text(encoding="utf-8"))
    if stored.get("critical_count") != report.get("critical_count") or stored.get("concept_count") != report.get("concept_count"):
        critical.append(QualityFinding("reports", "critical", "stale_reports", "Quality reports are stale; run `hyrule-knowledge quality --write`."))
    return critical


def _telemetry_status(observation_rows: list[dict[str, Any]]) -> dict[str, str]:
    if not observation_rows:
        return {"prometheus": "not_collected", "icinga": "not_collected", "hyrule_mcp": "not_collected"}
    latest = max(observation_rows, key=lambda row: str(row.get("observed_at") or ""))
    raw = latest.get("payload_json") or "{}"
    try:
        payload = json.loads(str(raw))
    except json.JSONDecodeError:
        return {"observation": "unparseable"}
    sources = payload.get("sources") if isinstance(payload, dict) else None
    if not isinstance(sources, dict):
        return {"observation": str(latest.get("status") or "unknown")}
    status: dict[str, str] = {}
    for name, source_payload in sources.items():
        if isinstance(source_payload, dict):
            status[str(name)] = str(source_payload.get("status") or "unknown")
    return status


def _frontmatter(bundle_root: Path, concept_id: str) -> dict[str, Any]:
    path = bundle_root / f"{concept_id}.md"
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    _, raw, _ = text.split("---\n", 2)
    parsed = yaml.safe_load(raw)
    return parsed if isinstance(parsed, dict) else {}


def _write_coverage_md(path: Path, report: dict[str, Any], findings: list[QualityFinding]) -> None:
    lines = [
        "# Knowledge coverage report",
        "",
        f"* Concepts: **{report['concept_count']}**",
        f"* Edges: **{report['edge_count']}**",
        f"* Critical findings: **{report['critical_count']}**",
        f"* Warnings: **{report['warning_count']}**",
        f"* Source repos indexed: **{report['source_repo_count']}**",
        f"* Source files with refs: **{report['source_file_ref_count']}**",
        f"* API endpoints: **{report['endpoint_count']}**",
        f"* API schemas: **{report['schema_count']}**",
        f"* Infrastructure hosts/routers: **{report['host_count']}**",
        f"* Observed concepts: **{report['observed_count']}**",
        f"* LLM enriched concepts: **{report['llm_enriched_count']}**",
        f"* LLM enrichment run status: **{report['llm_enrichment_run_status']}**",
        "",
        "# Telemetry source status",
        "",
    ]
    for key, value in report["telemetry_source_status"].items():
        lines.append(f"* `{key}`: `{value}`")
    lines.extend([
        "",
        "# Source repositories",
        "",
    ])
    for repo in report["source_repos"]:
        lines.append(f"* `{repo}`")
    lines.extend(
        [
            "",
            f"Source files skipped: {report['source_files_skipped']}",
            "",
            "# Concepts by type",
            "",
        ]
    )
    for key, value in report["concepts_by_type"].items():
        lines.append(f"* `{key}`: {value}")
    lines.extend(["", "# Critical findings", ""])
    critical = [finding for finding in findings if finding.severity == "critical"]
    if critical:
        lines.extend(f"* `{finding.concept_id}` — **{finding.code}**: {finding.message}" for finding in critical)
    else:
        lines.append("No critical findings.")
    lines.extend(["", "# Warning summary", ""])
    warning_counts = Counter(finding.code for finding in findings if finding.severity == "warning")
    if warning_counts:
        for code, count in sorted(warning_counts.items()):
            lines.append(f"* `{code}`: {count}")
    else:
        lines.append("No warnings.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_shallow_md(path: Path, findings: list[QualityFinding]) -> None:
    lines = ["# Shallow concepts", ""]
    shallow = [finding for finding in findings if finding.code in {"shallow_source_doc", "top_level_too_short"}]
    if not shallow:
        lines.append("No shallow concepts detected by current quality rules.")
    else:
        for finding in shallow:
            lines.append(f"* `{finding.concept_id}` — {finding.message}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
