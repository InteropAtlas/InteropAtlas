# InteropAtlas 当前路线图

> 状态：Living Roadmap（持续更新路线图）
>
> 当前阶段：**Foundation First（基础先行）**
>
> 当前主任务：**#61 Schema / Compatibility Design for Knowledge Model v0**
>
> 详细阶段定义：[`foundation-first-phase-v0.1.zh-CN.md`](foundation-first-phase-v0.1.zh-CN.md)

## Owner View — 默认管理视图

如果只从项目负责人视角看，当前路线可以压缩为：

```text
1. 定义项目是什么
   ✅ 基本完成

2. 搭好仓库结构与协作方式
   ✅ 基本完成

3. 定义“知识应该怎样被表达”
   ✅ 语义模型 v0 已批准

4. 把知识规则变成机器可执行合同
   🟡 NOW — #61

5. 完成面向人的信息组织 / 呈现 / 交互规范
   ⬜ NEXT — #14 / Gate B

6. 按规范继续建设 Reference Implementation
   ⬜ LATER

7. 增加 Search / Compare / Maps / Pathfinder / Analysis
   ⬜ LATER

8. Federation / 多后端 / 更高级治理
   ⬜ FUTURE
```

当前负责人需要重点把控的是：

- 项目 Scope 与边界；
- 核心语义原则；
- 高影响模型 / 迁移决策；
- 当前阶段是否做最重要的事；
- Foundation Gate 是否达到可依赖状态。

具体 Schema 语法、Loader、CI、migration script 等属于 Implementation View，不要求负责人全部掌握。

---

# 当前总体判断

Repository Structure 和 Open Collaboration 已经不再是主阻塞。

2026-09-01，#58 / PR #60 已正式批准并合并 **InteropAtlas Minimum Knowledge Representation Contract v0.1**。

采用的 Core Identity Families：

```text
concept
artifact
system
agent
```

同时正式采用：

- Identity Target Rule；
- `type / kind / Strong Profile / roles / authority` 分层；
- Object Property ≠ Statement / Claim；
- Object Source ≠ Statement Evidence；
- Fact ≠ Assessment；
- known / unknown / explicit none / not recorded 分离；
- semantic model ≠ validation ≠ serialization ≠ query；
- graph-native, database-agnostic；
- **Physical Storage ≠ Semantic Classification ≠ Index / View**。

因此知识模型已经从“研究 / Model Decision”进入“机器合同 / 兼容设计”阶段。

当前 Foundation 状态：

```text
F1 Repository Structure       ✅ COMPLETE
F2 Knowledge + Human Interface 🟡 MAIN P0
F3 Open Collaboration         ✅ V0.1 PILOT COMPLETE
F4 Curation / Evidence /
   Machine Correctness        🟡 PARALLEL FOUNDATION LINE
```

---

# F1 — Repository Structure：完成

**PASS — Draft Profile + physical implementation completed.**

当前核心结构：

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

已经完成：

- Canonical State / Runtime / Evolution 边界；
- storage path 与对象语义解耦；
- public route 与 physical source 解耦；
- Schema 与 State 共置；
- Research / Experiments / Change 与 `docs/` 分流；
- Markdown path CI。

F1 不再因知识模型变化重新设计语义文件夹。

---

# F2 — Knowledge Representation + Human Interface：当前主 P0

## F2-A — Knowledge Representation

### 已完成

```text
Prior Art Check
✅

SQL / RDF / Wikibase / Property Graph 数据语言比较
✅

10 个跨类别真实对象 Fit Test
✅

Model Decision / Stress Test
✅

Minimum Knowledge Representation Contract v0.1
✅ APPROVED / ADOPTED — #58 / PR #60
```

### 当前阶段

**#61 — Schema / Compatibility Design for Knowledge Model v0**

目的不是继续讨论 ontology，而是把批准的语义规则翻译成可执行机器合同。

当前顺序：

```text
#61 Phase A
Schema / Compatibility Design
        ↓
Design Review
        ↓
Representative Migration Pilot
        ↓
验证 stable IDs / Graph / Query / Renderer / Evidence
        ↓
Canonical Data 分批迁移
        ↓
Validator / Schema Enforcement
        ↓
#15 Knowledge Model implementation complete
```

### #61 必须解决

- `type = concept | artifact | system | agent` 的机器表达；
- `kind` 受控 vocabulary；
- Capability / Scenario 等 Strong Profiles；
- legacy `standard / implementation / organization / capability / scenario` compatibility；
- `reference_project` 逐对象 Identity Target audit，不允许批量替换；
- Relation → relationship Statement 的兼容演进；
- Evidence / Assessment / missing-value 机器表达；
- Engine dual-read；
- stable ID / public route 保持。

### 当前明确不做

- 不全量迁移 01_State；
- 不发明 IA Query Language；
- 不选择数据库；
- 不强制 RDF / OWL；
- 不创建语义物理目录；
- 不顺带启用全量 Schema enforcement。

---

## F2-B — Human Interface Standards Package

**Gate B 仍 NOT PASS。**

#14 已有：

- Human Interface 标准基线；
- Reference Map；
- 综合 `IA-HI v0.1`；
- 第一轮 Requirement-based audit。

