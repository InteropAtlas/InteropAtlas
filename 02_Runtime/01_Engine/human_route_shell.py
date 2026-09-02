#!/usr/bin/env python3
"""Permanent shared page-shell and breadcrumb helpers for the Human Route."""

from __future__ import annotations

import html
from pathlib import Path
from typing import Callable


HUMAN_VIEW_LABELS = {
    "capability": "能力",
    "standard": "标准与规范",
    "implementation": "实现",
    "organization": "组织",
}


def human_view_label(view_type: str | None) -> str:
    """Return a stable Human-facing label for a semantic Resource view."""

    return HUMAN_VIEW_LABELS.get(str(view_type), "对象")


def breadcrumb_for(
    obj: dict,
    prefix: str,
    semantic_view_type: Callable[[dict | None], str | None],
    display_name: Callable[[dict | None, str], str],
    human_value: Callable[[object], str],
    category_anchor: Callable[[str], str],
) -> str:
    """Build the shared semantic breadcrumb for a Human Resource page."""

    name = html.escape(display_name(obj, str(obj.get("id"))))
    current = f'<span aria-current="page">{name}</span>'
    view_type = semantic_view_type(obj)
    home = f'<a href="{prefix}index.html">首页</a>'
    separator = '<span aria-hidden="true">›</span>'
    if view_type == "capability":
        category = str(obj.get("category") or "uncategorized")
        label = "未分类" if category == "uncategorized" else human_value(category)
        category_link = (
            f'<a href="{prefix}index.html#{category_anchor(category)}">'
            f'{html.escape(label)}</a>'
        )
        return f'{home}{separator}<span>能力</span>{separator}{category_link}{separator}{current}'
    label = human_view_label(view_type)
    return f'{home}{separator}<span>{html.escape(label)}</span>{separator}{current}'


def object_html_href(
    source_obj: dict,
    target_obj: dict | None,
    semantic_view_type: Callable[[dict | None], str | None],
    supported_view_types: set[str],
    object_link: Callable[[dict, dict | None], str | None],
) -> str | None:
    """Resolve a stable Human HTML link without changing Canonical identity."""

    if not target_obj or semantic_view_type(target_obj) not in supported_view_types:
        return None
    link = object_link(source_obj, target_obj)
    if not link:
        return None
    return str(Path(link).with_suffix(".html")).replace("\\", "/")


def page_shell(
    legacy_site,
    title: str,
    body: str,
    prefix: str = "",
    breadcrumb: str | None = None,
) -> str:
    """Permanent Human Route entry point for the shared page shell.

    The low-level HTML/CSS primitive remains in the legacy renderer for this
    slice; Human Route modules no longer depend on that primitive directly.
    """

    return legacy_site.page_shell(title, body, prefix, breadcrumb)
