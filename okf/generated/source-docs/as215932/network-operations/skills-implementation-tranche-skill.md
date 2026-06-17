---
type: Skill
title: Implementation tranche
description: '--- name: implementation-tranche description: Working contract for the
  implementation backend producing one engineering-loop tranche inside a guarded worktree.
  triggers: [every implementation run] ---'
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/implementation-tranche/SKILL.md
tags:
- as215932
- network-operations
- skill
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: skills/implementation-tranche/SKILL.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-51
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/implementation-tranche/SKILL.md#L1-L51
last_verified_at: '2026-06-17T10:33:31Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: skills/implementation-tranche/SKILL.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `skills/implementation-tranche/SKILL.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `51` |

# Detected headings

* `# Implementation tranche`
* `## Workflow`
* `## Anti-rationalization`
* `## Exit criteria`

# Deterministic excerpt

```markdown
---
name: implementation-tranche
description: Working contract for the implementation backend producing one engineering-loop tranche inside a guarded worktree.
triggers: [every implementation run]
---

# Implementation tranche

You are producing the smallest useful tranche for the active task spec, in a
branch-backed worktree. The diff is the deliverable; evidence makes it real.

## Workflow

1. **Read the contract.** Open the task spec (`tasks/<change-id>.md`). Note
   `allowed_paths`, acceptance criteria, non-goals, and budget.
   *Checkpoint: restate the acceptance criteria in your plan before editing.*
2. **Read the lessons.** Open `memory/lessons/<repo>.md` if present. Treat
   every entry as a hard constraint.
3. **Explore before editing.** Find the existing pattern for what you're
   about to write (similar module, similar test, similar config block).
   Reuse it; do not invent a parallel convention.
4. **Implement inside `allowed_paths` only.** Touch only what the spec asks
   you to touch. If the right fix lies outside the allowlist, stop and
   report that instead of working around it.
5. **Run the gates yourself after each meaningful edit.** The spec lists
   them; default to the repo's gates in
   `docs/agent-loops/acceptance-gates.md`.
   *Checkpoint: paste the failing output you fixed, not just the final pass.*
6. **Self-review the diff** (`git diff`): no secrets, no commented-out
   code, no test deletions or skips, no drive-by refactors, complete-but-
   minimal.
7. **Report.** Summarize what changed, evidence per acceptance criterion,
   and anything you could not satisfy and why.

## Anti-rationalization

| Excuse | Rebuttal |
|---|---|
| "This task is too small for the spec's criteria" | Criteria still apply; satisfying five lines of criteria is fast.
...
```

# Citations

[1] [skills/implementation-tranche/SKILL.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/skills/implementation-tranche/SKILL.md)
