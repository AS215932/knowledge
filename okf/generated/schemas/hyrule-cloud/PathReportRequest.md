---
type: API Schema
title: PathReportRequest
description: Pydantic API schema `PathReportRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L732-L738
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
  lines: 732-738
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L732-L738
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: PathReportRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `PathReportRequest` |
| Source | `hyrule_cloud/models.py:732` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `target` | `str` | `False` | `Field(min_length=1, max_length=2048)` |  |
| `address_family` | `DiagnosticAddressFamily` | `False` | `DiagnosticAddressFamily.AUTO` |  |
| `vantages` | `list[DiagnosticVantage]` | `False` | `Field(default_factory=lambda: [DiagnosticVantage.EXTMON, DiagnosticVantage.AS...` |  |
| `checks` | `list[PathReportCheck]` | `False` | `Field(default_factory=lambda: [PathReportCheck.PING, PathReportCheck.TRACEROU...` |  |
| `max_duration_seconds` | `int` | `False` | `Field(default=60, ge=5, le=300)` |  |
| `include_raw` | `bool` | `False` | `False` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:732-738](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L732-L738)
