---
type: API Schema
title: BGPTimeSelector
description: Pydantic API schema `BGPTimeSelector` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L946-L951
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
  lines: 946-951
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L946-L951
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: BGPTimeSelector
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `BGPTimeSelector` |
| Source | `hyrule_cloud/models.py:946` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `mode` | `BGPTimeMode` | `False` | `BGPTimeMode.LATEST` |  |
| `at` | `datetime | None` | `False` | `None` |  |
| `from_time` | `datetime | None` | `False` | `None` |  |
| `until_time` | `datetime | None` | `False` | `None` |  |
| `max_age_seconds` | `int` | `False` | `Field(default=900, ge=0, le=86400)` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:946-951](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L946-L951)
