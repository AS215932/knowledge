---
type: API Endpoint
title: POST /v1/speedtest/
description: Static API endpoint `POST /v1/speedtest/` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/speedtest.py#L59-L62
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/speedtest.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 59-62
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/speedtest.py#L59-L62
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/speedtest/
source_path: hyrule_cloud/api/speedtest.py
function_name: create_speedtest
request_models:
- SpeedtestRequest
response_model: DiagnosticResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/speedtest/` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/speedtest.py:59` |
| Function/handler | `create_speedtest` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `DiagnosticResponse | Response` |
| Response model | `DiagnosticResponse` |

# Request/response models

* [SpeedtestRequest](../../schemas/hyrule-cloud/SpeedtestRequest.md)
* [DiagnosticResponse](../../schemas/hyrule-cloud/DiagnosticResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/speedtest.py:59-62](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/speedtest.py#L59-L62)
