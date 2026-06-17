---
type: API Endpoint
title: POST /approval/resume
description: Static API endpoint `POST /approval/resume` in AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L1087-L1098
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
  lines: 1087-1098
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L1087-L1098
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
method: POST
route: /approval/resume
source_path: app/main.py
function_name: signed_resume
request_models:
- SignedApprovalRequest
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/approval/resume` |
| Repository | `AS215932/noc-agent` |
| Source | `app/main.py:1087` |
| Function/handler | `signed_resume` |
| Router | `app` |
| Status codes | `404` |
| Return annotation | `not annotated` |
| Response model | `not statically declared` |

# Request/response models

* `SignedApprovalRequest`

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [app/main.py:1087-1098](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L1087-L1098)
