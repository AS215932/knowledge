---
type: API Endpoint
title: GET /control/proactive/status
description: Static API endpoint `GET /control/proactive/status` in AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L921-L952
tags:
- api
- get
- noc-agent
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: app/main.py
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  lines: 921-952
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L921-L952
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
method: GET
route: /control/proactive/status
source_path: app/main.py
function_name: control_proactive_status
request_models: []
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/control/proactive/status` |
| Repository | `AS215932/noc-agent` |
| Source | `app/main.py:921` |
| Function/handler | `control_proactive_status` |
| Router | `app` |
| Status codes | `Not statically detected` |
| Return annotation | `not annotated` |
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

[1] [app/main.py:921-952](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L921-L952)
