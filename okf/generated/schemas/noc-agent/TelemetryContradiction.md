---
type: API Schema
title: TelemetryContradiction
description: Pydantic API schema `TelemetryContradiction` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L100-L107
tags:
- api-schema
- noc-agent
- pydantic
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: app/agents/triage.py
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 100-107
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L100-L107
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: TelemetryContradiction
source_path: app/agents/triage.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `TelemetryContradiction` |
| Source | `app/agents/triage.py:100` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `contradiction_id` | `str` | `False` | `Field(default='', description='Stable contradiction ID.')` | Stable contradiction ID. |
| `summary` | `str` | `False` | `Field(default='', description='Incompatible telemetry or missing-data issue.')` | Incompatible telemetry or missing-data issue. |
| `status` | `ContradictionStatus` | `False` | `Field(default='unresolved', description='How the contradiction is classified.')` | How the contradiction is classified. |
| `evidence_refs` | `list[str]` | `False` | `Field(default_factory=list, description='Evidence IDs involved in the contrad...` | Evidence IDs involved in the contradiction. |
| `next_check` | `str` | `False` | `Field(default='', description='Independent check that should resolve or scope...` | Independent check that should resolve or scope it. |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/agents/triage.py:100-107](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L100-L107)
