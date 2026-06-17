---
type: Agent Instruction
title: AS215932 Infrastructure Agent Guide
description: '- Before making changes, run `git branch --show-current` and `git status
  --short`. - Unless the user explicitly says to continue work on the current branch,
  create a fresh task branch from up-to-date `main` before editing: - `git fetch o...'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md
tags:
- agent-instruction
- as215932
- network-operations
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: AGENTS.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-53
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md#L1-L53
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: AGENTS.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `AGENTS.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `53` |

# Detected headings

* `# AS215932 Infrastructure Agent Guide`
* `## Branch Hygiene - Read Before Editing or Pushing`
* `## Pull Request Hygiene - Do Not Hand Off Red PRs`
* `## Deployment Rules - Read Before Touching App Pins`
* `## Domain Policy`

# Deterministic excerpt

```markdown
# AS215932 Infrastructure Agent Guide

## Branch Hygiene - Read Before Editing or Pushing

- Before making changes, run `git branch --show-current` and `git status --short`.
- Unless the user explicitly says to continue work on the current branch, create a fresh task branch from up-to-date `main` before editing:
  - `git fetch origin main`
  - `git switch -c <type>/<short-task-name> origin/main`
- Never add unrelated work to an existing feature branch or PR just because it is currently checked out.
- If a task is about CI/CD, docs, runner config, or general maintenance, it almost always needs its own branch from `main`; do not build it on a feature branch such as NETCONF/YANG, app promotion, or routing changes.
- Before committing and before pushing, re-check `git status --short`, `git branch --show-current`, and `gh pr list --head "$(git branch --show-current)"` to confirm the branch matches the task.
- If you discover changes were made on the wrong branch, stop and split them onto a new branch from `main` before pushing.

## Pull Request Hygiene - Do Not Hand Off Red PRs

- After opening or updating a PR, wait for automated CI and AI agent reviews to complete before leaving it for a human reviewer.
- Inspect failing checks, AI review comments, and normal review comments; fix real issues in follow-up commits on the same PR branch.
- Respond to review comments that you address,
...
```

# Citations

[1] [AGENTS.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/AGENTS.md)
