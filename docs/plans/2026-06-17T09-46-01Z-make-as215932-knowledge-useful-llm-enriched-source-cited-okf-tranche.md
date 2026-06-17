---
created: 2026-06-17T09:46:01.999Z
source: pi-plan-mode
status: accepted-for-execution
---

# Make AS215932 Knowledge Useful — LLM-Enriched, Source-Cited OKF Tranche

## Summary

Upgrade `AS215932/knowledge` from a valid but shallow OKF catalog into a useful operational knowledge base.

This tranche will add:

- LLM-first, source-cited enrichment using OpenRouter Claude Sonnet 4.6.
- Rich top-level organization, project, service, architecture, policy, and lesson pages.
- Better endpoint, schema, workflow, infrastructure, DNS, deploy-pin, and monitoring extraction.
- Coverage and usefulness reports.
- CI gates for critical quality failures.
- Manual/local safe live telemetry ingestion for health/state evidence.
- Manual-dispatch LLM enrichment workflow, not nightly automatic LLM spend.

All repo-owned facts remain source-first. LLM output is advisory unless explicitly promoted/reviewed.

## Implementation Steps

1. Add enrichment, quality, and observation data models.
2. Refactor the generator into typed extractors.
3. Implement richer deterministic extraction.
4. Implement LLM-first source-cited enrichment.
5. Seed useful curated OKF pages.
6. Add safe live telemetry observation ingestion.
7. Add coverage reports and usefulness quality gates.
8. Update exports and SQLite schema.
9. Add workflows, tests, and documentation.
10. Regenerate the bundle and open one focused PR.

## Current State

`AS215932/knowledge` currently has:

- 617 OKF concepts.
- 1091 graph edges.
- JSONL and SQLite exports.
- Valid OKF frontmatter/provenance.
- Shallow generated content:
  - service pages mostly mirror GitHub descriptions;
  - endpoint pages only include method/path/source line;
  - host pages only include type/address/source;
  - no real org page under `okf/generated/org/`;
  - no quality/coverage report;
  - curated folders are empty placeholders.

## Key Decisions

- Use OpenRouter Claude Sonnet 4.6 by default:
  - env: `OPENROUTER_API_KEY`
  - model: `anthropic/claude-sonnet-4.6`
- Deliver as one focused PR/tranche.
- Seed curated source-backed pages.
- CI quality gates:
  - fail critical issues only;
  - report softer usefulness gaps.
- LLM enrichment:
  - manual dispatch only;
  - no nightly automatic LLM run.
- Live telemetry:
  - implement manual/local safe health/state ingestion now;
  - do not schedule until runner/network credentials are designed.
- Telemetry scope:
  - Prometheus target/up summaries;
  - selected Icinga host/service summaries;
  - Hyrule MCP health/tool availability;
  - no logs, packet captures, raw command output, secrets, or payload bodies.

## New/Updated Commands

Add these CLI commands:

```bash
uv run hyrule-knowledge ingest
uv run hyrule-knowledge enrich --target all
uv run hyrule-knowledge observe --profile safe-health
uv run hyrule-knowledge quality --write
uv run hyrule-knowledge quality --check
uv run hyrule-knowledge export
uv run hyrule-knowledge validate okf
uv run hyrule-knowledge scan-secrets okf exports reports
```

### `enrich`

Default behavior:

```bash
uv run hyrule-knowledge enrich \
  --target all \
  --provider openrouter \
  --model anthropic/claude-sonnet-4.6 \
  --max-input-chars 120000 \
  --temperature 0.2
```

Requires `OPENROUTER_API_KEY`.

### `observe`

Default behavior:

```bash
uv run hyrule-knowledge observe --profile safe-health
```

Reads optional env vars:

```text
PROMETHEUS_URL
ICINGA_API_BASE
ICINGA_API_USER
ICINGA_API_PASSWORD
HYRULE_MCP_HEALTH_URL
```

If a telemetry source is missing, write a degraded observation concept instead of failing the whole run.

## Repository Layout Changes

Add:

```text
okf/
├── generated/
│   ├── enriched/
│   ├── schemas/
│   ├── deployments/
│   ├── monitoring/
│   └── quality/
├── observed/
│   ├── index.md
│   ├── latest/
│   └── log.md
└── curated/
    ├── architecture/
    ├── decisions/
    ├── lessons/
    ├── policies/
    └── strategy/

reports/
├── coverage.md
├── coverage.json
├── quality.json
└── shallow-concepts.md

src/hyrule_knowledge/
├── enrich.py
├── llm.py
├── observe.py
├── quality.py
├── source_pack.py
└── extractors/
    ├── api.py
    ├── ansible.py
    ├── dns.py
    ├── github_actions.py
    ├── markdown.py
    ├── monitoring.py
    ├── pydantic_models.py
    └── workflows.py
```

## Frontmatter Extensions

All enriched concepts must include:

```yaml
enrichment:
  mode: llm
  provider: openrouter
  model: anthropic/claude-sonnet-4.6
  prompt_version: useful-v1
  input_hash: "<sha256>"
  output_hash: "<sha256>"
  generated_at: "<timestamp>"
review_status: proposed
```

