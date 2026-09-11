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

from relation_model import compatibility_warnings, normalize_relation, ref_id, relation_predicate
from semantic_model import is_capability


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


class GraphIndex:
    def __init__(self, objects: dict[str, dict[str, Any]], relations: list[dict[str, Any]]):
        self.objects = objects
        self.relations = relations
        self.edges: list[Edge] = []
        self.issues: list[ReferenceIssue] = []
        self.compatibility_warnings = []
        self._forward: dict[str, list[Edge]] = defaultdict(list)
        self._backlinks: dict[str, list[Edge]] = defaultdict(list)
        self._build()

    def _add_edge(self, edge: Edge) -> None:
        self.edges.append(edge)
        self._forward[edge.source_id].append(edge)
        self._backlinks[edge.target_id].append(edge)

    def _matches_expected_semantics(self, target: dict[str, Any], expected_type: str) -> bool:
        if expected_type == "capability":
            return is_capability(target)
        return target.get("type") == expected_type

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
        if expected_type and not self._matches_expected_semantics(target, expected_type):
            self.issues.append(
                ReferenceIssue(
                    "type_mismatch",
                    source_id,
                    target_id,
                    f"{field} expects semantic {expected_type}, got {target.get('type')}",
                )
            )
            return
        self._add_edge(Edge(source_id, target_id, "field_reference", "object", field=field))

    def _build_object_references(self) -> None:
        typed_list_fields = {"capabilities": "capability"}
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
            descriptor = normalize_relation(relation)
            relation_id = descriptor.relation_id or "<unnamed-relation>"
            source_id = descriptor.source_id
            target_id = descriptor.target_id
            predicate = descriptor.predicate

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

            # Legacy `{type,id}` hints are compatibility metadata, not identity.
            # A stale hint is reported but the stable ID edge remains valid.
            self.compatibility_warnings.extend(compatibility_warnings(relation, self.objects))
            self._add_edge(Edge(source_id, target_id, predicate, "relation", relation_id=relation_id))

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
            capabilities = normalize_relation(relation).context.get("capabilities", [])
            if capability_id in capabilities:
                result.append(relation)
        return result


def diagnostics(
    root: Path,
    storage_paths: Iterable[Path | str] | None = None,
) -> dict[str, Any]:
    from bootstrap_query import index_objects, load_atlas

    objects, relations = load_atlas(root, storage_paths)
    graph = GraphIndex(index_objects(objects), relations)
    return {
        "objects": len(objects),
        "relations": len(relations),
        "edges": len(graph.edges),
        "reference_issues": [asdict(issue) for issue in graph.issues],
        "compatibility_warnings": [asdict(item) for item in graph.compatibility_warnings],
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
