---
type: API Schema
title: IPLookupResponse
description: Pydantic API schema `IPLookupResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1124-L1136
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
  lines: 1124-1136
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1124-L1136
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: IPLookupResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `IPLookupResponse` |
| Source | `hyrule_cloud/models.py:1124` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `request_id` | `str` | `True` | `` |  |
| `address` | `str` | `True` | `` |  |
| `geo` | `IPGeoResult | None` | `False` | `None` |  |
| `network` | `IPNetworkResult | None` | `False` | `None` |  |
| `reverse_dns` | `list[str]` | `False` | `Field(default_factory=list)` |  |
| `rdap` | `dict[str, object] | None` | `False` | `None` |  |
| `whois` | `dict[str, object] | None` | `False` | `None` |  |
| `reputation` | `IPReputationResult | None` | `False` | `None` |  |
| `bgp` | `dict[str, object] | None` | `False` | `None` |  |
| `sources` | `dict[str, str]` | `False` | `Field(default_factory=dict)` |  |
| `partial` | `bool` | `False` | `False` |  |
| `generated_at` | `datetime` | `True` | `` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:1124-1136](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L1124-L1136)
