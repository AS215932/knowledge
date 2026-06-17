---
type: API Schema
title: MailSendRequest
description: Pydantic API schema `MailSendRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1618-L1628
tags:
- api-schema
- hyrule-cloud
- pydantic
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/models.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1618-1628
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1618-L1628
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: MailSendRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `MailSendRequest` |
| Source | `hyrule_cloud/models.py:1618` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `mailbox_id` | `str` | `True` | `` |  |
| `from_` | `str` | `False` | `Field(alias='from')` |  |
| `to` | `list[str]` | `True` | `` |  |
| `cc` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `bcc` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `subject` | `str` | `False` | `Field(max_length=998)` |  |
| `text` | `str | None` | `False` | `None` |  |
| `html` | `str | None` | `False` | `None` |  |
| `attachments` | `list[MailAttachment]` | `False` | `Field(default_factory=list)` |  |
| `idempotency_key` | `str | None` | `False` | `Field(default=None, max_length=128)` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:1618-1628](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1618-L1628)
