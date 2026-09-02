#!/usr/bin/env python3
"""Legacy/v0 compatibility adapter for the current InteropAtlas Human Route.

This module owns semantic compatibility concerns: Legacy/v0 Human View
selection, representative Organization projection and homepage grouping.
Shared page-shell, breadcrumb, route-link and Human-label behavior lives in
permanent Human Route modules.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import human_route_compare as human_compare
import human_route_runtime as human_route
import human_route_search as human_search
import human_route_shell as human_shell
import render_markdown as human_markdown
import render_site as legacy_site
from bootstrap_query import index_objects, load_atlas
from graph_index import GraphIndex
from kind_registry import has_profile, load_kind_registry
from render_markdown import display_name, human_value, output_path, render_object, semantic_view_type

_BASE_SEMANTIC_VIEW_TYPE = semantic_view_type
_KIND_REGISTRY = load_kind_registry()
SUPPORTED_VIEW_TYPES = {"capability", "standard", "implementation", "organization"}


def semantic_site_view_type(obj: dict | None) -> str | None:
    """Extend the current Human View projection with the v0 Organization profile."""
    view_type = _BASE_SEMANTIC_VIEW_TYPE(obj)
    if view_type is not None:
        return view_type
    if obj and has_profile(obj, "organization", _KIND_REGISTRY):
        return "organization"
    return None


def breadcrumb_for(obj: dict, prefix: str) -> str:
    """Compatibility hook delegating stable breadcrumb behavior to Human Route."""
    return human_shell.breadcrumb_for(
        obj,
        prefix,
        semantic_site_view_type,
        display_name,
        human_value,
        legacy_site.category_anchor,
    )


def object_html_href(source_obj: dict, target_obj: dict | None) -> str | None:
    """Compatibility hook delegating stable Human route links to Human Route."""
    return human_shell.object_html_href(
        source_obj,
        target_obj,
        semantic_site_view_type,
        SUPPORTED_VIEW_TYPES,
        legacy_site.object_link,
    )


def page_shell(title: str, body: str, prefix: str = "", breadcrumb: str | None = None) -> str:
    """Shared Human Route shell entry point used by Resource/Search/Compare pages."""
    return human_shell.page_shell(legacy_site, title, body, prefix, breadcrumb)


def render_organization(obj: dict, index: dict[str, dict], graph: GraphIndex) -> str:
    """Render the representative Agent/Organization Resource Page contract."""
    object_id = str(obj.get("id", "未命名对象"))
    lines = [f"# {display_name(obj, object_id)}", ""]
    summary = human_markdown.summary_of(obj)
    if summary:
        lines += [summary, ""]
    else:
        org_kind = human_value(obj.get("organization_kind") or "organization")
        official = str(obj.get("official_name") or obj.get("name_en") or obj.get("name_zh") or object_id)
        lines += [f"{official} 是 InteropAtlas 当前记录的{org_kind}组织对象。", ""]
    lines += ["## 基本信息", ""]
    lines.append("- **对象类型：** 组织（Organization）")
    lines.append(f"- **内部 ID：** `{object_id}`")
    if obj.get("official_name"):
        lines.append(f"- **官方名称：** {obj['official_name']}")
    if obj.get("organization_kind"):
        lines.append(f"- **组织类别：** {human_value(obj['organization_kind'])}")
    if obj.get("jurisdiction"):
        lines.append(f"- **活动范围 / 管辖：** {human_value(obj['jurisdiction'])}")
    if obj.get("official_url"):
        lines.append(f"- **官方网站：** {obj['official_url']}")
    lines.append("")
    domains = obj.get("domains") or []
    if domains:
        lines += ["## 相关领域", ""]
        lines.extend(f"- {human_value(item)}" for item in domains)
        lines.append("")
    human_markdown.add_one_hop_neighbors(lines, obj, index, graph)
    human_markdown.add_direct_relations(lines, obj, index, graph)
    human_markdown.add_sources(lines, obj)
    return human_markdown.finish(lines)


def render_human_object(obj: dict, index: dict[str, dict], graph: GraphIndex) -> str:
    if semantic_site_view_type(obj) == "organization":
        return render_organization(obj, index, graph)
    return render_object(obj, index, graph)


def build_homepage(objects: list[dict], relations: list[dict], rendered: list[tuple[dict, Path]]) -> str:
    """Keep the provisional Homepage neutral: one search action plus Atlas state."""
    return "".join(
        [
            "<h1>InteropAtlas</h1>",
            "<p>开放的互操作知识地图。当前首页只提供搜索与地图状态预览；更完整的导航方式仍在探索中。</p>",
            '<section class="homepage-search" aria-labelledby="homepage-search-heading">',
            '<h2 id="homepage-search-heading">搜索 InteropAtlas</h2>',
            '<p>从已经收录的标准、规范、能力、实现、组织与相关知识开始。</p>',
            '<p><a class="button" href="search.html">开始搜索</a></p>',
            '</section>',
            '<section class="atlas-status" aria-labelledby="atlas-status-heading">',
            '<h2 id="atlas-status-heading">当前地图状态</h2>',
            '<div class="grid">',
            f'<div class="card"><strong>{len(objects)}</strong><p>已收录对象</p></div>',
            f'<div class="card"><strong>{len(relations)}</strong><p>已记录关系</p></div>',
            f'<div class="card"><strong>{len(rendered)}</strong><p>当前可阅读页面</p></div>',
            '</div>',
            '<p class="muted">这些数字由当前 Canonical state 与 Human Route 构建结果实时派生，不代表覆盖已经完整。</p>',
            '</section>',
        ]
    )


def install_compatibility_hooks() -> None:
    """Install only Legacy/v0 semantic compatibility hooks."""
    human_markdown.semantic_view_type = semantic_site_view_type
    legacy_site.object_html_href = object_html_href
    legacy_site.breadcrumb_for = breadcrumb_for
    human_route.install_runtime_contract(legacy_site)


def build(root: Path, output: Path) -> dict[str, int]:
    install_compatibility_hooks()
    objects, relations = load_atlas(root)
    index = index_objects(objects)
    graph = GraphIndex(index, relations)
    rendered: list[tuple[dict, Path]] = []
    for obj in objects:
        if semantic_site_view_type(obj) not in SUPPORTED_VIEW_TYPES:
            continue
        md_path = output_path(obj)
        if not md_path:
            continue
        html_path = Path(md_path).with_suffix(".html")
        target = output / html_path
        target.parent.mkdir(parents=True, exist_ok=True)
        content = legacy_site.markdown_to_html(render_human_object(obj, index, graph))
        content = human_route.add_resource_fragment_targets(content)
        content = human_compare.inject_compare_entry(content, obj, index)
        local_map = human_route.build_local_map(legacy_site, obj, index, graph, semantic_site_view_type)
        content = legacy_site.inject_local_map(content, local_map)
        content = human_route.inject_resource_task_navigation(content)
        prefix = "../" * len(html_path.parent.parts)
        target.write_text(
            page_shell(display_name(obj, str(obj.get("id"))), content, prefix, breadcrumb_for(obj, prefix)),
            encoding="utf-8",
        )
        rendered.append((obj, html_path))
    output.mkdir(parents=True, exist_ok=True)
    homepage = build_homepage(objects, relations, rendered)
    (output / "index.html").write_text(page_shell("首页", homepage), encoding="utf-8")
    search_records = human_search.build_search_artifacts(
        output, rendered, page_shell, display_name, human_markdown.summary_of,
        lambda obj: human_route.human_object_type_label(obj, semantic_site_view_type),
    )
    human_compare.build_compare_artifact(output, index, relations, page_shell)
    (output / ".nojekyll").write_text("", encoding="utf-8")
    return {
        "objects_loaded": len(objects), "pages_rendered": len(rendered),
        "search_records": search_records, "compare_pages": 1,
        "graph_edges": len(graph.edges), "reference_issues": len(graph.issues),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path, default=Path("build/site"))
    args = parser.parse_args()
    result = build(args.root, args.output)
    print(
        f"Rendered {result['pages_rendered']} pages from {result['objects_loaded']} objects, "
        f"indexed {result['search_records']} Human resources, built {result['compare_pages']} Compare view, "
        f"with {result['graph_edges']} graph edges and {result['reference_issues']} reference issues into {args.output}"
    )


if __name__ == "__main__":
    main()
