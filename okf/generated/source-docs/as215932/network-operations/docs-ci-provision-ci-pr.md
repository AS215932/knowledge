---
type: Source Document
title: Provisioning the `ci-pr` VM (unprivileged PR runner)
description: '`ci-pr` is the **unprivileged** self-hosted GitHub Actions runner that
  handles untrusted PR code — PR-Agent, Semgrep, and (after Wave 4) every `pull_request`
  lint/test/build job. It is deliberately **disposable** and **isolated**:'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/provision-ci-pr.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/ci/provision-ci-pr.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-112
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/provision-ci-pr.md#L1-L112
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/ci/provision-ci-pr.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/ci/provision-ci-pr.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `112` |

# Detected headings

* `# Provisioning the `ci-pr` VM (unprivileged PR runner)`
* `## 0. Prereqs`
* `## 1. Create the VM on the customer (vm) bridge`
* `# On XOA (10.0.0.10, via the dom0 jump) or wherever xo-cli is configured:`
* `# Pick the xenbr-vm / "vm" network UUID:`
* `# create-vms.sh skips ci-pr unless VM_NET is set. It uses args 9,10 =`
* `# NETWORK + GATEWAY to place ci-pr on the vm bridge with the rtr enX3 gateway:`
* `#   create_vm ci-pr "..." 4 8589934592 21474836480 "2a0c:b641:b51::c1" "" "" "$VM_NET" "2a0c:b641:b51::1"`
* `## 2. Bootstrap firewall + monitoring (from the ops workstation)`
* `# Firewall: default-deny + node_exporter scrape from mon (host_vars/ci-pr.yml).`
* `# Monitoring: node_exporter + Icinga2 Host registration on mon.`
* `### 2a. Add `ci-pr` to Prometheus on mon (the one manual step)`
* `## 3. Register the runner in the `public-pr` group`
* `# Org runner registration token (1 h TTL):`
* `## 4. Verify isolation (acceptance probe)`
* `# Must FAIL/timeout (no infra/mgmt reachability):`
* `# Must SUCCEED (egress):`

# Deterministic excerpt

```markdown
# Provisioning the `ci-pr` VM (unprivileged PR runner)

`ci-pr` is the **unprivileged** self-hosted GitHub Actions runner that handles
untrusted PR code — PR-Agent, Semgrep, and (after Wave 4) every `pull_request`
lint/test/build job. It is deliberately **disposable** and **isolated**:

- On the **customer segment** `2a0c:b641:b51::c1/64` (rtr `enX3`/`xenbr-vm`), so
  rtr drops customer-sourced forwarded packets to the infra/router prefixes and
  drops `enX3` forwarding to the infra/mgmt bridges. The primary rule matches
  destination prefixes, not only `oifname`, so it remains effective under the
  overlay VRF. A compromised PR job here cannot reach production.
- **No** Vault AppRole, **no** `/etc/github-runner/secrets.env`, **no** `id_ci`
  deploy key, **no** Containerlab/xcaddy — see `host_vars/ci-pr.yml`.
- Registered in the **`public-pr`** org runner group (label `hyrule-public-pr`),
  separate from the privileged `ci` runner's `hyrule-ci` group.

Contrast with the privileged `ci` runner: see `docs/ci/provision.md`.

## 0. Prereqs

- `~/.ssh/id_servify` (ops workstation key — also authorizes `ci-pr` SSH).
- `gh` authenticated to the AS215932 org.
- Decide sizing: **4 vCPU, 8 GiB RAM, 20 GiB root** (Debian 13). No data disk. This remains a single GitHub Actions runner process (one job at a time); the larger VM reduces per-job runtime and avoids Docker/Semgrep/Ansible memory pressure without increasing PR job concurrency.

## 1. Create the VM on the customer (vm) bridge

The VM lands on `xenbr-vm`, not infra. Resolve that network's UUID on XOA, then
run the (now parameterized) `scripts/create-vms.sh` helper:

```bash
# On XOA (10.0.0.10, via the dom0 jump) or wherever xo-cli is configured:
xo-cli --list-objects type=network \
  | python3 -c 'import sys,json; [print(n
...
```

# Citations

[1] [docs/ci/provision-ci-pr.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/provision-ci-pr.md)
