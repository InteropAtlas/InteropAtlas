#!/usr/bin/env python3
"""Deterministic static Search view for the InteropAtlas Human Route."""

from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Callable


SEARCH_SCRIPT = """
<script>
(function(){
  const input=document.getElementById('atlas-search-input');
  const form=document.getElementById('atlas-search-form');
  const status=document.getElementById('atlas-search-status');
  const results=document.getElementById('atlas-search-results');
  if(!input||!form||!status||!results)return;

  let index=[];
  const normalize=value=>(value||'').toLocaleLowerCase();
  const escapeHtml=value=>String(value).replace(/[&<>\"']/g,ch=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[ch]));

  function currentQuery(){return new URL(location.href).searchParams.get('q')||'';}
  function score(item,q){
    const n=normalize(item.name), id=normalize(item.id), hay=normalize(item.search_text);
    if(n===q||id===q)return 0;
    if(n.startsWith(q)||id.startsWith(q))return 1;
    return hay.includes(q)?2:99;
  }
  function render(query){
    const trimmed=query.trim();
    input.value=trimmed;
    results.innerHTML='';
    if(!trimmed){status.textContent='输入名称、关键词或稳定 ID 开始搜索。';return;}
    const q=normalize(trimmed);
    const matches=index
      .map(item=>({item,rank:score(item,q)}))
      .filter(row=>row.rank<99)
      .sort((a,b)=>a.rank-b.rank||a.item.name.localeCompare(b.item.name,'zh-CN')||a.item.id.localeCompare(b.item.id))
      .map(row=>row.item);
    status.textContent=matches.length?`找到 ${matches.length} 个结果。`:'没有找到结果。';
    for(const item of matches){
      const card=document.createElement('article');
      card.className='card search-result';
      card.innerHTML=`<h2><a href="${escapeHtml(item.url)}">${escapeHtml(item.name)}</a></h2>`+
        `<p class="muted">${escapeHtml(item.type_label)} · <code>${escapeHtml(item.id)}</code></p>`+
        (item.summary?`<p>${escapeHtml(item.summary)}</p>`:'');
      results.appendChild(card);
    }
  }
  function setQuery(query,push){
    const url=new URL(location.href);
    if(query.trim())url.searchParams.set('q',query.trim());else url.searchParams.delete('q');
    if(push)history.pushState({},'',url);
    render(query);
  }

  form.addEventListener('submit',event=>{event.preventDefault();setQuery(input.value,true);});
  addEventListener('popstate',()=>render(currentQuery()));

  fetch('search-index.json',{credentials:'same-origin'})
    .then(response=>{if(!response.ok)throw new Error('HTTP '+response.status);return response.json();})
    .then(data=>{index=Array.isArray(data)?data:[];render(currentQuery());})
    .catch(()=>{status.textContent='搜索索引载入失败；稳定对象页面仍可通过首页和已有链接访问。';});
})();
</script>
"""

SEARCH_STYLE = """
.search-form{display:flex;gap:8px;align-items:flex-end;margin:20px 0 14px}.search-form label{display:flex;flex:1;flex-direction:column;gap:6px;font-weight:600}.search-form input{font:inherit;padding:9px 11px;border:1px solid var(--border);border-radius:8px;background:var(--card);color:var(--fg)}.search-form button{font:inherit;padding:9px 14px;border:1px solid var(--border);border-radius:8px;background:var(--card);color:var(--fg);cursor:pointer}.search-results{display:grid;gap:12px}.search-result h2{margin:0 0 4px;font-size:1.08em}.search-result p{margin:6px 0}@media(max-width:560px){.search-form{align-items:stretch;flex-direction:column}}
"""


def build_search_index(
    rendered: list[tuple[dict, Path]],
    display_name: Callable[[dict | None, str], str],
    summary_of: Callable[[dict], str | None],
    type_label: Callable[[dict], str],
) -> list[dict[str, str]]:
    """Build a stable, Human-only search projection from rendered resources."""

    rows: list[dict[str, str]] = []
    for obj, path in rendered:
        object_id = str(obj.get("id") or "")
        name = display_name(obj, object_id)
        summary = str(summary_of(obj) or "")
        label = type_label(obj)
        aliases = obj.get("aliases") or obj.get("aliases_en") or []
        if isinstance(aliases, str):
            aliases = [aliases]
        alias_text = " ".join(str(item) for item in aliases)
        search_text = " ".join((name, object_id, summary, label, alias_text))
        rows.append(
            {
                "id": object_id,
                "name": name,
                "summary": summary,
                "type_label": label,
                "url": path.as_posix(),
                "search_text": search_text,
            }
        )
    rows.sort(key=lambda row: (row["name"].casefold(), row["id"]))
    return rows


def search_page_body() -> str:
    return """<h1>搜索 InteropAtlas</h1>
<p>按名称、关键词或稳定 ID 查找当前 Human Route 已发布的对象。Search 是 View / Projection，不改变 Canonical 分类，也不会生成隐藏排名或推荐。</p>
<form id="atlas-search-form" class="search-form" action="search.html" method="get">
<label for="atlas-search-input">搜索词<input id="atlas-search-input" name="q" type="search" autocomplete="off" enterkeyhint="search"></label>
<button type="submit">搜索</button>
</form>
<p id="atlas-search-status" role="status" aria-live="polite">输入名称、关键词或稳定 ID 开始搜索。</p>
<div id="atlas-search-results" class="search-results"></div>
<noscript><p>当前 Search 结果需要 JavaScript；对象页、首页入口和稳定链接仍可正常使用。</p></noscript>""" + SEARCH_SCRIPT


def build_search_artifacts(
    output: Path,
    rendered: list[tuple[dict, Path]],
    page_shell: Callable[..., str],
    display_name: Callable[[dict | None, str], str],
    summary_of: Callable[[dict], str | None],
    type_label: Callable[[dict], str],
) -> int:
    """Write search.html and search-index.json. Returns indexed record count."""

    rows = build_search_index(rendered, display_name, summary_of, type_label)
    output.mkdir(parents=True, exist_ok=True)
    (output / "search-index.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    page = page_shell("搜索", search_page_body())
    page = page.replace("</style>", SEARCH_STYLE + "</style>", 1)
    (output / "search.html").write_text(page, encoding="utf-8")
    return len(rows)
