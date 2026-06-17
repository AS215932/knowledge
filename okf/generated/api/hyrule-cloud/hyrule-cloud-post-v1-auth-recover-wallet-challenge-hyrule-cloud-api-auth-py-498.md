---
type: API Endpoint
title: POST /v1/auth/recover/wallet/challenge
description: Static API endpoint `POST /v1/auth/recover/wallet/challenge` in AS215932/hyrule-cloud.
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L498-L537
tags:
- api
- hyrule-cloud
- post
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: hyrule_cloud/api/auth.py
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 498-537
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L498-L537
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
method: POST
route: /v1/auth/recover/wallet/challenge
source_path: hyrule_cloud/api/auth.py
function_name: recover_wallet_challenge
request_models:
- WalletChallengeRequest
response_model: WalletChallengeResponse
---

# Endpoint

| Field | Value |
| --- | --- |
| Method | `POST` |
| Path | `/v1/auth/recover/wallet/challenge` |
| Repository | `AS215932/hyrule-cloud` |
| Source | `hyrule_cloud/api/auth.py:498` |
| Function/handler | `recover_wallet_challenge` |
| Router | `router` |
| Status codes | `503` |
| Return annotation | `WalletChallengeResponse` |
| Response model | `WalletChallengeResponse` |

# Request/response models

* [WalletChallengeRequest](../../schemas/hyrule-cloud/WalletChallengeRequest.md)
* [WalletChallengeResponse](../../schemas/hyrule-cloud/WalletChallengeResponse.md)

# Dependencies

* `get_app_state`

# Function documentation

Issue a single-use, time-bound challenge for wallet-signature recovery.

We always insert + return a challenge — even for unknown account_ids —
so an attacker cannot enumerate which accounts exist. Verification will
fail at the signer-match step if no VM on this account was ever paid for
by the signing wallet.

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [hyrule_cloud/api/auth.py:498-537](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/hyrule_cloud/api/auth.py#L498-L537)
