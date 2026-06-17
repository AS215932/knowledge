---
type: API Endpoint
title: POST /v1/vm/quote
description: Static API endpoint `POST /v1/vm/quote` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L743-L788
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/routes.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 743-788
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L743-L788
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/vm/quote
source_path: hyrule_cloud/api/routes.py
function_name: create_vm_quote
request_models:
- VMQuoteRequest
response_model: VMQuoteResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/vm/quote` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/routes.py:743` |
| Function/handler | `create_vm_quote` |
| Router | `router` |
| Status codes | `201, 400, 409` |
| Return annotation | `Response` |
| Response model | `VMQuoteResponse` |

# Request/response models

* [VMQuoteRequest](../../schemas/hyrule-cloud/VMQuoteRequest.md)
* [VMQuoteResponse](../../schemas/hyrule-cloud/VMQuoteResponse.md)

# Dependencies

* `current_account`
* `get_cfg`
* `get_orch`

# Function documentation

Issue #14: price a VM order once and persist it as a durable quote.

Returns a `quote_id` the UI/agent pays against — it survives review-page
reloads and mobile wallet handoffs and locks the price for its TTL.
Idempotent on `client_order_id`: same key + same spec returns the existing
quote (200); same key + a different spec is a 409 conflict.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/routes.py:743-788](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L743-L788)
