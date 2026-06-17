---
type: Service
title: Hyrule NOC Agent
description: AS215932 Autonomous NOC Agent
resource: https://github.com/AS215932/noc-agent
tags:
- alertmanager
- automation
- fastapi
- hyrule
- icinga
- incident-response
- langgraph
- monitoring
- noc
- service
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: README.md
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 1-240
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/README.md#L1-L240
- repo: AS215932/noc-agent
  path: TESTING.md
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 1-16
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/TESTING.md#L1-L16
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
endpoint_count: 29
schema_count: 35
workflow_count: 4
---

# What this is

AS215932 Autonomous NOC Agent

# Responsibilities

* Alert intake, incident analysis, proactive hotspot scanning, operator approval, and Discord/local control surfaces.
* Consumes Hyrule MCP telemetry and stops at reviewable/human-gated proposals.

# Runtime/deployment shape

* Deployed on host `noc` via `noc_agent_version` pinned to `98e5010648e34ac0ea6ad8e6a925fef76d0dbea9`.
* Workflow `pr-agent` has deploy/promotion characteristics.
* Workflow `request-promotion` has deploy/promotion characteristics.

# Interfaces

* `POST /webhook/alertmanager` — `app/main.py:686`
* `POST /webhook/icinga` — `app/main.py:705`
* `POST /mail/poll` — `app/main.py:723`
* `POST /task` — `app/main.py:758`
* `GET /health` — `app/main.py:783`
* `GET /control/incidents/pending` — `app/main.py:788`
* `GET /control/incidents/{incident_id}` — `app/main.py:794`
* `GET /control` — `app/main.py:803`
* `GET /control/cases` — `app/main.py:809`
* `GET /control/cases/{case_id}` — `app/main.py:833`
* `GET /control/cases/{case_id}/events` — `app/main.py:842`
* `POST /control/cases/{case_id}/comment` — `app/main.py:851`
* `POST /control/cases/{case_id}/decision` — `app/main.py:866`
* `POST /control/cases/investigate` — `app/main.py:890`
* `POST /control/status` — `app/main.py:907`
* `GET /control/proactive/status` — `app/main.py:921`
* `POST /control/proactive/pause` — `app/main.py:974`
* `POST /control/proactive/resume` — `app/main.py:987`
* `POST /control/proactive/run-once` — `app/main.py:1000`
* `GET /control/proactive/suppressions` — `app/main.py:1033`
* `POST /control/proactive/ack` — `app/main.py:1043`
* `POST /control/proactive/unack` — `app/main.py:1061`
* `POST /control/incidents/{incident_id}/decision` — `app/main.py:1073`
* `POST /approval/resume` — `app/main.py:1087`
* `GET /health/mcp` — `app/main.py:1102`
* `GET /health/config` — `app/main.py:1110`
* `GET /health/model` — `app/main.py:1177`
* `GET /metrics` — `app/main.py:1197`
* `GET /health/mail` — `app/main.py:1204`
* Workflow `ci` from `.github/workflows/ci.yml`
* Workflow `pr-agent` from `.github/workflows/pr-agent.yml`
* Workflow `request-promotion` from `.github/workflows/request-promotion.yml`
* Workflow `semgrep` from `.github/workflows/semgrep.yml`

# Dependencies

* `fastapi` from `pyproject.toml`
* `httpx` from `pyproject.toml`
* `langgraph` from `pyproject.toml`
* `mcp` from `pyproject.toml`
* `structlog` from `pyproject.toml`
* `uvicorn` from `pyproject.toml`

# Source-of-truth files

* `README.md`
* `TESTING.md`
* `pyproject.toml`

# Operational runbooks

No repo-local runbook files detected in indexed sources.

# Safety/security constraints

* Production remediation remains human-gated; no-op rollback guards precede any mutating execution.
* Proactive loop is budgeted, read-only for investigation, and hands changes to engineering-loop issues.

# Related services

* [hyrule-mcp](/generated/services/hyrule-mcp.md)
* [network-operations](/generated/projects/network-operations.md)
* [engineering-loop](/generated/services/engineering-loop.md)

# Open issues/known gaps

* #12: Protect NOC control UI with OAuth/OIDC at the edge
* #10: CI: add a real test/lint gate (ruff + pytest) and make it required
* #1: noc-agent: add investigation discipline rules to system prompt (postmortem learnings)

# Canonicality

Repository-owned facts in this concept are derivative. If this concept disagrees with `AS215932/noc-agent` at commit `98e5010648e34ac0ea6ad8e6a925fef76d0dbea9` or a later source commit, the repository source wins and this concept is stale.

# Citations

[1] [AS215932/noc-agent:README.md](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/README.md#L1-L240)
[2] [AS215932/noc-agent:TESTING.md](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/TESTING.md#L1-L16)
