"""Command-line interface for AS215932 knowledge tooling."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import UTC, datetime
from pathlib import Path

from .agent_core_trace import emit_context_pack, emit_enrich_cost
from .authority import AuthorityTier
from .builder import build_all, source_ref
from .config import SourceConfig, load_config
from .context_pack import (
    build_context_pack,
    deployment_pins,
    diff_intended_observed,
    endpoint_schema,
    find_conflicts,
    find_stale,
    intended_state,
    observed_state,
)
from .enrich import enrich_target
from .evals import eval_check, load_eval_cases, write_eval_reports
from .exporter import exports_match, write_exports
from .github_source import collect_snapshot
from .knowledge_loop import KnowledgeLoopConfig
from .knowledge_loop import run_once as run_knowledge_loop_once
from .learning_ledger import (
    LearningLedgerError,
    import_learning_events,
    ledger_check,
    write_learning_ledger_reports,
)
from .models import Concept, RepoSnapshot, SourceRef
from .observe import collect_safe_health
from .okf_writer import reset_generated, write_concepts, write_indexes
from .policy import policy_decision_for
from .promotion import (
    LearningPromotionError,
    build_review_packet,
    lifecycle_check,
    promote_learning_event,
    promote_learning_event_for_pr,
    write_learning_lifecycle_reports,
)
from .quality import quality_check, write_quality_reports
from .retrieval import KnowledgeRetriever
from .store import KnowledgeStore, KnowledgeStoreError
from .validator import scan_paths, validate_okf


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def run_id() -> str:
    return os.environ.get("GITHUB_RUN_ID") or f"local-{datetime.now(UTC).strftime('%Y%m%d%H%M%S')}"


def print_json(data: object) -> None:
    print(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False))


def open_store(config_path: str) -> KnowledgeStore:
    config = load_config(Path(config_path))
    return KnowledgeStore(config.exports_dir / "knowledge.sqlite")


def ensure_curated_indexes() -> None:
    curated = Path("okf/curated")
    sections = {
        "architecture": "Cross-repo architecture notes.",
        "decisions": "ADRs and rationale.",
        "lessons": "Durable operational and engineering lessons.",
        "policies": "OKF-owned policy and escalation rules.",
        "postmortems": "Incident retrospectives.",
        "strategy": "Business and long-range context.",
        "summaries": "Human-reviewed learning and trace summaries.",
    }
    root_lines = ["# Curated knowledge", ""]
    for name, description in sections.items():
        path = curated / name
        path.mkdir(parents=True, exist_ok=True)
        index = path / "index.md"
        title = name.replace("-", " ").title()
        entries = sorted(p for p in path.glob("*.md") if p.name != "index.md")
        root_lines.append(f"* [{title}]({name}/) - {description}")
        lines = [f"# {title}\n"]
        if entries:
            for entry in entries:
                lines.append(f"* [{entry.stem.replace('-', ' ').title()}]({entry.name}) - Curated seed/proposed knowledge.")
        else:
            lines.append(f"* _No curated entries yet._ - {description}")
        lines.append("")
        index.write_text("\n".join(lines), encoding="utf-8")
    root_lines.append("")
    (curated / "index.md").write_text("\n".join(root_lines), encoding="utf-8")


def _snapshot_by_name(snapshots: list[tuple[SourceConfig, RepoSnapshot]], name: str) -> RepoSnapshot | None:
    for _, snapshot in snapshots:
        if snapshot.name == name:
            return snapshot
    return None


def _refs(snapshots: list[tuple[SourceConfig, RepoSnapshot]], items: list[tuple[str, str]]) -> list[SourceRef]:
    refs: list[SourceRef] = []
    for repo_name, path in items:
        snapshot = _snapshot_by_name(snapshots, repo_name)
        if snapshot and (snapshot.path / path).exists():
            refs.append(source_ref(snapshot, path))
    return refs


def curated_seed_concepts(snapshots: list[tuple[SourceConfig, RepoSnapshot]], verified_at: str) -> list[Concept]:
    seeds = [
        (
            "curated/architecture/as215932-system-map",
            "Architecture",
            "AS215932 System Map",
            "Cross-repo map of AS215932 infrastructure, services, and automation loops.",
            [("network-operations", "README.md"), (".github", "profile/README.md"), ("network-operations", "docs/network-flows.md")],
            """# System map

AS215932 combines an IPv6-first network operations repository, production VMs, Hyrule Cloud product services, NOC diagnostics, and an engineering automation loop.

# Core relationships

- `network-operations` is the production deployment record and intended-state source for infrastructure, app pins, DNS, monitoring, and firewall policy.
- `hyrule-cloud` provides the paid x402 VPS/API product surface.
- `hyrule-web` is the branded web/order/dashboard frontend.
- `hyrule-network-proxy` is an internal paid-request sidecar used by Hyrule Cloud.
- `noc-agent` consumes monitoring events and Hyrule MCP diagnostics for incident investigation.
- `hyrule-mcp` exposes bounded diagnostic tools for routing, host, monitoring, DNS, firewall, and packet-path inspection.
- `engineering-loop` creates draft PRs from approved work and hands production context back to operators.

