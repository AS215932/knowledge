"""Sanitized learning-ledger fixtures and validation.

The ledger is deliberately fixture/local-artifact first: committed data must be
sanitized summaries with citations, not raw traces, logs, packet captures, tool
output, credentials, or live telemetry dumps.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from .contracts import stable_hash, utc_now_iso

LEDGER_VERSION = "learning_ledger_v1"
DEFAULT_FIXTURE_DIR = Path("ledger/fixtures")
REPORT_JSON = Path("reports/learning-ledger.json")
REPORT_JSONL = Path("reports/learning-ledger.jsonl")
REPORT_MD = Path("reports/learning-ledger.md")

EVENT_TYPES = {
    "context_pack_used",
    "engineering_loop_run_summary",
    "noc_shadow_eval_summary",
    "eval_run_summary",
    "policy_review_summary",
    "lesson_candidate",
}
STATUSES = {"fixture", "proposed", "reviewed", "rejected", "superseded"}
PRODUCERS = {"knowledge", "engineering_loop", "noc_shadow", "human_review", "fixture"}
FORBIDDEN_DATA_CLASSES = {"secret", "credential", "raw_log", "packet_capture", "command_output", "live_trace"}
FORBIDDEN_KEY_PARTS = {
    "raw_log",
    "packet_capture",
    "pcap",
    "stdout",
    "stderr",
    "command_output",
    "transcript",
    "secret",
    "credential",
    "authorization",
    "cookie",
    "private_key",
    "password",
}
SECRET_VALUE_RE = re.compile(
    r"(-----BEGIN [A-Z ]+PRIVATE KEY-----|\bBearer\s+[A-Za-z0-9._~-]+|authorization:\s*bearer|x-api-key\s*[:=]|password\s*[:=])",
    re.IGNORECASE,
)


class LearningLedgerError(RuntimeError):
    """Raised when learning-ledger fixtures are malformed."""


def stable_learning_event_id(event: dict[str, Any]) -> str:
    return stable_hash(
        "learn",
        [
            event.get("event_type"),
            event.get("producer"),
            event.get("subject"),
            event.get("summary"),
            event.get("citations", []),
            event.get("context_pack_ids", []),
            event.get("policy_decision_ids", []),
        ],
    )


def normalize_learning_event(event: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(event)
    normalized.setdefault("ledger_version", LEDGER_VERSION)
    normalized.setdefault("id", stable_learning_event_id(normalized))
    normalized.setdefault("event_time", "2026-06-17T00:00:00Z")
    normalized.setdefault("status", "fixture")
    normalized.setdefault("authority_tier", "A4")
    normalized.setdefault("data_classes", ["sanitized_trace_summary", "source_ref", "okf_concept"])
    normalized.setdefault("citations", [])
    normalized.setdefault("context_pack_ids", [])
    normalized.setdefault("policy_decision_ids", [])
    normalized.setdefault("eval_case_ids", [])
    normalized.setdefault("metrics", {})
    normalized.setdefault("lessons", [])
    normalized.setdefault("promotion", {"review_required": True})
    normalized.setdefault("metadata", {})
    return normalized


def load_learning_events(paths: list[Path] | None = None) -> list[dict[str, Any]]:
    targets = paths or sorted(DEFAULT_FIXTURE_DIR.glob("*.json"))
    events: list[dict[str, Any]] = []
    for path in targets:
        if path.is_dir():
            events.extend(load_learning_events(sorted(path.glob("*.json"))))
            continue
        loaded = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(loaded, list):
            rows = loaded
        else:
            rows = [loaded]
        for row in rows:
            if not isinstance(row, dict):
                raise LearningLedgerError(f"learning event must be a JSON object: {path}")
            normalized = normalize_learning_event(row)
            normalized.setdefault("source", {"kind": "fixture", "path": path.as_posix()})
            events.append(normalized)
    return sorted(events, key=lambda event: str(event["id"]))


def validate_learning_event(event: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = ["id", "ledger_version", "event_type", "event_time", "producer", "subject", "summary", "status", "authority_tier"]
    for key in required:
        if not event.get(key):
            errors.append(f"missing required field: {key}")
    if event.get("ledger_version") != LEDGER_VERSION:
        errors.append(f"ledger_version must be {LEDGER_VERSION}")
    if event.get("event_type") not in EVENT_TYPES:
        errors.append(f"unknown event_type: {event.get('event_type')}")
    if event.get("status") not in STATUSES:
        errors.append(f"unknown status: {event.get('status')}")
    if event.get("producer") not in PRODUCERS:
        errors.append(f"unknown producer: {event.get('producer')}")
    if event.get("authority_tier") not in {"A2", "A3", "A4"}:
        errors.append("learning events must be A2 reviewed summaries, A3 observations, or A4 proposals/fixtures")
    raw_data_classes = event.get("data_classes")
    data_classes: list[Any] = raw_data_classes if isinstance(raw_data_classes, list) else []
    denied = sorted(set(str(item) for item in data_classes) & FORBIDDEN_DATA_CLASSES)
    if denied:
        errors.append(f"forbidden data_classes: {', '.join(denied)}")
    raw_citations = event.get("citations")
    citations: list[Any] = raw_citations if isinstance(raw_citations, list) else []
    if event.get("event_type") != "eval_run_summary" and not citations:
        errors.append("non-eval learning events require at least one citation")
    if citations:
        for idx, citation in enumerate(citations):
            if not isinstance(citation, dict):
                errors.append(f"citation[{idx}] must be an object")
                continue
            if not any(citation.get(key) for key in ("concept_id", "claim_id", "source_uri", "context_pack_id")):
                errors.append(f"citation[{idx}] must include concept_id, claim_id, source_uri, or context_pack_id")
    errors.extend(_forbidden_payload_findings(event))
    return errors


def validate_learning_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    seen: set[str] = set()
    for event in events:
        event_id = str(event.get("id", ""))
        if event_id in seen:
            findings.append({"event_id": event_id, "severity": "critical", "message": "duplicate learning event id"})
        seen.add(event_id)
        for message in validate_learning_event(event):
            findings.append({"event_id": event_id, "severity": "critical", "message": message})
    return findings


def write_learning_ledger_reports(paths: list[Path] | None = None) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    events = load_learning_events(paths)
    findings = validate_learning_events(events)
    REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(
        json.dumps({"ledger_version": LEDGER_VERSION, "event_count": len(events), "finding_count": len(findings), "findings": findings}, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    REPORT_JSONL.write_text("".join(json.dumps(event, sort_keys=True) + "\n" for event in events), encoding="utf-8")
    lines = ["# Learning ledger fixture report", "", f"* Events: **{len(events)}**", f"* Critical findings: **{len(findings)}**", ""]
    if findings:
        lines.append("## Findings")
        for finding in findings:
            lines.append(f"* `{finding['event_id']}` — {finding['message']}")
    else:
        lines.append("No critical findings.")
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return events, findings


def ledger_check(paths: list[Path] | None = None) -> list[str]:
    events = load_learning_events(paths)
    return [f"{finding['event_id']}: {finding['message']}" for finding in validate_learning_events(events)]


def _forbidden_payload_findings(value: Any, *, path: str = "$") -> list[str]:
    findings: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            key_text = str(key).lower()
            if any(part in key_text for part in FORBIDDEN_KEY_PARTS):
                findings.append(f"forbidden key at {path}.{key}: {key}")
            findings.extend(_forbidden_payload_findings(child, path=f"{path}.{key}"))
    elif isinstance(value, list):
        for idx, child in enumerate(value):
            findings.extend(_forbidden_payload_findings(child, path=f"{path}[{idx}]"))
    elif isinstance(value, str) and SECRET_VALUE_RE.search(value):
        findings.append(f"secret-like value at {path}")
    return findings


def build_local_learning_event(
    *,
    producer: str,
    event_type: str,
    subject: str,
    summary: str,
    citations: list[dict[str, Any]],
    status: str = "proposed",
    authority_tier: str = "A4",
    context_pack_ids: list[str] | None = None,
    policy_decision_ids: list[str] | None = None,
    eval_case_ids: list[str] | None = None,
    metrics: dict[str, Any] | None = None,
    lessons: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    event = normalize_learning_event(
        {
            "event_type": event_type,
            "event_time": utc_now_iso(),
            "producer": producer,
            "subject": subject,
            "summary": summary,
            "status": status,
            "authority_tier": authority_tier,
            "citations": citations,
            "context_pack_ids": context_pack_ids or [],
            "policy_decision_ids": policy_decision_ids or [],
            "eval_case_ids": eval_case_ids or [],
            "metrics": metrics or {},
            "lessons": lessons or [],
            "metadata": metadata or {},
            "promotion": {"review_required": True, "target": "okf/curated/lessons"},
        }
    )
    errors = validate_learning_event(event)
    if errors:
        raise LearningLedgerError("invalid learning event: " + "; ".join(errors))
    return event
