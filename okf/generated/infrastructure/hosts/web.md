---
type: Infrastructure Host
title: web
description: Infrastructure Host `web` with address `2a0c:b641:b50:2::30` and groups
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
  path: ansible/inventory/host_vars/web.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/web.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
host: web
address: 2a0c:b641:b50:2::30
groups:
- infra_vms
- linux
---

# Host

| Field | Value |
| --- | --- |
| Host | `web` |
| Type | `Infrastructure Host` |
| Address | `2a0c:b641:b50:2::30` |
| Groups | `infra_vms, linux` |
| Role comment | `web — hyrule-web (uvicorn :8080 hyrule.host) + nginx (:8081 as215932.net).` |
| Monitoring role | `not set` |
| Logs role | `web` |

# Deployed version pins

* `hyrule_web_version` = `d94146e67f9eb05f8eeb5c57cab74cbe676f5c79`

# Inbound firewall rules

* `tcp` port `8080` from `['{{ peers.proxy.ipv6 }}', '{{ peers.mon.ipv6 }}']` — hyrule-web upstream from proxy/mon
* `tcp` port `8081` from `['{{ peers.proxy.ipv6 }}', '{{ peers.mon.ipv6 }}']` — as215932.net upstream from proxy/mon
* `tcp` port `9100` from `{{ peers.mon.ipv6 }}` — node_exporter scrape

# Monitoring services

No host-local `monitoring_extra_services` found in host vars.

# Peer registry values

| Key | Value |
| --- | --- |
| `ipv6` | `2a0c:b641:b50:2::30` |

# Host variables summary

| Key | Value |
| --- | --- |
| `hyrule_web_version` | `d94146e67f9eb05f8eeb5c57cab74cbe676f5c79` |
| `logs_register` | `True` |
| `logs_role` | `web` |

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/web.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/web.yml)
