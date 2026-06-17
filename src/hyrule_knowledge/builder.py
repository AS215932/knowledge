"""Build useful OKF concepts from source repository snapshots."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .config import AppConfig, SourceConfig
from .extractors.ansible import HostInfo, extract_hosts, extract_network_constants
from .extractors.api import ApiEndpointInfo, PydanticModelInfo, extract_api, model_concept_id
from .extractors.dns import DnsZoneInfo, extract_zones
from .extractors.monitoring import monitoring_check_names, monitoring_config_paths
from .extractors.workflows import WorkflowInfo, extract_workflows
from .github_source import (
    collect_issues,
    collect_pull_requests,
    collect_releases,
    line_count,
    read_file,
    source_url,
)
from .models import Concept, Edge, RepoSnapshot, SourceRef
from .okf_writer import slugify

SENSITIVE_ASSIGNMENT_RE = re.compile(
    r"(?i)(api[_-]?key|auth[_-]?token|secret|password)\s*[:=]"
)


@dataclass
class BuildResult:
    concepts: list[Concept] = field(default_factory=list)
    edges: list[Edge] = field(default_factory=list)
    github_items: list[dict[str, Any]] = field(default_factory=list)
    source_shas: dict[str, str] = field(default_factory=dict)

    def add(self, concept: Concept) -> None:
        self.concepts.append(concept)

    def edge(self, source: str, target: str, edge_type: str, origin: str = "derived") -> None:
        self.edges.append(Edge(source=source, target=target, edge_type=edge_type, origin=origin))


@dataclass
class RepoBuildContext:
    source: SourceConfig
    snapshot: RepoSnapshot
    endpoints: list[ApiEndpointInfo] = field(default_factory=list)
    schemas: list[PydanticModelInfo] = field(default_factory=list)
    workflows: list[WorkflowInfo] = field(default_factory=list)
    hosts: list[HostInfo] = field(default_factory=list)
    zones: list[DnsZoneInfo] = field(default_factory=list)
    monitoring_paths: list[str] = field(default_factory=list)
    monitoring_checks: list[str] = field(default_factory=list)
    issues: list[dict[str, Any]] = field(default_factory=list)
    pull_requests: list[dict[str, Any]] = field(default_factory=list)
    releases: list[dict[str, Any]] = field(default_factory=list)

    @property
    def top_concept_id(self) -> str | None:
        if self.source.project_type == "Organization":
            return None
        concept_dir = "services" if self.source.project_type == "Service" else "projects"
        return f"generated/{concept_dir}/{self.source.concept_slug}"


def source_ref(snapshot: RepoSnapshot, rel_path: str | None = None, lines: str | None = None) -> SourceRef:
    url = snapshot.url
    if rel_path:
        url = source_url(snapshot.url, snapshot.commit, rel_path, lines)
    return SourceRef(repo=snapshot.repo, path=rel_path, commit=snapshot.commit, lines=lines, url=url)


def first_existing_source_ref(snapshot: RepoSnapshot, candidates: list[str]) -> SourceRef:
    for candidate in candidates:
        if (snapshot.path / candidate).exists():
            count = min(line_count(snapshot.path, candidate), 240)
            return source_ref(snapshot, candidate, f"1-{count}" if count else None)
    return source_ref(snapshot)


def _first_heading(text: str, default: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip() or default
    return default


def _first_paragraph(text: str, fallback: str) -> str:
    in_frontmatter = False
    started_frontmatter = False
    for block in text.split("\n\n"):
        clean = block.strip()
        if not clean:
            continue
        if clean == "---" and not started_frontmatter:
            started_frontmatter = True
            in_frontmatter = True
            continue
        if in_frontmatter:
            if clean.endswith("---") or clean == "---":
                in_frontmatter = False
            continue
        if clean.startswith("#") or clean.startswith("```"):
            continue
        sentence = " ".join(clean.split())
        if len(sentence) > 240:
            sentence = sentence[:237].rstrip() + "..."
        return sentence
    return fallback


def _useful_description(snapshot: RepoSnapshot, fallback: str) -> str:
    description = (snapshot.description or "").strip()
    generic = {"api", "website", "web", "mcp", "proxy", "agent", "repo", "repository"}
    if description and len(description) >= 18 and description.lower() not in generic:
        return description
    readme = read_file(snapshot.path, "README.md") if (snapshot.path / "README.md").exists() else ""
    return _first_paragraph(readme, description or fallback)


def _headings(text: str, limit: int = 24) -> list[str]:
    headings: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            headings.append(stripped)
        if len(headings) >= limit:
            break
    return headings


def _excerpt(text: str, max_chars: int = 1800) -> str:
    safe_lines: list[str] = []
    omitted = 0
    for line in text.splitlines():
        if SENSITIVE_ASSIGNMENT_RE.search(line):
            omitted += 1
            if not safe_lines or safe_lines[-1] != "[sensitive assignment line omitted]":
                safe_lines.append("[sensitive assignment line omitted]")
            continue
        safe_lines.append(line)
    clean = "\n".join(safe_lines).strip()
    if omitted:
        clean += f"\n\n[{omitted} sensitive assignment line(s) omitted from excerpt]"
    if len(clean) <= max_chars:
        return clean
    return clean[:max_chars].rstrip() + "\n..."


def _doc_type(path: str) -> str:
    name = Path(path).name
    lower = path.lower()
    if name in {"AGENTS.md", "CLAUDE.md"}:
        return "Agent Instruction"
    if name.startswith("SKILL") or "/skills/" in lower:
        return "Skill"
    if "/runbooks/" in lower or "runbook" in lower:
        return "Runbook"
    if path.startswith(".github/workflows/"):
        return "Workflow"
    if "business" in lower or "cost" in lower or "profit" in lower:
        return "Business Analysis"
    return "Source Document"


def _doc_concept_id(snapshot: RepoSnapshot, path: str, doc_type: str) -> str:
    slug = slugify(path.removesuffix(".md"))
    if doc_type == "Workflow":
        return f"generated/workflows/{snapshot.safe_slug}/{slug}"
    return f"generated/source-docs/{snapshot.owner.lower()}/{snapshot.safe_slug}/{slug}"


def _link(concept_id: str, title: str) -> str:
    return f"[{title}](/{concept_id}.md)"


def _host_concept_id(host_name: str) -> str:
    slug = slugify(host_name)
    if slug in {"index", "log"}:
        slug = f"host-{slug}"
    return f"generated/infrastructure/hosts/{slug}"


def _markdown_list(items: list[str], empty: str = "None detected from indexed sources.") -> str:
    if not items:
        return empty
    return "\n".join(f"* {item}" for item in items)


def _yaml_table_rows(data: dict[str, Any]) -> str:
    if not data:
        return "| _none_ | _none_ |\n"
    rows = []
    for key, value in sorted(data.items()):
        rendered = json.dumps(value, sort_keys=True) if isinstance(value, (dict, list)) else str(value)
        rows.append(f"| `{key}` | `{rendered}` |")
    return "\n".join(rows) + "\n"


def build_repository_concept(context: RepoBuildContext, verified_at: str) -> Concept:
    snapshot = context.snapshot
    source = context.source
    docs = [
        file
        for file in snapshot.files
        if file.lower().endswith((".md", ".yml", ".yaml", ".toml", ".json", ".mod", ".py", ".zone", ".service"))
    ]
    topics = ", ".join(snapshot.topics) if snapshot.topics else "none"
    description = _useful_description(snapshot, f"GitHub repository {snapshot.repo}.")
    related = []
    if context.top_concept_id:
        related.append(f"* Top-level concept: {_link(context.top_concept_id, source.title or snapshot.name)}")
    body = f"""# Repository

