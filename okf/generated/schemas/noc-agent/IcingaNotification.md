---
type: API Schema
title: IcingaNotification
description: Pydantic API schema `IcingaNotification` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L234-L242
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
  lines: 234-242
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L234-L242
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: IcingaNotification
source_path: app/main.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `IcingaNotification` |
| Source | `app/main.py:234` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `host_name` | `str` | `True` | `` |  |
| `host_address` | `str | None` | `False` | `None` |  |
| `service_name` | `str | None` | `False` | `None` |  |
| `check_command` | `str | None` | `False` | `None` |  |
| `state` | `str` | `True` | `` |  |
| `state_type` | `str | None` | `False` | `None` |  |
| `output` | `str | None` | `False` | `None` |  |
| `tags` | `dict` | `False` | `Field(default_factory=dict)` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/main.py:234-242](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L234-L242)
