---
type: API Endpoint
title: GET /v1/mx/tools
description: Static API endpoint `GET /v1/mx/tools` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mx.py#L69-L75
tags:
- api
- get
- hyrule-cloud
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/mx.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 69-75
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mx.py#L69-L75
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/mx/tools
source_path: hyrule_cloud/api/mx.py
function_name: get_mx_tools
request_models: []
response_model: MXToolsResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/mx/tools` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/mx.py:69` |
| Function/handler | `get_mx_tools` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `MXToolsResponse` |
| Response model | `MXToolsResponse` |

# Request/response models

* [MXToolsResponse](/generated/schemas/hyrule-cloud/MXToolsResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/mx.py:69-75](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mx.py#L69-L75)
