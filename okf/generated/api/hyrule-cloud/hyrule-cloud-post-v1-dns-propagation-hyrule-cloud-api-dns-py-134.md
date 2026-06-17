---
type: API Endpoint
title: POST /v1/dns/propagation
description: Static API endpoint `POST /v1/dns/propagation` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/dns.py#L134-L137
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/dns.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 134-137
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/dns.py#L134-L137
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/dns/propagation
source_path: hyrule_cloud/api/dns.py
function_name: dns_propagation
request_models:
- DNSPropagationRequest
response_model: DNSDiagnosticResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/dns/propagation` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/dns.py:134` |
| Function/handler | `dns_propagation` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `DNSDiagnosticResponse | Response` |
| Response model | `DNSDiagnosticResponse` |

# Request/response models

* [DNSPropagationRequest](../../schemas/hyrule-cloud/DNSPropagationRequest.md)
* `DNSDiagnosticResponse`

# Dependencies

No FastAPI dependencies statically detected.

# Function documentation

No function docstring found in source.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/dns.py:134-137](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/dns.py#L134-L137)
