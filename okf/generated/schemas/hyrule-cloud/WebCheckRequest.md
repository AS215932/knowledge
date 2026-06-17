---
type: API Schema
title: WebCheckRequest
description: Pydantic API schema `WebCheckRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L681-L686
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
  lines: 681-686
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L681-L686
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: WebCheckRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `WebCheckRequest` |
| Source | `hyrule_cloud/models.py:681` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `target` | `str` | `False` | `Field(min_length=1, max_length=2048)` |  |
| `checks` | `list[WebCheck]` | `False` | `Field(default_factory=lambda: [WebCheck.DNS, WebCheck.HTTP, WebCheck.TLS, Web...` |  |
| `vantages` | `list[DiagnosticVantage]` | `False` | `Field(default_factory=lambda: [DiagnosticVantage.EXTMON])` |  |
| `timeout_ms` | `int` | `False` | `Field(default=10000, ge=500, le=60000)` |  |
| `include_raw` | `bool` | `False` | `False` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:681-686](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L681-L686)
