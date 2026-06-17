---
type: API Schema
title: BGPSourceStatusIngest
description: Pydantic API schema `BGPSourceStatusIngest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/internal_bgp.py#L17-L21
tags:
- api-schema
- hyrule-cloud
- pydantic
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/internal_bgp.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 17-21
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/internal_bgp.py#L17-L21
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: BGPSourceStatusIngest
source_path: hyrule_cloud/api/internal_bgp.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `BGPSourceStatusIngest` |
| Source | `hyrule_cloud/api/internal_bgp.py:17` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `source_name` | `str` | `False` | `Field(min_length=1, max_length=64)` |  |
| `status` | `str` | `False` | `<string>` |  |
| `payload` | `dict[str, Any]` | `False` | `Field(default_factory=dict)` |  |
| `error` | `str | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/api/internal_bgp.py:17-21](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/internal_bgp.py#L17-L21)
