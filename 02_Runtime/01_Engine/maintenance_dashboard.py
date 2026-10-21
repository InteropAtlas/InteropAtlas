#!/usr/bin/env python3
"""Read-only public GitHub snapshot; a generated view, never task authority."""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timedelta, timezone
from html import escape
import json
from pathlib import Path
import urllib.request

REPO = 'InteropAtlas/InteropAtlas'
WEB = 'https://github.com/' + REPO
API = 'https://api.github.com/repos/' + REPO


def fetch_pages(resource, stop_before=None):
    rows = []
    for page in range(1, 101):
        request = urllib.request.Request(f'{API}/{resource}&per_page=100&page={page}', headers={'Accept': 'application/vnd.github+json', 'User-Agent': 'InteropAtlas-maintenance-view'})
        with urllib.request.urlopen(request, timeout=30) as response:
            batch = json.load(response)
        if not isinstance(batch, list):
            raise ValueError('Expected GitHub collection')
        rows.extend(batch)
        if len(batch) < 100 or (stop_before and batch[-1]['updated_at'] < stop_before):
            return rows
    raise ValueError('Pagination incomplete')


def compact(row):
    # Public fields only; never publish bodies, comments, credentials or private context.
    return {key: row.get(key) for key in ('number', 'title', 'html_url', 'updated_at', 'merged_at', 'draft')} | {
        'waiting_known': 'issue_field_values' in row,
        'waiting': next((x.get('single_select_option', {}).get('name') for x in row.get('issue_field_values', []) if x.get('issue_field_name') == 'Waiting For'), None)
    }


def collect(now=None):
    now = now or datetime.now(timezone.utc)
    cutoff = (now - timedelta(days=13)).date().isoformat()
    snapshot = {'generated_at': now.isoformat(), 'window_start': cutoff, 'sources': {}, 'errors': []}
    for key, resource in [('open_prs', 'pulls?state=open'), ('issues', 'issues?state=open'), ('merged_prs', 'pulls?state=closed&base=main&sort=updated&direction=desc')]:
        try:
            rows = fetch_pages(resource, cutoff if key == 'merged_prs' else None)
            if key == 'issues':
                rows = [r for r in rows if 'pull_request' not in r]
            if key == 'merged_prs':
                rows = [r for r in rows if r.get('merged_at') and r['merged_at'][:10] >= cutoff]
            snapshot['sources'][key] = [compact(r) for r in rows]
        except (OSError, ValueError, KeyError) as exc:
            snapshot['sources'][key] = None
            snapshot['errors'].append(key)  # Never serialize exception URLs/headers.
    return snapshot


def link(row):
    # Construct destination from numeric IDs, not untrusted external URLs.
    number = int(row['number'])
    return f'<a href="{WEB}/issues/{number}">{escape(str(row.get("title") or "未命名工作"))}</a>'


# Presentation-only translations of public titles, not a manually maintained status list.
TITLE_SUMMARIES = {
    'Legacy Reader Retirement / Archive Mode': '旧版读取方式的退役与归档',
    'Canonical Writer Cutover Gate': '正式知识写入工具的切换条件',
    'Public Intake Launch Checklist / Contribution-Ready Announcement': '开放外部贡献前的准备清单与公告',

    'fix: remove unsupported RFC3339 to ISO 8601-1:2019 edge': '纠正一条时间标准之间缺乏依据的关系',
    'data: add bounded FHIR Python model implementation precedent': '补充医疗数据的软件实现先例',
    'data: add bounded Python GeoJSON implementation precedent': '补充地理数据的软件实现先例',
    'research: 留存 UBL XSD 与空元素约束的有界反例': '记录电子商务文档验证中的一个反例',
    'intake: 收录有界 Python xmlschema 验证先例': '补充 XML 数据格式验证工具的先例',
    'intake: 补齐 UBL 固定 XML 与 XSD 引用路径': '补齐电子商务文档格式的标准依据',
    'intake: 收录 HTTPX 的有界 HTTP 客户端实现先例': '补充网络请求工具的实现先例',
    'docs: 修复当前任务入口与贡献规范链接': '修复参与入口和贡献说明的链接',
    'feat(naming): Adaptive Naming System v0.4.0': '自适应命名系统的功能提案',
}


