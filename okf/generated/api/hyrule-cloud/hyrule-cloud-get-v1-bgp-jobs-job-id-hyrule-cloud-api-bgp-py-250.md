---
type: API Endpoint
title: GET /v1/bgp/jobs/{job_id}
description: Static API endpoint `GET /v1/bgp/jobs/{job_id}` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/bgp.py#L250-L267
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
  lines: 250-267
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/bgp.py#L250-L267
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/bgp/jobs/{job_id}
source_path: hyrule_cloud/api/bgp.py
function_name: get_bgp_job
request_models: []
response_model: BGPJobResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/bgp/jobs/{job_id}` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/bgp.py:250` |
| Function/handler | `get_bgp_job` |
| Router | `router` |
| Status codes | `404` |
| Return annotation | `BGPJobResponse` |
| Response model | `BGPJobResponse` |

# Request/response models

* [BGPJobResponse](/generated/schemas/hyrule-cloud/BGPJobResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/bgp.py:250-267](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/bgp.py#L250-L267)
