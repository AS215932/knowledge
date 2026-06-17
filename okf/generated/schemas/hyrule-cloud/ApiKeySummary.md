---
type: API Schema
title: ApiKeySummary
description: Pydantic API schema `ApiKeySummary` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L257-L266
tags:
- api-schema
- hyrule-cloud
- pydantic
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/auth.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 257-266
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L257-L266
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: ApiKeySummary
source_path: hyrule_cloud/api/auth.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `ApiKeySummary` |
| Source | `hyrule_cloud/api/auth.py:257` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key_id` | `str` | `True` | `` |  |
| `name` | `str` | `True` | `` |  |
| `scopes` | `list[str]` | `True` | `` |  |
| `created_at` | `datetime` | `True` | `` |  |
| `last_used_at` | `datetime | None` | `False` | `None` |  |
| `expires_at` | `datetime | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

Shape used in list + create responses. Never carries the cleartext —
that's surfaced exactly once via ApiKeyCreateResponse.api_key.

# Citations

[1] [hyrule_cloud/api/auth.py:257-266](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L257-L266)
