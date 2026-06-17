---
type: API Endpoint
title: POST /v1/bgp/lookup
description: Static API endpoint `POST /v1/bgp/lookup` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/bgp.py#L165-L175
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/bgp.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 165-175
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/bgp.py#L165-L175
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/bgp/lookup
source_path: hyrule_cloud/api/bgp.py
function_name: bgp_lookup
request_models:
- BGPLookupRequest
response_model: BGPLookupResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/bgp/lookup` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/bgp.py:165` |
| Function/handler | `bgp_lookup` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `BGPLookupResponse | Response` |
| Response model | `BGPLookupResponse` |

# Request/response models

* [BGPLookupRequest](../../schemas/hyrule-cloud/BGPLookupRequest.md)
* [BGPLookupResponse](../../schemas/hyrule-cloud/BGPLookupResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/bgp.py:165-175](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/bgp.py#L165-L175)
