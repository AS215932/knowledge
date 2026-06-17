---
type: API Schema
title: SpecialistFinding
description: Pydantic API schema `SpecialistFinding` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/graph/state.py#L25-L32
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
  lines: 25-32
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/graph/state.py#L25-L32
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: SpecialistFinding
source_path: app/graph/state.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `SpecialistFinding` |
| Source | `app/graph/state.py:25` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `specialist` | `Literal['bgp', 'security_firewall', 'infrastructure']` | `True` | `` |  |
| `summary` | `str` | `True` | `` |  |
| `assessment` | `str` | `True` | `` |  |
| `confidence` | `float` | `False` | `Field(ge=0.0, le=1.0)` |  |
| `evidence` | `list[EvidenceItem]` | `False` | `Field(default_factory=list)` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/graph/state.py:25-32](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/graph/state.py#L25-L32)
