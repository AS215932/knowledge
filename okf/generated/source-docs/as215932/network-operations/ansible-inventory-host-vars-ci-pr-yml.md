---
type: Source Document
title: ci-pr — UNPRIVILEGED self-hosted GitHub Actions runner for untrusted PR code
description: '--- # ci-pr — UNPRIVILEGED self-hosted GitHub Actions runner for untrusted
  PR code # (PR-Agent, Semgrep, and — after Wave 4 — all pull_request lint/test/build
  jobs). # # Deliberately on the CUSTOMER-ISOLATED segment (2a0c:b641:b51::/48,...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ci-pr.yml
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/inventory/host_vars/ci-pr.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-68
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ci-pr.yml#L1-L68
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/inventory/host_vars/ci-pr.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/inventory/host_vars/ci-pr.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `68` |

# Detected headings

* `# ci-pr — UNPRIVILEGED self-hosted GitHub Actions runner for untrusted PR code`
* `# (PR-Agent, Semgrep, and — after Wave 4 — all pull_request lint/test/build jobs).`
* `#`
* `# Deliberately on the CUSTOMER-ISOLATED segment (2a0c:b641:b51::/48, rtr enX3):`
* `# rtr's forward chain drops enX3 -> { enX2 infra, enX0 mgmt }, so a compromised`
* `# PR job here cannot reach the management overlay. Treat ci-pr as DISPOSABLE.`
* `#`
* `# Hard isolation vs the privileged `ci` runner:`
* `#   - github_runner_vault_enabled: false  -> no Vault AppRole, no secrets.env`
* `#   - github_runner_ssh_key_path: ""      -> no id_ci fleet deploy key`
* `#   - containerlab/xcaddy disabled         -> no lab toolchain`
* `#   - no infra/mgmt reachability (customer isolation enforced on rtr)`
* `#`
* `# Monitoring works (mon -> ci-pr:9100 is infra->customer = permitted, pull-only).`
* `# Log shipping does NOT (ci-pr -> log:6000 is customer->infra = dropped by the`
* `# isolation), so logs_register stays false — local journald only. Turning it on`
* `# would require punching a ci-pr->log hole in the customer isolation; don't.`
* `#`
* `# Runbook: docs/ci/provision-ci-pr.md. Flows: docs/network-flows.md -> "### ci-pr".`
* `# --- github_runner role: UNPRIVILEGED profile ---`
* `# Routed-GUA container networking. Containers get GUAs from this /64 (a slice of`
* `# our customer /48); ci-pr forwards (net.ipv6.conf.all.forwarding=1, set by the`
* `# role) and rtr routes the /64 back via a static route`
* `# (2a0c:b641:b51:c1::/64 via 2a0c:b641:b51::c1, issue #132). Docker 26.x leaves`

# Citations

[1] [ansible/inventory/host_vars/ci-pr.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/inventory/host_vars/ci-pr.yml)
