---
type: API Endpoint
title: POST /webhook/icinga
description: Static API endpoint `POST /webhook/icinga` in AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L705-L719
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
  lines: 705-719
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L705-L719
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
method: POST
route: /webhook/icinga
source_path: app/main.py
function_name: icinga_webhook
request_models: []
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/webhook/icinga` |
| Repository | `AS215932/noc-agent` |
| Source | `app/main.py:705` |
| Function/handler | `icinga_webhook` |
| Router | `app` |
| Status codes | `Not statically detected` |
| Return annotation | `not annotated` |
| Response model | `not statically declared` |

# Request/response models

No request or response model statically detected.

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

Receives Icinga2 NotificationCommand POSTs and triggers the NOC agent.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [app/main.py:705-719](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L705-L719)
