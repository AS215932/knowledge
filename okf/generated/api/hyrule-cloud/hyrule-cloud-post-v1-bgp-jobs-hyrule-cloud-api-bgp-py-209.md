---
type: API Endpoint
title: POST /v1/bgp/jobs
description: Static API endpoint `POST /v1/bgp/jobs` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/bgp.py#L209-L246
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
  lines: 209-246
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/bgp.py#L209-L246
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/bgp/jobs
source_path: hyrule_cloud/api/bgp.py
function_name: create_bgpstream_job
request_models:
- BGPStreamJobRequest
response_model: BGPJobResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/bgp/jobs` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/bgp.py:209` |
| Function/handler | `create_bgpstream_job` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `BGPJobResponse | Response` |
| Response model | `BGPJobResponse` |

# Request/response models

* [BGPStreamJobRequest](../../schemas/hyrule-cloud/BGPStreamJobRequest.md)
* [BGPJobResponse](../../schemas/hyrule-cloud/BGPJobResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/bgp.py:209-246](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/bgp.py#L209-L246)
