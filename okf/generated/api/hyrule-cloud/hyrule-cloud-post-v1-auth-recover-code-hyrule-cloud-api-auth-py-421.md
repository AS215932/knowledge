---
type: API Endpoint
title: POST /v1/auth/recover/code
description: Static API endpoint `POST /v1/auth/recover/code` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L421-L470
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
  lines: 421-470
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L421-L470
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/auth/recover/code
source_path: hyrule_cloud/api/auth.py
function_name: recover_with_code
request_models:
- RecoveryCodeRequest
response_model: RecoveryCodeResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/auth/recover/code` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/auth.py:421` |
| Function/handler | `recover_with_code` |
| Router | `router` |
| Status codes | `401, 503` |
| Return annotation | `RecoveryCodeResponse` |
| Response model | `RecoveryCodeResponse` |

# Request/response models

* [RecoveryCodeRequest](../../schemas/hyrule-cloud/RecoveryCodeRequest.md)
* [RecoveryCodeResponse](../../schemas/hyrule-cloud/RecoveryCodeResponse.md)

# Dependencies

* `get_app_state`

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/auth.py:421-470](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L421-L470)
