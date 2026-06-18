from __future__ import annotations

import json
from pathlib import Path

import pytest

from hyrule_knowledge.learning_ledger import import_learning_events, load_learning_events
from hyrule_knowledge.promotion import (
    analyze_learning_lifecycle,
    build_promotion_pr_body,
    lifecycle_check,
    promote_learning_event,
    promote_learning_event_for_pr,
    write_learning_lifecycle_reports,
)


def _fixture(name: str) -> Path:
    return Path("evals/fixtures/learning-events") / name


def test_import_learning_event_writes_proposed_event(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    source = Path(__file__).resolve().parents[1] / _fixture("safe-engineering-event.json")
    results = import_learning_events([source])
    assert results[0]["status"] == "imported"
    target = Path(results[0]["target_path"])
    assert target.exists()
    imported = json.loads(target.read_text(encoding="utf-8"))
    assert imported["status"] == "proposed"
    assert imported["source"]["kind"] == "import"
    assert len(load_learning_events([Path("ledger/proposed")])) == 1


def test_import_learning_event_dedupes_by_event_id(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    source = Path(__file__).resolve().parents[1] / _fixture("safe-engineering-event.json")
    first = import_learning_events([source])
    second = import_learning_events([source])
    assert first[0]["status"] == "imported"
    assert second[0]["status"] == "skipped"
    assert second[0]["reason"] == "duplicate"


def test_import_learning_event_rejects_unsafe_fixture(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    source = Path(__file__).resolve().parents[1] / _fixture("unsafe-engineering-event.json")
    with pytest.raises(Exception) as exc:
        import_learning_events([source])
    assert "forbidden" in str(exc.value)


def test_promote_pr_writes_review_target_and_pr_body(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    fixture_root = Path(__file__).resolve().parents[1] / "ledger/fixtures/03-noc_shadow_eval_summary.json"
    target_fixture = tmp_path / "ledger/fixtures/03-noc_shadow_eval_summary.json"
    target_fixture.parent.mkdir(parents=True)
    target_fixture.write_text(fixture_root.read_text(encoding="utf-8"), encoding="utf-8")
    result = promote_learning_event_for_pr(
        "noc_shadow:fixture-shadow-eval-summary",
        reviewer="svag",
        promotion_kind="summary",
        rationale="Reviewed for PR helper test.",
    )
    assert result.wrote
    assert result.review_path.exists()
    assert result.target_path is not None and result.target_path.exists()
    assert Path("reports/learning-promotion-pr.md").exists()
    body = build_promotion_pr_body(result)
    assert "Learning event promotion PR" in body
    assert "No raw logs" in body


def test_lifecycle_detects_missing_approved_target(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    source = Path(__file__).resolve().parents[1] / "ledger/fixtures/03-noc_shadow_eval_summary.json"
    fixture = tmp_path / "ledger/fixtures/03-noc_shadow_eval_summary.json"
    fixture.parent.mkdir(parents=True)
    fixture.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    result = promote_learning_event(
        "noc_shadow:fixture-shadow-eval-summary",
        reviewer="svag",
        promotion_kind="summary",
        rationale="Reviewed for missing target test.",
    )
    assert result.target_path is not None
    result.target_path.unlink()
    report = analyze_learning_lifecycle()
    assert report["summary"]["critical_count"] == 1
    assert lifecycle_check()


def test_lifecycle_report_counts_rejections(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    source = Path(__file__).resolve().parents[1] / "ledger/fixtures/04-eval_run_summary.json"
    fixture = tmp_path / "ledger/fixtures/04-eval_run_summary.json"
    fixture.parent.mkdir(parents=True)
    fixture.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    promote_learning_event(
        "knowledge:baseline-evals",
        reviewer="svag",
        promotion_kind="summary",
        decision="rejected",
        rationale="Rejected in lifecycle test.",
    )
    report = write_learning_lifecycle_reports()
    assert report["summary"]["rejected_count"] == 1
    assert report["summary"]["critical_count"] == 0
    assert Path("reports/learning-lifecycle.md").exists()
