---
type: Source Document
title: frr role
description: Deploys the committed FRRouting config (`configs/<host>/frr.conf`) to
  a router and hot-reloads it. The repo's `configs/<host>/frr.conf` stays the single
  source of truth — this role does **not** template/render it; it pushes the file
  verb...
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/roles/frr/README.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: ansible/roles/frr/README.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-65
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/roles/frr/README.md#L1-L65
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: ansible/roles/frr/README.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `ansible/roles/frr/README.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `65` |

# Detected headings

* `# frr role`
* `## What it does (on `--tags apply` + `frr_apply=true`)`
* `## OS differences (`vars/<os_family>.yml`)`
* `## Key variables (`defaults/main.yml`)`
* `## Usage`
* `# Validate-only (no host connection, no change):`
* `# Apply to one router (Icinga-bracketed, serial:1):`

# Deterministic excerpt

```markdown
# frr role

Deploys the committed FRRouting config (`configs/<host>/frr.conf`) to a router
and hot-reloads it. The repo's `configs/<host>/frr.conf` stays the single source
of truth — this role does **not** template/render it; it pushes the file verbatim
and applies a delta-reload so iBGP/OSPF sessions are not flapped.

## What it does (on `--tags apply` + `frr_apply=true`)

1. Asserts `configs/<host>/frr.conf` exists (the validate/dry-run stops here).
2. Stages it to `<conf>.new` on the host.
3. Syntax-checks the staged file (`vtysh -C -f`).
4. Backs up the currently-loaded config.
5. Schedules an `at(1)` watchdog (default 5 min) that restores + reloads the
   backup if the play does not cancel it — covers a lockout from a bad policy.
6. Moves the new config into place, **reloads** (FRR integrated delta-reload —
   no restart), then **`clear bgp ipv6 unicast * soft`** to re-apply policy.
7. Cancels the watchdog once the reload completes cleanly.

The reload runs on **every** apply (not gated on the file changing): `frr-reload`
diffs against the *running daemon*, so a converged daemon is a cheap no-op, while
a daemon left stale by a prior run still gets converged. This avoids the trap
where the on-disk file already matches the repo but the daemon never ingested it.

`serial: 1` and the pre/post Icinga snapshot bracket are on the playbook
(`playbooks/frr.yml`), matching the `fire
...
```

# Citations

[1] [ansible/roles/frr/README.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/ansible/roles/frr/README.md)
