#!/usr/bin/env python3
"""Human Evidence Workspace presentation backed by workspace-projection-v1."""

from __future__ import annotations

import html

from workspace_projection import NOT_RECORDED, project_evidence


EVIDENCE_STYLE = """
.evidence-workspace{margin:12px 0 18px;padding:12px 14px;border:1px solid var(--border);border-radius:8px;background:var(--card)}
.evidence-workspace p{margin:.4em 0}.evidence-state{font-weight:600}.evidence-boundary{color:var(--muted);font-size:.92em}
"""


def inject_evidence_workspace(content: str, obj: dict) -> str:
    """Add projection semantics beside the existing Human source section without duplicating facts."""

    marker = '<h2 id="evidence">'
    if marker not in content:
        return content

    projection = project_evidence(obj)
    object_id = html.escape(str(projection["object_id"]))
    if projection["evidence_state"] == NOT_RECORDED:
        state_text = "当前 Canonical 记录未提供来源 / Evidence；状态为 not_recorded，不表示现实中不存在依据。"
    else:
        count = len(projection["sources"])
        state_text = f"当前 Evidence Projection 读取到 {count} 条 Canonical sources；此处不维护第二份来源事实。"

    assessment = projection["assessment"]
    if assessment["state"] == NOT_RECORDED:
        assessment_text = "当前未记录 InteropAtlas 自有评估。"
    else:
        assessment_text = (
            f"另有 {len(assessment['notes'])} 条 InteropAtlas 自有说明 / 评估；"
            "它们不是第三方权威来源，也不会被提升为 external evidence。"
        )

    panel = (
        '<div class="evidence-workspace" aria-label="Evidence Workspace">'
        f'<p class="evidence-state">{html.escape(state_text)}</p>'
        f'<p>{html.escape(assessment_text)}</p>'
        f'<p class="evidence-boundary">可恢复路径：Canonical object <code>{object_id}</code> → '
        '<code>sources</code> / <code>notes_zh</code>。Projection 只读，不构成 Canonical 写入。</p>'
        '</div>'
    )
    heading_end = content.find("</h2>", content.find(marker))
    if heading_end == -1:
        return content
    insert_at = heading_end + len("</h2>")
    return content[:insert_at] + panel + content[insert_at:]
