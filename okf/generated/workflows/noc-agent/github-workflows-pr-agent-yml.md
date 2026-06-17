---
type: Workflow
title: pr-agent
description: GitHub Actions workflow `pr-agent` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/.github/workflows/pr-agent.yml
tags:
- deploy
- github-actions
- noc-agent
- workflow
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: .github/workflows/pr-agent.yml
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/.github/workflows/pr-agent.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
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

[1] [.github/workflows/pr-agent.yml](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/.github/workflows/pr-agent.yml)
