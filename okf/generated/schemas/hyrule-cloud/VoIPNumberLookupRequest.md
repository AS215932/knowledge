---
type: API Schema
title: VoIPNumberLookupRequest
description: Pydantic API schema `VoIPNumberLookupRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L876-L880
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
  lines: 876-880
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L876-L880
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: VoIPNumberLookupRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `VoIPNumberLookupRequest` |
| Source | `hyrule_cloud/models.py:876` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `number` | `str` | `False` | `Field(min_length=3, max_length=32)` |  |
| `country` | `str | None` | `False` | `Field(default=None, max_length=2)` |  |
| `checks` | `list[VoIPCheck]` | `False` | `Field(default_factory=lambda: [VoIPCheck.NUMBER_INTEL, VoIPCheck.CNAM, VoIPCh...` |  |
| `include_raw` | `bool` | `False` | `False` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:876-880](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L876-L880)
