#!/usr/bin/env python3
"""Dedicated, deterministic Compare views for the InteropAtlas Human Route."""

from __future__ import annotations

import html
from pathlib import Path
from typing import Callable

from workspace_projection import NOT_RECORDED, project_compare, select_by_capability


CONTEXT_ID = "automated_build_deployment"
CANDIDATE_IDS = ("forgejo_actions", "github_actions")
RELATION_ID = "forgejo_actions_alternative_to_github_actions"
COMPARE_PATH = Path("compare/automated_build_deployment--forgejo_actions--github_actions.html")
COMPARE_FIELDS = ("open_source", "self_hostable", "deployment_models", "license_expression")

COMPARE_STYLE = """
.compare-context{border-left:4px solid var(--link);padding:10px 14px;background:var(--accent-soft);margin:18px 0 24px}.compare-candidates{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin:16px 0 26px}.compare-dimension{border-top:1px solid var(--border);padding:18px 0}.compare-dimension h2{margin:0 0 12px;font-size:1.08em}.compare-values{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.compare-value{border:1px solid var(--border);border-radius:8px;padding:12px;background:var(--card)}.compare-value strong{display:block;margin-bottom:6px}.compare-boundary{margin:24px 0;padding:14px;border:1px solid var(--border);border-radius:8px}.compare-entry{margin:22px 0;padding:14px;border:1px solid var(--border);border-radius:8px;background:var(--card)}.compare-entry ul{margin-bottom:10px}.compare-evidence{font-size:.9em;color:var(--muted);margin-top:6px}@media(max-width:620px){.compare-candidates,.compare-values{grid-template-columns:1fr}}
"""

_DEPLOYMENT_LABELS = {
    "self_hosted_platform": "完整平台可自托管",
    "self_hosted_runner": "可使用自托管 Runner",
    "github_hosted_runner": "GitHub 托管 Runner",
}


def _link(record: dict, label: str | None = None, prefix: str = "../") -> str:
    object_id = str(record.get("id"))
    name = label or str(record.get("name_zh") or record.get("name_en") or object_id)
    return f'<a href="{prefix}objects/{html.escape(object_id, quote=True)}.html">{html.escape(name)}</a>'


def capability_candidates(capability_id: str, index: dict[str, dict]) -> list[dict]:
    """Return records through the shared workspace selection contract."""

    return list(select_by_capability(capability_id, index)["records"])


def compare_entry_html(capability_id: str, index: dict[str, dict]) -> str:
    selection = select_by_capability(capability_id, index)
    candidates = selection["records"]
    if not candidates:
        return ""
    items = "".join(f"<li>{_link(candidate)}</li>" for candidate in candidates)
    candidate_ids = set(selection["selected_ids"])
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
        '<p>以下候选由当前 Canonical objects 的 capabilities 记录推导，并通过 Workspace Selection V1 读取；不使用相似度、推荐或等价性推断。</p>'
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


def _value_label(field_projection: dict) -> str:
    if field_projection["state"] == NOT_RECORDED:
        return "当前记录未提供（not recorded）"
    value = field_projection["value"]
    field = field_projection["field"]
    if field in {"open_source", "self_hostable"}:
        return "是" if value is True else "否" if value is False else str(value)
    if field == "deployment_models":
        return "；".join(_DEPLOYMENT_LABELS.get(str(item), str(item)) for item in (value or [])) or "当前记录未提供（not recorded）"
    return str(value)


def _evidence_html(field_projection: dict) -> str:
    evidence = field_projection.get("evidence") or []
    if not evidence:
        return '<div class="compare-evidence">当前投影未附带来源。</div>'
    links = "；".join(
        f'<a href="{html.escape(str(item["url"]), quote=True)}">{html.escape(str(item.get("title") or item["url"]))}</a>'
        for item in evidence
    )
    return f'<div class="compare-evidence">来源：{links}</div>'


def build_compare_body(index: dict[str, dict], relations: list[dict]) -> str:
    projection = project_compare(CONTEXT_ID, CANDIDATE_IDS, COMPARE_FIELDS, index)
    if projection["included_ids"] != list(CANDIDATE_IDS):
        raise ValueError("Compare candidates must both be explicitly selected by the V1 workspace contract")

    context = index[CONTEXT_ID]
    relation = next(item for item in relations if item.get("id") == RELATION_ID)
    projected = {item["id"]: item for item in projection["objects"]}
    left_record = index[CANDIDATE_IDS[0]]
    right_record = index[CANDIDATE_IDS[1]]
    left = projected[CANDIDATE_IDS[0]]
    right = projected[CANDIDATE_IDS[1]]

    context_name = str(context.get("name_zh") or context.get("name_en") or CONTEXT_ID)
    left_name = left["label"]
    right_name = right["label"]

    dimensions = (
        ("开放源码", "open_source"),
        ("完整平台可自托管", "self_hostable"),
        ("部署方式", "deployment_models"),
        ("许可证表达", "license_expression"),
    )

    parts = [
        "<h1>比较 Forgejo Actions 与 GitHub Actions</h1>",
        '<div class="compare-context">',
        '<strong>比较上下文：</strong> ',
        _link(context, context_name),
        "<p>候选集合来自 Workspace Selection V1。Compare 只读取投影，不创造新的 Canonical 事实。</p>",
        f'<p class="muted">选择依据：{html.escape(str(projection["selection"]["selection_reason"]))}</p>',
        "</div>",
        '<div class="compare-candidates">',
        f'<div class="card"><strong>候选 A</strong><p>{_link(left_record, left_name)}</p><p>{html.escape(str(left_record.get("summary_zh") or ""))}</p></div>',
        f'<div class="card"><strong>候选 B</strong><p>{_link(right_record, right_name)}</p><p>{html.escape(str(right_record.get("summary_zh") or ""))}</p></div>',
        "</div>",
    ]

    for dimension, field in dimensions:
        left_field = left["fields"][field]
        right_field = right["fields"][field]
        parts.extend(
            [
                '<section class="compare-dimension">',
                f"<h2>{html.escape(dimension)}</h2>",
                '<div class="compare-values">',
                f'<div class="compare-value"><strong>{html.escape(left_name)}</strong><span>{html.escape(_value_label(left_field))}</span>{_evidence_html(left_field)}</div>',
                f'<div class="compare-value"><strong>{html.escape(right_name)}</strong><span>{html.escape(_value_label(right_field))}</span>{_evidence_html(right_field)}</div>',
                "</div></section>",
            ]
        )

    conditions = str(relation.get("conditions_zh") or "")
    parts.extend(
        [
            '<section class="compare-boundary">',
            "<h2>关系语义边界</h2>",
            f"<p><strong>关系类型：alternative_to。</strong> {html.escape(conditions)}</p>",
            "<p><strong>本页不输出 winner（胜者）、overall score（总分）或推荐结论。</strong>这些边界由 Workspace Projection V1 明确声明。</p>",
            "<p>“当前记录未提供”是机器可区分的 not_recorded 状态，不等于 false、none 或现实中不存在该属性。</p>",
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
