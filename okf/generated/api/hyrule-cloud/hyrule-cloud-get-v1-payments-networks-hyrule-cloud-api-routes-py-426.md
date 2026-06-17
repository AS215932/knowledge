---
type: API Endpoint
title: GET /v1/payments/networks
description: Static API endpoint `GET /v1/payments/networks` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L426-L466
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
  lines: 426-466
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L426-L466
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: GET
route: /v1/payments/networks
source_path: hyrule_cloud/api/routes.py
function_name: get_payment_networks
request_models: []
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `GET` |
| Path | `/v1/payments/networks` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/routes.py:426` |
| Function/handler | `get_payment_networks` |
| Router | `router` |
| Status codes | `Not statically detected` |
| Return annotation | `dict` |
| Response model | `not statically declared` |

# Request/response models

No request or response model statically detected.

# Dependencies

* `get_app_state`
* `get_cfg`

# Function documentation

Block C (Wave 3): the canonical list of supported payment chains.

The frontend chain selector and any agent SDK that wants to know what
chains we accept reads from here — NEVER hardcodes the list client-side
(per feedback_verified_payment_chains.md). Operators can flip a chain
off via Vault (PAYMENT_PAYMENT_NETWORKS__N__enabled=false) and the
frontend picks it up on the next poll without a redeploy.

Shape: `{ networks: [...], native: [...], receiver_address, facilitator_url }`. Each
network dict carries the CAIP-2 identifier (canonical for x402 v2), the
EIP-712 domain shape (so the wallet adapter doesn't have to bake one
in), and the explorer URL for the post-pay receipt link.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/routes.py:426-466](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/routes.py#L426-L466)
