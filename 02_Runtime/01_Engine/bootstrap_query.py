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
from urllib.parse import quote

import yaml

from kind_registry import has_profile, load_kind_registry
from repository_layout import repository_layout


def repository_root() -> Path:
    """Find the repository root without depending on Engine folder depth."""

    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".git").exists() or (parent / "01_State").exists():
            return parent
    raise RuntimeError("could not locate InteropAtlas repository root")


def yaml_documents(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for document in yaml.safe_load_all(handle):
            if isinstance(document, dict):
                yield document


def relation_predicate(relation: dict[str, Any]) -> str | None:
    for key in ("relation", "predicate", "kind"):
        value = relation.get(key)
        if isinstance(value, str):
            return value
    return None


def is_relation_document(document: dict[str, Any]) -> bool:
    if document.get("type") == "relation":
        return True
    if document.get("type") is not None:
        return False
    return (
        document.get("source") is not None
        and document.get("target") is not None
        and relation_predicate(document) is not None
    )


def logical_source_path(document: dict[str, Any], is_relation: bool) -> str | None:
    document_id = document.get("id")
    if not isinstance(document_id, str) or not document_id:
        return None
    safe_id = quote(document_id, safe="-._~")
    namespace = "relations" if is_relation else "objects"
    return f"{namespace}/{safe_id}.yaml"


def load_atlas(
    root: Path,
    storage_paths: Iterable[Path | str] | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    layout = repository_layout(root, storage_paths)
    objects: list[dict[str, Any]] = []
    relations: list[dict[str, Any]] = []

    for path in layout.iter_yaml_files():
        for document in yaml_documents(path):
            physical_source = layout.physical_source(path)
            relation_document = is_relation_document(document)
            logical_source = logical_source_path(document, relation_document)
            document.setdefault("_physical_source", physical_source)
            document.setdefault("_source", logical_source or physical_source)
            if relation_document:
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
    registry = load_kind_registry()
    return [
        obj
        for obj in objects
        if has_profile(obj, "implementation", registry)
        and capability_id in (obj.get("capabilities") or [])
    ]


def ref_id(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        candidate = value.get("id")
        return candidate if isinstance(candidate, str) else None
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
    parser.add_argument("--root", type=Path, default=repository_root())
    parser.add_argument(
        "--storage-path",
        type=Path,
        action="append",
        dest="storage_paths",
        help=(
            "repository-relative canonical storage location; repeat for multiple "
            "locations. If omitted, use the current configured State locations."
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
