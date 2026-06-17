---
type: Source Document
title: Provisioning the `ci` VM
description: The `ci` VM hosts the self-hosted GitHub Actions runner that powers every
  workflow in `.github/workflows/`. It must exist before the workflows can do any
  work — until then the workflow jobs sit queued.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/provision.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/ci/provision.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-150
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/provision.md#L1-L150
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/ci/provision.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/ci/provision.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `150` |

# Detected headings

* `# Provisioning the `ci` VM`
* `## 1. Provision the VM via Xen Orchestra`
* `## 2. Bootstrap firewall + monitoring + logs`
* `# Firewall first (default-deny + extra rules from host_vars/ci.yml).`
* `# Monitoring (node_exporter + Icinga2 host registration).`
* `# Logs (Vector agent → log VM).`
* `## 3. Mint a runner registration token`
* `## 4. Apply the github_runner role`
* `## 5. Verify`
* `## Tear down / re-register`
* `# Drop the old registration on GitHub`
* `# Mint a new token, re-apply`

# Deterministic excerpt

```markdown
# Provisioning the `ci` VM

The `ci` VM hosts the self-hosted GitHub Actions runner that powers every
workflow in `.github/workflows/`. It must exist before the workflows can
do any work — until then the workflow jobs sit queued.

Reasonable size: **4 vCPU, 8 GiB RAM, 20 GiB root disk + 50 GiB runner data disk** (Debian 13). The runner still serializes one GitHub Actions job at a time, but the extra headroom keeps Docker, Ansible, and trusted lab bursts from stretching the PR/apply queue.

## 1. Provision the VM via Xen Orchestra

The repo's established pattern is `xo-cli` run **on XOA** (`10.0.0.10`, reached
via overlay v6 `2a0c:b641:b50:2::70` or the dom0 jump `193.70.32.138`) — see
`scripts/create-vms.sh` for the `vm.create` + `vdi.set` + `vm.setBootOrder` +
`vm.start` sequence. The `ci` VM follows it with these parameters:

- Template: **Debian 13 cloud-init**. Name: `ci`. 4 vCPU, 8 GiB RAM,
  20 GiB root disk on `local_storage` plus a second 50 GiB data disk attached
  at VBD position `8` so the guest sees it as `/dev/xvdi`.
- VIF on `xenbr-infra` (overlay). Static IPv6 `2a0c:b641:b50:2::d0`
  (matches `peers.ci.ipv6` in `group_vars/all.yml` and
  `ci.as215932.net`).
- Cloud-init user-data from `autoinstall/debian-cloud-init.yaml.j2`;
  hostname `ci.as215932.net`; `id_servify.pub` authorized for root.

The XOA web UI (New → VM → Debian 13 cloud-init) is an equivalent manual
path if you prefer.

Start the VM, wait for cloud-init to finish, and verify `ssh svag@ci` works
over overlay v6.

If you are retrofitting the existing `ci` host rather than building a fresh VM,
attach the new 50 GiB VDI in Xen Orchestra first and place it at VBD position
`8` so the guest sees `/dev/xvdi` before you re-apply the role.

## 2. Bootstrap firewall + monitoring + logs

The same way e
...
```

# Citations

[1] [docs/ci/provision.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/ci/provision.md)
