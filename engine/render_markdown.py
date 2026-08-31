#!/usr/bin/env python3
"""Render InteropAtlas objects into linked, human-readable Chinese Markdown views."""

from __future__ import annotations

import argparse
import posixpath
from pathlib import Path
from typing import Any

from bootstrap_query import index_objects, load_atlas
from graph_index import GraphIndex, ref_id, relation_predicate

TYPE_LABELS = {
    "implementation": "实现（Implementation）",
    "capability": "能力（Capability）",
    "standard": "标准 / 规范（Standard）",
    "scenario": "场景（Scenario）",
    "organization": "组织（Organization）",
    "map": "地图（Map）",
}

VALUE_LABELS = {
    "platform_service": "平台服务",
    "software": "软件",
    "library": "程序库",
    "tool": "工具",
    "service": "服务",
    "hardware": "硬件",
    "firmware": "固件",
    "reference_implementation": "参考实现",
    "self_hosted_platform": "自行部署完整平台",
    "self_hosted_runner": "自行部署执行器（Runner）",
    "format": "数据格式",
    "protocol": "协议",
    "specification": "规范",
    "standard": "标准",
    "api": "API",
    "profile": "配置档 / Profile",
    "interface": "接口",
    "device_class": "设备类别",
    "sense": "感知",
    "transport": "传输",
    "represent": "表达",
    "compute": "计算",
    "reason": "推理",
    "communicate": "通信",
    "coordinate": "协调",
    "act": "执行",
    "store": "存储",
    "identity_trust": "身份与信任",
    "govern": "治理",
    "mature": "成熟",
    "stable": "稳定",
    "draft": "草案",
    "published": "已发布",
    "open": "开放",
    "unknown": "未知",
    "not_required": "不要求",
}

RELATION_LABELS = {
    "alternative_to": "可替代于",
    "depends_on": "依赖",
    "uses": "使用",
    "implements": "实现",
    "extends": "扩展",
    "replaces": "替代",
    "supersedes": "取代",
    "compatible_with": "兼容",
    "incompatible_with": "不兼容",
    "bridges_to": "桥接到",
    "maps_to": "映射到",
    "encapsulates": "封装",
    "transports": "传输",
    "describes": "描述",
    "requires": "要求",
    "recommended_with": "建议与其配合",
    "governed_by": "由其治理",
    "implemented_by": "由其实现",
    "secures": "保护",
    "discovers": "发现",
    "identifies": "标识",
    "synchronizes": "同步",
    "provides": "提供",
    "inspired_by": "参考 / 受启发于",
}

RELATION_GROUPS = [
    ("能力与实现", {"provides", "implements", "implemented_by", "describes"}),
    (
        "替代与兼容",
        {"alternative_to", "compatible_with", "incompatible_with", "replaces", "supersedes"},
    ),
    (
        "依赖与使用",
        {"depends_on", "uses", "requires", "recommended_with", "extends", "encapsulates", "transports"},
    ),
    ("治理与基础设施", {"governed_by", "secures", "discovers", "identifies", "synchronizes"}),
    ("映射与桥接", {"bridges_to", "maps_to"}),
    ("参考与来源", {"inspired_by"}),
]

HUMAN_VIEW_TYPES = {"implementation", "capability", "standard"}


def human_value(value: Any) -> str:
    if value is True:
        return "是"
    if value is False:
        return "否"
    if value is None:
        return "未知"
    return VALUE_LABELS.get(str(value), str(value))


def display_name(obj: dict[str, Any] | None, fallback: str) -> str:
    if not obj:
        return fallback
    zh = obj.get("name_zh")
    en = obj.get("name_en")
    if isinstance(zh, str) and isinstance(en, str) and zh != en:
        return f"{zh}（{en}）"
    return str(zh or en or fallback)


def summary_of(obj: dict[str, Any]) -> str | None:
    value = obj.get("summary_zh") or obj.get("description_zh")
    return str(value).strip() if value else None


def output_path(obj: dict[str, Any]) -> str | None:
    source = obj.get("_source")
    if not isinstance(source, str) or not source.endswith(".yaml"):
        return None
    return source[:-5] + ".md"


def object_link(source_obj: dict[str, Any], target_obj: dict[str, Any]) -> str | None:
    source_path = output_path(source_obj)
    target_path = output_path(target_obj)
    if not source_path or not target_path:
        return None
    start = posixpath.dirname(source_path)
    return posixpath.relpath(target_path, start=start or ".")


def linked_name(source_obj: dict[str, Any], target_obj: dict[str, Any] | None, fallback: str) -> str:
    label = display_name(target_obj, fallback)
    if not target_obj:
        return label
    link = object_link(source_obj, target_obj)
    return f"[{label}]({link})" if link else label


def relationship_name(source_obj: dict[str, Any], target_obj: dict[str, Any] | None, fallback: str) -> str:
    if not target_obj or target_obj.get("type") not in HUMAN_VIEW_TYPES:
        return display_name(target_obj, fallback)
    return linked_name(source_obj, target_obj, fallback)


