---
type: API Endpoint
title: GET /v1/products/vms
description: Static API endpoint `GET /v1/products/vms` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L498-L514
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
  lines: 498-514
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L498-L514
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/products/vms
source_path: hyrule_cloud/api/routes.py
function_name: get_vm_products
request_models: []
response_model: VMProductsResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/products/vms` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/routes.py:498` |
| Function/handler | `get_vm_products` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `VMProductsResponse` |
| Response model | `VMProductsResponse` |

# Request/response models

* [VMProductsResponse](../../schemas/hyrule-cloud/VMProductsResponse.md)

# Dependencies

* `get_cfg`

# Function documentation

Issue #14: machine-readable VM catalog (specs + daily price per size) so
agents get the product list without scraping the /services HTML. Sourced from
VM_SPECS + the configured per-size prices (the same source as /v1/pricing).

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/routes.py:498-514](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L498-L514)
