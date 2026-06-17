---
type: API Endpoint
title: GET /v1/intent/{intent_id}
description: Static API endpoint `GET /v1/intent/{intent_id}` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L1279-L1317
tags:
- api
- get
- hyrule-cloud
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/routes.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1279-1317
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L1279-L1317
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/intent/{intent_id}
source_path: hyrule_cloud/api/routes.py
function_name: get_crypto_intent_status
request_models: []
response_model: CryptoIntentResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/intent/{intent_id}` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/routes.py:1279` |
| Function/handler | `get_crypto_intent_status` |
| Router | `router` |
| Status codes | `404` |
| Return annotation | `CryptoIntentResponse` |
| Response model | `CryptoIntentResponse` |

# Request/response models

* [CryptoIntentResponse](/generated/schemas/hyrule-cloud/CryptoIntentResponse.md)

# Dependencies

* `current_account`
* `get_orch`

# Function documentation

Returns current intent state. On the first GET after PROVISIONED, the
one-shot `anon_token_cleartext` column is included in the response AND
immediately nulled so subsequent GETs cannot re-reveal it.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/routes.py:1279-1317](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L1279-L1317)
