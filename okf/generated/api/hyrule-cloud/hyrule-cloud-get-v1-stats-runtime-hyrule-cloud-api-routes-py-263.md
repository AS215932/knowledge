---
type: API Endpoint
title: GET /v1/stats/runtime
description: Static API endpoint `GET /v1/stats/runtime` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L263-L342
tags:
- api
- get
- hyrule-cloud
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/routes.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 263-342
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L263-L342
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/stats/runtime
source_path: hyrule_cloud/api/routes.py
function_name: get_runtime_stats
request_models: []
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/stats/runtime` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/routes.py:263` |
| Function/handler | `get_runtime_stats` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `dict` |
| Response model | `not statically declared` |

# Request/response models

No request or response model statically detected.

# Dependencies

* `get_orch`

# Function documentation

Per-process live runtime metrics.

Source is labelled `api-process-local-rolling-window` because the
deque is per-worker (uvicorn runs one event loop per worker; we don't
aggregate). Fleet-wide stats land in Block H via Prometheus on `mon`.

Fields always present (with sensible fallbacks when no samples exist
yet):
  - api_p50_ms: p50 of the last 1000 requests, milliseconds
  - api_p50_source: provenance label
  - sample_count: how many samples back the p50
  - live_vms: VMs currently READY
  - build_queue: VMs currently PROVISIONING
  - avg_provision_seconds: rolling avg of (provisioned_at - created_at)
    over the last 50 READY VMs (None if no provisioned_at data)
  - updated_at: ISO8601 UTC when computed

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/routes.py:263-342](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L263-L342)
