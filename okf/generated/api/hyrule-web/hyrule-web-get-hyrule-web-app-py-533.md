---
type: API Endpoint
title: GET /
description: Static API endpoint `GET /` in AS215932/hyrule-web.
resource: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/hyrule_web/app.py#L533-L549
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
  lines: 533-549
  url: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/hyrule_web/app.py#L533-L549
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-web
method: GET
route: /
source_path: hyrule_web/app.py
function_name: page_index
request_models: []
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/` |
| Repository | `AS215932/hyrule-web` |
| Source | `hyrule_web/app.py:533` |
| Function/handler | `page_index` |
| Router | `app` |
| Status codes | `Not statically detected` |
| Return annotation | `Response` |
| Response model | `not statically declared` |

# Request/response models

No request or response model statically detected.

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

Block B: homepage pulls live runtime stats. Replaces the hardcoded
`api · 24ms / queue 3 / 58s / 1284 VMs` block with values from the
backend, cached for 15s and stale-on-error.

Issue #14: the settlement-chain copy is also driven from the live
/v1/payments/networks list (single source of truth, same as /faq and
llms.txt) — never hardcoded — per [[feedback_verified_payment_chains]].

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_web/app.py:533-549](https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/hyrule_web/app.py#L533-L549)
