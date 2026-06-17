---
type: API Schema
title: DomainRegisterRequest
description: Pydantic API schema `DomainRegisterRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L464-L470
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
  lines: 464-470
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L464-L470
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: DomainRegisterRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `DomainRegisterRequest` |
| Source | `hyrule_cloud/models.py:464` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `domain` | `str | None` | `False` | `Field(default=None, min_length=3, max_length=253)` |  |
| `name` | `str | None` | `False` | `Field(default=None, max_length=128)` |  |
| `extension` | `str | None` | `False` | `Field(default=None, max_length=32)` |  |
| `duration_years` | `int` | `False` | `Field(default=1, ge=1, le=10)` |  |
| `ipv6` | `str | None` | `False` | `Field(default=None, max_length=64)` |  |
| `client_order_id` | `str | None` | `False` | `Field(default=None, max_length=64)` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:464-470](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L464-L470)
