---
type: API Schema
title: MXCheckOptions
description: Pydantic API schema `MXCheckOptions` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1395-L1401
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
  lines: 1395-1401
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1395-L1401
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: MXCheckOptions
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `MXCheckOptions` |
| Source | `hyrule_cloud/models.py:1395` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `timeout_ms` | `int` | `False` | `Field(default=5000, ge=500, le=60000)` |  |
| `include_raw` | `bool` | `False` | `False` |  |
| `dkim_selectors` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `smtp_starttls` | `bool` | `False` | `True` |  |
| `include_recommendations` | `bool` | `False` | `True` |  |
| `port` | `int | None` | `False` | `Field(default=None, ge=1, le=65535)` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:1395-1401](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1395-L1401)
