---
type: API Schema
title: MailMessageSummary
description: Pydantic API schema `MailMessageSummary` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1631-L1641
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
  lines: 1631-1641
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1631-L1641
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: MailMessageSummary
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `MailMessageSummary` |
| Source | `hyrule_cloud/models.py:1631` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `message_id` | `str` | `True` | `` |  |
| `mailbox_id` | `str` | `True` | `` |  |
| `folder` | `str` | `False` | `<string>` |  |
| `from_` | `str` | `False` | `Field(alias='from')` |  |
| `to` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `subject` | `str | None` | `False` | `None` |  |
| `received_at` | `datetime | None` | `False` | `None` |  |
| `sent_at` | `datetime | None` | `False` | `None` |  |
| `flags` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `has_attachments` | `bool` | `False` | `False` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:1631-1641](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1631-L1641)