# Review status

This curated page is a proposed cross-repo synthesis. Verify against cited source repos before treating it as durable policy.
""",
        ),
        (
            "curated/architecture/production-deployment-flow",
            "Architecture",
            "Production Deployment Flow",
            "How app repositories promote reviewed commits into production through network-operations.",
            [("network-operations", "README.md"), ("network-operations", "docs/ci/deploy-runbook.md"), ("network-operations", "AGENTS.md")],
            """# Production deployment flow

App repositories do not directly define production state. They produce reviewed commits and request promotion. `network-operations` pins exact app SHAs in Ansible inventory, renders intended state, and runs production applies behind human approval.

# Normal path

1. App CI succeeds on the app repository's `main` branch.
2. The app requests promotion or an operator runs `promote-apps`.
3. A promotion PR updates exact 40-character SHAs in `network-operations` host vars.
4. Reviewers merge the promotion PR after render/CI checks.
5. `app-promotion-deploy` calls `apply.yml` for affected playbooks.
6. A human approves the GitHub `production` environment gate.
7. Operators review Icinga pre/post snapshot diffs.

# Safety lessons

The deployment record lives in one repo; app repos remain implementation sources. This avoids accidental production deploys on application merge.
""",
        ),
        (
            "curated/architecture/noc-mcp-diagnostics-loop",
            "Architecture",
            "NOC and MCP Diagnostics Loop",
            "How alerts flow through NOC Agent and Hyrule MCP diagnostic tools.",
            [("network-operations", "docs/autonomous-noc.md"), ("noc-agent", "README.md"), ("hyrule-mcp", "README.md")],
            """# NOC/MCP diagnostics loop

`noc-agent` receives monitoring events, normalizes and investigates incidents, and uses `hyrule-mcp` for bounded live diagnostics. The loop is diagnostic-first and human-gated.

# Flow

1. Alertmanager or Icinga posts to `noc-agent`.
2. The graph deduplicates symptoms and recalls recent incident memory.
3. Specialist reasoning is checked against evidence and golden-state context.
4. Hyrule MCP provides read-biased tools for Prometheus, Icinga, FRR, firewall, DNS, WireGuard, host status, and packet-path checks.
5. A proposal is recorded for operator review through Discord or local `nocctl`.

# Boundary

The NOC loop responds to production symptoms. The engineering loop writes code/config PRs. Do not merge those responsibilities.
""",
        ),
        (
            "curated/architecture/hyrule-cloud-product-stack",
            "Architecture",
            "Hyrule Cloud Product Stack",
            "Product architecture for Hyrule Cloud, Hyrule Web, and the network proxy sidecar.",
            [("hyrule-cloud", "README.md"), ("hyrule-web", "pyproject.toml"), ("hyrule-network-proxy", "README.md"), ("network-operations", "docs/x402-network-proxy-sidecar-plan.md")],
            """# Hyrule Cloud product stack

Hyrule Cloud is an agentic VPS hosting/API product using x402 payments. Hyrule Web provides the web/order/dashboard frontend. Hyrule Network Proxy executes internal already-authorized paid network requests.

# Product responsibilities

- Hyrule Cloud: payment verification, VM lifecycle, DNS, domain registration, pricing, database state, and public API contract.
- Hyrule Web: customer-facing site, order flow, dashboard, and committed frontend bundle.
- Hyrule Network Proxy: internal egress execution for direct/Tor/I2P/Yggdrasil modes, never public and never payment-aware.

# Deployment ownership

Production versions are pinned in `network-operations` host vars and promoted through the deployment flow.
""",
        ),
        (
            "curated/architecture/engineering-loop-vs-noc-loop",
            "Architecture",
            "Engineering Loop vs NOC Loop",
            "Boundary between agentic development automation and production incident investigation.",
            [("engineering-loop", "docs/agentic-development-loop.md"), ("network-operations", "docs/agentic-development-loop.md"), ("network-operations", "docs/autonomous-noc.md")],
            """# Boundary

The Hyrule Engineering Loop and Hyrule NOC Loop are separate systems.

# Engineering Loop

Designs changes, coordinates coding agents, validates worktrees, prepares draft PRs, and stops for human sign-off.

# NOC Loop

Responds to alerts, investigates production, detects drift, proposes remediation, verifies recovery, and records human decisions.

# Allowed connection

Engineering Loop can provide deploy notes, expected impact, and rollback plans to NOC context. NOC observations can create issue feedback for Engineering Loop.

# Forbidden connection

NOC Agent must not become a normal feature-planning or PR-generation system.
""",
        ),
        (
            "curated/policies/source-of-truth-and-canonicality",
            "Policy",
            "Source of Truth and Canonicality Policy",
            "Typed source-first hybrid truth model for AS215932 knowledge.",
            [("network-operations", "AGENTS.md"), ("network-operations", "README.md"), ("hyrule-cloud", "AGENTS.md")],
            """# Policy

Source repositories are canonical for implemented behavior, executable state, APIs, configuration, schemas, tests, CI/CD, deployment workflows, repo-local docs, and intended infrastructure state committed as code.

