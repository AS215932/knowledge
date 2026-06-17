---
type: Infrastructure Host
title: noc
description: Infrastructure Host `noc` with address `2a0c:b641:b50:2::a0` and groups
  `infra_vms, linux`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
tags:
- host
- infra_vms
- infrastructure
- linux
- vm
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/noc.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/noc.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: noc
address: 2a0c:b641:b50:2::a0
groups:
- infra_vms
- linux
---

# Host

| Field | Value |
| --- | --- |
| Host | `noc` |
| Type | `Infrastructure Host` |
| Address | `2a0c:b641:b50:2::a0` |
| Groups | `infra_vms, linux` |
| Role comment | `noc — autonomous NOC agent + hyrule-mcp tool server.` |
| Monitoring role | `noc` |
| Logs role | `noc` |

# Deployed version pins

* `noc_agent_version` = `98e5010648e34ac0ea6ad8e6a925fef76d0dbea9`
* `hyrule_mcp_version` = `326bcc85e1c69f0d7c1839ebaa4abb73acd84185`

# Inbound firewall rules

* `tcp` port `8000` from `{{ peers.mon.ipv6 }}` — noc-agent webhook from mon (Alertmanager + Icinga)
* `tcp` port `8000` from `{{ peers.proxy.ipv6 }}` — noc-agent control dashboard via Caddy (proxy)
* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape

# Monitoring services

* `noc-agent-health` (http) — FastAPI liveness for noc-agent
* `noc-agent-mcp-health` (noc_agent_mcp_health) — MCP subprocess connectivity for Prometheus/SSH and Xen Orchestra tools
* `noc-agent-config-health` (http) — Required noc-agent runtime configuration and secret presence
* `noc-agent-mail-health` (noc_agent_mail_health) — NOC mailbox IMAP login/select used by mail polling
* `noc-agent-model-health` (noc_agent_model_health) — Configured AI model and fallback access for noc-agent

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::a0` |

# Host variables summary

| Key | Value |
| --- | --- |
| `hyrule_mcp_version` | `326bcc85e1c69f0d7c1839ebaa4abb73acd84185` |
| `logs_register` | `True` |
| `logs_role` | `noc` |
| `monitoring_register` | `True` |
| `monitoring_role` | `noc` |
| `noc_agent_mcp_health_timeout_seconds` | `12` |
| `noc_agent_version` | `98e5010648e34ac0ea6ad8e6a925fef76d0dbea9` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/noc.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/noc.yml)
