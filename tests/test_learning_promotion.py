from __future__ import annotations

from pathlib import Path

import pytest

from hyrule_knowledge.authority import AuthorityTier, authority_from_concept
from hyrule_knowledge.claims import compile_claims
from hyrule_knowledge.promotion import (
    LearningPromotionError,
    build_promoted_concept,
    build_review_packet,
    find_learning_event,
    promote_learning_event,
    validate_promoted_concept_markdown,
)


def test_review_packet_has_blocker_free_summary_preview() -> None:
    event = find_learning_event("engineering_loop:fixture-run-summary")
    packet = build_review_packet(str(event["id"]), promotion_kind="summary")
    assert packet["promotion_blockers"] == []
    assert packet["preview"]["authority_tier"] == "A2"
    assert packet["suggested_target"]["path"].startswith("okf/curated/summaries/")


def test_promote_learning_event_dry_run_summary_is_a2() -> None:
    event = find_learning_event("noc_shadow:fixture-shadow-eval-summary")
    result = promote_learning_event(
        str(event["id"]),
        reviewer="svag",
        promotion_kind="summary",
        rationale="Reviewed fixture for deterministic promotion workflow test.",
        dry_run=True,
    )
    assert result.wrote is False
    assert result.target_concept_id is not None
    assert result.target_concept_id.startswith("curated/summaries/")
    assert result.concept_markdown is not None
    assert validate_promoted_concept_markdown(result.concept_markdown, expected_tier="A2") == []


def test_promoted_lesson_is_reviewed_okf_a1() -> None:
    event = find_learning_event("engineering_loop:fixture-context-pack-consumption")
    concept = build_promoted_concept(
        event,
        reviewer="svag",
        promotion_kind="lesson",
        rationale="Reviewed lesson promotion.",
        reviewed_at="2026-06-17T00:00:00Z",
    )
    assert concept.concept_type == "Lesson"
    row = {"id": concept.concept_id, **concept.frontmatter(), "source_refs": [ref.as_frontmatter() for ref in concept.source_refs]}
    assert authority_from_concept(row) == AuthorityTier.A1
    claims = compile_claims([{**row, "body": concept.body, "frontmatter": concept.frontmatter()}], [], extracted_at="2026-06-17T00:00:00Z")
    assert any(claim.predicate == "promoted_to_lesson" for claim in claims)


def test_promoted_summary_claims_are_a2() -> None:
    event = find_learning_event("noc_shadow:fixture-shadow-eval-summary")
    concept = build_promoted_concept(
        event,
        reviewer="svag",
        promotion_kind="summary",
        rationale="Reviewed summary promotion.",
        reviewed_at="2026-06-17T00:00:00Z",
    )
    row = {"id": concept.concept_id, **concept.frontmatter(), "source_refs": [ref.as_frontmatter() for ref in concept.source_refs], "body": concept.body, "frontmatter": concept.frontmatter()}
    assert authority_from_concept(row) == AuthorityTier.A2
    claims = compile_claims([row], [], extracted_at="2026-06-17T00:00:00Z")
    assert claims
    assert all(str(claim.authority_tier) == "A2" for claim in claims)


def test_promotion_requires_reviewer() -> None:
    event = find_learning_event("knowledge:baseline-evals")
    with pytest.raises(LearningPromotionError):
        promote_learning_event(str(event["id"]), reviewer="", promotion_kind="summary", dry_run=True)


def test_promotion_can_write_review_record_and_curated_concept(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    (tmp_path / "ledger/fixtures").mkdir(parents=True)
    source = Path(__file__).resolve().parents[1] / "ledger/fixtures/03-noc_shadow_eval_summary.json"
    (tmp_path / "ledger/fixtures/03-noc_shadow_eval_summary.json").write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    result = promote_learning_event(
        "noc_shadow:fixture-shadow-eval-summary",
        reviewer="svag",
        promotion_kind="summary",
        rationale="Reviewed in isolated write test.",
        dry_run=False,
    )
    assert result.review_path.exists()
    assert result.target_path is not None and result.target_path.exists()
    assert "reviewed_by: svag" in result.target_path.read_text(encoding="utf-8")
