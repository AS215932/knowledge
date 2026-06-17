---
type: API Schema
title: StoredDraft
description: Pydantic API schema `StoredDraft` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/mail.py#L49-L59
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
  lines: 49-59
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/mail.py#L49-L59
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: StoredDraft
source_path: app/mail.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `StoredDraft` |
| Source | `app/mail.py:49` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `draft_id` | `str` | `True` | `` |  |
| `created_at` | `str` | `True` | `` |  |
| `source_uid` | `str` | `True` | `` |  |
| `source_message_id` | `str | None` | `True` | `` |  |
| `original_recipient` | `str | None` | `True` | `` |  |
| `sender` | `str` | `True` | `` |  |
| `subject` | `str` | `True` | `` |  |
| `plan` | `MailDraftPlan` | `True` | `` |  |
| `approval_required` | `bool` | `False` | `True` |  |
| `sent` | `bool` | `False` | `False` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/mail.py:49-59](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/mail.py#L49-L59)
