---
type: API Endpoint
title: POST /v1/auth/login
description: Static API endpoint `POST /v1/auth/login` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L366-L403
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
  lines: 366-403
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L366-L403
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/auth/login
source_path: hyrule_cloud/api/auth.py
function_name: login
request_models:
- AuthLoginRequest
response_model: AuthLoginResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/auth/login` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/auth.py:366` |
| Function/handler | `login` |
| Router | `router` |
| Status codes | `401, 503` |
| Return annotation | `AuthLoginResponse` |
| Response model | `AuthLoginResponse` |

# Request/response models

* [AuthLoginRequest](../../schemas/hyrule-cloud/AuthLoginRequest.md)
* [AuthLoginResponse](../../schemas/hyrule-cloud/AuthLoginResponse.md)

# Dependencies

* `get_app_state`

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/auth.py:366-403](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L366-L403)
