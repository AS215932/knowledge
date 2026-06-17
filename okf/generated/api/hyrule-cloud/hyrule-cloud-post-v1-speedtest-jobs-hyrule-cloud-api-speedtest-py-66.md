---
type: API Endpoint
title: POST /v1/speedtest/jobs
description: Static API endpoint `POST /v1/speedtest/jobs` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/speedtest.py#L66-L70
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
  lines: 66-70
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/speedtest.py#L66-L70
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/speedtest/jobs
source_path: hyrule_cloud/api/speedtest.py
function_name: create_speedtest_job
request_models:
- SpeedtestRequest
response_model: DiagnosticJobResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/speedtest/jobs` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/speedtest.py:66` |
| Function/handler | `create_speedtest_job` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `DiagnosticJobResponse | Response` |
| Response model | `DiagnosticJobResponse` |

# Request/response models

* [SpeedtestRequest](/generated/schemas/hyrule-cloud/SpeedtestRequest.md)
* [DiagnosticJobResponse](/generated/schemas/hyrule-cloud/DiagnosticJobResponse.md)

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/speedtest.py:66-70](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/speedtest.py#L66-L70)
