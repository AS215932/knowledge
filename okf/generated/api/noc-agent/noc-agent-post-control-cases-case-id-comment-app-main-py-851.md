---
type: API Endpoint
title: POST /control/cases/{case_id}/comment
description: Static API endpoint `POST /control/cases/{case_id}/comment` in AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L851-L862
tags:
- api
- noc-agent
- post
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: app/main.py
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 851-862
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L851-L862
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
method: POST
route: /control/cases/{case_id}/comment
source_path: app/main.py
function_name: control_case_comment
request_models:
- CommentRequest
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/control/cases/{case_id}/comment` |
| Repository | `AS215932/noc-agent` |
| Source | `app/main.py:851` |
| Function/handler | `control_case_comment` |
| Router | `app` |
| Status codes | `404` |
| Return annotation | `not annotated` |
| Response model | `not statically declared` |

# Request/response models

* [CommentRequest](/generated/schemas/noc-agent/CommentRequest.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [app/main.py:851-862](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L851-L862)