def relation_group(kind: str) -> str:
    for heading, kinds in RELATION_GROUPS:
        if kind in kinds:
            return heading
    return "其他关系"


def grouped_by_relation_kind(items: list[Any], kind_getter) -> list[tuple[str, list[Any]]]:
    buckets: dict[str, list[Any]] = {}
    for item in items:
        heading = relation_group(str(kind_getter(item)))
        buckets.setdefault(heading, []).append(item)
    order = [heading for heading, _ in RELATION_GROUPS] + ["其他关系"]
    return [(heading, buckets[heading]) for heading in order if heading in buckets]


def add_sources(lines: list[str], obj: dict[str, Any]) -> None:
    sources = obj.get("sources") or []
    if not sources:
        return
    lines += ["## 来源", ""]
    for source in sources:
        if not isinstance(source, dict):
            continue
        title = source.get("title") or source.get("url") or "来源"
        url = source.get("url")
        lines.append(f"- [{title}]({url})" if url else f"- {title}")
    lines.append("")


def add_capabilities(lines: list[str], obj: dict[str, Any], index: dict[str, dict[str, Any]]) -> None:
    capability_ids = obj.get("capabilities") or []
    if not capability_ids:
        return
    lines += ["## 它涉及什么能力？", ""]
    for capability_id in capability_ids:
        target = index.get(capability_id)
        lines.append(f"- {linked_name(obj, target, capability_id)} (`{capability_id}`)")
    lines.append("")


def common_header(obj: dict[str, Any]) -> list[str]:
    object_id = str(obj.get("id", "未命名对象"))
    lines = [f"# {display_name(obj, object_id)}", ""]
    summary = summary_of(obj)
    if summary:
        lines += [summary, ""]
    lines += ["## 基本信息", ""]
    lines.append(f"- **对象类型：** {TYPE_LABELS.get(str(obj.get('type')), str(obj.get('type', '未知')))}")
    lines.append(f"- **内部 ID：** `{object_id}`")
    if obj.get("status") is not None:
        lines.append(f"- **状态：** {human_value(obj.get('status'))}")
    if obj.get("maturity") is not None:
        lines.append(f"- **成熟度：** {human_value(obj.get('maturity'))}")
    return lines


def add_direct_relations(
    lines: list[str],
    obj: dict[str, Any],
    index: dict[str, dict[str, Any]],
    graph: GraphIndex,
) -> None:
    object_id = str(obj.get("id"))
    outgoing = [edge for edge in graph.forward(object_id) if edge.origin == "relation"]
    incoming = [edge for edge in graph.backlinks(object_id) if edge.origin == "relation"]
    if not outgoing and not incoming:
        return

    lines += ["## 直接关系", ""]
    all_edges = outgoing + incoming
    for group_heading, group_items in grouped_by_relation_kind(all_edges, lambda edge: edge.kind):
        lines += [f"### {group_heading}", ""]
        group_outgoing = [edge for edge in group_items if edge in outgoing]
        group_incoming = [edge for edge in group_items if edge in incoming]

        if group_outgoing:
            lines += ["**从本对象出发**", ""]
            for edge in sorted(group_outgoing, key=lambda item: (item.kind, item.target_id)):
                target = index.get(edge.target_id)
                label = RELATION_LABELS.get(edge.kind, edge.kind)
                lines.append(f"- **{label}** → {relationship_name(obj, target, edge.target_id)}")
            lines.append("")

        if group_incoming:
            lines += ["**指向本对象**", ""]
            for edge in sorted(group_incoming, key=lambda item: (item.kind, item.source_id)):
                source = index.get(edge.source_id)
                label = RELATION_LABELS.get(edge.kind, edge.kind)
                lines.append(f"- {relationship_name(obj, source, edge.source_id)} → **{label}** → 本对象")
            lines.append("")


def render_implementation(
    obj: dict[str, Any],
    index: dict[str, dict[str, Any]],
    graph: GraphIndex | None = None,
) -> str:
    lines = common_header(obj)
    lines.append(f"- **实现类别：** {human_value(obj.get('kind'))}")
    lines.append(f"- **开源：** {human_value(obj.get('open_source'))}")
    lines.append(f"- **可自行部署：** {human_value(obj.get('self_hostable'))}")
    if obj.get("license_expression"):
        lines.append(f"- **许可证：** `{obj['license_expression']}`")
    lines.append("")
    add_capabilities(lines, obj, index)
    if graph is not None:
        add_direct_relations(lines, obj, index, graph)

    models = obj.get("deployment_models") or []
    if models:
        lines += ["## 部署方式", ""]
        lines.extend(f"- {human_value(item)}" for item in models)
        lines.append("")

    notes = obj.get("notes_zh") or []
    if notes:
        lines += ["## 需要注意", ""]
        lines.extend(f"- {note}" for note in notes)
        lines.append("")
    add_sources(lines, obj)
    return finish(lines)


