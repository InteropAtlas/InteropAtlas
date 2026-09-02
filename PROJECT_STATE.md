# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-02T13:00:00+08:00
Metadata Backfilled At: 2026-09-02T11:45:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Not independently reviewed — checkpoint sync only
  GitHub Actor: ff6962757
-->

> Status: Living Project Checkpoint（持续更新的项目断点）
>
> Verified At: 2026-09-02T13:00:00+08:00
>
> Purpose: 给新的 Human / Agent 一个短小的“现在在哪、为什么、从哪里继续”入口。它不替代 Issue、PR、Git history 或完整 Phase Plan。

## 1. Project in one sentence

InteropAtlas 是一个开放、机器可读、可持续分析的 **Interoperability Solution Space（互操作方案空间）** 知识地图，用来连接标准、成熟先例、方法、实现、组织、能力、场景、关系、证据与开放缺口，并服务 Human（人类）与 Agent（智能体）的发现、比较、组合、验证和改进。

完整定义：`docs/interopatlas-definition-and-scope-v0.2.zh-CN.md`。

## 2. Core invariants（核心不变量）

任何方向判断先保护这些原则：

- `Adopt → Profile → Extend → Invent（采用 → 定制 → 扩展 → 最后才自行发明）`；
- `Evidence Before Assertion（先证据，后断言）`；
- `Fact ≠ Assessment（事实 ≠ 评估）`；
- `Physical Storage ≠ Semantic Classification ≠ Index / View（物理存储 ≠ 语义分类 ≠ 索引 / 视图）`；
- Stable Identity（稳定身份）不能依赖文件路径或显示名称；
- Canonical State（规范状态）与 Generated View（生成视图）分离；
- Search / Compare / Map 是 View / Projection（视图 / 投影），不是新的 Canonical Fact 来源；
- Private Chat（私人聊天）不是项目状态；
- Human / Agent 协作使用公开、可恢复的 GitHub / Repository Artifact；
- 高影响治理、破坏性迁移和仓库规则变更需要明确 Human Maintainer 授权。

## 3. Foundation status

```text
Gate A — Repository Structure
✅ PASS

Gate B — Human Interface
✅ PASS

Gate C — Open Collaboration
✅ PASS at v0.1 Pilot

Knowledge Model / Machine Contract
✅ representative foundation complete

F4 — Curation / Evidence / Machine Correctness
🟡 parallel quality line
```

Gate B Final Conformance Audit：
`03_Evolution/01_Research/gate-b-final-conformance-audit-2026-09-02.zh-CN.md`。

Foundation 的三项主要 Gate 已经达到最小可依赖状态。项目当前处于真实 Reference Implementation（参考实现）演进，而不是继续无限补 Foundation。

## 4. Current phase

**Reference Implementation Evolution（参考实现演进）**

当前 Phase Plan：
`03_Evolution/03_Change/reference-implementation-phase-v0.1.zh-CN.md`。

当前主 umbrella：**#16 — 按 Human Interface Specification / Profiles 审计并重构当前网站**。

Post-Gate 已落地的主线 slices：

1. **#101 / PR #102 — Permanent Human Route runtime boundary ✅**
   - Local Map loading / success / failure / retry；
   - focus / reduced-motion；
   - Human map-center label 不再泄漏 raw core type。

2. **#103 / PR #104 — Task-oriented Search v0.1 ✅**
   - 99 个 Human Resources 的 deterministic search index；
   - stable ID / name / summary / Human type / alias 透明匹配；
   - query URL / Back / Forward；无隐藏 ranking。

3. **#105 / PR #106 — First dedicated Compare UI ✅**
   - Forgejo Actions vs GitHub Actions；
   - false / not-recorded 边界；
   - 无 winner / score / recommendation。

4. **#107 / PR #109 — Second permanent Human Route shell boundary ✅**
   - `human_route_shell.py`；
   - semantic Breadcrumb / Human route-link helper / shared Human view labels 迁入 permanent Human Route；
   - Resource / Search / Compare 共用 permanent Page Shell entry point。

5. **#110 / PR #111 — First Evidence / Assessment Human View ✅**
   - Canonical `sources` 与 IA `notes_zh` 在 Human View 中明确分工；
   - missing source 表达为 not recorded，而不是 false / none；
   - Forgejo Actions + YAML 1.2.2 representative slice；
   - Browser E2E **32 / 32 PASS**；
   - 99 Resource Pages / 131 Objects / 170 Graph edges / 0 reference issues。

## 5. Resume Here

Search、Compare、Evidence presentation 和两批 permanent renderer boundary 已经形成可依赖的小闭环。当前最明显的产品缺口不是再发明一个新引擎，而是：这些能力分别存在，但 Homepage 仍主要要求用户从 Capability 分类理解 Atlas。

当前 Work Item：**#112 — Task-oriented Homepage Entry v0.1**。

```text
#16 Reference Implementation umbrella
        ↓
#112 Task-oriented Homepage Entry
        ↓
1. Expose existing Human Route abilities as user tasks
   Find / Understand / Compare / Verify / Relate-Explore
        ↓
2. Keep Capability-first browse as one valid entry, not the only entry
        ↓
3. Do not advertise unimplemented general Compare / large Graph Explorer
        ↓
4. Preserve stable routes / JS-disabled reading / Browser regressions
```