| Field | Value |
| --- | --- |
| Repository | `{snapshot.repo}` |
| Default branch | `{snapshot.default_branch}` |
| Commit | `{snapshot.commit}` |
| Visibility | `{'private' if snapshot.is_private else 'public'}` |
| Primary language | `{snapshot.primary_language or 'unknown'}` |
| Topics | {topics} |
| GitHub URL | {snapshot.url} |

# Description

{description}

# Extracted inventory

| Asset | Count |
| --- | ---: |
| Indexed source files | {len(docs)} |
| API endpoints | {len(context.endpoints)} |
| API schemas | {len(context.schemas)} |
| Workflows | {len(context.workflows)} |
| Open issues | {len(context.issues)} |
| Open pull requests | {len(context.pull_requests)} |
| Releases | {len(context.releases)} |

# Related concepts

{chr(10).join(related) if related else 'No top-level concept generated for this repository.'}

# Indexed source material

"""
    if docs:
        for rel_path in docs[:120]:
            doc_type = _doc_type(rel_path)
            concept_id = _doc_concept_id(snapshot, rel_path, doc_type)
            body += f"* {_link(concept_id, rel_path)}\n"
        if len(docs) > 120:
            body += f"* ... {len(docs) - 120} additional indexed files omitted from this glance list.\n"
    else:
        body += "No matching source files were indexed.\n"
    body += f"\n# Citations\n\n[1] [{snapshot.repo}]({snapshot.url})\n"
    return Concept(
        concept_id=snapshot.repo_concept_id,
        concept_type="Repository",
        title=source.title or snapshot.repo,
        description=description,
        resource=snapshot.url,
        tags=sorted({"repository", snapshot.owner.lower(), snapshot.name, *snapshot.topics, *source.tags}),
        timestamp=snapshot.updated_at,
        truth_owner="external",
        authority="evidence",
        source_refs=[source_ref(snapshot)],
        last_verified_at=verified_at,
        confidence="high",
        dispute_policy="evidence_only",
        extra={"repo": snapshot.repo, "default_branch": snapshot.default_branch, "commit": snapshot.commit},
        body=body,
    )


def _top_refs(snapshot: RepoSnapshot) -> list[SourceRef]:
    refs: list[SourceRef] = []
    for candidate in ["README.md", "profile/README.md", "AGENTS.md", "CLAUDE.md", "TESTING.md", "hosting-cost-analysis.md"]:
        if (snapshot.path / candidate).exists():
            count = min(line_count(snapshot.path, candidate), 240)
            refs.append(source_ref(snapshot, candidate, f"1-{count}" if count else None))
    if not refs:
        refs.append(source_ref(snapshot))
    return refs


def _source_truth_files(snapshot: RepoSnapshot) -> list[str]:
    preferred = [
        "README.md",
        "AGENTS.md",
        "CLAUDE.md",
        "TESTING.md",
        "pyproject.toml",
        "package.json",
        "go.mod",
    ]
    existing = [path for path in preferred if (snapshot.path / path).exists()]
    docs = [path for path in snapshot.files if path.startswith("docs/") and path.endswith(".md")]
    return [*existing, *docs[:12]]


def _service_interfaces(context: RepoBuildContext) -> list[str]:
    items: list[str] = []
    for endpoint in context.endpoints[:30]:
        items.append(f"`{endpoint.method} {endpoint.route}` — `{endpoint.source_path}:{endpoint.line}`")
    if len(context.endpoints) > 30:
        items.append(f"... {len(context.endpoints) - 30} additional endpoint concepts under `/generated/api/{context.snapshot.safe_slug}/`.")
    for workflow in context.workflows[:8]:
        items.append(f"Workflow `{workflow.name}` from `{workflow.source_path}`")
    return items


def _service_dependencies(context: RepoBuildContext) -> list[str]:
    snapshot = context.snapshot
    deps: list[str] = []
    pyproject = snapshot.path / "pyproject.toml"
    if pyproject.exists():
        text = pyproject.read_text(encoding="utf-8", errors="replace")
        for token in ["fastapi", "sqlalchemy", "asyncpg", "x402", "langgraph", "mcp", "uvicorn", "httpx", "structlog"]:
            if token in text.lower():
                deps.append(f"`{token}` from `pyproject.toml`")
    package_json = snapshot.path / "package.json"
    if package_json.exists():
        text = package_json.read_text(encoding="utf-8", errors="replace")
        for token in ["vite", "typescript", "tailwindcss", "walletconnect", "vitest"]:
            if token in text.lower():
                deps.append(f"`{token}` from `package.json`")
    go_mod = snapshot.path / "go.mod"
    if go_mod.exists():
        deps.append("Go module dependencies from `go.mod`")
    return sorted(dict.fromkeys(deps))


def _deployment_shape(context: RepoBuildContext, all_contexts: list[RepoBuildContext]) -> list[str]:
    repo_name = context.snapshot.name
    shapes: list[str] = []
    netops = next((item for item in all_contexts if item.snapshot.name == "network-operations"), None)
    if netops:
        for host in netops.hosts:
            for pin, value in host.version_pins.items():
                normalized = pin.removesuffix("_version").replace("_", "-")
                if normalized in {repo_name, repo_name.replace("noc-agent", "noc-agent")} or (
                    repo_name == "hyrule-mcp" and pin == "hyrule_mcp_version"
                ):
                    shapes.append(f"Deployed on host `{host.name}` via `{pin}` pinned to `{value}`.")
        if repo_name == "network-operations":
            shapes.append("Owns production deployment record, Ansible inventory, workflow gates, and app version pins.")
    if context.workflows:
        deploys = [wf for wf in context.workflows if wf.deploy_like]
        if deploys:
            shapes.extend(f"Workflow `{wf.name}` has deploy/promotion characteristics." for wf in deploys[:6])
    return shapes


def build_project_concept(
    context: RepoBuildContext, all_contexts: list[RepoBuildContext], verified_at: str
) -> Concept | None:
    source = context.source
    snapshot = context.snapshot
    if source.project_type == "Organization":
        return None
    concept_dir = "services" if source.project_type == "Service" else "projects"
    concept_id = f"generated/{concept_dir}/{source.concept_slug}"
    title = source.service_title or source.title or snapshot.name
    description = _useful_description(snapshot, f"{title} project knowledge derived from {snapshot.repo}.")
    source_files = _source_truth_files(snapshot)
    runbooks = [path for path in source_files if "/runbooks/" in path or "runbook" in path]
    interfaces = _service_interfaces(context)
    dependencies = _service_dependencies(context)
    deployment = _deployment_shape(context, all_contexts)
    related = _related_services(context, all_contexts)
    open_items = [f"#{item.get('number')}: {item.get('title')}" for item in context.issues[:8]]
    body = f"""# What this is

{description}

# Responsibilities

