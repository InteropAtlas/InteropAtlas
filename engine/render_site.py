#!/usr/bin/env python3
"""Build a minimal static HTML site from InteropAtlas structured data."""

from __future__ import annotations

import argparse
import html
from collections import defaultdict
from pathlib import Path

import markdown

from bootstrap_query import index_objects, load_atlas
from graph_index import GraphIndex
from render_markdown import (
    FIELD_REFERENCE_LABELS,
    RELATION_LABELS,
    display_name,
    human_value,
    object_link,
    output_path,
    relation_group,
    render_object,
)

SUPPORTED_TYPES = {"implementation", "capability", "standard"}

STYLE = """
:root{color-scheme:light dark;--bg:#fff;--fg:#202124;--muted:#57606a;--border:#d0d7de;--code:#f6f8fa;--link:#0969da;--card:#fff;--accent-soft:#f0f6ff}
@media (prefers-color-scheme:dark){:root{--bg:#0d1117;--fg:#e6edf3;--muted:#8b949e;--border:#30363d;--code:#161b22;--link:#58a6ff;--card:#161b22;--accent-soft:#0d1f33}}
html[data-theme='light']{color-scheme:light;--bg:#fff;--fg:#202124;--muted:#57606a;--border:#d0d7de;--code:#f6f8fa;--link:#0969da;--card:#fff;--accent-soft:#f0f6ff}
html[data-theme='dark']{color-scheme:dark;--bg:#0d1117;--fg:#e6edf3;--muted:#8b949e;--border:#30363d;--code:#161b22;--link:#58a6ff;--card:#161b22;--accent-soft:#0d1f33}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;max-width:980px;margin:0 auto;padding:32px 20px;line-height:1.65;color:var(--fg);background:var(--bg)}
a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}
nav{display:flex;align-items:center;gap:8px;margin-bottom:18px;padding-bottom:14px;border-bottom:1px solid var(--border)}
.theme-toggle{margin-left:auto;border:1px solid var(--border);background:var(--card);color:var(--fg);border-radius:999px;padding:6px 11px;cursor:pointer}
.breadcrumb{font-size:.92em;color:var(--muted);margin:0 0 24px}.breadcrumb span{margin:0 6px}.breadcrumb a{color:var(--muted)}
code{background:var(--code);padding:.15em .35em;border-radius:4px}
blockquote{color:var(--muted);border-left:4px solid var(--border);margin-left:0;padding-left:16px}
h1,h2,h3{line-height:1.25}h2{margin-top:34px}.meta,.muted{color:var(--muted)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}.card{border:1px solid var(--border);background:var(--card);border-radius:8px;padding:16px}
.category-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:16px}.category-card{border:1px solid var(--border);background:var(--card);border-radius:10px;padding:18px;scroll-margin-top:24px}.category-card h3{margin:0 0 6px}.category-card ul{margin:12px 0 0;padding-left:20px}.category-card li+li{margin-top:8px}.count{font-size:.9em;color:var(--muted)}
details{border-top:1px solid var(--border);padding:14px 0}summary{cursor:pointer;font-weight:600}details .grid{margin-top:14px}
.local-map{margin:28px 0 10px;padding:18px;border:1px solid var(--border);border-radius:14px;background:var(--code)}
.local-map-title{display:flex;align-items:baseline;justify-content:space-between;gap:12px;margin-bottom:14px}.local-map-title strong{font-size:1.05em}.local-map-title span{font-size:.86em;color:var(--muted)}
.map-controls{display:flex;flex-direction:column;gap:8px;margin:0 0 16px}.map-filter-row{display:flex;align-items:center;flex-wrap:wrap;gap:7px}.map-filter-label{font-size:.82em;color:var(--muted);margin-right:2px}.map-filter{border:1px solid var(--border);background:var(--card);color:var(--fg);border-radius:999px;padding:4px 9px;font-size:.8em;cursor:pointer}.map-filter:hover{border-color:var(--link)}.map-filter.is-active{border-color:var(--link);background:var(--accent-soft);color:var(--link)}
.local-map-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(190px,.8fr) minmax(0,1fr);gap:16px;align-items:center}
.map-column{display:flex;flex-direction:column;gap:10px}.map-column-title{text-align:center;color:var(--muted);font-size:.82em;font-weight:600;text-transform:uppercase;letter-spacing:.04em}
.map-node{border:1px solid var(--border);background:var(--card);border-radius:11px;padding:11px 12px;min-width:0}.map-node-name{font-weight:600;overflow-wrap:anywhere}.map-edge{display:block;margin-top:4px;color:var(--muted);font-size:.82em;line-height:1.4}.map-origin{display:inline-block;margin-left:5px;padding:1px 5px;border:1px solid var(--border);border-radius:999px;font-size:.9em}
.map-center{border:2px solid var(--link);background:var(--accent-soft);text-align:center;padding:18px 14px}.map-center .map-node-name{font-size:1.05em}.map-center .map-edge{margin-top:6px}
.map-empty,.map-filter-empty{color:var(--muted);font-size:.9em;text-align:center;padding:10px}.map-filter-empty[hidden]{display:none}
@media(max-width:760px){.local-map-grid{grid-template-columns:1fr}.map-center{order:-1}.map-column-title{text-align:left}.local-map-title{display:block}.local-map-title span{display:block;margin-top:4px}.map-filter-row{align-items:flex-start}}
"""

