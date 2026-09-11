#!/usr/bin/env python3
"""One-shot #287 maintenance. No main writes, force pushes, or benchmark runs.
prepare: preserve the frozen inventory under an archive tag; prepare historical PR30.
cleanup: only retire frozen, independently reviewed branches with fresh SHA guards.
The final PR30 merge is deliberately left to the ordinary PR merge API.
"""
import base64
import datetime
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile

REPO = 'InteropAtlas/InteropAtlas'
MAIN = '6972f84fec4d4f0813ba98079f030d8a3b35649b'
NAMING = 'feat/adaptive-naming-skill-v0.1'
NAMING_HEAD = '10125cb04dcbe4270230f3ba7db45f039c7a7330'
HELPER = 'maintenance/287-branch-pr-audit-20260911'
TAG = 'archive/maintenance-287-2026-09-11'
SOURCE_ARTIFACT = 10269776373
SOURCE_DIGEST = '31c2adb6783d9a4d7fa0192f1c9464460680d7099af3dad0181ae3e1e8e7b59e'
PR30_OLD = '72d7996be45494ad8f4bbf97249486e432149712'
PR30_BRANCH = 'task-23-non-normative-fit-test-batch-1'
OUT = Path('maintenance-output')
OUT.mkdir(exist_ok=True)
assert os.environ['GITHUB_REPOSITORY'] == REPO
assert os.environ['GITHUB_REF'] == 'refs/heads/' + HELPER
API = 'https://api.github.com/repos/' + REPO
TOKEN = os.environ['GH_TOKEN']

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def enc(s):
    return urllib.parse.quote(s, safe='')

def api(path, method='GET', body=None, allow_error=False):
    assert path == '' or path.startswith('/')
    req = urllib.request.Request(API + path, method=method,
        data=json.dumps(body, ensure_ascii=False).encode() if body is not None else None,
        headers={'Authorization': 'Bearer ' + TOKEN, 'Accept': 'application/vnd.github+json',
                 'Content-Type': 'application/json', 'X-GitHub-Api-Version': '2022-11-28',
                 'User-Agent': 'InteropAtlas-maintenance-287'})
    try:
        with urllib.request.urlopen(req, timeout=90) as response:
            raw = response.read()
            return json.loads(raw) if raw else {'http_status': response.status}
    except urllib.error.HTTPError as error:
        detail = {'http_error': error.code, 'path': path, 'body': error.read().decode()}
        if allow_error:
            return detail
        raise RuntimeError(json.dumps(detail)) from error

def collection(path):
    result = []
    for page in range(1, 101):
        items = api(path + ('&' if '?' in path else '?') + 'per_page=100&page=' + str(page))
        assert isinstance(items, list)
        result.extend(items)
        if not items:
            return result
    raise RuntimeError('Pagination exceeded bounded limit')

def git(*args, check=True):
    p = subprocess.run(['git', *args], text=True, capture_output=True)
    if check and p.returncode:
        raise RuntimeError(p.stderr)
    return p.stdout if check else p

def ancestor(a, b):
    return git('merge-base', '--is-ancestor', a, b, check=False).returncode == 0

def text(ref, path):
    return git('show', ref + ':' + path)

