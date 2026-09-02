# InteropAtlas Project State

> Status: Living Project Checkpoint（持续更新的项目断点）
>
> Verified At: 2026-09-02T11:02:00+08:00
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

Foundation 的三项主要 Gate 已经达到最小可依赖状态。项目不再以“继续补基础规范”为唯一主 P0。

## 4. Current phase

**Reference Implementation Evolution（参考实现演进）**

当前 Phase Plan：
`03_Evolution/03_Change/reference-implementation-phase-v0.1.zh-CN.md`。

当前主 umbrella：**#16 — 按 Human Interface Specification / Profiles 审计并重构当前网站**。

Gate B 期间已经稳定形成：

- 五个 Human Interface Draft Profiles；
- Four-family representative Resource Page contract；
- real Chromium Browser E2E；
- keyboard / focus / reflow / semantic evidence；
- Local Map loading / success / failure / retry evidence；
- Minimal Compare semantic contract；
- representative Human Task Walkthrough；
- Final Gate B audit。

这些现在是后续网站建设的回归合同，而不是继续拖延产品实现的理由。

## 5. Resume Here

当前下一条主线：

```text
1. #16 — Audit current transitional Human Route architecture
        ↓
2. Define one small permanent-renderer migration slice
   把 Gate B compatibility hooks 从临时桥接结构推进到长期 Human Route 架构
        ↓
3. Preserve existing Browser / task / semantic regression evidence
        ↓
4. Choose first high-value product slice
   Task-oriented Search / entry OR dedicated Compare UI
```

### 第一小步的停止条件

> Human Route 从“Gate B 临时 compatibility adapter 能工作”推进到“长期实现结构可以继续承载产品能力”，但不重写整站、不改变 Knowledge Model。

新 Agent 收到“继续”时，应先验证 #16 当前状态和最近相关 PR，再从上述第一项尚未完成的工作继续。

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
- Gate B P0 gap priority audit；
- Browser E2E / accessibility foundation；
- Four-family representative Resource Page contract；
- Minimal Compare Contract；
- Minimal Human Task Walkthrough；
- Gate B Final Conformance Audit；
- Agent Onboarding / Context Continuity layer；
- Contribution Identity + Provenance / Traceability baseline。

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

Gate B PASS 不改变这些授权边界。

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
→ Gate B Final Audit
→ Human Interface Profiles
→ render_site_semantic.py / current Human Route architecture
→ related Browser E2E
```

理解知识模型：
`03_Evolution/03_Change/knowledge-representation-model-decision-v0.1.zh-CN.md` + current Schema / semantic engine。

理解协作：
`CONTRIBUTING.md` + Collaboration Task System + Agent Continuity Profile。

## 12. Staleness check

这个文件是最后一次经过核验的项目快照，不是自动实时数据库。

新 Agent 在依赖 `Resume Here` 前必须检查：

1. `Verified At` 之后 main 是否有改变 Phase / Gate / 主线的提交；
2. #16 或其最新 child PR / Issue 是否已完成或改变方向；
3. 如果状态已经变化，先更新本文件，再继续。

不要让旧 `foundation-first-phase-v0.1.zh-CN.md` 的历史“NOW”状态覆盖本文件和更新的 Reference Implementation Phase Plan。
