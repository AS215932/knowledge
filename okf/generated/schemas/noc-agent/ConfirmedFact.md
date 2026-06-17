---
type: API Schema
title: ConfirmedFact
description: Pydantic API schema `ConfirmedFact` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L81-L86
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
  lines: 81-86
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L81-L86
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: ConfirmedFact
source_path: app/agents/triage.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `ConfirmedFact` |
| Source | `app/agents/triage.py:81` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fact_id` | `str` | `False` | `Field(default='', description='Stable fact ID.')` | Stable fact ID. |
| `statement` | `str` | `False` | `Field(default='', description='Fact directly proven by telemetry.')` | Fact directly proven by telemetry. |
| `evidence_refs` | `list[str]` | `False` | `Field(default_factory=list, description='Evidence IDs proving this fact.')` | Evidence IDs proving this fact. |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/agents/triage.py:81-86](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L81-L86)