### #112 当前停止条件

> Homepage 至少形成 4 个真实可用、任务导向的入口，并只连接已经存在且有验证证据的 Human Route 能力；不创建新的 Canonical taxonomy，不扩张成全站产品重写。

#112 当前为 Ready。新的执行者应先 Claim / 更新 Lease，再开始实现。

## 6. Gate B final result

全部冻结的 Gate B Stop Conditions 已满足：

- [x] 五个 Profile 可独立审计；
- [x] 关键要求有 upstream basis；
- [x] Adopt / Profile / Extend / Invent 边界已记录；
- [x] 四类 representative Resource Page 已浏览器验证；
- [x] Browser E2E baseline 可重复；
- [x] keyboard / focus / reflow / semantic evidence；
- [x] Local Map success / loading / failure feedback；
- [x] Minimal Compare contract；
- [x] representative Human Task Walkthrough；
- [x] Final Conformance Audit 无 unresolved P0 structural non-conformance；
- [x] 剩余 Human Interface gaps 已分类为 P1 / Later / accepted boundary。

Gate B PASS **不等于完整网站、完整 WCAG certification、完整 Search / Compare / Graph 产品已经完成**。

## 7. Recent stable milestones

近期稳定落地：

- Repository Structure 三大区：`01_State / 02_Runtime / 03_Evolution`；
- Knowledge Representation Contract v0.1；
- Semantic Normalization / Kind Registry / v0 Schemas / Relation compatibility；
- Machine Review；
- Representative Migration Pilot；
- Human Interface five-profile consolidation；
- Gate B Browser E2E / accessibility foundation；
- Four-family representative Resource Page contract；
- Minimal Compare Contract；
- Minimal Human Task Walkthrough；
- Gate B Final Conformance Audit；
- Agent Onboarding / Context Continuity layer；
- Contribution Identity + Provenance / Traceability baseline；
- Permanent Human Route runtime boundary；
- Task-oriented Search v0.1；
- First dedicated Compare UI slice；
- Second permanent Human Route shell boundary；
- First Evidence / Assessment Human View。

## 8. Cross-cutting / delegated work

Lifecycle / provenance historical backfill **#89–#93 已完成并关闭**。它留下的 never-verified / source-evidence gaps 是后续质量债，不代表 #89 未完成；当前 Reference Implementation 主线不要重复执行历史 backfill。

Agent Continuity 的 fresh-session / different-agent takeover validation 由 #86 跟踪，是 P1 cross-cutting validation，不阻塞当前产品主线。

F4 Validator / Curation / Evidence / Query correctness 继续并行；#110 只完成第一批 Human View presentation，不等价于全量 Evidence 模型建设。

## 9. Open decision gates — DO NOT auto-execute

以下事项仍需要单独 Human Maintainer 授权：

- Full Canonical Migration（全量规范数据迁移）；
- Repository-wide Schema Enforcement（全仓库 Schema 强制执行）；
- Ruleset / Branch Protection / Governance Automation；
- 大规模数据删除或破坏性 Schema 变更；
- stable Specification promotion（稳定规范升级）；
- License / Security policy 重大变化；
- 大型 frontend framework rewrite / infrastructure replacement。

Gate B PASS 和当前 Reference Implementation 进展不改变这些授权边界。

## 10. Known open / unrelated work

不要自动合并或吞并无关工作：

- PR #26 — Open Collaboration v0.2：高影响 Review Gate；
- PR #30 — Fit Test Batch 1：独立未合并工作；
- Issue #15 — 更广泛 Schema / Validator / migration debt；
- Issue #86 — Agent Continuity takeover validation；
- F4 Machine / Curation / Evidence tasks。

## 11. Where to read next

第一次理解项目：

```text
AGENTS.md
→ PROJECT_STATE.md
→ README.md
→ docs/interopatlas-definition-and-scope-v0.2.zh-CN.md
→ 03_Evolution/03_Change/reference-implementation-phase-v0.1.zh-CN.md
```

继续当前主线：

```text
Issue #16
→ Issue #112
→ render_site_semantic.py / build_homepage()
→ human_route_shell.py
→ Search / Compare / Evidence Human View contracts
→ related Browser E2E
```

理解 renderer architecture：
`03_Evolution/03_Change/human-route-renderer-boundary-v0.2.zh-CN.md` + `human_route_shell.py` + `human_route_runtime.py`。

理解 Evidence presentation：
`03_Evolution/03_Change/human-evidence-presentation-v0.1.zh-CN.md`。

理解知识模型：
`03_Evolution/03_Change/knowledge-representation-model-decision-v0.1.zh-CN.md` + current Schema / semantic engine。

理解协作：
`CONTRIBUTING.md` + Collaboration Task System + Agent Continuity Profile。

## 12. Staleness check

这个文件是最后一次经过核验的项目快照，不是自动实时数据库。

新 Agent 在依赖 `Resume Here` 前必须检查：

1. `Verified At` 之后 main 是否有改变 Phase / 主线的提交；
2. #16 / #112 或其最新 PR 是否已完成或改变方向；
3. 如果状态已经变化，先更新本文件，再继续。

不要让旧 `foundation-first-phase-v0.1.zh-CN.md` 的历史“NOW”状态覆盖本文件和更新的 Reference Implementation Phase Plan。
