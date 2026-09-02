#!/usr/bin/env python3
"""Legacy/v0 compatibility adapter for the current InteropAtlas Human Route.

This module owns semantic compatibility concerns: Legacy/v0 Human View
selection, representative Organization projection and homepage grouping.
Shared page-shell, breadcrumb, route-link and Human-label behavior lives in
permanent Human Route modules.
"""

from __future__ import annotations

import argparse
import html
from collections import defaultdict
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


def build_homepage(rendered: list[tuple[dict, Path]]) -> str:
    capabilities = [(obj, path) for obj, path in rendered if semantic_site_view_type(obj) == "capability"]
    standards = [(obj, path) for obj, path in rendered if semantic_site_view_type(obj) == "standard"]
    implementations = [(obj, path) for obj, path in rendered if semantic_site_view_type(obj) == "implementation"]
    organizations = [(obj, path) for obj, path in rendered if semantic_site_view_type(obj) == "organization"]
    sections = [
        "<h1>InteropAtlas</h1>",
        "<p>探索互操作方案空间中的能力、标准、规范、实现、组织、关系与证据。你可以先从要完成的任务进入，也可以继续按能力浏览。</p>",
        f'<p class="muted">当前可浏览：{len(capabilities)} 个能力 · {len(standards)} 个标准 / 规范 · {len(implementations)} 个实现 · {len(organizations)} 个组织</p>',
        '<section aria-labelledby="task-entry-heading">',
        '<h2 id="task-entry-heading">你想做什么？</h2>',
        '<p>这些入口只连接当前已经实现的 Human View 能力，不代表所有能力都已通用化。</p>',
        '<div class="grid task-entry-grid">',
        '<article class="card"><h3><a href="search.html">查找对象</a></h3><p>按名称、关键词或稳定 ID 查找当前已发布对象。</p></article>',
        '<article class="card"><h3><a href="objects/automated_build_deployment.html">理解一个对象</a></h3><p>从代表性 Resource Page 查看对象身份、基本信息和相关对象。</p></article>',
        '<article class="card"><h3><a href="compare/automated_build_deployment--forgejo_actions--github_actions.html">比较候选方案</a></h3><p>查看当前已实现的 Forgejo Actions 与 GitHub Actions 代表性比较；尚不是全站任意对象比较。</p></article>',
        '<article class="card"><h3><a href="objects/forgejo_actions.html#evidence">验证来源</a></h3><p>查看代表性页面中 Canonical 来源与 InteropAtlas 说明 / 评估的明确分工。</p></article>',
        '<article class="card"><h3><a href="objects/forgejo_actions.html#local-map">探索关系</a></h3><p>从代表性对象的 Local Map 探索局部关系；尚不是大型 Graph Explorer。</p></article>',
        '</div></section>',
        "<h2>按能力浏览</h2>",
        "<p>Capability-first 仍是一个有效入口。同一个标准或实现可以连接到多个能力，不把 Atlas 固定成唯一目录树。</p>",
    ]
    categories: dict[str, list[tuple[dict, Path]]] = defaultdict(list)
    for obj, path in capabilities:
        categories[str(obj.get("category") or "uncategorized")].append((obj, path))
    sections.append('<div class="category-grid">')
    for category, items in sorted(categories.items(), key=lambda item: human_value(item[0])):
        label = "未分类" if category == "uncategorized" else human_value(category)
        sections.append(f'<section class="category-card" id="{html.escape(legacy_site.category_anchor(category))}">')
        sections.append(f'<h3>{html.escape(label)}</h3><div class="count">{len(items)} 个能力</div><ul>')
        for obj, path in sorted(items, key=lambda item: display_name(item[0], str(item[0].get("id")))):
            name = html.escape(display_name(obj, str(obj.get("id"))))
            sections.append(f'<li><a href="{path.as_posix()}">{name}</a></li>')
        sections.append('</ul></section>')
    sections.append('</div>')
    sections += ["<h2>其他入口</h2>", '<p class="muted">这些仍是辅助浏览入口；它们不代表 Atlas 存在唯一 Canonical 分类树。</p>']
    for heading, items in (("标准与规范", standards), ("实现", implementations), ("组织", organizations)):
        sections.append(f'<details><summary>{heading} <span class="count">({len(items)})</span></summary><div class="grid">')
        for obj, path in sorted(items, key=lambda item: display_name(item[0], str(item[0].get("id")))):
            sections.append(legacy_site.object_card(obj, path))
        sections.append('</div></details>')
    return "".join(sections)


def install_compatibility_hooks() -> None:
    """Install only Legacy/v0 semantic compatibility hooks."""
    human_markdown.semantic_view_type = semantic_site_view_type
    legacy_site.object_html_href = object_html_href
    legacy_site.breadcrumb_for = breadcrumb_for
    legacy_site.build_homepage = build_homepage
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
    (output / "index.html").write_text(page_shell("首页", build_homepage(rendered)), encoding="utf-8")
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
