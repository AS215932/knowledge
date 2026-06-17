---
type: API Schema
title: StateDelta
description: Pydantic API schema `StateDelta` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L68-L78
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
  lines: 68-78
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L68-L78
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: StateDelta
source_path: app/agents/triage.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `StateDelta` |
| Source | `app/agents/triage.py:68` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `delta_id` | `str` | `False` | `Field(default='', description='Stable delta ID.')` | Stable delta ID. |
| `subject` | `str` | `False` | `Field(default='', description='Object whose intended and observed states diff...` | Object whose intended and observed states differ. |
| `attribute` | `str` | `False` | `Field(default='', description='Differing property.')` | Differing property. |
| `expected_value` | `str` | `False` | `Field(default='', description='Expected value from manifest or perimeter cont...` | Expected value from manifest or perimeter context. |
| `observed_value` | `str` | `False` | `Field(default='', description='Observed value from telemetry.')` | Observed value from telemetry. |
| `delta_type` | `DeltaKind` | `False` | `Field(default='unknown', description='Class of mismatch.')` | Class of mismatch. |
| `impact` | `str` | `False` | `Field(default='', description='Operational impact of the mismatch.')` | Operational impact of the mismatch. |
| `evidence_refs` | `list[str]` | `False` | `Field(default_factory=list, description='Evidence IDs proving this delta.')` | Evidence IDs proving this delta. |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/agents/triage.py:68-78](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L68-L78)
