#!/usr/bin/env python3
"""Semantic normalization for legacy and Knowledge Model v0 records.

This module is deliberately read-only: it describes a record's semantic view
without mutating Canonical YAML. It is the I1 compatibility layer from #61.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


CORE_FAMILIES = frozenset({"concept", "artifact", "system", "agent"})

_CLEAR_ARTIFACT_STANDARD_KINDS = frozenset(
    {"standard", "protocol", "specification", "format", "profile"}
)
_STANDARD_AUDIT_KINDS = frozenset({"api", "interface", "device_class"})


@dataclass(frozen=True)
class SemanticDescriptor:
    """Runtime-only normalized semantics for one repository record."""

    record_class: str
    family: str | None = None
    kind: str | None = None
    profiles: tuple[str, ...] = ()
    legacy_type: str | None = None
    migration_status: str = "normalized"


def normalize_record(record: Mapping[str, Any]) -> SemanticDescriptor:
    """Return a stable semantic view without changing *record*.

    ``migration_status`` is descriptive rather than a validation result:
    - ``v0``: already uses a Core Identity Family.
    - ``legacy``: safe legacy normalization is available.
    - ``audit_required``: reality identity cannot be inferred safely.
    - ``provisional``: record class is known but its future profile is open.
    - ``unknown``: I1 intentionally has no semantic mapping yet.
    """

    raw_type = record.get("type")
    raw_kind = record.get("kind")

    if raw_type in CORE_FAMILIES:
        return SemanticDescriptor(
            record_class="identity",
            family=raw_type,
            kind=raw_kind,
            profiles=_profiles_for(raw_type, raw_kind),
            migration_status="v0",
        )

    if _looks_like_relation(record):
        return SemanticDescriptor(
            record_class="statement",
            kind="relation",
            profiles=("relation",),
            legacy_type=raw_type if raw_type != "relation" else None,
            migration_status="legacy" if raw_type != "relation" else "normalized",
        )

    if raw_type == "capability":
        return _legacy_identity("concept", "capability", "capability")

    if raw_type == "scenario":
        return _legacy_identity("concept", "scenario", "scenario")

    if raw_type == "implementation":
        if raw_kind == "reference_implementation":
            return _audit_identity(None, raw_kind, raw_type)
        return SemanticDescriptor(
            record_class="identity",
            family="system",
            kind=raw_kind,
            profiles=("implementation",),
            legacy_type=raw_type,
            migration_status="legacy",
        )

    if raw_type == "organization":
        if record.get("organization_kind") == "open_source_project":
            return _audit_identity(None, "open_source_project", raw_type)
        return _legacy_identity("agent", "organization", "organization")

    if raw_type == "standard":
        if raw_kind in _STANDARD_AUDIT_KINDS:
            return _audit_identity(None, raw_kind, raw_type)
        if raw_kind in _CLEAR_ARTIFACT_STANDARD_KINDS or raw_kind is None:
            return SemanticDescriptor(
                record_class="identity",
                family="artifact",
                kind=raw_kind or "standard",
                profiles=("normative_artifact",),
                legacy_type=raw_type,
                migration_status="legacy",
            )
        # Unknown legacy Standard kinds are not guessed into a stable identity.
        return _audit_identity(None, raw_kind, raw_type)

    if raw_type == "reference_project":
        return SemanticDescriptor(
            record_class="identity",
            kind=raw_kind,
            legacy_type=raw_type,
            migration_status="audit_required",
        )

    if raw_type == "map":
        return SemanticDescriptor(record_class="view", kind="map", migration_status="legacy")

    if raw_type == "open_gap":
        return SemanticDescriptor(
            record_class="finding",
            kind="open_gap",
            legacy_type=raw_type,
            migration_status="provisional",
        )

    return SemanticDescriptor(
        record_class="unknown",
        kind=raw_kind,
        legacy_type=raw_type,
        migration_status="unknown",
    )


def is_identity(record: Mapping[str, Any]) -> bool:
    return normalize_record(record).record_class == "identity"


def semantic_family(record: Mapping[str, Any]) -> str | None:
    return normalize_record(record).family


def semantic_kind(record: Mapping[str, Any]) -> str | None:
    return normalize_record(record).kind


def is_capability(record: Mapping[str, Any]) -> bool:
    descriptor = normalize_record(record)
    return descriptor.family == "concept" and descriptor.kind == "capability"


def is_scenario(record: Mapping[str, Any]) -> bool:
    descriptor = normalize_record(record)
    return descriptor.family == "concept" and descriptor.kind == "scenario"


def is_implementation_system(record: Mapping[str, Any]) -> bool:
    descriptor = normalize_record(record)
    return descriptor.family == "system" and "implementation" in descriptor.profiles


def is_organization_agent(record: Mapping[str, Any]) -> bool:
    descriptor = normalize_record(record)
    return descriptor.family == "agent" and "organization" in descriptor.profiles


def _profiles_for(family: str, kind: str | None) -> tuple[str, ...]:
    if family == "concept" and kind == "capability":
        return ("capability",)
    if family == "concept" and kind == "scenario":
        return ("scenario",)
    if family == "system" and kind == "software":
        return ("implementation",)
    if family == "agent" and kind == "organization":
        return ("organization",)
    if family == "artifact" and kind in _CLEAR_ARTIFACT_STANDARD_KINDS:
        return ("normative_artifact",)
    return ()


def _legacy_identity(family: str, kind: str, profile: str) -> SemanticDescriptor:
    return SemanticDescriptor(
        record_class="identity",
        family=family,
        kind=kind,
        profiles=(profile,),
        legacy_type={
            "capability": "capability",
            "scenario": "scenario",
            "organization": "organization",
        }.get(kind),
        migration_status="legacy",
    )


def _audit_identity(
    family: str | None,
    kind: str | None,
    legacy_type: str | None,
    profiles: tuple[str, ...] = (),
) -> SemanticDescriptor:
    return SemanticDescriptor(
        record_class="identity",
        family=family,
        kind=kind,
        profiles=profiles,
        legacy_type=legacy_type,
        migration_status="audit_required",
    )


def _looks_like_relation(record: Mapping[str, Any]) -> bool:
    if record.get("type") == "relation":
        return True
    return (
        "source" in record
        and "target" in record
        and any(key in record for key in ("relation", "predicate", "kind"))
    )
