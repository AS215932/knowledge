---
type: Deployment
title: AS215932 NOC Knowledge Bundle on noc
description: Intended deployment pin `noc_knowledge_version` for AS215932 NOC Knowledge Bundle on `noc`.
resource: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/noc.yml
tags:
- deployment
- knowledge
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
service_repo: AS215932/knowledge
host: noc
pin_name: noc_knowledge_version
pin_value: 5a6666cbb9d290868db3fb854ffed39099515b91
---

# Deployment pin

| Field | Value |
| --- | --- |
| Service | `AS215932 NOC Knowledge Bundle` |
| Host | [noc](../infrastructure/hosts/noc.md) |
| Pin variable | `noc_knowledge_version` |
| Pinned version | `5a6666cbb9d290868db3fb854ffed39099515b91` |
| Source host vars | `ansible/inventory/host_vars/noc.yml` |

# Interpretation

This concept represents intended deployment state from `network-operations`: the AS215932/knowledge NOC Knowledge Bundle component is pinned to the recorded source revision/version on the target host. Runtime state still needs observed evidence from `okf/observed/` before claiming that the host is actually running this version.

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/noc.yml](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/noc.yml)
