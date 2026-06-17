---
type: Workflow
title: Advisory AI PR review (replaces hosted Sourcery). Runs on the UNPRIVILEGED
description: '--- name: pr-agent'
resource: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/.github/workflows/pr-agent.yml
tags:
- as215932
- hyrule-mcp
- workflow
timestamp: '2026-06-15T17:46:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-mcp
  path: .github/workflows/pr-agent.yml
  commit: 326bcc85e1c69f0d7c1839ebaa4abb73acd84185
  lines: 1-51
  url: https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/.github/workflows/pr-agent.yml#L1-L51
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-mcp
source_path: .github/workflows/pr-agent.yml
commit: 326bcc85e1c69f0d7c1839ebaa4abb73acd84185
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-mcp` |
| Path | `.github/workflows/pr-agent.yml` |
| Commit | `326bcc85e1c69f0d7c1839ebaa4abb73acd84185` |
| Lines | `51` |

# Detected headings

* `# Advisory AI PR review (replaces hosted Sourcery). Runs on the UNPRIVILEGED`
* `# `hyrule-public-pr` runner only, with read + PR/issue-comment permissions and`
* `# our own OpenRouter key. Never deploys, never writes code, never auto-merges.`
* `# Config (model/fallback/instructions): .pr_agent.toml.`
* `# Public-fork policy: auto-review ONLY for same-repo PRs; slash commands`
* `# ONLY from trusted authors. Keeps OPENROUTER_API_KEY off fork PRs.`
* `# Pin our models via dynaconf env (SECTION__KEY, same path that`
* `# delivers OPENROUTER__KEY). .pr_agent.toml is only honoured once it is`
* `# on the default branch, so until this PR merges PR-Agent would`
* `# otherwise fall back to its packaged gpt-5.5 default. deepseek-v4-flash`
* `# / minimax-m2.7 are custom models → custom_model_max_tokens required.`

# Citations

[1] [.github/workflows/pr-agent.yml](https://github.com/AS215932/hyrule-mcp/blob/326bcc85e1c69f0d7c1839ebaa4abb73acd84185/.github/workflows/pr-agent.yml)
