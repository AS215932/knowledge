---
type: API Endpoint
title: POST /v1/me/api-keys
description: Static API endpoint `POST /v1/me/api-keys` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L1025-L1071
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/auth.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1025-1071
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L1025-L1071
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/me/api-keys
source_path: hyrule_cloud/api/auth.py
function_name: create_api_key_endpoint
request_models:
- ApiKeyCreateRequest
response_model: ApiKeyCreateResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/me/api-keys` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/auth.py:1025` |
| Function/handler | `create_api_key_endpoint` |
| Router | `router` |
| Status codes | `400, 403, 503` |
| Return annotation | `ApiKeyCreateResponse` |
| Response model | `ApiKeyCreateResponse` |

# Request/response models

* [ApiKeyCreateRequest](../../schemas/hyrule-cloud/ApiKeyCreateRequest.md)
* [ApiKeyCreateResponse](../../schemas/hyrule-cloud/ApiKeyCreateResponse.md)

# Dependencies

* `get_app_state`
* `require_account`

# Function documentation

Mint a new API key. The cleartext bearer is in the response — show
once and discard. Re-fetching the key from /v1/me/api-keys returns the
summary only; the cleartext is not stored server-side.

Scope rules:
  - Cookie session: any scope is allowed (you have full account access).
  - API key: needs `api_keys:write` AND every requested scope must be a
    subset of the issuing key's scopes (no escalation — a vm:read-only
    key cannot mint a vm:destroy key).

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/auth.py:1025-1071](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L1025-L1071)
