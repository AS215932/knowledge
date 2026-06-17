---
type: API Schema
title: BGPLookupResponse
description: Pydantic API schema `BGPLookupResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L991-L1000
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
  lines: 991-1000
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L991-L1000
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: BGPLookupResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `BGPLookupResponse` |
| Source | `hyrule_cloud/models.py:991` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `request_id` | `str` | `True` | `` |  |
| `subject` | `dict[str, str | int]` | `True` | `` |  |
| `resolved` | `BGPResolvedSubject` | `False` | `Field(default_factory=BGPResolvedSubject)` |  |
| `results` | `dict[str, object]` | `False` | `Field(default_factory=dict)` |  |
| `assertions` | `dict[str, object]` | `False` | `Field(default_factory=dict)` |  |
| `sources` | `dict[str, SourceHealth]` | `False` | `Field(default_factory=dict)` |  |
| `partial` | `bool` | `False` | `False` |  |
| `charged_amount_usd` | `str | None` | `False` | `None` |  |
| `generated_at` | `datetime` | `True` | `` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:991-1000](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L991-L1000)
