---
type: Deployment
title: Hyrule Network Proxy on netproxy
description: Intended deployment pin `hyrule_network_proxy_version` for Hyrule Network
  Proxy on `netproxy`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/netproxy.yml
tags:
- deployment
- hyrule-network-proxy
- netproxy
- pin
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/hosts.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/netproxy.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/netproxy.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
service_repo: AS215932/hyrule-network-proxy
host: netproxy
pin_name: hyrule_network_proxy_version
pin_value: b82dc72bbf382167062bff272606ce84ec20538c
---

# Deployment pin

| Field | Value |
| --- | --- |
| Service | [Hyrule Network Proxy](../services/hyrule-network-proxy.md) |
| Host | [netproxy](../infrastructure/hosts/netproxy.md) |
| Pin variable | `hyrule_network_proxy_version` |
| Pinned version | `b82dc72bbf382167062bff272606ce84ec20538c` |
| Source host vars | `ansible/inventory/host_vars/netproxy.yml` |

# Interpretation

This concept represents intended deployment state from `network-operations`: the named service is pinned to the recorded source revision/version on the target host. Runtime state still needs observed evidence from `okf/observed/` before claiming that the host is actually running this version.

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/netproxy.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/netproxy.yml)
