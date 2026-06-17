---
type: API Schema
title: VoIPCheckRequest
description: Pydantic API schema `VoIPCheckRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L868-L873
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
  lines: 868-873
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L868-L873
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: VoIPCheckRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `VoIPCheckRequest` |
| Source | `hyrule_cloud/models.py:868` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `target` | `str` | `False` | `Field(min_length=1, max_length=2048)` |  |
| `checks` | `list[VoIPCheck]` | `False` | `Field(default_factory=lambda: [VoIPCheck.SIP_DNS, VoIPCheck.SIP_TLS])` |  |
| `sip_port` | `int` | `False` | `Field(default=5061, ge=1, le=65535)` |  |
| `timeout_ms` | `int` | `False` | `Field(default=10000, ge=500, le=60000)` |  |
| `include_raw` | `bool` | `False` | `False` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:868-873](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L868-L873)
