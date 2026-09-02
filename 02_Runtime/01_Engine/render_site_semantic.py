#!/usr/bin/env python3
"""Semantic compatibility adapter for the current InteropAtlas static site.

The existing site UI remains intentionally stable while object selection,
breadcrumbs, homepage grouping, and links become Legacy/v0 dual-read. During
Gate B this transitional adapter also carries bounded Human Interface
conformance hooks and the representative four-family Resource Page slice.
These hooks should move into the final Human Route implementation during the
post-Gate conformance refactor.
"""

from __future__ import annotations

import argparse
import html
from collections import defaultdict
from pathlib import Path

import render_markdown as human_markdown
import render_site as legacy_site
from bootstrap_query import index_objects, load_atlas
from graph_index import GraphIndex
from kind_registry import has_profile, load_kind_registry
from render_markdown import display_name, human_value, output_path, render_object, semantic_view_type


_BASE_SEMANTIC_VIEW_TYPE = semantic_view_type
_KIND_REGISTRY = load_kind_registry()
SUPPORTED_VIEW_TYPES = {"capability", "standard", "implementation", "organization"}

INTERACTION_CONFORMANCE_STYLE = """
.map-status{min-height:1.4em;margin:10px 0 14px;color:var(--muted);font-size:.9em}
.map-status.is-error{color:var(--fg);font-weight:600}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:3px solid var(--link);outline-offset:2px}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto!important}
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
}
"""


def semantic_site_view_type(obj: dict | None) -> str | None:
    """Extend the current Human View projection with the v0 Organization profile."""

    view_type = _BASE_SEMANTIC_VIEW_TYPE(obj)
    if view_type is not None:
        return view_type
    if obj and has_profile(obj, "organization", _KIND_REGISTRY):
        return "organization"
    return None


def _replace_once(source: str, old: str, new: str, label: str) -> str:
    if old not in source:
        raise RuntimeError(f"Human Interface compatibility hook marker missing: {label}")
    return source.replace(old, new, 1)


def interaction_conformance_script(source: str) -> str:
    """Patch the transitional Local Map script with bounded Gate B behavior."""

    source = _replace_once(
        source,
        "<script>\n(function(){\n  function setActive",
        """<script>
(function(){
  function ensureStatus(section){
    let status=section.querySelector('.map-status');
    if(status)return status;
    status=document.createElement('div');
    status.className='map-status';
    status.setAttribute('role','status');
    status.setAttribute('aria-live','polite');
    status.setAttribute('aria-atomic','true');
    const controls=section.querySelector('.map-controls');
    if(controls)controls.after(status);else section.prepend(status);
    return status;
  }
  function setStatus(section,message,isError){
    const status=ensureStatus(section);
    status.textContent=message||'';
    status.classList.toggle('is-error',Boolean(isError));
  }
  function setActive""",
        "status helper insertion",
    )
    source = _replace_once(
        source,
        "    section.classList.add('map-loading');\n    const originalText=trigger.textContent;",
        "    section.classList.add('map-loading');\n    setStatus(section,'正在加载局部地图…',false);\n    const originalText=trigger.textContent;",
        "recenter loading status",
    )
    source = _replace_once(
        source,
        "      section.replaceWith(replacement);\n      apply(replacement);\n      replacement.scrollIntoView({behavior:'smooth',block:'start'});",
        """      section.replaceWith(replacement);
      apply(replacement);
      setStatus(replacement,'地图中心已更新。',false);
      const reduceMotion=matchMedia('(prefers-reduced-motion: reduce)').matches;
      replacement.scrollIntoView({behavior:reduceMotion?'auto':'smooth',block:'start'});""",
        "recenter success and reduced motion",
    )
    source = _replace_once(
        source,
        "      trigger.textContent=originalText;\n      trigger.disabled=true;\n      trigger.title='局部地图载入失败；对象详情仍可通过标题链接打开';",
        """      trigger.textContent=originalText;
      trigger.disabled=false;
      trigger.title='局部地图载入失败；对象详情仍可通过标题链接打开';
      setStatus(section,'局部地图载入失败；可以重试，或通过对象标题链接打开详情。',true);""",
        "recenter failure feedback",
    )
    source = _replace_once(
        source,
        "  addEventListener('DOMContentLoaded',function(){document.querySelectorAll('.local-map').forEach(apply);});",
        """  addEventListener('DOMContentLoaded',function(){
    document.querySelectorAll('.local-map').forEach(function(section){ensureStatus(section);apply(section);});
  });""",
        "status initialization",
    )
    return source


def breadcrumb_for(obj: dict, prefix: str) -> str:
    name = html.escape(display_name(obj, str(obj.get("id"))))
    current = f'<span aria-current="page">{name}</span>'
    view_type = semantic_site_view_type(obj)
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
    labels = {"standard": "标准与规范", "implementation": "实现", "organization": "组织"}
    label = labels.get(str(view_type), str(obj.get("type") or "对象"))
    return f'{home}{separator}<span>{html.escape(label)}</span>{separator}{current}'


def object_html_href(source_obj: dict, target_obj: dict | None) -> str | None:
    if not target_obj or semantic_site_view_type(target_obj) not in SUPPORTED_VIEW_TYPES:
        return None
    link = legacy_site.object_link(source_obj, target_obj)
    if not link:
        return None
    return str(Path(link).with_suffix(".html")).replace("\\", "/")


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
        "<p>从“能力”开始探索开放标准、规范与实现。当前网站仍处于早期实验阶段，导航结构会随着 Atlas 数据和关系逐步演进。</p>",
        f'<p class="muted">当前可浏览：{len(capabilities)} 个能力 · {len(standards)} 个标准 / 规范 · {len(implementations)} 个实现 · {len(organizations)} 个组织</p>',
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
        "<p class=\"muted\">这些仍是辅助浏览入口；它们不代表 Atlas 存在唯一 Canonical 分类树。</p>",
    ]
    for heading, items in (
        ("标准与规范", standards),
        ("实现", implementations),
        ("组织", organizations),
    ):
        sections.append(
            f'<details><summary>{heading} <span class="count">({len(items)})</span></summary><div class="grid">'
        )
        for obj, path in sorted(items, key=lambda item: display_name(item[0], str(item[0].get("id")))):
            sections.append(legacy_site.object_card(obj, path))
        sections.append('</div></details>')

    return "".join(sections)


def install_compatibility_hooks() -> None:
    """Install semantic and bounded Human Interface compatibility hooks."""

    # Let shared relation rendering recognize Organization targets as Human Views.
    human_markdown.semantic_view_type = semantic_site_view_type
    legacy_site.object_html_href = object_html_href
    legacy_site.breadcrumb_for = breadcrumb_for
    legacy_site.build_homepage = build_homepage

    if INTERACTION_CONFORMANCE_STYLE not in legacy_site.STYLE:
        legacy_site.STYLE += INTERACTION_CONFORMANCE_STYLE
    if "function ensureStatus(section)" not in legacy_site.MAP_SCRIPT:
        legacy_site.MAP_SCRIPT = interaction_conformance_script(legacy_site.MAP_SCRIPT)


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
