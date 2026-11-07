"""Recover SEM-408-003 from retained Actions logs. Never invokes a model.

Raw job logs remain distinct from original HTTP responses / runner workspace.
Collect and upload an artifact BEFORE optimistic, non-force repository publication.
"""
from __future__ import annotations
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import unittest
from unittest.mock import patch
import tempfile
import urllib.error
import urllib.request

REPO = 'InteropAtlas/InteropAtlas'
BRANCH = 'feat/adaptive-naming-skill-v0.1'
RUN = 34737301186
JOB = 103670853467
SOURCE = '3b2144413d938bde7cfe1772ec60efd635365e2d'
STATE = '03_Evolution/01_Research/03_Tests/organization-naming-411-state.yaml'
STATE_BLOB = '769a87ceb3055123b1aa157225ccbb45cdd54992'
HOME = '03_Evolution/01_Research/03_Tests/naming-evidence-pilot/model-aware/semantic-review-pilot-003'
RESULT = HOME + '/results/recovery-run-34737301186'
EXPECTED = dict(zip(('C001','C002','C003','C004','C005','C006'),
                    ('Scribble','Diffly','Linetap','SideBy','Textal','Sublyte')))
ERROR = 'AssertionError: branch changed during frozen run'
NEXT = 'qualify_independent_reviewer_task_understanding_before_further_inference'


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


class SafeRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        redirected = super().redirect_request(req, fp, code, msg, headers, newurl)
        if redirected is not None:
            redirected.remove_header('Authorization')
        return redirected


def api(path, method='GET', body=None, raw=False, absent_ok=False):
    request = urllib.request.Request('https://api.github.com/repos/' + REPO + path,
        method=method, data=encoded(body) if body is not None else None,
        headers={'Authorization': 'Bearer ' + os.environ['GH_TOKEN'],
                 'Accept': 'application/vnd.github+json', 'Content-Type': 'application/json'})
    try:
        with urllib.request.build_opener(SafeRedirect).open(request, timeout=60) as response:
            data = response.read(5_000_001)
    except urllib.error.HTTPError as error:
        if error.code == 404 and absent_ok:
            return None
        raise
    if len(data) > 5_000_000:
        raise ValueError('response_exceeds_bounded_capture_size')
    return data if raw else json.loads(data)


def extract(log):
    text = log.decode('utf-8-sig')
    rows = []
    for number, line in enumerate(text.splitlines(), 1):
        match = re.match(r'^(\d{4}-\d\d-\d\dT\S+Z) (\{.*\})$', line)
        if not match:
            continue
        value = json.loads(match[2])
        if 'id' not in value or 'name' not in value or 'status' not in value:
            continue
        if value['id'] not in EXPECTED or EXPECTED[value['id']] != value['name']:
            raise ValueError('unexpected_candidate')
        if any(row['record']['id'] == value['id'] for row in rows):
            raise ValueError('duplicate_candidate')
        if value['status'] != 'review_complete_not_truth' or value.get('review', {}).get('id') != value['id']:
            raise ValueError('unexpected_result_shape')
        for key in ('input_tokens', 'output_tokens'):
            if type(value.get(key)) is not int or value[key] < 0:
                raise ValueError('invalid_token_count')
        rows.append({'log_line': number, 'logged_at': match[1], 'record': value})
    if [row['record']['id'] for row in rows] != list(EXPECTED):
        raise ValueError('incomplete_or_reordered_log_records')
    if ERROR not in text:
        raise ValueError('missing_archival_failure_evidence')
    return rows


