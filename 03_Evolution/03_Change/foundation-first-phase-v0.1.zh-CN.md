# InteropAtlas Foundation First Phase v0.1

> 状态：Working Plan / 暂定阶段计划
>
> 当前阶段：**Foundation First**
>
> 当前主任务：**#61 Schema / Compatibility Design for Knowledge Model v0**

## 0. Foundation Gate 状态

截至 2026-09-01：

- **Gate A — Repository Structure：PASS + implemented**；
- **Gate B — Human Interface：NOT YET PASS**；
- **Gate C — Open Collaboration：PASS + V0.1 Pilot completed**。

整个 Foundation Gate 仍未完成，主要原因是 Gate B 尚未通过，同时 F4 Machine / Curation / Trust 仍需补齐最小可靠性。

## 1. Foundation First 当前含义

Foundation First 不等于继续整理目录，也不等于无限研究基础理论。

当前原则是：

> **先让知识语义、机器合同、人机界面规范、可信收录和协作边界达到最小可依赖状态，再扩大 Reference Implementation 与高级产品能力。**

当前主链已经从旧的：

```text
Knowledge Object Fit Test
→ Model Decision
```

推进到：

```text
Knowledge Model v0
✅ APPROVED
        ↓
Schema / Compatibility Design
🟡 NOW
        ↓
Representative Migration Pilot
        ↓
Human Interface Standards Package
        ↓
Gate B Audit
        ↓
Reference Implementation 恢复为主要实现线
```

---

# 2. 四个基础工作包

## F1 — Repository Structure & Artifact Boundaries

### 状态

**COMPLETE / PASS**

已经实施：

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

关键不变量：

> **Physical Storage ≠ Semantic Classification ≠ Index / View**

Repository Structure 不再等待 Knowledge Model 决定语义文件夹。

---

## F2 — Knowledge Representation + Human Interface

### F2-A Knowledge Representation

#### 已完成

- Prior Art / 成熟标准研究；
- SQL / RDF / Wikibase / Property Graph 技术栈比较；
- 10 个真实对象 Fit Test；
- Model Decision / Stress Test；
- #58 / PR #60：Minimum Knowledge Representation Contract v0.1 正式批准。

采用：

```text
Core Identity Families
concept / artifact / system / agent
```

以及：

- Identity Target Rule；
- Kind / Strong Profile / Role / Authority 分层；
- Object / Statement 分离；
- Context / Evidence / Provenance；
- Fact / Assessment 分离；
- missing / unknown / explicit none 分离；
- graph-native, database-agnostic。

#### 当前任务：#61

**Schema / Compatibility Design for Knowledge Model v0**

#61 先做 Phase A 设计：

1. 4-family machine discriminator；
2. `kind` controlled vocabulary；
3. Capability / Scenario / Standard / System / Agent Strong Profiles；
4. legacy → v0 compatibility matrix；
5. Relation / Statement compatibility；
6. Evidence / Missing semantics；
7. Engine dual-read strategy；
8. stable ID / stable public route guarantees。

只有设计经过 Review 后，才进入 Representative Migration Pilot。

#### Representative Migration Pilot

Pilot 只选少量代表对象：

- Standard / Artifact；
- Implementation / System；
- Organization / Agent；
- Capability；
- Scenario；
- Apple HIG / AGENTS.md 等 boundary objects；
- 少量 Relations；
- 至少一个 Fact / Assessment 债务样本。

Pilot 必须验证：

- stable ID 不变；
- Graph / edges 不意外断裂；
- public routes 不变；
- representative queries 可表达；
- Engine legacy + v0 可共存；
- Renderer 不退化；
- Evidence / Assessment 边界更清楚。

不允许直接 big-bang migration。

---

### F2-B Human Interface Standards Package

### 状态

**IN PROGRESS / Gate B NOT PASS**

已有：

- Human Interface 标准基线；
- Reference Map；
- 综合 `IA-HI v0.1`；
- 第一轮 Requirement-based audit。

仍需形成五个独立 Draft Profiles：

1. Information Architecture；
2. Information Presentation；
3. Interaction；
4. Visual Presentation；
5. Accessibility / Conformance。

每个模块至少需要：

- 用户任务 / Context of Use；
- 正式标准与 Mature Prior Art；
- Adopt / Profile / Extend / Invent；
- Requirement IDs；
- conformance 方法；
- 模块依赖 / 冲突处理。

### 当前依赖关系

Knowledge Model 的语义 Decision 已不再阻塞 #14。

