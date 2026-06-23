---
type: Deployment
title: Hyrule MCP on noc
description: Intended deployment pin `hyrule_mcp_version` for Hyrule MCP on `noc`.
resource: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/noc.yml
tags:
- deployment
- hyrule-mcp
- noc
- pin
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
service_repo: AS215932/hyrule-mcp
host: noc
pin_name: hyrule_mcp_version
pin_value: 05b1245710e6a67ad40ccd62c033755f48ad4958
---

# Deployment pin

| Field | Value |
| --- | --- |
| Service | [Hyrule MCP](../services/hyrule-mcp.md) |
| Host | [noc](../infrastructure/hosts/noc.md) |
| Pin variable | `hyrule_mcp_version` |
| Pinned version | `05b1245710e6a67ad40ccd62c033755f48ad4958` |
| Source host vars | `ansible/inventory/host_vars/noc.yml` |

# Interpretation

This concept represents intended deployment state from `network-operations`: the named service is pinned to the recorded source revision/version on the target host. Runtime state still needs observed evidence from `okf/observed/` before claiming that the host is actually running this version.

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/noc.yml](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/noc.yml)
