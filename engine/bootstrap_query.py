#!/usr/bin/env python3
"""Minimal deterministic InteropAtlas bootstrap query.

Temporary executable harness. It intentionally does not perform semantic/AI
reasoning: it loads facts, indexes objects, filters fields and follows recorded
relations.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

import yaml

from repository_layout import repository_layout


def yaml_documents(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for document in yaml.safe_load_all(handle):
            if isinstance(document, dict):
                yield document


def load_atlas(
    root: Path,
    storage_paths: Iterable[Path | str] | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Load canonical Atlas objects from configured physical storage locations.

    Storage locations are repository plumbing only. Object semantics come from
    the document itself: a Relation is a Relation because ``type: relation``,
    not because the YAML happened to live in a directory named ``relations``.
    """

    layout = repository_layout(root, storage_paths)
    objects: list[dict[str, Any]] = []
    relations: list[dict[str, Any]] = []

    for path in layout.iter_yaml_files():
        for document in yaml_documents(path):
            source = layout.physical_source(path)
            # Keep current generated-view behaviour unchanged until a later
            # migration explicitly defines a storage-independent public route.
            document.setdefault("_source", source)
            document.setdefault("_physical_source", source)
            if document.get("type") == "relation":
                relations.append(document)
            else:
                objects.append(document)

    return objects, relations


def index_objects(objects: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    duplicates: list[str] = []
    for obj in objects:
        object_id = obj.get("id")
        if not isinstance(object_id, str):
            continue
        if object_id in index:
            duplicates.append(object_id)
        index[object_id] = obj
    if duplicates:
        raise ValueError(f"duplicate object ids: {', '.join(sorted(set(duplicates)))}")
    return index


def implementations_for_capability(
    objects: list[dict[str, Any]], capability_id: str
) -> list[dict[str, Any]]:
    return [
        obj
        for obj in objects
        if obj.get("type") == "implementation"
        and capability_id in (obj.get("capabilities") or [])
    ]


def ref_id(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        candidate = value.get("id")
        return candidate if isinstance(candidate, str) else None
    return None


def relation_predicate(relation: dict[str, Any]) -> str | None:
    for key in ("relation", "predicate", "kind"):
        value = relation.get(key)
        if isinstance(value, str):
            return value
    return None


def alternative_relations(
    relations: list[dict[str, Any]], capability_id: str
) -> list[dict[str, Any]]:
    result = []
    for relation in relations:
        if relation_predicate(relation) != "alternative_to":
            continue
        context = relation.get("capability_context")
        if context is not None and ref_id(context) != capability_id and context != capability_id:
            continue
        result.append(relation)
    return result


def run(
    root: Path,
    capability_id: str,
    storage_paths: Iterable[Path | str] | None = None,
) -> dict[str, Any]:
    objects, relations = load_atlas(root, storage_paths)
    index = index_objects(objects)
    implementations = implementations_for_capability(objects, capability_id)
    open_self_hostable = [
        item
        for item in implementations
        if item.get("open_source") is True and item.get("self_hostable") is True
    ]

    return {
        "experiment": "capability_implementation_supportability",
        "mode": "deterministic",
        "capability": capability_id,
        "capability_exists": capability_id in index,
        "implementation_ids": [item.get("id") for item in implementations],
        "open_source_and_self_hostable_ids": [item.get("id") for item in open_self_hostable],
        "alternative_relations": [
            {
                "source": ref_id(item.get("source")),
                "relation": relation_predicate(item),
                "target": ref_id(item.get("target")),
            }
            for item in alternative_relations(relations, capability_id)
        ],
        "counts": {
            "objects": len(objects),
            "relations": len(relations),
            "matching_implementations": len(implementations),
        },
        "interpretation_boundary": (
            "This output reports recorded facts only. It does not decide whether an "
            "implementation is a sufficient substitute or whether an Open Gap exists."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--storage-path",
        type=Path,
        action="append",
        dest="storage_paths",
        help=(
            "repository-relative canonical storage location; repeat for multiple "
            "locations. If omitted, use the current legacy locations."
        ),
    )
    parser.add_argument("--capability", default="automated_build_deployment")
    args = parser.parse_args()
    print(
        json.dumps(
            run(args.root, args.capability, args.storage_paths),
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
