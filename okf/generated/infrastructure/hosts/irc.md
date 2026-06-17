---
type: Infrastructure Host
title: irc
description: Infrastructure Host `irc` with address `2a0c:b641:b50:2::80` and groups
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
  path: ansible/inventory/host_vars/irc.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/irc.yml
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: irc
address: 2a0c:b641:b50:2::80
groups:
- infra_vms
- linux
---

# Host

| Field | Value |
| --- | --- |
| Host | `irc` |
| Type | `Infrastructure Host` |
| Address | `2a0c:b641:b50:2::80` |
| Groups | `infra_vms, linux` |
| Role comment | `irc — Soju IRC bouncer.` |
| Monitoring role | `irc` |
| Logs role | `irc` |

# Deployed version pins

No app version pins found in host vars.

# Inbound firewall rules

* `tcp` port `6697` from `any` — Soju IRCS (public)
* `tcp` port `80` from `any` — ACME HTTP-01 (certbot standalone)
* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape

# Monitoring services

* `ircs-tcp` (tcp) — Soju TLS listener on tcp/6697
* `ircs-cert-validity` (ssl) — TLS certificate days-until-expiry on Soju

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::80` |

# Host variables summary

| Key | Value |
| --- | --- |
| `logs_register` | `True` |
| `logs_role` | `irc` |
| `monitoring_display_name` | `irc (Soju IRC bouncer)` |
| `monitoring_register` | `True` |
| `monitoring_role` | `irc` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/irc.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/irc.yml)
