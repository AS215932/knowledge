---
type: API Endpoint
title: POST /v1/mail/accounts
description: Static API endpoint `POST /v1/mail/accounts` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L107-L113
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
  lines: 107-113
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L107-L113
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/mail/accounts
source_path: hyrule_cloud/api/mail.py
function_name: create_mail_account
request_models:
- MailAccountCreateRequest
response_model: MailAccountResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/mail/accounts` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/mail.py:107` |
| Function/handler | `create_mail_account` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `JSONResponse | Response` |
| Response model | `MailAccountResponse` |

# Request/response models

* [MailAccountCreateRequest](../../schemas/hyrule-cloud/MailAccountCreateRequest.md)
* [MailAccountResponse](../../schemas/hyrule-cloud/MailAccountResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/mail.py:107-113](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L107-L113)
