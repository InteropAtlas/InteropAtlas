# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-02T10:43:23+08:00
Metadata Backfilled At: 2026-09-02T10:49:00+08:00
Metadata Provenance: reconstructed_from_git
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human — ff6962757
  GitHub Actor: ff6962757
-->

> Status: Living Project Checkpoint（持续更新的项目断点）
>
> Verified At: 2026-09-02T09:35:00+08:00
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
🟡 CLOSE / NOT YET PASS

Gate C — Open Collaboration
✅ PASS at v0.1 Pilot

F4 — Curation / Evidence / Machine Correctness
🟡 parallel foundation line
```

Knowledge Model v0、Machine Contract I1–I6、Representative Migration Pilot 已完成，不再阻塞 Human Interface 主线。

## 4. Current main line

**Current P0: Issue #14 — Human Interface / Gate B**

五个 Human Interface Draft Profiles 已经形成并完成第一轮整合审计：

1. Information Architecture；
2. Information Presentation；
3. Interaction；
4. Visual Presentation；
5. Accessibility / Conformance。

浏览器级基础也已经建立：

- Playwright Browser E2E；
- keyboard / focus / reflow / semantic baseline；
- Local Map Recenter loading / success / failure feedback；
- reduced-motion evidence；
- Legacy/v0 semantic renderer deployment alignment；
- 四个 Core Identity Family 的 representative Resource Page 浏览器验证。

这些结果说明 Gate B 已经接近终点，但**还没有通过最终 Gate B Conformance Audit**。

## 5. Resume Here

当前主线按以下顺序继续：

```text
1. Minimal Compare Contract
   最小 Compare（比较）任务 / 信息架构 / 比较维度合同
        ↓
2. Minimal Human Task Walkthrough
   从 Home / Capability / Implementation / Relation / Local Map / Source / Compare
   完成一条代表性 Human Task 路径
        ↓
3. Gate B Conformance Audit
   检查所有 P0 结构性要求是否有证据
        ↓
4. PASS
   或形成明确 blocker list（阻塞项清单）
```

如果新 Agent 收到用户只说“继续”，默认先验证这四步的真实 GitHub / main 状态，再从尚未完成的第一步继续。

## 6. Gate B stop condition

当前已满足：

- [x] 五个 Profile 可独立审计；
- [x] 关键要求有 upstream basis（上游依据）；
- [x] Adopt / Profile / Extend / Invent 边界已记录；
- [x] 四类 representative Resource Page 已浏览器验证；
- [x] Browser E2E baseline 可重复；
- [x] keyboard / focus / reflow / semantic evidence；
- [x] 当前 Local Map Recenter feedback；

仍需：

- [ ] Minimal Compare contract；
- [ ] representative Human Task Walkthrough；
- [ ] 最终 Gate B Conformance Audit 无 unresolved P0 structural non-conformance；
- [ ] 剩余 gap 明确降级为 P1 / Later 或 accepted risk。

## 7. Recent stable milestones

近期已经稳定落地：

- Repository Structure 三大区：`01_State / 02_Runtime / 03_Evolution`；
- Knowledge Representation Contract v0.1；
- Semantic Normalization / Kind Registry / v0 Schemas / Relation compatibility；
- Machine Review；
- Representative Migration Pilot；
- Human Interface five-profile consolidation；
- Gate B P0 gap priority audit；
- Browser E2E / accessibility foundation；
- Four-family representative Resource Page contract；
- Contribution Identity（三核心身份 + GitHub Actor 分离）；
- Record lifecycle / source / verification provenance 规则；
- W3C PROV / SPDX / DCMI / SLSA Provenance prior-art intake。

## 8. Current cross-cutting continuity work

本次分支正在补齐 **Agent Onboarding / Context Continuity（智能体入门 / 上下文连续性）**：

- `AGENTS.md` 作为 Agent Bootstrap Router；
- `PROJECT_STATE.md` 作为项目级断点；
- Issue / PR / Handoff 保持任务级状态；
- 重要 Decision Artifact 保存长期理由；
- 新会话 / 不同 Agent 将通过 takeover test（接管测试）验证。

完成后应回到 #14 Gate B 主线，不把 Context Continuity 演变成长期 P0 旁支。

## 9. Open decision gates — DO NOT auto-execute

以下事项需要单独 Human Maintainer 授权：

- Full Canonical Migration（全量规范数据迁移）；
- Repository-wide Schema Enforcement（全仓库 Schema 强制执行）；
- Ruleset / Branch Protection / Governance Automation；
- 大规模数据删除或破坏性 Schema 变更；
- stable Specification promotion（稳定规范升级）；
- License / Security policy 重大变化。

## 10. Known open / unrelated work

不要为了“顺手整理”自动合并或吞并无关工作：

- PR #26 — Open Collaboration v0.2：高影响 Review Gate，未授权自动合并；
- PR #30 — Fit Test Batch 1：仍是独立未合并工作；
- Issue #15 — 更广泛 Schema / Validator / migration debt；
- F4 Validator / Curation / Evidence / Query correctness 继续作为并行线。

## 11. Where to read next

第一次理解项目：

```text
AGENTS.md
→ PROJECT_STATE.md
→ README.md
→ docs/interopatlas-definition-and-scope-v0.2.zh-CN.md
→ 03_Evolution/03_Change/foundation-first-phase-v0.1.zh-CN.md
```

继续 #14：读取 Issue #14、五个 Human Interface Profiles、Gate B gap audit 和最近相关 PR / commits。

理解知识模型：读取 `03_Evolution/03_Change/knowledge-representation-model-decision-v0.1.zh-CN.md` 及当前 Schema / semantic engine。

理解协作：读取 `CONTRIBUTING.md`、`docs/collaboration-task-system-v0.1.zh-CN.md`、`docs/agent-attribution-contribution-identity-profile-v0.1.zh-CN.md`。

理解 Agent 连续性：读取 `docs/agent-onboarding-context-continuity-profile-v0.1.zh-CN.md`。

## 12. Staleness check

这个文件是“最后一次经过核验的项目快照”，不是自动实时数据库。

新 Agent 在依赖 `Resume Here` 前必须检查：

1. `Verified At` 之后 main 是否有明显改变阶段 / Gate / 主线的提交；
2. 当前主 Issue / PR 是否已关闭、合并或发生阻塞；
3. 如果状态已经变化，先更新本文件，再继续新的主线。

不要因为旧 Phase Plan 或旧 Issue comment 写着“下一步是 X”，就覆盖更新的 main / PR / Project State 证据。
