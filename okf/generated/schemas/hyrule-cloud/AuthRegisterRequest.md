---
type: API Schema
title: AuthRegisterRequest
description: Pydantic API schema `AuthRegisterRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L115-L118
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
  lines: 115-118
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L115-L118
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: AuthRegisterRequest
source_path: hyrule_cloud/api/auth.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `AuthRegisterRequest` |
| Source | `hyrule_cloud/api/auth.py:115` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `password` | `str` | `False` | `Field(min_length=12, max_length=256)` |  |
| `with_api_key` | `bool` | `False` | `False` |  |
| `api_key_name` | `str | None` | `False` | `Field(default=None, max_length=64)` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/api/auth.py:115-118](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L115-L118)
