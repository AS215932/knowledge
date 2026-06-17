---
type: Workflow
title: .github/workflows/ci.yml for AS215932/engineering-loop
description: 'on: pull_request: branches: [main] push: branches: [main]'
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/.github/workflows/ci.yml
tags:
- as215932
- engineering-loop
- workflow
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: .github/workflows/ci.yml
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-66
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/.github/workflows/ci.yml#L1-L66
last_verified_at: '2026-06-17T09:19:10Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: .github/workflows/ci.yml
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `.github/workflows/ci.yml` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
| Lines | `66` |

# Detected headings

* `# .github/workflows/ci.yml for AS215932/engineering-loop`
* `#`
* `# Runs on the UNPRIVILEGED ci-pr runner (label hyrule-public-pr, runner group`
* `# public-pr). The loop's backend executes generated code, so this repo must`
* `# NEVER be added to the privileged hyrule-ci group or the hyrule/hyrule-infra`
* `# runner. Required checks for branch protection on main: ruff, mypy, pytest.`
* `#`
* `# The ci-pr runner has no uv preinstalled; each job installs it via the astral`
* `# script and calls it at ~/.local/bin (matching the hyrule-web CI convention).`
* `# HYRULE_MOCK_LLM defaults on; the suite runs fully offline with the`
* `# MockBackend and never invokes a real harness binary or provider.`
* `# TMPDIR=/tmp so pytest's tmp_path lands under /tmp: the worktree`
* `# tests render NOC handoffs there, and the policy guard's`
* `# allowed_handoff_dirs is ["/tmp"]. The runner's default TMPDIR is`
* `# not /tmp, which would otherwise fail those tests on the handoff`
* `# allowlist while passing locally.`
* `# Offline, deterministic domain-judgment suite; no model, no network.`
* `# Captures AS215932 token capital and blocks regressions in CI.`

# Citations

[1] [.github/workflows/ci.yml](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/.github/workflows/ci.yml)
