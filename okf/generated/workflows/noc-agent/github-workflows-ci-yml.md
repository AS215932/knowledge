---
type: Workflow
title: ci
description: GitHub Actions workflow `ci` from AS215932/noc-agent.
resource: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/.github/workflows/ci.yml
tags:
- ci
- github-actions
- noc-agent
- workflow
timestamp: '2026-06-17T07:49:45Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/noc-agent
  path: .github/workflows/ci.yml
  commit: 98e5010648e34ac0ea6ad8e6a925fef76d0dbea9
  url: https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/.github/workflows/ci.yml
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/noc-agent
source_path: .github/workflows/ci.yml
triggers:
- pull_request
- push
---

# Workflow

| Field | Value |
| --- | --- |
| Name | `ci` |
| Source | `.github/workflows/ci.yml` |
| Triggers | `pull_request, push` |
| Deploy-like | `False` |
| Workflow permissions | `{"contents": "read"}` |

# Jobs

| Job | Runs on | Environment | Permissions |
| --- | --- | --- | --- |
| `test` | `self-hosted, linux, x64, hyrule-public-pr` | `` | `{}` |

# Secrets referenced by name

No `secrets.*` references detected.

# Operational notes

This workflow summary is statically parsed from GitHub Actions YAML. It intentionally records secret names only, never values.

# Citations

[1] [.github/workflows/ci.yml](https://github.com/AS215932/noc-agent/blob/98e5010648e34ac0ea6ad8e6a925fef76d0dbea9/.github/workflows/ci.yml)
