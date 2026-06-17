---
type: Source Document
title: Task spec template — tasks/<change-id>.md
description: '--- change_id: EXAMPLE_CHANGE change_class: app_bugfix # one of the
  v1 change classes risk_level: low # low | medium | high | critical customer_impact:
  none # none | possible | expected repos: hyrule-cloud: allowed_paths: ["hyrule_cloud/...'
resource: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/engineering-loop/templates/task-spec.md
tags:
- as215932
- engineering-loop
- source-document
timestamp: '2026-06-16T07:29:23Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/engineering-loop
  path: docs/engineering-loop/templates/task-spec.md
  commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
  lines: 1-57
  url: https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/engineering-loop/templates/task-spec.md#L1-L57
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/engineering-loop
source_path: docs/engineering-loop/templates/task-spec.md
commit: 768cde6c996e42f3f91d395347ba9809e2e020e5
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/engineering-loop` |
| Path | `docs/engineering-loop/templates/task-spec.md` |
| Commit | `768cde6c996e42f3f91d395347ba9809e2e020e5` |
| Lines | `57` |

# Detected headings

* `# Task spec template — tasks/<change-id>.md`
* `#`
* `# The sprint contract for one engineering-loop tranche. Frontmatter is the`
* `# machine-readable contract; the body is the human/agent-readable intent.`
* `# "Done" is defined here, before generation starts — evaluators grade the`
* `# diff against the acceptance criteria below, not against vibes.`
* `## Intent`
* `## Acceptance criteria`
* `## Done-conditions`
* `## Non-goals`
* `## Role consult notes`
* `## Rollback sketch`

# Deterministic excerpt

```markdown
# Task spec template — tasks/<change-id>.md
#
# The sprint contract for one engineering-loop tranche. Frontmatter is the
# machine-readable contract; the body is the human/agent-readable intent.
# "Done" is defined here, before generation starts — evaluators grade the
# diff against the acceptance criteria below, not against vibes.

---
change_id: EXAMPLE_CHANGE
change_class: app_bugfix          # one of the v1 change classes
risk_level: low                   # low | medium | high | critical
customer_impact: none             # none | possible | expected
repos:
  hyrule-cloud:
    allowed_paths: ["hyrule_cloud/", "tests/"]
required_roles: []                # filled by the planner from the role matrix
gates: []                         # filled from acceptance-gates.md per repo/class
budget:
  max_iterations: 20
  max_wall_clock_minutes: 45
  max_cost_usd: 5.00
intake_source: "operator"         # operator | issue:<repo>#<n> | signal:<miner>
---

## Intent

One or two sentences: what this tranche changes and why.

## Acceptance criteria

Testable statements only. Each criterion must be verifiable by a gate, a
test, or direct inspection of the diff.

1. ...
2. ...

## Done-conditions

The run is complete when all acceptance criteria hold AND:

- all gates in the frontmatter pass in the worktree;
- the diff touches only `allowed_paths`;
- every required role judgment is `approve`.

## Non-goals

What this tranche explicitly does not do (scope fence for the backend).

## Role consult notes

Appended by the plan-consult pass — one subsection per required role with
the constraints that role demands of the diff.

## Rollback sketch

How this change is undone if it regresses after deploy (feeds the PR
contract's rollback section and the NOC handoff).
```

# Citations

[1] [docs/engineering-loop/templates/task-spec.md](https://github.com/AS215932/engineering-loop/blob/768cde6c996e42f3f91d395347ba9809e2e020e5/docs/engineering-loop/templates/task-spec.md)
