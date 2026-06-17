# AS215932 Knowledge Repository

Private OKF knowledge bundle for Servify / Hyrule / AS215932.

This repository is the generated and curated institutional knowledge database for AS215932. It uses Google's draft Open Knowledge Format (OKF): Markdown files with YAML frontmatter, plus deterministic JSONL and SQLite exports for integration. It also provides the read-only foundation for the AS215932 governed learning control plane: authority tiers, machine-checkable claims, policy decisions, context packs, and deterministic eval fixtures.

## Source-of-truth model

Source repositories remain canonical for implemented behavior, executable state, APIs, config, schemas, tests, CI/CD, deployment workflows, repo-local docs, and intended infrastructure state committed as code/config.

OKF is derivative for repo-owned facts. Generated concepts summarize, index, explain, and cross-link source material, but cite repository paths and commits. OKF may be canonical only for explicitly authored institutional knowledge that does not naturally belong in a single repo: cross-repo architecture, ADR rationale, postmortems, operator lessons, durable policy, escalation rules, and strategy.

Conflict policy:

- If OKF disagrees with repo-owned facts, the repo wins and OKF is stale.
- If repo behavior disagrees with OKF-owned institutional policy, create an adjudication issue/task.
- If live state disagrees with repo intended state, treat it as drift evidence.
- If an agent summary disagrees with cited source evidence, source evidence wins.
- If an OKF fact has no citation/provenance, treat it as unverified/advisory.

## Layout

| Path | Purpose |
| --- | --- |
| `okf/` | OKF Markdown bundle. |
| `okf/generated/` | Generated concepts from source repos and GitHub metadata. Do not hand-edit. |
| `okf/curated/` | Human-authored institutional knowledge. Reviewed edits live here. |
| `exports/` | Deterministic JSONL and SQLite exports generated from OKF. |
| `schema/` | Frontmatter, claim, context-pack, policy-decision, and SQLite schemas. |
| `evals/` | Deterministic baseline eval schemas and fixture cases. |
| `src/hyrule_knowledge/` | Ingestion, validation, export, retrieval, policy, context-pack, eval, and MCP tooling. |
| `knowledge.config.yml` | Source list, include/exclude patterns, and project mapping. |
| `knowledge-policy.yml` | Built-in YAML policy evaluator configuration. |

## Common commands

```bash
uv run hyrule-knowledge ingest
uv run hyrule-knowledge enrich --target all --dry-run
uv run hyrule-knowledge observe --profile safe-health
uv run hyrule-knowledge quality --write
uv run hyrule-knowledge quality --check
uv run hyrule-knowledge validate okf
uv run hyrule-knowledge export
uv run hyrule-knowledge query "POST /v1/vm/create schema" --json
uv run hyrule-knowledge context-pack --task "Engineer change to POST /v1/vm/create" --role engineering_loop
uv run hyrule-knowledge eval --check
uv run hyrule-knowledge ledger --check
uv run hyrule-knowledge ledger lifecycle --check
uv run hyrule-knowledge ledger --review noc_shadow:fixture-shadow-eval-summary --promotion-kind summary
uv run hyrule-knowledge scan-secrets okf exports reports evals ledger schema
```

Regenerate and verify everything:

```bash
uv run hyrule-knowledge ingest
uv run hyrule-knowledge validate okf
uv run hyrule-knowledge quality --check
uv run hyrule-knowledge export --check
uv run hyrule-knowledge eval --check
uv run hyrule-knowledge ledger --check
uv run hyrule-knowledge ledger lifecycle --check
uv run hyrule-knowledge scan-secrets okf exports reports evals ledger schema
```

Manual LLM enrichment uses OpenRouter Claude Sonnet 4.6 by default and requires `OPENROUTER_API_KEY` unless `--dry-run` is set:

```bash
uv run hyrule-knowledge enrich --target services --model anthropic/claude-sonnet-4.6
```

Manual safe-health observation uses whichever read-only endpoints are available in the environment and writes observed/evidence concepts under `okf/observed/`:

```bash
PROMETHEUS_URL=http://[mon]:9090 \
HYRULE_MCP_HEALTH_URL=http://127.0.0.1:8765/health \
uv run hyrule-knowledge observe --profile safe-health
```

## Automation

`.github/workflows/ingest.yml` runs nightly and on manual dispatch. When source knowledge changes, it opens a refresh PR. The PR must be reviewed before merge; generated knowledge is never auto-merged.

## Governed agent consumption

Humans can browse `okf/index.md`. Agents should first read `okf/index.md`, then directory indexes, then individual concepts. Machine consumers should prefer `exports/knowledge.sqlite` and the JSONL exports:

- `claims.jsonl` / `claims` table for subject-predicate-object facts with authority tier, freshness, and provenance.
- `concepts.jsonl`, `edges.jsonl`, and SQLite FTS for exact + graph + text retrieval.
- `context-packs.jsonl` / `context_packs` table for policy-aware task context when explicitly generated.
- `policy-decisions.jsonl` / `policy_decisions` table for audited policy outputs.
- `eval-cases.jsonl` and `eval-results.jsonl` for deterministic retrieval/grounding/policy baselines.
- `learning-events.jsonl` / `learning_events` table for sanitized fixture/local-artifact learning summaries awaiting human review.
- `ledger/reviews/` for human review decisions that promote or reject learning events.

Authority tiers are ordered A0 source truth, A1 reviewed OKF, A2 reviewed trace summaries, A3 observations, A4 hypotheses, A5 vector hints. Vectors are deliberately not implemented in this tranche; retrieval score objects include null vector fields for future compatibility only.

Useful read-only commands:

```bash
uv run hyrule-knowledge resolve generated/services/hyrule-cloud
uv run hyrule-knowledge claims --subject service:hyrule-cloud --authority-min A0
uv run hyrule-knowledge neighborhood generated/services/hyrule-cloud --depth 2
uv run hyrule-knowledge endpoint-schema POST /v1/vm/create
uv run hyrule-knowledge deployment-pins hyrule-cloud
uv run hyrule-knowledge policy-decision --actor engineering_loop --action knowledge.search
uv run hyrule-knowledge ledger --write
uv run hyrule-knowledge ledger import /path/to/*.learning-event.json
uv run hyrule-knowledge ledger --list
uv run hyrule-knowledge ledger --review engineering_loop:fixture-run-summary --promotion-kind summary
uv run hyrule-knowledge ledger promote-pr engineering_loop:fixture-run-summary --reviewer svag --promotion-kind summary --rationale "reviewed"
uv run hyrule-knowledge ledger lifecycle --write
uv run hyrule-knowledge mcp --transport stdio
```
