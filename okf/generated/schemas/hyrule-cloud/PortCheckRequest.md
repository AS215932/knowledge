---
type: API Schema
title: PortCheckRequest
description: Pydantic API schema `PortCheckRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L769-L776
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
  lines: 769-776
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L769-L776
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: PortCheckRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `PortCheckRequest` |
| Source | `hyrule_cloud/models.py:769` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `target` | `str` | `False` | `Field(min_length=1, max_length=2048)` |  |
| `port` | `int` | `False` | `Field(ge=1, le=65535)` |  |
| `protocol` | `PortProtocol` | `False` | `PortProtocol.TCP` |  |
| `profile` | `PortProfile` | `False` | `PortProfile.CUSTOM` |  |
| `vantage` | `DiagnosticVantage` | `False` | `DiagnosticVantage.EXTMON` |  |
| `timeout_ms` | `int` | `False` | `Field(default=5000, ge=500, le=30000)` |  |
| `include_banner` | `bool` | `False` | `False` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:769-776](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L769-L776)
