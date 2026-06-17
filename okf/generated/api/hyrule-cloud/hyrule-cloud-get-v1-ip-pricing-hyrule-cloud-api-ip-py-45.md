---
type: API Endpoint
title: GET /v1/ip/pricing
description: Static API endpoint `GET /v1/ip/pricing` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/ip.py#L45-L46
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
  lines: 45-46
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/ip.py#L45-L46
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/ip/pricing
source_path: hyrule_cloud/api/ip.py
function_name: get_ip_pricing
request_models: []
response_model: IPPricingResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/ip/pricing` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/ip.py:45` |
| Function/handler | `get_ip_pricing` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `IPPricingResponse` |
| Response model | `IPPricingResponse` |

# Request/response models

* [IPPricingResponse](../../schemas/hyrule-cloud/IPPricingResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/ip.py:45-46](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/ip.py#L45-L46)