def summary(row):
    title = str(row.get('title') or '')
    if title in TITLE_SUMMARIES:
        return TITLE_SUMMARIES[title]
    if any(0x4E00 <= ord(ch) <= 0x9FFF for ch in title):
        return title.split(': ', 1)[-1]
    return '一项项目改动（展开查看原记录）'


def readable_time(value):
    try:
        parsed = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
        if parsed.tzinfo is None:
            return '未知'
        return parsed.astimezone(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M') + '（UTC+8）'
    except (TypeError, ValueError):
        return '未知'


def cards(rows, empty, limit=6, mode='updated'):
    if rows is None:
        return '<p class="notice">本次未能取得数据。状态未知，请到 GitHub 核实。</p>'
    if not rows:
        return f'<p class="muted">{empty}</p>'
    result = []
    for row in sorted(rows, key=lambda r: r.get('merged_at' if mode == 'merged' else 'updated_at') or '', reverse=True)[:limit]:
        label = '合并于' if mode == 'merged' else '记录更新于'
        stamp = readable_time(row.get('merged_at' if mode == 'merged' else 'updated_at'))
        badge = '草稿，尚未交付' if row.get('draft') else ('已合并到主线' if mode == 'merged' else '未关闭，不代表正在执行')
        result.append(f'<li><span class="tag">{badge}</span><h3>{escape(summary(row))}</h3><small>{label} {escape(stamp)}</small><details><summary>查看原始记录与依据</summary>{link(row)}</details></li>')
    return '<ul class="work-list">' + ''.join(result) + '</ul>'


def render(snapshot):
    sources = snapshot.get('sources', {})
    prs, issues, merged = (sources.get(k) for k in ('open_prs', 'issues', 'merged_prs'))
    waiting = None if issues is None or any(not r.get('waiting_known') for r in issues) else [r for r in issues if r.get('waiting')]
    raw_stamp = snapshot.get('generated_at', '未采集')
    stamp = escape(raw_stamp)
    try:
        local_stamp = datetime.fromisoformat(raw_stamp).astimezone(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S') + '（UTC+8）'
    except ValueError:
        local_stamp = '未采集'
    local_stamp = escape(local_stamp)
    cutoff = snapshot.get('window_start')
    chart = '<p class="notice">本次趋势数据未知，不显示为零。</p>'
    if merged is not None and cutoff:
        start = datetime.fromisoformat(cutoff)
        counts = Counter(r['merged_at'][:10] for r in merged)
        peak = max(counts.values(), default=1)
        chart = '<div class="chart" role="list" aria-label="近14个UTC日期每日合并改动数量">'
        for offset in range(14):
            date = (start + timedelta(days=offset)).date().isoformat()
            count = counts[date]
            chart += f'<div class="bar-column" role="listitem" aria-label="{date}：{count} 项"><span>{count}</span><div class="bar" style="height:{max(2, count / peak * 100):.1f}px"></div><small>{date[5:]}</small></div>'
        chart += '</div>'
    wait_html = '<p class="notice">等待条件数据未知。</p>' if waiting is None else ''
    if waiting is not None:
        labels = {'Evidence': '等待更多证据', 'Scale': '等待规模条件成熟', 'Owner': '等待负责人决定'}
        wait_html = '<div class="waiting">' + ''.join(f'<div><strong>{sum(r.get("waiting") == key for r in waiting)}</strong><span>{label}</span></div>' for key, label in labels.items()) + '</div>'
        wait_html += '<p class="muted">包括长期保留事项，不等于今天都要处理。</p>'
        wait_html += cards([r for r in waiting if r.get('waiting') == 'Owner'], '没有标为等待负责人决定的公开工作项。', 3)
    def count(rows):
        return '未知' if rows is None else str(len(rows))
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>维护指挥台 · InteropAtlas</title><style>
:root{{color-scheme:dark;--bg:#0b1422;--panel:#142236;--muted:#b3c3d8;--line:#30445f;--cyan:#80e6df}}*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:#f1f5fb;font:16px/1.65 system-ui,sans-serif}}a{{color:var(--cyan);text-underline-offset:4px}}a:focus-visible{{outline:3px solid #ffd18a;outline-offset:4px}}.wrap{{max-width:1200px;margin:auto;padding:32px 24px}}nav{{display:flex;gap:24px;flex-wrap:wrap}}.eyebrow{{color:var(--cyan);letter-spacing:.16em;font-size:12px;margin-top:44px}}h1{{font-size:clamp(32px,5vw,52px);line-height:1.2;margin:12px 0}}h2{{font-size:22px;margin:0 0 16px}}h3{{font-size:17px}}.muted,small{{color:var(--muted)}}.lead{{font-size:19px;max-width:780px}}.notice{{border-left:3px solid #ffcc80;background:#2c2730;padding:14px 18px}}.stamp{{font-size:14px;overflow-wrap:anywhere}}.metrics{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:28px 0}}.metric,.panel{{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:24px}}.metric strong{{display:block;font-size:34px}}.metric span{{color:var(--muted)}}.grid{{display:flex;flex-wrap:wrap;gap:20px}}.grid>.panel{{flex:1 1 400px;min-width:0}}.grid>.wide{{flex-basis:100%}}.work-list{{list-style:none;padding:0;margin:0}}.work-list li{{padding:17px 0;border-bottom:1px solid var(--line)}}.work-list li:last-child{{border-bottom:0}}.work-list a,.work-list small{{display:block;overflow-wrap:anywhere}}.tag{{color:#ffd18a;font-size:12px}}.chart{{display:flex;align-items:flex-end;gap:8px;min-height:150px;overflow-x:auto;padding-top:10px}}.bar-column{{flex:1;min-width:38px;text-align:center;font-size:13px}}.bar{{background:var(--cyan);border-radius:4px 4px 0 0;margin:4px auto;width:80%;max-width:42px}}.bar-column small{{font-size:11px;white-space:nowrap}}.waiting{{display:flex;gap:24px;flex-wrap:wrap}}.waiting strong{{display:block;font-size:28px}}.waiting span{{font-size:14px;color:var(--muted)}}footer{{padding:28px 0;color:var(--muted);font-size:14px}}details{{margin-top:18px}}details:not([open])>:not(summary){{display:none}}summary{{cursor:pointer}}@media(max-width:700px){{.grid>.panel{{flex-basis:100%}}.metrics{{grid-template-columns:1fr}}.wrap{{padding:24px 16px}}.metric{{padding:16px}}.metric strong{{display:inline;margin-right:14px}}.chart{{gap:3px}}.bar-column{{min-width:0;font-size:11px}}.bar-column small{{font-size:9px}}.bar-column:nth-child(even) small{{visibility:hidden}}}}
</style></head><body><main class="wrap"><nav aria-label="页面导航"><a href="index.html">← 知识地图</a><a href="{WEB}/issues">公开工作项</a><a href="{WEB}/pulls">改动记录</a></nav>
<p class="eyebrow">INTEROPATLAS / MAINTENANCE DESK</p><h1>维护指挥台</h1><p class="lead">最近交付了什么，还有什么没落地，接下来该关注哪里。</p>
<p class="notice"><strong>更新于 {local_stamp}</strong><br>这是最近一次公开记录，不是实时在线状态。<a href="#data-notes">了解数据边界</a></p>
<div class="metrics"><div class="metric"><strong>{count(merged)}</strong><span>近14个UTC日期已合并改动</span></div><div class="metric"><strong>{count(prs)}</strong><span>未合并提案（含草稿）</span></div><div class="metric"><strong>持续积累</strong><span>标准与先例没有已知总量，不计算完成率</span></div></div>
<div class="grid"><section class="panel wide"><h2>交付活动 / 近14天</h2><p class="muted">每日合并改动数（UTC，含今天的未完整日期）。衡量留下了多少交付记录，不评价个人效率或知识覆盖率。</p>{chart}</section><section class="panel"><h2>01 / 还有什么没交付</h2><p class="muted">公开提案中的未完成事项。草稿可能已搁置，不能据此判断正在开工。</p>{cards(prs, '采集时没有未合并提案；不代表没有人在工作。')}<p><a href="{WEB}/pulls">查看全部提案 →</a></p></section>
<section class="panel"><h2>02 / 最近解决和补充了什么</h2><p class="muted">以下改动已被项目接受，打开记录可看具体内容。</p>{cards(merged, '此时间窗口内没有已合并改动。', mode='merged')}<p><a href="{WEB}/pulls?q=is%3Apr+is%3Amerged">查看全部已合并改动 →</a></p></section>

<section class="panel"><h2>03 / 阻塞与需决定</h2>{wait_html}<p><a href="{WEB}/issues">核实等待条件和依赖 →</a></p></section>
<section class="panel"><h2>04 / 下一阶段看什么</h2><p>下一项具体开工任务：<strong>本快照未确认</strong>。不会把未关闭的愿望清单自动当作承诺。</p><ol><li>先核实未合并提案是否仍有效，以及审核反馈。</li><li>从已有工作项确认下一项可推进工作及其等待条件。</li><li>标准与成熟先例持续补充，按证据逐项积累，不承诺“还差多少”。</li></ol><p class="muted">这是阅读顺序建议，不是新增排期或任务授权。</p><a href="{WEB}/blob/main/PROJECT_STATE.md">查看项目参与入口 →</a></section></div>
<footer id="data-notes"><strong>数据来源：项目公开的改动与工作项</strong><p>中文摘要帮助阅读，不替代原始记录。<a href="{WEB}/actions/workflows/pages.yml">查看网站构建记录</a></p><details><summary>数据边界、更新时间与下载</summary><p>采集时间（UTC）：{stamp}。随现有网站构建更新，不会因打开页面自动刷新。当前执行者、正在运行的会话与下一次交付时间未接入可靠公开数据；最近记录不等于此刻仍在运行，没有新记录也不能证明工作已停止。</p><p>来源：GitHub 公开 Pull Requests、Issues 的 Waiting For 字段。只读投影，不修改任务、权限或知识事实。工作项总数不是待补标准数量；等待标记缺失不代表无阻塞。中文摘要是公开标题的展示翻译，不新增项目分类。合并不等于解决了所有相关问题。</p><p>不同数据源依次采集，可能有短暂时间差。采集失败显示“未知”，不沿用旧值冒充新数据。已关闭但未合并的提案不计入交付。未接入 GitHub Project 的实时执行状态、私人对话或内部审批记录。</p><p><a href="maintenance-snapshot.json">下载本次公开数据快照</a> · <a href="{WEB}/blob/main/02_Runtime/01_Engine/maintenance_dashboard.py">查看生成逻辑</a></p></details></footer></main></body></html>'''


def build(output, snapshot=None):
    snapshot = snapshot or {'sources': {}, 'generated_at': '未采集（本地构建）'}
    output.mkdir(parents=True, exist_ok=True)
    (output / 'maintenance.html').write_text(render(snapshot), encoding='utf-8')
    (output / 'maintenance-snapshot.json').write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('build/site'))
    parser.add_argument('--refresh', action='store_true', help='Read public GitHub data; no credentials or writes')
    args = parser.parse_args()
    build(args.output, collect() if args.refresh else None)
