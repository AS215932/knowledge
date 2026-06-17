---
type: Source Document
title: NetOps testing strategy
description: 'How AS215932 IaC changes are validated, from a cheap stdlib check on
  every PR up to full control-plane modelling and a live dynamic lab. The tiers map
  onto the two-runner security model (`docs/ci/security-model.md`): untrusted PR code
  ru...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/netops/testing-strategy.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/netops/testing-strategy.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-96
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/netops/testing-strategy.md#L1-L96
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/netops/testing-strategy.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/netops/testing-strategy.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `96` |

# Detected headings

* `# NetOps testing strategy`
* `## Tiers`
* `### Tier 0 — static (required)`
* `### Tiers 1–2 — Batfish & Containerlab (trusted-only)`
* `## The `iac-gate` and branch protection`
* `## Adding a check`

# Deterministic excerpt

```markdown
# NetOps testing strategy

How AS215932 IaC changes are validated, from a cheap stdlib check on every PR
up to full control-plane modelling and a live dynamic lab. The tiers map onto
the two-runner security model (`docs/ci/security-model.md`): untrusted PR code
runs only on the unprivileged `hyrule-public-pr` runner; the heavy labs run on
the privileged `ci` runner on trusted triggers only.

## Tiers

| Tier | Jobs | Runner | Trigger | Gating |
|------|------|--------|---------|--------|
| 0 — static | `static-iac`, `ansible-idempotency` | `hyrule-public-pr` (unprivileged) | PRs with IaC path changes | **required** via `iac-gate` |
| 1 — Batfish | `batfish` | `ci` (privileged) | `workflow_dispatch`, repo var `ENABLE_BATFISH_TESTS`, nightly | advisory / trusted-only |
| 2 — Containerlab | `containerlab-frr` | `ci` (privileged) | `workflow_dispatch`, repo var `ENABLE_CONTAINERLAB_TESTS`, nightly | advisory / trusted-only |
| 3 — deploy safety | `apply.yml` (manual, `production`, Icinga pre/post + Goss), `drift-detection.yml` (nightly check-mode) | `ci` (privileged) | manual / schedule | deploy-time |

All of Tier 0 is in `.github/workflows/iac-tests.yml`. Tiers 1–2 also live there
(gated off PRs) and run nightly via `.github/workflows/netops-nightly.yml`.

### Tier 0 — static (required)

`static-iac` runs `scripts/ci/iac-static.sh`, which is intentionally
dependency-light: a stdlib `unittest` discovery over `tests/iac/` plus external
validators (`named-checkzone`, `systemd-analyze`, `caddy adapt`,
`unbound-checkconf`, `nft -c`) when the tool is present on the runner.

The `unittest` suite includes the **source-of-truth schema gate**
(`tests/iac/test_inventory_schema.py`): it validates the structure and internal
consistency of `ansible/inventory/{hosts.yml,group_vars/all.y
...
```

# Citations

[1] [docs/netops/testing-strategy.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/netops/testing-strategy.md)
