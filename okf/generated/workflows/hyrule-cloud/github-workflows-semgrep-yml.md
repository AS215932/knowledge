---
type: Workflow
title: Token-less Semgrep SAST on the UNPRIVILEGED hyrule-public-pr runner; uploads
description: '--- name: semgrep'
resource: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/.github/workflows/semgrep.yml
tags:
- as215932
- hyrule-cloud
- workflow
timestamp: '2026-06-16T13:11:34Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-cloud
  path: .github/workflows/semgrep.yml
  commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
  lines: 1-52
  url: https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/.github/workflows/semgrep.yml#L1-L52
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-cloud
source_path: .github/workflows/semgrep.yml
commit: 81e4316f3d1f4e7f770bc2589bd84a2c7972aad5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-cloud` |
| Path | `.github/workflows/semgrep.yml` |
| Commit | `81e4316f3d1f4e7f770bc2589bd84a2c7972aad5` |
| Lines | `52` |

# Detected headings

* `# Token-less Semgrep SAST on the UNPRIVILEGED hyrule-public-pr runner; uploads`
* `# SARIF to GitHub Code Scanning (free for this public repo). No SEMGREP_APP_TOKEN.`
* `# Reporting-only during baseline (continue-on-error) — flip to a gate later.`
* `# Run via `docker run` (not a job-level container:) so upload-sarif (Node)`
* `# runs in the normal runner env, not the minimal semgrep image.`

# Citations

[1] [.github/workflows/semgrep.yml](https://github.com/AS215932/hyrule-cloud/blob/81e4316f3d1f4e7f770bc2589bd84a2c7972aad5/.github/workflows/semgrep.yml)