All observed concepts must include:

```yaml
truth_owner: observed
authority: evidence
dispute_policy: evidence_only
observed_at: "<timestamp>"
expires_at: "<timestamp>"
collection_profile: safe-health
```

## LLM Safety Rules

The enrichment prompt must require:

- use only provided source pack content;
- every factual claim must cite a source ref;
- unknown facts must be written as “Unknown from indexed sources”;
- no secrets, token values, cookies, private keys, wallet data, or raw credentials;
- no live-state claims unless sourced from `okf/observed`;
- generated content is advisory unless reviewed.

Reject LLM output if:

- invalid JSON;
- missing citations;
- references unknown source IDs;
- contains forbidden secret patterns;
- contains unsupported canonicality claims;
- produces fewer than required sections for the target type.

## Rich Page Targets

### Organization

Create:

```text
okf/generated/org/as215932.md
```

Required sections:

- Overview
- Identity and domains
- Repositories
- Production services
- Infrastructure footprint
- Operational loops
- Source-of-truth rules
- Key contacts/resources
- Current gaps/open follow-ups
- Citations

### Services/projects

Rewrite/enrich these concepts:

```text
okf/generated/projects/network-operations.md
okf/generated/projects/hyrule-business.md
okf/generated/services/hyrule-cloud.md
okf/generated/services/hyrule-web.md
okf/generated/services/noc-agent.md
okf/generated/services/hyrule-mcp.md
okf/generated/services/hyrule-network-proxy.md
okf/generated/services/engineering-loop.md
okf/generated/services/as215932-net.md
```

Required sections:

- What this is
- Responsibilities
- Runtime/deployment shape
- Interfaces
- Dependencies
- Source-of-truth files
- Operational runbooks
- Safety/security constraints
- Related services
- Open issues/known gaps
- Citations

### Curated seed pages

Create source-backed proposed curated pages:

```text
okf/curated/architecture/as215932-system-map.md
okf/curated/architecture/production-deployment-flow.md
okf/curated/architecture/noc-mcp-diagnostics-loop.md
okf/curated/architecture/hyrule-cloud-product-stack.md
okf/curated/architecture/engineering-loop-vs-noc-loop.md
okf/curated/policies/source-of-truth-and-canonicality.md
okf/curated/policies/domain-policy.md
okf/curated/lessons/deployment-safety-lessons.md
okf/curated/strategy/hyrule-cloud-business-context.md
```

Use:

```yaml
truth_owner: okf
authority: advisory
review_status: proposed
dispute_policy: adjudicate
```

## Deterministic Extraction Improvements

### API extractor

For FastAPI routes:

- parse decorators with `ast`;
- detect method/path;
- detect APIRouter prefix where statically resolvable;
- capture function name;
- capture docstring;
- capture request body parameter model;
- capture response model from decorator if present;
- capture return annotation if present;
- capture dependencies;
- capture status codes from decorator and `HTTPException`;
- link to Pydantic model concepts.

For Go handlers:

- detect registered paths and handler symbols;
- include source line and package;
- mark method as `ANY` unless method gating is detected.

### Schema/model extractor

Generate `API Schema` concepts for Pydantic `BaseModel` classes:

- class name;
- source path/line;
- fields;
- types;
- defaults when safe;
- descriptions if present;
- validators if statically detectable;
- model inheritance;
- linked endpoint consumers.

### Infrastructure extractor

Parse:

```text
network-operations/ansible/inventory/hosts.yml
network-operations/ansible/inventory/group_vars/all.yml
network-operations/ansible/inventory/host_vars/*.yml
network-operations/configs/*.service
network-operations/configs/*.zone
network-operations/configs/mon/**
network-operations/.github/workflows/*.yml
```

Generate richer concepts for:

- hosts;
- routers;
- subnets/prefixes;
- DNS zones;
- app deployment pins;
- systemd services;
- firewall rules;
- monitoring checks;
- CI/CD workflows;
- source repo → deployed host relationships.

Host pages must include:

- host role;
- addresses;
- OS/group membership;
- inbound firewall rules;
- monitored services;
- logging role;
- deployed app/version pin where present;
- related docs/runbooks.

### Workflow extractor

For each GitHub Actions workflow:

- triggers;
- jobs;
- runner labels;
- permissions;
- environments;
- secrets referenced by name only;
- deploy/promotion behavior;
- required check names where inferable.

## Quality and Coverage Reports

Generate:

```text
reports/coverage.md
reports/coverage.json
reports/quality.json
reports/shallow-concepts.md
```

Coverage report must include:

- source repos indexed;
- source files included/skipped;
- concepts by type;
- concepts by authority/truth owner;
- shallow concepts;
- concepts missing inbound links;
- concepts missing outbound links;
- endpoint/schema coverage;
- infrastructure host coverage;
- observed telemetry source status;
- LLM enrichment run status.

Critical CI failures:

