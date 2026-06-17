---
type: API Endpoint
title: POST /dashboard/vms/{vm_id}/destroy
description: Static API endpoint `POST /dashboard/vms/{vm_id}/destroy` in AS215932/hyrule-web.
resource: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/hyrule_web/app.py#L865-L868
tags:
- api
- hyrule-web
- post
timestamp: '2026-06-16T15:09:49Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-web
  path: hyrule_web/app.py
  commit: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
  lines: 865-868
  url: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/hyrule_web/app.py#L865-L868
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-web
method: POST
route: /dashboard/vms/{vm_id}/destroy
source_path: hyrule_web/app.py
function_name: dash_destroy
request_models: []
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/dashboard/vms/{vm_id}/destroy` |
| Repository | `AS215932/hyrule-web` |
| Source | `hyrule_web/app.py:865` |
| Function/handler | `dash_destroy` |
| Router | `app` |
| Status codes | `Not statically detected` |
| Return annotation | `Response` |
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

[1] [hyrule_web/app.py:865-868](https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/hyrule_web/app.py#L865-L868)
