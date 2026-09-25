"""Synthetic control fixtures; no naming quality or real screening claims."""
import copy
import json
from validate_evidence import REQUIRED, validate

def base():
    return {
        'record_kind': 'synthetic', 'owner_paused': True,
        'generation_resume_requested': False,
        'artifacts': [
            {'id': 'IN', 'kind': 'synthetic', 'text': '比较匿名样例的结构。'},
            {'id': 'OUT', 'kind': 'synthetic', 'text': 'A、B、C 为匿名测试 ID，不是名称。'},
            {'id': 'FB', 'kind': 'synthetic', 'text': '我更喜欢A，B暂时没有感觉。'}],
        'batches': [{
            'batch_id': 'SYN-1', 'purpose': 'exploration',
            'method_ref': 'pilot-v0.1', 'runtime': {'level': 'synthetic'},
            'inputs': ['IN'], 'outputs': ['OUT'],
            'stages': {'generated': ['A', 'B', 'C'], 'intrinsic': ['A', 'B'], 'reality': ['A'], 'exposed': ['A']},
            'decisions': [
                {'candidate_id': 'C', 'from': 'generated', 'to': 'intrinsic', 'reason': '合成质量淘汰'},
                {'candidate_id': 'B', 'from': 'intrinsic', 'to': 'reality', 'reason': '合成现实淘汰'}],
            'feedback': [{'source_artifact': 'FB', 'quote': '我更喜欢A，B暂时没有感觉。',
                          'interpretation': '原因未知；短度仅作为待验证解释。', 'basis': 'inference', 'role': 'prefer'}],
            'screenings': [{'candidate_id': 'A', 'claim': 'available', 'observed_at': '2026-09-11T00:00:00Z',
                'queries': [{'intent': i, 'source': 'synthetic-fixture', 'result': '仅合成测试'} for i in ('identity', 'public_tm', 'domain')]}],
            'batch_review': {'assessment': '筛查导致集合缩小；原因未由名称判断。', 'stage_observations': {'generated': '三项', 'intrinsic': '两项', 'reality': '一项', 'exposed': '一项'}, 'evidence_refs': ['OUT'], 'scope': 'synthetic'}}],
        'recovery': {key: {'status': 'present', 'value': '合成状态'} for key in REQUIRED}}

def run():
    results = []
    def check(name, change, expected_error=None, gap=None, previous=None):
        record = base()
        change(record)
        result = validate(record, previous)
        ok = expected_error in result['errors'] if expected_error else gap in result['gaps'] if gap else result['capture_complete']
        results.append({'case': name, 'input': record, 'previous': previous, 'actual': result, 'passed': ok})
    check('完整匿名合成链', lambda r: None)
    check('允许声明同族探索', lambda r: (r['batches'][0].update(purpose='exploitation'), r['batches'][0]['batch_review'].update(assessment='有预算的同族对比，不要求固定类数')))
    check('缺少实际输入', lambda r: r['batches'][0].update(inputs=[]), gap='inputs_missing')
    check('不存在的产物引用', lambda r: r['batches'][0].update(outputs=['MISSING']), expected_error='artifact_reference_missing')
    check('转述冒充直接反馈', lambda r: (r['artifacts'][2].update(kind='reported'), r['batches'][0]['feedback'][0].update(basis='direct_reason')), expected_error='reported_feedback_promoted_to_direct')
    check('推断升级硬门槛', lambda r: r['batches'][0]['feedback'][0].update(role='gate'), expected_error='gate_without_direct_authorization')
    check('筛选后新增候选', lambda r: r['batches'][0]['stages'].update(intrinsic=['A', 'B', 'Z']), expected_error='candidate_added_after_generation')
    check('缺少去留依据', lambda r: r['batches'][0].update(decisions=[]), expected_error='drop_reason_missing')
    check('域名结论缺查询', lambda r: r['batches'][0]['screenings'][0].update(queries=[]), expected_error='available_without_required_evidence')
    check('恢复字段静默丢失', lambda r: r['recovery'].pop('search_landscape'), expected_error='recovery_entry_dropped:search_landscape', previous=base())
    check('诚实记录历史未知', lambda r: r['recovery'].update(search_landscape={'status': 'unknown', 'reason': '原始记录未找到'}), gap='recovery_unknown:search_landscape')
    check('重建不能冒充原始输出', lambda r: (r.update(record_kind='reconstruction'), r['artifacts'][1].update(kind='reconstructed')), gap='outputs_not_original')
    check('用户暂停优先', lambda r: r.update(generation_resume_requested=True), expected_error='resume_not_ready')
    check('空批次不是完整链', lambda r: r.update(batches=[]), gap='batches_missing')
    check('原始证据缺出处', lambda r: (r.update(record_kind='live'), [a.update(kind='original') for a in r['artifacts']]), gap='original_source_locator_missing')
    check('合成反馈混入真实记录', lambda r: r.update(record_kind='live'), expected_error='synthetic_artifact_in_real_record')
    check('占位审查不足', lambda r: r['batches'][0].update(batch_review={'checked': True}), gap='batch_review_missing')
    check('反馈角色缺失', lambda r: r['batches'][0]['feedback'][0].pop('role'), expected_error='feedback_role_invalid')
    check('未展示项错误筛查仍检查', lambda r: r['batches'][0]['screenings'].append({'candidate_id': 'B', 'claim': 'available', 'queries': []}), expected_error='available_without_required_evidence')
    check('筛查结论缺失', lambda r: r['batches'][0]['screenings'][0].pop('claim'), expected_error='screen_claim_missing')
    check('本地原始产物有执行定位', lambda r: (r.update(record_kind='live'), [a.update(kind='original', origin='local_execution', execution_ref='synthetic-test-execution') for a in r['artifacts']]))
    report = {'test_kind': 'synthetic_structural_regression', 'passed': sum(x['passed'] for x in results), 'total': len(results), 'cases': results,
              'limits': '不是历史重放，不测试名称质量，不证明偏好解释或现实结果真实。'}
    with open('test-results.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(json.dumps({k: v for k, v in report.items() if k != 'cases'}, ensure_ascii=False))
    return 0 if all(x['passed'] for x in results) else 1

if __name__ == '__main__':
    raise SystemExit(run())
