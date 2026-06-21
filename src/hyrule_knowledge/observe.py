"""Manual safe-health observation ingestion."""

from __future__ import annotations

import base64
import json
import os
import urllib.error
import urllib.request
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

from .models import Concept, ObservationMetadata, SourceRef
from .okf_writer import dump_concept
from .validator import parse_frontmatter


def collect_safe_health(bundle_root: Path, profile: str = "safe-health") -> Path:
    observed_at_dt = datetime.now(UTC).replace(microsecond=0)
    observed_at = observed_at_dt.isoformat().replace("+00:00", "Z")
    expires_at = (observed_at_dt + timedelta(hours=24)).isoformat().replace("+00:00", "Z")
    sources: dict[str, dict[str, Any]] = {
        "prometheus": _prometheus_summary(),
        "icinga": _icinga_summary(),
        "hyrule_mcp": _mcp_summary(),
    }
    payload: dict[str, Any] = {
        "profile": profile,
        "observed_at": observed_at,
        "sources": sources,
    }
    status = "ok" if any(src.get("status") == "ok" for src in sources.values()) else "degraded"
    body = _observation_body(payload)
    concept = Concept(
        concept_id="observed/latest/safe-health",
        concept_type="Observation",
        title="Safe health observation snapshot",
        description="Manual/local safe-health snapshot for Prometheus, Icinga, and Hyrule MCP availability.",
        tags=["observed", "safe-health", "telemetry"],
        truth_owner="observed",
        authority="evidence",
        source_refs=[SourceRef(url="manual://safe-health")],
        last_verified_at=observed_at,
        confidence="medium" if status == "ok" else "low",
        dispute_policy="evidence_only",
        observation=ObservationMetadata(
            observed_at=observed_at,
            expires_at=expires_at,
            collection_profile=profile,
            source="manual-local",
            status=status,
        ),
        extra={"payload_json": json.dumps(payload, sort_keys=True)},
        body=body,
    )
    path = bundle_root.parent / concept.path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump_concept(concept), encoding="utf-8")
    _write_observed_indexes(bundle_root)
    return path


def _get_json(url: str, headers: dict[str, str] | None = None, timeout: int = 10) -> dict[str, Any]:
    request = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = response.read().decode("utf-8")
    parsed = json.loads(data)
    return parsed if isinstance(parsed, dict) else {"data": parsed}


def _prometheus_summary() -> dict[str, Any]:
    base = os.environ.get("PROMETHEUS_URL", "").rstrip("/")
    if not base:
        return {"status": "unavailable", "reason": "PROMETHEUS_URL not set"}
    try:
        up = _get_json(f"{base}/api/v1/query?query=up")
        result = up.get("data", {}).get("result", []) if isinstance(up.get("data"), dict) else []
        total = len(result) if isinstance(result, list) else 0
        down = 0
        if isinstance(result, list):
            for series in result:
                value = series.get("value") if isinstance(series, dict) else None
                if isinstance(value, list) and len(value) > 1 and str(value[1]) == "0":
                    down += 1
        return {"status": "ok", "up_series": total, "down_series": down}
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        return {"status": "unavailable", "reason": str(exc)}


def _icinga_summary() -> dict[str, Any]:
    base = os.environ.get("ICINGA_API_BASE", "").rstrip("/")
    user = os.environ.get("ICINGA_API_USER", "")
    password = os.environ.get("ICINGA_API_PASSWORD", "")
    if not base or not user or not password:
        return {"status": "unavailable", "reason": "ICINGA_API_BASE/USER/PASSWORD not fully set"}
    auth = base64.b64encode(f"{user}:{password}".encode()).decode("ascii")
    headers = {"authorization": f"Basic {auth}", "accept": "application/json"}
    try:
        hosts = _get_json(f"{base}/v1/objects/hosts?attrs=state&attrs=name", headers=headers)
        services = _get_json(f"{base}/v1/objects/services?attrs=state&attrs=name", headers=headers)
        host_results = hosts.get("results", []) if isinstance(hosts.get("results"), list) else []
        service_results = services.get("results", []) if isinstance(services.get("results"), list) else []
        return {
            "status": "ok",
            "host_count": len(host_results),
            "service_count": len(service_results),
            "problem_hosts": _icinga_problem_count(host_results),
            "problem_services": _icinga_problem_count(service_results),
        }
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        return {"status": "unavailable", "reason": str(exc)}


