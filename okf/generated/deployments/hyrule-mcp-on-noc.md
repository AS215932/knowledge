---
type: Deployment
title: Hyrule MCP on noc
description: Intended deployment pin `hyrule_mcp_version` for Hyrule MCP on `noc`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/noc.yml
tags:
- deployment
- hyrule-mcp
- noc
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
service_repo: AS215932/hyrule-mcp
host: noc
pin_name: hyrule_mcp_version
pin_value: 326bcc85e1c69f0d7c1839ebaa4abb73acd84185
---

# Deployment pin

| Field | Value |
| --- | --- |
| Service | [Hyrule MCP](../services/hyrule-mcp.md) |
| Host | [noc](../infrastructure/hosts/noc.md) |
| Pin variable | `hyrule_mcp_version` |
| Pinned version | `326bcc85e1c69f0d7c1839ebaa4abb73acd84185` |
| Source host vars | `ansible/inventory/host_vars/noc.yml` |

# Interpretation

This concept represents intended deployment state from `network-operations`: the named service is pinned to the recorded source revision/version on the target host. Runtime state still needs observed evidence from `okf/observed/` before claiming that the host is actually running this version.

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/noc.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/noc.yml)
