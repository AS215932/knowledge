---
type: API Schema
title: SourceHealth
description: Pydantic API schema `SourceHealth` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L524-L529
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
  lines: 524-529
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L524-L529
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: SourceHealth
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `SourceHealth` |
| Source | `hyrule_cloud/models.py:524` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `status` | `SourceStatus | str` | `False` | `Field(description='ok, stale, degraded, unavailable, error, or source_not_con...` | ok, stale, degraded, unavailable, error, or source_not_configured |
| `age_seconds` | `int | None` | `False` | `None` |  |
| `message` | `str | None` | `False` | `None` |  |
| `checked_at` | `datetime | None` | `False` | `None` |  |
| `source_url` | `str | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:524-529](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L524-L529)
