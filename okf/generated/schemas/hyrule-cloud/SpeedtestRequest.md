---
type: API Schema
title: SpeedtestRequest
description: Pydantic API schema `SpeedtestRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L899-L904
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
  lines: 899-904
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L899-L904
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: SpeedtestRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `SpeedtestRequest` |
| Source | `hyrule_cloud/models.py:899` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `target` | `str` | `False` | `<string>` |  |
| `direction` | `SpeedtestDirection` | `False` | `SpeedtestDirection.BIDIRECTIONAL` |  |
| `duration_seconds` | `int` | `False` | `Field(default=10, ge=3, le=60)` |  |
| `max_megabytes` | `int` | `False` | `Field(default=25, ge=1, le=250)` |  |
| `vantages` | `list[DiagnosticVantage]` | `False` | `Field(default_factory=lambda: [DiagnosticVantage.AS215932])` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:899-904](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L899-L904)