THEME_SCRIPT = """
<script>
(function(){
  const root=document.documentElement;
  const saved=localStorage.getItem('ia-theme');
  if(saved==='light'||saved==='dark') root.dataset.theme=saved;
  function current(){return root.dataset.theme|| (matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');}
  function update(){const b=document.getElementById('theme-toggle');if(!b)return;b.textContent=current()==='dark'?'☀ 亮色':'☾ 深色';b.setAttribute('aria-label','切换亮色或深色模式');}
  window.toggleTheme=function(){const next=current()==='dark'?'light':'dark';root.dataset.theme=next;localStorage.setItem('ia-theme',next);update();};
  addEventListener('DOMContentLoaded',update);
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!localStorage.getItem('ia-theme'))update();});
})();
</script>
"""

MAP_SCRIPT = """
<script>
(function(){
  function setActive(section, kind, value){
    section.querySelectorAll('.map-filter[data-filter-kind="'+kind+'"]').forEach(function(button){
      button.classList.toggle('is-active', button.dataset.filterValue===value);
      button.setAttribute('aria-pressed', button.dataset.filterValue===value ? 'true' : 'false');
    });
  }
  function apply(section){
    const origin=section.dataset.filterOrigin||'all';
    const group=section.dataset.filterGroup||'all';
    section.querySelectorAll('.map-edge[data-origin]').forEach(function(edge){
      const originOk=origin==='all'||edge.dataset.origin===origin;
      const groupOk=group==='all'||edge.dataset.group===group;
      edge.hidden=!(originOk&&groupOk);
    });
    section.querySelectorAll('.map-column').forEach(function(column){
      let visible=0;
      column.querySelectorAll('.map-node:not(.map-center)').forEach(function(node){
        const hasVisible=Array.from(node.querySelectorAll('.map-edge[data-origin]')).some(function(edge){return !edge.hidden;});
        node.hidden=!hasVisible;
        if(hasVisible) visible+=1;
      });
      const empty=column.querySelector('.map-filter-empty');
      if(empty) empty.hidden=visible!==0;
    });
  }
  window.filterLocalMap=function(button){
    const section=button.closest('.local-map');
    if(!section)return;
    const kind=button.dataset.filterKind;
    const value=button.dataset.filterValue;
    if(kind==='origin'){
      section.dataset.filterOrigin=value;
      if(value==='field'){
        section.dataset.filterGroup='all';
        setActive(section,'group','all');
      }
    }else if(kind==='group'){
      section.dataset.filterGroup=value;
      if(value!=='all'&&section.dataset.filterOrigin==='field'){
        section.dataset.filterOrigin='relation';
        setActive(section,'origin','relation');
      }
    }
    setActive(section,kind,value);
    apply(section);
  };
  addEventListener('DOMContentLoaded',function(){document.querySelectorAll('.local-map').forEach(apply);});
})();
</script>
"""


def page_shell(title: str, body: str, prefix: str = "", breadcrumb: str | None = None) -> str:
    trail = f'<div class="breadcrumb">{breadcrumb}</div>' if breadcrumb else ""
    return f"""<!doctype html>
<html lang=\"zh-CN\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"><title>{html.escape(title)} · InteropAtlas</title><style>{STYLE}</style>{THEME_SCRIPT}{MAP_SCRIPT}</head>
<body><nav><a href=\"{prefix}index.html\"><strong>InteropAtlas</strong></a><span>· 人类可读实验站</span><button id=\"theme-toggle\" class=\"theme-toggle\" type=\"button\" onclick=\"toggleTheme()\">主题</button></nav>{trail}{body}</body></html>"""