def _icinga_problem_count(results: list[Any]) -> int:
    count = 0
    for item in results:
        attrs = item.get("attrs") if isinstance(item, dict) else None
        state = attrs.get("state") if isinstance(attrs, dict) else None
        if isinstance(state, (int, float)) and state != 0:
            count += 1
    return count


def _mcp_summary() -> dict[str, Any]:
    url = os.environ.get("HYRULE_MCP_HEALTH_URL", "").strip()
    if not url:
        return {"status": "unavailable", "reason": "HYRULE_MCP_HEALTH_URL not set"}
    try:
        health = _get_json(url)
        return {"status": "ok", "health": health}
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        return {"status": "unavailable", "reason": str(exc)}


def _observation_body(payload: dict[str, Any]) -> str:
    rows = "| Source | Status | Summary |\n| --- | --- | --- |\n"
    sources = payload.get("sources", {})
    if isinstance(sources, dict):
        for name, source_payload in sources.items():
            if isinstance(source_payload, dict):
                status = source_payload.get("status", "unknown")
                summary = json.dumps({k: v for k, v in source_payload.items() if k != "health"}, sort_keys=True)
                rows += f"| `{name}` | `{status}` | `{summary}` |\n"
    return f"""# Safe health observation

Observed at: `{payload.get('observed_at')}`

This is observed evidence only. It must not redefine repo-owned intended state.

# Source summary

{rows}
# Sanitized payload

```json
{json.dumps(payload, sort_keys=True, indent=2)}
```
"""


def _write_observed_indexes(bundle_root: Path) -> None:
    observed = bundle_root / "observed"
    latest = observed / "latest"
    latest.mkdir(parents=True, exist_ok=True)
    (observed / "index.md").write_text(
        "# Observed evidence\n\n"
        "Manual/local read-only observations are written here. `uv run hyrule-knowledge observe --profile safe-health` can write the default `safe-health.md` snapshot when local environment variables are configured.\n\n"
        "Observed concepts are evidence-only, expire quickly, and must not be treated as canonical intended state.\n\n"
        "* [Latest observations](latest/) - Most recent sanitized snapshots.\n"
        "* [Update log](log.md) - Human-readable observation ingestion log.\n",
        encoding="utf-8",
    )
    entries = _latest_observation_index_entries(latest)
    if not entries:
        entries = ["* No observation snapshots have been collected yet."]
    (latest / "index.md").write_text(
        "# Latest observations\n\n"
        + "\n".join(entries)
        + "\n\nRun `uv run hyrule-knowledge observe --profile safe-health` locally to write or refresh `safe-health.md` here.\n",
        encoding="utf-8",
    )
    log = observed / "log.md"
    if not log.exists():
        log.write_text(
            "# Observed Evidence Update Log\n\n"
            "Observations are manual/local and time-bounded. Do not commit secrets, logs, packet captures, or raw command output here.\n",
            encoding="utf-8",
        )


def _latest_observation_index_entries(latest: Path) -> list[str]:
    entries: list[str] = []
    for path in sorted(latest.glob("*.md")):
        if path.name == "index.md":
            continue
        try:
            frontmatter, _ = parse_frontmatter(path)
            title = str(frontmatter.get("title") or path.stem)
            description = str(frontmatter.get("description") or "Observation snapshot.")
        except Exception:  # pragma: no cover - index best-effort for manual files
            title = path.stem
            description = "Observation snapshot."
        entries.append(f"* [{title}]({path.name}) - {description}")
    return entries
