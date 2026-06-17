"""Small built-in policy evaluator for knowledge access and safe agent actions."""

from __future__ import annotations

import fnmatch
from pathlib import Path
from typing import Any

import yaml

from .contracts import PolicyDecision, PolicyRequest

DEFAULT_POLICY_PATH = Path("knowledge-policy.yml")
DEFAULT_POLICY_VERSION = "knowledge_policy_v1"
PRODUCTION_MUTATION_ACTIONS = {
    "production.deploy",
    "production.restart_service",
    "production.modify_firewall",
    "production.modify_routing",
    "production.rotate_credentials",
}


class KnowledgePolicyError(RuntimeError):
    """Raised when a policy file is malformed."""


def load_policy(path: Path | str | None = None) -> dict[str, Any]:
    policy_path = Path(path) if path is not None else DEFAULT_POLICY_PATH
    if not policy_path.exists():
        return default_policy()
    loaded = yaml.safe_load(policy_path.read_text(encoding="utf-8")) or {}
    if not isinstance(loaded, dict):
        raise KnowledgePolicyError(f"policy file must be a mapping: {policy_path}")
    return loaded


def default_policy() -> dict[str, Any]:
    return {
        "version": DEFAULT_POLICY_VERSION,
        "defaults": {
            "result": "deny",
            "max_context_pack_tokens": 8000,
            "max_result_refs": 40,
            "deny_data_classes": ["secret", "raw_log", "packet_capture", "credential"],
            "production_mutation_result": "require_human",
        },
        "roles": {
            "engineering_loop": {
                "allow_actions": [
                    "knowledge.resolve",
                    "knowledge.search",
                    "knowledge.claims",
                    "knowledge.neighborhood",
                    "knowledge.context_pack.generate",
                    "knowledge.intended_state",
                    "knowledge.observed_state",
                    "knowledge.diff_intended_observed",
                    "knowledge.endpoint_schema",
                    "knowledge.deployment_pins",
                    "knowledge.policy_decision",
                    "knowledge.related_runbooks",
                    "knowledge.find_conflicts",
                    "knowledge.find_stale",
                    "local.test.run",
                    "draft_pr.create",
                ],
                "require_human_actions": sorted(PRODUCTION_MUTATION_ACTIONS),
            },
            "noc_shadow": {
                "allow_actions": [
                    "knowledge.resolve",
                    "knowledge.search",
                    "knowledge.claims",
                    "knowledge.context_pack.generate",
                    "knowledge.intended_state",
                    "knowledge.observed_state.fixture",
                    "knowledge.diff_intended_observed",
                    "knowledge.related_runbooks",
                    "knowledge.find_conflicts",
                    "knowledge.find_stale",
                ],
                "deny_actions": ["production.*", "live_diagnostic.*", "secret.*"],
            },
            "general": {
                "allow_actions": [
                    "knowledge.resolve",
                    "knowledge.search",
                    "knowledge.claims",
                    "knowledge.context_pack.generate",
                    "knowledge.intended_state",
                    "knowledge.endpoint_schema",
                ]
            },
        },
    }


def _mapping(value: Any, *, label: str) -> dict[str, Any]:
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise KnowledgePolicyError(f"{label} must be a mapping")
    return value


def _list(value: Any, *, label: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise KnowledgePolicyError(f"{label} must be a list of strings")
    return list(value)


def _matches(action: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatch(action, pattern) for pattern in patterns)


def evaluate_policy(request: PolicyRequest, policy: dict[str, Any] | None = None) -> PolicyDecision:
    active = policy or load_policy()
    version = str(active.get("version") or DEFAULT_POLICY_VERSION)
    defaults = _mapping(active.get("defaults"), label="defaults")
    roles = _mapping(active.get("roles"), label="roles")
    role = _mapping(roles.get(request.actor), label=f"roles.{request.actor}")
    reasons: list[str] = []
    forbid_data_classes = _list(defaults.get("deny_data_classes"), label="defaults.deny_data_classes")
    constraints = {
        "max_context_pack_tokens": int(defaults.get("max_context_pack_tokens", 8000)),
        "max_result_refs": int(defaults.get("max_result_refs", 40)),
        "require_citations": True,
        "forbid_data_classes": forbid_data_classes,
    }

    denied_data = sorted(set(request.data_classes) & set(forbid_data_classes))
    if denied_data:
        return PolicyDecision.build(
            request=request,
            result="deny",
            policy_version=version,
            reasons=[f"request includes denied data classes: {', '.join(denied_data)}"],
            constraints=constraints,
        )

    deny_actions = _list(role.get("deny_actions"), label=f"roles.{request.actor}.deny_actions")
    if _matches(request.action, deny_actions):
        return PolicyDecision.build(
            request=request,
            result="deny",
            policy_version=version,
            reasons=[f"action denied for actor {request.actor}: {request.action}"],
            constraints=constraints,
        )

    require_human = _list(role.get("require_human_actions"), label=f"roles.{request.actor}.require_human_actions")
    production_default = str(defaults.get("production_mutation_result", "require_human"))
    if _matches(request.action, require_human) or _matches(request.action, sorted(PRODUCTION_MUTATION_ACTIONS)):
        result = "require_human" if production_default == "require_human" else "deny"
        return PolicyDecision.build(
            request=request,
            result=result,  # type: ignore[arg-type]
            policy_version=version,
            reasons=[f"production-sensitive action requires human control: {request.action}"],
            constraints=constraints,
        )

    allow_actions = _list(role.get("allow_actions"), label=f"roles.{request.actor}.allow_actions")
    if _matches(request.action, allow_actions):
        reasons.append(f"{request.actor} may perform read-only action {request.action}")
        if request.environment == "production" and request.tool_tier >= 4:
            return PolicyDecision.build(
                request=request,
                result="require_human",
                policy_version=version,
                reasons=[*reasons, "production tier-4 actions require human approval"],
                constraints=constraints,
            )
        return PolicyDecision.build(
            request=request,
            result="allow",
            policy_version=version,
            reasons=reasons,
            constraints=constraints,
        )

    fallback = str(defaults.get("result", "deny"))
    return PolicyDecision.build(
        request=request,
        result="deny" if fallback not in {"allow", "require_human", "allow_readonly_substitute"} else fallback,  # type: ignore[arg-type]
        policy_version=version,
        reasons=[f"no allow rule matched for actor={request.actor} action={request.action}"],
        constraints=constraints,
    )


def policy_decision_for(
    *,
    actor: str,
    action: str,
    target: str | None = None,
    environment: str = "local",
    risk_level: str = "low",
    tool_tier: int = 0,
    data_classes: list[str] | None = None,
    context: dict[str, Any] | None = None,
    policy_path: Path | str | None = None,
) -> PolicyDecision:
    request = PolicyRequest.build(
        actor=actor,
        action=action,
        target=target,
        environment=environment,
        risk_level=risk_level,
        tool_tier=tool_tier,
        data_classes=data_classes or [],
        context=context or {},
    )
    return evaluate_policy(request, load_policy(policy_path))
