from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

from hyrule_knowledge.extractors.ansible import extract_hosts
from hyrule_knowledge.extractors.api import extract_api
from hyrule_knowledge.extractors.workflows import extract_workflows
from hyrule_knowledge.llm import LLMError, validate_enrichment_json
from hyrule_knowledge.models import RepoSnapshot
from hyrule_knowledge.observe import collect_safe_health
from hyrule_knowledge.quality import evaluate_quality


def _git_repo(path: Path) -> None:
    subprocess.run(["git", "init", "-b", "main"], cwd=path, check=True, stdout=subprocess.DEVNULL)
    subprocess.run(["git", "add", "."], cwd=path, check=True, stdout=subprocess.DEVNULL)


def _snapshot(path: Path, name: str = "demo") -> RepoSnapshot:
    return RepoSnapshot(
        repo=f"AS215932/{name}",
        owner="AS215932",
        name=name,
        path=path,
        commit="0" * 40,
        default_branch="main",
        url=f"https://github.com/AS215932/{name}",
        description="demo repo",
        is_private=False,
        primary_language="Python",
        topics=[],
        files=[],
    )


def test_fastapi_and_pydantic_extraction(tmp_path: Path) -> None:
    (tmp_path / "app.py").write_text(
        '''from fastapi import APIRouter, Depends, HTTPException\nfrom pydantic import BaseModel, Field\n\nrouter = APIRouter(prefix="/v1")\n\nclass WidgetRequest(BaseModel):\n    name: str = Field(..., description="Widget name")\n\n@router.post("/widgets", response_model=WidgetRequest, status_code=201)\nasync def create_widget(body: WidgetRequest, dep = Depends(object)) -> WidgetRequest:\n    """Create a widget."""\n    raise HTTPException(409, "exists")\n''',
        encoding="utf-8",
    )
    _git_repo(tmp_path)
    endpoints, models = extract_api(_snapshot(tmp_path))
    assert endpoints[0].method == "POST"
    assert endpoints[0].route == "/v1/widgets"
    assert endpoints[0].request_models == ["WidgetRequest"]
    assert 409 in endpoints[0].status_codes
    assert models[0].name == "WidgetRequest"
    assert models[0].fields[0].name == "name"


def test_workflow_extraction(tmp_path: Path) -> None:
    workflow = tmp_path / ".github/workflows/deploy.yml"
    workflow.parent.mkdir(parents=True)
    workflow.write_text(
        """name: deploy\non: [workflow_dispatch]\npermissions:\n  contents: read\njobs:\n  deploy:\n    runs-on: [self-hosted, hyrule]\n    environment: production\n    steps:\n      - run: echo ${{ secrets.DEPLOY_KEY }}\n""",
        encoding="utf-8",
    )
    _git_repo(tmp_path)
    snap = _snapshot(tmp_path)
    snap.files = [".github/workflows/deploy.yml"]
    workflows = extract_workflows(snap)
    assert workflows[0].deploy_like is True
    assert workflows[0].secrets == ["DEPLOY_KEY"]
    assert workflows[0].jobs[0].environment == "production"


def test_ansible_host_extraction(tmp_path: Path) -> None:
    inv = tmp_path / "ansible/inventory"
    (inv / "host_vars").mkdir(parents=True)
    (inv / "group_vars").mkdir(parents=True)
    (inv / "hosts.yml").write_text(
        """all:\n  children:\n    routers:\n      hosts:\n        rtr:\n          ansible_host: 2001:db8::1\n""",
        encoding="utf-8",
    )
    (inv / "group_vars/all.yml").write_text("peers:\n  rtr:\n    ipv6: 2001:db8::1\n", encoding="utf-8")
    (inv / "host_vars/rtr.yml").write_text(
        """---\n# rtr — router\nfirewall_extra_rules:\n  - { proto: tcp, dport: 179, src: any, comment: bgp }\nmonitoring_role: router\nlogs_role: rtr\n""",
        encoding="utf-8",
    )
    hosts = extract_hosts(_snapshot(tmp_path, "network-operations"))
    assert hosts[0].concept_type == "Router"
    assert hosts[0].firewall_rules[0].dport == 179
    assert hosts[0].logs_role == "rtr"


