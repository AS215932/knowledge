---
type: API Schema
title: AcceptedPaymentMethods
description: Pydantic API schema `AcceptedPaymentMethods` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L248-L253
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
  lines: 248-253
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L248-L253
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: AcceptedPaymentMethods
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `AcceptedPaymentMethods` |
| Source | `hyrule_cloud/models.py:248` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `evm` | `list[QuoteEvmMethod]` | `False` | `Field(default_factory=list)` |  |
| `native` | `list[str]` | `False` | `Field(default_factory=list)` |  |

# Validators

No validators statically detected.

# Documentation

Single source of truth, derived from live backend config: enabled EVM
chains + whether the native (BTC/XMR) intent rail is wired.

# Citations

[1] [hyrule_cloud/models.py:248-253](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L248-L253)
