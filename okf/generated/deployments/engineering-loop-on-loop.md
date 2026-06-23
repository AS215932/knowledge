---
type: Deployment
title: Hyrule Engineering Loop on loop
description: Intended deployment pin `engineering_loop_version` for Hyrule Engineering
  Loop on `loop`.
resource: https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/loop.yml
tags:
- deployment
- engineering-loop
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
service_repo: AS215932/engineering-loop
host: loop
pin_name: engineering_loop_version
pin_value: eb37b1c4d1d7c3f349c8c6cdb3bd890f168c2755
---

# Deployment pin

| Field | Value |
| --- | --- |
| Service | [Hyrule Engineering Loop](../services/engineering-loop.md) |
| Host | [loop](../infrastructure/hosts/loop.md) |
| Pin variable | `engineering_loop_version` |
| Pinned version | `eb37b1c4d1d7c3f349c8c6cdb3bd890f168c2755` |
| Source host vars | `ansible/inventory/host_vars/loop.yml` |

# Interpretation

This concept represents intended deployment state from `network-operations`: the named service is pinned to the recorded source revision/version on the target host. Runtime state still needs observed evidence from `okf/observed/` before claiming that the host is actually running this version.

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/loop.yml](https://github.com/AS215932/network-operations/blob/fe46c3c3580ff79e8009ca839ab579f0691b55b8/ansible/inventory/host_vars/loop.yml)
