---
type: API Endpoint
title: POST /v1/web/reports
description: Static API endpoint `POST /v1/web/reports` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/web.py#L127-L131
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/web.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 127-131
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/web.py#L127-L131
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/web/reports
source_path: hyrule_cloud/api/web.py
function_name: create_web_report
request_models:
- WebReportRequest
response_model: DiagnosticJobResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/web/reports` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/web.py:127` |
| Function/handler | `create_web_report` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `DiagnosticJobResponse | Response` |
| Response model | `DiagnosticJobResponse` |

# Request/response models

* `WebReportRequest`
* [DiagnosticJobResponse](/generated/schemas/hyrule-cloud/DiagnosticJobResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/web.py:127-131](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/web.py#L127-L131)
