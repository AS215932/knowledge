---
type: API Schema
title: MailDraftPlan
description: Pydantic API schema `MailDraftPlan` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/mail.py#L9-L17
tags:
- api-schema
- noc-agent
- pydantic
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: app/agents/mail.py
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 9-17
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/mail.py#L9-L17
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
model: MailDraftPlan
source_path: app/agents/mail.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `MailDraftPlan` |
| Source | `app/agents/mail.py:9` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `classification` | `str` | `False` | `Field(description='Operational category such as noc, abuse, peering, dh, bill...` | Operational category such as noc, abuse, peering, dh, billing, or unknown |
| `urgency` | `str` | `False` | `Field(description='Urgency of the message: HIGH, MEDIUM, or LOW')` | Urgency of the message: HIGH, MEDIUM, or LOW |
| `summary` | `str` | `False` | `Field(description='Short operational summary of the inbound email')` | Short operational summary of the inbound email |
| `requires_human` | `bool` | `False` | `Field(default=True, description='Always true for v1 draft-and-approve handling')` | Always true for v1 draft-and-approve handling |
| `suggested_reply_subject` | `str` | `False` | `Field(description='Subject line for the draft response')` | Subject line for the draft response |
| `reply_summary` | `str` | `False` | `Field(description='A brief summary of what the drafted response says')` | A brief summary of what the drafted response says |
| `suggested_reply_body` | `str` | `False` | `Field(description='Plain-text draft response for human review')` | Plain-text draft response for human review |
| `internal_notes` | `list[str]` | `False` | `Field(default_factory=list, description='Notes for the operator reviewing the...` | Notes for the operator reviewing the draft |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [app/agents/mail.py:9-17](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/agents/mail.py#L9-L17)
