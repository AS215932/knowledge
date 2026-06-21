from __future__ import annotations

import json
from pathlib import Path

from hyrule_knowledge.exporter import exports_match, read_jsonl, write_exports


def _write_observation(root: Path) -> None:
    path = root / "observed/latest/example.md"
    path.parent.mkdir(parents=True)
    payload = {"sources": {"icinga": {"status": "ok"}}}
    payload_json = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    path.write_text(
        "---\n"
        "type: Observation\n"
        "title: Example observation\n"
        "truth_owner: observed\n"
        "authority: evidence\n"
        "source_refs:\n"
        "- url: manual://example\n"
        "last_verified_at: '2026-01-01T00:00:00Z'\n"
        "confidence: medium\n"
        "dispute_policy: evidence_only\n"
        "observed_at: '2026-01-01T00:00:00Z'\n"
        "expires_at: '2026-01-02T00:00:00Z'\n"
        "observation_source: manual-local\n"
        "observation_status: ok\n"
        f"payload_json: '{payload_json}'\n"
        "---\n\n"
        "# Example\n",
        encoding="utf-8",
    )


def test_write_exports_uses_run_timestamp_for_observation_freshness(tmp_path: Path) -> None:
    root = tmp_path / "okf"
    exports = tmp_path / "exports"
    _write_observation(root)

    write_exports(root, exports, edges=[], run_id="local-20260103000000")

    manifest = json.loads((exports / "manifest.json").read_text(encoding="utf-8"))
    claims = read_jsonl(exports / "claims.jsonl")
    assert manifest["claim_extracted_at"] == "2026-01-03T00:00:00Z"
    assert {claim["freshness_status"] for claim in claims} == {"expired"}
    assert exports_match(root, exports)
