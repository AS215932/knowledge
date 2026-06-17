---
type: API Schema
title: VMProductsResponse
description: Pydantic API schema `VMProductsResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L341-L348
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
  lines: 341-348
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L341-L348
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: VMProductsResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `VMProductsResponse` |
| Source | `hyrule_cloud/models.py:341` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `currency` | `str` | `False` | `<string>` |  |
| `billing` | `str` | `False` | `<string>` |  |
| `products` | `list[VMProduct]` | `True` | `` |  |
| `os_templates_url` | `str` | `True` | `` |  |

# Validators

No validators statically detected.

# Documentation

Agent-facing VM catalog so non-browser clients get specs + pricing
without scraping the /services HTML.

# Citations

[1] [hyrule_cloud/models.py:341-348](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L341-L348)
