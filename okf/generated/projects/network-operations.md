---
type: Project
title: Network Operations
description: Network operations and infrastructure tracking for AS215932 (Hyrule).
  Building a complete ISP from scratch - BGP/OSPFv3 routing, IXP peering, automation.
  Working in public.
resource: https://github.com/AS215932/network-operations
tags:
- ansible
- as215932
- autonomous-system
- bgp
- devops
- frrouting
- infrastructure
- infrastructure-as-code
- ipv6
- irr
- isp
- ixp
- jinja2
- looking-glass
- network-automation
- network-operations
- ospf
- ospf-v3
- peering
- project
- ripe
- rpki
- wireguard
- xcp-ng
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: README.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-207
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md#L1-L207
- repo: AS215932/network-operations
  path: AGENTS.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-53
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md#L1-L53
- repo: AS215932/network-operations
  path: CLAUDE.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-240
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CLAUDE.md#L1-L240
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
endpoint_count: 0
schema_count: 2
workflow_count: 10
---

# What this is

Network operations and infrastructure tracking for AS215932 (Hyrule). Building a complete ISP from scratch - BGP/OSPFv3 routing, IXP peering, automation. Working in public.

# Responsibilities

* Production deployment record and source of intended infrastructure state.
* Ansible inventory, host vars, firewall rules, monitoring config, DNS zones, and deployment workflows.
* Promotion PRs pin exact app SHAs before production applies.

# Runtime/deployment shape

* Owns production deployment record, Ansible inventory, workflow gates, and app version pins.
* Workflow `app-promotion-deploy` has deploy/promotion characteristics.
* Workflow `apply` has deploy/promotion characteristics.
* Workflow `drift-detection` has deploy/promotion characteristics.
* Workflow `netops-nightly` has deploy/promotion characteristics.
* Workflow `pr-agent` has deploy/promotion characteristics.
* Workflow `promote-apps` has deploy/promotion characteristics.

# Interfaces

* Workflow `app-promotion-deploy` from `.github/workflows/app-promotion-deploy.yml`
* Workflow `apply` from `.github/workflows/apply.yml`
* Workflow `drift-detection` from `.github/workflows/drift-detection.yml`
* Workflow `iac-tests` from `.github/workflows/iac-tests.yml`
* Workflow `lint` from `.github/workflows/lint.yml`
* Workflow `netops-nightly` from `.github/workflows/netops-nightly.yml`
* Workflow `pr-agent` from `.github/workflows/pr-agent.yml`
* Workflow `promote-apps` from `.github/workflows/promote-apps.yml`

# Dependencies

* `langgraph` from `pyproject.toml`

# Source-of-truth files

* `README.md`
* `AGENTS.md`
* `CLAUDE.md`
* `pyproject.toml`
* `docs/agent-loops/acceptance-gates.md`
* `docs/agent-loops/change-orchestrator.md`
* `docs/agent-loops/finops-billing-integrity-engineer.md`
* `docs/agent-loops/implementation-writer.md`
* `docs/agent-loops/repo-map.md`
* `docs/agent-loops/senior-devops-netops-engineer.md`
* `docs/agent-loops/senior-network-architect.md`
* `docs/agent-loops/senior-security-cryptographic-auditor.md`
* `docs/agent-loops/senior-systems-engineer.md`
* `docs/agent-loops/virtual-lab-chaos-simulation-engineer.md`
* `docs/ci/branch-protection.md`
* `docs/ci/deploy-runbook.md`

# Operational runbooks

* `docs/ci/deploy-runbook.md`

# Safety/security constraints

* Production applies require human approval through GitHub `production` environment gates.
* Every live deployment must compare Icinga snapshots before and after the change.
* Firewall changes must update `docs/network-flows.md`, host vars, and rendered artifacts together.

# Related services

* [noc-agent](../services/noc-agent.md)
* [hyrule-mcp](../services/hyrule-mcp.md)
* [engineering-loop](../services/engineering-loop.md)
* [hyrule-cloud](../services/hyrule-cloud.md)
* [hyrule-web](../services/hyrule-web.md)
* [hyrule-network-proxy](../services/hyrule-network-proxy.md)
* [as215932.net](../services/as215932-net.md)

# Open issues/known gaps

* #272: CI: skip the heavy IaC matrix on app-promotion (SHA-pin-only) PRs
* #268: hyrule-cloud monero-wallet-rpc: not syncing (no daemon) + restore script breaks on password rotation
* #267: rtr: root disk chronically tight (2.8G volume; Vector buffer + 3 kernels)
* #265: app-promotion-deploy: manual/auto apply concurrency collisions + wrong detect matrix
* #262: promote-apps: reused promotion branch + --force-with-lease breaks after each merge
* #256: monero-wallet-rpc bootstrap broken on api (invalid password + ringdb perms); restore PAYMENT_REQUIRE_NATIVE
* #254: Configure reliable Monero daemon for monero-wallet-rpc
* #253: Populate and validate HYRULE_NETWORK_PROXY_TOKEN for hyrule-cloud

# Canonicality

Repository-owned facts in this concept are derivative. If this concept disagrees with `AS215932/network-operations` at commit `67061d325834a7145252cdf851da1df6a4a38b9e` or a later source commit, the repository source wins and this concept is stale.

# Citations

[1] [AS215932/network-operations:README.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/README.md#L1-L207)
[2] [AS215932/network-operations:AGENTS.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md#L1-L53)
[3] [AS215932/network-operations:CLAUDE.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/CLAUDE.md#L1-L240)
