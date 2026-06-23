---
type: Deployment
title: Hyrule NOC Agent on noc
description: Intended deployment pin `noc_agent_version` for Hyrule NOC Agent on `noc`.
resource: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/noc.yml
tags:
- deployment
- noc
- noc-agent
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
service_repo: AS215932/noc-agent
host: noc
pin_name: noc_agent_version
pin_value: be0924a2903568558f0ce81370d6e1a099fc1bee
---

# Deployment pin

| Field | Value |
| --- | --- |
| Service | [Hyrule NOC Agent](../services/noc-agent.md) |
| Host | [noc](../infrastructure/hosts/noc.md) |
| Pin variable | `noc_agent_version` |
| Pinned version | `be0924a2903568558f0ce81370d6e1a099fc1bee` |
| Source host vars | `ansible/inventory/host_vars/noc.yml` |

# Interpretation

This concept represents intended deployment state from `network-operations`: the named service is pinned to the recorded source revision/version on the target host. Runtime state still needs observed evidence from `okf/observed/` before claiming that the host is actually running this version.

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/noc.yml](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/noc.yml)