{_markdown_list(_responsibilities_for(snapshot.name), 'Unknown from indexed sources.')}

# Runtime/deployment shape

{_markdown_list(deployment, 'Unknown from indexed sources. Check deployment inventory and workflows.')}

# Interfaces

{_markdown_list(interfaces, 'No public or internal API/workflow interfaces detected from indexed sources.')}

# Dependencies

{_markdown_list(dependencies, 'No package-level dependencies summarized from indexed source files.')}

# Source-of-truth files

{_markdown_list([f'`{path}`' for path in source_files], 'No source-of-truth files matched the configured include set.')}

# Operational runbooks

{_markdown_list([f'`{path}`' for path in runbooks], 'No repo-local runbook files detected in indexed sources.')}

# Safety/security constraints

{_markdown_list(_safety_constraints_for(snapshot.name), 'No specific constraints extracted; follow repository `AGENTS.md` if present.')}

# Related services

{_markdown_list(related, 'No cross-service relationships inferred.')}

# Open issues/known gaps

{_markdown_list(open_items, 'No open GitHub issues indexed for this repository.')}

# Canonicality

Repository-owned facts in this concept are derivative. If this concept disagrees with `{snapshot.repo}` at commit `{snapshot.commit}` or a later source commit, the repository source wins and this concept is stale.

# Citations

"""
    refs = _top_refs(snapshot)
    for idx, ref in enumerate(refs, start=1):
        body += f"[{idx}] [{ref.repo}:{ref.path or 'repository'}]({ref.url})\n"
    return Concept(
        concept_id=concept_id,
        concept_type=source.project_type,
        title=title,
        description=description,
        resource=snapshot.url,
        tags=sorted({source.project_type.lower(), *source.tags, *snapshot.topics}),
        timestamp=snapshot.updated_at,
        truth_owner="repo",
        authority="canonical",
        source_refs=refs,
        last_verified_at=verified_at,
        confidence="high",
        dispute_policy="repo_wins",
        extra={
            "repo": snapshot.repo,
            "commit": snapshot.commit,
            "endpoint_count": len(context.endpoints),
            "schema_count": len(context.schemas),
            "workflow_count": len(context.workflows),
        },
        body=body,
    )


def _responsibilities_for(repo_name: str) -> list[str]:
    mapping = {
        "network-operations": [
            "Production deployment record and source of intended infrastructure state.",
            "Ansible inventory, host vars, firewall rules, monitoring config, DNS zones, and deployment workflows.",
            "Promotion PRs pin exact app SHAs before production applies.",
        ],
        "hyrule-cloud": [
            "Agentic VPS hosting API with x402 payment gating.",
            "Coordinates VM lifecycle, DNS, XCP-NG, PostgreSQL state, domain registration, and paid diagnostic/network resources.",
        ],
        "hyrule-web": [
            "Server-rendered public website and Hyrule Cloud order/dashboard frontend.",
            "Ships committed Vite assets for hosts without Node in production.",
        ],
        "noc-agent": [
            "Alert intake, incident analysis, proactive hotspot scanning, operator approval, and Discord/local control surfaces.",
            "Consumes Hyrule MCP telemetry and stops at reviewable/human-gated proposals.",
        ],
        "hyrule-mcp": [
            "Bounded live diagnostic MCP substrate for routing, monitoring, firewall, host, DNS, and packet-path inspection.",
            "Read-biased tool server used by the NOC agent and operators.",
        ],
        "hyrule-network-proxy": [
            "Internal sidecar that executes already-authorized Hyrule Cloud x402 network requests.",
            "Enforces egress policy and explicit direct/Tor/I2P/Yggdrasil modes.",
        ],
        "engineering-loop": [
            "Autonomous development loop that creates draft PRs from approved issues and requests.",
            "Runs guarded worktrees, policy checks, gates, role judgments, and reflection.",
        ],
        "as215932.net": ["Static ASN website for topology, prefixes, peering, weathermap, and looking-glass stubs."],
        "hyrule-business": ["Business analysis, hosting economics, pricing, profitability, and strategy notes."],
    }
    return mapping.get(repo_name, [])


def _safety_constraints_for(repo_name: str) -> list[str]:
    mapping = {
        "network-operations": [
            "Production applies require human approval through GitHub `production` environment gates.",
            "Every live deployment must compare Icinga snapshots before and after the change.",
            "Firewall changes must update `docs/network-flows.md`, host vars, and rendered artifacts together.",
        ],
        "hyrule-cloud": [
            "Payment verification uses the official x402 flow before paid operations are executed.",
            "Default VM firewall denies inbound except SSH/HTTP/HTTPS and blocks outbound SMTP.",
            "Management endpoints currently require careful ownership/auth review where source says deferred.",
        ],
        "hyrule-network-proxy": [
            "Internal API must not be public.",
            "Do not log bodies, payment headers, authorization headers, cookies, or add residential proxying.",
        ],
        "noc-agent": [
            "Production remediation remains human-gated; no-op rollback guards precede any mutating execution.",
            "Proactive loop is budgeted, read-only for investigation, and hands changes to engineering-loop issues.",
        ],
        "hyrule-mcp": [
            "Raw SSH is bounded and mutative commands are rejected unless explicit action gates are enabled.",
            "Heavy diagnostics are capped server-side.",
        ],
        "engineering-loop": [
            "Stops at draft PR for human review; merges and production applies remain human-gated.",
            "Must not run on privileged GitHub Actions contexts with untrusted code.",
        ],
    }
    return mapping.get(repo_name, [])


def _related_services(context: RepoBuildContext, all_contexts: list[RepoBuildContext]) -> list[str]:
    repo_name = context.snapshot.name
    ids = {ctx.snapshot.name: ctx.top_concept_id for ctx in all_contexts if ctx.top_concept_id}
    relation_names: dict[str, list[str]] = {
        "noc-agent": ["hyrule-mcp", "network-operations", "engineering-loop"],
        "hyrule-mcp": ["noc-agent", "network-operations"],
        "engineering-loop": ["network-operations", "noc-agent", "hyrule-cloud", "hyrule-web"],
        "hyrule-cloud": ["hyrule-web", "hyrule-network-proxy", "network-operations"],
        "hyrule-web": ["hyrule-cloud", "as215932.net", "network-operations"],
        "hyrule-network-proxy": ["hyrule-cloud", "network-operations"],
        "as215932.net": ["network-operations", "hyrule-web"],
        "network-operations": ["noc-agent", "hyrule-mcp", "engineering-loop", "hyrule-cloud", "hyrule-web", "hyrule-network-proxy", "as215932.net"],
        "hyrule-business": ["hyrule-cloud", "network-operations"],
    }
    related: list[str] = []
    for name in relation_names.get(repo_name, []):
        concept_id = ids.get(name)
        if concept_id:
            related.append(_link(concept_id, name))
    return related


def build_organization_concept(contexts: list[RepoBuildContext], verified_at: str) -> Concept:
    repos = [ctx.snapshot for ctx in contexts]
    refs = [first_existing_source_ref(ctx.snapshot, ["profile/README.md", "README.md"]) for ctx in contexts]
    services = [ctx for ctx in contexts if ctx.source.project_type == "Service"]
    projects = [ctx for ctx in contexts if ctx.source.project_type == "Project"]
    netops = next((ctx for ctx in contexts if ctx.snapshot.name == "network-operations"), None)
    hosts = netops.hosts if netops else []
    prefixes = extract_network_constants(netops.snapshot).prefixes if netops else {}
    body = f"""# Overview

