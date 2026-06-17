---
type: API Schema
title: CommentRequest
description: Pydantic API schema `CommentRequest` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L748-L750
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
  lines: 748-750
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L748-L750
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: CommentRequest
source_path: app/main.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `CommentRequest` |
| Source | `app/main.py:748` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `operator` | `str` | `False` | `<string>` |  |
| `comment` | `str` | `True` | `` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/main.py:748-750](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L748-L750)
