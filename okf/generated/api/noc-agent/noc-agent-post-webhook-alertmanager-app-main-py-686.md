---
type: API Endpoint
title: POST /webhook/alertmanager
description: Static API endpoint `POST /webhook/alertmanager` in AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L686-L701
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
  lines: 686-701
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L686-L701
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
method: POST
route: /webhook/alertmanager
source_path: app/main.py
function_name: alertmanager_webhook
request_models:
- AlertManagerPayload
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/webhook/alertmanager` |
| Repository | `AS215932/noc-agent` |
| Source | `app/main.py:686` |
| Function/handler | `alertmanager_webhook` |
| Router | `app` |
| Status codes | `Not statically detected` |
| Return annotation | `not annotated` |
| Response model | `not statically declared` |

# Request/response models

* [AlertManagerPayload](../../schemas/noc-agent/AlertManagerPayload.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

Receives alerts from Prometheus Alertmanager and triggers the NOC agent.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [app/main.py:686-701](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/app/main.py#L686-L701)