AS215932 is the Servify / Hyrule organization knowledge domain for an IPv6-first ISP, Hyrule Cloud product surface, autonomous NOC tooling, and agentic engineering automation. This concept is generated from organization and repository source material and links to the canonical repo-owned concepts.

# Identity and domains

- `hyrule.host` — customer-facing Hyrule Cloud/product identity.
- `servify.network` — infrastructure identity for nameservers, underlay, management, providers, and internal UIs.
- `as215932.net` — AS215932 overlay/routing identity and public ASN website.

See {_link('generated/infrastructure/domain-policy', 'AS215932 Domain Policy')}.

# Repositories

{_markdown_list([_link(ctx.snapshot.repo_concept_id, ctx.snapshot.repo) for ctx in contexts])}

# Production services

{_markdown_list([_link(ctx.top_concept_id or ctx.snapshot.repo_concept_id, ctx.source.title or ctx.snapshot.name) for ctx in services])}

# Projects and strategy

{_markdown_list([_link(ctx.top_concept_id or ctx.snapshot.repo_concept_id, ctx.source.title or ctx.snapshot.name) for ctx in projects])}

# Infrastructure footprint

| Asset | Count |
| --- | ---: |
| Repositories indexed | {len(repos)} |
| Infrastructure hosts | {len(hosts)} |
| Routers | {len([host for host in hosts if host.concept_type == 'Router'])} |
| API endpoints detected | {sum(len(ctx.endpoints) for ctx in contexts)} |
| API schemas detected | {sum(len(ctx.schemas) for ctx in contexts)} |
| Workflows detected | {sum(len(ctx.workflows) for ctx in contexts)} |

## Prefixes

{_markdown_list([f'`{name}` = `{value}`' for name, value in sorted(prefixes.items())], 'No network prefixes extracted.')}

# Operational loops

- {_link('generated/services/noc-agent', 'Hyrule NOC Agent')} handles alert intake, incident investigation, proactive hotspot detection, and human-gated operator decisions.
- {_link('generated/services/hyrule-mcp', 'Hyrule MCP')} provides bounded diagnostic tools for live routing, host, monitoring, DNS, firewall, and packet-path context.
- {_link('generated/services/engineering-loop', 'Hyrule Engineering Loop')} turns approved issues and requests into draft PRs through guarded coding-agent workflows.

# Source-of-truth rules

- Source repositories are canonical for implemented behavior, config, APIs, tests, workflows, deployment pins, and intended infrastructure state.
- Generated OKF concepts are derivative and must cite repo paths/commits.
- OKF-owned curated concepts are advisory/proposed until explicitly reviewed.
- Observed telemetry is evidence only and never silently redefines intended state.

# Key contacts/resources

- NOC: `noc@as215932.net`
- PeeringDB: https://www.peeringdb.com/asn/215932
- Public website: https://as215932.net

# Current gaps/open follow-ups

- Configure `KNOWLEDGE_GH_TOKEN` for scheduled private-repo ingestion.
- Enable branch protection when private branch protection is available for the org/account plan.
- Review proposed curated architecture, policy, lessons, and strategy pages.
- Decide when/where to schedule safe telemetry ingestion beyond manual/local collection.

# Citations

"""
    for idx, ref in enumerate(refs, start=1):
        body += f"[{idx}] [{ref.repo}:{ref.path or 'repository'}]({ref.url})\n"
    return Concept(
        concept_id="generated/org/as215932",
        concept_type="Organization",
        title="AS215932 / Servify / Hyrule Knowledge Domain",
        description="Organization-level map of AS215932 repositories, services, infrastructure, operational loops, and source-of-truth rules.",
        resource="https://github.com/AS215932",
        tags=["as215932", "servify", "hyrule", "organization", "knowledge"],
        truth_owner="derived",
        authority="advisory",
        source_refs=refs,
        last_verified_at=verified_at,
        confidence="high",
        dispute_policy="repo_wins",
        extra={"repository_count": len(repos), "host_count": len(hosts)},
        body=body,
    )


def build_source_doc_concept(snapshot: RepoSnapshot, path: str, verified_at: str) -> Concept:
    text = read_file(snapshot.path, path)
    doc_type = _doc_type(path)
    concept_id = _doc_concept_id(snapshot, path, doc_type)
    title = _first_heading(text, Path(path).name)
    description = _first_paragraph(text, f"Indexed source document `{path}` from {snapshot.repo}.")
    count = line_count(snapshot.path, path)
    headings = _headings(text)
    body = f"""# Source

| Field | Value |
| --- | --- |
| Repository | `{snapshot.repo}` |
| Path | `{path}` |
| Commit | `{snapshot.commit}` |
| Lines | `{count}` |

# Detected headings

"""
    body += ("\n".join(f"* `{heading}`" for heading in headings) + "\n") if headings else "No markdown headings detected.\n"
    if path.lower().endswith(".md"):
        body += f"\n# Deterministic excerpt\n\n```markdown\n{_excerpt(text)}\n```\n"
    body += f"\n# Citations\n\n[1] [{path}]({source_url(snapshot.url, snapshot.commit, path)})\n"
    return Concept(
        concept_id=concept_id,
        concept_type=doc_type,
        title=title,
        description=description,
        resource=source_url(snapshot.url, snapshot.commit, path),
        tags=sorted({doc_type.lower().replace(" ", "-"), snapshot.name, snapshot.owner.lower()}),
        timestamp=snapshot.updated_at,
        truth_owner="repo",
        authority="canonical",
        source_refs=[source_ref(snapshot, path, f"1-{count}" if count else None)],
        last_verified_at=verified_at,
        confidence="high",
        dispute_policy="repo_wins",
        extra={"repo": snapshot.repo, "source_path": path, "commit": snapshot.commit},
        body=body,
    )


def _api_model_link(snapshot_slug: str, model: str, schema_names: set[str]) -> str:
    if model in schema_names and re.match(r"^[A-Za-z_]\w*$", model):
        return _link(model_concept_id(snapshot_slug, model), model)
    return f"`{model}`"


def build_endpoint_concept(
    snapshot: RepoSnapshot, endpoint: ApiEndpointInfo, verified_at: str, schema_names: set[str]
) -> Concept:
    slug = slugify(f"{snapshot.safe_slug}-{endpoint.method}-{endpoint.route}-{endpoint.source_path}-{endpoint.line}")
    status = ", ".join(str(code) for code in endpoint.status_codes) if endpoint.status_codes else "Not statically detected"
    request_models = endpoint.request_models
    model_links = [_api_model_link(snapshot.safe_slug, model, schema_names) for model in request_models if model and model != "None"]
    if endpoint.response_model and endpoint.response_model != "None":
        model_links.append(_api_model_link(snapshot.safe_slug, endpoint.response_model, schema_names))
    line_ref = str(endpoint.line) if endpoint.end_line is None else f"{endpoint.line}-{endpoint.end_line}"
    body = f"""# Endpoint

