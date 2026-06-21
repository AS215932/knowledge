from __future__ import annotations

import json

from hyrule_knowledge.claims import compile_claims


def _observation_concept() -> dict[str, object]:
    payload = {"sources": {"icinga": {"status": "ok"}}}
    return {
        "id": "observed/latest/example",
        "type": "Observation",
        "source_refs": [{"url": "manual://example"}],
        "frontmatter": {
            "expires_at": "2026-01-02T00:00:00Z",
            "payload_json": json.dumps(payload, sort_keys=True),
        },
        "expires_at": "2026-01-02T00:00:00Z",
        "payload_json": json.dumps(payload, sort_keys=True),
    }


def test_observation_freshness_uses_extracted_at_not_wall_clock() -> None:
    current_claims = compile_claims(
        [_observation_concept()],
        [],
        extracted_at="2026-01-01T00:00:00Z",
    )
    expired_claims = compile_claims(
        [_observation_concept()],
        [],
        extracted_at="2026-01-03T00:00:00Z",
    )

    assert {claim.freshness_status for claim in current_claims} == {"current"}
    assert {claim.freshness_status for claim in expired_claims} == {"expired"}
    assert {claim.id for claim in current_claims} == {claim.id for claim in expired_claims}
