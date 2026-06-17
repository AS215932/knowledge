---
type: API Endpoint
title: GET /v1/mail/accounts/{mailbox_id}/aliases
description: Static API endpoint `GET /v1/mail/accounts/{mailbox_id}/aliases` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L177-L178
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
  lines: 177-178
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L177-L178
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/mail/accounts/{mailbox_id}/aliases
source_path: hyrule_cloud/api/mail.py
function_name: list_mail_aliases
request_models: []
response_model: list[MailAliasResponse]
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/mail/accounts/{mailbox_id}/aliases` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/mail.py:177` |
| Function/handler | `list_mail_aliases` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `JSONResponse` |
| Response model | `list[MailAliasResponse]` |

# Request/response models

* `list[MailAliasResponse]`

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/mail.py:177-178](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/mail.py#L177-L178)
