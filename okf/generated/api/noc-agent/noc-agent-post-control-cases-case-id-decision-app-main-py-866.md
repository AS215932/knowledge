---
type: API Endpoint
title: POST /control/cases/{case_id}/decision
description: Static API endpoint `POST /control/cases/{case_id}/decision` in AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L866-L886
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
  lines: 866-886
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L866-L886
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
method: POST
route: /control/cases/{case_id}/decision
source_path: app/main.py
function_name: control_case_decision
request_models:
- LocalDecisionRequest
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/control/cases/{case_id}/decision` |
| Repository | `AS215932/noc-agent` |
| Source | `app/main.py:866` |
| Function/handler | `control_case_decision` |
| Router | `app` |
| Status codes | `404` |
| Return annotation | `not annotated` |
| Response model | `not statically declared` |

# Request/response models

* [LocalDecisionRequest](/generated/schemas/noc-agent/LocalDecisionRequest.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [app/main.py:866-886](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L866-L886)
