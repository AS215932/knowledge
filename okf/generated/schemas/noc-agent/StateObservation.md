---
type: API Schema
title: StateObservation
description: Pydantic API schema `StateObservation` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L58-L65
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
  lines: 58-65
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L58-L65
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: StateObservation
source_path: app/agents/triage.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `StateObservation` |
| Source | `app/agents/triage.py:58` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `subject` | `str` | `False` | `Field(default='', description='Object being described, such as host, peer, pr...` | Object being described, such as host, peer, prefix, service, or zone. |
| `attribute` | `str` | `False` | `Field(default='', description='Observed or intended property.')` | Observed or intended property. |
| `value` | `str` | `False` | `Field(default='', description='Compact state value.')` | Compact state value. |
| `source` | `ObservationSource` | `False` | `Field(default='derived', description='Where this observation came from.')` | Where this observation came from. |
| `evidence_refs` | `list[str]` | `False` | `Field(default_factory=list, description='Evidence IDs supporting observed sta...` | Evidence IDs supporting observed state. |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/agents/triage.py:58-65](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L58-L65)
