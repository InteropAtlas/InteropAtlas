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
from render_markdown import display_name, human_value, output_path, render_object

SUPPORTED_TYPES = {"implementation", "capability", "standard"}

STYLE = """
:root{color-scheme:light dark;--bg:#fff;--fg:#202124;--muted:#57606a;--border:#d0d7de;--code:#f6f8fa;--link:#0969da;--card:#fff}
@media (prefers-color-scheme:dark){:root{--bg:#0d1117;--fg:#e6edf3;--muted:#8b949e;--border:#30363d;--code:#161b22;--link:#58a6ff;--card:#161b22}}
html[data-theme='light']{color-scheme:light;--bg:#fff;--fg:#202124;--muted:#57606a;--border:#d0d7de;--code:#f6f8fa;--link:#0969da;--card:#fff}
html[data-theme='dark']{color-scheme:dark;--bg:#0d1117;--fg:#e6edf3;--muted:#8b949e;--border:#30363d;--code:#161b22;--link:#58a6ff;--card:#161b22}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;max-width:980px;margin:0 auto;padding:32px 20px;line-height:1.65;color:var(--fg);background:var(--bg)}
a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}
nav{display:flex;align-items:center;gap:8px;margin-bottom:28px;padding-bottom:14px;border-bottom:1px solid var(--border)}
.theme-toggle{margin-left:auto;border:1px solid var(--border);background:var(--card);color:var(--fg);border-radius:999px;padding:6px 11px;cursor:pointer}
code{background:var(--code);padding:.15em .35em;border-radius:4px}
blockquote{color:var(--muted);border-left:4px solid var(--border);margin-left:0;padding-left:16px}
h1,h2,h3{line-height:1.25}h2{margin-top:34px}.meta,.muted{color:var(--muted)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}.card{border:1px solid var(--border);background:var(--card);border-radius:8px;padding:16px}
.category-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:16px}.category-card{border:1px solid var(--border);background:var(--card);border-radius:10px;padding:18px}.category-card h3{margin:0 0 6px}.category-card ul{margin:12px 0 0;padding-left:20px}.category-card li+li{margin-top:8px}.count{font-size:.9em;color:var(--muted)}
details{border-top:1px solid var(--border);padding:14px 0}summary{cursor:pointer;font-weight:600}details .grid{margin-top:14px}
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


def page_shell(title: str, body: str, prefix: str = "") -> str:
    return f"""<!doctype html>
<html lang=\"zh-CN\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"><title>{html.escape(title)} · InteropAtlas</title><style>{STYLE}</style>{THEME_SCRIPT}</head>
<body><nav><a href=\"{prefix}index.html\"><strong>InteropAtlas</strong></a><span>· 人类可读实验站</span><button id=\"theme-toggle\" class=\"theme-toggle\" type=\"button\" onclick=\"toggleTheme()\">主题</button></nav>{body}</body></html>"""


def markdown_to_html(text: str) -> str:
    text = text.replace(".md)", ".html)")
    return markdown.markdown(text, extensions=["extra", "sane_lists"])


def object_card(obj: dict, path: Path) -> str:
    name = html.escape(display_name(obj, str(obj.get("id"))))
    summary = html.escape(str(obj.get("summary_zh") or obj.get("description_zh") or ""))
    return f'<div class="card"><a href="{path.as_posix()}"><strong>{name}</strong></a><p>{summary}</p></div>'


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
        sections.append('<section class="category-card">')
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
        prefix = "../" * len(html_path.parent.parts)
        target.write_text(page_shell(display_name(obj, str(obj.get("id"))), content, prefix), encoding="utf-8")
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
