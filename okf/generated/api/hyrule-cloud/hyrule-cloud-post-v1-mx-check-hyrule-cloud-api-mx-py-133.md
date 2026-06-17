---
type: API Endpoint
title: POST /v1/mx/check
description: Static API endpoint `POST /v1/mx/check` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mx.py#L133-L136
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/mx.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 133-136
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mx.py#L133-L136
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/mx/check
source_path: hyrule_cloud/api/mx.py
function_name: mx_check
request_models:
- MXCheckRequest
response_model: MXCheckResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/mx/check` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/mx.py:133` |
| Function/handler | `mx_check` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `MXCheckResponse | Response` |
| Response model | `MXCheckResponse` |

# Request/response models

* [MXCheckRequest](../../schemas/hyrule-cloud/MXCheckRequest.md)
* [MXCheckResponse](../../schemas/hyrule-cloud/MXCheckResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/mx.py:133-136](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mx.py#L133-L136)
