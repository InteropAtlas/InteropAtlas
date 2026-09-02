#!/usr/bin/env python3
"""Permanent Human Route runtime contracts shared by current renderers.

This module owns user-observable interaction/accessibility behavior that survived
Gate B validation. Legacy/v0 object selection remains outside this boundary.
"""

from __future__ import annotations

import html
from collections.abc import Callable


INTERACTION_STYLE = """
.map-status{min-height:1.4em;margin:10px 0 14px;color:var(--muted);font-size:.9em}
.map-status.is-error{color:var(--fg);font-weight:600}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:3px solid var(--link);outline-offset:2px}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto!important}
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
}
"""

MAP_SCRIPT = """
<script>
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
  function setActive(section, kind, value){
    section.querySelectorAll('.map-filter[data-filter-kind="'+kind+'"]').forEach(function(button){
      button.classList.toggle('is-active', button.dataset.filterValue===value);
      button.setAttribute('aria-pressed', button.dataset.filterValue===value ? 'true' : 'false');
    });
  }
  function updateStats(section){
    const neighborIds=new Set();
    let incoming=0;
    let outgoing=0;
    section.querySelectorAll('.map-column[data-direction]').forEach(function(column){
      const direction=column.dataset.direction;
      column.querySelectorAll('.map-node[data-neighbor-id]:not([hidden])').forEach(function(node){neighborIds.add(node.dataset.neighborId);});
      const visibleEdges=Array.from(column.querySelectorAll('.map-edge[data-origin]')).filter(function(edge){return !edge.hidden;}).length;
      if(direction==='incoming')incoming+=visibleEdges;
      if(direction==='outgoing')outgoing+=visibleEdges;
    });
    const current=section.querySelector('.map-stats-current');
    if(current)current.textContent='当前：'+neighborIds.size+' 个邻居 · '+incoming+' 条入向连接 · '+outgoing+' 条出向连接';
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
        if(hasVisible)visible+=1;
      });
      const empty=column.querySelector('.map-filter-empty');
      if(empty)empty.hidden=visible!==0;
    });
    updateStats(section);
  }
  function absolutizeMap(section, baseUrl){
    section.querySelectorAll('a[href]').forEach(function(link){
      link.setAttribute('href',new URL(link.getAttribute('href'),baseUrl).href);
    });
    section.querySelectorAll('[data-map-href]').forEach(function(button){
      button.dataset.mapHref=new URL(button.dataset.mapHref,baseUrl).href;
    });
  }
  async function recenter(trigger){
    const section=trigger.closest('.local-map');
    if(!section)return;
    const href=new URL(trigger.dataset.mapHref,location.href).href;
    section.classList.add('map-loading');
    setStatus(section,'正在加载局部地图…',false);
    const originalText=trigger.textContent;
    trigger.textContent='载入中…';
    try{
      const response=await fetch(href,{credentials:'same-origin'});
      if(!response.ok)throw new Error('HTTP '+response.status);
      const documentText=await response.text();
      const parsed=new DOMParser().parseFromString(documentText,'text/html');
      const nextMap=parsed.querySelector('.local-map');
      if(!nextMap)throw new Error('target page has no local map');
      absolutizeMap(nextMap,response.url||href);
      const replacement=document.importNode(nextMap,true);
      section.replaceWith(replacement);
      apply(replacement);
      setStatus(replacement,'地图中心已更新。',false);
      const reduceMotion=matchMedia('(prefers-reduced-motion: reduce)').matches;
      replacement.scrollIntoView({behavior:reduceMotion?'auto':'smooth',block:'start'});
    }catch(error){
      console.warn('Local map recenter failed.',error);
      section.classList.remove('map-loading');
      trigger.textContent=originalText;
      trigger.disabled=false;
      trigger.title='局部地图载入失败；对象详情仍可通过标题链接打开';
      setStatus(section,'局部地图载入失败；可以重试，或通过对象标题链接打开详情。',true);
    }
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
  window.recenterLocalMap=function(button){recenter(button);};
  addEventListener('DOMContentLoaded',function(){
    document.querySelectorAll('.local-map').forEach(function(section){ensureStatus(section);apply(section);});
  });
})();
</script>
"""


_VIEW_LABELS = {
    "capability": "能力",
    "standard": "标准 / 规范",
    "implementation": "实现",
    "organization": "组织",
}

_CORE_TYPE_LABELS = {
    "concept": "概念",
    "artifact": "制品",
    "system": "系统",
    "agent": "主体 / 组织",
    "capability": "能力",
    "standard": "标准 / 规范",
    "implementation": "实现",
    "organization": "组织",
}


def human_object_type_label(
    obj: dict,
    view_type_resolver: Callable[[dict | None], str | None] | None = None,
) -> str:
    """Return a stable Human label without exposing raw storage/model enums."""

    view_type = view_type_resolver(obj) if view_type_resolver else None
    if view_type in _VIEW_LABELS:
        return _VIEW_LABELS[view_type]
    raw_type = str(obj.get("type") or "object")
    return _CORE_TYPE_LABELS.get(raw_type, "对象")


def install_runtime_contract(site_module) -> None:
    """Install the permanent interaction contract into a renderer module."""

    if INTERACTION_STYLE not in site_module.STYLE:
        site_module.STYLE += INTERACTION_STYLE
    site_module.MAP_SCRIPT = MAP_SCRIPT


def build_local_map(
    site_module,
    obj: dict,
    index: dict[str, dict],
    graph,
    view_type_resolver: Callable[[dict | None], str | None] | None = None,
) -> str:
    """Render the existing graph projection with Human semantic center labeling."""

    content = site_module.build_local_map(obj, index, graph)
    if not content:
        return content
    raw_type = html.escape(str(obj.get("type") or "object"))
    human_type = html.escape(human_object_type_label(obj, view_type_resolver))
    return content.replace(
        f"当前地图中心 · {raw_type}</span>",
        f"当前地图中心 · {human_type}</span>",
        1,
    )
