---
type: API Endpoint
title: POST /mail/poll
description: Static API endpoint `POST /mail/poll` in AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L723-L726
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
  lines: 723-726
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L723-L726
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
method: POST
route: /mail/poll
source_path: app/main.py
function_name: poll_mailbox
request_models: []
response_model: MailPollResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/mail/poll` |
| Repository | `AS215932/noc-agent` |
| Source | `app/main.py:723` |
| Function/handler | `poll_mailbox` |
| Router | `app` |
| Status codes | `Not statically detected` |
| Return annotation | `not annotated` |
| Response model | `MailPollResponse` |

# Request/response models

* [MailPollResponse](../../schemas/noc-agent/MailPollResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

Poll the shared NOC mailbox and store draft replies for human approval.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [app/main.py:723-726](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L723-L726)
