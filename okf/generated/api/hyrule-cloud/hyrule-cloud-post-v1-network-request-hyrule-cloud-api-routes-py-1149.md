---
type: API Endpoint
title: POST /v1/network/request
description: Static API endpoint `POST /v1/network/request` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L1149-L1182
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
  lines: 1149-1182
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L1149-L1182
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/network/request
source_path: hyrule_cloud/api/routes.py
function_name: proxy_network_request
request_models:
- NetworkRequest
response_model: NetworkResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/network/request` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/routes.py:1149` |
| Function/handler | `proxy_network_request` |
| Router | `router` |
| Status codes | `503` |
| Return annotation | `not annotated` |
| Response model | `NetworkResponse` |

# Request/response models

* [NetworkRequest](/generated/schemas/hyrule-cloud/NetworkRequest.md)
* [NetworkResponse](/generated/schemas/hyrule-cloud/NetworkResponse.md)

# Dependencies

* `get_cfg`
* `get_gate`
* `get_network`

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/routes.py:1149-1182](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L1149-L1182)
