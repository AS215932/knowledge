---
type: API Endpoint
title: GET /v1/ip/{address}/rdns
description: Static API endpoint `GET /v1/ip/{address}/rdns` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/ip.py#L82-L85
tags:
- api
- get
- hyrule-cloud
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/ip.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 82-85
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/ip.py#L82-L85
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/ip/{address}/rdns
source_path: hyrule_cloud/api/ip.py
function_name: ip_rdns
request_models: []
response_model: IPLookupResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/ip/{address}/rdns` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/ip.py:82` |
| Function/handler | `ip_rdns` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `IPLookupResponse | Response` |
| Response model | `IPLookupResponse` |

# Request/response models

* [IPLookupResponse](/generated/schemas/hyrule-cloud/IPLookupResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/ip.py:82-85](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/ip.py#L82-L85)