OKF generated concepts are derivative: they summarize and cross-link source material but must cite repo paths and commits.

OKF curated concepts can be canonical only for cross-repo institutional knowledge that does not naturally belong in one repo. New curated pages start as `review_status: proposed` and `authority: advisory` until reviewed.

Observed telemetry is evidence only. It can prove drift or support investigation but does not silently redefine intended state.
""",
        ),
        (
            "curated/policies/domain-policy",
            "Policy",
            "Domain Policy",
            "Curated statement of AS215932 domain identity boundaries.",
            [("network-operations", "AGENTS.md"), ("hyrule-cloud", "AGENTS.md"), ("hyrule-network-proxy", "AGENTS.md")],
            """# Domain policy

- `hyrule.host` is customer-facing Hyrule Cloud/product identity.
- `servify.network` is infrastructure identity for nameservers, underlay, management, providers, internal UIs, and partner-facing infrastructure hostnames.
- `as215932.net` is AS215932 overlay/routing identity only.

Do not blindly replace `servify.network`; many infrastructure references intentionally live there.
""",
        ),
        (
            "curated/lessons/deployment-safety-lessons",
            "Lesson",
            "Deployment Safety Lessons",
            "Durable safety lessons extracted from deployment and infrastructure guidance.",
            [("network-operations", "CLAUDE.md"), ("network-operations", "docs/ci/deploy-runbook.md"), ("network-operations", "AGENTS.md")],
            """# Lessons

1. App merges are not production deploys; production is represented by pinned SHAs in `network-operations`.
2. Real deployments need Icinga snapshots before and after applies so operators can separate already-broken from newly-broken state.
3. Firewall changes must update the network-flow inventory first, then host vars, then rendered artifacts.
4. Branch hygiene matters: start from fresh `main` branches for unrelated work to avoid accidental PR contamination.
5. Generated knowledge must cite source repos, or it is advisory at best.
""",
        ),
        (
            "curated/strategy/hyrule-cloud-business-context",
            "Strategy",
            "Hyrule Cloud Business Context",
            "Business and pricing context for Hyrule Cloud hosting economics.",
            [("hyrule-business", "hosting-cost-analysis.md"), ("hyrule-cloud", "README.md")],
            """# Business context

Hyrule Cloud targets AI agents and builders that need deployable VPS capacity with x402 payment flows. The business notes model OVH/XCP-ng hosting economics, IPv6-only margins, optional IPv4 lease costs, and small/medium/large VM pricing.

# Strategy signals

- IPv6-only capacity materially improves early economics.
- A leased IPv4 /24 is a fixed cost that becomes efficient only at higher density.
- RISE-S class servers are modeled as cost-efficient launch capacity.
- Product simplicity matters: bare VMs reduce PaaS support burden while preserving agent autonomy.

# Review status

