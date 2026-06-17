---
type: Service
title: Hyrule MCP
description: MCP tools for administrating AS215932
resource: https://github.com/AS215932/hyrule-mcp
tags:
- automation
- bgp
- diagnostics
- frrouting
- hyrule
- mcp
- model-context-protocol
- monitoring
- networking
- service
timestamp: '2026-06-15T17:46:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-mcp
  path: README.md
  commit: 326bcc85e1c69f0d7c1839ebaa4abb73acd84185
  lines: 1-177
  url: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/README.md#L1-L177
- repo: AS215932/hyrule-mcp
  path: TESTING.md
  commit: 326bcc85e1c69f0d7c1839ebaa4abb73acd84185
  lines: 1-15
  url: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/TESTING.md#L1-L15
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-mcp
commit: 326bcc85e1c69f0d7c1839ebaa4abb73acd84185
endpoint_count: 0
schema_count: 5
workflow_count: 4
---

# What this is

MCP tools for administrating AS215932

# Responsibilities

* Bounded live diagnostic MCP substrate for routing, monitoring, firewall, host, DNS, and packet-path inspection.
* Read-biased tool server used by the NOC agent and operators.

# Runtime/deployment shape

* Deployed on host `noc` via `hyrule_mcp_version` pinned to `326bcc85e1c69f0d7c1839ebaa4abb73acd84185`.
* Workflow `pr-agent` has deploy/promotion characteristics.
* Workflow `request-promotion` has deploy/promotion characteristics.

# Interfaces

* Workflow `ci` from `.github/workflows/ci.yml`
* Workflow `pr-agent` from `.github/workflows/pr-agent.yml`
* Workflow `request-promotion` from `.github/workflows/request-promotion.yml`
* Workflow `semgrep` from `.github/workflows/semgrep.yml`

# Dependencies

* `fastapi` from `pyproject.toml`
* `httpx` from `pyproject.toml`
* `mcp` from `pyproject.toml`
* `structlog` from `pyproject.toml`
* `uvicorn` from `pyproject.toml`

# Source-of-truth files

* `README.md`
* `TESTING.md`
* `pyproject.toml`

# Operational runbooks

No repo-local runbook files detected in indexed sources.

# Safety/security constraints

* Raw SSH is bounded and mutative commands are rejected unless explicit action gates are enabled.
* Heavy diagnostics are capped server-side.

# Related services

* [noc-agent](/generated/services/noc-agent.md)
* [network-operations](/generated/projects/network-operations.md)

# Open issues/known gaps

* #15: CI: add a real test/lint gate (ruff + pytest) and make it required
* #10: hyrule-mcp: smaller helpers (prometheus_list_targets, dns_probe_burst, path_explain, ISO timestamps)
* #9: hyrule-mcp: add vault_agent_status (templates, last render, command directives)
* #8: hyrule-mcp: add service_restart_history (cadence detection for systemd units)
* #7: hyrule-mcp: add ecmp_path_select (probe N flows with varying L4 keys to surface ECMP-driven failures)
* #6: hyrule-mcp: add multi_source_probe (parallel reachability test from N internal hosts)
* #5: hyrule-mcp: add ndp_state and arp_state (cache contents with state + expiry)
* #4: hyrule-mcp: add firewall_state (rule stats + tables + counters)

# Canonicality

Repository-owned facts in this concept are derivative. If this concept disagrees with `AS215932/hyrule-mcp` at commit `326bcc85e1c69f0d7c1839ebaa4abb73acd84185` or a later source commit, the repository source wins and this concept is stale.

# Citations

[1] [AS215932/hyrule-mcp:README.md](https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/README.md#L1-L177)
[2] [AS215932/hyrule-mcp:TESTING.md](https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/TESTING.md#L1-L15)
