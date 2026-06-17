"""Ansible inventory and host variable extraction."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from hyrule_knowledge.models import RepoSnapshot


@dataclass(frozen=True)
class FirewallRuleInfo:
    proto: str | None
    dport: str | int | None
    src: Any
    comment: str | None


@dataclass(frozen=True)
class MonitoringServiceInfo:
    name: str
    check_command: str | None = None
    notes: str | None = None


@dataclass(frozen=True)
class HostInfo:
    name: str
    concept_type: str
    address: str | None
    groups: list[str]
    attrs: dict[str, Any]
    peer: dict[str, Any] = field(default_factory=dict)
    host_vars: dict[str, Any] = field(default_factory=dict)
    role_comment: str | None = None
    firewall_rules: list[FirewallRuleInfo] = field(default_factory=list)
    monitoring_services: list[MonitoringServiceInfo] = field(default_factory=list)
    version_pins: dict[str, str] = field(default_factory=dict)
    logs_role: str | None = None
    monitoring_role: str | None = None


@dataclass(frozen=True)
class NetworkConstants:
    prefixes: dict[str, str]
    peers: dict[str, dict[str, Any]]


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def _role_comment(path: Path) -> str | None:
    if not path.exists():
        return None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        stripped = line.strip()
        if stripped.startswith("#") and "—" in stripped:
            return stripped.lstrip("#").strip()
    return None


def _walk_inventory(group_name: str, group: Any, hosts: dict[str, dict[str, Any]], groups: dict[str, set[str]]) -> None:
    if not isinstance(group, dict):
        return
    raw_hosts = group.get("hosts")
    if isinstance(raw_hosts, dict):
        for host, attrs in raw_hosts.items():
            host_name = str(host)
            groups.setdefault(host_name, set()).add(group_name)
            if isinstance(attrs, dict):
                hosts.setdefault(host_name, {}).update(attrs)
            else:
                hosts.setdefault(host_name, {})
    children = group.get("children")
    if isinstance(children, dict):
        for child_name, child in children.items():
            _walk_inventory(str(child_name), child, hosts, groups)


def _firewall_rules(host_vars: dict[str, Any]) -> list[FirewallRuleInfo]:
    raw = host_vars.get("firewall_extra_rules")
    if not isinstance(raw, list):
        return []
    rules: list[FirewallRuleInfo] = []
    for item in raw:
        if not isinstance(item, dict):
            continue
        rules.append(
            FirewallRuleInfo(
                proto=str(item.get("proto")) if item.get("proto") is not None else None,
                dport=item.get("dport"),
                src=item.get("src"),
                comment=str(item.get("comment")) if item.get("comment") is not None else None,
            )
        )
    return rules


def _monitoring_services(host_vars: dict[str, Any]) -> list[MonitoringServiceInfo]:
    raw = host_vars.get("monitoring_extra_services")
    if not isinstance(raw, list):
        return []
    services: list[MonitoringServiceInfo] = []
    for item in raw:
        if not isinstance(item, dict) or not item.get("name"):
            continue
        services.append(
            MonitoringServiceInfo(
                name=str(item["name"]),
                check_command=str(item.get("check_command")) if item.get("check_command") else None,
                notes=str(item.get("notes")) if item.get("notes") else None,
            )
        )
    return services


def _version_pins(host_vars: dict[str, Any]) -> dict[str, str]:
    pins: dict[str, str] = {}
    for key, value in host_vars.items():
        if key.endswith("_version") and isinstance(value, str):
            pins[key] = value
    return pins


def extract_network_constants(snapshot: RepoSnapshot) -> NetworkConstants:
    all_vars = _load_yaml(snapshot.path / "ansible/inventory/group_vars/all.yml")
    prefixes: dict[str, str] = {}
    for key, value in all_vars.items():
        if key.endswith("_subnet") or key.endswith("_prefix") or key in {"as215932_prefix"}:
            if isinstance(value, str):
                prefixes[key] = value
    raw_peers = all_vars.get("peers", {})
    peers = raw_peers if isinstance(raw_peers, dict) else {}
    normalized_peers = {
        str(name): value for name, value in peers.items() if isinstance(value, dict)
    }
    return NetworkConstants(prefixes=prefixes, peers=normalized_peers)


def extract_hosts(snapshot: RepoSnapshot) -> list[HostInfo]:
    inventory = _load_yaml(snapshot.path / "ansible/inventory/hosts.yml")
    hosts: dict[str, dict[str, Any]] = {}
    group_membership: dict[str, set[str]] = {}
    _walk_inventory("all", inventory.get("all", inventory), hosts, group_membership)
    constants = extract_network_constants(snapshot)

    result: list[HostInfo] = []
    host_vars_dir = snapshot.path / "ansible/inventory/host_vars"
    for name, attrs in sorted(hosts.items()):
        host_vars_path = host_vars_dir / f"{name}.yml"
        host_vars = _load_yaml(host_vars_path)
        groups = sorted(group_membership.get(name, set()))
        concept_type = "Router" if "routers" in groups else "Infrastructure Host"
        peer = constants.peers.get(name) or constants.peers.get(name.replace("-", "_")) or {}
        address = attrs.get("ansible_host") or peer.get("ipv6") or peer.get("loopback")
        result.append(
            HostInfo(
                name=name,
                concept_type=concept_type,
                address=str(address) if address is not None else None,
                groups=groups,
                attrs=attrs,
                peer=peer,
                host_vars=host_vars,
                role_comment=_role_comment(host_vars_path),
                firewall_rules=_firewall_rules(host_vars),
                monitoring_services=_monitoring_services(host_vars),
                version_pins=_version_pins(host_vars),
                logs_role=str(host_vars.get("logs_role")) if host_vars.get("logs_role") else None,
                monitoring_role=str(host_vars.get("monitoring_role")) if host_vars.get("monitoring_role") else None,
            )
        )
    return result
