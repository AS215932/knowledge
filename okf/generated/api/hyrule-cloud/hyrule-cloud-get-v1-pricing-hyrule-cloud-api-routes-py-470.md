---
type: API Endpoint
title: GET /v1/pricing
description: Static API endpoint `GET /v1/pricing` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L470-L486
tags:
- api
- get
- hyrule-cloud
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/routes.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 470-486
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L470-L486
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/pricing
source_path: hyrule_cloud/api/routes.py
function_name: get_pricing
request_models: []
response_model: PricingResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/pricing` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/routes.py:470` |
| Function/handler | `get_pricing` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `PricingResponse` |
| Response model | `PricingResponse` |

# Request/response models

* [PricingResponse](/generated/schemas/hyrule-cloud/PricingResponse.md)

# Dependencies

* `get_cfg`

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/routes.py:470-486](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L470-L486)
