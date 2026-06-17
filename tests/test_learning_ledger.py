from __future__ import annotations

import json
from pathlib import Path

from hyrule_knowledge.learning_ledger import (
    build_local_learning_event,
    load_learning_events,
    validate_learning_event,
    validate_learning_events,
)


def test_learning_ledger_fixtures_are_valid() -> None:
    events = load_learning_events([Path("ledger/fixtures")])
    assert len(events) >= 4
    assert not validate_learning_events(events)
    assert all(event["ledger_version"] == "learning_ledger_v1" for event in events)


def test_learning_ledger_rejects_forbidden_payload() -> None:
    event = build_local_learning_event(
        producer="engineering_loop",
        event_type="lesson_candidate",
        subject="engineering_loop:test",
        summary="safe summary",
        citations=[{"concept_id": "generated/services/engineering-loop"}],
    )
    event["metadata"] = {"stdout": "raw command output"}
    errors = validate_learning_event(event)
    assert any("forbidden key" in error for error in errors)


def test_learning_ledger_rejects_uncited_non_eval_event() -> None:
    event = {
        "id": "learn_" + "a" * 32,
        "ledger_version": "learning_ledger_v1",
        "event_type": "lesson_candidate",
        "event_time": "2026-06-17T00:00:00Z",
        "producer": "engineering_loop",
        "subject": "engineering_loop:test",
        "summary": "missing citation",
        "status": "fixture",
        "authority_tier": "A4",
        "citations": [],
        "data_classes": ["sanitized_trace_summary"],
        "metrics": {},
        "lessons": [],
        "promotion": {"review_required": True},
        "metadata": {},
    }
    assert "non-eval learning events require at least one citation" in validate_learning_event(event)


def test_build_local_learning_event_is_sanitized_json() -> None:
    event = build_local_learning_event(
        producer="engineering_loop",
        event_type="engineering_loop_run_summary",
        subject="engineering_loop:change-1",
        summary="A compact status-only run summary.",
        citations=[{"concept_id": "generated/services/hyrule-cloud", "source_uri": "repo://AS215932/hyrule-cloud/README.md@fixture"}],
        metrics={"gate_status": "passed"},
    )
    raw = json.dumps(event, sort_keys=True)
    assert "stdout" not in raw
    assert "Bearer " not in raw
    assert event["id"].startswith("learn_")
