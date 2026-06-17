---
type: Runbook
title: VPS launch-proof smoke
description: 'End-to-end proof of the AS215932 VPS launch-proof wedge: a customer
  can quote a VM, be told payment is required, pay, watch it provision, and reach
  a working box — or get a safe failure with rollback available. This runbook is the
  human...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/runbooks/vps-launch-proof-smoke.md
tags:
- as215932
- network-operations
- runbook
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/runbooks/vps-launch-proof-smoke.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-56
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/runbooks/vps-launch-proof-smoke.md#L1-L56
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/runbooks/vps-launch-proof-smoke.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/runbooks/vps-launch-proof-smoke.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `56` |

# Detected headings

* `# VPS launch-proof smoke`
* `## Preconditions`
* `## Promotion (deploy #29's contract — do this first)`
* `## Smoke sequence`
* `## Acceptance`
* `## Failure handling`

# Deterministic excerpt

```markdown
# VPS launch-proof smoke

End-to-end proof of the AS215932 VPS launch-proof wedge: a customer can quote a
VM, be told payment is required, pay, watch it provision, and reach a working
box — or get a safe failure with rollback available. This runbook is the
human procedure; `scripts/smoke/vps-launch-proof.sh` automates the
no-payment-required checks and the status-contract assertions.

Identities (do not conflate): product = `hyrule.host`, infra = `servify.network`,
AS/routing = `as215932.net`.

## Preconditions

- The launch-proof contract (`AS215932/hyrule-cloud#29`) is **deployed** to the
  running cloud app — i.e. `hyrule_cloud_version` in `ansible/inventory/host_vars/`
  has been **promoted** to a SHA that includes #29 and applied (see Promotion below).
- A controlled **test order** and **test wallet / payment path** for the paid leg.
- Default is controlled simulation; real XCP-NG/Openprovider/DNS are opt-in on the
  cloud side via `HCP_LAUNCH_PROOF_REAL_XCPNG=1`.

## Promotion (deploy #29's contract — do this first)

Use the app-promotion path, never a manual pin edit:

1. `gh workflow run promote-apps.yml -F hyrule_cloud_sha=<#29 merge SHA> -F note="VPS launch-proof contract"`
2. Review + merge the promotion PR.
3. `app-promotion-deploy` calls `apply.yml playbook=cloud`; approve the `production` gate.
4. Record the **rollback SHA** = the `hyrule_cloud_version` *before* this promotion (for the rollback-by-SHA step).

## Smoke sequence

Run `scripts/smoke/vps-launch-proof.sh --base <cloud-api-base>` (it performs 1–2, 5–7
and prints the launch-proof fields); steps 3–4 and 8–9 are operator-driven.

1. **Quote** — `POST /v1/vm/quote` → `quote_id`, `payment_required`, accepted methods.
2. **Unpaid create returns 402** — `POST /v1/vm/create` without payment → **HTTP 402
...
```

# Citations

[1] [docs/runbooks/vps-launch-proof-smoke.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/runbooks/vps-launch-proof-smoke.md)
