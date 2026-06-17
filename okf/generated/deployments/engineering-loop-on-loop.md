---
type: Deployment
title: Hyrule Engineering Loop on loop
description: Intended deployment pin `engineering_loop_version` for Hyrule Engineering
  Loop on `loop`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/loop.yml
tags:
- deployment
- engineering-loop
- loop
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
  path: ansible/inventory/host_vars/loop.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/loop.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
service_repo: AS215932/engineering-loop
host: loop
pin_name: engineering_loop_version
pin_value: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Deployment pin

| Field | Value |
| --- | --- |
| Service | [Hyrule Engineering Loop](../services/engineering-loop.md) |
| Host | [loop](../infrastructure/hosts/loop.md) |
| Pin variable | `engineering_loop_version` |
| Pinned version | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
| Source host vars | `ansible/inventory/host_vars/loop.yml` |

# Interpretation

This concept represents intended deployment state from `network-operations`: the named service is pinned to the recorded source revision/version on the target host. Runtime state still needs observed evidence from `okf/observed/` before claiming that the host is actually running this version.

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/loop.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/loop.yml)
