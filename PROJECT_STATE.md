# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-02T11:43:21+08:00
Metadata Backfilled At: 2026-09-02T11:45:00+08:00
Metadata Provenance: reconstructed_from_git
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Pending
  GitHub Actor: ff6962757
-->

> Status: Living Project Checkpoint（持续更新的项目断点）
>
> Verified At: 2026-09-02T11:44:00+08:00
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

Post-Gate 第一批 vertical slices 已经落地：

1. **#101 / PR #102 — Permanent Human Route runtime boundary ✅**
   - Local Map loading / success / failure / retry；
   - focus / reduced-motion；
   - 不再由 `render_site_semantic.py` 通过脆弱字符串 patch 注入；
   - Human map-center label 不再泄漏 raw `system / concept / artifact / agent`。

2. **#103 / PR #104 — Task-oriented Search v0.1 ✅**
   - 99 个当前 Human Resources 的 deterministic search index；
   - name / stable ID / summary / Human type / alias 简单透明匹配；
   - query 进入 `?q=`，支持刷新 / Back / Forward；
   - 无 embedding、LLM ranking、隐藏推荐。

3. **#105 / PR #106 — First dedicated Compare UI ✅**
   - `automated_build_deployment` 下 Forgejo Actions vs GitHub Actions；
   - 真实 dedicated Compare page；
   - 保留 false / not recorded 边界；
   - `alternative_to` 不升级为 `compatible_with`；
   - 无 winner / score / recommendation；
   - 修复 automated review 发现的 Compare → Home 相对路径问题。

当前最新 Browser baseline：**30 / 30 Chromium tests PASS**；Human Route build 仍保持 99 Resource Pages / 131 Objects / 170 Graph edges / 0 reference issues，并额外生成 99-record Search index 与 1 个 dedicated Compare view。

## 5. Resume Here

Search 和第一个 Compare 已经证明 permanent Human Route 可以承载真实产品能力。现在不应立刻继续横向堆更多产品功能。

下一条主线优先收敛第二批 renderer architecture debt（渲染器架构债务）：

```text
1. #16 — Second permanent Human Route boundary slice
        ↓
2. Move Page Shell / semantic breadcrumb / shared Human labels
   away from transitional semantic adapter where practical
        ↓
3. Preserve Search / Compare / Resource Page / Browser regressions
        ↓
4. Re-evaluate next product slice
   broader task-oriented entry points OR Compare generalization OR Evidence presentation
```

### 第二小步的停止条件

> 进一步缩窄 `render_site_semantic.py` 作为 Legacy/v0 compatibility adapter 的职责，把已经稳定、与 Legacy/v0 兼容无关的共享 Human Route 页面职责迁入长期模块；但不重写整站、不改变 Knowledge Model、不引入前端框架。

新 Agent 收到“继续”时，应先检查 #16 的最新 child Issue / PR，然后从这个第二 permanent-boundary slice 继续。

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
- First dedicated Compare UI slice。

## 8. Cross-cutting / delegated work

Lifecycle / provenance historical backfill 已由 #89–#93 单独跟踪，并已交由其他 Agent 执行；当前 Reference Implementation 主线不要重复抢占这项工作。

Agent Continuity 的 fresh-session / different-agent takeover validation 由 #86 跟踪，是 P1 cross-cutting validation，不阻塞当前产品主线。

F4 Validator / Curation / Evidence / Query correctness 继续并行。

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
- #89–#93 — delegated lifecycle/provenance backfill；
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
→ PROJECT_STATE.md Resume Here
→ human-route-renderer-boundary-v0.1.zh-CN.md
→ human_route_runtime.py
→ render_site_semantic.py
→ Search / Compare modules
→ related Browser E2E
```

理解知识模型：
`03_Evolution/03_Change/knowledge-representation-model-decision-v0.1.zh-CN.md` + current Schema / semantic engine。

理解协作：
`CONTRIBUTING.md` + Collaboration Task System + Agent Continuity Profile。

## 12. Staleness check

这个文件是最后一次经过核验的项目快照，不是自动实时数据库。

新 Agent 在依赖 `Resume Here` 前必须检查：

1. `Verified At` 之后 main 是否有改变 Phase / 主线的提交；
2. #16 或其最新 child PR / Issue 是否已完成或改变方向；
3. 如果状态已经变化，先更新本文件，再继续。

不要让旧 `foundation-first-phase-v0.1.zh-CN.md` 的历史“NOW”状态覆盖本文件和更新的 Reference Implementation Phase Plan。
