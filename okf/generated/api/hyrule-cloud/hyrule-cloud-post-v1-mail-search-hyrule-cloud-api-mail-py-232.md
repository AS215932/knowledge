---
type: API Endpoint
title: POST /v1/mail/search
description: Static API endpoint `POST /v1/mail/search` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L232-L233
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
  lines: 232-233
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L232-L233
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/mail/search
source_path: hyrule_cloud/api/mail.py
function_name: search_mail_messages
request_models:
- MailSearchRequest
response_model: MailMessageListResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/mail/search` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/mail.py:232` |
| Function/handler | `search_mail_messages` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `JSONResponse` |
| Response model | `MailMessageListResponse` |

# Request/response models

* [MailSearchRequest](/generated/schemas/hyrule-cloud/MailSearchRequest.md)
* [MailMessageListResponse](/generated/schemas/hyrule-cloud/MailMessageListResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/mail.py:232-233](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L232-L233)
