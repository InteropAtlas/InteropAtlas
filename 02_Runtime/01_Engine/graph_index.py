#!/usr/bin/env python3
"""Minimal resolved reference graph for InteropAtlas.

This module intentionally keeps two kinds of edges distinct:
- field references recorded directly on objects, such as ``capabilities``;
- explicit semantic Relation objects.

It resolves IDs against the loaded object index and records validation issues
without inventing semantic relationships that are not present in source data.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


@dataclass(frozen=True)
class Edge:
    source_id: str
    target_id: str
    kind: str
    origin: str
    field: str | None = None
    relation_id: str | None = None


@dataclass(frozen=True)
class ReferenceIssue:
    code: str
    source_id: str
    target_id: str | None
    detail: str


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


class GraphIndex:
    def __init__(self, objects: dict[str, dict[str, Any]], relations: list[dict[str, Any]]):
        self.objects = objects
        self.relations = relations
        self.edges: list[Edge] = []
        self.issues: list[ReferenceIssue] = []
        self._forward: dict[str, list[Edge]] = defaultdict(list)
        self._backlinks: dict[str, list[Edge]] = defaultdict(list)
        self._build()

    def _add_edge(self, edge: Edge) -> None:
        self.edges.append(edge)
        self._forward[edge.source_id].append(edge)
        self._backlinks[edge.target_id].append(edge)

    def _resolve_field_reference(
        self,
        source: dict[str, Any],
        field: str,
        target_id: str,
        expected_type: str | None = None,
    ) -> None:
        source_id = str(source.get("id", "<unknown>"))
        target = self.objects.get(target_id)
        if target is None:
            self.issues.append(
                ReferenceIssue("unknown_reference", source_id, target_id, f"{field} references unknown object")
            )
            return
        if expected_type and target.get("type") != expected_type:
            self.issues.append(
                ReferenceIssue(
                    "type_mismatch",
                    source_id,
                    target_id,
                    f"{field} expects {expected_type}, got {target.get('type')}",
                )
            )
            return
        self._add_edge(Edge(source_id, target_id, "field_reference", "object", field=field))

    def _build_object_references(self) -> None:
        # Start with fields already used by the current vertical slice. Extend only
        # when real objects require more reference-bearing fields.
        typed_list_fields = {
            "capabilities": "capability",
        }
        for source in self.objects.values():
            for field, expected_type in typed_list_fields.items():
                values = source.get(field) or []
                if not isinstance(values, list):
                    continue
                for value in values:
                    target_id = ref_id(value)
                    if target_id:
                        self._resolve_field_reference(source, field, target_id, expected_type)

    def _build_relations(self) -> None:
        for relation in self.relations:
            relation_id = str(relation.get("id", "<unnamed-relation>"))
            source_ref = relation.get("source")
            target_ref = relation.get("target")
            source_id = ref_id(source_ref)
            target_id = ref_id(target_ref)
            predicate = relation_predicate(relation)

            if not source_id or not target_id or not predicate:
                self.issues.append(
                    ReferenceIssue("invalid_relation", relation_id, target_id, "relation requires source, target and predicate")
                )
                continue
            source = self.objects.get(source_id)
            target = self.objects.get(target_id)
            if source is None:
                self.issues.append(
                    ReferenceIssue("unknown_relation_source", relation_id, source_id, "relation source does not exist")
                )
                continue
            if target is None:
                self.issues.append(
                    ReferenceIssue("unknown_relation_target", relation_id, target_id, "relation target does not exist")
                )
                continue

            if isinstance(source_ref, dict) and source_ref.get("type") and source_ref.get("type") != source.get("type"):
                self.issues.append(
                    ReferenceIssue("relation_source_type_mismatch", relation_id, source_id, "declared source type does not match object")
                )
                continue
            if isinstance(target_ref, dict) and target_ref.get("type") and target_ref.get("type") != target.get("type"):
                self.issues.append(
                    ReferenceIssue("relation_target_type_mismatch", relation_id, target_id, "declared target type does not match object")
                )
                continue

            self._add_edge(
                Edge(source_id, target_id, predicate, "relation", relation_id=relation_id)
            )

    def _build(self) -> None:
        self._build_object_references()
        self._build_relations()

    def forward(self, object_id: str) -> list[Edge]:
        return list(self._forward.get(object_id, ()))

    def backlinks(self, object_id: str) -> list[Edge]:
        return list(self._backlinks.get(object_id, ()))

    def relation_objects_for_capability(self, capability_id: str) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        for relation in self.relations:
            context = relation.get("capability_context")
            values = context if isinstance(context, list) else [context] if context is not None else []
            if any(ref_id(value) == capability_id for value in values):
                result.append(relation)
        return result


def diagnostics(
    root: Path,
    storage_paths: Iterable[Path | str] | None = None,
) -> dict[str, Any]:
    # Local import avoids making bootstrap_query depend on graph_index.
    from bootstrap_query import index_objects, load_atlas

    objects, relations = load_atlas(root, storage_paths)
    graph = GraphIndex(index_objects(objects), relations)
    return {
        "objects": len(objects),
        "relations": len(relations),
        "edges": len(graph.edges),
        "reference_issues": [asdict(issue) for issue in graph.issues],
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
    args = parser.parse_args()
    print(json.dumps(diagnostics(args.root, args.storage_paths), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
