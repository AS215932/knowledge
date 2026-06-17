---
type: Workflow
title: Tiered IaC test pipeline (Wave 5).
description: '--- name: iac-tests'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/iac-tests.yml
tags:
- as215932
- network-operations
- workflow
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: .github/workflows/iac-tests.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-239
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/iac-tests.yml#L1-L239
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: .github/workflows/iac-tests.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `.github/workflows/iac-tests.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `239` |

# Detected headings

* `# Tiered IaC test pipeline (Wave 5).`
* `#`
* `#   Tier 0  static-iac, ansible-idempotency   unprivileged ci-pr   required (via iac-gate)`
* `#   Tier 1  batfish                            privileged   ci      trusted-only (dispatch/nightly/var)`
* `#   Tier 2  containerlab-frr                   privileged   ci      trusted-only (dispatch/nightly/var)`
* `#`
* `# Tier 0 runs untrusted PR code, so it lives on the unprivileged hyrule-public-pr`
* `# runner. Tiers 1-2 spin up Batfish / Containerlab (heavy lab infra + Docker) on`
* `# the privileged ci runner and only run on a trusted trigger — never automatically`
* `# on an arbitrary PR. The `iac-gate` job is the single REQUIRED status context:`
* `# this workflow always starts, a cheap `changes` job decides whether IaC paths`
* `# changed, and `iac-gate` reports for both docs-only and IaC PRs. IaC PRs only`
* `# pass when the required tiers succeed and the lab tiers are`
* `# success-or-skipped (never failed). See docs/netops/testing-strategy.md.`
* `# ---- Tier 0: static, unprivileged, required ---------------------------`
* `# ---- Tier 1: Batfish control-plane model (privileged, trusted-only) ---`
* `# ---- Tier 2: Containerlab dynamic FRR (privileged, trusted-only) ------`
* `# ---- Aggregating gate: the single REQUIRED context --------------------`
* `# Required tiers must succeed when IaC-relevant paths changed.`
* `# Trusted lab tiers may be skipped on PRs, but must never fail.`

# Citations

[1] [.github/workflows/iac-tests.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/iac-tests.yml)
