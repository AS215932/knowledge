---
type: API Endpoint
title: GET /faq
description: Static API endpoint `GET /faq` in AS215932/hyrule-web.
resource: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/hyrule_web/app.py#L947-L957
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
  lines: 947-957
  url: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/hyrule_web/app.py#L947-L957
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-web
method: GET
route: /faq
source_path: hyrule_web/app.py
function_name: page_faq
request_models: []
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/faq` |
| Repository | `AS215932/hyrule-web` |
| Source | `hyrule_web/app.py:947` |
| Function/handler | `page_faq` |
| Router | `app` |
| Status codes | `Not statically detected` |
| Return annotation | `Response` |
| Response model | `not statically declared` |

# Request/response models

No request or response model statically detected.

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

FAQ + FAQPage JSON-LD (Block G). Only mentions live payment methods —
the chain list comes from /v1/payments/networks, never hardcoded.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_web/app.py:947-957](https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/hyrule_web/app.py#L947-L957)
