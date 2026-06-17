---
type: Deployment
title: Hyrule Cloud on api
description: Intended deployment pin `hyrule_cloud_version` for Hyrule Cloud on `api`.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/api.yml
tags:
- api
- deployment
- hyrule-cloud
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
  path: ansible/inventory/host_vars/api.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/api.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
service_repo: AS215932/hyrule-cloud
host: api
pin_name: hyrule_cloud_version
pin_value: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Deployment pin

| Field | Value |
| --- | --- |
| Service | [Hyrule Cloud](../services/hyrule-cloud.md) |
| Host | [api](../infrastructure/hosts/api.md) |
| Pin variable | `hyrule_cloud_version` |
| Pinned version | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Source host vars | `ansible/inventory/host_vars/api.yml` |

# Interpretation

This concept represents intended deployment state from `network-operations`: the named service is pinned to the recorded source revision/version on the target host. Runtime state still needs observed evidence from `okf/observed/` before claiming that the host is actually running this version.

# Citations

[1] [Ansible inventory](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/hosts.yml)
[2] [ansible/inventory/host_vars/api.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/api.yml)
