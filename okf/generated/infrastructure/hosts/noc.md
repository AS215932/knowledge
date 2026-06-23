---
type: Infrastructure Host
title: noc
description: Infrastructure Host `noc` with address `2a0c:b641:b50:2::a0` and groups
  `infra_vms, linux`.
resource: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml
tags:
- host
- infra_vms
- infrastructure
- linux
- vm
timestamp: '2026-06-23T09:21:09Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/noc.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/noc.yml
last_verified_at: '2026-06-23T10:06:29Z'
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

* `noc_agent_version` = `be0924a2903568558f0ce81370d6e1a099fc1bee`
* `hyrule_mcp_version` = `05b1245710e6a67ad40ccd62c033755f48ad4958`
* `noc_knowledge_version` = `5a6666cbb9d290868db3fb854ffed39099515b91`

# Inbound firewall rules

* `tcp` port `8000` from `{{ peers.mon.ipv6 }}` — noc-agent webhook from mon (Alertmanager + Icinga)
* `tcp` port `8000` from `{{ peers.proxy.ipv6 }}` — noc-agent control dashboard via Caddy (proxy)
* `tcp` port `8000` from `{{ peers.loop.ipv6 }}` — LHP-v1 Engineering Loop fetch/callback to noc-agent
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
| `hyrule_mcp_version` | `05b1245710e6a67ad40ccd62c033755f48ad4958` |
| `logs_register` | `True` |
| `logs_role` | `noc` |
| `monitoring_register` | `True` |
| `monitoring_role` | `noc` |
| `noc_agent_mcp_health_timeout_seconds` | `12` |
| `noc_agent_version` | `be0924a2903568558f0ce81370d6e1a099fc1bee` |
| `noc_case_auto_resolve_enabled` | `False` |
| `noc_case_verification_dry_run` | `False` |
| `noc_case_verification_enabled` | `True` |
| `noc_disk_alert_handoff_enabled` | `True` |
| `noc_engineering_handoff_delivery_enabled` | `True` |
| `noc_knowledge_context_enabled` | `True` |
| `noc_knowledge_version` | `5a6666cbb9d290868db3fb854ffed39099515b91` |
| `noc_lhp_disk_alert_fingerprint` | `8fb421ff94bb1285` |
| `noc_lhp_enabled` | `True` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/noc.yml](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/noc.yml)
