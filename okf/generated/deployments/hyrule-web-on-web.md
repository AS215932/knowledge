---
type: Deployment
title: Hyrule Web on web
description: Intended deployment pin `hyrule_web_version` for Hyrule Web on `web`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/web.yml
tags:
- deployment
- hyrule-web
- pin
- web
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
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
service_repo: AS215932/hyrule-web
host: web
pin_name: hyrule_web_version
pin_value: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
---

# Deployment pin

| Field | Value |
| --- | --- |
| Service | [Hyrule Web](/generated/services/hyrule-web.md) |
| Host | [web](/generated/infrastructure/hosts/web.md) |
| Pin variable | `hyrule_web_version` |
| Pinned version | `d94146e67f9eb05f8eeb5c57cab74cbe676f5c79` |
| Source host vars | `ansible/inventory/host_vars/web.yml` |

# Interpretation

This concept represents intended deployment state from `network-operations`: the named service is pinned to the recorded source revision/version on the target host. Runtime state still needs observed evidence from `okf/observed/` before claiming that the host is actually running this version.

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/web.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/web.yml)
