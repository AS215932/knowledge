---
type: API Schema
title: Hypothesis
description: Pydantic API schema `Hypothesis` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L89-L97
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
  lines: 89-97
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L89-L97
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: Hypothesis
source_path: app/agents/triage.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `Hypothesis` |
| Source | `app/agents/triage.py:89` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `hypothesis_id` | `str` | `False` | `Field(default='', description='Stable hypothesis ID.')` | Stable hypothesis ID. |
| `statement` | `str` | `False` | `Field(default='', description='Plausible but not fully proven explanation.')` | Plausible but not fully proven explanation. |
| `failure_domain` | `FailureDomain` | `False` | `Field(default='unknown', description='Most likely failure domain.')` | Most likely failure domain. |
| `likelihood` | `Literal['low', 'medium', 'high']` | `False` | `Field(default='low', description='Conservative likelihood.')` | Conservative likelihood. |
| `evidence_refs` | `list[str]` | `False` | `Field(default_factory=list, description='Evidence IDs supporting the hypothes...` | Evidence IDs supporting the hypothesis. |
| `missing_evidence` | `list[str]` | `False` | `Field(default_factory=list, description='Checks needed before promoting to fa...` | Checks needed before promoting to fact. |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/agents/triage.py:89-97](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/triage.py#L89-L97)
