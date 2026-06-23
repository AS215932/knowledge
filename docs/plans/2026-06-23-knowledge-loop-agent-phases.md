# Knowledge Loop Agent — Phases 1 and 2

## Intent

Turn `AS215932/knowledge` from a manual/tooling repository plus read-only MCP server into a governed autonomous Knowledge Loop agent, comparable in shape to Engineering Loop and NOC Agent.

The read-only Knowledge MCP remains a serving dependency for Engineering Loop. The Knowledge Loop is a separate producer agent that refreshes, validates, enriches, imports learning artifacts, and opens reviewable PRs/issues. It must never auto-merge and must not promote generated synthesis to canonical truth without human review.

## Runtime boundaries

- Run on `loop` as a dedicated unprivileged `knowledge-loop` runtime.
- Use a systemd one-shot service plus timer.
- Use Vault-backed runtime credentials scoped to Knowledge Loop only.
- Do not mount fleet SSH credentials, Docker socket, app runtime credentials, wallet data, or broad Vault access.
- Do not write directly to `main`.
- All repository mutation exits as a PR.
- All generated synthesis remains advisory unless reviewed/promoted by humans.

## Phase 1 — deterministic loop skeleton

Build `hyrule-knowledge loop --once` with:

1. Singleton state lock under the Knowledge Loop state directory.
2. Per-day ledger with cycle and PR counters.
3. Deterministic refresh and validation commands:
   - `hyrule-knowledge ingest`
   - `ruff check src tests`
   - `mypy --strict src`
   - `pytest`
   - `hyrule-knowledge validate okf`
   - `hyrule-knowledge quality --check`
   - `hyrule-knowledge export --check`
   - `hyrule-knowledge eval --check`
   - `hyrule-knowledge ledger --check`
   - `hyrule-knowledge ledger lifecycle --check`
   - `hyrule-knowledge scan-secrets okf exports reports evals ledger schema`
4. Optional dry-run enrichment plumbing for proving source-pack/writer paths without provider calls.
5. Git branch/commit/push/PR creation when there are changes.
6. JSON report output for every cycle.
7. Optional passive Icinga heartbeat.
8. Tests for lock, budget, command sequencing, PR gating, and heartbeat behavior.

## Phase 2 — Knowledge production work

Extend the loop with opt-in bounded producer work:

1. OpenRouter LLM enrichment targets using the Knowledge Loop credential scope.
2. Learning-event import from sanitized artifact directories.
3. Budget gates for provider calls and imported artifacts.
4. Validation/export/eval/secret-scan after phase-2 mutation.
5. PR output for enrichment/import changes.
6. Tests that prove phase-2 command sequencing and budget behavior without live provider calls.

## Deployment follow-up

Add NetOps source-managed runtime:

- `knowledge_loop` Ansible role.
- Vault Agent template for `/etc/knowledge-loop/knowledge-loop.env`.
- systemd service/timer.
- host_vars on `loop` for disabled-by-default canary rollout.
- monitoring passive check for loop freshness/status.

## Human gates

- Humans review Knowledge Loop PRs.
- Humans merge Knowledge PRs.
- Humans decide curated A1 promotion.
- Deployment of updated Knowledge MCP remains a NetOps pin-bump/apply path.
