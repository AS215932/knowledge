---
type: API Schema
title: MailBounceParseResponse
description: Pydantic API schema `MailBounceParseResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1317-L1325
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
  lines: 1317-1325
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1317-L1325
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: MailBounceParseResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `MailBounceParseResponse` |
| Source | `hyrule_cloud/models.py:1317` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `status` | `DiagnosticStatus` | `True` | `` |  |
| `classification` | `MailBounceClassification` | `True` | `` |  |
| `smtp_status` | `str | None` | `False` | `None` |  |
| `remote_mta` | `str | None` | `False` | `None` |  |
| `probable_causes` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `recommended_actions` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `evidence` | `dict[str, object]` | `False` | `Field(default_factory=dict)` |  |
| `generated_at` | `datetime` | `False` | `Field(default_factory=lambda: datetime.now(UTC))` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:1317-1325](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1317-L1325)
