"""Build OKF concepts from source repository snapshots."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from .config import AppConfig, SourceConfig
from .github_source import (
    collect_issues,
    collect_pull_requests,
    collect_releases,
    line_count,
    read_file,
    run_text,
    source_url,
)
from .models import Concept, Edge, RepoSnapshot, SourceRef
from .okf_writer import slugify

FASTAPI_ROUTE_RE = re.compile(
    r"@(?:app|router|api_router)\.(get|post|put|patch|delete)\(\s*['\"]([^'\"]+)['\"]",
    re.IGNORECASE,
)
GO_HANDLE_RE = re.compile(r"(?:HandleFunc|Handle)\(\s*['\"]([^'\"]+)['\"]")


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


def source_ref(snapshot: RepoSnapshot, rel_path: str | None = None, lines: str | None = None) -> SourceRef:
    url = snapshot.url
    if rel_path:
        url = source_url(snapshot.url, snapshot.commit, rel_path, lines)
    return SourceRef(repo=snapshot.repo, path=rel_path, commit=snapshot.commit, lines=lines, url=url)


def first_existing_source_ref(snapshot: RepoSnapshot, candidates: list[str]) -> SourceRef:
    for candidate in candidates:
        if (snapshot.path / candidate).exists():
            count = min(line_count(snapshot.path, candidate), 200)
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


def _headings(text: str, limit: int = 24) -> list[str]:
    items: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            items.append(stripped)
        if len(items) >= limit:
            break
    return items


SENSITIVE_ASSIGNMENT_RE = re.compile(
    r"(?i)(api[_-]?key|auth[_-]?token|secret|password)\s*[:=]"
)


def _excerpt(text: str, max_chars: int = 1400) -> str:
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


def build_repository_concept(snapshot: RepoSnapshot, source: SourceConfig, verified_at: str) -> Concept:
    docs = [f for f in snapshot.files if f.lower().endswith(('.md', '.yml', '.yaml', '.toml', '.json', '.mod', '.py', '.zone', '.service'))]
    topics = ", ".join(snapshot.topics) if snapshot.topics else "none"
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

{snapshot.description or 'No GitHub description set.'}

# Indexed source material

"""
    if docs:
        for rel_path in docs[:80]:
            doc_type = _doc_type(rel_path)
            concept_id = _doc_concept_id(snapshot, rel_path, doc_type)
            body += f"* [{rel_path}](/" + concept_id + ".md)\n"
        if len(docs) > 80:
            body += f"* ... {len(docs) - 80} additional indexed files omitted from this glance list.\n"
    else:
        body += "No matching source files were indexed.\n"
    body += f"\n# Citations\n\n[1] [{snapshot.repo}]({snapshot.url})\n"
    return Concept(
        concept_id=snapshot.repo_concept_id,
        concept_type="Repository",
        title=source.title or snapshot.repo,
        description=snapshot.description or f"GitHub repository {snapshot.repo}.",
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


def build_project_concept(snapshot: RepoSnapshot, source: SourceConfig, verified_at: str) -> Concept:
    concept_dir = "services" if source.project_type == "Service" else "projects"
    concept_id = f"generated/{concept_dir}/{source.concept_slug}"
    readme_candidates = ["README.md", "profile/README.md", "hosting-cost-analysis.md"]
    ref = first_existing_source_ref(snapshot, readme_candidates)
    description = snapshot.description or f"{source.title or snapshot.name} project knowledge derived from {snapshot.repo}."
    body = f"""# Overview

{description}

# Source repository

Implemented or documented by [{snapshot.repo}](/generated/repositories/{snapshot.owner.lower()}/{snapshot.name}.md).

# Canonicality

Repository-owned facts in this concept are derivative. If this concept disagrees with `{snapshot.repo}` at commit `{snapshot.commit}` or a later source commit, the repository source wins and this concept is stale.

# Citations

[1] [{snapshot.repo}]({snapshot.url})
"""
    return Concept(
        concept_id=concept_id,
        concept_type=source.project_type,
        title=source.service_title or source.title or snapshot.name,
        description=description,
        resource=snapshot.url,
        tags=sorted({source.project_type.lower(), *source.tags, *snapshot.topics}),
        timestamp=snapshot.updated_at,
        truth_owner="repo",
        authority="canonical",
        source_refs=[ref],
        last_verified_at=verified_at,
        confidence="high",
        dispute_policy="repo_wins",
        extra={"repo": snapshot.repo, "commit": snapshot.commit},
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
    if headings:
        body += "\n".join(f"* `{heading}`" for heading in headings) + "\n"
    else:
        body += "No markdown headings detected.\n"
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


def _tracked_source_files(snapshot: RepoSnapshot) -> list[str]:
    raw = run_text(["git", "ls-files", "*.py", "*.go"], cwd=snapshot.path, allow_failure=True)
    return sorted(line.strip() for line in raw.splitlines() if line.strip())


def build_api_endpoint_concepts(snapshot: RepoSnapshot, verified_at: str) -> list[Concept]:
    concepts: list[Concept] = []
    for rel_path in _tracked_source_files(snapshot):
        text = read_file(snapshot.path, rel_path)
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in FASTAPI_ROUTE_RE.finditer(line):
                method = match.group(1).upper()
                route = match.group(2)
                concepts.append(_endpoint_concept(snapshot, rel_path, line_number, method, route, verified_at))
            for match in GO_HANDLE_RE.finditer(line):
                route = match.group(1)
                concepts.append(_endpoint_concept(snapshot, rel_path, line_number, "ANY", route, verified_at))
    return concepts


def _endpoint_concept(
    snapshot: RepoSnapshot, rel_path: str, line_number: int, method: str, route: str, verified_at: str
) -> Concept:
    slug = slugify(f"{snapshot.safe_slug}-{method}-{route}-{rel_path}-{line_number}")
    title = f"{method} {route}"
    description = f"Detected API endpoint in {snapshot.repo}:{rel_path}."
    body = f"""# Endpoint

| Field | Value |
| --- | --- |
| Method | `{method}` |
| Path | `{route}` |
| Repository | `{snapshot.repo}` |
| Source | `{rel_path}:{line_number}` |

This endpoint was detected deterministically from source code. Check the cited source for request/response semantics.

# Citations

[1] [{rel_path}:{line_number}]({source_url(snapshot.url, snapshot.commit, rel_path, str(line_number))})
"""
    return Concept(
        concept_id=f"generated/api/{snapshot.safe_slug}/{slug}",
        concept_type="API Endpoint",
        title=title,
        description=description,
        resource=source_url(snapshot.url, snapshot.commit, rel_path, str(line_number)),
        tags=["api", snapshot.name, method.lower()],
        timestamp=snapshot.updated_at,
        truth_owner="repo",
        authority="canonical",
        source_refs=[source_ref(snapshot, rel_path, str(line_number))],
        last_verified_at=verified_at,
        confidence="medium",
        dispute_policy="repo_wins",
        extra={"repo": snapshot.repo, "method": method, "route": route, "source_path": rel_path},
        body=body,
    )


def _all_hosts(hosts_tree: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], set[str]]:
    hosts: dict[str, dict[str, Any]] = {}
    routers: set[str] = set()

    def walk_group(name: str, group: Any) -> None:
        if not isinstance(group, dict):
            return
        raw_hosts = group.get("hosts")
        if isinstance(raw_hosts, dict):
            for hostname, attrs in raw_hosts.items():
                existing = hosts.setdefault(str(hostname), {})
                if isinstance(attrs, dict):
                    existing.update(attrs)
                if name == "routers":
                    routers.add(str(hostname))
        children = group.get("children")
        if isinstance(children, dict):
            for child_name, child in children.items():
                walk_group(str(child_name), child)

    walk_group("all", hosts_tree.get("all", hosts_tree))
    children = hosts_tree.get("all", {}).get("children", {}) if isinstance(hosts_tree.get("all"), dict) else {}
    if isinstance(children, dict) and isinstance(children.get("routers"), dict):
        raw = children["routers"].get("hosts", {})
        if isinstance(raw, dict):
            routers.update(str(name) for name in raw)
    return hosts, routers


def build_infrastructure_concepts(snapshot: RepoSnapshot, verified_at: str) -> list[Concept]:
    concepts: list[Concept] = []
    inventory = snapshot.path / "ansible/inventory/hosts.yml"
    if inventory.exists():
        data = yaml.safe_load(inventory.read_text())
        if isinstance(data, dict):
            hosts, routers = _all_hosts(data)
            for host, attrs in sorted(hosts.items()):
                addr = attrs.get("ansible_host") if isinstance(attrs, dict) else None
                concept_type = "Router" if host in routers else "Infrastructure Host"
                slug = slugify(host)
                description = f"{concept_type} `{host}` from Ansible inventory."
                if addr:
                    description += f" Address: `{addr}`."
                body = f"""# Host

| Field | Value |
| --- | --- |
| Host | `{host}` |
| Type | `{concept_type}` |
| Address | `{addr or 'not specified'}` |
| Source | `ansible/inventory/hosts.yml` |

# Citations

[1] [Ansible inventory]({source_url(snapshot.url, snapshot.commit, 'ansible/inventory/hosts.yml')})
"""
                concepts.append(
                    Concept(
                        concept_id=f"generated/infrastructure/hosts/{slug}",
                        concept_type=concept_type,
                        title=host,
                        description=description,
                        resource=source_url(snapshot.url, snapshot.commit, "ansible/inventory/hosts.yml"),
                        tags=["infrastructure", "host", "router" if host in routers else "vm"],
                        timestamp=snapshot.updated_at,
                        truth_owner="repo",
                        authority="canonical",
                        source_refs=[source_ref(snapshot, "ansible/inventory/hosts.yml")],
                        last_verified_at=verified_at,
                        confidence="high",
                        dispute_policy="repo_wins",
                        extra={"repo": snapshot.repo, "host": host, "address": addr},
                        body=body,
                    )
                )
    for zone_path in sorted(snapshot.path.glob("configs/*.zone")):
        rel_path = zone_path.relative_to(snapshot.path).as_posix()
        zone_name = zone_path.name.removesuffix(".zone")
        body = f"""# DNS zone

| Field | Value |
| --- | --- |
| Zone file | `{rel_path}` |
| Repository | `{snapshot.repo}` |
| Commit | `{snapshot.commit}` |

# Citations

[1] [{rel_path}]({source_url(snapshot.url, snapshot.commit, rel_path)})
"""
        concepts.append(
            Concept(
                concept_id=f"generated/infrastructure/dns-zones/{slugify(zone_name)}",
                concept_type="DNS Zone",
                title=zone_name,
                description=f"DNS zone file `{rel_path}` from network operations.",
                resource=source_url(snapshot.url, snapshot.commit, rel_path),
                tags=["dns", "zone", "infrastructure"],
                timestamp=snapshot.updated_at,
                truth_owner="repo",
                authority="canonical",
                source_refs=[source_ref(snapshot, rel_path)],
                last_verified_at=verified_at,
                confidence="high",
                dispute_policy="repo_wins",
                extra={"repo": snapshot.repo, "source_path": rel_path},
                body=body,
            )
        )
    readme = snapshot.path / "README.md"
    if readme.exists() and "2a0c:b641:b50::/44" in readme.read_text(errors="replace"):
        concepts.append(
            Concept(
                concept_id="generated/infrastructure/prefixes/2a0c-b641-b50-44",
                concept_type="Network Prefix",
                title="2a0c:b641:b50::/44",
                description="AS215932 IPv6 overlay prefix documented by network operations.",
                resource=source_url(snapshot.url, snapshot.commit, "README.md"),
                tags=["ipv6", "prefix", "as215932"],
                timestamp=snapshot.updated_at,
                truth_owner="repo",
                authority="canonical",
                source_refs=[source_ref(snapshot, "README.md")],
                last_verified_at=verified_at,
                confidence="high",
                dispute_policy="repo_wins",
                extra={"repo": snapshot.repo, "prefix": "2a0c:b641:b50::/44"},
                body="# Prefix\n\n`2a0c:b641:b50::/44` is the documented AS215932 IPv6 overlay prefix.\n",
            )
        )
    return concepts


def build_domain_policy_concept(snapshots: list[RepoSnapshot], verified_at: str) -> Concept | None:
    refs: list[SourceRef] = []
    for snapshot in snapshots:
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


def build_github_item_concepts(snapshot: RepoSnapshot, config: AppConfig, verified_at: str) -> list[Concept]:
    concepts: list[Concept] = []
    issue_limit = int(config.github.get("issue_limit", 100))
    pr_limit = int(config.github.get("pr_limit", 100))
    release_limit = int(config.github.get("release_limit", 20))

    for item in collect_issues(snapshot.repo, issue_limit):
        concepts.append(_github_item_concept(snapshot, "GitHub Issue", item, verified_at))
    for item in collect_pull_requests(snapshot.repo, pr_limit):
        concepts.append(_github_item_concept(snapshot, "GitHub Pull Request", item, verified_at))
    for item in collect_releases(snapshot.repo, release_limit):
        concepts.append(_github_item_concept(snapshot, "Release", item, verified_at))
    return concepts


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
    label_names = [
        str(label.get("name")) for label in labels if isinstance(label, dict) and label.get("name")
    ]
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


def build_all(
    config: AppConfig, snapshots: list[tuple[SourceConfig, RepoSnapshot]], verified_at: str
) -> BuildResult:
    result = BuildResult()
    for source, snapshot in snapshots:
        result.source_shas[snapshot.repo] = snapshot.commit
        repo_concept = build_repository_concept(snapshot, source, verified_at)
        project_concept = build_project_concept(snapshot, source, verified_at)
        result.add(repo_concept)
        result.add(project_concept)
        result.edge(project_concept.concept_id, repo_concept.concept_id, "implemented-by")

        for rel_path in snapshot.files:
            doc_concept = build_source_doc_concept(snapshot, rel_path, verified_at)
            result.add(doc_concept)
            result.edge(repo_concept.concept_id, doc_concept.concept_id, "contains")
            result.edge(project_concept.concept_id, doc_concept.concept_id, "documented-by")

        for endpoint in build_api_endpoint_concepts(snapshot, verified_at):
            result.add(endpoint)
            result.edge(project_concept.concept_id, endpoint.concept_id, "exposes")
            result.edge(endpoint.concept_id, repo_concept.concept_id, "defined-in")

        if snapshot.name == "network-operations":
            for concept in build_infrastructure_concepts(snapshot, verified_at):
                result.add(concept)
                result.edge(project_concept.concept_id, concept.concept_id, "owns-intended-state")

        for item_concept in build_github_item_concepts(snapshot, config, verified_at):
            result.add(item_concept)
            result.edge(repo_concept.concept_id, item_concept.concept_id, "has-github-evidence")
            result.github_items.append(item_concept.extra | {"id": item_concept.concept_id})

    domain_policy = build_domain_policy_concept([snapshot for _, snapshot in snapshots], verified_at)
    if domain_policy:
        result.add(domain_policy)
    return result
