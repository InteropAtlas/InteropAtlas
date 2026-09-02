#!/usr/bin/env python3
"""Dedicated, deterministic Compare views for the InteropAtlas Human Route."""

from __future__ import annotations

import html
from pathlib import Path
from typing import Callable


CONTEXT_ID = "automated_build_deployment"
CANDIDATE_IDS = ("forgejo_actions", "github_actions")
RELATION_ID = "forgejo_actions_alternative_to_github_actions"
COMPARE_PATH = Path("compare/automated_build_deployment--forgejo_actions--github_actions.html")

COMPARE_STYLE = """
.compare-context{border-left:4px solid var(--link);padding:10px 14px;background:var(--accent-soft);margin:18px 0 24px}.compare-candidates{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin:16px 0 26px}.compare-dimension{border-top:1px solid var(--border);padding:18px 0}.compare-dimension h2{margin:0 0 12px;font-size:1.08em}.compare-values{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.compare-value{border:1px solid var(--border);border-radius:8px;padding:12px;background:var(--card)}.compare-value strong{display:block;margin-bottom:6px}.compare-boundary{margin:24px 0;padding:14px;border:1px solid var(--border);border-radius:8px}.compare-entry{margin:22px 0;padding:14px;border:1px solid var(--border);border-radius:8px;background:var(--card)}.compare-entry ul{margin-bottom:10px}@media(max-width:620px){.compare-candidates,.compare-values{grid-template-columns:1fr}}
"""

_DEPLOYMENT_LABELS = {
    "self_hosted_platform": "完整平台可自托管",
    "self_hosted_runner": "可使用自托管 Runner",
    "github_hosted_runner": "GitHub 托管 Runner",
}


def _bool_label(value: object) -> str:
    if value is True:
        return "是"
    if value is False:
        return "否"
    return "当前记录未提供"


def _deployment_labels(record: dict) -> str:
    models = record.get("deployment_models") or []
    if not models:
        return "当前记录未提供"
    return "；".join(_DEPLOYMENT_LABELS.get(str(item), str(item)) for item in models)


def _license_label(record: dict) -> str:
    value = record.get("license_expression")
    return str(value) if value else "当前记录未提供（not recorded）"


def _supports_capability(record: dict, capability_id: str) -> str:
    return "支持" if capability_id in (record.get("capabilities") or []) else "当前记录未建立支持关系"


def _link(record: dict, label: str | None = None, prefix: str = "../") -> str:
    object_id = str(record.get("id"))
    name = label or str(record.get("name_zh") or record.get("name_en") or object_id)
    return f'<a href="{prefix}objects/{html.escape(object_id, quote=True)}.html">{html.escape(name)}</a>'


def capability_candidates(capability_id: str, index: dict[str, dict]) -> list[dict]:
    """Project implementation candidates from Canonical capability membership."""

    candidates = [
        record for record in index.values()
        if capability_id in (record.get("capabilities") or [])
    ]
    return sorted(
        candidates,
        key=lambda record: str(record.get("name_zh") or record.get("name_en") or record.get("id")),
    )


def compare_entry_html(capability_id: str, index: dict[str, dict]) -> str:
    """Render candidates from Canonical state and expose only an implemented Compare artifact."""

    candidates = capability_candidates(capability_id, index)
    if not candidates:
        return ""
    items = "".join(f"<li>{_link(candidate)}</li>" for candidate in candidates)
    candidate_ids = {str(candidate.get("id")) for candidate in candidates}
    compare_link = ""
    if capability_id == CONTEXT_ID and set(CANDIDATE_IDS).issubset(candidate_ids):
        href = "../" + COMPARE_PATH.as_posix()
        compare_link = (
            f'<p><a href="{html.escape(href, quote=True)}">比较 Forgejo Actions 与 GitHub Actions</a></p>'
            '<p class="muted">当前 dedicated Compare 只覆盖上述这一对候选，不代表其他组合已经可比较。</p>'
        )
    return (
        '<section class="compare-entry" aria-label="可比较实现">'
        '<strong>支持这个能力的实现</strong>'
        '<p>以下候选由当前 Canonical objects 的 capabilities 记录推导；Renderer 不维护第二份候选清单。</p>'
        f'<ul>{items}</ul>{compare_link}'
        '</section>'
    )


