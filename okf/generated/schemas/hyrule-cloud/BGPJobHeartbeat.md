---
type: API Schema
title: BGPJobHeartbeat
description: Pydantic API schema `BGPJobHeartbeat` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/internal_bgp.py#L40-L44
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
  lines: 40-44
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/internal_bgp.py#L40-L44
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: BGPJobHeartbeat
source_path: hyrule_cloud/api/internal_bgp.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `BGPJobHeartbeat` |
| Source | `hyrule_cloud/api/internal_bgp.py:40` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `claimed_by` | `str | None` | `False` | `None` |  |
| `status` | `str | None` | `False` | `None` |  |
| `error` | `str | None` | `False` | `None` |  |
| `artifact_snapshot_id` | `str | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/api/internal_bgp.py:40-44](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/internal_bgp.py#L40-L44)
