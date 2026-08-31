#!/usr/bin/env python3
"""Build a minimal static HTML site from InteropAtlas structured data."""

from __future__ import annotations

import argparse
import html
from pathlib import Path

import markdown

from bootstrap_query import index_objects, load_atlas
from graph_index import GraphIndex
from render_markdown import display_name, output_path, render_object

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
h1,h2{line-height:1.25}h2{margin-top:30px}.meta{color:var(--muted)}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}.card{border:1px solid var(--border);background:var(--card);border-radius:8px;padding:16px}
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

    groups = [("能力（Capabilities）", "capability"),("标准与规范（Standards）", "standard"),("实现（Implementations）", "implementation")]
    sections = ["<h1>InteropAtlas</h1>", "<p>这是从 InteropAtlas 结构化事实自动生成的人类可读实验站。当前优先验证阅读、链接与导航体验。</p>"]
    for heading, type_name in groups:
        items = [(obj, path) for obj, path in rendered if obj.get("type") == type_name]
        if not items:
            continue
        sections.append(f"<h2>{heading}</h2><div class=\"grid\">")
        for obj, path in sorted(items, key=lambda item: display_name(item[0], str(item[0].get("id")))):
            name = html.escape(display_name(obj, str(obj.get("id"))))
            summary = html.escape(str(obj.get("summary_zh") or obj.get("description_zh") or ""))
            sections.append(f'<div class="card"><a href="{path.as_posix()}"><strong>{name}</strong></a><p>{summary}</p></div>')
        sections.append("</div>")

    output.mkdir(parents=True, exist_ok=True)
    (output / "index.html").write_text(page_shell("首页", "".join(sections)), encoding="utf-8")
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