def test_observe_degraded_without_env(tmp_path: Path, monkeypatch) -> None:  # type: ignore[no-untyped-def]
    monkeypatch.delenv("PROMETHEUS_URL", raising=False)
    monkeypatch.delenv("ICINGA_API_BASE", raising=False)
    monkeypatch.delenv("HYRULE_MCP_HEALTH_URL", raising=False)
    root = tmp_path / "okf"
    path = collect_safe_health(root)
    assert path.exists()
    text = path.read_text(encoding="utf-8")
    assert "truth_owner: observed" in text
    assert "observation_status: degraded" in text


def test_quality_detects_missing_org(tmp_path: Path) -> None:
    root = tmp_path / "okf"
    exports = tmp_path / "exports"
    root.mkdir()
    exports.mkdir()
    (exports / "edges.jsonl").write_text("", encoding="utf-8")
    report, findings = evaluate_quality(root, exports)
    assert report["critical_count"] > 0
    assert any(finding.code == "missing_top_level" for finding in findings)


def test_quality_uses_latest_observed_at_for_telemetry_status(tmp_path: Path) -> None:
    root = tmp_path / "okf"
    latest = root / "observed/latest"
    latest.mkdir(parents=True)
    exports = tmp_path / "exports"
    exports.mkdir()
    (exports / "edges.jsonl").write_text("", encoding="utf-8")
    observation_rows = []
    for name, observed_at, source, status in [
        ("z-old", "2026-01-01T00:00:00Z", "old_source", "degraded"),
        ("a-new", "2026-01-02T00:00:00Z", "new_source", "ok"),
    ]:
        payload = {"observed_at": observed_at, "sources": {source: {"status": status}}}
        payload_json = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        observation_rows.append(
            {
                "concept_id": f"observed/latest/{name}",
                "observed_at": observed_at,
                "expires_at": "2026-01-03T00:00:00Z",
                "source": "test",
                "status": status,
                "payload_json": payload_json,
            }
        )
        (latest / f"{name}.md").write_text(
            "---\n"
            "type: Observation\n"
            f"title: {name}\n"
            "truth_owner: observed\n"
            "authority: evidence\n"
            "source_refs:\n"
            "- url: manual://test\n"
            f"last_verified_at: '{observed_at}'\n"
            "confidence: medium\n"
            "dispute_policy: evidence_only\n"
            f"observed_at: '{observed_at}'\n"
            "expires_at: '2026-01-03T00:00:00Z'\n"
            "collection_profile: test\n"
            "observation_source: test\n"
            f"observation_status: {status}\n"
            f"payload_json: '{payload_json}'\n"
            "---\n\n# Observation\n",
            encoding="utf-8",
        )
    (exports / "observations.jsonl").write_text(
        "".join(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n" for row in observation_rows),
        encoding="utf-8",
    )
    report, _ = evaluate_quality(root, exports)
    assert report["telemetry_source_status"] == {"new_source": "ok"}


def test_llm_enrichment_validation_rejects_missing_or_unknown_citations() -> None:
    valid = {
        "sections": [{"heading": "Summary", "body": "Supported.", "citations": ["generated/services/hyrule-cloud"]}],
        "claims": [{"text": "Supported claim.", "citations": ["AS215932/hyrule-cloud:README.md"]}],
    }
    validate_enrichment_json(valid, {"generated/services/hyrule-cloud", "AS215932/hyrule-cloud:README.md"})
    with pytest.raises(LLMError):
        validate_enrichment_json({"sections": [{"heading": "Bad", "body": "Unsupported.", "citations": []}]}, {"x"})
    with pytest.raises(LLMError):
        validate_enrichment_json({"sections": [{"heading": "Bad", "body": "Unsupported.", "citations": ["missing"]}]}, {"x"})


def test_llm_enrichment_validation_rejects_secret_like_output() -> None:
    with pytest.raises(LLMError):
        validate_enrichment_json(
            {"sections": [{"heading": "Bad", "body": "api_key = abc123", "citations": ["x"]}]},
            {"x"},
        )
