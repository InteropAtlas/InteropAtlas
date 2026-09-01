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

from repository_layout import RELATION_FAMILY, repository_layout


def yaml_documents(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for document in yaml.safe_load_all(handle):
            if isinstance(document, dict):
                yield document


def load_atlas(
    root: Path,
    data_root: Path | str | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Load canonical Atlas objects through the repository layout contract.

    ``root`` remains the repository checkout root. ``data_root`` is a
    repository-relative physical location for canonical object families and
    defaults to the current contract (``.``). No caller needs to know the list
    of object-family directories.
    """

    layout = repository_layout(root, data_root)
    objects: list[dict[str, Any]] = []
    relations: list[dict[str, Any]] = []

    for family, path in layout.iter_yaml_files():
        for document in yaml_documents(path):
            # `_source` is intentionally the stable logical source consumed by
            # generated views. `_physical_source` preserves the actual repository
            # path for migration/debug traceability. Today they are identical;
            # after a future root -> data/ migration only the physical path changes.
            document.setdefault("_source", layout.logical_source(family, path))
            document.setdefault("_physical_source", layout.physical_source(path))
            document.setdefault("_object_family", family)
            if family == RELATION_FAMILY or document.get("type") == "relation":
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
    data_root: Path | str | None = None,
) -> dict[str, Any]:
    objects, relations = load_atlas(root, data_root)
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
        "--data-root",
        type=Path,
        help="repository-relative canonical data root; defaults to the repository layout contract",
    )
    parser.add_argument("--capability", default="automated_build_deployment")
    args = parser.parse_args()
    print(
        json.dumps(
            run(args.root, args.capability, args.data_root),
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
