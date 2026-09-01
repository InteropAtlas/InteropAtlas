# InteropAtlas 当前路线图

> 状态：Living Roadmap（持续更新路线图）
>
> 当前阶段：**Foundation First（基础先行）**
>
> 当前主任务：**#14 Human Interface Standards Package / IA Design Profile**
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
   ✅ Knowledge Model v0 已批准

4. 把知识规则变成机器可执行合同
   ✅ I1–I6 + Representative Migration Pilot 已完成

5. 完成面向人的信息组织 / 呈现 / 交互规范
   🟡 NOW — #14 / Gate B

6. 按规范继续建设 Reference Implementation
   ⬜ NEXT AFTER GATE B

7. 增加 Search / Compare / Maps / Pathfinder / Analysis
   ⬜ LATER

8. Federation / 多后端 / 更高级治理
   ⬜ FUTURE
```

当前负责人需要重点把控的是：

- 项目 Scope 与边界；
- 核心语义原则；
- Human Interface 的关键取舍与用户任务；
- 高影响迁移 / enforcement / governance 决策；
- Foundation Gate 是否达到可依赖状态。

具体 Schema 语法、Loader、CI、migration script 等属于 Implementation View，不要求负责人全部掌握。

---

# 当前总体判断

Repository Structure、Knowledge Model v0 的机器合同、Open Collaboration v0.1 都已不再是主阻塞。

Knowledge Model 采用的 Core Identity Families：

```text
concept
artifact
system
agent
```

并已经把以下原则落实到 Runtime / Schema / Machine Review / 真实 Pilot：

- Identity Target Rule；
- `type / kind / Strong Profile / roles / authority` 分层；
- Object Property ≠ Statement / Claim；
- Object Source ≠ Statement Evidence；
- Fact ≠ Assessment；
- known / unknown / explicit none / not recorded 分离；
- semantic model ≠ validation ≠ serialization ≠ query；
- graph-native, database-agnostic；
- **Physical Storage ≠ Semantic Classification ≠ Index / View**。

#61 已完成从设计到 I1–I6 的整个 approved implementation sequence。Representative Migration Pilot 证明 Legacy/v0 可以共存，并在真实 Canonical Data 上保持 stable IDs、Graph、Query 和 Human Route。

因此项目现在应停止把“继续钻知识模型实现”当作默认 P0，主线正式转回 Human Interface。

当前 Foundation 状态：

```text
F1 Repository Structure        ✅ COMPLETE
F2-A Knowledge Representation ✅ MACHINE CONTRACT + PILOT COMPLETE
F2-B Human Interface           🟡 MAIN P0 / GATE B
F3 Open Collaboration          ✅ V0.1 PILOT COMPLETE
F4 Curation / Evidence /
   Machine Correctness         🟡 PARALLEL FOUNDATION LINE
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

### ✅ 已完成的主闭环

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
✅ APPROVED / ADOPTED

#61 Schema / Compatibility Design
✅

I1 Semantic Normalization
✅

I2 Kind Registry + Validator skeleton
✅

I3 v0 Identity / Strong Profile Schemas
✅

I4 Relation ID-only + Context compatibility
✅

I5 Deterministic Machine Review
✅

I6 Representative Migration Pilot
✅
```

### Representative Migration Pilot 结果

Pilot 已在真实 Canonical Data 中迁移小型代表切片：

- Capability → `concept / capability`；
- Scenario → `concept / scenario`；
- Implementation → `system / platform_service`；
- Organization → `agent / organization`；
- 一个 Relation → ID-only endpoint。

验证结果：

- stable IDs 保持；
- 121 Objects / 107 Relations / 170 Graph edges 保持；
- Graph reference issues = 0；
- Machine Review deterministic errors = 0；
- Legacy/v0 Human Route 双读工作；
- stable public object route 保持；
- capability supportability query 保持正确结果；
- Pilot 还发现并修复了一个 capability context 泄漏造成的 Query 假阳性。

### 仍存在、但不再阻塞 #14 的 migration debt

以下问题继续作为明确债务，而不是继续把 F2-A 无限延长：

- Legacy `maturity` 等字段迁移到 Assessment；
- bare `confidence` 的 assessor / basis；
- `reference_project` 逐对象 Identity Target audit；
- Standard `api / interface / device_class` Identity Target audit；
- `organization_kind: open_source_project` Identity Target audit；
- Legacy Relation stale type hints cleanup；
- full Canonical migration；
- repository-wide Schema enforcement。

其中 **full migration / enforcement 是新的独立决策门**，不会因 Pilot PASS 自动启用。

---

## F2-B — Human Interface Standards Package

**Gate B 仍 NOT PASS。现在是主 P0。**

#14 已有：

- Human Interface 标准基线；
- Reference Map；
- 综合 `IA-HI v0.1`；
- 第一轮 Requirement-based audit。

Gate B 仍要求五个可独立审计的 Draft Profile：

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

### 当前 Human Interface 主问题

现在不应先问“网站再加什么功能”，而应先回答：

```text
人来到 InteropAtlas 想完成什么任务？
↓
信息应该怎样组织？
↓
一个对象页面先让人看到什么？
↓
关系、证据、比较、地图应该什么时候出现？
↓
交互怎样保持可预测、可恢复、可访问？
↓
怎样证明实现符合规范？
```

现有网站继续作为 Test Bed / Conformance Evidence Source，但不能反向决定规范。

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
- semantic normalization；
- controlled Kind Registry；
- v0 Identity / Strong Profile Schemas；
- Relation ID-only compatibility；
- Graph / Backlink Index；
- stable public object route；
- canonical storage contract；
- deterministic Machine Review；
- representative real-data migration tests；
- reference resolution health baseline。

当前并行重点：

1. **#8 Validator / Schema correctness** — 扩展 Machine Review，但不提前开启 repository-wide enforcement；
2. **#9 Curation / Contribution** — 最小收录、去重、版本更新、Review；
3. **#10 Evidence / Provenance / Trust** — Fact / Statement → Evidence → Source / Assessment；
4. **#7 Query correctness** — scope、context 与 regression；
5. migration debt queue — Assessment、Identity Target audit、Legacy Relation cleanup。

这些工作可以作为并行基础线推进，但不得抢占 #14 / Gate B 主闭环。

---

# 当前执行顺序

## 主线

```text
#14 Human Interface Standards Package
        ← NOW
        ↓
五个 Draft Profiles
        ↓
Requirement IDs / upstream basis / conformance methods
        ↓
Gate B Audit
        ↓
Reference Implementation 按规范恢复为 P0
        ↓
Search / Compare / Maps / Pathfinder / Analysis
```

## 并行线

```text
#8 Validator correctness
#9 Curation
#10 Evidence / Provenance
#7 Query correctness
migration debt audit
```

## 单独决策门

```text
Full Canonical Migration
Repository-wide Schema Enforcement
Ruleset / Governance Automation
```

这些不因 I6 PASS 自动执行。

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
- [x] v0 machine compatibility / representative intake path usable；
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
