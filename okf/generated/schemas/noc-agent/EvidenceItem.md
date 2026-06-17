---
type: API Schema
title: EvidenceItem
description: Pydantic API schema `EvidenceItem` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/graph/state.py#L16-L22
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
  lines: 16-22
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/graph/state.py#L16-L22
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: EvidenceItem
source_path: app/graph/state.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `EvidenceItem` |
| Source | `app/graph/state.py:16` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `tool` | `str` | `True` | `` |  |
| `summary` | `str` | `True` | `` |  |
| `direct_measurement` | `bool` | `False` | `False` |  |
| `payload` | `dict[str, Any]` | `False` | `Field(default_factory=dict)` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/graph/state.py:16-22](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/graph/state.py#L16-L22)
