---
type: Deployment
title: AS215932 Knowledge MCP on loop
description: Intended deployment pin `knowledge_mcp_version` for AS215932 Knowledge MCP on `loop`.
resource: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/loop.yml
tags:
- deployment
- knowledge
- loop
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
  path: ansible/inventory/host_vars/loop.yml
  commit: fe46c3c3580ff79e8009ca839ab579f0691b55b8
  url: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/loop.yml
last_verified_at: '2026-06-23T10:06:29Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
service_repo: AS215932/knowledge
host: loop
pin_name: knowledge_mcp_version
pin_value: 5a6666cbb9d290868db3fb854ffed39099515b91
---

# Deployment pin

| Field | Value |
| --- | --- |
| Service | `AS215932 Knowledge MCP` |
| Host | [loop](../infrastructure/hosts/loop.md) |
| Pin variable | `knowledge_mcp_version` |
| Pinned version | `5a6666cbb9d290868db3fb854ffed39099515b91` |
| Source host vars | `ansible/inventory/host_vars/loop.yml` |

# Interpretation

This concept represents intended deployment state from `network-operations`: the AS215932/knowledge Knowledge MCP component is pinned to the recorded source revision/version on the target host. Runtime state still needs observed evidence from `okf/observed/` before claiming that the host is actually running this version.

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/loop.yml](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/loop.yml)
