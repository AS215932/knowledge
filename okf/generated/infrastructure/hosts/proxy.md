---
type: Infrastructure Host
title: proxy
description: Infrastructure Host `proxy` with address `2a0c:b641:b50:2::40` and groups
  `infra_vms, linux, public_facing`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
tags:
- host
- infra_vms
- infrastructure
- linux
- public_facing
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
  path: ansible/inventory/host_vars/proxy.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/proxy.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: proxy
address: 2a0c:b641:b50:2::40
groups:
- infra_vms
- linux
- public_facing
---

# Host

| Field | Value |
| --- | --- |
| Host | `proxy` |
| Type | `Infrastructure Host` |
| Address | `2a0c:b641:b50:2::40` |
| Groups | `infra_vms, linux, public_facing` |
| Role comment | `proxy — Caddy TLS reverse proxy + ACME DNS-01 (RFC 2136 to dns).` |
| Monitoring role | `not set` |
| Logs role | `proxy` |

# Deployed version pins

No app version pins found in host vars.

# Inbound firewall rules

* `tcp` port `80` from `any` — HTTP (ACME + redirect)
* `tcp` port `443` from `any` — HTTPS (Caddy TLS)
* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape

# Monitoring services

No host-local `monitoring_extra_services` found in host vars.

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::40` |

# Host variables summary

| Key | Value |
| --- | --- |
| `logs_register` | `True` |
| `logs_role` | `proxy` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/proxy.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/proxy.yml)
