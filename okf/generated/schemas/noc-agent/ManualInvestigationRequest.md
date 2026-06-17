---
type: API Schema
title: ManualInvestigationRequest
description: Pydantic API schema `ManualInvestigationRequest` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L733-L735
tags:
- api-schema
- noc-agent
- pydantic
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: app/main.py
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 733-735
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L733-L735
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: ManualInvestigationRequest
source_path: app/main.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `ManualInvestigationRequest` |
| Source | `app/main.py:733` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `prompt` | `str` | `True` | `` |  |
| `operator` | `str` | `False` | `<string>` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/main.py:733-735](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L733-L735)
