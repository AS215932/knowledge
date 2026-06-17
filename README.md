# AS215932 Knowledge Repository

Private OKF knowledge bundle for Servify / Hyrule / AS215932.

This repository is the generated and curated institutional knowledge database for AS215932. It uses Google's draft Open Knowledge Format (OKF): Markdown files with YAML frontmatter, plus deterministic JSONL and SQLite exports for integration.

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
| `schema/` | Frontmatter and SQLite schemas. |
| `src/hyrule_knowledge/` | Ingestion, validation, and export tooling. |
| `knowledge.config.yml` | Source list, include/exclude patterns, and project mapping. |

## Common commands

```bash
uv run hyrule-knowledge ingest
uv run hyrule-knowledge enrich --target all --dry-run
uv run hyrule-knowledge observe --profile safe-health
uv run hyrule-knowledge quality --write
uv run hyrule-knowledge quality --check
uv run hyrule-knowledge validate okf
uv run hyrule-knowledge export
uv run hyrule-knowledge scan-secrets okf exports reports
```

Regenerate and verify everything:

```bash
uv run hyrule-knowledge ingest
uv run hyrule-knowledge validate okf
uv run hyrule-knowledge quality --check
uv run hyrule-knowledge export --check
uv run hyrule-knowledge scan-secrets okf exports reports
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

## OKF consumption

Humans can browse `okf/index.md`. Agents should first read `okf/index.md`, then directory indexes, then individual concepts. Machine consumers should prefer `exports/concepts.jsonl`, `exports/edges.jsonl`, and `exports/knowledge.sqlite`.
