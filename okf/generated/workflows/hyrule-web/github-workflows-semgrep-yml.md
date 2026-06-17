---
type: Workflow
title: Token-less Semgrep SAST. Runs on the UNPRIVILEGED `hyrule-public-pr` runner,
description: '--- name: semgrep'
resource: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/semgrep.yml
tags:
- as215932
- hyrule-web
- workflow
timestamp: '2026-06-16T15:09:49Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-web
  path: .github/workflows/semgrep.yml
  commit: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
  lines: 1-65
  url: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/semgrep.yml#L1-L65
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-web
source_path: .github/workflows/semgrep.yml
commit: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-web` |
| Path | `.github/workflows/semgrep.yml` |
| Commit | `d94146e67f9eb05f8eeb5c57cab74cbe676f5c79` |
| Lines | `65` |

# Detected headings

* `# Token-less Semgrep SAST. Runs on the UNPRIVILEGED `hyrule-public-pr` runner,`
* `# uploads SARIF to GitHub Code Scanning (free for this public repo). No`
* `# SEMGREP_APP_TOKEN / no Semgrep Cloud account. Reporting-only during baseline`
* `# (continue-on-error) — flip to a gate once findings are triaged.`
* `# hyrule-web is Python(uv) backend + TS/Vite frontend, so both stacks' packs.`
* `# Cap a cold pull of the heavy semgrep image on the small ci-pr VM.`
* `# Run Semgrep via `docker run` (not a job-level `container:`) so the`
* `# Node-based upload-sarif action runs in the normal runner environment,`
* `# not inside the minimal semgrep image (which has no Node).`
* `# Same-repo PRs / pushes get Code Scanning upload. Fork PRs lack`
* `# security-events:write — surfaced via job logs/summary instead.`

# Citations

[1] [.github/workflows/semgrep.yml](https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/semgrep.yml)
