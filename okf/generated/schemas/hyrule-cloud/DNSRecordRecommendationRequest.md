---
type: API Schema
title: DNSRecordRecommendationRequest
description: Pydantic API schema `DNSRecordRecommendationRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1230-L1239
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
  lines: 1230-1239
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1230-L1239
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: DNSRecordRecommendationRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `DNSRecordRecommendationRequest` |
| Source | `hyrule_cloud/models.py:1230` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `domain` | `str` | `False` | `Field(min_length=1, max_length=253)` |  |
| `use_case` | `DNSRecordRecommendationUseCase` | `False` | `DNSRecordRecommendationUseCase.WEB` |  |
| `hostname` | `str | None` | `False` | `None` |  |
| `ipv4` | `str | None` | `False` | `None` |  |
| `ipv6` | `str | None` | `False` | `None` |  |
| `mail_provider` | `str | None` | `False` | `None` |  |
| `verification_name` | `str | None` | `False` | `None` |  |
| `verification_value` | `str | None` | `False` | `None` |  |
| `sip_target` | `str | None` | `False` | `None` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:1230-1239](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1230-L1239)
