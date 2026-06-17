---
type: Source Document
title: ci — self-hosted GitHub Actions runner for AS215932/network-operations.
description: '--- # ci — self-hosted GitHub Actions runner for AS215932/network-operations.
  # # The runner picks up workflow jobs labeled `self-hosted, linux, x64, hyrule-infra`
  # (see .github/workflows/*.yml). It has overlay v6 reach to every infra h...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ci.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/ci.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-31
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ci.yml#L1-L31
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/host_vars/ci.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/host_vars/ci.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `31` |

# Detected headings

* `# ci — self-hosted GitHub Actions runner for AS215932/network-operations.`
* `#`
* `# The runner picks up workflow jobs labeled `self-hosted, linux, x64, hyrule-infra``
* `# (see .github/workflows/*.yml). It has overlay v6 reach to every infra host and`
* `# a Vault AppRole for secret retrieval during apply runs.`
* `#`
* `# First-time provisioning runbook: docs/ci/provision.md`
* `# node_exporter scrape from mon only.`
* `# Monitoring — register on mon (new host, not in legacy infra-vms.conf).`
* `# The runner-health check lives in configs/mon/icinga2/services/github-runner.conf`
* `# (Prometheus query on node_systemd_unit_state) — no by_ssh trust plumbing needed.`
* `# Logs — ship journald to log VM.`

# Citations

[1] [ansible/inventory/host_vars/ci.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ci.yml)
