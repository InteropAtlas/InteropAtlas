#!/usr/bin/env python3
"""Semantic compatibility adapter for the current InteropAtlas static site.

The existing site UI remains intentionally unchanged while object selection,
breadcrumbs, homepage grouping, and links become Legacy/v0 dual-read. This
keeps the Human Route stable during the representative migration pilot without
mixing ontology migration with a visual redesign.
"""

from __future__ import annotations

import argparse
import html
from collections import defaultdict
from pathlib import Path

import render_site as legacy_site
from bootstrap_query import index_objects, load_atlas
from graph_index import GraphIndex
from render_markdown import display_name, human_value, output_path, render_object, semantic_view_type


SUPPORTED_VIEW_TYPES = {"capability", "standard", "implementation"}


def breadcrumb_for(obj: dict, prefix: str) -> str:
    name = html.escape(display_name(obj, str(obj.get("id"))))
    current = f'<span aria-current="page">{name}</span>'
    view_type = semantic_view_type(obj)
    home = f'<a href="{prefix}index.html">首页</a>'
    separator = '<span aria-hidden="true">›</span>'
    if view_type == "capability":
        category = str(obj.get("category") or "uncategorized")
        label = "未分类" if category == "uncategorized" else human_value(category)
        category_link = (
            f'<a href="{prefix}index.html#{legacy_site.category_anchor(category)}">'
            f'{html.escape(label)}</a>'
        )
        return f'{home}{separator}<span>能力</span>{separator}{category_link}{separator}{current}'
    labels = {"standard": "标准与规范", "implementation": "实现"}
    label = labels.get(str(view_type), str(obj.get("type") or "对象"))
    return f'{home}{separator}<span>{html.escape(label)}</span>{separator}{current}'


def object_html_href(source_obj: dict, target_obj: dict | None) -> str | None:
    if not target_obj or semantic_view_type(target_obj) not in SUPPORTED_VIEW_TYPES:
        return None
    link = legacy_site.object_link(source_obj, target_obj)
    if not link:
        return None
    return str(Path(link).with_suffix(".html")).replace("\\", "/")


def build_homepage(rendered: list[tuple[dict, Path]]) -> str:
    capabilities = [(obj, path) for obj, path in rendered if semantic_view_type(obj) == "capability"]
    standards = [(obj, path) for obj, path in rendered if semantic_view_type(obj) == "standard"]
    implementations = [(obj, path) for obj, path in rendered if semantic_view_type(obj) == "implementation"]

    sections = [
        "<h1>InteropAtlas</h1>",
        "<p>从“能力”开始探索开放标准、规范与实现。当前网站仍处于早期实验阶段，导航结构会随着 Atlas 数据和关系逐步演进。</p>",
        f'<p class="muted">当前可浏览：{len(capabilities)} 个能力 · {len(standards)} 个标准 / 规范 · {len(implementations)} 个实现</p>',
        "<h2>从能力开始</h2>",
        "<p>能力是当前第一版主入口。同一个标准或实现可以连接到多个能力，不把 Atlas 固定成唯一目录树。</p>",
    ]

    categories: dict[str, list[tuple[dict, Path]]] = defaultdict(list)
    for obj, path in capabilities:
        category = str(obj.get("category") or "uncategorized")
        categories[category].append((obj, path))

    sections.append('<div class="category-grid">')
    for category, items in sorted(categories.items(), key=lambda item: human_value(item[0])):
        label = "未分类" if category == "uncategorized" else human_value(category)
        sections.append(
            f'<section class="category-card" id="{html.escape(legacy_site.category_anchor(category))}">'
        )
        sections.append(f'<h3>{html.escape(label)}</h3><div class="count">{len(items)} 个能力</div><ul>')
        for obj, path in sorted(items, key=lambda item: display_name(item[0], str(item[0].get("id")))):
            name = html.escape(display_name(obj, str(obj.get("id"))))
            sections.append(f'<li><a href="{path.as_posix()}">{name}</a></li>')
        sections.append('</ul></section>')
    sections.append('</div>')

    sections += [
        "<h2>其他入口</h2>",
        "<p class=\"muted\">这些仍是对象类型入口，先作为辅助浏览方式保留；后续会逐步增加领域、系统层级、组织、场景和动态地图等视角。</p>",
    ]
    for heading, items in (("标准与规范", standards), ("实现", implementations)):
        sections.append(
            f'<details><summary>{heading} <span class="count">({len(items)})</span></summary><div class="grid">'
        )
        for obj, path in sorted(items, key=lambda item: display_name(item[0], str(item[0].get("id")))):
            sections.append(legacy_site.object_card(obj, path))
        sections.append('</div></details>')

    return "".join(sections)


def install_compatibility_hooks() -> None:
    """Make existing map/link helpers use semantic view selection too."""

    legacy_site.object_html_href = object_html_href
    legacy_site.breadcrumb_for = breadcrumb_for
    legacy_site.build_homepage = build_homepage


def build(root: Path, output: Path) -> dict[str, int]:
    install_compatibility_hooks()
    objects, relations = load_atlas(root)
    index = index_objects(objects)
    graph = GraphIndex(index, relations)
    rendered: list[tuple[dict, Path]] = []

    for obj in objects:
        if semantic_view_type(obj) not in SUPPORTED_VIEW_TYPES:
            continue
        md_path = output_path(obj)
        if not md_path:
            continue
        html_path = Path(md_path).with_suffix(".html")
        target = output / html_path
        target.parent.mkdir(parents=True, exist_ok=True)
        content = legacy_site.markdown_to_html(render_object(obj, index, graph))
        content = legacy_site.inject_local_map(content, legacy_site.build_local_map(obj, index, graph))
        prefix = "../" * len(html_path.parent.parts)
        target.write_text(
            legacy_site.page_shell(
                display_name(obj, str(obj.get("id"))),
                content,
                prefix,
                breadcrumb_for(obj, prefix),
            ),
            encoding="utf-8",
        )
        rendered.append((obj, html_path))

    output.mkdir(parents=True, exist_ok=True)
    (output / "index.html").write_text(
        legacy_site.page_shell("首页", build_homepage(rendered)), encoding="utf-8"
    )
    (output / ".nojekyll").write_text("", encoding="utf-8")
    return {
        "objects_loaded": len(objects),
        "pages_rendered": len(rendered),
        "graph_edges": len(graph.edges),
        "reference_issues": len(graph.issues),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path, default=Path("build/site"))
    args = parser.parse_args()
    result = build(args.root, args.output)
    print(
        f"Rendered {result['pages_rendered']} pages from {result['objects_loaded']} objects "
        f"with {result['graph_edges']} graph edges and {result['reference_issues']} reference issues "
        f"into {args.output}"
    )


if __name__ == "__main__":
    main()