def markdown_to_html(text: str) -> str:
    text = text.replace(".md)", ".html)")
    return markdown.markdown(text, extensions=["extra", "sane_lists"])


def object_card(obj: dict, path: Path) -> str:
    name = html.escape(display_name(obj, str(obj.get("id"))))
    summary = html.escape(str(obj.get("summary_zh") or obj.get("description_zh") or ""))
    return f'<div class="card"><a href="{path.as_posix()}"><strong>{name}</strong></a><p>{summary}</p></div>'


def category_anchor(category: str) -> str:
    return f"category-{category}"


def breadcrumb_for(obj: dict, prefix: str) -> str:
    name = html.escape(display_name(obj, str(obj.get("id"))))
    object_type = obj.get("type")
    home = f'<a href="{prefix}index.html">首页</a>'
    separator = '<span>›</span>'
    if object_type == "capability":
        category = str(obj.get("category") or "uncategorized")
        label = "未分类" if category == "uncategorized" else human_value(category)
        category_link = f'<a href="{prefix}index.html#{category_anchor(category)}">{html.escape(label)}</a>'
        return f'{home}{separator}<span>能力</span>{separator}{category_link}{separator}{name}'
    labels = {"standard": "标准与规范", "implementation": "实现"}
    label = labels.get(str(object_type), str(object_type or "对象"))
    return f'{home}{separator}<span>{html.escape(label)}</span>{separator}{name}'


def object_html_link(source_obj: dict, target_obj: dict | None, fallback: str) -> str:
    label = html.escape(display_name(target_obj, fallback))
    if not target_obj or target_obj.get("type") not in SUPPORTED_TYPES:
        return label
    link = object_link(source_obj, target_obj)
    if not link:
        return label
    href = html.escape(str(Path(link).with_suffix(".html")).replace("\\", "/"), quote=True)
    return f'<a href="{href}">{label}</a>'


def map_edge_label(edge) -> tuple[str, str]:
    if edge.origin == "relation":
        return RELATION_LABELS.get(edge.kind, edge.kind), relation_group(edge.kind)
    return FIELD_REFERENCE_LABELS.get(edge.field or "", edge.field or "字段引用"), "字段引用"


def map_column_html(source_obj: dict, index: dict[str, dict], edges: list, incoming: bool) -> str:
    grouped: dict[str, list] = defaultdict(list)
    for edge in edges:
        neighbor_id = edge.source_id if incoming else edge.target_id
        grouped[neighbor_id].append(edge)

    if not grouped:
        return '<div class="map-empty">暂无</div>'

    cards = []
    for neighbor_id, neighbor_edges in sorted(
        grouped.items(),
        key=lambda item: display_name(index.get(item[0]), item[0]),
    ):
        neighbor = index.get(neighbor_id)
        labels = []
        for edge in sorted(neighbor_edges, key=lambda item: (item.origin, item.kind, item.field or "")):
            label, group = map_edge_label(edge)
            origin = "Relation" if edge.origin == "relation" else "字段"
            origin_key = "relation" if edge.origin == "relation" else "field"
            arrow = "→ 当前对象" if incoming else "当前对象 →"
            labels.append(
                f'<span class="map-edge" data-origin="{origin_key}" data-group="{html.escape(group, quote=True)}">'
                f'{html.escape(arrow)} {html.escape(label)} · {html.escape(group)}'
                f'<span class="map-origin">{origin}</span></span>'
            )
        cards.append(
            '<div class="map-node">'
            f'<div class="map-node-name">{object_html_link(source_obj, neighbor, neighbor_id)}</div>'
            f'{"".join(labels)}</div>'
        )
    cards.append('<div class="map-filter-empty" hidden>当前筛选下暂无邻居</div>')
    return "".join(cards)


def map_filter_button(kind: str, value: str, label: str, active: bool = False) -> str:
    active_class = " is-active" if active else ""
    pressed = "true" if active else "false"
    return (
        f'<button type="button" class="map-filter{active_class}" data-filter-kind="{html.escape(kind, quote=True)}" '
        f'data-filter-value="{html.escape(value, quote=True)}" aria-pressed="{pressed}" '
        f'onclick="filterLocalMap(this)">{html.escape(label)}</button>'
    )


