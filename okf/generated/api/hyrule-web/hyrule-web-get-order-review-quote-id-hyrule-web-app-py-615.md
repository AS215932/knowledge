---
type: API Endpoint
title: GET /order/review/{quote_id}
description: Static API endpoint `GET /order/review/{quote_id}` in AS215932/hyrule-web.
resource: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/hyrule_web/app.py#L615-L653
tags:
- api
- get
- hyrule-web
timestamp: '2026-06-16T15:09:49Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-web
  path: hyrule_web/app.py
  commit: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
  lines: 615-653
  url: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/hyrule_web/app.py#L615-L653
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-web
method: GET
route: /order/review/{quote_id}
source_path: hyrule_web/app.py
function_name: page_review_quote
request_models: []
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/order/review/{quote_id}` |
| Repository | `AS215932/hyrule-web` |
| Source | `hyrule_web/app.py:615` |
| Function/handler | `page_review_quote` |
| Router | `app` |
| Status codes | `Not statically detected` |
| Return annotation | `Response` |
| Response model | `not statically declared` |

# Request/response models

No request or response model statically detected.

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

Issue #14: reload-safe review page backed by a durable quote.

The order form (order.ts) creates a quote and sends the browser here, so a
mobile wallet handoff that reloads the page just re-GETs this URL and the
order is re-rendered from the backend — no lost POST body. Unknown quote →
back to the order form; expired quote → render with a restart banner.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_web/app.py:615-653](https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/hyrule_web/app.py#L615-L653)
