# InteropAtlas Foundation First Phase v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: Working Plan / 暂定阶段计划
Document Created At: 2026-09-01T10:45:40+08:00
Document Updated At: 2026-09-01T23:37:20+08:00
Metadata Backfilled At: 2026-09-02T11:02:46+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: owner_confirmed_cutoff
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human — ff6962757
  GitHub Actor: ff6962757
-->

> 状态：Working Plan / 暂定阶段计划
>
> 当前阶段：**Foundation First**
>
> 当前主任务：**#14 Human Interface Standards Package / IA Design Profile**

## 0. Foundation Gate 状态

截至 2026-09-01：

- **Gate A — Repository Structure：PASS + implemented**；
- **Gate B — Human Interface：NOT YET PASS**；
- **Gate C — Open Collaboration：PASS + V0.1 Pilot completed**；
- Knowledge Model v0 的 machine contract + Representative Migration Pilot 已完成。

整个 Foundation Gate 仍未完成，当前唯一主线 Gate 是 Gate B；F4 Machine / Curation / Trust 继续作为并行基础线。

## 1. Foundation First 当前含义

Foundation First 不等于继续整理目录，也不等于无限研究基础理论。

当前原则是：

> **先让知识语义、机器合同、人机界面规范、可信收录和协作边界达到最小可依赖状态，再扩大 Reference Implementation 与高级产品能力。**

主链已经推进到：

```text
Knowledge Model v0
✅ APPROVED
        ↓
Schema / Compatibility + I1–I5
✅ COMPLETE
        ↓
Representative Migration Pilot
✅ COMPLETE
        ↓
Human Interface Standards Package
🟡 NOW
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

#### 状态

**CORE MACHINE CONTRACT + REPRESENTATIVE PILOT COMPLETE**

已完成：

- Prior Art / 成熟标准研究；
- SQL / RDF / Wikibase / Property Graph 技术栈比较；
- 10 个真实对象 Fit Test；
- Model Decision / Stress Test；
- #58 / PR #60：Minimum Knowledge Representation Contract v0.1；
- #61 Schema / Compatibility Design；
- I1 Semantic Normalization；
- I2 Kind Registry + Validator skeleton；
- I3 v0 Identity / Strong Profile Schemas；
- I4 Relation ID-only + Context compatibility；
- I5 deterministic Machine Review；
- I6 Representative Migration Pilot。

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

#### Representative Migration Pilot 结果

真实 Pilot 已验证：

- Capability → `concept / capability`；
- Scenario → `concept / scenario`；
- Implementation → `system / platform_service`；
- Organization → `agent / organization`；
- Relation → ID-only endpoint；
- Stable ID 不变；
- 121 Objects / 107 Relations / 170 Graph edges 保持；
- Graph reference issues = 0；
- Machine Review deterministic errors = 0；
- Legacy + v0 Human Route 可共存；
- representative Query / Renderer / public route 不退化。

Pilot 还发现并修复了：

1. YAML unquoted date 进入 v0 Schema 时产生的类型差异；
2. capability-specific Query 把无上下文 Relation 错当成任意 capability evidence 的假阳性。

#### 明确保留的 migration debt

以下不再阻塞 Human Interface 主线：

- Artifact 上 Legacy `maturity` → Assessment；
- Relation bare `confidence` → assessor / basis / Assessment；
- `reference_project` Identity Target audit；
- `api / interface / device_class` boundary Standard audit；
- `open_source_project` organization audit；
- Legacy Relation stale type hint cleanup；
- full Canonical migration；
- repository-wide Schema enforcement。

Full migration / enforcement 不因 Pilot PASS 自动获得授权。

---

### F2-B Human Interface Standards Package

### 状态

**MAIN P0 / Gate B NOT PASS**

已有：

- Human Interface 标准基线；
- Reference Map；
- 综合 `IA-HI v0.1`；
- 第一轮 Requirement-based audit。

现在需要形成五个独立 Draft Profiles：

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

Knowledge Model 和 representative machine intake path 已不再阻塞 #14。

因此现在的主顺序是：

```text
#14 五个 Human Interface Draft Profiles
        ↓
Requirement coverage / conflict rules
        ↓
Gate B Conformance Audit
        ↓
Reference Implementation 恢复为主要 P0
```

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
- semantic normalization；
- controlled Kind Registry；
- v0 Identity / Strong Profile Schemas；
- Relation compatibility；
- Graph / Backlink Index；
- stable public object routes；
- canonical storage contract；
- deterministic Machine Review；
- representative Canonical migration regression；
- reference resolution health baseline。

当前并行基础工作：

1. #8 Validator / Schema correctness；
2. #9 Curation / Contribution；
3. #10 Evidence / Provenance / Trust；
4. #7 Query correctness；
5. migration debt audit / cleanup。

这些工作继续复用同一 Knowledge Model，不另起一套 Fact / Evidence / Assessment 语义。

---

# 3. Reference Implementation 的定位

当前网站、Renderer、Graph、Local Map 等继续作为：

> **Reference Implementation / Test Bed**

规则：

- 已完成且符合上游规范的实现不回滚；
- 当前不以新增网页功能作为主要进度指标；
- #12 / #13 / #16 / #17 等继续保留，但不抢占 #14 / Gate B 主线；
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
- [x] representative machine intake / compatibility path usable；
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
migration debt audit
```

## 单独高影响决策门

```text
Full Canonical Migration
Repository-wide Schema Enforcement
Ruleset / Governance Automation
```

这些不会自动执行。

---

# 6. 当前下一小步

**开始 #14 的 Human Interface Package consolidation / gap audit。**

第一步不是改网页，而是把已有标准基线、Reference Map、综合 IA-HI 草案和 conformance audit 对齐到五个 Profile：

```text
existing standards + prior art
        ↓
existing IA-HI requirements
        ↓
five-profile coverage matrix
        ↓
gaps / conflicts / duplicated rules
        ↓
Draft Profile extraction
        ↓
Gate B audit
```

只有规范覆盖与验收合同清楚后，Reference Implementation 才恢复为主要实现线。

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
