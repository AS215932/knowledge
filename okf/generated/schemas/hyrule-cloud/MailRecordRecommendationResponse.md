---
type: API Schema
title: MailRecordRecommendationResponse
description: Pydantic API schema `MailRecordRecommendationResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1352-L1357
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
  lines: 1352-1357
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1352-L1357
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: MailRecordRecommendationResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `MailRecordRecommendationResponse` |
| Source | `hyrule_cloud/models.py:1352` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `domain` | `str` | `True` | `` |  |
| `provider` | `str` | `True` | `` |  |
| `records` | `list[MailRecordRecommendation]` | `True` | `` |  |
| `warnings` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `generated_at` | `datetime` | `False` | `Field(default_factory=lambda: datetime.now(UTC))` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:1352-1357](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1352-L1357)
