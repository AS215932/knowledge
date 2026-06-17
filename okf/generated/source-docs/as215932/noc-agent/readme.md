---
type: Source Document
title: Hyrule Networks (AS215932) NOC Agent
description: '`noc-agent` is the operator-facing investigation service for Hyrule
  Networks (AS215932). It accepts monitoring events, runs structured incident analysis,
  records human-review proposals, and keeps a fallback local control plane available...'
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/README.md
tags:
- as215932
- noc-agent
- source-document
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: README.md
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 1-262
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/README.md#L1-L262
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
source_path: README.md
commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/noc-agent` |
| Path | `README.md` |
| Commit | `98e5010648e34ac0ea6ad8e6a925fef76d0dbea9` |
| Lines | `262` |

# Detected headings

* `# Hyrule Networks (AS215932) NOC Agent`
* `## Runtime shape`
* `## Primary interfaces`
* `## Operator control`
* `## Approved remediation (gated, no-op first)`
* `## Proactive loop`
* `## Discord bot`
* `## Golden-state context`
* `## Key configuration`
* `## Model backend configuration`
* `## Tests`

# Deterministic excerpt

```markdown
# Hyrule Networks (AS215932) NOC Agent

`noc-agent` is the operator-facing investigation service for Hyrule Networks
(AS215932). It accepts monitoring events, runs structured incident analysis,
records human-review proposals, and keeps a fallback local control plane available
even when chat tooling is unreachable.

## Runtime shape

- FastAPI receives Alertmanager and Icinga webhooks.
- A LangGraph investigation runtime normalizes the alert, correlates repeated
  incidents, routes to a specialist profile, validates confidence, checks
  golden-state drift, and produces a reviewable proposal.
- Redis stores graph checkpoint state plus short-lived incident memory.
- Discord can act as the interactive operator console.
- A loopback-only local control API plus `nocctl` gives operators an SSH/VPN
  fallback for review and decision recording.
- Hyrule MCP provides live diagnostic telemetry; NOC Agent consumes it through
  the configured daemon URL or the legacy stdio path.

The current tranche is intentionally diagnostic-only. Approval records and
resumes operator state, but it does not execute infrastructure changes.

## Primary interfaces

Existing interfaces preserved:

- `POST /webhook/alertmanager`
- `POST /webhook/icinga`
- `POST /task`
- `POST /mail/poll`
- `GET /health`
- `GET /health/mcp`
- `GET /health/config`
- `GET /health/model`
- `GET /health/mail`
- `GET /metrics`

New control-plane interfaces:

- `GET /control/incidents/pending`
- `GET /control/incidents/{incident_id}`
- `POST /control/incidents/{incident_id}/decision`
- `POST /approval/resume`
- `GET /control/proactive/status`
- `POST /control/proactive/pause`
- `POST /control/proactive/resume`
- `POST /control/proactive/run-once`
- `GET /control/proactive/suppressions`
- `POST /control/proactive/ack` / `POST
...
```

# Citations

[1] [README.md](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/README.md)
