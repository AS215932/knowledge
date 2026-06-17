"""DNS zone extraction."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from hyrule_knowledge.models import RepoSnapshot

RECORD_TYPES = {
    "A",
    "AAAA",
    "CNAME",
    "MX",
    "NS",
    "SOA",
    "SRV",
    "TXT",
    "CAA",
    "PTR",
    "TLSA",
    "SSHFP",
}


@dataclass(frozen=True)
class DnsZoneInfo:
    zone_name: str
    source_path: str
    origin: str | None
    ttl: str | None
    record_counts: dict[str, int]
    sample_records: list[str] = field(default_factory=list)


def parse_zone(path: Path, rel_path: str) -> DnsZoneInfo:
    origin: str | None = None
    ttl: str | None = None
    counts: Counter[str] = Counter()
    samples: list[str] = []
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.split(";", 1)[0].strip()
        if not line:
            continue
        if line.startswith("$ORIGIN"):
            parts = line.split()
            if len(parts) > 1:
                origin = parts[1]
            continue
        if line.startswith("$TTL"):
            parts = line.split()
            if len(parts) > 1:
                ttl = parts[1]
            continue
        parts = line.split()
        record_type = next((part.upper() for part in parts if part.upper() in RECORD_TYPES), None)
        if record_type:
            counts[record_type] += 1
            if len(samples) < 12:
                samples.append(line)
    return DnsZoneInfo(
        zone_name=path.name.removesuffix(".zone"),
        source_path=rel_path,
        origin=origin,
        ttl=ttl,
        record_counts=dict(sorted(counts.items())),
        sample_records=samples,
    )


def extract_zones(snapshot: RepoSnapshot) -> list[DnsZoneInfo]:
    zones: list[DnsZoneInfo] = []
    for zone_path in sorted(snapshot.path.glob("configs/*.zone")):
        rel_path = zone_path.relative_to(snapshot.path).as_posix()
        zones.append(parse_zone(zone_path, rel_path))
    return zones
