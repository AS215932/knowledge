---
type: Workflow
title: roles_path lives in ansible/ansible.cfg, which isn't picked up when lint
description: '--- name: lint'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/lint.yml
tags:
- as215932
- network-operations
- workflow
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: .github/workflows/lint.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-84
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/lint.yml#L1-L84
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: .github/workflows/lint.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `.github/workflows/lint.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `84` |

# Detected headings

* `# roles_path lives in ansible/ansible.cfg, which isn't picked up when lint`
* `# runs from the repo root — point ansible at ansible/roles explicitly so`
* `# syntax-check can resolve role references.`
* `# Skip generated/, but lint all hand-written scripts.`
* `# --severity=error keeps this permissive at launch (the existing`
* `# scripts have warning/style/info findings only); tighten via #58.`

# Citations

[1] [.github/workflows/lint.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/lint.yml)
