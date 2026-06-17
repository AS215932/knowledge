---
type: Deployment
title: Hyrule NOC Agent on noc
description: Intended deployment pin `noc_agent_version` for Hyrule NOC Agent on `noc`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/noc.yml
tags:
- deployment
- noc
- noc-agent
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
  path: ansible/inventory/host_vars/noc.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/noc.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
service_repo: AS215932/noc-agent
host: noc
pin_name: noc_agent_version
pin_value: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
---

# Deployment pin

| Field | Value |
| --- | --- |
| Service | [Hyrule NOC Agent](../services/noc-agent.md) |
| Host | [noc](../infrastructure/hosts/noc.md) |
| Pin variable | `noc_agent_version` |
| Pinned version | `98e5010648e34ac0ea6ad8e6a925fef76d0dbea9` |
| Source host vars | `ansible/inventory/host_vars/noc.yml` |

# Interpretation

This concept represents intended deployment state from `network-operations`: the named service is pinned to the recorded source revision/version on the target host. Runtime state still needs observed evidence from `okf/observed/` before claiming that the host is actually running this version.

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/noc.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/noc.yml)
