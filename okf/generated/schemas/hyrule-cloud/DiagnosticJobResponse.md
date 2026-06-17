---
type: API Schema
title: DiagnosticJobResponse
description: Pydantic API schema `DiagnosticJobResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L612-L623
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
  lines: 612-623
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L612-L623
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: DiagnosticJobResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `DiagnosticJobResponse` |
| Source | `hyrule_cloud/models.py:612` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `job_id` | `str` | `False` | `Field(default_factory=generate_diagnostic_job_id)` |  |
| `job_access_token` | `str | None` | `False` | `None` |  |
| `service` | `str` | `True` | `` |  |
| `kind` | `DiagnosticJobKind | str` | `True` | `` |  |
| `status` | `DiagnosticJobStatus` | `True` | `` |  |
| `status_url` | `str | None` | `False` | `None` |  |
| `download_url` | `str | None` | `False` | `None` |  |
| `charged_amount_usd` | `str | None` | `False` | `None` |  |
| `error` | `str | None` | `False` | `None` |  |
| `created_at` | `datetime` | `False` | `Field(default_factory=lambda: datetime.now(UTC))` |  |
| `expires_at` | `datetime | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:612-623](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L612-L623)
