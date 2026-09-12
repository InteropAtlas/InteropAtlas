"""One-shot exact v93-to-v94 integration. No inference or repository writes here."""
from pathlib import Path
import hashlib
import json
import subprocess

HOME=Path('03_Evolution/01_Research/03_Tests/naming-evidence-pilot/model-aware')
BASE='036568195c8996aff710fe75e87982d571ff6d43'
NAMES=['workflow.py','test_workflow.py','SKILL.md','README.md']
for name in NAMES:
    raw=subprocess.check_output(['git','show',BASE+':'+str(HOME/name)])
    assert (HOME/name).read_bytes()==raw,name
path=HOME/'workflow.py';s=path.read_text()
s=s.replace('import local_runner as r\n','import local_runner as r\nimport format_adapter as f\nimport selection_policy as selection\n')
s=s.replace("('workflow.py', 'protocol.py', 'local_runner.py')", "('workflow.py', 'protocol.py', 'local_runner.py', 'format_adapter.py', 'selection_policy.py')")
s=s.replace("runtime: dict, method='redesign'", "runtime: dict, method='simple'")
s=s.replace("plan = {'schema_version': 1,", "plan = {'schema_version': 2, 'selection_policy': selection.VERSION,")
s=s.replace("default='redesign'", "default='simple'")
s=s.replace("    return plan\n\n\nclass LocalBackend", "    require(plan.get('selection_policy') == selection.VERSION, 'explicit_policy_migration_required')\n    return plan\n\n\nclass LocalBackend")
s=s.replace("        return json_answer((directory / 'answer.raw').read_bytes())", "        normalized = normalized_answer(directory, (directory / 'answer.raw').read_bytes(), question)\n        return json_answer(normalized)")
s=s.replace("    parsed = json_answer(raw)  # Invalid raw output stays recorded; no automatic repair.", "    normalized = normalized_answer(directory, raw, question)\n    parsed = json_answer(normalized)  # No semantic repairs or automatic model retries.")
a=s.index('def review_question(');b=s.index('\n\ndef compute_round',a)
s=s[:a]+'''def normalized_answer(directory, raw, question):
    normalized, audit = f.normalize(raw, json.loads(question))
    target = directory / 'normalization.json'
    if target.exists():
        require(p.read(target) == audit, 'normalization_audit_changed')
    else:
        p.write_new(target, audit)
    if audit['action'].startswith('refused_'):
        raise ValueError(audit['action'])
    if audit['changed']:
        target = directory / 'normalized-answer.json'
        if target.exists():
            require(target.read_bytes() == normalized, 'normalized_answer_changed')
        else:
            with target.open('xb') as stream:
                stream.write(normalized)
    return normalized


def review_question(stage, rows):
    return selection.review_question(stage, rows)'''+s[b:]
