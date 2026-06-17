---
type: API Endpoint
title: GET /v1/web/pricing
description: Static API endpoint `GET /v1/web/pricing` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/web.py#L61-L66
tags:
- api
- get
- hyrule-cloud
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/web.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 61-66
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/web.py#L61-L66
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/web/pricing
source_path: hyrule_cloud/api/web.py
function_name: get_web_pricing
request_models: []
response_model: WebPricingResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/web/pricing` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/web.py:61` |
| Function/handler | `get_web_pricing` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `WebPricingResponse` |
| Response model | `WebPricingResponse` |

# Request/response models

* [WebPricingResponse](/generated/schemas/hyrule-cloud/WebPricingResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/web.py:61-66](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/web.py#L61-L66)
