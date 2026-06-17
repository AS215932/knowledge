---
type: Workflow
title: semgrep
description: GitHub Actions workflow `semgrep` from AS215932/hyrule-web.
resource: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/semgrep.yml
tags:
- ci
- github-actions
- hyrule-web
- workflow
timestamp: '2026-06-16T15:09:49Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-web
  path: .github/workflows/semgrep.yml
  commit: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
  url: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/semgrep.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-web
source_path: .github/workflows/semgrep.yml
triggers:
- pull_request
- workflow_dispatch
- push
- schedule
---

# Workflow

| Field | Value |
| --- | --- |
| Name | `semgrep` |
| Source | `.github/workflows/semgrep.yml` |
| Triggers | `pull_request, workflow_dispatch, push, schedule` |
| Deploy-like | `False` |
| Workflow permissions | `{"contents": "read", "security-events": "write"}` |

# Jobs

| Job | Runs on | Environment | Permissions |
| --- | --- | --- | --- |
| `semgrep` | `self-hosted, linux, x64, hyrule-public-pr` | `` | `{}` |

# Secrets referenced by name

No `secrets.*` references detected.

# Operational notes

This workflow summary is statically parsed from GitHub Actions YAML. It intentionally records secret names only, never values.

# Citations

[1] [.github/workflows/semgrep.yml](https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/semgrep.yml)