This page is proposed strategy synthesis. Treat the business repo as canonical for numeric assumptions.
""",
        ),
    ]
    concepts: list[Concept] = []
    for concept_id, concept_type, title, description, ref_items, body in seeds:
        refs = _refs(snapshots, ref_items)
        concepts.append(
            Concept(
                concept_id=concept_id,
                concept_type=concept_type,
                title=title,
                description=description,
                tags=["curated", "proposed", concept_type.lower()],
                truth_owner="okf",
                authority="advisory",
                source_refs=refs,
                last_verified_at=verified_at,
                confidence="medium",
                dispute_policy="adjudicate",
                review_status="proposed",
                body=body + "\n# Citations\n\n" + "".join(
                    f"[{idx}] [{ref.repo}:{ref.path}]({ref.url})\n" for idx, ref in enumerate(refs, start=1)
                ),
            )
        )
    return concepts


def cmd_ingest(args: argparse.Namespace) -> int:
    config = load_config(Path(args.config))
    verified_at = utc_now()
    snapshots: list[tuple[SourceConfig, RepoSnapshot]] = []
    for source in config.sources:
        print(f"collecting {source.repo}", file=sys.stderr)
        snapshot = collect_snapshot(config, source)
        snapshots.append((source, snapshot))
    result = build_all(config, snapshots, verified_at)
    result.concepts.extend(curated_seed_concepts(snapshots, verified_at))
    ids = [concept.concept_id for concept in result.concepts]
    duplicates = sorted({concept_id for concept_id in ids if ids.count(concept_id) > 1})
    if duplicates:
        for duplicate in duplicates:
            print(f"duplicate concept id: {duplicate}", file=sys.stderr)
        return 1
    reset_generated(config.bundle_root)
    write_concepts(config.bundle_root, result.concepts)
    write_indexes(config.bundle_root, result.concepts)
    ensure_curated_indexes()
    write_exports(config.bundle_root, config.exports_dir, edges=result.edges, source_shas=result.source_shas, run_id=run_id())
    write_quality_reports(config.bundle_root, Path("reports"), config.exports_dir)
    write_exports(config.bundle_root, config.exports_dir, edges=result.edges, source_shas=result.source_shas, run_id=run_id())
    print(f"wrote {len(result.concepts)} concepts and {len(result.edges)} edges")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    root = Path(args.path)
    errors = validate_okf(root)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        print(f"validation failed: {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("OKF validation passed")
    return 0


def cmd_quality(args: argparse.Namespace) -> int:
    config = load_config(Path(args.config))
    if args.write:
        write_quality_reports(config.bundle_root, Path("reports"), config.exports_dir)
        print("quality reports written")
        return 0
    critical = quality_check(config.bundle_root, Path("reports"), config.exports_dir)
    for finding in critical:
        print(f"{finding.concept_id}: {finding.code}: {finding.message}", file=sys.stderr)
    if critical:
        print(f"quality check failed: {len(critical)} critical finding(s)", file=sys.stderr)
        return 1
    print("quality check passed")
    return 0


def cmd_enrich(args: argparse.Namespace) -> int:
    config = load_config(Path(args.config))
    try:
        path = enrich_target(
            config.bundle_root,
            args.target,
            provider=args.provider,
            model=args.model,
            max_input_chars=args.max_input_chars,
            temperature=args.temperature,
            dry_run=args.dry_run,
        )
    except Exception as exc:
        print(f"enrichment failed: {exc}", file=sys.stderr)
        return 1
    print(f"wrote enrichment concept: {path}")
    if not args.dry_run:
        emit_enrich_cost(args.provider, args.model, args.target)
    return 0


def cmd_observe(args: argparse.Namespace) -> int:
    config = load_config(Path(args.config))
    path = collect_safe_health(config.bundle_root, args.profile)
    write_quality_reports(config.bundle_root, Path("reports"), config.exports_dir)
    write_exports(config.bundle_root, config.exports_dir, run_id=run_id())
    print(f"wrote observation concept: {path}")
    return 0


def cmd_export(args: argparse.Namespace) -> int:
    config = load_config(Path(args.config))
    if args.check:
        if exports_match(config.bundle_root, config.exports_dir):
            print("exports are up to date")
            return 0
        print("exports are stale; run `uv run hyrule-knowledge export`", file=sys.stderr)
        return 1
    write_exports(config.bundle_root, config.exports_dir, run_id=run_id())
    print("exports written")
    return 0


def cmd_scan_secrets(args: argparse.Namespace) -> int:
    config = load_config(Path(args.config))
    findings = scan_paths([Path(path) for path in args.paths], config)
    for finding in findings:
        print(finding, file=sys.stderr)
    if findings:
        print(f"secret scan failed: {len(findings)} finding(s)", file=sys.stderr)
        return 1
    print("secret scan passed")
    return 0


def cmd_resolve(args: argparse.Namespace) -> int:
    try:
        with open_store(args.config) as store:
            result = KnowledgeRetriever(store).resolve(args.reference, authority_min=AuthorityTier(args.authority_min))
    except KnowledgeStoreError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print_json(result)
    return 0


def cmd_query(args: argparse.Namespace) -> int:
    try:
        with open_store(args.config) as store:
            candidates = KnowledgeRetriever(store).query(
                args.query,
                authority_min=AuthorityTier(args.authority_min),
                freshness=args.freshness,
                limit=args.limit,
                concept_type=args.type,
                repo=args.repo,
            )
    except KnowledgeStoreError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    rows = [candidate.as_json() for candidate in candidates]
    if args.json:
        print_json({"query": args.query, "candidates": rows})
    else:
        for row in rows:
            print(f"{row['concept_id']}\t{row['authority_tier']}\t{row['reason']}\t{row['title']}")
    return 0


def cmd_claims(args: argparse.Namespace) -> int:
    try:
        with open_store(args.config) as store:
            rows = store.claims(
                subject=args.subject,
                predicate=args.predicate,
                object_value=args.object,
                concept_id=args.concept_id,
                authority_min=AuthorityTier(args.authority_min),
                freshness=args.freshness,
                limit=args.limit,
            )
    except KnowledgeStoreError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print_json({"claims": rows})
    return 0


def cmd_neighborhood(args: argparse.Namespace) -> int:
    try:
        edge_types = set(args.edge_type or []) or None
        with open_store(args.config) as store:
            rows = KnowledgeRetriever(store).neighborhood(
                args.concept_id,
                depth=args.depth,
                edge_types=edge_types,
                authority_min=AuthorityTier(args.authority_min),
            )
    except KnowledgeStoreError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print_json({"concept_id": args.concept_id, "neighbors": rows})
    return 0


def cmd_context_pack(args: argparse.Namespace) -> int:
    task = Path(args.task_file).read_text(encoding="utf-8") if args.task_file else args.task
    if not task:
        print("context-pack requires --task or --task-file", file=sys.stderr)
        return 1
    try:
        with open_store(args.config) as store:
            pack = build_context_pack(
                task=task,
                role=args.role,
                store=store,
                risk_level=args.risk_level,
                token_budget=args.budget_tokens,
                authority_min=AuthorityTier(args.authority_min),
            )
    except KnowledgeStoreError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    data = pack.as_json()
    emit_context_pack(data)
    if args.write:
        out = Path(args.write)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(data, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        reports = Path("reports/context-packs.jsonl")
        reports.parent.mkdir(parents=True, exist_ok=True)
        reports.write_text(json.dumps(data, sort_keys=True) + "\n", encoding="utf-8")
    print_json(data)
    return 0


def cmd_intended_state(args: argparse.Namespace) -> int:
    try:
        with open_store(args.config) as store:
            result = intended_state(store, args.scope)
    except KnowledgeStoreError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print_json(result)
    return 0


def cmd_observed_state(args: argparse.Namespace) -> int:
    try:
        with open_store(args.config) as store:
            result = observed_state(store, args.scope, window_hours=args.window_hours)
    except KnowledgeStoreError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print_json(result)
    return 0


def cmd_diff_intended_observed(args: argparse.Namespace) -> int:
    try:
        with open_store(args.config) as store:
            result = diff_intended_observed(store, args.scope)
    except KnowledgeStoreError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print_json(result)
    return 0


def cmd_deployment_pins(args: argparse.Namespace) -> int:
    try:
        with open_store(args.config) as store:
            result = deployment_pins(store, args.service)
    except KnowledgeStoreError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print_json(result)
    return 0


def cmd_endpoint_schema(args: argparse.Namespace) -> int:
    try:
        with open_store(args.config) as store:
            result = endpoint_schema(store, args.method, args.route)
    except KnowledgeStoreError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print_json(result)
    return 0


def cmd_policy_decision(args: argparse.Namespace) -> int:
    decision = policy_decision_for(
        actor=args.actor,
        action=args.action,
        target=args.target,
        environment=args.environment,
        risk_level=args.risk_level,
        tool_tier=args.tool_tier,
        data_classes=args.data_class or [],
    )
    reports = Path("reports/policy-decisions.jsonl")
    reports.parent.mkdir(parents=True, exist_ok=True)
    reports.write_text(json.dumps(decision.as_json(), sort_keys=True) + "\n", encoding="utf-8")
    print_json(decision.as_json())
    return 0


def cmd_find_conflicts(args: argparse.Namespace) -> int:
    try:
        with open_store(args.config) as store:
            rows = find_conflicts(store, scope=args.scope)
    except KnowledgeStoreError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print_json({"conflicts": rows})
    return 0


def cmd_find_stale(args: argparse.Namespace) -> int:
    try:
        with open_store(args.config) as store:
            rows = find_stale(store, scope=args.scope)
    except KnowledgeStoreError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print_json({"stale": rows})
    return 0


def cmd_ledger(args: argparse.Namespace) -> int:
    ledger_args = list(args.ledger_args or [])
    command = ledger_args[0] if ledger_args and ledger_args[0] in {"import", "promote-pr", "lifecycle"} else None
    positional = ledger_args[1:] if command else ledger_args
    paths = [Path(path) for path in positional] if positional else None
    if command == "import":
        if not positional:
            print("ledger import requires at least one file, directory, or glob", file=sys.stderr)
            return 1
        try:
            results = import_learning_events([Path(path) for path in positional], replace=args.replace)
            write_learning_ledger_reports()
            write_learning_lifecycle_reports()
            config = load_config(Path(args.config))
            write_exports(config.bundle_root, config.exports_dir, run_id=run_id())
            print_json({"results": results})
        except (LearningLedgerError, LearningPromotionError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0
    if command == "lifecycle":
        if args.write:
            report = write_learning_lifecycle_reports(paths=paths)
            print_json(report)
            return 1 if report["summary"].get("critical_count", 0) else 0
        failures = lifecycle_check(paths=paths)
        for failure in failures:
            print(failure, file=sys.stderr)
        if failures:
            print(f"learning lifecycle check failed: {len(failures)} critical finding(s)", file=sys.stderr)
            return 1
        print("learning lifecycle check passed")
        return 0
    if command == "promote-pr":
        if not positional:
            print("ledger promote-pr requires an event id or subject", file=sys.stderr)
            return 1
        try:
            result = promote_learning_event_for_pr(
                positional[0],
                reviewer=args.reviewer or "",
                promotion_kind=args.promotion_kind,
                decision=args.decision,
                rationale=args.rationale,
                paths=None,
                dry_run=args.dry_run,
            )
            if result.wrote:
                ensure_curated_indexes()
                write_learning_lifecycle_reports()
                config = load_config(Path(args.config))
                write_exports(config.bundle_root, config.exports_dir, run_id=run_id())
            print_json(result.as_json())
        except (LearningLedgerError, LearningPromotionError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0
    if args.list:
        events, findings = write_learning_ledger_reports(paths)
        print_json({"events": [{"id": event["id"], "event_type": event["event_type"], "producer": event["producer"], "subject": event["subject"], "status": event["status"]} for event in events], "findings": findings})
        return 1 if findings else 0
    if args.review:
        try:
            print_json(build_review_packet(args.review, paths=paths, promotion_kind=args.promotion_kind))
        except (LearningLedgerError, LearningPromotionError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0
    if args.promote:
        try:
            result = promote_learning_event(
                args.promote,
                reviewer=args.reviewer or "",
                promotion_kind=args.promotion_kind,
                decision=args.decision,
                rationale=args.rationale,
                paths=paths,
                dry_run=args.dry_run,
            )
            if result.wrote:
                ensure_curated_indexes()
                write_learning_lifecycle_reports()
                config = load_config(Path(args.config))
                write_exports(config.bundle_root, config.exports_dir, run_id=run_id())
            print_json(result.as_json())
        except (LearningLedgerError, LearningPromotionError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0
    if args.write:
        _, findings = write_learning_ledger_reports(paths)
        write_learning_lifecycle_reports(paths=paths)
        for finding in findings:
            print(f"{finding['event_id']}: {finding['message']}", file=sys.stderr)
        if findings:
            print(f"learning ledger report failed: {len(findings)} finding(s)", file=sys.stderr)
            return 1
        print("learning ledger reports written")
        return 0
    failures = ledger_check(paths)
    for failure in failures:
        print(failure, file=sys.stderr)
    if failures:
        print(f"learning ledger check failed: {len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("learning ledger check passed")
    return 0


def cmd_eval(args: argparse.Namespace) -> int:
    try:
        with open_store(args.config) as store:
            if args.write:
                results = write_eval_reports(store=store, suite=args.suite)
                config = load_config(Path(args.config))
                cases = [case.as_json() for case in load_eval_cases()]
                Path("reports/eval-cases.jsonl").write_text("".join(json.dumps(case, sort_keys=True) + "\n" for case in cases), encoding="utf-8")
                write_exports(config.bundle_root, config.exports_dir, run_id=run_id())
                print(f"eval reports written: {sum(1 for result in results if result.passed)}/{len(results)} passed")
                return 0
    except KnowledgeStoreError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    failures = eval_check()
    for failure in failures:
        print(failure, file=sys.stderr)
    if failures:
        print(f"eval check failed: {len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("eval check passed")
    return 0


def _truthy(value: str | None) -> bool:
    return value is not None and value.strip().lower() in {"1", "true", "yes", "on"}


def _env_paths(name: str) -> list[Path]:
    value = os.environ.get(name, "").strip()
    if not value:
        return []
    return [Path(item) for item in value.split(os.pathsep) if item]


def _env_csv(name: str) -> list[str]:
    value = os.environ.get(name, "").strip()
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def _env_int(name: str, default: int) -> int:
    value = os.environ.get(name, "").strip()
    if not value:
        return default
    try:
        return int(value)
    except ValueError:
        return default


def _env_str(name: str, default: str) -> str:
    value = os.environ.get(name, "").strip()
    return value or default


def cmd_loop(args: argparse.Namespace) -> int:
    if not args.once:
        print("knowledge loop currently requires --once", file=sys.stderr)
        return 1
    config = KnowledgeLoopConfig(
        repo_path=Path(args.repo_path),
        config_path=Path(args.config),
        state_dir=Path((args.state_dir or "").strip() or _env_str("HYRULE_KNOWLEDGE_LOOP_STATE_DIR", ".cache/hyrule-knowledge/loop-state")),
        branch_prefix=args.branch_prefix,
        base_branch=args.base_branch,
        create_pr=bool(args.create_pr or _truthy(os.environ.get("HYRULE_KNOWLEDGE_LOOP_CREATE_PR"))),
        dry_run=bool(args.dry_run),
        git_user_name=args.git_user_name,
        git_user_email=args.git_user_email,
        max_cycles_per_day=args.max_cycles_per_day,
        max_prs_per_day=args.max_prs_per_day,
        max_openrouter_calls_per_day=args.max_openrouter_calls_per_day,
        max_learning_events_per_day=args.max_learning_events_per_day,
        enrich_targets=tuple(args.enrich_target or _env_csv("HYRULE_KNOWLEDGE_LOOP_ENRICH_TARGETS")),
        enrich_live=bool(args.enrich_live or _truthy(os.environ.get("HYRULE_KNOWLEDGE_LOOP_ENRICH_LIVE"))),
        dry_run_enrich_targets=tuple(args.dry_run_enrich_target or _env_csv("HYRULE_KNOWLEDGE_LOOP_DRY_RUN_ENRICH_TARGETS")),
        learning_event_paths=tuple([*(Path(path) for path in (args.learning_event or [])), *_env_paths("HYRULE_KNOWLEDGE_LOOP_LEARNING_EVENTS")]),
        replace_learning_events=bool(args.replace_learning_events),
        run_validation=not args.skip_validation,
    )
    report = run_knowledge_loop_once(config)
    print_json(report.as_json())
    return 0 if report.outcome in {"published", "changes_detected", "idle", "locked"} else 1


def cmd_mcp(args: argparse.Namespace) -> int:
    from .mcp_server import main as mcp_main

    db_path = args.db or str(load_config(Path(args.config)).exports_dir / "knowledge.sqlite")
    mcp_args = [
        "--transport",
        args.transport,
        "--db",
        db_path,
        "--host",
        args.host,
        "--port",
        str(args.port),
        "--log-level",
        args.log_level,
        "--mount-path",
        args.mount_path,
        "--sse-path",
        args.sse_path,
        "--message-path",
        args.message_path,
        "--mcp-path",
        args.mcp_path,
    ]
    if args.stateless_http:
        mcp_args.append("--stateless-http")
    return mcp_main(mcp_args)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="hyrule-knowledge")
    parser.add_argument("--config", default="knowledge.config.yml")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest = subparsers.add_parser("ingest")
    ingest.set_defaults(func=cmd_ingest)

    validate = subparsers.add_parser("validate")
    validate.add_argument("path", nargs="?", default="okf")
    validate.set_defaults(func=cmd_validate)

    quality = subparsers.add_parser("quality")
    quality.add_argument("--write", action="store_true")
    quality.add_argument("--check", action="store_true")
    quality.set_defaults(func=cmd_quality)

    enrich = subparsers.add_parser("enrich")
    enrich.add_argument("--target", default="all")
    enrich.add_argument("--provider", default="openrouter")
    enrich.add_argument("--model", default="anthropic/claude-sonnet-4.6")
    enrich.add_argument("--max-input-chars", type=int, default=120_000)
    enrich.add_argument("--temperature", type=float, default=0.2)
    enrich.add_argument("--dry-run", action="store_true")
    enrich.set_defaults(func=cmd_enrich)

    observe = subparsers.add_parser("observe")
    observe.add_argument("--profile", default="safe-health")
    observe.set_defaults(func=cmd_observe)

    resolve = subparsers.add_parser("resolve")
    resolve.add_argument("reference")
    resolve.add_argument("--authority-min", default="A5", choices=["A0", "A1", "A2", "A3", "A4", "A5"])
    resolve.set_defaults(func=cmd_resolve)

    query = subparsers.add_parser("query")
    query.add_argument("query")
    query.add_argument("--authority-min", default="A5", choices=["A0", "A1", "A2", "A3", "A4", "A5"])
    query.add_argument("--freshness", default="current", choices=["current", "include_expired"])
    query.add_argument("--limit", type=int, default=10)
    query.add_argument("--type")
    query.add_argument("--repo")
    query.add_argument("--json", action="store_true")
    query.set_defaults(func=cmd_query)

    claims = subparsers.add_parser("claims")
    claims.add_argument("--subject")
    claims.add_argument("--predicate")
    claims.add_argument("--object")
    claims.add_argument("--concept-id")
    claims.add_argument("--authority-min", default="A5", choices=["A0", "A1", "A2", "A3", "A4", "A5"])
    claims.add_argument("--freshness", default="current", choices=["current", "include_expired"])
    claims.add_argument("--limit", type=int, default=50)
    claims.set_defaults(func=cmd_claims)

    neighborhood = subparsers.add_parser("neighborhood")
    neighborhood.add_argument("concept_id")
    neighborhood.add_argument("--depth", type=int, default=1)
    neighborhood.add_argument("--edge-type", action="append")
    neighborhood.add_argument("--authority-min", default="A5", choices=["A0", "A1", "A2", "A3", "A4", "A5"])
    neighborhood.set_defaults(func=cmd_neighborhood)

    context_pack = subparsers.add_parser("context-pack")
    context_pack.add_argument("--task")
    context_pack.add_argument("--task-file")
    context_pack.add_argument("--role", default="engineering_loop", choices=["engineering_loop", "noc_shadow", "general"])
    context_pack.add_argument("--risk-level", default="low", choices=["low", "medium", "high", "critical"])
    context_pack.add_argument("--budget-tokens", type=int, default=6000)
    context_pack.add_argument("--authority-min", default="A4", choices=["A0", "A1", "A2", "A3", "A4", "A5"])
    context_pack.add_argument("--write")
    context_pack.set_defaults(func=cmd_context_pack)

    intended = subparsers.add_parser("intended-state")
    intended.add_argument("scope")
    intended.set_defaults(func=cmd_intended_state)

    observed_state_parser = subparsers.add_parser("observed-state")
    observed_state_parser.add_argument("scope")
    observed_state_parser.add_argument("--window-hours", type=int, default=24)
    observed_state_parser.set_defaults(func=cmd_observed_state)

    diff = subparsers.add_parser("diff-intended-observed")
    diff.add_argument("scope")
    diff.set_defaults(func=cmd_diff_intended_observed)

    pins = subparsers.add_parser("deployment-pins")
    pins.add_argument("service")
    pins.set_defaults(func=cmd_deployment_pins)

    endpoint = subparsers.add_parser("endpoint-schema")
    endpoint.add_argument("method")
    endpoint.add_argument("route")
    endpoint.set_defaults(func=cmd_endpoint_schema)

    policy = subparsers.add_parser("policy-decision")
    policy.add_argument("--actor", default="engineering_loop")
    policy.add_argument("--action", required=True)
    policy.add_argument("--target")
    policy.add_argument("--environment", default="local")
    policy.add_argument("--risk-level", default="low")
    policy.add_argument("--tool-tier", type=int, default=0)
    policy.add_argument("--data-class", action="append")
    policy.set_defaults(func=cmd_policy_decision)

    conflicts = subparsers.add_parser("find-conflicts")
    conflicts.add_argument("--scope")
    conflicts.set_defaults(func=cmd_find_conflicts)

    stale = subparsers.add_parser("find-stale")
    stale.add_argument("--scope")
    stale.set_defaults(func=cmd_find_stale)

    eval_parser = subparsers.add_parser("eval")
    eval_parser.add_argument("--suite")
    eval_parser.add_argument("--write", action="store_true")
    eval_parser.add_argument("--check", action="store_true")
    eval_parser.set_defaults(func=cmd_eval)

    ledger = subparsers.add_parser("ledger")
    ledger.add_argument("ledger_args", nargs="*", help="optional paths, or subcommands: import, promote-pr, lifecycle")
    ledger.add_argument("--write", action="store_true", help="write ledger validation reports")
    ledger.add_argument("--check", action="store_true", help="validate ledger fixtures")
    ledger.add_argument("--list", action="store_true", help="list learning events with validation findings")
    ledger.add_argument("--review", help="print a human review packet for a learning event id/subject")
    ledger.add_argument("--promote", help="promote a learning event id/subject into curated OKF")
    ledger.add_argument("--reviewer", help="human reviewer identity for --promote")
    ledger.add_argument("--promotion-kind", choices=["lesson", "summary"], default="summary")
    ledger.add_argument("--decision", choices=["approved", "rejected"], default="approved")
    ledger.add_argument("--rationale", default="Reviewed and accepted for curated OKF promotion.")
    ledger.add_argument("--dry-run", action="store_true")
    ledger.add_argument("--replace", action="store_true", help="replace existing proposed event on ledger import")
    ledger.set_defaults(func=cmd_ledger)

    loop = subparsers.add_parser("loop")
    loop.add_argument("--once", action="store_true", help="run exactly one Knowledge Loop cycle")
    loop.add_argument("--repo-path", default=".")
    loop.add_argument("--state-dir")
    loop.add_argument("--branch-prefix", default="bot/knowledge-loop")
    loop.add_argument("--base-branch", default="main")
    loop.add_argument("--create-pr", action="store_true", help="push a branch and open a PR when changes are detected")
    loop.add_argument("--dry-run", action="store_true", help="run the cycle but do not commit/push/open PR")
    loop.add_argument("--skip-validation", action="store_true")
    loop.add_argument("--git-user-name", default=os.environ.get("HYRULE_KNOWLEDGE_LOOP_GIT_USER_NAME", "hyrule-knowledge-loop[bot]"))
    loop.add_argument("--git-user-email", default=os.environ.get("HYRULE_KNOWLEDGE_LOOP_GIT_USER_EMAIL", "knowledge-loop@as215932.net"))
    loop.add_argument("--max-cycles-per-day", type=int, default=_env_int("HYRULE_KNOWLEDGE_LOOP_MAX_CYCLES_PER_DAY", 1))
    loop.add_argument("--max-prs-per-day", type=int, default=_env_int("HYRULE_KNOWLEDGE_LOOP_MAX_PRS_PER_DAY", 1))
    loop.add_argument("--dry-run-enrich-target", action="append", help="phase-1 enrichment plumbing target; never calls a provider")
    loop.add_argument("--enrich-target", action="append", help="phase-2 enrichment target; dry-run unless --enrich-live is set")
    loop.add_argument("--enrich-live", action="store_true", help="allow live OpenRouter enrichment for --enrich-target")
    loop.add_argument("--max-openrouter-calls-per-day", type=int, default=_env_int("HYRULE_KNOWLEDGE_LOOP_MAX_OPENROUTER_CALLS_PER_DAY", 0))
    loop.add_argument("--learning-event", action="append", help="phase-2 learning-event file, directory, or glob to import")
    loop.add_argument("--replace-learning-events", action="store_true")
    loop.add_argument("--max-learning-events-per-day", type=int, default=_env_int("HYRULE_KNOWLEDGE_LOOP_MAX_LEARNING_EVENTS_PER_DAY", 100))
    loop.set_defaults(func=cmd_loop)

    mcp = subparsers.add_parser("mcp")
    mcp.add_argument("--transport", default="stdio", choices=["stdio", "sse", "streamable-http", "http"])
    mcp.add_argument("--db", help="SQLite export path (default: configured exports/knowledge.sqlite)")
    mcp.add_argument("--host", default="127.0.0.1")
    mcp.add_argument("--port", type=int, default=8767)
    mcp.add_argument("--log-level", default="INFO")
    mcp.add_argument("--mount-path", default="/")
    mcp.add_argument("--sse-path", default="/sse")
    mcp.add_argument("--message-path", default="/messages/")
    mcp.add_argument("--mcp-path", default="/mcp")
    mcp.add_argument("--stateless-http", action="store_true")
    mcp.set_defaults(func=cmd_mcp)

    export = subparsers.add_parser("export")
    export.add_argument("--check", action="store_true")
    export.set_defaults(func=cmd_export)

    scan = subparsers.add_parser("scan-secrets")
    scan.add_argument("paths", nargs="+", default=["okf", "exports", "reports"])
    scan.set_defaults(func=cmd_scan_secrets)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
