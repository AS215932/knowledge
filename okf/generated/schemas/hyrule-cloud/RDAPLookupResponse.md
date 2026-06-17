---
type: API Schema
title: RDAPLookupResponse
description: Pydantic API schema `RDAPLookupResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1265-L1272
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
  lines: 1265-1272
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1265-L1272
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: RDAPLookupResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `RDAPLookupResponse` |
| Source | `hyrule_cloud/models.py:1265` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `request_id` | `str` | `True` | `` |  |
| `subject` | `RegistrySubject` | `True` | `` |  |
| `registry` | `str | None` | `False` | `None` |  |
| `bootstrap_url` | `str | None` | `False` | `None` |  |
| `parsed` | `dict[str, object]` | `False` | `Field(default_factory=dict)` |  |
| `raw` | `dict[str, object] | None` | `False` | `None` |  |
| `generated_at` | `datetime` | `True` | `` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:1265-1272](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1265-L1272)
