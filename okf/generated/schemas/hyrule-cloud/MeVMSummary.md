---
type: API Schema
title: MeVMSummary
description: Pydantic API schema `MeVMSummary` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L202-L210
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
  lines: 202-210
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L202-L210
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: MeVMSummary
source_path: hyrule_cloud/api/auth.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `MeVMSummary` |
| Source | `hyrule_cloud/api/auth.py:202` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `vm_id` | `str` | `True` | `` |  |
| `status` | `VMStatus` | `True` | `` |  |
| `os` | `str | None` | `False` | `None` |  |
| `size` | `str | None` | `False` | `None` |  |
| `ipv6` | `str | None` | `False` | `None` |  |
| `hostname` | `str | None` | `False` | `None` |  |
| `expires_at` | `datetime | None` | `False` | `None` |  |
| `created_at` | `datetime | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/api/auth.py:202-210](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L202-L210)