def write_json(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def comment(body):
    return api('/issues/287/comments', 'POST', {'body': body})

def source():
    archive = subprocess.check_output(['gh', 'api', 'repos/' + REPO + '/actions/artifacts/' + str(SOURCE_ARTIFACT) + '/zip'])
    assert hashlib.sha256(archive).hexdigest() == SOURCE_DIGEST
    with zipfile.ZipFile(io.BytesIO(archive)) as z:
        raw = z.read('inventory.json')
        Path('audit-input.bundle').write_bytes(z.read('repository.bundle'))
    git('bundle', 'unbundle', 'audit-input.bundle')
    d = json.loads(raw)
    assert d['main'] == MAIN and len(d['pulls']) == 88
    rows = [r for r in d['analysis'] if r['branch'] != HELPER]
    assert len(rows) == 105 and len({r['branch'] for r in rows}) == 105
    assert sum(bool(r['prs']) and any(p['merged_at'] for p in r['prs']) for r in rows) == 77
    return d, rows, raw

def proofs(rows):
    verified = []
    for row in rows:
        for p in row['prs']:
            if not p['merged_at']:
                continue
            h, m = row['head'], p['merge_commit_sha']
            assert h == p['terminal_pr_commit'] and p['post_pr_commits'] == 0
            assert ancestor(m, MAIN)
            parent = git('rev-parse', m + '^1').strip()
            actual = git('merge-tree', '--write-tree', parent, h).strip()
            expected = git('rev-parse', m + '^{tree}').strip()
            assert actual == expected
            verified.append({'branch': row['branch'], 'head': h, 'pr': p['number'],
                'merge_commit': m, 'merge_parent': parent, 'head_equals_pr_terminal': True,
                'post_merge_commits': 0, 'merge_in_main': True, 'expected_tree': expected,
                'reconstructed_tree': actual, 'tree_equivalent': True})
    assert len(verified) == 77
    return verified

def decisions(rows):
    result = []
    for r in rows:
        b = r['branch']
        if b == 'main':
            decision, why = '保留', '默认主线'
        elif b == NAMING:
            decision, why = '保留', '#416 Draft; Skill 0.4.0 / v84; generation remains paused; live-fit gate not satisfied'
        elif b == PR30_BRANCH:
            decision, why = '历史研究整理后合并', '#30 Batch1 missing from main but cited by Batch2; preserve original text with temporal disclaimer; no current model promotion'
        elif r['prs'] and any(p['merged_at'] for p in r['prs']):
            decision, why = '可直接删除', 'merged PR terminal=head; zero later commits; exact reconstructed merge-tree equivalence and merge reachable from main'
        elif b == 'docs/p1-closeout-state-sync':
            assert r['head'] == 'b0b529b2faf0855ade960c81b325cbf825742383' and ancestor(r['head'], MAIN)
            decision, why = '可直接删除', 'head is merged PR123 commit already reachable from main'
        elif b == 'docs/knowledge-workspace-principles-v0.1':
            assert r['head'] == 'a027ef4d0a38cef9c468135be3e840f9d4fa4b41'
            decision, why = '归档后删除', 'v0.1 principles superseded by PR123/current v1.0; retain 158-commit original stream, not merge transient status files'
        elif any(p['number'] in (20,26,108) for p in r['prs']):
            decision, why = '已被替代，归档后删除', {20:'current AGENTS/PROJECT_STATE/collaboration replace old roadmap; retain old proposal',26:'current provisional v0.3 supersedes v0.2; no stable/governance approval',108:'merged PR109 implements accepted shell boundary differently; preserve unique alternative implementation/tests'}[r['prs'][0]['number']]
        elif not r['prs'] and (b.startswith('tmp/') or b.startswith('tmp-rdap-')):
            decision, why = '归档后删除', 'reviewed stopped domain/benchmark experiment; retain all intermediate scripts/corpora/plans; zero net diff is not no history; do not execute'
        else:
            raise RuntimeError('Unreviewed branch: ' + b)
        result.append({'branch': b, 'head': r['head'], 'prs': [p['number'] for p in r['prs']],
            'decision': decision, 'reason': why, 'changed_from_merge_base': r['changed_from_merge_base'],
            'intermediate_changed_paths': sorted(set(git('log','--format=','--name-only',r['merge_base']+'..'+r['head']).split()))})
    assert sum(r['decision'] == '归档后删除' for r in result) == 21
    return result

def archive_commit(tag, files, parents, message):
    old = api('/git/ref/tags/' + enc(tag), allow_error=True)
    assert old.get('http_error') == 404, 'Archive tag already exists; never overwrite'
    entries = []
    for name, data in files.items():
        blob = api('/git/blobs', 'POST', {'content': base64.b64encode(data).decode(), 'encoding': 'base64'})
        entries.append({'path': name, 'mode':'100644', 'type':'blob', 'sha':blob['sha']})
    tree = api('/git/trees', 'POST', {'tree': entries})['sha']
    unique = list(dict.fromkeys(parents))
    chain = None
    for start in range(0, len(unique), 16):
        ps = ([chain] if chain else []) + unique[start:start+16]
        chain = api('/git/commits','POST',{'message': message + '\n\nArchival reachability only, NOT a content merge or acceptance into main. Never merge this retention chain into main.', 'tree':tree, 'parents':ps})['sha']
    created = api('/git/refs','POST',{'ref':'refs/tags/'+tag,'sha':chain})
    assert created['object']['sha'] == chain
    assert api('/git/ref/tags/' + enc(tag))['object']['sha'] == chain
    git('fetch','origin','refs/tags/'+tag)
    assert all(ancestor(p, chain) for p in unique)
    return chain

def prepare(d, rows, raw):
    assert api('/branches/main')['commit']['sha'] == MAIN
    assert api('/branches/' + enc(NAMING))['commit']['sha'] == NAMING_HEAD
    verification = proofs(rows)
    plan = decisions(rows)
    manifest = {'task':287,'created_at':now(),'repository':REPO,'main_before':MAIN,
        'original_branch_count':105,'original_pr_count':88,'source_run':d['run_id'],
        'source_artifact':SOURCE_ARTIFACT,'source_zip_sha256':SOURCE_DIGEST,
        'pagination':d['pages'],'decisions':plan,'merged_branch_content_proofs':verification,
        'authority':'Owner explicitly authorized bounded cleanup; not stable promotion',
        'archive_semantics':'Retention graph only; tree is evidence not a repository distribution; never merge archive into main',
        'naming':'keep original branch/head; Skill0.4.0/v84 paused'}
    readme = '''# #287 分支与 PR 整理归档\n\n此 tag 是历史保留引用，不是发行版、当前规则或工作分支。**不要把此归档提交链合入 main。**\n\nmanifest.json 为逐分支决定和完整 SHA、77 项实际 tree 等效证据；source-inventory.json.gz 为完整原始分页审计快照。归档提交的父提交链只用于保证所有原分支及 PR 提交可达，不表示接受其代码、规范、方法或实验。\n\n恢复：`git fetch origin refs/tags/archive/maintenance-287-2026-09-11:refs/tags/archive/maintenance-287-2026-09-11`，从 manifest 查原 SHA，使用 `git switch -c recover/<name> <original_sha>`。浏览中间脚本用 `git log <sha>` / `git show <sha>:<path>`。恢复分支或运行旧脚本需新的工作授权；本次不恢复命名 benchmark。\n\n实时执行结果及后续 head 漂移见 Issue #287；此处记录冻结基线，不冒称所有计划均已执行。\n'''
    heads = [r['head'] for r in rows] + [p['head']['sha'] for p in d['pulls']] + [os.environ['GITHUB_SHA']]
    saved = archive_commit(TAG, {'README.md':readme.encode(),'manifest.json':json.dumps(manifest,ensure_ascii=False,indent=2).encode(),'source-inventory.json.gz':gzip.compress(raw,mtime=0)}, heads, 'archive(#287): retain all original branch and PR histories before cleanup')
    write_json('manifest.json',manifest)
    comment('## 归档已建立（尚未批量删除）\n\nTag: `'+TAG+'`\n\nArchive commit: `'+saved+'`\n\n已验证所有原有分支 head、全部 88 个 PR head 以及本轮维护程序提交均可由该 tag 到达。归档仅保留历史，不合入 main、不执行实验。逐项清单与实际 tree 证明见 tag 中 `manifest.json`；原始分页数据见 `source-inventory.json.gz`。\n\n恢复：`git fetch origin refs/tags/'+TAG+':refs/tags/'+TAG+'` 后，按 manifest 的原 SHA 创建恢复分支。')
    current = api('/pulls/30')
    assert current['state']=='open' and current['head']['sha']==PR30_OLD
    assert api('/branches/main')['commit']['sha']==MAIN
    source_path='03_Evolution/01_Research/non-normative-object-fit-test-batch-1.zh-CN.md'
    target='03_Evolution/01_Research/03_Tests/non-normative-object-fit-test-batch-1.zh-CN.md'
    second='03_Evolution/01_Research/03_Tests/non-normative-object-fit-test-batch-2.zh-CN.md'
    original=text(PR30_OLD,source_path)
    assert git('rev-parse',PR30_OLD+':'+source_path).strip()=='22df4f3869067c59fc86fd939bbcd7622a993325'
    prefix='''<!-- InteropAtlas Document Metadata v0
Document Status: Historical Research / Archived Model Input（历史研究，非当前规范）
Document Imported At: 2026-09-11
Metadata Provenance: direct_record
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-6 Astra Pro（历史收录，不冒充原研究作者）
  Reviewer: archival integrity self-check only; original research not independently revalidated
  GitHub Actor: github-actions[bot]
-->

> **历史收录说明（#287，2026-09-11）**：本文件保存 #23 / PR #30 的 Batch 1 原始研究，补齐已在主线的 Batch 2 所引用的上游材料。
> 原提交：`72d7996be45494ad8f4bbf97249486e432149712`；原路径：`03_Evolution/01_Research/non-normative-object-fit-test-batch-1.zh-CN.md`；原 blob：`22df4f3869067c59fc86fd939bbcd7622a993325`。
> 下方原文未改写。其中“当前”、Schema 缺口、物理路径、下一批计划及来源时效，均指原研究时期，**不构成今天的规范、任务状态或已验证结论**。本次只验证来源完整性与文件/链接迁移，不重新验证原研究的现实事实，不晋升模型、治理或命名方法。
> 后续研究见 [Batch 2](non-normative-object-fit-test-batch-2.zh-CN.md)；当前模型以主线 `docs/02_System/01_Knowledge/`、Canonical 与 Runtime 合同为准。

---

<!-- BEGIN ORIGINAL RESEARCH (unaltered) -->
'''
    imported=prefix+original
    batch2=text(MAIN,second)
    needle='Batch 1 PR #30'
    assert batch2.count(needle)==1
    linked=batch2.replace(needle,'[Batch 1 历史研究](non-normative-object-fit-test-batch-1.zh-CN.md)（原 PR #30；原文为当时研究，非当前规范）')
    tree=api('/git/trees','POST',{'base_tree':git('rev-parse',MAIN+'^{tree}').strip(),'tree':[{'path':target,'mode':'100644','type':'blob','content':imported},{'path':second,'mode':'100644','type':'blob','content':linked}]})['sha']
    commit=api('/git/commits','POST',{'message':'docs(#30,#287): preserve Batch 1 as historical research without model promotion','tree':tree,'parents':[PR30_OLD,MAIN]})['sha']
    assert api('/pulls/30')['head']['sha']==PR30_OLD
    assert api('/branches/main')['commit']['sha']==MAIN
    api('/git/refs/heads/'+enc(PR30_BRANCH),'PATCH',{'sha':commit,'force':False})
    git('fetch','origin',commit)
    assert sorted(git('diff','--name-only',MAIN,commit).splitlines())==sorted([target,second])
    assert text(commit,target).split('<!-- BEGIN ORIGINAL RESEARCH (unaltered) -->\n',1)[1]==original
    git('diff','--check',MAIN,commit)
    result={'archive_tag':TAG,'archive_commit':saved,'prepared_pr30_head':commit,'main_unchanged':api('/branches/main')['commit']['sha']==MAIN,'changed_files':[target,second],'original_body_sha256':hashlib.sha256(original.encode()).hexdigest(),'checks':{'original_body_byte_equal':True,'only_two_historical_documents_changed':True,'diff_check':True},'merge_performed':False}
    write_json('prepare-result.json',result)
    (OUT/'batch1-imported.md').write_text(imported)
    comment('## #30 历史研究整理完成，等待本轮最终合并审查\n\nPrepared head: `'+commit+'`。main 未变化。PR 差异仅两个研究文档：Batch1 在现有 Tests 主目录归档收录（原文逐字节相同，加历史/非规范说明）；Batch2 补本地上游链接。`git diff --check`、原文完整性和两文件边界均通过。尚未执行 merge。#416 未修改。')
    print(json.dumps(result,ensure_ascii=False,indent=2))

def cleanup(d, rows, raw):
    expected_main=os.environ['EXPECTED_MAIN']
    expected_pr30=os.environ['EXPECTED_PR30_HEAD']
    expected_archive=os.environ['EXPECTED_ARCHIVE_COMMIT']
    assert api('/git/ref/tags/'+enc(TAG))['object']['sha']==expected_archive
    assert api('/branches/main')['commit']['sha']==expected_main
    assert api('/branches/'+enc(NAMING))['commit']['sha']==NAMING_HEAD
    git('fetch','origin',expected_main,'refs/tags/'+TAG)
    assert ancestor(MAIN,expected_main) and ancestor(expected_pr30,expected_main)
    pr30=api('/pulls/30')
    assert pr30['merged'] and pr30['head']['sha']==expected_pr30 and pr30['merge_commit_sha']==expected_main
    for n in (20,26,108):
        p=api('/pulls/'+str(n))
        assert p['state']=='closed' and not p['merged']
        assert p['head']['sha']==d['open_pull_details'][str(n)]['pr']['head']['sha']
    proofs(rows)
    plan=decisions(rows)
    before=collection('/branches')
    outcomes=[]
    comment('## 批量清理开始（归档已验证，PR 处置已核实）\n\nmain: `'+expected_main+'`；#30 已按历史研究范围合并；#20/#26/#108 已关闭而未合并；#416 保持 Draft。删除仅限原清单中除 main / 命名分支外的 103 个分支，加本轮唯一临时维护分支。每项执行前复查 exact head、保护、PR 状态及开放 PR 头/基分支引用；有并发变化或权限拒绝则跳过并记录。归档 tag `'+TAG+'` 已验证，不依赖 Actions artifact 的过期时间。')
    for row in plan:
        b=row['branch']
        if b in ('main',NAMING):
            continue
        expected=expected_pr30 if b==PR30_BRANCH else row['head']
        item={'branch':b,'original_head':row['head'],'expected_deletion_head':expected,'decision':row['decision'],'checked_at':now()}
        try:
            if api('/branches/main')['commit']['sha']!=expected_main:
                item['result']='skipped_main_changed'
            else:
                branch=api('/branches/'+enc(b),allow_error=True)
                if branch.get('http_error')==404:
                    item['result']='already_absent'
                elif branch.get('http_error'):
                    item['result']='skipped_read_error'; item['detail']=branch
                elif branch['commit']['sha']!=expected:
                    item['result']='skipped_head_changed'; item['actual_head']=branch['commit']['sha']
                elif branch['protected']:
                    item['result']='skipped_protected'
                else:
                    assert ancestor(expected,expected_archive) or ancestor(expected,expected_main)
                    for n in row['prs']:
                        p=api('/pulls/'+str(n))
                        assert p['state']=='closed' and p['head']['sha']==expected
                    head_open=collection('/pulls?state=open&head='+enc('InteropAtlas:'+b))
                    base_open=collection('/pulls?state=open&base='+enc(b))
                    if head_open or base_open:
                        item['result']='skipped_open_pr_reference'
                    else:
                        # Re-read immediately before the DELETE; no force or protection override.
                        fresh=api('/git/ref/heads/'+enc(b))
                        if fresh['object']['sha']!=expected:
                            item['result']='skipped_final_head_changed'
                        else:
                            deletion=api('/git/refs/heads/'+enc(b),'DELETE',allow_error=True)
                            item['delete_response']=deletion
                            absent=api('/git/ref/heads/'+enc(b),allow_error=True)
                            item['result']='deleted' if deletion.get('http_status')==204 and absent.get('http_error')==404 else 'not_confirmed'
        except Exception as error:
            item['result']='skipped_error'; item['error']=str(error)
        outcomes.append(item)
        print(json.dumps(item,ensure_ascii=False),flush=True)
        write_json('deletion-results.json',outcomes)
        time.sleep(1.2)
    # The normal token may lack administration permission. Do not elevate or change protection.
    settings=api('', 'PATCH', {'delete_branch_on_merge':True}, allow_error=True)
    settings_result={k:settings.get(k) for k in ('http_error','path','body','delete_branch_on_merge') if k in settings}
    write_json('settings-result.json',settings_result)
    helper_head=api('/branches/'+enc(HELPER))['commit']['sha']
    helper_outcome={'branch':HELPER,'expected_head':os.environ['GITHUB_SHA'],'actual_head':helper_head,'result':'pending_final_archive_guard'}
    summary={'task':287,'finished_at':now(),'original_branches':105,'pre_cleanup_branches':len(before),'main_after_pr30':expected_main,'pr30_head':expected_pr30,'archive_before':{'tag':TAG,'sha':expected_archive},'deleted_original':sum(r['result']=='deleted' for r in outcomes),'results':outcomes,'auto_delete_setting_attempt':settings_result,'helper':helper_outcome,'note':'helper outcome and final ref census are completed in Issue #287 after this frozen archive'}
    final_tag=TAG+'-result'
    final_archive=archive_commit(final_tag,{'README.md':b'# Maintenance #287 execution evidence\n\nNot a release. Do not merge this retention commit into main. Original full inventory is in the preceding archive tag. Final helper deletion and ref census are recorded in Issue #287.\n','execution-results.json':json.dumps(summary,ensure_ascii=False,indent=2).encode()},[expected_archive,os.environ['GITHUB_SHA'],expected_main,expected_pr30],'archive(#287): retain cleanup execution and maintenance source')
    if helper_head==os.environ['GITHUB_SHA']:
        fresh=api('/git/ref/heads/'+enc(HELPER))
        branch=api('/branches/'+enc(HELPER))
        open_heads=collection('/pulls?state=open&head='+enc('InteropAtlas:'+HELPER))
        open_bases=collection('/pulls?state=open&base='+enc(HELPER))
        if fresh['object']['sha']==helper_head and not branch['protected'] and not open_heads and not open_bases:
            assert ancestor(helper_head,final_archive)
            fresh=api('/git/ref/heads/'+enc(HELPER))
            if fresh['object']['sha']==helper_head:
                result=api('/git/refs/heads/'+enc(HELPER),'DELETE',allow_error=True)
                absent=api('/git/ref/heads/'+enc(HELPER),allow_error=True)
                helper_outcome['result']='deleted' if result.get('http_status')==204 and absent.get('http_error')==404 else 'not_confirmed'
                helper_outcome['response']=result
    else:
        helper_outcome['result']='skipped_head_changed'
    after=collection('/branches')
    open_prs=collection('/pulls?state=open')
    summary.update({'helper':helper_outcome,'archive_result':{'tag':final_tag,'sha':final_archive},'branches_after':after,'branch_count_after':len(after),'open_prs_after':[{'number':p['number'],'head':p['head']['sha'],'draft':p['draft']} for p in open_prs]})
    write_json('final-result.json',summary)
    table=['|分支|原 head / 删除前 head|结果|','|---|---|---|']
    for r in outcomes:
        hashes=r['original_head'] if r['original_head']==r['expected_deletion_head'] else r['original_head']+' → '+r['expected_deletion_head']
        table.append('|`'+r['branch']+'`|`'+hashes+'`|'+r['result']+'|')
    body='## 分支清理执行完成\n\n原有 105 分支；本轮实际删除原分支 **'+str(summary['deleted_original'])+'**；临时维护分支结果 `'+helper_outcome['result']+'`；最终分支 **'+str(len(after))+'**。\n\n合并：#30（只收录历史研究）；关闭未合并：#20/#26/#108；保留：#416 Draft、Skill 0.4.0、snapshot84、生成暂停。\n\n原始清单/完整历史：`'+TAG+'` @ `'+expected_archive+'`。执行结果/维护脚本：`'+final_tag+'` @ `'+final_archive+'`。后一个归档在删除维护分支前建立且验证可达；本评论补齐归档后的最终删除和完整分页核对。\n\n自动删除配置尝试：`'+json.dumps(settings_result,ensure_ascii=False)+'`。未使用额外权限，未修改保护。\n\n最终分支：'+', '.join('`'+b['name']+'` @ `'+b['commit']['sha']+'`' for b in after)+'。\n\n'+ '\n'.join(table)
    final_comment=comment(body)
    summary['final_issue_comment_id']=final_comment['id']
    write_json('final-result.json',summary)
    print(json.dumps({k:v for k,v in summary.items() if k not in ('results','branches_after')},ensure_ascii=False,indent=2))

if __name__=='__main__':
    mode=sys.argv[1]
    data, original_rows, raw_data=source()
    if mode=='prepare':
        prepare(data,original_rows,raw_data)
    elif mode=='cleanup':
        cleanup(data,original_rows,raw_data)
    else:
        raise RuntimeError('Unsupported mode')
