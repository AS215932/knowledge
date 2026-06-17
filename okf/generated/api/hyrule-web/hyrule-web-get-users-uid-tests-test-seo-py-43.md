---
type: API Endpoint
title: GET /users/{uid}
description: Static API endpoint `GET /users/{uid}` in AS215932/hyrule-web.
resource: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/tests/test_seo.py#L43-L44
tags:
- api
- get
- hyrule-web
timestamp: '2026-06-16T15:09:49Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-web
  path: tests/test_seo.py
  commit: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
  lines: 43-44
  url: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/tests/test_seo.py#L43-L44
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-web
method: GET
route: /users/{uid}
source_path: tests/test_seo.py
function_name: user
request_models: []
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/users/{uid}` |
| Repository | `AS215932/hyrule-web` |
| Source | `tests/test_seo.py:43` |
| Function/handler | `user` |
| Router | `a` |
| Status codes | `Not statically detected` |
| Return annotation | `str` |
| Response model | `not statically declared` |

# Request/response models

No request or response model statically detected.

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [tests/test_seo.py:43-44](https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/tests/test_seo.py#L43-L44)
