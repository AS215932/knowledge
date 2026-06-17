---
type: API Endpoint
title: GET /v1/nat/ip
description: Static API endpoint `GET /v1/nat/ip` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/nat.py#L46-L58
tags:
- api
- get
- hyrule-cloud
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/nat.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 46-58
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/nat.py#L46-L58
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/nat/ip
source_path: hyrule_cloud/api/nat.py
function_name: nat_ip
request_models: []
response_model: NATIPResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/nat/ip` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/nat.py:46` |
| Function/handler | `nat_ip` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `NATIPResponse` |
| Response model | `NATIPResponse` |

# Request/response models

* [NATIPResponse](/generated/schemas/hyrule-cloud/NATIPResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/nat.py:46-58](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/nat.py#L46-L58)
