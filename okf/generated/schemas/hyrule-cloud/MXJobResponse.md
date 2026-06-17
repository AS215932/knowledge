---
type: API Schema
title: MXJobResponse
description: Pydantic API schema `MXJobResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1456-L1467
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
  lines: 1456-1467
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1456-L1467
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: MXJobResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `MXJobResponse` |
| Source | `hyrule_cloud/models.py:1456` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `job_id` | `str` | `True` | `` |  |
| `job_access_token` | `str | None` | `False` | `None` |  |
| `status` | `MXJobStatus` | `True` | `` |  |
| `target` | `str` | `True` | `` |  |
| `profile` | `MXProfile` | `True` | `` |  |
| `status_url` | `str | None` | `False` | `None` |  |
| `download_url` | `str | None` | `False` | `None` |  |
| `results` | `list[MXCheckResponse]` | `False` | `Field(default_factory=list)` |  |
| `error` | `str | None` | `False` | `None` |  |
| `created_at` | `datetime` | `True` | `` |  |
| `expires_at` | `datetime | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:1456-1467](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1456-L1467)
