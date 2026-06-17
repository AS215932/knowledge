---
type: Source Document
title: Hyrule Repo Map
description: '- Purpose: AS215932 infrastructure, Ansible, network configuration,
  CI/deploy workflows, and operating docs. - Common classes: `infra_ansible`, `routing_bgp_frr`,
  `firewall_policy`, `dns`, `vault_secret_plane`, `monitoring_logging`, `mix...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/repo-map.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/agent-loops/repo-map.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-53
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/repo-map.md#L1-L53
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/agent-loops/repo-map.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/agent-loops/repo-map.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `53` |

# Detected headings

* `# Hyrule Repo Map`
* `## hyrule-infra`
* `## hyrule-cloud`
* `## hyrule-web`
* `## hyrule-mcp`
* `## hyrule-noc-agent`
* `## hyrule-business`

# Deterministic excerpt

```markdown
# Hyrule Repo Map

## hyrule-infra

- Purpose: AS215932 infrastructure, Ansible, network configuration, CI/deploy
  workflows, and operating docs.
- Common classes: `infra_ansible`, `routing_bgp_frr`, `firewall_policy`, `dns`,
  `vault_secret_plane`, `monitoring_logging`, `mixed`.
- Source of truth: `AGENTS.md`, `docs/network-flows.md`, `docs/architecture.md`,
  Ansible inventory, CI workflow docs.
- Gates: `git diff --check` for docs; Ansible validate and existing CI workflows
  for config/infra changes.

## hyrule-cloud

- Purpose: Hyrule Cloud API, VPS provisioning, x402/payment flows, quota and
  metering behavior.
- Common classes: `cloud_api`, `app_feature`, `app_bugfix`, `mixed`.
- Required roles: Systems, DevOps/NetOps, FinOps for billing/provisioning
  paths, Security for tenant isolation or secret handling.
- Gates: pytest, ruff, mypy.

## hyrule-web

- Purpose: customer-facing web frontend for Hyrule Cloud.
- Common classes: `frontend`, `app_feature`, `app_bugfix`.
- Required roles: Systems and DevOps/NetOps; FinOps when pricing/payment UI
  affects state semantics.
- Gates: pytest and `npm run check`.

## hyrule-mcp

- Purpose: diagnostic MCP server exposing AS215932 infrastructure tools.
- Common classes: `mcp_diagnostic_tooling`, `monitoring_logging`, `mixed`.
- Required roles: Systems and DevOps/NetOps; Security when output may expose
  secrets, tenant data, or p
...
```

# Citations

[1] [docs/agent-loops/repo-map.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/repo-map.md)
