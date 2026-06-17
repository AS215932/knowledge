---
type: API Endpoint
title: GET /v1/mail/accounts/{mailbox_id}/delivery-log
description: Static API endpoint `GET /v1/mail/accounts/{mailbox_id}/delivery-log`
  in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L306-L307
tags:
- api
- get
- hyrule-cloud
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/mail.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 306-307
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L306-L307
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/mail/accounts/{mailbox_id}/delivery-log
source_path: hyrule_cloud/api/mail.py
function_name: list_mail_delivery_log
request_models: []
response_model: None
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/mail/accounts/{mailbox_id}/delivery-log` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/mail.py:306` |
| Function/handler | `list_mail_delivery_log` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `Response` |
| Response model | `None` |

# Request/response models

No request or response model statically detected.

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/mail.py:306-307](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L306-L307)
