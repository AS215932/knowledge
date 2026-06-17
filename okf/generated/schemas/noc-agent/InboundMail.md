---
type: API Schema
title: InboundMail
description: Pydantic API schema `InboundMail` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/mail.py#L38-L46
tags:
- api-schema
- noc-agent
- pydantic
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: app/mail.py
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 38-46
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/mail.py#L38-L46
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: InboundMail
source_path: app/mail.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `InboundMail` |
| Source | `app/mail.py:38` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `uid` | `str` | `True` | `` |  |
| `message_id` | `str | None` | `False` | `None` |  |
| `from_address` | `str` | `True` | `` |  |
| `to_addresses` | `list[str]` | `True` | `` |  |
| `original_recipient` | `str | None` | `False` | `None` |  |
| `subject` | `str` | `True` | `` |  |
| `text_body` | `str` | `True` | `` |  |
| `received_at` | `str | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/mail.py:38-46](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/mail.py#L38-L46)
