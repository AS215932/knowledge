---
type: API Schema
title: DNSLookupResponse
description: Pydantic API schema `DNSLookupResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1188-L1198
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
  lines: 1188-1198
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1188-L1198
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: DNSLookupResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `DNSLookupResponse` |
| Source | `hyrule_cloud/models.py:1188` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `request_id` | `str` | `True` | `` |  |
| `question` | `DNSQuestion` | `True` | `` |  |
| `answers` | `list[DNSRecordAnswer]` | `False` | `Field(default_factory=list)` |  |
| `authority` | `list[DNSRecordAnswer]` | `False` | `Field(default_factory=list)` |  |
| `additional` | `list[DNSRecordAnswer]` | `False` | `Field(default_factory=list)` |  |
| `rcode` | `str` | `True` | `` |  |
| `dnssec` | `DNSSECResult | None` | `False` | `None` |  |
| `resolver` | `str` | `True` | `` |  |
| `trace` | `list[dict[str, object]]` | `False` | `Field(default_factory=list)` |  |
| `generated_at` | `datetime` | `True` | `` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:1188-1198](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1188-L1198)
