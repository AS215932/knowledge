---
type: API Endpoint
title: GET /dashboard
description: Static API endpoint `GET /dashboard` in AS215932/hyrule-web.
resource: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/hyrule_web/app.py#L833-L849
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
  lines: 833-849
  url: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/hyrule_web/app.py#L833-L849
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-web
method: GET
route: /dashboard
source_path: hyrule_web/app.py
function_name: page_dashboard
request_models: []
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/dashboard` |
| Repository | `AS215932/hyrule-web` |
| Source | `hyrule_web/app.py:833` |
| Function/handler | `page_dashboard` |
| Router | `app` |
| Status codes | `Not statically detected` |
| Return annotation | `Response` |
| Response model | `not statically declared` |

# Request/response models

No request or response model statically detected.

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

Renders the signed-in dashboard. /v1/me 401 → redirect to /login. Any
other backend failure renders the shell with an error banner so the user
can still log out / claim a VM without a forced loop.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_web/app.py:833-849](https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/hyrule_web/app.py#L833-L849)
