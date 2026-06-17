---
type: Architecture
title: AS215932 System Map
description: Cross-repo map of AS215932 infrastructure, services, and automation loops.
tags:
- architecture
- curated
- proposed
truth_owner: okf
authority: advisory
source_refs:
- repo: AS215932/network-operations
  path: README.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md
- repo: AS215932/.github
  path: profile/README.md
  commit: e225c3fe957d598f2e53a52d301730e81ec221d8
  url: https://github.com/AS215932/.github/blob/e225c3fe957d598f2e53a52d301730e81ec221d8/profile/README.md
- repo: AS215932/network-operations
  path: docs/network-flows.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/network-flows.md
last_verified_at: '2026-06-17T10:33:31Z'
confidence: medium
dispute_policy: adjudicate
review_status: proposed
---

# System map

AS215932 combines an IPv6-first network operations repository, production VMs, Hyrule Cloud product services, NOC diagnostics, and an engineering automation loop.

# Core relationships

- `network-operations` is the production deployment record and intended-state source for infrastructure, app pins, DNS, monitoring, and firewall policy.
- `hyrule-cloud` provides the paid x402 VPS/API product surface.
- `hyrule-web` is the branded web/order/dashboard frontend.
- `hyrule-network-proxy` is an internal paid-request sidecar used by Hyrule Cloud.
- `noc-agent` consumes monitoring events and Hyrule MCP diagnostics for incident investigation.
- `hyrule-mcp` exposes bounded diagnostic tools for routing, host, monitoring, DNS, firewall, and packet-path inspection.
- `engineering-loop` creates draft PRs from approved work and hands production context back to operators.

# Review status

This curated page is a proposed cross-repo synthesis. Verify against cited source repos before treating it as durable policy.

# Citations

[1] [AS215932/network-operations:README.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md)
[2] [AS215932/.github:profile/README.md](https://github.com/AS215932/.github/blob/e225c3fe957d598f2e53a52d301730e81ec221d8/profile/README.md)
[3] [AS215932/network-operations:docs/network-flows.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/network-flows.md)