但为了让 Method / Framework / Design System / Evidence 等对象真正进入 Canonical State 并可被机器稳定使用，当前先完成 #61 + Representative Migration Pilot。

然后回到 #14，完成五个 Profile 与 Gate B Audit。

---

## F3 — Open Collaboration / Human–AI Collaboration

### 状态

**COMPLETE AT V0.1 PILOT / Gate C PASS**

已经落地：

- `CONTRIBUTING.md`；
- `AGENTS.md`；
- Work Item Issue Form；
- PR Template；
- task lifecycle / handoff / review semantics；
- GitHub-native 实际 Pilot；
- friction / gap audit。

后续但不阻塞主线：

- PR #26 Open Collaboration v0.2；
- #27 participant / Agent identity；
- Issue Fields / CODEOWNERS / Ruleset / automation 按实际摩擦增加；
- 不自动创造 Lease Server / heartbeat。

Open Collaboration 继续作为 cross-cutting operating layer，而不是第六条 knowledge-system route。

---

## F4 — Curation / Evidence / Machine Correctness

### 状态

**IN PROGRESS / NOT PASS**

已经具备：

- deterministic Loader；
- Graph / Backlink Index；
- stable public object routes；
- canonical storage contract；
- reference resolution health baseline。

当前并行基础工作：

1. #61 Schema / Compatibility；
2. #8 Validator / Schema correctness；
3. #9 Curation / Contribution；
4. #10 Evidence / Provenance / Trust；
5. #7 Query correctness；
6. legacy Relation cleanup。

#58 的知识模型 Decision 已经为 #9 / #10 提供共同语义基础，后续应复用，不重复设计另一套 Fact / Evidence / Assessment 模型。

---

# 3. Reference Implementation 的定位

当前网站、Renderer、Graph、Local Map 等继续作为：

> **Reference Implementation / Test Bed**

规则：

- 已完成且符合上游规范的实现不回滚；
- 当前不以新增网页功能作为主要进度指标；
- #12 / #13 / #16 / #17 等继续保留，但不抢占 #61 / Gate B 主线；
- Human Interface Profile 可以使用现有网站产生 conformance evidence；
- 现有代码不能反向决定语义模型或 UI 规范。

---

# 4. Foundation Gates

## Gate A — Repository Structure

**✅ PASS**

- [x] Repository Structure Profile；
- [x] 三大生命周期区域；
- [x] Canonical State / Runtime 迁移；
- [x] storage / semantics / route 解耦；
- [x] docs / Evolution boundary；
- [x] migration regression baseline。

## Gate B — Human Interface

**❌ NOT PASS**

- [ ] Information Architecture Draft；
- [ ] Information Presentation Draft；
- [ ] Interaction Draft；
- [ ] Visual Presentation Draft；
- [ ] Accessibility / Conformance Draft；
- [ ] 关键 Requirements 有上游依据；
- [x] Knowledge Representation Model Decision available；
- [ ] representative machine intake / compatibility path usable；
- [ ] Gate B conformance audit。

## Gate C — Open Collaboration

**✅ PASS**

- [x] Open Collaboration Profile v0.1；
- [x] participant/task/review/handoff semantics；
- [x] GitHub-native mapping；
- [x] Collaboration Pilot；
- [x] friction / gap audit。

---

# 5. 当前执行顺序

## P0 主线

```text
#61 Schema / Compatibility Design
        ↓
Representative Migration Pilot
        ↓
#15 Knowledge Model implementation readiness
        ↓
#14 Human Interface 五个 Draft Profiles
        ↓
Gate B Audit
        ↓
Reference Implementation 恢复为 P0
```

## Foundation 并行线

```text
#8 Validator correctness
#9 Curation
#10 Evidence / Provenance
#7 Query correctness
```

## 后续演化线

```text
PR #26 Open Collaboration v0.2 review
#27 participant / Agent identity research
```

---

# 6. 当前下一小步

**开始 #61 Phase A：Schema / Compatibility Design。**

第一小步只做 Design Draft，不改 Canonical Data：

```text
Approved semantic model
        ↓
proposed machine contract
        ↓
legacy compatibility matrix
        ↓
Strong Profile design
        ↓
Relation / Statement compatibility
        ↓
Engine dual-read strategy
        ↓
Review Gate
```

只有这个 Design Draft 明确以后，才进入 Representative Migration Pilot。

---

# 7. 采用原则

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

所有 Schema、Evidence、交互、查询、协作和治理设计都先检查成熟标准 / Prior Art，再做最小 IA-specific 扩展。