def patch_state(text, recovery):
    if text.count('  snapshot_version: 95\n') != 1 or '\nsemantic_review_recovery:' in text:
        raise ValueError('state_has_advanced_or_already_recovered')
    match = re.search(r'^next_action:\n.*?(?=^stop:\n)', text, re.M | re.S)
    if match is None or 'design_independent_semantic_validation_on_existing_candidates' not in match[0]:
        raise ValueError('unexpected_next_action')
    replacement = ('next_action:\n  action: ' + NEXT + '\n  rationale: >-\n'
        '    SEM-408-003已经执行六次，但归档因分支推进失败；现仅恢复Actions日志，不是完整原始响应。\n'
        '    事后审计发现把名称当产品、把说明词当名称和循环论证；不能把六项hold当质量结论。\n'
        '    先在既有材料上定义最小任务理解对照及停止条件，确认能区分命名对象与产品能力，\n'
        '    再决定是否进行一个有界真实canary；不直接重跑六项，不改selector、不新增名称。\n'
        '  requires_owner: false_for_bounded_method_research_no_paid_or_ia_generation\n\n')
    updated = text[:match.start()] + replacement + text[match.end():]
    updated = updated.replace('  snapshot_version: 95\n', '  snapshot_version: 96\n', 1)
    section = {
        'id': 'SEM-408-003-RECOVERY-01', 'primary_issue': 408,
        'status': 'executed_log_recovered_semantic_validity_not_established',
        'source_run': RUN, 'source_job': JOB, 'source_commit': SOURCE,
        'record': RESULT.replace('03_Evolution/01_Research/03_Tests/', '') + '/recovery.json',
        'report': HOME.replace('03_Evolution/01_Research/03_Tests/', '') + '/REPORT.zh-CN.md',
        'logged_completed_review_calls': len(recovery['records']),
        'new_model_calls_this_recovery': 0,
        'capture_class': 'retained_actions_log_not_original_http_workspace',
        'original_workspace_recovered': False,
        'independent_reviewer_execution': 'cross_family_single_candidate_code_and_log_evidence',
        'independent_semantic_validation_passed': False,
        'posthoc_audit': 'controller_assessment_not_new_independent_review',
        'cross_model_quality_comparison': 'withheld',
        'quality_ground_truth': None, 'new_names': 0, 'paid_api_calls': 0,
        'ia_generation': False, 'stable_promotion': False,
        'historical_counts_scope_unchanged': True}
    return updated.rstrip() + '\n\n# v96: execution, capture and semantic validity are separate.\nsemantic_review_recovery:\n  ' + json.dumps(section, ensure_ascii=False, indent=2).replace('\n', '\n  ') + '\n'


