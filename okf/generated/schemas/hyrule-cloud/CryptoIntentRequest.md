---
type: API Schema
title: CryptoIntentRequest
description: Pydantic API schema `CryptoIntentRequest` from AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L379-L392
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
  lines: 379-392
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L379-L392
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
model: CryptoIntentRequest
source_path: hyrule_cloud/models.py
---

# API schema

| Field | Value |
| --- | --- |
| Model | `CryptoIntentRequest` |
| Source | `hyrule_cloud/models.py:379` |
| Bases | `BaseModel` |

# Fields

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `asset` | `str` | `False` | `Field(description='Asset symbol: BTC or XMR')` | Asset symbol: BTC or XMR |
| `order_payload` | `VMCreateRequest` | `False` | `Field(description='The VM spec to provision once the payment settles.')` | The VM spec to provision once the payment settles. |
| `client_order_id` | `str | None` | `False` | `Field(default=None, max_length=64, description='Idempotency key. Repeated POS...` | Idempotency key. Repeated POSTs with the same key return the same intent. |

# Validators

No validators statically detected.

# Documentation

Block E: payment-intent creation. `order_payload` carries the full VM
spec so the orchestrator can provision on settlement without re-asking
the client. `client_order_id` is the idempotency key.

# Citations

[1] [hyrule_cloud/models.py:379-392](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/models.py#L379-L392)
