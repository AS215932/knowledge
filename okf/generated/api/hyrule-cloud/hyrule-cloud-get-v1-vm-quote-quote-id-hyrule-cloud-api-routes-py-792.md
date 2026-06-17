---
type: API Endpoint
title: GET /v1/vm/quote/{quote_id}
description: Static API endpoint `GET /v1/vm/quote/{quote_id}` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L792-L811
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
  lines: 792-811
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L792-L811
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/vm/quote/{quote_id}
source_path: hyrule_cloud/api/routes.py
function_name: get_vm_quote
request_models: []
response_model: VMQuoteResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/vm/quote/{quote_id}` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/routes.py:792` |
| Function/handler | `get_vm_quote` |
| Router | `router` |
| Status codes | `404` |
| Return annotation | `VMQuoteResponse` |
| Response model | `VMQuoteResponse` |

# Request/response models

* [VMQuoteResponse](../../schemas/hyrule-cloud/VMQuoteResponse.md)

# Dependencies

* `current_account`
* `get_cfg`
* `get_orch`

# Function documentation

Restore a durable quote by id (reload-safe). Expired quotes still return
200 with status=expired so the UI can render a restart state.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/routes.py:792-811](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L792-L811)