REPORT = '''# SEM-408-003：日志恢复与语义有效性审计（v96）

## 1. 实际执行与可恢复证据

Primary Home：#408；#411 真实组织命名仍暂停，#416 保持 Draft。执行者：OpenAI / ChatGPT / GPT-6 Astra Pro。审计类别：读取原始日志后的 Controller 事后分析，不是新增独立盲评。

原运行 `34737301186` / job `103670853467` 在 2026-09-13 06:20:36 UTC 开始，06:27:44 UTC 结束。源码冻结在 `3b2144413d938bde7cfe1772ec60efd635365e2d`。运行已结束，不再是 queued；六个独立请求均在日志中留下 `review_complete_not_truth` 记录。原日志内六项均为 hold、brief_fit 均 weak；这些是模型输出，不是审计认可的质量标签。

失败发生在后续归档：`AssertionError: branch changed during frozen run`。分支推进保护有效阻止了旧源码基线上的写回；缺陷是此前没有独立 artifact 备份，归档把来源 commit 与投递时 branch head 耦合。原运行 artifacts API 返回 0。本轮保留完整可下载 job log、运行/job/artifact 元数据快照及按行派生的六项记录；不重跑模型，不把后补记录伪装成原 runner workspace。

记录入口：`results/recovery-run-34737301186/recovery.json`；原始留存日志：同目录 `job.log`；重算程序：`recover.py`。日志 SHA256、记录所在行号和原 logged_at 均在 recovery.json；原HTTP响应、渲染后的实际token请求、server.log、plan内GGUF hash等没有从此次运行恢复。可确认声明的模型/固定代码与实际输出，不可补填为逐字完整请求或已核实权重哈希。

## 2. 为什么不能进行可信的跨模型质量比较

下列判断是可复核的 Controller 解释，原文不修改：

| 既有候选ID | 日志中的问题 | 审计意义 |
| --- | --- | --- |
| C001 | 用名称不具备 inherent analytical value 解释弱匹配 | 可能把产品能力当作裸名必须自身具备的属性，违反本次明确的非字面编码边界 |
| C002 | 把 frozen brief、validation 写进名称观察/联想，进而评价 fragmented system | 混淆任务说明、命名对象与候选词形 |
| C003 | 理由为 “It’s a name, not a tool.” | 以“名称不是工具”否定命名，构成任务层级错误 |
| C004 | 用 lacks inherent product features 解释弱匹配；多个联想夹在一个带列表残片的字符串中 | 结构可解析不等于语义或内容表示正确 |
| C005 | 联想含 “a specific type ofal”，其余包含笼统好评 | 联想与理由缺少可依赖的候选级依据，不据此认定名称好或坏 |
| C006 | 观察和最终理由都只是名称包含自身 | 通过包含名称的字符串门槛，仍然是循环陈述 |

`substantive()` 只检查禁用占位短语、包含候选名和字符串长度，能让上述循环陈述通过。因此本轮不能把“canary_passed / review_complete_not_truth”升级为“独立语义验证通过”。这不是以六项都 hold 本身判定失败；依据是具体理由与任务要求的错位。也不据此泛化为 Gemma 家族或所有小模型无效。

Gemma 使用单候选裸名；Qwen-v95 使用批量候选和生成者意图等不同输入。即便未来 reviewer 有效，差异也不能只归因于模型家族。当前不计算名称质量胜率、不让这六项覆盖 Qwen 的 priority/hold、不选择 winner，也不让 ChatGPT 变成隐藏运行时兜底。

## 3. 已完成修复与下一步

恢复采用先写本地证据、再独立上传 artifact、最后受保护投递的顺序。投递使用最新父提交，但要求目标 state 的 blob 与预期相同、新证据路径不存在；不 force、不覆盖别人的新 state。若分支竞争发生，公开 artifact 仍保留，不能为了让任务变绿而改写历史或自动重跑模型。

state 只将 snapshot95 更新为96、替换过时 next_action 并追加本轮来源/限制，其余使命、偏好、候选、Skill v0.4.0、历史计数和实验原判定保留。NAMING_RECOVERY.md 的稳定路径不变，不重复维护第二套状态。

下一动作：先用既有材料冻结一个最小“任务理解”对照，检查 reviewer 是否在评价名称而不是要求名称本身实现产品功能；明确可接受依据、任务错位与循环陈述的停止条件，然后才决定单项真实 canary。不是继续加 selector 规则，也不是立刻再跑六项。当前无新增名称、无新增模型调用、无付费推理API、无现实查询/购买注册、无IA/G0–G8恢复、无合并或稳定晋升。
'''


def collect(output):
    output.mkdir(parents=True, exist_ok=False)
    run = api(f'/actions/runs/{RUN}')
    job = api(f'/actions/jobs/{JOB}')
    artifacts = api(f'/actions/runs/{RUN}/artifacts')
    if run['status'] != 'completed' or run['head_sha'] != SOURCE or job['run_id'] != RUN:
        raise ValueError('source_identity_or_completion_mismatch')
    log = api(f'/actions/jobs/{JOB}/logs', raw=True)
    (output / 'job.log').write_bytes(log)
    for name, value in [('source-run.json', run), ('source-job.json', job), ('source-artifacts.json', artifacts)]:
        (output / name).write_bytes(encoded(value))
    records = extract(log)
    if not all(r['record']['review']['disposition'] == 'hold' and r['record']['review']['brief_fit']['level'] == 'weak' for r in records):
        raise ValueError('log_differs_from_audited_result_do_not_publish_static_report')
    recovery = {'id': 'SEM-408-003-RECOVERY-01', 'source_run': RUN, 'source_job': JOB,
        'source_commit': SOURCE, 'log_sha256': hashlib.sha256(log).hexdigest(),
        'capture_class': 'retained_actions_stdout_not_original_http_workspace',
        'records': records, 'logged_completed_review_calls': len(records),
        'logged_input_tokens': sum(r['record']['input_tokens'] for r in records),
        'logged_output_tokens': sum(r['record']['output_tokens'] for r in records),
        'logged_inference_seconds': sum(r['record']['seconds'] for r in records),
        'artifact_count_observed': artifacts['total_count'], 'new_model_calls_this_recovery': 0,
        'original_workspace_recovered': False, 'semantic_validation_passed': False,
        'quality_ground_truth': None, 'cross_model_quality_comparison': 'withheld'}
    (output / 'recovery.json').write_bytes(encoded(recovery))
    print(json.dumps({key: value for key, value in recovery.items() if key != 'records'}, ensure_ascii=False))


