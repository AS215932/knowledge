---
type: Architecture
title: NOC and MCP Diagnostics Loop
description: How alerts flow through NOC Agent and Hyrule MCP diagnostic tools.
tags:
- architecture
- curated
- proposed
truth_owner: okf
authority: advisory
source_refs:
- repo: AS215932/network-operations
  path: docs/autonomous-noc.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/autonomous-noc.md
- repo: AS215932/noc-agent
  path: README.md
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/README.md
- repo: AS215932/hyrule-mcp
  path: README.md
  commit: 326bcc85e1c69f0d7c1839ebaa4abb73acd84185
  url: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/README.md
last_verified_at: '2026-06-17T10:33:31Z'
confidence: medium
dispute_policy: adjudicate
review_status: proposed
---

# NOC/MCP diagnostics loop

`noc-agent` receives monitoring events, normalizes and investigates incidents, and uses `hyrule-mcp` for bounded live diagnostics. The loop is diagnostic-first and human-gated.

# Flow

1. Alertmanager or Icinga posts to `noc-agent`.
2. The graph deduplicates symptoms and recalls recent incident memory.
3. Specialist reasoning is checked against evidence and golden-state context.
4. Hyrule MCP provides read-biased tools for Prometheus, Icinga, FRR, firewall, DNS, WireGuard, host status, and packet-path checks.
5. A proposal is recorded for operator review through Discord or local `nocctl`.

# Boundary

The NOC loop responds to production symptoms. The engineering loop writes code/config PRs. Do not merge those responsibilities.

# Citations

[1] [AS215932/network-operations:docs/autonomous-noc.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/autonomous-noc.md)
[2] [AS215932/noc-agent:README.md](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/README.md)
[3] [AS215932/hyrule-mcp:README.md](https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/README.md)
