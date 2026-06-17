---
type: API Endpoint
title: GET /v1/bgp/status
description: Static API endpoint `GET /v1/bgp/status` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/bgp.py#L57-L63
tags:
- api
- get
- hyrule-cloud
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/bgp.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 57-63
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/bgp.py#L57-L63
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/bgp/status
source_path: hyrule_cloud/api/bgp.py
function_name: get_bgp_status
request_models: []
response_model: BGPStatusResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/bgp/status` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/bgp.py:57` |
| Function/handler | `get_bgp_status` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `BGPStatusResponse` |
| Response model | `BGPStatusResponse` |

# Request/response models

* [BGPStatusResponse](/generated/schemas/hyrule-cloud/BGPStatusResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

Free Hyrule/AS215932 BGP status.

This endpoint is intentionally scoped to Hyrule's own monitored network.
Arbitrary prefix/IP/ASN investigation belongs to /v1/bgp/lookup.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/bgp.py:57-63](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/bgp.py#L57-L63)
