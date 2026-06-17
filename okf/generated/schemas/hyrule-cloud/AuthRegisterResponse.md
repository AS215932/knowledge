---
type: API Schema
title: AuthRegisterResponse
description: Pydantic API schema `AuthRegisterResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L121-L130
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
  lines: 121-130
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L121-L130
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: AuthRegisterResponse
source_path: hyrule_cloud/api/auth.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `AuthRegisterResponse` |
| Source | `hyrule_cloud/api/auth.py:121` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `str` | `True` | `` |  |
| `recovery_code` | `str` | `True` | `` |  |
| `api_key` | `str | None` | `False` | `None` |  |
| `api_key_id` | `str | None` | `False` | `None` |  |
| `api_key_scopes` | `list[str] | None` | `False` | `None` |  |
| `message` | `str` | `False` | `<string>` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/api/auth.py:121-130](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L121-L130)
