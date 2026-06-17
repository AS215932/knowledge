---
type: API Schema
title: WalletChallengeRequest
description: Pydantic API schema `WalletChallengeRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L154-L155
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
  lines: 154-155
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L154-L155
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: WalletChallengeRequest
source_path: hyrule_cloud/api/auth.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `WalletChallengeRequest` |
| Source | `hyrule_cloud/api/auth.py:154` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `account_id` | `str` | `False` | `Field(min_length=11, max_length=11)` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/api/auth.py:154-155](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L154-L155)
