---
type: API Schema
title: ProactiveAckRequest
description: Pydantic API schema `ProactiveAckRequest` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L1012-L1017
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
  lines: 1012-1017
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L1012-L1017
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: ProactiveAckRequest
source_path: app/main.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `ProactiveAckRequest` |
| Source | `app/main.py:1012` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fingerprint` | `str` | `True` | `` |  |
| `reason` | `str` | `False` | `<string>` |  |
| `issue` | `str` | `False` | `<string>` |  |
| `operator` | `str` | `False` | `<string>` |  |
| `ttl_hours` | `float | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/main.py:1012-1017](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L1012-L1017)
