---
type: API Endpoint
title: POST /v1/mx/bounce/parse
description: Static API endpoint `POST /v1/mx/bounce/parse` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mx.py#L140-L143
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
  lines: 140-143
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mx.py#L140-L143
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/mx/bounce/parse
source_path: hyrule_cloud/api/mx.py
function_name: parse_mx_bounce
request_models:
- MailBounceParseRequest
response_model: MailBounceParseResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/mx/bounce/parse` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/mx.py:140` |
| Function/handler | `parse_mx_bounce` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `MailBounceParseResponse | Response` |
| Response model | `MailBounceParseResponse` |

# Request/response models

* [MailBounceParseRequest](/generated/schemas/hyrule-cloud/MailBounceParseRequest.md)
* [MailBounceParseResponse](/generated/schemas/hyrule-cloud/MailBounceParseResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/mx.py:140-143](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mx.py#L140-L143)
