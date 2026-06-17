---
type: API Schema
title: MXCheckResponse
description: Pydantic API schema `MXCheckResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1422-L1431
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
  lines: 1422-1431
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1422-L1431
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: MXCheckResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `MXCheckResponse` |
| Source | `hyrule_cloud/models.py:1422` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `request_id` | `str` | `True` | `` |  |
| `tool` | `MXTool` | `True` | `` |  |
| `target` | `str` | `True` | `` |  |
| `status` | `MXStatus` | `True` | `` |  |
| `summary` | `str` | `True` | `` |  |
| `findings` | `list[MXFinding]` | `False` | `Field(default_factory=list)` |  |
| `raw` | `dict[str, object] | None` | `False` | `None` |  |
| `sources` | `dict[str, str]` | `False` | `Field(default_factory=dict)` |  |
| `generated_at` | `datetime` | `True` | `` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:1422-1431](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1422-L1431)