s=s.replace("    rp = root / ('round-'", "    result.update(selection.resource_queues(result))\n    result['unverified_inquiries'] = selection.inquiry_register(pool)\n    rp = root / ('round-'")
s=s.replace("return [], list(result['intrinsic_shortlist_ids'])", "return [], list(result['screening_queue_ids'])")
s=s.replace("        if row['status'] == 'pass' and verified", "        if ident in result['priority_ids'] and row['status'] == 'pass' and verified")
s=s.replace("(set(result['intrinsic_shortlist_ids']) - seen)", "(set(result['screening_queue_ids']) - seen)")
s=s.replace("else 'awaiting_screening_evidence' if result['intrinsic_shortlist_ids'] else 'no_intrinsic_survivor')", "else 'awaiting_screening_evidence' if result['priority_ids'] else 'awaiting_substantive_hold_resolution' if result['hold_ids'] else 'no_intrinsic_survivor')")
s=s.replace("                'unresolved_screening_ids': unknown,", "                'priority_ids': result['priority_ids'], 'hold_ids': result['hold_ids'],\n                'not_pursued_ids': result['not_pursued_ids'],\n                'unresolved_screening_ids': unknown,")
path.write_text(s)
path=HOME/'test_workflow.py';s=path.read_text();a=s.index('    def test_supplied_screening_checked_then_feedback_without_assistant');b=s.index('    def test_bad_source',a)
s=s[:a]+s[a:b].replace("'C001'","'C002'")+s[b:];path.write_text(s)
path=HOME/'SKILL.md';s=path.read_text().replace('version: 0.1.0-experimental','version: 0.2.0-experimental')
s=s.replace('实验简洁组为一次直接探索；','新建任务默认simple，一次直接探索；显式`--method redesign`仍可作对照。')
s=s.replace('另一次请求才给完整简短说明，','另一次请求才给标注为未经核实的生成者意图，')
s=s.replace('记录keep/hold/drop及理由；hold不是通过。','记录keep/hold/drop及理由。生成者risk保留在原始记录和待查问题登记，不进入质量评审包；生成者词源/意义不是已经验证的语言学或外部事实。程序不能识别全部无依据推断，语义正确性仍需实测。')
s=s.replace('### 核查\n','### 核查\n\n结果分为`priority_ids`、`hold_ids`、`not_pursued_ids`。只自动安排priority进入核查；hold及复核分歧保留，但现实筛查通过本身不能把它升级为推荐。没有priority时明确报告待解决，不凑推荐数量。\n')
s=s.replace('已完成步骤复用，不重发；','完整无歧义的候选数组、匹配名称冗余字段、唯一output_contract包装可无损规范化。原始字节和规范化副本分别保存；内容不全或含冲突仍拒绝。旧计划受代码哈希保护，必须用原Git版本继续或显式迁移，不能直接重解释旧实验。已完成步骤复用，不重发；')
path.write_text(s)
path=HOME/'README.md';s=path.read_text()+'''\n\n## v94：简单默认与选择证据边界

实验Skill为0.2.0，冻结的正式研究Skill仍0.4.0。新任务不传`--method`时为simple；三路线显式选择，不作为默认必需。生成者意图以未核实提案进入评审，risk原文只留在待查登记，不提供质量许可。

priority仅表示值得优先投入核查，hold保留但不自动安排核查/作为推荐展示；已查证现实条件不自动解决语义分歧。不能因所有项待定而强行填足优先队列。`format_adapter.py`只处理完整且唯一的结构差异，保留模型原文和转换记录，不补名字、理由或决定。

旧工作目录的实现哈希会拒绝新代码。复跑001/002/003必须checkout各自冻结源码；不要直接以新默认、新提示或新包装层改写旧结果。

本次选择对照及回执位于`selection-pilot/`，只复用003候选，不新增名称。它检验已暴露缺陷，不是独立盲评、留出任务或方法已普遍有效的证明。
''';path.write_text(s)
expected={
 'workflow.py':'f8e754b45cd7d8f4909b08cc3bdc86444728c85b596a4b284331d967adcf459b',
 'test_workflow.py':'ea36782567ef63519ab89b77e3a6bf471b2492b447e5a5508185a7081b76a6df',
 'SKILL.md':'c0296ce6324e3ede118bec2a9e2a1c99afe68171d6bdcbd8c2deea6e80456e58',
 'README.md':'bd39360e0ab82eb92ff70d9956668cde10f60d0afc9043d538568b90b5bbc9d7',
 'format_adapter.py':'505e4c11776fb64b0bcd64317c450d5d162fc32c70a6f49a95de084f0434d13c',
 'selection_policy.py':'9a3182152d3b5c7a70640d29d96f4c9b51aead8a4b0c7350e82fd00ddb13f3f7',
 'test_selection_policy.py':'1b6fc1a68cf1dd6a83f37b3530956627279319c1855959f29b9f1829c87c628e',
 'selection-pilot/run.py':'25af17e324d4537c42d5fc2c204b7269f770a4fbaf67a1048c4d3eb25322ceee'}
for name,sha in expected.items():assert hashlib.sha256((HOME/name).read_bytes()).hexdigest()==sha,name
print(json.dumps({'expected_sha256':expected,'baseline':BASE,'patch_applied':NAMES},indent=2))
