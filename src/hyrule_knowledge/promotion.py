"""Human-reviewed promotion of learning events into curated OKF."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

import yaml

from .contracts import stable_hash, utc_now_iso
from .learning_ledger import load_learning_events, validate_learning_event
from .models import Concept, SourceRef
from .okf_writer import dump_concept, slugify

PromotionDecision = Literal["approved", "rejected"]
PromotionKind = Literal["lesson", "summary"]

REVIEWS_DIR = Path("ledger/reviews")
CURATED_LESSONS_DIR = Path("okf/curated/lessons")
CURATED_SUMMARIES_DIR = Path("okf/curated/summaries")
PROMOTION_PR_MD = Path("reports/learning-promotion-pr.md")
LIFECYCLE_JSON = Path("reports/learning-lifecycle.json")
LIFECYCLE_MD = Path("reports/learning-lifecycle.md")


class LearningPromotionError(RuntimeError):
    """Raised when a learning event cannot be promoted."""


@dataclass(frozen=True)
class PromotionResult:
    event_id: str
    decision: PromotionDecision
    promotion_kind: PromotionKind
    reviewer: str
    review_id: str
    review_path: Path
    target_concept_id: str | None
    target_path: Path | None
    wrote: bool
    review_record: dict[str, Any]
    concept_markdown: str | None = None

    def as_json(self) -> dict[str, Any]:
        return {
            "event_id": self.event_id,
            "decision": self.decision,
            "promotion_kind": self.promotion_kind,
            "reviewer": self.reviewer,
            "review_id": self.review_id,
            "review_path": self.review_path.as_posix(),
            "target_concept_id": self.target_concept_id,
            "target_path": self.target_path.as_posix() if self.target_path else None,
            "wrote": self.wrote,
            "review_record": self.review_record,
            "concept_markdown": self.concept_markdown,
        }


def find_learning_event(reference: str, *, paths: list[Path] | None = None) -> dict[str, Any]:
    events = load_learning_events(paths)
    for event in events:
        candidates = {
            str(event.get("id")),
            str(event.get("subject")),
            slugify(str(event.get("subject") or "")),
            slugify(str(event.get("summary") or ""))[:80],
        }
        raw_source = event.get("source")
        source: dict[str, Any] = raw_source if isinstance(raw_source, dict) else {}
        if source.get("path"):
            candidates.add(Path(str(source["path"])).stem)
        if reference in candidates:
            return event
    raise LearningPromotionError(f"learning event not found: {reference}")


def build_review_packet(reference: str, *, paths: list[Path] | None = None, promotion_kind: PromotionKind = "summary") -> dict[str, Any]:
    event = find_learning_event(reference, paths=paths)
    errors = validate_learning_event(event)
    evidence = _event_evidence(event)
    blockers = list(errors)
    if not evidence:
        blockers.append("event has no promotable citations/context/eval evidence")
    target = _target_for_event(event, promotion_kind)
    concept = build_promoted_concept(
        event,
        reviewer="<reviewer>",
        promotion_kind=promotion_kind,
        rationale="<human review rationale>",
        reviewed_at="<reviewed_at>",
    )
    return {
        "event": _safe_event_summary(event),
        "validation_errors": errors,
        "promotion_blockers": blockers,
        "suggested_target": target,
        "source_refs": [ref.as_frontmatter() for ref in _source_refs_from_event(event)],
        "preview": {
            "concept_id": concept.concept_id,
            "type": concept.concept_type,
            "authority_tier": "A2" if promotion_kind == "summary" else "A1",
            "title": concept.title,
            "body_excerpt": concept.body[:1200],
        },
    }


def promote_learning_event_for_pr(
    reference: str,
    *,
    reviewer: str,
    promotion_kind: PromotionKind,
    decision: PromotionDecision = "approved",
    rationale: str = "Reviewed and accepted for curated OKF promotion.",
    paths: list[Path] | None = None,
    dry_run: bool = False,
) -> PromotionResult:
    result = promote_learning_event(
        reference,
        reviewer=reviewer,
        promotion_kind=promotion_kind,
        decision=decision,
        rationale=rationale,
        paths=paths,
        dry_run=dry_run,
    )
    body = build_promotion_pr_body(result)
    if not dry_run:
        PROMOTION_PR_MD.parent.mkdir(parents=True, exist_ok=True)
        PROMOTION_PR_MD.write_text(body, encoding="utf-8")
    return result


def build_promotion_pr_body(result: PromotionResult) -> str:
    target = result.target_path.as_posix() if result.target_path else "none"
    lines = [
        "# Learning event promotion PR",
        "",
        f"* Event: `{result.event_id}`",
        f"* Decision: `{result.decision}`",
        f"* Promotion kind: `{result.promotion_kind}`",
        f"* Reviewer: `{result.reviewer}`",
        f"* Review record: `{result.review_path.as_posix()}`",
        f"* Curated target: `{target}`",
        "",
        "## Checklist",
        "",
        "- [ ] Human reviewer identity is correct.",
        "- [ ] Rationale explains why the event is worth promoting.",
        "- [ ] Source refs/citations are preserved.",
        "- [ ] No raw logs, packet captures, command output, credentials, or secrets are included.",
        "- [ ] A0 source truth remains authoritative if conflicts are discovered.",
        "- [ ] `uv run hyrule-knowledge validate okf` passes.",
        "- [ ] `uv run hyrule-knowledge eval --check` passes.",
        "- [ ] `uv run hyrule-knowledge ledger lifecycle --check` passes.",
        "",
    ]
    return "\n".join(lines)


def promote_learning_event(
    reference: str,
    *,
    reviewer: str,
    promotion_kind: PromotionKind,
    decision: PromotionDecision = "approved",
    rationale: str = "Reviewed and accepted for curated OKF promotion.",
    paths: list[Path] | None = None,
    dry_run: bool = False,
) -> PromotionResult:
    if not reviewer.strip():
        raise LearningPromotionError("--reviewer is required for human-reviewed promotion")
    event = find_learning_event(reference, paths=paths)
    validation_errors = validate_learning_event(event)
    if validation_errors:
        raise LearningPromotionError("event failed validation: " + "; ".join(validation_errors))
    if decision == "approved" and not _event_evidence(event):
        raise LearningPromotionError("approved promotions require citations, context-pack IDs, policy IDs, or eval-case IDs")
    reviewed_at = utc_now_iso()
    target_concept: Concept | None = None
    concept_markdown: str | None = None
    target_path: Path | None = None
    if decision == "approved":
        target_concept = build_promoted_concept(
            event,
            reviewer=reviewer,
            promotion_kind=promotion_kind,
            rationale=rationale,
            reviewed_at=reviewed_at,
        )
        concept_markdown = dump_concept(target_concept)
        target_path = target_concept.path
    review_id = stable_hash("review", [event.get("id"), decision, promotion_kind, reviewer, rationale])
    review_path = REVIEWS_DIR / f"{review_id}.json"
    review_record: dict[str, Any] = {
        "id": review_id,
        "ledger_version": str(event.get("ledger_version")),
        "event_id": str(event.get("id")),
        "event_type": str(event.get("event_type")),
        "decision": decision,
        "promotion_kind": promotion_kind,
        "reviewer": reviewer,
        "reviewed_at": reviewed_at,
        "rationale": rationale,
        "target_concept_id": target_concept.concept_id if target_concept else None,
        "target_path": target_path.as_posix() if target_path else None,
        "authority_tier_after_promotion": "A2" if promotion_kind == "summary" and decision == "approved" else "A1" if decision == "approved" else None,
        "event_hash": stable_hash("event", event),
        "validation_errors": validation_errors,
        "source_refs": [ref.as_frontmatter() for ref in _source_refs_from_event(event)],
    }
    if not dry_run:
        REVIEWS_DIR.mkdir(parents=True, exist_ok=True)
        review_path.write_text(json.dumps(review_record, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        if target_path and concept_markdown:
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(concept_markdown, encoding="utf-8")
    return PromotionResult(
        event_id=str(event["id"]),
        decision=decision,
        promotion_kind=promotion_kind,
        reviewer=reviewer,
        review_id=review_id,
        review_path=review_path,
        target_concept_id=target_concept.concept_id if target_concept else None,
        target_path=target_path,
        wrote=not dry_run,
        review_record=review_record,
        concept_markdown=concept_markdown,
    )


def load_learning_reviews() -> list[dict[str, Any]]:
    reviews: list[dict[str, Any]] = []
    for path in sorted(REVIEWS_DIR.glob("*.json")):
        loaded = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(loaded, dict):
            reviews.append({"path": path.as_posix(), **loaded})
    return reviews


def analyze_learning_lifecycle(*, paths: list[Path] | None = None) -> dict[str, Any]:
    events = {str(event["id"]): event for event in load_learning_events(paths)}
    reviews = load_learning_reviews()
    findings: list[dict[str, Any]] = []
    reviews_by_event: dict[str, list[dict[str, Any]]] = {}
    for review in reviews:
        reviews_by_event.setdefault(str(review.get("event_id")), []).append(review)
    for event_id, event in events.items():
        if event.get("status") in {"fixture", "proposed"} and event_id not in reviews_by_event:
            findings.append({"severity": "info", "code": "needs_review", "event_id": event_id, "message": "learning event has not been reviewed"})
    for review in reviews:
        event_id = str(review.get("event_id"))
        reviewed_event = events.get(event_id)
        if reviewed_event is None:
            findings.append({"severity": "warning", "code": "review_event_missing", "event_id": event_id, "review_id": review.get("id"), "message": "review references a learning event that is not present"})
            continue
        current_hash = stable_hash("event", reviewed_event)
        if review.get("event_hash") != current_hash:
            findings.append({"severity": "warning", "code": "needs_re_review", "event_id": event_id, "review_id": review.get("id"), "message": "learning event changed after review"})
        if review.get("decision") == "approved":
            target_path = Path(str(review.get("target_path") or ""))
            if not target_path.exists():
                findings.append({"severity": "critical", "code": "approved_target_missing", "event_id": event_id, "review_id": review.get("id"), "message": f"approved target is missing: {target_path}"})
            else:
                frontmatter = _read_markdown_frontmatter(target_path)
                if frontmatter.get("review_status") != "reviewed":
                    findings.append({"severity": "warning", "code": "target_not_reviewed", "event_id": event_id, "review_id": review.get("id"), "message": "approved target does not have review_status=reviewed"})
                if frontmatter.get("learning_event_id") != event_id:
                    findings.append({"severity": "warning", "code": "target_event_mismatch", "event_id": event_id, "review_id": review.get("id"), "message": "approved target learning_event_id does not match review"})
    for event_id, event_reviews in reviews_by_event.items():
        approved = [review for review in event_reviews if review.get("decision") == "approved"]
        if len(approved) > 1:
            findings.append({"severity": "warning", "code": "duplicate_approved_promotions", "event_id": event_id, "message": "multiple approved promotions exist for one event; consider superseding older summaries"})
    summary = {
        "event_count": len(events),
        "review_count": len(reviews),
        "approved_count": sum(1 for review in reviews if review.get("decision") == "approved"),
        "rejected_count": sum(1 for review in reviews if review.get("decision") == "rejected"),
        "needs_review_count": sum(1 for finding in findings if finding["code"] == "needs_review"),
        "needs_re_review_count": sum(1 for finding in findings if finding["code"] == "needs_re_review"),
        "critical_count": sum(1 for finding in findings if finding["severity"] == "critical"),
        "warning_count": sum(1 for finding in findings if finding["severity"] == "warning"),
    }
    return {"summary": summary, "findings": findings}


def write_learning_lifecycle_reports(*, paths: list[Path] | None = None) -> dict[str, Any]:
    report = analyze_learning_lifecycle(paths=paths)
    LIFECYCLE_JSON.parent.mkdir(parents=True, exist_ok=True)
    LIFECYCLE_JSON.write_text(json.dumps(report, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Learning lifecycle report",
        "",
        f"* Events: **{report['summary']['event_count']}**",
        f"* Reviews: **{report['summary']['review_count']}**",
        f"* Approved: **{report['summary']['approved_count']}**",
        f"* Rejected: **{report['summary']['rejected_count']}**",
        f"* Needs review: **{report['summary']['needs_review_count']}**",
        f"* Needs re-review: **{report['summary']['needs_re_review_count']}**",
        f"* Critical findings: **{report['summary']['critical_count']}**",
        "",
    ]
    if report["findings"]:
        lines.append("## Findings")
        for finding in report["findings"]:
            lines.append(f"* `{finding['severity']}` `{finding['code']}` `{finding.get('event_id', '')}` — {finding['message']}")
    else:
        lines.append("No lifecycle findings.")
    LIFECYCLE_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report


def lifecycle_check(*, paths: list[Path] | None = None) -> list[str]:
    report = analyze_learning_lifecycle(paths=paths)
    return [f"{finding.get('event_id', '')}: {finding['message']}" for finding in report["findings"] if finding["severity"] == "critical"]


def _read_markdown_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    try:
        _, raw, _ = text.split("---", 2)
    except ValueError:
        return {}
    loaded = yaml.safe_load(raw) or {}
    return loaded if isinstance(loaded, dict) else {}


def build_promoted_concept(
    event: dict[str, Any],
    *,
    reviewer: str,
    promotion_kind: PromotionKind,
    rationale: str,
    reviewed_at: str,
) -> Concept:
    subject_slug = slugify(str(event.get("subject") or event.get("id") or "learning-event"))
    event_type = str(event.get("event_type") or "learning_event")
    title_subject = str(event.get("subject") or event.get("summary") or event.get("id"))
    if promotion_kind == "lesson":
        concept_id = f"curated/lessons/{subject_slug}"
        concept_type = "Lesson"
        title = f"Lesson: {_title_text(title_subject)}"
        description = "Human-reviewed lesson promoted from a sanitized learning event."
        authority_tier = "A1"
    else:
        concept_id = f"curated/summaries/{subject_slug}"
        concept_type = "Learning Summary"
        title = f"Learning Summary: {_title_text(title_subject)}"
        description = "Human-reviewed A2 summary promoted from a sanitized learning event."
        authority_tier = "A2"
    return Concept(
        concept_id=concept_id,
        concept_type=concept_type,
        title=title,
        description=description,
        body=_promoted_body(event, reviewer=reviewer, rationale=rationale, promotion_kind=promotion_kind, authority_tier=authority_tier),
        tags=["learning-ledger", "human-reviewed", event_type, promotion_kind],
        truth_owner="okf",
        authority="canonical",
        source_refs=_source_refs_from_event(event),
        last_verified_at=reviewed_at if reviewed_at != "<reviewed_at>" else None,
        confidence="medium",
        dispute_policy="adjudicate",
        review_status="reviewed" if reviewer != "<reviewer>" else "review-required",
        extra={
            "learning_event_id": event.get("id"),
            "learning_event_type": event.get("event_type"),
            "learning_event_subject": event.get("subject"),
            "reviewed_by": reviewer,
            "reviewed_at": reviewed_at if reviewed_at != "<reviewed_at>" else None,
            "promotion_kind": promotion_kind,
            "authority_tier": authority_tier,
        },
    )


def validate_promoted_concept_markdown(markdown: str, *, expected_tier: str) -> list[str]:
    errors: list[str] = []
    if not markdown.startswith("---\n"):
        return ["promoted concept must have YAML frontmatter"]
    try:
        _, raw_fm, body = markdown.split("---", 2)
        frontmatter = yaml.safe_load(raw_fm) or {}
    except (ValueError, yaml.YAMLError) as exc:
        return [f"invalid promoted concept frontmatter: {exc}"]
    if not isinstance(frontmatter, dict):
        return ["promoted concept frontmatter must be a mapping"]
    if frontmatter.get("truth_owner") != "okf":
        errors.append("promoted concept truth_owner must be okf")
    if frontmatter.get("authority") != "canonical":
        errors.append("promoted concept authority must be canonical")
    if frontmatter.get("review_status") != "reviewed":
        errors.append("promoted concept review_status must be reviewed")
    if frontmatter.get("authority_tier") != expected_tier:
        errors.append(f"promoted concept authority_tier must be {expected_tier}")
    if not frontmatter.get("reviewed_by"):
        errors.append("promoted concept must include reviewed_by")
    if not frontmatter.get("source_refs"):
        errors.append("promoted concept must preserve source_refs")
    if "## Evidence" not in body:
        errors.append("promoted concept must include an Evidence section")
    if "raw_log" in markdown or "packet_capture" in markdown or "Bearer " in markdown:
        errors.append("promoted concept includes forbidden raw/sensitive markers")
    return errors


def _target_for_event(event: dict[str, Any], promotion_kind: PromotionKind) -> dict[str, Any]:
    concept = build_promoted_concept(
        event,
        reviewer="<reviewer>",
        promotion_kind=promotion_kind,
        rationale="<human review rationale>",
        reviewed_at="<reviewed_at>",
    )
    return {
        "promotion_kind": promotion_kind,
        "concept_id": concept.concept_id,
        "path": concept.path.as_posix(),
        "authority_tier": "A2" if promotion_kind == "summary" else "A1",
    }


def _safe_event_summary(event: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": event.get("id"),
        "event_type": event.get("event_type"),
        "producer": event.get("producer"),
        "subject": event.get("subject"),
        "summary": event.get("summary"),
        "status": event.get("status"),
        "authority_tier": event.get("authority_tier"),
        "citation_count": len(event.get("citations", [])) if isinstance(event.get("citations"), list) else 0,
        "lesson_count": len(event.get("lessons", [])) if isinstance(event.get("lessons"), list) else 0,
    }


def _event_evidence(event: dict[str, Any]) -> list[Any]:
    evidence: list[Any] = []
    for key in ("citations", "context_pack_ids", "policy_decision_ids", "eval_case_ids"):
        value = event.get(key)
        if isinstance(value, list):
            evidence.extend(value)
    return evidence


def _source_refs_from_event(event: dict[str, Any]) -> list[SourceRef]:
    refs: list[SourceRef] = []
    raw_citations = event.get("citations")
    citations: list[Any] = raw_citations if isinstance(raw_citations, list) else []
    for citation in citations:
        if not isinstance(citation, dict):
            continue
        source_uri = citation.get("source_uri")
        if isinstance(source_uri, str) and source_uri.startswith("repo://"):
            refs.append(_repo_source_ref(source_uri))
        elif source_uri:
            refs.append(SourceRef(url=str(source_uri)))
        if citation.get("concept_id"):
            refs.append(SourceRef(url=f"okf://{citation['concept_id']}"))
        if citation.get("claim_id"):
            refs.append(SourceRef(url=f"claim://{citation['claim_id']}"))
        if citation.get("context_pack_id"):
            refs.append(SourceRef(url=f"context-pack://{citation['context_pack_id']}"))
    for key, prefix in (("context_pack_ids", "context-pack"), ("policy_decision_ids", "policy"), ("eval_case_ids", "eval-case")):
        values = event.get(key)
        if isinstance(values, list):
            for value in values:
                refs.append(SourceRef(url=f"{prefix}://{value}"))
    unique: dict[tuple[str | None, str | None, str | None, str | None, str | None], SourceRef] = {}
    for ref in refs:
        key_tuple = (ref.repo, ref.path, ref.commit, ref.lines, ref.url)
        unique[key_tuple] = ref
    return list(unique.values()) or [SourceRef(url=f"learning-event://{event.get('id')}")]


def _repo_source_ref(source_uri: str) -> SourceRef:
    raw = source_uri.removeprefix("repo://")
    before_commit, sep, commit = raw.partition("@")
    before_lines, _, lines = before_commit.partition("#L")
    parts = before_lines.split("/", 2)
    if len(parts) < 3:
        return SourceRef(url=source_uri)
    owner, repo_name, path = parts
    return SourceRef(repo=f"{owner}/{repo_name}", path=path, commit=commit if sep else None, lines=lines.replace("-L", "-") if lines else None)


def _title_text(value: str) -> str:
    text = value.replace(":", " ").replace("-", " ").strip()
    return " ".join(word.capitalize() for word in text.split())[:90]


def _promoted_body(event: dict[str, Any], *, reviewer: str, rationale: str, promotion_kind: PromotionKind, authority_tier: str) -> str:
    lessons = event.get("lessons") if isinstance(event.get("lessons"), list) else []
    metrics = event.get("metrics") if isinstance(event.get("metrics"), dict) else {}
    lines = [
        f"# Human-reviewed {promotion_kind}",
        "",
        f"This page promotes sanitized learning event `{event.get('id')}` into reviewed OKF knowledge.",
        "",
        "## Review",
        "",
        f"- Reviewer: `{reviewer}`",
        f"- Promotion kind: `{promotion_kind}`",
        f"- Authority tier after promotion: `{authority_tier}`",
        f"- Rationale: {rationale}",
        "",
        "## Summary",
        "",
        str(event.get("summary") or "No summary supplied."),
        "",
        "## Lessons",
        "",
    ]
    if lessons:
        lines.extend(f"- {lesson}" for lesson in lessons)
    else:
        lines.append("- No standalone lesson text was supplied; retain this page as a reviewed summary.")
    lines.extend(["", "## Metrics", ""])
    if metrics:
        for key, value in sorted(metrics.items()):
            lines.append(f"- `{key}`: `{value}`")
    else:
        lines.append("- No metrics supplied.")
    lines.extend(["", "## Evidence", ""])
    for ref in _source_refs_from_event(event):
        fm = ref.as_frontmatter()
        if fm.get("repo") and fm.get("path"):
            commit = f"@{fm['commit']}" if fm.get("commit") else ""
            lines.append(f"- `{fm['repo']}/{fm['path']}{commit}`")
        elif fm.get("url"):
            lines.append(f"- `{fm['url']}`")
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- This is a human-reviewed learning artifact, not a replacement for A0 source truth.",
            "- If this page conflicts with cited source repositories, the source repositories win and this page is stale.",
            "- Raw logs, command output, packet captures, credentials, and secrets are intentionally excluded.",
            "",
        ]
    )
    return "\n".join(lines)
