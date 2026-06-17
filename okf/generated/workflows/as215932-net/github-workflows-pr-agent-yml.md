---
type: Workflow
title: pr-agent
description: GitHub Actions workflow `pr-agent` from AS215932/as215932.net.
resource: https://github.com/AS215932/as215932.net/blob/9c0ee2d8f2bb793ea799589ca0fe4f77571b2572/.github/workflows/pr-agent.yml
tags:
- as215932.net
- deploy
- github-actions
- workflow
timestamp: '2026-06-13T17:48:17Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/as215932.net
  path: .github/workflows/pr-agent.yml
  commit: 9c0ee2d8f2bb793ea799589ca0fe4f77571b2572
  url: https://github.com/AS215932/as215932.net/blob/9c0ee2d8f2bb793ea799589ca0fe4f77571b2572/.github/workflows/pr-agent.yml
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/as215932.net
source_path: .github/workflows/pr-agent.yml
triggers:
- pull_request
- issue_comment
---

# Workflow

| Field | Value |
| --- | --- |
| Name | `pr-agent` |
| Source | `.github/workflows/pr-agent.yml` |
| Triggers | `pull_request, issue_comment` |
| Deploy-like | `True` |
| Workflow permissions | `{"contents": "read", "issues": "write", "pull-requests": "write"}` |

# Jobs

| Job | Runs on | Environment | Permissions |
| --- | --- | --- | --- |
| `pr-agent` | `self-hosted, linux, x64, hyrule-public-pr` | `` | `{}` |

# Secrets referenced by name

* `GITHUB_TOKEN`
* `OPENROUTER_API_KEY`

# Operational notes

This workflow summary is statically parsed from GitHub Actions YAML. It intentionally records secret names only, never values.

# Citations

[1] [.github/workflows/pr-agent.yml](https://github.com/AS215932/as215932.net/blob/9c0ee2d8f2bb793ea799589ca0fe4f77571b2572/.github/workflows/pr-agent.yml)
