---
type: Workflow
title: Renders every playbook in --tags validate --connection=local mode and
description: '--- name: render-check'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/render-check.yml
tags:
- as215932
- network-operations
- workflow
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: .github/workflows/render-check.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-53
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/render-check.yml#L1-L53
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: .github/workflows/render-check.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `.github/workflows/render-check.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `53` |

# Detected headings

* `# Renders every playbook in --tags validate --connection=local mode and`
* `# asserts that the checked-in ansible/generated/ output matches what the`
* `# render produces. Catches stale generated/ checkins (the operator forgot`
* `# to commit a re-render) and template typos that don't surface until apply.`
* `# Catch BOTH modified tracked files and brand-new untracked renders`
* `# (a never-committed generated file slips past `git diff --exit-code`).`

# Citations

[1] [.github/workflows/render-check.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/render-check.yml)