def inject_compare_entry(content: str, obj: dict, index: dict[str, dict]) -> str:
    capability_id = str(obj.get("id"))
    entry = compare_entry_html(capability_id, index)
    if not entry:
        return content
    marker = "<h2>一跳邻居</h2>"
    if marker in content:
        return content.replace(marker, entry + marker, 1)
    return content + entry


def build_compare_body(index: dict[str, dict], relations: list[dict]) -> str:
    context = index[CONTEXT_ID]
    left = index[CANDIDATE_IDS[0]]
    right = index[CANDIDATE_IDS[1]]
    relation = next(item for item in relations if item.get("id") == RELATION_ID)

    context_name = str(context.get("name_zh") or context.get("name_en") or CONTEXT_ID)
    left_name = str(left.get("name_zh") or left.get("name_en") or CANDIDATE_IDS[0])
    right_name = str(right.get("name_zh") or right.get("name_en") or CANDIDATE_IDS[1])

    dimensions = (
        ("支持当前能力", _supports_capability(left, CONTEXT_ID), _supports_capability(right, CONTEXT_ID)),
        ("开放源码", _bool_label(left.get("open_source")), _bool_label(right.get("open_source"))),
        ("完整平台可自托管", _bool_label(left.get("self_hostable")), _bool_label(right.get("self_hostable"))),
        ("部署方式", _deployment_labels(left), _deployment_labels(right)),
        ("许可证表达", _license_label(left), _license_label(right)),
        (
            "替代关系",
            "在当前 CI/CD / 仓库工作流上下文中记录为 alternative_to GitHub Actions",
            "是上述 alternative_to 关系的目标对象；不自动推导反向等价关系",
        ),
        (
            "兼容性声明",
            "未建立 compatible_with；现有 Relation 明确说明不追求完全兼容",
            "没有从该单向 alternative_to Relation 推导任何反向兼容声明",
        ),
    )

    parts = [
        "<h1>比较 Forgejo Actions 与 GitHub Actions</h1>",
        '<div class="compare-context">',
        '<strong>比较上下文：</strong> ',
        _link(context, context_name),
        "<p>只有在这个明确 Capability（能力）上下文中，两者才进入本次候选集合。Compare 是 View / Projection，不创造新的事实。</p>",
        "</div>",
        '<div class="compare-candidates">',
        f'<div class="card"><strong>候选 A</strong><p>{_link(left, left_name)}</p><p>{html.escape(str(left.get("summary_zh") or ""))}</p></div>',
        f'<div class="card"><strong>候选 B</strong><p>{_link(right, right_name)}</p><p>{html.escape(str(right.get("summary_zh") or ""))}</p></div>',
        "</div>",
    ]

    for dimension, left_value, right_value in dimensions:
        parts.extend(
            [
                '<section class="compare-dimension">',
                f"<h2>{html.escape(dimension)}</h2>",
                '<div class="compare-values">',
                f'<div class="compare-value"><strong>{html.escape(left_name)}</strong><span>{html.escape(left_value)}</span></div>',
                f'<div class="compare-value"><strong>{html.escape(right_name)}</strong><span>{html.escape(right_value)}</span></div>',
                "</div></section>",
            ]
        )

    conditions = str(relation.get("conditions_zh") or "")
    parts.extend(
        [
            '<section class="compare-boundary">',
            "<h2>关系语义边界</h2>",
            f"<p>{html.escape(conditions)}</p>",
            "<p><strong>本页不输出 winner（胜者）、overall score（总分）或推荐结论。</strong>开放源码、自托管等事实可能对某些任务重要，但不会被自动合成为“谁整体更好”。</p>",
            "<p>“当前记录未提供”表示字段缺失，不等于 false、none 或不存在该现实属性。</p>",
            "</section>",
        ]
    )
    return "".join(parts)


def build_compare_artifact(
    output: Path,
    index: dict[str, dict],
    relations: list[dict],
    page_shell: Callable[..., str],
) -> Path:
    target = output / COMPARE_PATH
    target.parent.mkdir(parents=True, exist_ok=True)
    page = page_shell("比较 Forgejo Actions 与 GitHub Actions", build_compare_body(index, relations), "../")
    page = page.replace("</style>", COMPARE_STYLE + "</style>", 1)
    target.write_text(page, encoding="utf-8")
    return target
