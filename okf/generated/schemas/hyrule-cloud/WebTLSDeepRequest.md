---
type: API Schema
title: WebTLSDeepRequest
description: Pydantic API schema `WebTLSDeepRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L693-L698
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
  lines: 693-698
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L693-L698
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: WebTLSDeepRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `WebTLSDeepRequest` |
| Source | `hyrule_cloud/models.py:693` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `host` | `str` | `False` | `Field(min_length=1, max_length=253)` |  |
| `port` | `int` | `False` | `Field(default=443, ge=1, le=65535)` |  |
| `scan_profile` | `str` | `False` | `<string>` |  |
| `checks` | `list[WebTLSDeepCheck]` | `False` | `Field(default_factory=lambda: [check for check in WebTLSDeepCheck])` |  |
| `include_raw` | `bool` | `False` | `False` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:693-698](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L693-L698)
