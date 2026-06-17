---
type: API Endpoint
title: POST /v1/mail/messages/{message_id}/forward
description: Static API endpoint `POST /v1/mail/messages/{message_id}/forward` in
  AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L266-L267
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/mail.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 266-267
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L266-L267
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/mail/messages/{message_id}/forward
source_path: hyrule_cloud/api/mail.py
function_name: forward_mail_message
request_models:
- MailMessageActionRequest
response_model: MailMessageResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/mail/messages/{message_id}/forward` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/mail.py:266` |
| Function/handler | `forward_mail_message` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `JSONResponse` |
| Response model | `MailMessageResponse` |

# Request/response models

* [MailMessageActionRequest](/generated/schemas/hyrule-cloud/MailMessageActionRequest.md)
* `MailMessageResponse`

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/mail.py:266-267](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L266-L267)