| Field | Value |
| --- | --- |
| Method | `{endpoint.method}` |
| Path | `{endpoint.route}` |
| Repository | `{snapshot.repo}` |
| Source | `{endpoint.source_path}:{endpoint.line}` |
| Function/handler | `{endpoint.function_name or endpoint.handler_symbol or 'unknown'}` |
| Router | `{endpoint.router_name or 'unknown'}` |
| Status codes | `{status}` |
| Return annotation | `{endpoint.return_annotation or 'not annotated'}` |
| Response model | `{endpoint.response_model or 'not statically declared'}` |

# Request/response models

{_markdown_list(model_links, 'No request or response model statically detected.')}

# Dependencies

{_markdown_list([f'`{dep}`' for dep in endpoint.dependencies], 'No FastAPI dependencies statically detected.')}

# Function documentation

{endpoint.docstring or 'No function docstring found in source.'}

# Notes

This concept is generated from static source analysis. Check the cited source for full validation, side effects, authentication, payment gating, and runtime behavior.

# Citations

[1] [{endpoint.source_path}:{line_ref}]({source_url(snapshot.url, snapshot.commit, endpoint.source_path, line_ref)})
"""
    return Concept(
        concept_id=f"generated/api/{snapshot.safe_slug}/{slug}",
        concept_type="API Endpoint",
        title=f"{endpoint.method} {endpoint.route}",
        description=f"Static API endpoint `{endpoint.method} {endpoint.route}` in {snapshot.repo}.",
        resource=source_url(snapshot.url, snapshot.commit, endpoint.source_path, line_ref),
        tags=["api", snapshot.name, endpoint.method.lower()],
        timestamp=snapshot.updated_at,
        truth_owner="repo",
        authority="canonical",
        source_refs=[source_ref(snapshot, endpoint.source_path, line_ref)],
        last_verified_at=verified_at,
        confidence="high" if endpoint.function_name else "medium",
        dispute_policy="repo_wins",
        extra={
            "repo": snapshot.repo,
            "method": endpoint.method,
            "route": endpoint.route,
            "source_path": endpoint.source_path,
            "function_name": endpoint.function_name,
            "request_models": request_models,
            "response_model": endpoint.response_model,
        },
        body=body,
    )


def build_schema_concept(snapshot: RepoSnapshot, model: PydanticModelInfo, verified_at: str) -> Concept:
    line_ref = str(model.line) if model.end_line is None else f"{model.line}-{model.end_line}"
    rows = "| Field | Type | Required | Default | Description |\n| --- | --- | --- | --- | --- |\n"
    for field_info in model.fields:
        rows += f"| `{field_info.name}` | `{field_info.type}` | `{field_info.required}` | `{field_info.default or ''}` | {field_info.description or ''} |\n"
    body = f"""# API schema

| Field | Value |
| --- | --- |
| Model | `{model.name}` |
| Source | `{model.source_path}:{model.line}` |
| Bases | `{', '.join(model.bases)}` |

# Fields

{rows}
# Validators

{_markdown_list([f'`{validator}`' for validator in model.validators], 'No validators statically detected.')}

# Documentation

{model.docstring or 'No class docstring found in source.'}

# Citations

[1] [{model.source_path}:{line_ref}]({source_url(snapshot.url, snapshot.commit, model.source_path, line_ref)})
"""
    return Concept(
        concept_id=model_concept_id(snapshot.safe_slug, model.name),
        concept_type="API Schema",
        title=model.name,
        description=f"Pydantic API schema `{model.name}` from {snapshot.repo}.",
        resource=source_url(snapshot.url, snapshot.commit, model.source_path, line_ref),
        tags=["api-schema", "pydantic", snapshot.name],
        timestamp=snapshot.updated_at,
        truth_owner="repo",
        authority="canonical",
        source_refs=[source_ref(snapshot, model.source_path, line_ref)],
        last_verified_at=verified_at,
        confidence="high",
        dispute_policy="repo_wins",
        extra={"repo": snapshot.repo, "model": model.name, "source_path": model.source_path},
        body=body,
    )


def build_deployment_concept(
    snapshot: RepoSnapshot,
    host: HostInfo,
    pin_name: str,
    pin_value: str,
    service_context: RepoBuildContext,
    verified_at: str,
) -> Concept:
    host_var_path = f"ansible/inventory/host_vars/{host.name}.yml"
    service_title = service_context.source.service_title or service_context.source.title or service_context.snapshot.name
    service_id = service_context.top_concept_id or service_context.snapshot.repo_concept_id
    service_slug = service_context.source.concept_slug or service_context.snapshot.safe_slug
    host_id = _host_concept_id(host.name)
    refs = [source_ref(snapshot, "ansible/inventory/hosts.yml")]
    if (snapshot.path / host_var_path).exists():
        refs.append(source_ref(snapshot, host_var_path))
    body = f"""# Deployment pin

| Field | Value |
| --- | --- |
| Service | {_link(service_id, service_title)} |
| Host | {_link(host_id, host.name)} |
| Pin variable | `{pin_name}` |
| Pinned version | `{pin_value}` |
| Source host vars | `{host_var_path}` |

# Interpretation

This concept represents intended deployment state from `network-operations`: the named service is pinned to the recorded source revision/version on the target host. Runtime state still needs observed evidence from `okf/observed/` before claiming that the host is actually running this version.

# Citations

[1] [Ansible inventory]({source_url(snapshot.url, snapshot.commit, 'ansible/inventory/hosts.yml')})
"""
    if (snapshot.path / host_var_path).exists():
        body += f"[2] [{host_var_path}]({source_url(snapshot.url, snapshot.commit, host_var_path)})\n"
    return Concept(
        concept_id=f"generated/deployments/{service_slug}-on-{slugify(host.name)}",
        concept_type="Deployment",
        title=f"{service_title} on {host.name}",
        description=f"Intended deployment pin `{pin_name}` for {service_title} on `{host.name}`.",
        resource=source_url(snapshot.url, snapshot.commit, host_var_path if (snapshot.path / host_var_path).exists() else "ansible/inventory/hosts.yml"),
        tags=["deployment", "pin", service_context.snapshot.name, host.name],
        timestamp=snapshot.updated_at,
        truth_owner="repo",
        authority="canonical",
        source_refs=refs,
        last_verified_at=verified_at,
        confidence="high",
        dispute_policy="repo_wins",
        extra={
            "repo": snapshot.repo,
            "service_repo": service_context.snapshot.repo,
            "host": host.name,
            "pin_name": pin_name,
            "pin_value": pin_value,
        },
        body=body,
    )


def build_host_concept(snapshot: RepoSnapshot, host: HostInfo, verified_at: str) -> Concept:
    concept_id = _host_concept_id(host.name)
    firewall = [
        f"`{rule.proto or 'any'}` port `{rule.dport or 'any'}` from `{rule.src}` — {rule.comment or 'no comment'}"
        for rule in host.firewall_rules
    ]
    monitoring = [
        f"`{service.name}` ({service.check_command or 'unspecified'}) — {service.notes or 'no notes'}"
        for service in host.monitoring_services
    ]
    pins = [f"`{key}` = `{value}`" for key, value in host.version_pins.items()]
    peer_rows = _yaml_table_rows(host.peer)
    host_var_rows = _yaml_table_rows({k: v for k, v in host.host_vars.items() if k not in {"firewall_extra_rules", "monitoring_extra_services"}})
    body = f"""# Host

