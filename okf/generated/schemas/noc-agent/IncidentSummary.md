---
type: API Schema
title: IncidentSummary
description: Pydantic API schema `IncidentSummary` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/graph/state.py#L62-L84
tags:
- api-schema
- noc-agent
- pydantic
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: app/graph/state.py
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 62-84
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/graph/state.py#L62-L84
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: IncidentSummary
source_path: app/graph/state.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `IncidentSummary` |
| Source | `app/graph/state.py:62` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `incident_id` | `str` | `True` | `` |  |
| `case_number` | `str` | `False` | `<string>` |  |
| `resource_id` | `str` | `False` | `<string>` |  |
| `title` | `str` | `True` | `` |  |
| `status` | `Literal['running', 'investigating', 'waiting_approval', 'recovered_pending', 'resolved', 'expired', 'linked', 'approved', 'rejected', 'finalized']` | `True` | `` |  |
| `chronic_instability` | `bool` | `False` | `False` |  |
| `active_specialist` | `str | None` | `False` | `None` |  |
| `proposal_count` | `int` | `False` | `0` |  |
| `updated_at` | `str` | `False` | `Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/graph/state.py:62-84](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/graph/state.py#L62-L84)
