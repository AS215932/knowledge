---
type: API Endpoint
title: POST /v1/intent/create
description: Static API endpoint `POST /v1/intent/create` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L1226-L1275
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/routes.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1226-1275
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L1226-L1275
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/intent/create
source_path: hyrule_cloud/api/routes.py
function_name: create_crypto_intent
request_models:
- CryptoIntentRequest
response_model: CryptoIntentResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/intent/create` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/routes.py:1226` |
| Function/handler | `create_crypto_intent` |
| Router | `router` |
| Status codes | `400, 503` |
| Return annotation | `CryptoIntentResponse` |
| Response model | `CryptoIntentResponse` |

# Request/response models

* [CryptoIntentRequest](/generated/schemas/hyrule-cloud/CryptoIntentRequest.md)
* [CryptoIntentResponse](/generated/schemas/hyrule-cloud/CryptoIntentResponse.md)

# Dependencies

* `current_account`
* `get_cfg`
* `get_orch`

# Function documentation

Block E: open a payment intent for BTC or XMR.

Idempotent on `client_order_id`: repeated POSTs with the same key return
the existing intent unchanged (no second deposit address is allocated).

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/routes.py:1226-1275](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L1226-L1275)