| Field | Value |
| --- | --- |
| Host | `{host.name}` |
| Type | `{host.concept_type}` |
| Address | `{host.address or 'not specified'}` |
| Groups | `{', '.join(host.groups)}` |
| Role comment | `{host.role_comment or 'not found'}` |
| Monitoring role | `{host.monitoring_role or 'not set'}` |
| Logs role | `{host.logs_role or 'not set'}` |

# Deployed version pins

{_markdown_list(pins, 'No app version pins found in host vars.')}

# Inbound firewall rules

{_markdown_list(firewall, 'No `firewall_extra_rules` found in host vars.')}

# Monitoring services

{_markdown_list(monitoring, 'No host-local `monitoring_extra_services` found in host vars.')}

# Peer registry values

| Key | Value |
| --- | --- |
{peer_rows}
# Host variables summary

| Key | Value |
| --- | --- |
{host_var_rows}
# Citations

[1] [Ansible inventory]({source_url(snapshot.url, snapshot.commit, 'ansible/inventory/hosts.yml')})
"""
    refs = [source_ref(snapshot, "ansible/inventory/hosts.yml")]
    host_var_path = f"ansible/inventory/host_vars/{host.name}.yml"
    if (snapshot.path / host_var_path).exists():
        refs.append(source_ref(snapshot, host_var_path))
        body += f"[2] [{host_var_path}]({source_url(snapshot.url, snapshot.commit, host_var_path)})\n"
    return Concept(
        concept_id=concept_id,
        concept_type=host.concept_type,
        title=host.name,
        description=f"{host.concept_type} `{host.name}` with address `{host.address or 'unknown'}` and groups `{', '.join(host.groups)}`.",
        resource=source_url(snapshot.url, snapshot.commit, "ansible/inventory/hosts.yml"),
        tags=["infrastructure", "host", "router" if host.concept_type == "Router" else "vm", *host.groups],
        timestamp=snapshot.updated_at,
        truth_owner="repo",
        authority="canonical",
        source_refs=refs,
        last_verified_at=verified_at,
        confidence="high",
        dispute_policy="repo_wins",
        extra={"repo": snapshot.repo, "host": host.name, "address": host.address, "groups": host.groups},
        body=body,
    )


def build_dns_zone_concept(snapshot: RepoSnapshot, zone: DnsZoneInfo, verified_at: str) -> Concept:
    rows = "| Type | Count |\n| --- | ---: |\n"
    for record_type, count in zone.record_counts.items():
        rows += f"| `{record_type}` | {count} |\n"
    body = f"""# DNS zone

| Field | Value |
| --- | --- |
| Zone | `{zone.zone_name}` |
| Zone file | `{zone.source_path}` |
| Origin | `{zone.origin or 'not declared'}` |
| TTL | `{zone.ttl or 'not declared'}` |
| Repository | `{snapshot.repo}` |
| Commit | `{snapshot.commit}` |

# Record summary

{rows}
# Sample records

```zone
{chr(10).join(zone.sample_records) if zone.sample_records else 'No records parsed.'}
```

# Citations

[1] [{zone.source_path}]({source_url(snapshot.url, snapshot.commit, zone.source_path)})
"""
    return Concept(
        concept_id=f"generated/infrastructure/dns-zones/{slugify(zone.zone_name)}",
        concept_type="DNS Zone",
        title=zone.zone_name,
        description=f"DNS zone `{zone.zone_name}` with {sum(zone.record_counts.values())} parsed records.",
        resource=source_url(snapshot.url, snapshot.commit, zone.source_path),
        tags=["dns", "zone", "infrastructure"],
        timestamp=snapshot.updated_at,
        truth_owner="repo",
        authority="canonical",
        source_refs=[source_ref(snapshot, zone.source_path)],
        last_verified_at=verified_at,
        confidence="high",
        dispute_policy="repo_wins",
        extra={"repo": snapshot.repo, "source_path": zone.source_path, "record_counts": zone.record_counts},
        body=body,
    )


def build_workflow_concept(snapshot: RepoSnapshot, workflow: WorkflowInfo, verified_at: str) -> Concept:
    job_rows = "| Job | Runs on | Environment | Permissions |\n| --- | --- | --- | --- |\n"
    for job in workflow.jobs:
        job_rows += f"| `{job.name}` | `{job.runs_on}` | `{job.environment or ''}` | `{json.dumps(job.permissions, sort_keys=True)}` |\n"
    body = f"""# Workflow

| Field | Value |
| --- | --- |
| Name | `{workflow.name}` |
| Source | `{workflow.source_path}` |
| Triggers | `{', '.join(workflow.triggers)}` |
| Deploy-like | `{workflow.deploy_like}` |
| Workflow permissions | `{json.dumps(workflow.permissions, sort_keys=True)}` |

# Jobs

{job_rows}
# Secrets referenced by name

{_markdown_list([f'`{secret}`' for secret in workflow.secrets], 'No `secrets.*` references detected.')}

# Operational notes

This workflow summary is statically parsed from GitHub Actions YAML. It intentionally records secret names only, never values.

# Citations

[1] [{workflow.source_path}]({source_url(snapshot.url, snapshot.commit, workflow.source_path)})
"""
    return Concept(
        concept_id=_doc_concept_id(snapshot, workflow.source_path, "Workflow"),
        concept_type="Workflow",
        title=workflow.name,
        description=f"GitHub Actions workflow `{workflow.name}` from {snapshot.repo}.",
        resource=source_url(snapshot.url, snapshot.commit, workflow.source_path),
        tags=["workflow", "github-actions", snapshot.name, "deploy" if workflow.deploy_like else "ci"],
        timestamp=snapshot.updated_at,
        truth_owner="repo",
        authority="canonical",
        source_refs=[source_ref(snapshot, workflow.source_path)],
        last_verified_at=verified_at,
        confidence="high",
        dispute_policy="repo_wins",
        extra={"repo": snapshot.repo, "source_path": workflow.source_path, "triggers": workflow.triggers},
        body=body,
    )


def build_monitoring_concept(snapshot: RepoSnapshot, paths: list[str], checks: list[str], verified_at: str) -> Concept | None:
    if not paths:
        return None
    refs = [source_ref(snapshot, path) for path in paths[:12]]
    body = f"""# Monitoring configuration

This concept summarizes tracked monitoring source files under `configs/mon/`.

# Files

{_markdown_list([f'`{path}`' for path in paths[:80]])}

# Check/service names

{_markdown_list([f'`{check}`' for check in checks], 'No monitoring check names inferred.')}

# Citations