- missing org concept;
- missing any top-level service/project concept;
- top-level service/project body under 800 chars;
- generated concept missing source refs;
- LLM-enriched concept missing enrichment metadata;
- LLM-enriched concept missing citations;
- observed concept marked canonical;
- endpoint concept missing method/path/source;
- host concept missing source and role/address;
- exports stale;
- secret scan finding.

Warnings only:

- source-doc concept shallow;
- no inbound links;
- no related services;
- no open issue links;
- low quality score;
- telemetry source unavailable.

## SQLite/Export Updates

Update `schema/sqlite-schema.sql` and exporter to include:

- `review_status`
- `quality_score`
- `observed_at`
- `expires_at`
- `enrichment_json`

Add tables:

```sql
quality_findings(concept_id, severity, code, message)
observations(concept_id, observed_at, expires_at, source, status, payload_json)
claims(concept_id, claim_text, source_ref_index, confidence)
enrichment_runs(run_id, provider, model, prompt_version, input_hash, output_hash, created_at)
```

Update JSONL exports:

```text
exports/concepts.jsonl
exports/edges.jsonl
exports/sources.jsonl
exports/quality.jsonl
exports/observations.jsonl
exports/enrichment-runs.jsonl
```

## Workflows

### Update `validate.yml`

Run:

```bash
uv run ruff check src tests
uv run mypy --strict src
uv run pytest
uv run hyrule-knowledge validate okf
uv run hyrule-knowledge quality --check
uv run hyrule-knowledge export --check
uv run hyrule-knowledge scan-secrets okf exports reports
```

### Add `enrich.yml`

Manual dispatch only.

Inputs:

```yaml
target: all | org | services | architecture | api | infrastructure
max_concepts: integer
model: string
dry_run: boolean
```

Behavior:

1. checkout;
2. install dependencies;
3. run `ingest`;
4. run `enrich`;
5. run `quality --write`;
6. run `export`;
7. validate/scan;
8. open PR with generated diffs.

Requires secret:

```text
OPENROUTER_API_KEY
```

Do not run on schedule.

### Telemetry

Do not add scheduled telemetry workflow in this tranche.

Add local/manual command and docs only:

```bash
uv run hyrule-knowledge observe --profile safe-health
```

## Testing Plan

Add unit tests for:

- FastAPI route AST extraction;
- Pydantic schema extraction;
- Go handler extraction;
- Ansible inventory and host-vars extraction;
- DNS zone parsing;
- GitHub Actions workflow parsing;
- quality scoring and critical/warn classification;
- LLM JSON validation with fixture output;
- LLM rejection when citations are missing;
- observation concept generation from mocked Prometheus/Icinga/MCP responses;
- export schema compatibility;
- secret scanning against LLM and observed outputs.

No test may call OpenRouter or live telemetry.

## Acceptance Criteria

The tranche is complete when:

- `okf/generated/org/as215932.md` exists and is useful.
- Every top-level service/project page has rich sections and citations.
- At least the listed curated seed pages exist with `review_status: proposed`.
- Endpoint pages include function/model/status/dependency context where statically available.
- Pydantic model concepts exist and are linked to endpoint concepts.
- Host pages include role, address, firewall, monitoring, logs, and deployed version pins where available.
- DNS zone concepts include parsed record summaries.
- Workflow concepts include triggers/jobs/permissions/runner/environment summaries.
- `reports/coverage.md` and `reports/quality.json` exist.
- `quality --check` fails only critical issues and reports warnings.
- `observe --profile safe-health` can produce observed evidence concepts without secrets.
- `enrich.yml` is manual-dispatch only.
- `validate.yml` passes.
- `exports/*.jsonl` and `exports/knowledge.sqlite` are regenerated and current.
- Secret scan passes.

## Non-Goals for This Tranche

- No automatic nightly LLM enrichment.
- No scheduled telemetry ingestion yet.
- No log ingestion.
- No packet captures.
- No mutating MCP tools.
- No RAG/vector database.
- No hosted API.
- No MCP server for the knowledge repo yet.

<!-- pi-plan-progress:start -->
## Progress

Status legend: `[x]` done, `[-]` skipped, `[>]` deferred, `[!]` blocked, `[ ]` pending.

- [x] 1. Add enrichment, quality, and observation data models. `[DONE:1]`
- [x] 2. Refactor the generator into typed extractors. `[DONE:2]`
- [x] 3. Implement richer deterministic extraction. `[DONE:3]`
- [x] 4. Implement LLM-first source-cited enrichment. `[DONE:4]`
- [x] 5. Seed useful curated OKF pages. `[DONE:5]`
- [x] 6. Add safe live telemetry observation ingestion. `[DONE:6]`
- [x] 7. Add coverage reports and usefulness quality gates. `[DONE:7]`
- [x] 8. Update exports and SQLite schema. `[DONE:8]`
- [x] 9. Add workflows, tests, and documentation. `[DONE:9]`
- [ ] 10. Regenerate the bundle and open one focused PR. _(bundle regenerated; PR pending)_

<!-- pi-plan-progress:end -->
