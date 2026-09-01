#!/usr/bin/env python3
"""Relation compatibility normalization for Knowledge Model v0.

Canonical v0 Relations use ID-only source/target refs and a unified context.
Legacy `{type, id}` refs and legacy context fields remain readable during the
migration window. Normalization is read-only and never mutates source records.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True)
class RelationDescriptor:
    relation_id: str | None
    source_id: str | None
    predicate: str | None
    target_id: str | None
    context: dict[str, Any]
    evidence: tuple[Mapping[str, Any], ...]
    assertor: str | None
    canonical_refs: bool


@dataclass(frozen=True)
class RelationCompatibilityWarning:
    code: str
    relation_id: str | None
    endpoint: str
    object_id: str | None
    declared_type: str | None
    actual_type: str | None
    message: str


def ref_id(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, Mapping):
        candidate = value.get("id")
        return candidate if isinstance(candidate, str) else None
    return None


def relation_predicate(record: Mapping[str, Any]) -> str | None:
    for key in ("relation", "predicate", "kind"):
        value = record.get(key)
        if isinstance(value, str):
            return value
    return None


def normalize_relation(record: Mapping[str, Any]) -> RelationDescriptor:
    source_ref = record.get("source")
    target_ref = record.get("target")
    context = _normalized_context(record)
    evidence_value = record.get("evidence")
    evidence = (
        tuple(item for item in evidence_value if isinstance(item, Mapping))
        if isinstance(evidence_value, list)
        else ()
    )
    assertor = record.get("assertor")
    if not isinstance(assertor, str):
        assertor = None

    return RelationDescriptor(
        relation_id=record.get("id") if isinstance(record.get("id"), str) else None,
        source_id=ref_id(source_ref),
        predicate=relation_predicate(record),
        target_id=ref_id(target_ref),
        context=context,
        evidence=evidence,
        assertor=assertor,
        canonical_refs=isinstance(source_ref, str) and isinstance(target_ref, str),
    )


def compatibility_warnings(
    record: Mapping[str, Any], objects: Mapping[str, Mapping[str, Any]]
) -> tuple[RelationCompatibilityWarning, ...]:
    """Report stale Legacy type hints without rejecting stable ID references."""

    relation_id = record.get("id") if isinstance(record.get("id"), str) else None
    warnings: list[RelationCompatibilityWarning] = []
    for endpoint in ("source", "target"):
        ref = record.get(endpoint)
        if not isinstance(ref, Mapping):
            continue
        object_id = ref_id(ref)
        declared_type = ref.get("type") if isinstance(ref.get("type"), str) else None
        target = objects.get(object_id) if object_id else None
        actual_type = target.get("type") if isinstance(target, Mapping) and isinstance(target.get("type"), str) else None
        if declared_type and actual_type and declared_type != actual_type:
            warnings.append(
                RelationCompatibilityWarning(
                    code="legacy_relation_type_hint_stale",
                    relation_id=relation_id,
                    endpoint=endpoint,
                    object_id=object_id,
                    declared_type=declared_type,
                    actual_type=actual_type,
                    message=(
                        f"Legacy {endpoint} type hint '{declared_type}' is stale; "
                        f"stable ID resolves to current type '{actual_type}'."
                    ),
                )
            )
    return tuple(warnings)


def _normalized_context(record: Mapping[str, Any]) -> dict[str, Any]:
    raw_context = record.get("context")
    context: dict[str, Any] = deepcopy(raw_context) if isinstance(raw_context, Mapping) else {}

    _merge_context_refs(context, "capabilities", record.get("capability_context"))
    _merge_context_refs(context, "scenarios", record.get("scenario_context"))

    for legacy_key in ("conditions_zh", "conditions_en"):
        value = record.get(legacy_key)
        if legacy_key not in context and isinstance(value, str):
            context[legacy_key] = value

    return context


def _merge_context_refs(context: dict[str, Any], key: str, legacy_value: Any) -> None:
    if key in context or legacy_value is None:
        return
    values = legacy_value if isinstance(legacy_value, list) else [legacy_value]
    ids = [item_id for item in values if (item_id := ref_id(item))]
    if ids:
        context[key] = ids
