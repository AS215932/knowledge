---
type: API Schema
title: MXCheckRequest
description: Pydantic API schema `MXCheckRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1404-L1411
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
  lines: 1404-1411
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1404-L1411
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: MXCheckRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `MXCheckRequest` |
| Source | `hyrule_cloud/models.py:1404` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `tool` | `MXTool | None` | `False` | `None` |  |
| `target` | `str | None` | `False` | `Field(default=None, min_length=1, max_length=2048)` |  |
| `command` | `str | None` | `False` | `Field(default=None, description='SuperTool-compatible command, e.g. mx:exampl...` | SuperTool-compatible command, e.g. mx:example.com or blacklist:8.8.8.8 |
| `options` | `MXCheckOptions` | `False` | `Field(default_factory=MXCheckOptions)` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:1404-1411](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1404-L1411)