def add_capability_backlinks(
    lines: list[str],
    obj: dict[str, Any],
    index: dict[str, dict[str, Any]],
    graph: GraphIndex,
) -> None:
    capability_id = str(obj.get("id"))
    referenced_by = []
    for edge in graph.backlinks(capability_id):
        if edge.origin != "object" or edge.field != "capabilities":
            continue
        source = index.get(edge.source_id)
        if source:
            referenced_by.append(source)

    groups = [
        ("## 相关标准 / 规范", "standard"),
        ("## 哪些实现提供这个能力？", "implementation"),
    ]
    for heading, object_type in groups:
        items = [item for item in referenced_by if item.get("type") == object_type]
        if not items:
            continue
        lines += [heading, ""]
        for item in sorted(items, key=lambda candidate: display_name(candidate, str(candidate.get("id")))):
            item_id = str(item.get("id"))
            lines.append(f"- {linked_name(obj, item, item_id)}")
        lines.append("")

    relations = graph.relation_objects_for_capability(capability_id)
    if relations:
        lines += ["## 这个能力下已记录的关系", ""]
        for group_heading, group_relations in grouped_by_relation_kind(
            relations, lambda relation: relation_predicate(relation) or "related_to"
        ):
            lines += [f"### {group_heading}", ""]
            for relation in sorted(group_relations, key=lambda item: str(item.get("id"))):
                source_id = ref_id(relation.get("source")) or "未知对象"
                target_id = ref_id(relation.get("target")) or "未知对象"
                source = index.get(source_id)
                target = index.get(target_id)
                predicate = relation_predicate(relation) or "related_to"
                predicate_label = RELATION_LABELS.get(predicate, predicate)
                lines.append(
                    f"- {relationship_name(obj, source, source_id)} **{predicate_label}** "
                    f"{relationship_name(obj, target, target_id)}"
                )
            lines.append("")


def render_capability(
    obj: dict[str, Any],
    index: dict[str, dict[str, Any]],
    graph: GraphIndex | None = None,
) -> str:
    lines = common_header(obj)
    if obj.get("category") is not None:
        lines.append(f"- **能力类别：** {human_value(obj.get('category'))}")
    lines.append("")

    if graph is not None:
        add_capability_backlinks(lines, obj, index, graph)
    else:
        capability_id = obj.get("id")
        implementations = [
            candidate
            for candidate in index.values()
            if candidate.get("type") == "implementation"
            and capability_id in (candidate.get("capabilities") or [])
        ]
        if implementations:
            lines += ["## 哪些实现提供这个能力？", ""]
            for implementation in sorted(implementations, key=lambda item: str(item.get("id"))):
                implementation_id = str(implementation.get("id"))
                lines.append(f"- {linked_name(obj, implementation, implementation_id)}")
            lines.append("")
    return finish(lines)


def render_standard(
    obj: dict[str, Any],
    index: dict[str, dict[str, Any]],
    graph: GraphIndex | None = None,
) -> str:
    lines = common_header(obj)
    if obj.get("kind") is not None:
        lines.append(f"- **标准类别：** {human_value(obj.get('kind'))}")
    if obj.get("official_name"):
        lines.append(f"- **官方名称：** {obj['official_name']}")
    if obj.get("official_url"):
        lines.append(f"- **官方网站：** {obj['official_url']}")
    lines.append("")
    add_capabilities(lines, obj, index)
    if graph is not None:
        add_direct_relations(lines, obj, index, graph)

    openness = obj.get("openness")
    if isinstance(openness, dict) and openness:
        labels = {
            "specification_access": "规范访问",
            "governance": "治理开放性",
            "patent_terms": "专利条款",
            "certification": "认证要求",
        }
        lines += ["## 开放性记录", ""]
        for key, value in openness.items():
            lines.append(f"- **{labels.get(key, key)}：** {human_value(value)}")
        lines.append("")

    versions = obj.get("versions") or []
    if versions:
        lines += ["## 版本", ""]
        for version in versions:
            if isinstance(version, dict):
                text = str(version.get("version", "未知版本"))
                if version.get("date"):
                    text += f" · {version['date']}"
                if version.get("status"):
                    text += f" · {human_value(version['status'])}"
                lines.append(f"- {text}")
        lines.append("")
    add_sources(lines, obj)
    return finish(lines)


def finish(lines: list[str]) -> str:
    lines += [
        "---",
        "",
        "> 本页由 InteropAtlas 结构化数据自动生成。YAML 是事实源，本页只是人类可读视图。",
        "",
    ]
    return "\n".join(lines)


def render_object(
    obj: dict[str, Any],
    index: dict[str, dict[str, Any]],
    graph: GraphIndex | None = None,
) -> str:
    object_type = obj.get("type")
    if object_type == "capability":
        return render_capability(obj, index, graph)
    if object_type == "implementation":
        return render_implementation(obj, index, graph)
    if object_type == "standard":
        return render_standard(obj, index, graph)
    raise ValueError(f"renderer does not support object type yet: {object_type}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("object_id")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    objects, relations = load_atlas(args.root)
    index = index_objects(objects)
    graph = GraphIndex(index, relations)
    obj = index.get(args.object_id)
    if not obj:
        raise SystemExit(f"unknown object id: {args.object_id}")

    rendered = render_object(obj, index, graph)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