"""
    for idx, ref in enumerate(refs, start=1):
        body += f"[{idx}] [{ref.path}]({ref.url})\n"
    return Concept(
        concept_id="generated/monitoring/network-operations-monitoring",
        concept_type="Monitoring Inventory",
        title="Network Operations Monitoring Inventory",
        description="Tracked Prometheus/Icinga/blackbox monitoring configuration files from network-operations.",
        tags=["monitoring", "prometheus", "icinga", "network-operations"],
        timestamp=snapshot.updated_at,
        truth_owner="repo",
        authority="canonical",
        source_refs=refs,
        last_verified_at=verified_at,
        confidence="medium",
        dispute_policy="repo_wins",
        body=body,
    )


def build_prefix_concepts(snapshot: RepoSnapshot, verified_at: str) -> list[Concept]:
    constants = extract_network_constants(snapshot)
    concepts: list[Concept] = []
    for name, prefix in sorted(constants.prefixes.items()):
        concepts.append(
            Concept(
                concept_id=f"generated/infrastructure/prefixes/{slugify(name)}",
                concept_type="Network Prefix",
                title=f"{name}: {prefix}",
                description=f"Network prefix `{prefix}` from `ansible/inventory/group_vars/all.yml` (`{name}`).",
                resource=source_url(snapshot.url, snapshot.commit, "ansible/inventory/group_vars/all.yml"),
                tags=["ipv6" if ":" in prefix else "ipv4", "prefix", "as215932", "infrastructure"],
                timestamp=snapshot.updated_at,
                truth_owner="repo",
                authority="canonical",
                source_refs=[source_ref(snapshot, "ansible/inventory/group_vars/all.yml")],
                last_verified_at=verified_at,
                confidence="high",
                dispute_policy="repo_wins",
                extra={"repo": snapshot.repo, "prefix_name": name, "prefix": prefix},
                body=f"# Prefix\n\n`{name}` is `{prefix}` in the network operations peer/constants registry.\n",
            )
        )
    return concepts


def build_domain_policy_concept(contexts: list[RepoBuildContext], verified_at: str) -> Concept | None:
    refs: list[SourceRef] = []
    for context in contexts:
        snapshot = context.snapshot
        for path in ["AGENTS.md", "CLAUDE.md", "README.md"]:
            file_path = snapshot.path / path
            if file_path.exists():
                text = file_path.read_text(errors="replace")
                if "hyrule.host" in text and "servify.network" in text and "as215932.net" in text:
                    refs.append(source_ref(snapshot, path))
    if not refs:
        return None
    body = """# Domain policy

The deterministic source documents agree on this identity split:

- `hyrule.host` is customer-facing Hyrule Cloud/product identity.
- `servify.network` is infrastructure identity for nameservers, underlay, management, provider relationships, internal UIs, and partner-facing infrastructure hostnames.
- `as215932.net` is AS215932 overlay/routing identity only.

This concept is generated from cited repo-local agent guidance and docs. If a repo-owned domain policy changes, regenerate this concept.

# Citations

"""
    for idx, ref in enumerate(refs, start=1):
        body += f"[{idx}] [{ref.repo}:{ref.path}]({ref.url})\n"
    return Concept(
        concept_id="generated/infrastructure/domain-policy",
        concept_type="Domain Policy",
        title="AS215932 Domain Policy",
        description="Identity split for hyrule.host, servify.network, and as215932.net.",
        tags=["domains", "identity", "policy", "as215932"],
        truth_owner="repo",
        authority="canonical",
        source_refs=refs,
        last_verified_at=verified_at,
        confidence="high",
        dispute_policy="repo_wins",
        body=body,
    )


def _github_item_concept(snapshot: RepoSnapshot, concept_type: str, item: dict[str, Any], verified_at: str) -> Concept:
    number = item.get("number")
    tag = item.get("tagName")
    slug_base = str(number or tag or item.get("name") or item.get("title") or "item")
    section = {
        "GitHub Issue": "issues",
        "GitHub Pull Request": "pull-requests",
        "Release": "releases",
    }[concept_type]
    title = str(item.get("title") or item.get("name") or tag or slug_base)
    url = str(item.get("url") or snapshot.url)
    description = f"{concept_type} evidence item for {snapshot.repo}."
    if number:
        description = f"{concept_type} #{number}: {title}"
    elif tag:
        description = f"Release {tag}: {title}"
    raw_labels = item.get("labels")
    labels: list[Any] = raw_labels if isinstance(raw_labels, list) else []
    label_names = [str(label.get("name")) for label in labels if isinstance(label, dict) and label.get("name")]
    body = f"""# GitHub evidence

| Field | Value |
| --- | --- |
| Repository | `{snapshot.repo}` |
| Type | `{concept_type}` |
| Number/tag | `{number or tag or ''}` |
| State | `{item.get('state') or ''}` |
| Updated | `{item.get('updatedAt') or item.get('publishedAt') or ''}` |
| URL | {url} |

# Labels

{', '.join(label_names) if label_names else 'No labels.'}

# Raw metadata

```json
{json.dumps(item, sort_keys=True, indent=2)}
```

# Citations