def publish(output):
    recovery = json.loads((output / 'recovery.json').read_bytes())
    log = (output / 'job.log').read_bytes()
    if hashlib.sha256(log).hexdigest() != recovery['log_sha256'] or extract(log) != recovery['records']:
        raise ValueError('evidence_integrity_mismatch')
    current = api('/git/ref/heads/' + BRANCH)['object']['sha']
    state = api('/contents/' + STATE + '?ref=' + current)
    if state['sha'] != STATE_BLOB:
        raise ValueError('state_changed_keep_artifact_do_not_overwrite')
    replacement = patch_state(base64.b64decode(state['content']).decode(), recovery)
    entries = [{'path': STATE, 'mode': '100644', 'type': 'blob', 'content': replacement}]
    documents = {RESULT + '/' + p.name: p.read_bytes().decode('utf-8') for p in output.iterdir() if p.is_file()}
    documents[HOME + '/REPORT.zh-CN.md'] = REPORT
    for path, content in documents.items():
        if api('/contents/' + path + '?ref=' + current, absent_ok=True) is not None:
            raise ValueError('destination_exists_keep_artifact_do_not_overwrite: ' + path)
        entries.append({'path': path, 'mode': '100644', 'type': 'blob', 'content': content})
    tree = api('/git/trees', 'POST', {'base_tree': api('/git/commits/' + current)['tree']['sha'], 'tree': entries})['sha']
    commit = api('/git/commits', 'POST', {'message': 'evidence(#408): recover SEM-408-003 logs and reconcile snapshot96\n\nNo model calls, original HTTP reconstruction, semantic approval, IA generation or promotion.\nExecutor: OpenAI / ChatGPT / GPT-6 Astra Pro', 'tree': tree, 'parents': [current]})['sha']
    api('/git/refs/heads/' + BRANCH, 'PATCH', {'sha': commit, 'force': False})
    print(json.dumps({'published_commit': commit, 'parent': current, 'source_run_commit': SOURCE,
                      'files': len(entries), 'snapshot_version': 96, 'new_model_calls': 0}))


