---
type: Workflow
title: 'Nightly cadence for the heavy NetOps lab tiers (Wave 5, Stage 1: manual +'
description: '--- name: netops-nightly'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/netops-nightly.yml
tags:
- as215932
- network-operations
- workflow
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: .github/workflows/netops-nightly.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-95
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/netops-nightly.yml#L1-L95
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: .github/workflows/netops-nightly.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `.github/workflows/netops-nightly.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `95` |

# Detected headings

* `# Nightly cadence for the heavy NetOps lab tiers (Wave 5, Stage 1: manual +`
* `# nightly). Batfish (control-plane model) and Containerlab (dynamic FRR) are`
* `# too heavy / lab-bound to run on every PR, and they need the privileged ci`
* `# runner (Docker + lab infra), so they run here on a schedule and on manual`
* `# dispatch — never automatically on an untrusted PR. Live check-mode drift is`
* `# owned by drift-detection.yml; render validation by render-check.yml; this`
* `# workflow does not duplicate either. Failures alert the NOC via Discord.`

# Citations

[1] [.github/workflows/netops-nightly.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/netops-nightly.yml)
