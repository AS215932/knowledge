"""Authority tiers and source-of-truth ordering for AS215932 knowledge."""

from __future__ import annotations

from enum import StrEnum
from typing import Any


class AuthorityTier(StrEnum):
    """Ordered authority tiers used by the learning control plane."""

    A0 = "A0"  # hard source of truth
    A1 = "A1"  # reviewed OKF institutional knowledge
    A2 = "A2"  # reviewed trace/promotion summaries
    A3 = "A3"  # observed evidence
    A4 = "A4"  # proposed/advisory/agent-generated
    A5 = "A5"  # similarity hints only


_TIER_RANK = {
    AuthorityTier.A0: 0,
    AuthorityTier.A1: 1,
    AuthorityTier.A2: 2,
    AuthorityTier.A3: 3,
    AuthorityTier.A4: 4,
    AuthorityTier.A5: 5,
}


def tier_rank(tier: AuthorityTier | str) -> int:
    """Return lower-is-stronger rank for an authority tier."""
    return _TIER_RANK[AuthorityTier(str(tier))]


def tier_allows(candidate: AuthorityTier | str, minimum: AuthorityTier | str) -> bool:
    """Return True when candidate is at least as authoritative as minimum."""
    return tier_rank(candidate) <= tier_rank(minimum)


def weaker_tier(left: AuthorityTier | str, right: AuthorityTier | str) -> AuthorityTier:
    """Return the weaker/lower-authority tier of two tiers."""
    return AuthorityTier(str(left)) if tier_rank(left) >= tier_rank(right) else AuthorityTier(str(right))


def stronger_tier(left: AuthorityTier | str, right: AuthorityTier | str) -> AuthorityTier:
    """Return the stronger/higher-authority tier of two tiers."""
    return AuthorityTier(str(left)) if tier_rank(left) <= tier_rank(right) else AuthorityTier(str(right))


def authority_from_concept(concept: dict[str, Any]) -> AuthorityTier:
    """Map an OKF concept/export row to an authority tier.

    Generated concepts are derivative files, but repo-owned generated concepts
    may emit A0 claims because their claims point back to repo source refs.
    Proposed curated/enriched knowledge remains A4 until reviewed.
    """
    concept_id = str(concept.get("id") or "")
    concept_type = str(concept.get("type") or "")
    truth_owner = str(concept.get("truth_owner") or "")
    authority = str(concept.get("authority") or "")
    review_status = str(concept.get("review_status") or "")
    source_refs = concept.get("source_refs") or []

    if concept_id.startswith("observed/") or truth_owner == "observed" or authority == "evidence":
        return AuthorityTier.A3
    if concept_id.startswith("generated/enriched/") or concept_type in {"Reference", "Hypothesis"}:
        return AuthorityTier.A4
    if truth_owner == "repo" and source_refs:
        return AuthorityTier.A0
    if truth_owner == "derived" and source_refs and authority == "canonical":
        return AuthorityTier.A0
    if truth_owner == "okf" and authority == "canonical" and review_status in {
        "reviewed",
        "approved",
        "accepted",
        "canonical",
    }:
        return AuthorityTier.A1
    if truth_owner == "okf" and review_status in {"reviewed", "approved", "accepted"}:
        return AuthorityTier.A1
    if truth_owner == "external" and source_refs:
        return AuthorityTier.A2
    return AuthorityTier.A4


def concept_authority_map(concepts: list[dict[str, Any]]) -> dict[str, AuthorityTier]:
    """Return authority tier by concept id."""
    return {str(concept["id"]): authority_from_concept(concept) for concept in concepts}
