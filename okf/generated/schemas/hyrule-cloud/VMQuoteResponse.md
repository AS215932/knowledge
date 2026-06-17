---
type: API Schema
title: VMQuoteResponse
description: Pydantic API schema `VMQuoteResponse` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L256-L264
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
  lines: 256-264
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L256-L264
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: VMQuoteResponse
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `VMQuoteResponse` |
| Source | `hyrule_cloud/models.py:256` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `quote_id` | `str` | `True` | `` |  |
| `status` | `QuoteStatus` | `True` | `` |  |
| `order_payload` | `VMCreateRequest` | `True` | `` |  |
| `amount_usd` | `str` | `True` | `` |  |
| `currency` | `str` | `False` | `<string>` |  |
| `accepted_payment_methods` | `AcceptedPaymentMethods` | `True` | `` |  |
| `created_at` | `datetime` | `True` | `` |  |
| `expires_at` | `datetime` | `True` | `` |  |

# Validators

No validators statically detected.

# Documentation

No class docstring found in source.

# Citations

[1] [hyrule_cloud/models.py:256-264](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L256-L264)
