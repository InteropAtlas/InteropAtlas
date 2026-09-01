# InteropAtlas 当前路线图

> 状态：Living Roadmap（持续更新路线图）
>
> 当前阶段：**Foundation First（基础先行）**
>
> 详细阶段定义：[`foundation-first-phase-v0.1.zh-CN.md`](foundation-first-phase-v0.1.zh-CN.md)

## 当前总体判断

仓库结构本身已经不再是当前主要阻塞项。

经过 Repository migration、docs / Evolution 分流以及 Collaboration Implementation Pilot，当前 Foundation 的真实状态是：

```text
F1 Repository Structure       已完成 Draft Profile + 物理迁移
F2 Human Interface            仍是主要 P0，尚未通过 Gate B
F3 Open Collaboration         已完成 Draft Profile + V0.1 Pilot
F4 Curation / Evidence /      仍需并行补齐
   Machine Correctness
```

因此当前不应该继续花主要精力调整根目录，也不应该恢复“先做网站、再反推规范”的路线。

当前最重要的是把 **知识模型 → Human Interface 规范 → 可验证实现** 这条链补完整。

继续遵守：

- Interoperability 是问题边界；
- Reuse Before Invent；
- Adopt → Profile → Extend → Invent；
- Evidence Before Assertion；
- Fact ≠ Assessment；
- Structured Source, Linked View；
- Flat Objects + Rich Relations + Dynamic Maps；
- Human ↔ Machine Co-development；
- Practice-driven Feedback；
- graph-native, database-agnostic；
- **Physical Storage ≠ Semantic Classification ≠ Index / View**。

## F1 — Repository Structure：完成

### 状态

**PASS — Draft Profile + physical implementation completed.**

当前核心结构已经实际落地：

```text
01_State/
├── 01_Objects/
└── 02_Relations/

02_Runtime/
├── 01_Engine/
├── 02_Tools/
└── 03_Outputs/

03_Evolution/
├── 01_Research/
├── 02_Experiments/
└── 03_Change/
```

外围继续保留 GitHub / 开源项目所需入口：

```text
.github/
docs/
LICENSES/
README.md
CONTRIBUTING.md
AGENTS.md
...
```

已经完成：

- Repository Structure Profile；
- storage path 与对象语义解耦；
- public route 与 physical source 解耦；
- Schema 与 State 共置；
- Canonical Objects / Relations 物理迁移；
- Runtime 物理迁移；
- Evolution 建立；
- Research / Experiments / Change 从 `docs/` 分流；
- Markdown 路径自动检查。

迁移基线保持：

```text
objects             112
relations           107
resolved edges      161
reference_issues      0
```

当前 Repository Structure 不再等待 #15 决定文件夹。#15 只决定知识语义模型。

当前结构规范见 [`../../docs/repository-structure-profile-v0.1.zh-CN.md`](../../docs/repository-structure-profile-v0.1.zh-CN.md)。

## F3 — Open Collaboration：V0.1 Pilot 已完成

### 状态

**PASS — Draft Profile + Collaboration Implementation Pilot completed.**

Work Package B #22 已实际完成：

- `CONTRIBUTING.md`；
- root `AGENTS.md`；
- Work Item Issue Form；
- PR Template；
- Lifecycle / Lease / Handoff / Review Class operational mapping；
- Ready Tasks #23 / #24 / #25；
- #24 的真实 Ready → Claim → Work → PR → Handoff → Review 试运行；
- Pilot friction / gap audit。

因此“实现 Collaboration Pilot”已经不是 Candidate Next Work Package。

### 当前仍开放但不阻塞主线

- PR #26：Open Collaboration v0.2 Draft，仍处于 high-impact Review Gate；
- #27：Human / Agent 共用 GitHub 账号导致身份折叠；
- Issue Fields / CODEOWNERS / Ruleset / automation：只有真实 friction 持续出现时再增强；
- 不自动开发 Lease Server / heartbeat。

这些是 F3 的后续演化，不应再次阻塞 F2 / F4。

## F2 — Human Interface Standards Package：当前主要 P0

### 状态

**NOT PASS.**

#14 已经完成了大量上游标准收集、Reference Map、综合 `IA-HI v0.1` 草案和第一轮审计，但 Gate B 要求的五个可独立审计 Profile 仍未形成完整 Draft coverage：

1. Information Architecture；
2. Information Presentation；
3. Interaction；
4. Visual Presentation；
5. Accessibility / Conformance。

每个模块至少需要：

- 用户任务 / Context of Use；
- 上游正式标准与 Mature Prior Art；
- Adopt / Profile / Extend / Invent 判断；
- BCP 14 Requirement IDs；
- 可验证的 conformance 方法；
- 与其他模块的依赖 / 冲突处理。