但 Gate B 仍要求五个可独立审计的 Draft Profile：

1. Information Architecture；
2. Information Presentation；
3. Interaction；
4. Visual Presentation；
5. Accessibility / Conformance。

每个 Profile 应包含：

- 用户任务 / Context of Use；
- 上游标准 / Mature Prior Art；
- Adopt / Profile / Extend / Invent；
- BCP 14 Requirement IDs；
- 可执行 conformance 方法；
- 与其他 Profile 的依赖 / 冲突处理。

### 与知识模型的关系

#15 的语义模型已经批准，因此 Human Interface 不再等待“我们到底怎样理解 Method / Framework / Design System”等基本身份问题。

但在大量收录这些 Prior Art 前，应先让 #61 + Migration Pilot 给机器一个可用合同。

因此当前顺序仍是：

```text
#61 Schema / Compatibility Design
        ↓
Representative Migration Pilot
        ↓
#14 五个 Human Interface Draft Profiles
        ↓
Gate B Audit
        ↓
Reference Implementation 恢复为主要 P0
```

---

# F3 — Open Collaboration：V0.1 Pilot 完成

**PASS — Draft Profile + GitHub-native Pilot completed.**

已经落地：

- `CONTRIBUTING.md`；
- root `AGENTS.md`；
- Work Item Issue Form；
- PR Template；
- Ready / Claim / Handoff / Review Class 等协作语义；
- 真实任务 Pilot；
- friction / gap audit。

仍开放但不阻塞主线：

- PR #26：Open Collaboration v0.2 high-impact review；
- #27：Human / Agent 身份折叠；
- CODEOWNERS / Ruleset / automation 只有真实 friction 证明必要时增强；
- 不自动开发 Lease Server / heartbeat。

Open Collaboration 继续作为 cross-cutting operating layer，不作为第六条 knowledge-system route。

---

# F4 — Curation / Evidence / Machine Correctness：并行基础线

**NOT PASS / 持续推进。**

已经具备：

- deterministic Loader；
- Graph / Backlink Index；
- stable public object route；
- canonical storage contract；
- reference resolution health baseline。

当前并行重点：

1. **#61 Schema / Compatibility** — 当前与 F2 共用的最重要机器基础；
2. **#8 Validator / Schema correctness** — 待 v0 compatibility contract 明确后继续；
3. **#9 Curation / Contribution** — 最小收录、去重、版本更新、Review；
4. **#10 Evidence / Provenance / Trust** — Fact / Statement → Evidence → Source；
5. **#7 Query correctness** — scope 与 regression；
6. Legacy Relation cleanup — 与模型迁移分开处理。

知识模型 v0 已经为 #9/#10 提供了重要上游语义：Statement、Evidence、Assessment、Agent、Missing Semantics 等不再需要重新发明。

---

# 当前执行顺序

## 主线

```text
#61 Schema / Compatibility Design
        ← NOW
        ↓
Representative Migration Pilot
        ↓
#15 Machine Contract / Migration readiness
        ↓
#14 Human Interface 五个 Draft Profiles
        ↓
Gate B Audit
        ↓
Reference Implementation 恢复为 P0
```

## 并行线

```text
#8 Validator correctness
#9 Curation
#10 Evidence / Provenance
#7 Query correctness
```

这些工作可以并行研究，但不得抢占 #61 / Gate B 主闭环。

---

# Reference Implementation：当前仍保持 P1

现有网站、Renderer、Graph、Local Map 等继续作为：

> **Reference Implementation / Test Bed**

已完成且符合规范的实现不回滚。

当前不以增加网站功能作为主要进度指标。

以下仍等待 Gate B：

- #12 Capability-first Navigation；
- #13 Browser E2E / Accessibility；
- #16 Conformance-driven refactor；
- #17 Object Page Shell 后续；
- Search / Global Explore；
- Visual Tokens；
- 大型 Graph / Map UI。

---

# Foundation Gates

## Gate A — Repository Structure

**✅ PASS + implemented**

## Gate B — Human Interface

**❌ NOT YET PASS**

最低条件：

- [ ] Information Architecture Draft；
- [ ] Information Presentation Draft；
- [ ] Interaction Draft；
- [ ] Visual Presentation Draft；
- [ ] Accessibility / Conformance Draft；
- [ ] 关键 Requirement IDs + upstream basis；
- [x] Knowledge Representation Model Decision available；
- [ ] v0 machine compatibility / representative intake path usable；
- [ ] Gate B conformance audit。

## Gate C — Open Collaboration

**✅ PASS + V0.1 Pilot completed**

整个 Foundation Gate 仍因 Gate B 未通过而保持未完成。

---

# 项目原则

继续遵守：

> **Reuse Before Invent**
>
> **Adopt → Profile → Extend → Invent**
>
> **Evidence Before Assertion**
>
> **Fact ≠ Assessment**
>
> **Physical Storage ≠ Semantic Classification ≠ Index / View**
>
> **graph-native, database-agnostic**

新的标准、Schema、查询能力、交互规则、Agent 机制或治理方法，都先检查成熟方案空间，再决定 IA-specific 扩展。
