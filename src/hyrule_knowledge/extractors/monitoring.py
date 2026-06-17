"""Monitoring configuration helpers."""

from __future__ import annotations

from pathlib import Path

from hyrule_knowledge.models import RepoSnapshot


def monitoring_config_paths(snapshot: RepoSnapshot) -> list[str]:
    root = snapshot.path / "configs/mon"
    if not root.exists():
        return []
    paths: list[str] = []
    for path in root.rglob("*"):
        if path.is_file():
            paths.append(path.relative_to(snapshot.path).as_posix())
    return sorted(paths)


def monitoring_check_names(snapshot: RepoSnapshot) -> list[str]:
    names: list[str] = []
    for rel_path in monitoring_config_paths(snapshot):
        if "/services/" in rel_path or rel_path.endswith("prometheus.yml"):
            names.append(Path(rel_path).stem)
    return sorted(dict.fromkeys(names))
