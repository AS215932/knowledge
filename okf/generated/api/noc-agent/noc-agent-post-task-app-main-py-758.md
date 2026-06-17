---
type: API Endpoint
title: POST /task
description: Static API endpoint `POST /task` in AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L758-L780
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
  lines: 758-780
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L758-L780
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
method: POST
route: /task
source_path: app/main.py
function_name: run_task
request_models:
- TaskRequest
response_model: MailPollResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/task` |
| Repository | `AS215932/noc-agent` |
| Source | `app/main.py:758` |
| Function/handler | `run_task` |
| Router | `app` |
| Status codes | `Not statically detected` |
| Return annotation | `not annotated` |
| Response model | `MailPollResponse` |

# Request/response models

* [TaskRequest](/generated/schemas/noc-agent/TaskRequest.md)
* [MailPollResponse](/generated/schemas/noc-agent/MailPollResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

Run an arbitrary task on the NOC Triage agent (e.g. 'Draft email to LocIX').

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [app/main.py:758-780](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L758-L780)
