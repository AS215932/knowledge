---
type: API Schema
title: MailAccountResponse
description: Pydantic API schema `MailAccountResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1539-L1549
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
  lines: 1539-1549
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1539-L1549
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: MailAccountResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `MailAccountResponse` |
| Source | `hyrule_cloud/models.py:1539` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `mailbox_id` | `str` | `True` | `` |  |
| `address` | `str` | `True` | `` |  |
| `status` | `MailAccountStatus` | `True` | `` |  |
| `management_token` | `str | None` | `False` | `None` |  |
| `management_url` | `str | None` | `False` | `None` |  |
| `smtp` | `MailEndpointConfig | None` | `False` | `None` |  |
| `imap` | `MailEndpointConfig | None` | `False` | `None` |  |
| `api` | `MailAPIAccessConfig | None` | `False` | `None` |  |
| `limits` | `MailLimits` | `True` | `` |  |
| `expires_at` | `datetime | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:1539-1549](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1539-L1549)
