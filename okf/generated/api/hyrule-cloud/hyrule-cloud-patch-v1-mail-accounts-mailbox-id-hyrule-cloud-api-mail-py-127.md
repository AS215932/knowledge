---
type: API Endpoint
title: PATCH /v1/mail/accounts/{mailbox_id}
description: Static API endpoint `PATCH /v1/mail/accounts/{mailbox_id}` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L127-L128
tags:
- api
- hyrule-cloud
- patch
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/mail.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 127-128
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L127-L128
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: PATCH
route: /v1/mail/accounts/{mailbox_id}
source_path: hyrule_cloud/api/mail.py
function_name: update_mail_account
request_models:
- MailAccountUpdateRequest
response_model: MailAccountResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `PATCH` |
| Path | `/v1/mail/accounts/{mailbox_id}` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/mail.py:127` |
| Function/handler | `update_mail_account` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `JSONResponse` |
| Response model | `MailAccountResponse` |

# Request/response models

* [MailAccountUpdateRequest](/generated/schemas/hyrule-cloud/MailAccountUpdateRequest.md)
* [MailAccountResponse](/generated/schemas/hyrule-cloud/MailAccountResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/mail.py:127-128](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L127-L128)
