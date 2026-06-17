---
type: API Schema
title: VMStatusResponse
description: Pydantic API schema `VMStatusResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L267-L276
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
  lines: 267-276
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L267-L276
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: VMStatusResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `VMStatusResponse` |
| Source | `hyrule_cloud/models.py:267` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `vm_id` | `str` | `True` | `` |  |
| `status` | `VMStatus` | `True` | `` |  |
| `ipv6` | `str | None` | `False` | `None` |  |
| `hostname` | `str | None` | `False` | `None` |  |
| `ssh` | `str | None` | `False` | `None` |  |
| `expires_at` | `datetime | None` | `False` | `None` |  |
| `firewall` | `FirewallState | None` | `False` | `None` |  |
| `error` | `str | None` | `False` | `None` |  |
| `cost_breakdown` | `CostBreakdown | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:267-276](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L267-L276)
