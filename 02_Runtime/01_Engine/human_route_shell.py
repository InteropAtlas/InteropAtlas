#!/usr/bin/env python3
"""Permanent shared page-shell and breadcrumb contracts for Human Route views."""

from __future__ import annotations

import html
from collections.abc import Callable


def page_shell(site_module, title: str, body: str, prefix: str = "", breadcrumb: str | None = None) -> str:
    """Render the stable Human Route document shell using current shared assets."""

    trail = f'<nav class="breadcrumb" aria-label="面包屑">{breadcrumb}</nav>' if breadcrumb else ""
    return f"""<!doctype html>
<html lang=\"zh-CN\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"><title>{html.escape(title)} · InteropAtlas</title><style>{site_module.STYLE}</style>{site_module.THEME_SCRIPT}{site_module.MAP_SCRIPT}</head>
<body><nav class=\"site-nav\" aria-label=\"主导航\"><a href=\"{prefix}index.html\"><strong>InteropAtlas</strong></a><span>· 人类可读实验站</span><button id=\"theme-toggle\" class=\"theme-toggle\" type=\"button\" onclick=\"toggleTheme()\">主题</button></nav>{trail}<main>{body}</main></body></html>"""


def breadcrumb_for(
    obj: dict,
    prefix: str,
    *,
    display_name: Callable[[dict | None, str], str],
    view_type_resolver: Callable[[dict | None], str | None],
    human_value: Callable[[object], str],
    category_anchor: Callable[[str], str],
) -> str:
    """Render semantic breadcrumb as a navigation View, not a Canonical tree."""

    name = html.escape(display_name(obj, str(obj.get("id"))))
    current = f'<span aria-current="page">{name}</span>'
    view_type = view_type_resolver(obj)
    home = f'<a href="{prefix}index.html">首页</a>'
    separator = '<span aria-hidden="true">›</span>'

    if view_type == "capability":
        category = str(obj.get("category") or "uncategorized")
        label = "未分类" if category == "uncategorized" else human_value(category)
        category_link = (
            f'<a href="{prefix}index.html#{html.escape(category_anchor(category), quote=True)}">'
            f'{html.escape(label)}</a>'
        )
        return f'{home}{separator}<span>能力</span>{separator}{category_link}{separator}{current}'

    labels = {
        "standard": "标准与规范",
        "implementation": "实现",
        "organization": "组织",
    }
    label = labels.get(str(view_type), "对象")
    return f'{home}{separator}<span>{html.escape(label)}</span>{separator}{current}'
