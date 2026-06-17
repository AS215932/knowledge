---
type: Source Document
title: Acceptance Gates
description: The Hyrule Engineering Loop must select gates based on changed repos
  and change class. Production apply is never automatic from the development loop.
resource: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/acceptance-gates.md
tags:
- as215932
- network-operations
- source-document
timestamp: '2026-06-17T08:13:24Z'
truth_owner: repo
authority: canonical
source_refs:
- repo: AS215932/network-operations
  path: docs/agent-loops/acceptance-gates.md
  commit: 67061d325834a7145252cdf851da1df6a4a38b9e
  lines: 1-419
  url: https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/acceptance-gates.md#L1-L419
last_verified_at: '2026-06-17T10:18:30Z'
confidence: high
dispute_policy: repo_wins
repo: AS215932/network-operations
source_path: docs/agent-loops/acceptance-gates.md
commit: 67061d325834a7145252cdf851da1df6a4a38b9e
---

# Source

| Field | Value |
| --- | --- |
| Repository | `AS215932/network-operations` |
| Path | `docs/agent-loops/acceptance-gates.md` |
| Commit | `67061d325834a7145252cdf851da1df6a4a38b9e` |
| Lines | `419` |

# Detected headings

* `# Acceptance Gates`
* `## hyrule-infra`
* `## hyrule-cloud`
* `## hyrule-web`
* `## hyrule-mcp`
* `## hyrule-noc-agent`
* `## MCP Contract Enforcement`
* `## Digital Twin / Local Emulation`
* `## Break-Glass Rollback`
* `## Phase 2 Local Gate Runner`
* `## Phase 3 Mutation Workspace`
* `## Phase 4 NOC Handoff`
* `## Phase 5 Worktree Promotion`
* `## Phase 6 PR Boundary`
* `## Phase 7 Policy Guards`
* `## Phase 8 Repo Adapter Dry Run`
* `## Phase 10 Operator Dry-Run Harness`
* `## Phase 11 Sibling-Repo Canary Dry Run`
* `## Phase 13 Feature Intake`
* `## Phase 14 Trace And Pi Loop UX`
* `## Phase 15 Model Routing`
* `## Phase 16 Model UX And Trace Review`
* `## Phase 17 Feature Writer UX`
* `## Phase 18 Live Implementation Writer`

# Deterministic excerpt

```markdown
# Acceptance Gates

The Hyrule Engineering Loop must select gates based on changed repos and change
class. Production apply is never automatic from the development loop.

## hyrule-infra

Docs-only:

```bash
git diff --check
```

Ansible/config:

```bash
cd ansible
ansible-playbook playbooks/firewall.yml --tags validate --connection=local --skip-tags snapshot
```

Broader infra uses existing CI workflows:

- `render-check.yml`
- `iac-tests.yml`
- `netops-nightly.yml`
- `drift-detection.yml`
- manual `apply.yml` with production environment approval

## hyrule-cloud

```bash
uv run --group dev python -m pytest -q
uv run --group dev ruff check .
uv run --group dev mypy hyrule_cloud
```

## hyrule-web

```bash
uv run --group dev python -m pytest -q
npm run check
```

## hyrule-mcp

```bash
uv run --group dev python -m pytest -q
```

Live smoke is opt-in only:

```bash
HYRULE_MCP_LIVE_SMOKE=1 uv run --group dev python -m pytest -q tests/test_live_smoke.py
```

## hyrule-noc-agent

```bash
uv run --group dev python -m pytest -q
```

Live smoke is opt-in only:

```bash
NOC_AGENT_LIVE_SMOKE=1 uv run --group dev python -m pytest -q tests/test_live_smoke.py
```

## MCP Contract Enforcement

If an engineering change alters diagnostic output, command syntax, log shape,
or MCP tool schema, set `mcp_schema_breaking = true`. The change then requires
coordinated planning with `hyrule-mcp` so NOC incident diagnostics are not
blinded by schema drift.

## Digital Twin / Local Emulation

Required for:

- `routing_bgp_frr`
- `firewall_policy`
- high-risk OS/runtime changes

Use trusted lab tooling where available, such as Batfish, Containerlab, or
nested local hypervisor validation. The gate must verify native target config
parsing, routing convergence or firewall isolation, expected failur
...
```

# Citations

[1] [docs/agent-loops/acceptance-gates.md](https://github.com/AS215932/network-operations/blob/67061d325834a7145252cdf851da1df6a4a38b9e/docs/agent-loops/acceptance-gates.md)
