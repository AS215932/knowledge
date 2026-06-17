---
type: Workflow
title: Token-less Semgrep SAST. Runs on the UNPRIVILEGED `hyrule-public-pr` runner,
description: '--- name: semgrep'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/semgrep.yml
tags:
- as215932
- network-operations
- workflow
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: .github/workflows/semgrep.yml
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-64
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/semgrep.yml#L1-L64
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: .github/workflows/semgrep.yml
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `.github/workflows/semgrep.yml` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `64` |

# Detected headings

* `# Token-less Semgrep SAST. Runs on the UNPRIVILEGED `hyrule-public-pr` runner,`
* `# uploads SARIF to GitHub Code Scanning (free for this public repo). No`
* `# SEMGREP_APP_TOKEN / no Semgrep Cloud account. Reporting-only during baseline`
* `# (continue-on-error) — flip to a gate once findings are triaged.`
* `# Design: docs/ci/semgrep.md.`
* `# Fail fast instead of hanging the single runner. The semgrep image (~1.3 GB)`
* `# is heavy on first pull on the small ci-pr VM; it's pre-cached, but this caps`
* `# a cold pull. (The job previously had no timeout, so a slow pull hung it.)`
* `# Run Semgrep via `docker run` (not a job-level `container:`) so the`
* `# Node-based upload-sarif action runs in the normal runner environment,`
* `# not inside the minimal semgrep image (which has no Node).`
* `# Same-repo PRs / pushes get Code Scanning upload. Fork PRs lack`
* `# security-events:write — Wave 3 adds a $GITHUB_STEP_SUMMARY fallback.`

# Citations

[1] [.github/workflows/semgrep.yml](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/.github/workflows/semgrep.yml)
