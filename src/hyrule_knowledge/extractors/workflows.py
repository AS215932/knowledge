"""GitHub Actions workflow extraction."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

import yaml

from hyrule_knowledge.github_source import read_file
from hyrule_knowledge.models import RepoSnapshot

SECRET_RE = re.compile(r"secrets\.([A-Za-z0-9_]+)")


@dataclass(frozen=True)
class WorkflowJobInfo:
    name: str
    runs_on: str
    environment: str | None = None
    permissions: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class WorkflowInfo:
    name: str
    source_path: str
    triggers: list[str]
    permissions: dict[str, Any]
    jobs: list[WorkflowJobInfo]
    secrets: list[str]
    deploy_like: bool


def _trigger_names(data: dict[str, Any]) -> list[str]:
    data_any: dict[Any, Any] = data
    raw = data_any.get("on", data_any.get(True, {}))
    if isinstance(raw, str):
        return [raw]
    if isinstance(raw, list):
        return [str(item) for item in raw]
    if isinstance(raw, dict):
        return [str(key) for key in raw]
    return []


def _runs_on(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    return "unspecified"


def _environment(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, dict) and value.get("name"):
        return str(value["name"])
    return None


def extract_workflow(snapshot: RepoSnapshot, rel_path: str) -> WorkflowInfo | None:
    text = read_file(snapshot.path, rel_path)
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError:
        return None
    if not isinstance(data, dict):
        return None
    raw_jobs = data.get("jobs", {})
    jobs: list[WorkflowJobInfo] = []
    if isinstance(raw_jobs, dict):
        for name, job in raw_jobs.items():
            if not isinstance(job, dict):
                continue
            raw_permissions = job.get("permissions", {})
            permissions = raw_permissions if isinstance(raw_permissions, dict) else {}
            jobs.append(
                WorkflowJobInfo(
                    name=str(name),
                    runs_on=_runs_on(job.get("runs-on")),
                    environment=_environment(job.get("environment")),
                    permissions=permissions,
                )
            )
    raw_permissions = data.get("permissions", {})
    permissions = raw_permissions if isinstance(raw_permissions, dict) else {}
    secrets = sorted(set(SECRET_RE.findall(text)))
    lower = text.lower()
    deploy_like = any(token in lower for token in ["deploy", "production", "environment:", "apply.yml", "promote"])
    return WorkflowInfo(
        name=str(data.get("name") or rel_path),
        source_path=rel_path,
        triggers=_trigger_names(data),
        permissions=permissions,
        jobs=jobs,
        secrets=secrets,
        deploy_like=deploy_like,
    )


def extract_workflows(snapshot: RepoSnapshot) -> list[WorkflowInfo]:
    workflows: list[WorkflowInfo] = []
    for rel_path in snapshot.files:
        if rel_path.startswith(".github/workflows/") and rel_path.endswith((".yml", ".yaml")):
            workflow = extract_workflow(snapshot, rel_path)
            if workflow is not None:
                workflows.append(workflow)
    return workflows
