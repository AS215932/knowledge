---
type: Source Document
title: x402 official SDK (x402-foundation)
description: '[project] name = "hyrule-cloud" version = "0.1.0" description = "Agentic
  VPS hosting with x402 payments on AS215932" requires-python = ">=3.12" dependencies
  = [ "fastapi>=0.115", "uvicorn[standard]>=0.34", "pydantic>=2.10", "pydantic-set...'
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/pyproject.toml
tags:
- as215932
- hyrule-cloud
- source-document
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: pyproject.toml
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-115
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/pyproject.toml#L1-L115
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: pyproject.toml
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `pyproject.toml` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `115` |

# Detected headings

* `# x402 official SDK (x402-foundation)`
* `# DNS (RFC 2136 dynamic updates)`
* `# XO WebSocket JSON-RPC`
* `# Database`
* `# MCP server`
* `# Block A1 (Wave 2): argon2id for passwords + recovery codes`
* `# Block A1 (Wave 2): TTL cache for per-IP rate-limit buckets`
* `# Block E (Wave 4): pure-Python BIP32/BIP84 HD derivation for BTC receive`
* `# addresses from a watch-only xpub (no keys held). coincurve is bip-utils'`
* `# secp256k1 backend; pinned for the Debian 13 / Python 3.13 runner.`
* `# Block F (Wave 5): EIP-191 signature recovery for wallet-signature account`
* `# recovery (recover the signer address from a personal_sign signature).`
* `# Block H (Wave 5): mock httpx for the Prometheus /v1/stats/network tests.`
* `# E402 / E501 globally ignored: both are pre-A0 baseline noise (toy`
* `# AccountRow patches at the bottom of db.py force mid-file imports;`
* `# several SQLAlchemy Enum / route signatures sit at 100-200 chars).`
* `# The post-A0 cleanup PR will refactor db.py and reflow long lines;`
* `# until then, gating new touched files on these style rules would`
* `# block Wave 1 for cosmetic reasons that don't catch real bugs.`
* `# RUF012: mutable class defaults in test mock classes. Each test defines`
* `# fresh nested mock classes (MockOrchestrator, _OrchOK, etc.) and the`
* `# mutable-default pitfall (state bleeding across instances) doesn't`
* `# apply — they're per-test scaffolding. Suppressed only under tests/.`
* `# F811: cross-file pytest fixtures (e.g. tests/test_api_keys.py imports`

# Citations

[1] [pyproject.toml](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/pyproject.toml)
