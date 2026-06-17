---
type: API Schema
title: NetworkRequest
description: Pydantic API schema `NetworkRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L361-L367
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
  lines: 361-367
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L361-L367
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: NetworkRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `NetworkRequest` |
| Source | `hyrule_cloud/models.py:361` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `url` | `str` | `False` | `Field(max_length=2048, description='The full URL to fetch')` | The full URL to fetch |
| `method` | `str` | `False` | `Field(default='GET', description='HTTP method: GET, HEAD, or POST')` | HTTP method: GET, HEAD, or POST |
| `headers` | `dict[str, str] | None` | `False` | `Field(default=None, description='Custom headers')` | Custom headers |
| `body` | `str | None` | `False` | `Field(default=None, max_length=65536, description='Request body')` | Request body |
| `proxy_mode` | `ProxyMode` | `False` | `Field(default=ProxyMode.DIRECT, description='Routing mode')` | Routing mode |
| `timeout_seconds` | `int` | `False` | `Field(default=15, ge=1, le=60, description='Request timeout')` | Request timeout |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:361-367](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L361-L367)
