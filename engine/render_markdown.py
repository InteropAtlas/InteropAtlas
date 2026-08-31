#!/usr/bin/env python3
"""Render a single InteropAtlas object into human-readable Chinese Markdown."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from bootstrap_query import index_objects, load_atlas


def yes_no(value: Any) -> str:
    if value is True:
        return "是"
    if value is False:
        return "否"
    return "未知"


def display_name(obj: dict[str, Any] | None, fallback: str) -> str:
    if not obj:
        return fallback
    zh = obj.get("name_zh")
    en = obj.get("name_en")
    if isinstance(zh, str) and isinstance(en, str) and zh != en:
        return f"{zh}（{en}）"
    return str(zh or en or fallback)


def render_implementation(obj: dict[str, Any], index: dict[str, dict[str, Any]]) -> str:
    title = display_name(obj, str(obj.get("id", "未命名对象")))
    lines = [f"# {title}", ""]

    summary = obj.get("summary_zh") or obj.get("description_zh")
    if summary:
        lines += [str(summary).strip(), ""]

    lines += ["## 基本信息", ""]
    lines.append(f"- **对象类型：** 实现（Implementation）")
    lines.append(f"- **实现类别：** `{obj.get('kind', 'unknown')}`")
    lines.append(f"- **开源：** {yes_no(obj.get('open_source'))}")
    lines.append(f"- **可自行部署：** {yes_no(obj.get('self_hostable'))}")
    if obj.get("license_expression"):
        lines.append(f"- **许可证：** `{obj['license_expression']}`")
    lines.append("")

    capability_ids = obj.get("capabilities") or []
    if capability_ids:
        lines += ["## 它解决什么能力？", ""]
        for capability_id in capability_ids:
            target = index.get(capability_id)
            lines.append(f"- {display_name(target, capability_id)} (`{capability_id}`)")
        lines.append("")

    deployment_models = obj.get("deployment_models") or []
    if deployment_models:
        lines += ["## 部署方式", ""]
        for item in deployment_models:
            lines.append(f"- `{item}`")
        lines.append("")

    notes = obj.get("notes_zh") or []
    if notes:
        lines += ["## 需要注意", ""]
        for note in notes:
            lines.append(f"- {note}")
        lines.append("")

    sources = obj.get("sources") or []
    if sources:
        lines += ["## 来源", ""]
        for source in sources:
            if not isinstance(source, dict):
                continue
            title_text = source.get("title") or source.get("url") or "来源"
            url = source.get("url")
            if url:
                lines.append(f"- [{title_text}]({url})")
            else:
                lines.append(f"- {title_text}")
        lines.append("")

    lines += [
        "---",
        "",
        "> 本页由 InteropAtlas 结构化数据自动生成。YAML 是事实源，本页只是人类可读视图。",
        "",
    ]
    return "\n".join(lines)


def render_object(obj: dict[str, Any], index: dict[str, dict[str, Any]]) -> str:
    if obj.get("type") == "implementation":
        return render_implementation(obj, index)
    raise ValueError(f"renderer does not support object type yet: {obj.get('type')}")


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
