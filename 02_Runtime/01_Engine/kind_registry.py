#!/usr/bin/env python3
"""Controlled object-kind vocabulary support for Knowledge Model v0."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from semantic_model import CORE_FAMILIES, normalize_record


DEFAULT_REGISTRY = (
    Path(__file__).resolve().parents[2]
    / "01_State"
    / "01_Objects"
    / "object-kind.vocabulary.json"
)


@dataclass(frozen=True)
class KindFinding:
    code: str
    message: str
    object_id: str | None = None
    family: str | None = None
    kind: str | None = None


def load_kind_registry(path: Path = DEFAULT_REGISTRY) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    _validate_registry_shape(data)
    return data


def validate_v0_identity(
    record: Mapping[str, Any], registry: Mapping[str, Any]
) -> tuple[KindFinding, ...]:
    """Validate family/kind membership for v0 Identity Objects only.

    Legacy and audit-required records are deliberately outside I2 enforcement.
    """

    descriptor = normalize_record(record)
    if descriptor.record_class != "identity" or descriptor.migration_status != "v0":
        return ()

    object_id = record.get("id")
    family = descriptor.family
    kind = descriptor.kind

    if family not in CORE_FAMILIES:
        return (
            KindFinding(
                code="IA-MR-005",
                message="Identity family is not a registered Core Identity Family.",
                object_id=object_id,
                family=family,
                kind=kind,
            ),
        )

    if not kind:
        return (
            KindFinding(
                code="IA-MR-005",
                message="v0 Identity Object requires a controlled kind.",
                object_id=object_id,
                family=family,
            ),
        )

    term = registry["terms"].get(kind)
    if term is None:
        return (
            KindFinding(
                code="IA-MR-005",
                message="Kind is not registered in the controlled object-kind vocabulary.",
                object_id=object_id,
                family=family,
                kind=kind,
            ),
        )

    if term["family"] != family:
        return (
            KindFinding(
                code="IA-MR-005",
                message=f"Kind '{kind}' belongs to family '{term['family']}', not '{family}'.",
                object_id=object_id,
                family=family,
                kind=kind,
            ),
        )

    if term.get("status") != "active":
        return (
            KindFinding(
                code="IA-MR-005",
                message=f"Kind '{kind}' is not active.",
                object_id=object_id,
                family=family,
                kind=kind,
            ),
        )

    return ()


def profiles_for_v0_identity(
    record: Mapping[str, Any], registry: Mapping[str, Any]
) -> tuple[str, ...]:
    findings = validate_v0_identity(record, registry)
    if findings:
        return ()
    kind = record.get("kind")
    return tuple(registry["terms"][kind].get("profiles", ()))


def _validate_registry_shape(data: Mapping[str, Any]) -> None:
    terms = data.get("terms")
    if not isinstance(terms, dict) or not terms:
        raise ValueError("object-kind registry must contain a non-empty 'terms' object")

    for term_name, term in terms.items():
        if not isinstance(term_name, str) or not term_name:
            raise ValueError("kind term names must be non-empty strings")
        if not isinstance(term, dict):
            raise ValueError(f"kind term '{term_name}' must be an object")
        family = term.get("family")
        if family not in CORE_FAMILIES:
            raise ValueError(f"kind term '{term_name}' has invalid family '{family}'")
        profiles = term.get("profiles", [])
        if not isinstance(profiles, list) or not all(isinstance(p, str) and p for p in profiles):
            raise ValueError(f"kind term '{term_name}' profiles must be a string array")
        if term.get("status") not in {"active", "deprecated", "reserved"}:
            raise ValueError(f"kind term '{term_name}' has invalid status")