def build_map_controls(edges: list) -> str:
    origin_row = (
        '<div class="map-filter-row"><span class="map-filter-label">连接来源</span>'
        + map_filter_button("origin", "all", "全部", True)
        + map_filter_button("origin", "relation", "显式 Relation")
        + map_filter_button("origin", "field", "字段引用")
        + '</div>'
    )
    relation_groups = sorted({relation_group(edge.kind) for edge in edges if edge.origin == "relation"})
    if not relation_groups:
        return f'<div class="map-controls">{origin_row}</div>'
    group_row = (
        '<div class="map-filter-row"><span class="map-filter-label">关系语义</span>'
        + map_filter_button("group", "all", "全部", True)
        + "".join(map_filter_button("group", group, group) for group in relation_groups)
        + '</div>'
    )
    return f'<div class="map-controls">{origin_row}{group_row}</div>'


def build_local_map(obj: dict, index: dict[str, dict], graph: GraphIndex) -> str:
    object_id = str(obj.get("id"))
    outgoing = graph.forward(object_id)
    incoming = graph.backlinks(object_id)
    if not outgoing and not incoming:
        return ""

    all_edges = incoming + outgoing
    neighbor_ids = {edge.target_id for edge in outgoing} | {edge.source_id for edge in incoming}
    center_name = html.escape(display_name(obj, object_id))
    center_type = html.escape(str(obj.get("type") or "object"))
    return (
        '<section class="local-map" aria-label="一跳局部地图" data-filter-origin="all" data-filter-group="all">'
        '<div class="local-map-title"><strong>一跳局部地图</strong>'
        f'<span>{len(neighbor_ids)} 个邻居 · {len(incoming)} 条入向连接 · {len(outgoing)} 条出向连接</span></div>'
        f'{build_map_controls(all_edges)}'
        '<div class="local-map-grid">'
        '<div class="map-column"><div class="map-column-title">指向当前对象</div>'
        f'{map_column_html(obj, index, incoming, True)}</div>'
        '<div class="map-node map-center">'
        f'<div class="map-node-name">{center_name}</div>'
        f'<span class="map-edge">当前对象 · {center_type}</span></div>'
        '<div class="map-column"><div class="map-column-title">当前对象指向</div>'
        f'{map_column_html(obj, index, outgoing, False)}</div>'
        '</div></section>'
    )


def inject_local_map(content: str, local_map: str) -> str:
    if not local_map:
        return content
    marker = "<h2>基本信息</h2>"
    if marker in content:
        return content.replace(marker, f"{local_map}{marker}", 1)
    return local_map + content


def build_homepage(rendered: list[tuple[dict, Path]]) -> str:
    capabilities = [(obj, path) for obj, path in rendered if obj.get("type") == "capability"]
    standards = [(obj, path) for obj, path in rendered if obj.get("type") == "standard"]
    implementations = [(obj, path) for obj, path in rendered if obj.get("type") == "implementation"]

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
        sections.append(f'<section class="category-card" id="{html.escape(category_anchor(category))}">')
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
        sections.append(f'<details><summary>{heading} <span class="count">({len(items)})</span></summary><div class="grid">')
        for obj, path in sorted(items, key=lambda item: display_name(item[0], str(item[0].get("id")))):
            sections.append(object_card(obj, path))
        sections.append('</div></details>')

    return "".join(sections)


def build(root: Path, output: Path) -> dict[str, int]:
    objects, relations = load_atlas(root)
    index = index_objects(objects)
    graph = GraphIndex(index, relations)
    rendered = []
    for obj in objects:
        if obj.get("type") not in SUPPORTED_TYPES:
            continue
        md_path = output_path(obj)
        if not md_path:
            continue
        html_path = Path(md_path).with_suffix(".html")
        target = output / html_path
        target.parent.mkdir(parents=True, exist_ok=True)
        content = markdown_to_html(render_object(obj, index, graph))
        content = inject_local_map(content, build_local_map(obj, index, graph))
        prefix = "../" * len(html_path.parent.parts)
        target.write_text(
            page_shell(
                display_name(obj, str(obj.get("id"))),
                content,
                prefix,
                breadcrumb_for(obj, prefix),
            ),
            encoding="utf-8",
        )
        rendered.append((obj, html_path))

    output.mkdir(parents=True, exist_ok=True)
    (output / "index.html").write_text(page_shell("首页", build_homepage(rendered)), encoding="utf-8")
    (output / ".nojekyll").write_text("", encoding="utf-8")
    return {
        "objects_loaded": len(objects),
        "pages_rendered": len(rendered),
        "graph_edges": len(graph.edges),
        "reference_issues": len(graph.issues),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
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
