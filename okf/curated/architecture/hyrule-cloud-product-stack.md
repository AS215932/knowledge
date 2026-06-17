---
type: Architecture
title: Hyrule Cloud Product Stack
description: Product architecture for Hyrule Cloud, Hyrule Web, and the network proxy
  sidecar.
tags:
- architecture
- curated
- proposed
truth_owner: okf
authority: advisory
source_refs:
- repo: AS215932/hyrule-cloud
  path: README.md
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/README.md
- repo: AS215932/hyrule-web
  path: pyproject.toml
  commit: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
  url: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/pyproject.toml
- repo: AS215932/hyrule-network-proxy
  path: README.md
  commit: b82dc72bbf382167062bff272606ce84ec20538c
  url: https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/README.md
- repo: AS215932/network-operations
  path: docs/x402-network-proxy-sidecar-plan.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/x402-network-proxy-sidecar-plan.md
last_verified_at: '2026-06-17T10:33:31Z'
confidence: medium
dispute_policy: adjudicate
review_status: proposed
---

# Hyrule Cloud product stack

Hyrule Cloud is an agentic VPS hosting/API product using x402 payments. Hyrule Web provides the web/order/dashboard frontend. Hyrule Network Proxy executes internal already-authorized paid network requests.

# Product responsibilities

- Hyrule Cloud: payment verification, VM lifecycle, DNS, domain registration, pricing, database state, and public API contract.
- Hyrule Web: customer-facing site, order flow, dashboard, and committed frontend bundle.
- Hyrule Network Proxy: internal egress execution for direct/Tor/I2P/Yggdrasil modes, never public and never payment-aware.

# Deployment ownership

Production versions are pinned in `network-operations` host vars and promoted through the deployment flow.

# Citations

[1] [AS215932/hyrule-cloud:README.md](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/README.md)
[2] [AS215932/hyrule-web:pyproject.toml](https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/pyproject.toml)
[3] [AS215932/hyrule-network-proxy:README.md](https://github.com/AS215932/hyrule-network-proxy/blob/b82dc72bbf382167062bff272606ce84ec20538c/README.md)
[4] [AS215932/network-operations:docs/x402-network-proxy-sidecar-plan.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/x402-network-proxy-sidecar-plan.md)