class RecoveryTests(unittest.TestCase):
    def fixture(self):
        lines = []
        for id_, name in EXPECTED.items():
            record = {'id': id_, 'name': name, 'status': 'review_complete_not_truth',
                      'review': {'id': id_}, 'input_tokens': 1, 'output_tokens': 2, 'seconds': 3.0}
            lines.append('2026-09-13T06:24:49.0000000Z ' + json.dumps(record))
        return ('\n'.join(lines) + '\n' + ERROR).encode()
    def test_six_log_records_not_semantic_proof(self): self.assertEqual(len(extract(self.fixture())), 6)
    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError): extract(self.fixture() + b'\n' + self.fixture())
    def test_missing_candidate_rejected(self):
        with self.assertRaises(ValueError): extract(b'\n'.join(self.fixture().splitlines()[1:]))
    def test_wrong_name_rejected(self):
        with self.assertRaises(ValueError): extract(self.fixture().replace(b'Scribble', b'Diffly', 1))
    def test_missing_archival_error_rejected(self):
        with self.assertRaises(ValueError): extract(self.fixture().replace(ERROR.encode(), b''))
    def test_boolean_token_rejected(self):
        with self.assertRaises(ValueError): extract(self.fixture().replace(b'"input_tokens": 1', b'"input_tokens": true', 1))
    def test_patch_is_bounded(self):
        old = 'task:\n  snapshot_version: 95\n  skill_version: 0.4.0\n\nnext_action:\n  action: design_independent_semantic_validation_on_existing_candidates\n\nstop:\n  status: generation_paused_process_review_active\n'
        new = patch_state(old, {'records': extract(self.fixture())})
        self.assertIn('snapshot_version: 96', new)
        self.assertIn('skill_version: 0.4.0', new)
        self.assertIn('generation_paused_process_review_active', new)
        self.assertIn(NEXT, new)
        with self.assertRaises(ValueError): patch_state(new, {'records': []})
    def test_redirect_drops_credential(self):
        req = urllib.request.Request('https://api.github.com/a', headers={'Authorization': 'Bearer fixture'})
        redirected = SafeRedirect().redirect_request(req, None, 302, '', {}, 'https://example.com/log')
        self.assertIsNone(redirected.get_header('Authorization'))
    def publication(self, scenario):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            log = self.fixture().replace(b'\n', b'\r\n')
            (output / 'job.log').write_bytes(log)
            recovery = {'records': extract(log), 'log_sha256': hashlib.sha256(log).hexdigest()}
            (output / 'recovery.json').write_bytes(encoded(recovery))
            old = 'task:\n  snapshot_version: 95\nnext_action:\n  action: design_independent_semantic_validation_on_existing_candidates\nstop:\n  status: generation_paused_process_review_active\n'
            calls = []
            def fake_api(path, method='GET', body=None, **kwargs):
                calls.append((path, method, body))
                if path.startswith('/git/ref/heads/'):
                    return {'object': {'sha': 'new-parent'}}
                if path.startswith('/contents/' + STATE):
                    return {'sha': 'changed' if scenario == 'changed_state' else STATE_BLOB,
                            'content': base64.b64encode(old.encode()).decode()}
                if path.startswith('/contents/'):
                    return {'sha': 'existing'} if scenario == 'existing_destination' else None
                if path == '/git/commits/new-parent': return {'tree': {'sha': 'current-tree'}}
                if path == '/git/trees':
                    self.assertEqual(body['base_tree'], 'current-tree')
                    logged = next(v for v in body['tree'] if v['path'].endswith('/job.log'))
                    self.assertEqual(logged['content'].encode(), log)
                    return {'sha': 'new-tree'}
                if path == '/git/commits':
                    self.assertEqual(body['parents'], ['new-parent'])
                    return {'sha': 'new-commit'}
                if path.startswith('/git/refs/heads/'):
                    self.assertFalse(body['force'])
                    if scenario == 'conflict': raise RuntimeError('simulated_ref_conflict')
                    return {'object': {'sha': 'new-commit'}}
                raise AssertionError(path)
            with patch(__name__ + '.api', side_effect=fake_api):
                if scenario in ('changed_state', 'existing_destination'):
                    with self.assertRaises(ValueError): publish(output)
                    self.assertFalse(any(method != 'GET' for _, method, _ in calls))
                elif scenario == 'conflict':
                    with self.assertRaises(RuntimeError): publish(output)
                else: publish(output)
            self.assertEqual((output / 'job.log').read_bytes(), log)
    def test_changed_state_no_write(self): self.publication('changed_state')
    def test_existing_destination_no_write(self): self.publication('existing_destination')
    def test_new_parent_and_exact_crlf_bytes(self): self.publication('success')
    def test_ref_conflict_preserves_local_evidence(self): self.publication('conflict')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['test', 'collect', 'publish'])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.command == 'test':
        unittest.main(argv=['recover.py'], verbosity=2)
    elif args.output is None:
        parser.error('--output is required')
    else:
        (collect if args.command == 'collect' else publish)(args.output)