### 当前真正的前置瓶颈：#15 Knowledge Object Model

#14 已经明确暴露出：Method、Heuristic、Framework、Design System 等非规范性依据不能继续被随意塞入 `reference_project`。

因此当前第一优先级不是继续增加 Human Interface 文档数量，而是先推进 #15 的真实对象 Fit Test。

当前已有 Ready Task：#23 / PR #30。

推荐顺序：

```text
#23 Batch 1
4 个真实对象 Fit Test
    ↓
纠正 PR #30 中已被 #31 推翻的目录语义
    ↓
Batch 2
再补 4–8 个跨类别真实样本
    ↓
比较候选模型
    ↓
Model Decision / Rationale
    ↓
必要时再修改 Schema
    ↓
让 #14 的非规范性依据可以正确进入 Atlas
    ↓
完成五个 Human Interface Draft Profiles
```

重要：**#15 决定对象是什么，不决定对象住哪个语义文件夹。** Canonical Object 继续平级进入 `01_State/01_Objects/`。

## F4 — Curation / Evidence / Machine Correctness：并行基础线

### 状态

**NOT PASS / 持续推进。**

当前 Engine 已经具备确定性 Loader、Graph / Backlink Index、稳定 public route 和 `reference_issues = 0` 基线，因此早期 #1 / #8 中相当一部分基础能力已经落地。

真正剩余的 Machine / Trust 工作应重新聚焦在：

1. **Schema enforcement**
   - Schema 已归位，但尚未启用全量验证；
   - 需要把 JSON Schema correctness 接入 Validator / CI。
2. **Curation / Contribution** — #9
   - 最小收录条件；
   - Prior Art Check；
   - 去重、版本更新、Review。
3. **Evidence / Provenance / Trust** — #10
   - Fact / Claim → Evidence → Source；
   - retrieved_at / version / context；
   - Fact 与 Assessment 的不同证据要求。
4. **Query correctness** — #7
   - 修复 `alternative_to` 作用域；
   - 增加回归测试。
5. **Legacy Relation cleanup**
   - 历史 Relation 补 `type: relation`；
   - 与物理迁移保持分离。

F4 可以与 #15 / #14 并行，但不应该重新打开仓库目录设计。

## 当前执行顺序

现在的主路线收敛为：

```text
主线：
#15 / #23 Knowledge Object Fit Test
        ↓
Knowledge Object Model Decision
        ↓
#14 Human Interface 五个 Draft Profiles
        ↓
Gate B Audit
        ↓
恢复 Reference Implementation 为 P0

并行线：
#8 剩余 Validator / Schema correctness
#9 Curation
#10 Evidence / Provenance
#7 Query correctness
```

### 当前下一小步

**先处理 #23 / PR #30。**

原因：

- 已经有四个真实对象的研究成果；
- 只需先修正其中已经被 Repository Structure #31 推翻的目录结论，并把 Research artifact 放入正确的 Evolution 区域；
- 它直接为 #15 下一批 Fit Test 提供统一格式；
- #15 又直接支撑 #14。

PR #30 在完成这些纠正前不合并。

## Reference Implementation：继续保持 P1

以下工作继续保留，但不作为当前主 P0：

- #12 Capability-first Navigation；
- #13 Browser E2E / Accessibility；
- #16 Human Interface Conformance-driven refactor；
- #17 Object Page Shell 后续；
- Search / Global Explore / Visual Tokens / 大型 Graph UI。

已经完成且符合规范的实现不回滚。

当 Gate B 达到 Draft coverage 后，再从 Specification 推导 Reference Implementation，而不是反过来。

## Foundation Gate

### Gate A — Repository

**PASS + implemented.**

### Gate B — Human Interface

**NOT YET PASS.**

最低条件：

- [ ] Information Architecture Draft；
- [ ] Information Presentation Draft；
- [ ] Interaction Draft；
- [ ] Visual Presentation Draft；
- [ ] Accessibility / Conformance Draft；
- [ ] 关键 Requirement IDs + upstream basis；
- [ ] Non-normative HCI knowledge object model 可用。

### Gate C — Open Collaboration

**PASS + V0.1 Pilot completed.**

整个 Foundation Gate 当前仍因 Gate B 未通过而保持未完成状态。

## Prior Art 是持续前置流程

所有方向继续遵守：

> **Reuse Before Invent**
>
> **Adopt → Profile → Extend → Invent**

新的标准、规范、Schema、交互模式、Agent 机制或项目规则，都必须先确认现有方案空间，而不是因为“项目内部需要”就直接创造。
