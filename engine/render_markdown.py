#!/usr/bin/env python3
"""Render InteropAtlas objects into human-readable Chinese Markdown views."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from bootstrap_query import index_objects, load_atlas

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
        lines.append(f"- {display_name(target, capability_id)} (`{capability_id}`)")
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


def render_implementation(obj: dict[str, Any], index: dict[str, dict[str, Any]]) -> str:
    lines = common_header(obj)
    lines.append(f"- **实现类别：** {human_value(obj.get('kind'))}")
    lines.append(f"- **开源：** {human_value(obj.get('open_source'))}")
    lines.append(f"- **可自行部署：** {human_value(obj.get('self_hostable'))}")
    if obj.get("license_expression"):
        lines.append(f"- **许可证：** `{obj['license_expression']}`")
    lines.append("")
    add_capabilities(lines, obj, index)

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


def render_capability(obj: dict[str, Any], _index: dict[str, dict[str, Any]]) -> str:
    lines = common_header(obj)
    if obj.get("category") is not None:
        lines.append(f"- **能力类别：** {human_value(obj.get('category'))}")
    lines.append("")
    return finish(lines)


def render_standard(obj: dict[str, Any], index: dict[str, dict[str, Any]]) -> str:
    lines = common_header(obj)
    if obj.get("kind") is not None:
        lines.append(f"- **标准类别：** {human_value(obj.get('kind'))}")
    if obj.get("official_name"):
        lines.append(f"- **官方名称：** {obj['official_name']}")
    if obj.get("official_url"):
        lines.append(f"- **官方网站：** {obj['official_url']}")
    lines.append("")
    add_capabilities(lines, obj, index)

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


def render_object(obj: dict[str, Any], index: dict[str, dict[str, Any]]) -> str:
    renderers = {
        "implementation": render_implementation,
        "capability": render_capability,
        "standard": render_standard,
    }
    renderer = renderers.get(obj.get("type"))
    if not renderer:
        raise ValueError(f"renderer does not support object type yet: {obj.get('type')}")
    return renderer(obj, index)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("object_id")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    objects, _relations = load_atlas(args.root)
    index = index_objects(objects)
    obj = index.get(args.object_id)
    if not obj:
        raise SystemExit(f"unknown object id: {args.object_id}")

    rendered = render_object(obj, index)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
