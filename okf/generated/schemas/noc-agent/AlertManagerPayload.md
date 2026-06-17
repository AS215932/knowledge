---
type: API Schema
title: AlertManagerPayload
description: Pydantic API schema `AlertManagerPayload` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L221-L231
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
  lines: 221-231
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L221-L231
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: AlertManagerPayload
source_path: app/main.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `AlertManagerPayload` |
| Source | `app/main.py:221` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `receiver` | `str` | `True` | `` |  |
| `status` | `str` | `True` | `` |  |
| `alerts` | `list[dict]` | `True` | `` |  |
| `groupLabels` | `dict` | `True` | `` |  |
| `commonLabels` | `dict` | `True` | `` |  |
| `commonAnnotations` | `dict` | `True` | `` |  |
| `externalURL` | `str` | `True` | `` |  |
| `version` | `str` | `True` | `` |  |
| `groupKey` | `str` | `True` | `` |  |
| `truncatedAlerts` | `int` | `False` | `0` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/main.py:221-231](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L221-L231)