[1] [{title}]({url})
"""
    return Concept(
        concept_id=f"generated/github/{section}/{snapshot.safe_slug}/{slugify(slug_base)}",
        concept_type=concept_type,
        title=title,
        description=description,
        resource=url,
        tags=sorted({"github", section, snapshot.name, *label_names}),
        timestamp=str(item.get("updatedAt") or item.get("publishedAt") or verified_at),
        truth_owner="external",
        authority="evidence",
        source_refs=[SourceRef(repo=snapshot.repo, url=url)],
        last_verified_at=verified_at,
        confidence="high",
        dispute_policy="evidence_only",
        extra={"repo": snapshot.repo, "github_type": concept_type, "number": number, "tag": tag},
        body=body,
    )


def collect_contexts(config: AppConfig, snapshots: list[tuple[SourceConfig, RepoSnapshot]]) -> list[RepoBuildContext]:
    contexts: list[RepoBuildContext] = []
    issue_limit = int(config.github.get("issue_limit", 100))
    pr_limit = int(config.github.get("pr_limit", 100))
    release_limit = int(config.github.get("release_limit", 20))
    for source, snapshot in snapshots:
        endpoints, schemas = extract_api(snapshot)
        workflows = extract_workflows(snapshot)
        hosts = extract_hosts(snapshot) if snapshot.name == "network-operations" else []
        zones = extract_zones(snapshot) if snapshot.name == "network-operations" else []
        monitoring_paths = monitoring_config_paths(snapshot) if snapshot.name == "network-operations" else []
        monitoring_checks = monitoring_check_names(snapshot) if snapshot.name == "network-operations" else []
        contexts.append(
            RepoBuildContext(
                source=source,
                snapshot=snapshot,
                endpoints=endpoints,
                schemas=schemas,
                workflows=workflows,
                hosts=hosts,
                zones=zones,
                monitoring_paths=monitoring_paths,
                monitoring_checks=monitoring_checks,
                issues=collect_issues(snapshot.repo, issue_limit),
                pull_requests=collect_pull_requests(snapshot.repo, pr_limit),
                releases=collect_releases(snapshot.repo, release_limit),
            )
        )
    return contexts


def build_all(
    config: AppConfig, snapshots: list[tuple[SourceConfig, RepoSnapshot]], verified_at: str
) -> BuildResult:
    result = BuildResult()
    contexts = collect_contexts(config, snapshots)
    context_by_repo = {context.snapshot.repo: context for context in contexts}
    schema_ids_by_repo: dict[str, set[str]] = defaultdict(set)

    result.add(build_organization_concept(contexts, verified_at))

    for context in contexts:
        snapshot = context.snapshot
        result.source_shas[snapshot.repo] = snapshot.commit
        repo_concept = build_repository_concept(context, verified_at)
        result.add(repo_concept)
        result.edge("generated/org/as215932", repo_concept.concept_id, "contains-repository")

        project_concept = build_project_concept(context, contexts, verified_at)
        if project_concept:
            result.add(project_concept)
            result.edge(project_concept.concept_id, repo_concept.concept_id, "implemented-by")
            result.edge("generated/org/as215932", project_concept.concept_id, "contains-service")

        for rel_path in snapshot.files:
            if rel_path.startswith(".github/workflows/"):
                continue
            doc_concept = build_source_doc_concept(snapshot, rel_path, verified_at)
            result.add(doc_concept)
            result.edge(repo_concept.concept_id, doc_concept.concept_id, "contains")
            if project_concept:
                result.edge(project_concept.concept_id, doc_concept.concept_id, "documented-by")

        for workflow in context.workflows:
            workflow_concept = build_workflow_concept(snapshot, workflow, verified_at)
            result.add(workflow_concept)
            result.edge(repo_concept.concept_id, workflow_concept.concept_id, "defines-workflow")
            if project_concept:
                result.edge(project_concept.concept_id, workflow_concept.concept_id, "operated-by")

        for schema in context.schemas:
            schema_concept = build_schema_concept(snapshot, schema, verified_at)
            schema_ids_by_repo[snapshot.repo].add(schema_concept.concept_id)
            result.add(schema_concept)
            result.edge(repo_concept.concept_id, schema_concept.concept_id, "defines-schema")
            if project_concept:
                result.edge(project_concept.concept_id, schema_concept.concept_id, "uses-schema")

        schema_names = {schema.name for schema in context.schemas}
        for endpoint in context.endpoints:
            endpoint_concept = build_endpoint_concept(snapshot, endpoint, verified_at, schema_names)
            result.add(endpoint_concept)
            result.edge(endpoint_concept.concept_id, repo_concept.concept_id, "defined-in")
            if project_concept:
                result.edge(project_concept.concept_id, endpoint_concept.concept_id, "exposes")
            for model in [*endpoint.request_models, endpoint.response_model or ""]:
                if not model or model == "None":
                    continue
                schema_id = model_concept_id(snapshot.safe_slug, model)
                if schema_id in schema_ids_by_repo[snapshot.repo]:
                    result.edge(endpoint_concept.concept_id, schema_id, "uses-schema")

        if snapshot.name == "network-operations":
            for host in context.hosts:
                host_concept = build_host_concept(snapshot, host, verified_at)
                result.add(host_concept)
                if project_concept:
                    result.edge(project_concept.concept_id, host_concept.concept_id, "owns-intended-state")
                for pin, value in host.version_pins.items():
                    service_repo = _repo_for_pin(pin)
                    service_context = context_by_repo.get(service_repo) if service_repo else None
                    if service_context and service_context.top_concept_id:
                        deployment_concept = build_deployment_concept(snapshot, host, pin, value, service_context, verified_at)
                        result.add(deployment_concept)
                        result.edge(service_context.top_concept_id, host_concept.concept_id, "deployed-on")
                        result.edge(service_context.top_concept_id, deployment_concept.concept_id, "has-deployment-pin")
                        result.edge(deployment_concept.concept_id, host_concept.concept_id, "targets-host")
                        result.edge(deployment_concept.concept_id, service_context.top_concept_id, "deploys-service")
                        if project_concept:
                            result.edge(project_concept.concept_id, deployment_concept.concept_id, "owns-deployment-pin")
            for zone in context.zones:
                zone_concept = build_dns_zone_concept(snapshot, zone, verified_at)
                result.add(zone_concept)
                if project_concept:
                    result.edge(project_concept.concept_id, zone_concept.concept_id, "owns-dns-zone")
            for prefix_concept in build_prefix_concepts(snapshot, verified_at):
                result.add(prefix_concept)
                if project_concept:
                    result.edge(project_concept.concept_id, prefix_concept.concept_id, "owns-prefix")
            monitoring_concept = build_monitoring_concept(snapshot, context.monitoring_paths, context.monitoring_checks, verified_at)
            if monitoring_concept:
                result.add(monitoring_concept)
                if project_concept:
                    result.edge(project_concept.concept_id, monitoring_concept.concept_id, "owns-monitoring")

        for item in context.issues:
            item_concept = _github_item_concept(snapshot, "GitHub Issue", item, verified_at)
            result.add(item_concept)
            result.edge(repo_concept.concept_id, item_concept.concept_id, "has-github-evidence")
            result.github_items.append(item_concept.extra | {"id": item_concept.concept_id})
        for item in context.pull_requests:
            item_concept = _github_item_concept(snapshot, "GitHub Pull Request", item, verified_at)
            result.add(item_concept)
            result.edge(repo_concept.concept_id, item_concept.concept_id, "has-github-evidence")
            result.github_items.append(item_concept.extra | {"id": item_concept.concept_id})
        for item in context.releases:
            item_concept = _github_item_concept(snapshot, "Release", item, verified_at)
            result.add(item_concept)
            result.edge(repo_concept.concept_id, item_concept.concept_id, "has-github-evidence")
            result.github_items.append(item_concept.extra | {"id": item_concept.concept_id})

    domain_policy = build_domain_policy_concept(contexts, verified_at)
    if domain_policy:
        result.add(domain_policy)
        result.edge("generated/org/as215932", domain_policy.concept_id, "has-policy")

    for source_name, target_names in _service_relationships().items():
        source_context = next((ctx for ctx in contexts if ctx.snapshot.name == source_name), None)
        if not source_context or not source_context.top_concept_id:
            continue
        for target_name in target_names:
            target_context = next((ctx for ctx in contexts if ctx.snapshot.name == target_name), None)
            if target_context and target_context.top_concept_id:
                result.edge(source_context.top_concept_id, target_context.top_concept_id, "related-to")

    return result


def _repo_for_pin(pin: str) -> str | None:
    mapping = {
        "hyrule_cloud_version": "AS215932/hyrule-cloud",
        "hyrule_web_version": "AS215932/hyrule-web",
        "noc_agent_version": "AS215932/noc-agent",
        "hyrule_mcp_version": "AS215932/hyrule-mcp",
        "hyrule_network_proxy_version": "AS215932/hyrule-network-proxy",
        "engineering_loop_version": "AS215932/engineering-loop",
    }
    return mapping.get(pin)


def _service_relationships() -> dict[str, list[str]]:
    return {
        "network-operations": ["noc-agent", "hyrule-mcp", "engineering-loop", "hyrule-cloud", "hyrule-web", "hyrule-network-proxy", "as215932.net"],
        "noc-agent": ["hyrule-mcp", "network-operations", "engineering-loop"],
        "hyrule-mcp": ["noc-agent", "network-operations"],
        "engineering-loop": ["network-operations", "noc-agent", "hyrule-cloud", "hyrule-web"],
        "hyrule-cloud": ["hyrule-web", "hyrule-network-proxy", "network-operations"],
        "hyrule-web": ["hyrule-cloud", "as215932.net"],
        "hyrule-network-proxy": ["hyrule-cloud"],
        "as215932.net": ["network-operations", "hyrule-web"],
        "hyrule-business": ["hyrule-cloud"],
    }
