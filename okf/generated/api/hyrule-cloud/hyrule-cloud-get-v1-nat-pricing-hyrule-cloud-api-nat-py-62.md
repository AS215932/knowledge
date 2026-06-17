---
type: API Endpoint
title: GET /v1/nat/pricing
description: Static API endpoint `GET /v1/nat/pricing` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/nat.py#L62-L66
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
  lines: 62-66
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/nat.py#L62-L66
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/nat/pricing
source_path: hyrule_cloud/api/nat.py
function_name: get_nat_pricing
request_models: []
response_model: NATPricingResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/nat/pricing` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/nat.py:62` |
| Function/handler | `get_nat_pricing` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `NATPricingResponse` |
| Response model | `NATPricingResponse` |

# Request/response models

* [NATPricingResponse](../../schemas/hyrule-cloud/NATPricingResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/nat.py:62-66](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/nat.py#L62-L66)
