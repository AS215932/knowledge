---
type: Workflow
title: Advisory AI PR review (replaces hosted Sourcery). Runs on the UNPRIVILEGED
description: '--- name: pr-agent'
resource: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/pr-agent.yml
tags:
- as215932
- hyrule-web
- workflow
timestamp: '2026-06-16T15:09:49Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/hyrule-web
  path: .github/workflows/pr-agent.yml
  commit: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
  lines: 1-57
  url: https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/pr-agent.yml#L1-L57
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/hyrule-web
source_path: .github/workflows/pr-agent.yml
commit: d94146e67f9eb05f8eeb5c57cab74cbe676f5c79
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/hyrule-web` |
| Path | `.github/workflows/pr-agent.yml` |
| Commit | `d94146e67f9eb05f8eeb5c57cab74cbe676f5c79` |
| Lines | `57` |

# Detected headings

* `# Advisory AI PR review (replaces hosted Sourcery). Runs on the UNPRIVILEGED`
* `# `hyrule-public-pr` runner only, with read + PR/issue-comment permissions and`
* `# our own OpenRouter key. Never deploys, never writes code, never auto-merges.`
* `# Config (model/fallback/instructions): .pr_agent.toml.`
* `# Public-fork policy: auto-review ONLY for same-repo (internal) PRs, and`
* `# slash commands ONLY from trusted authors. This keeps OPENROUTER_API_KEY`
* `# off untrusted fork PRs and stops anyone from burning the OpenRouter`
* `# budget via /ask, /improve, etc.`
* `# PR-Agent reads the OpenRouter key from openrouter__key; litellm also`
* `# honours OPENROUTER_API_KEY. Set both from the org secret.`
* `# Force our models via dynaconf env (SECTION__KEY, double underscore —`
* `# the same mechanism OPENROUTER__KEY uses, proven to reach the action`
* `# container). .pr_agent.toml is NOT honoured until it is on the default`
* `# branch (no checkout step; PR-Agent loads repo settings from the`
* `# default branch), so until this merges PR-Agent would fall back to its`
* `# packaged gpt-5.5 default. These env vars override that regardless.`
* `# deepseek-v4-flash/minimax-m2.7 are custom models → max_tokens needed.`

# Citations

[1] [.github/workflows/pr-agent.yml](https://github.com/AS215932/hyrule-web/blob/d94146e67f9eb05f8eeb5c57cab74cbe676f5c79/.github/workflows/pr-agent.yml)
