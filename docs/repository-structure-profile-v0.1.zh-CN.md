# InteropAtlas Repository Structure Profile v0.1

> 状态：Draft / Provisional Specification（草案 / 暂定规范）
>
> 关联：Issue #21；输入包括 `repository-structure-prior-art-and-options-v0.1.zh-CN.md` 与 `repository-current-to-target-mapping-v0.1.zh-CN.md`。
>
> 本 Profile 定义仓库的**职责边界、产物类型、目标结构与迁移合同**。它不是一次文件整理，也不在本文发布时自动执行目录迁移。

## 1. 规范关键词

本文中的 MUST、MUST NOT、SHOULD、SHOULD NOT、MAY 按 BCP 14（RFC 2119 + RFC 8174）理解。

## 2. 上游依据与依据强度

本 Profile 不是来自某一个“国际仓库目录标准”，而是对多类 Existing Standards & Prior Art 的 Profile。

| 上游依据 | 身份 | 直接采用的内容 | 依据强度 |
|---|---|---|---|
| GitHub Community Health / Issue & PR Templates | 平台官方约定 | README / CONTRIBUTING / CODE_OF_CONDUCT / SECURITY / SUPPORT / templates 的受支持位置与平台行为 | 强，平台级约束 |
| GitHub CODEOWNERS / Rulesets / Required Review | 平台官方机制 | ownership / review / protected main 的实现原语 | 强，平台级约束 |
| REUSE Specification 3.3 | 正式规范 | `LICENSES/` 根目录及许可证文件规则 | **规范性 MUST** |
| OpenSSF Best Practices / Scorecard | 成熟开放项目安全实践 | 安全政策、review、CI、维护健康度等检查思路 | 强参考 |
| W3C browser-specs / MDN BCD | 成熟机器可读知识仓库 | Data + Schema + Tooling + Tests 可在同一仓库共同演化 | 成熟先例 |
| CNCF Landscape | 成熟 Landscape 项目 | Data 与 Generator 在合同稳定后可拆分 | 成熟先例 |
| SPDX License List | 成熟标准数据项目 | Authoritative Source 与 Generated Outputs 明确分离 | 成熟先例 |
| Diátaxis / Docs as Code | 方法 / 框架 | 用户文档按任务组织；文档进入 version/review/test 工作流 | 方法依据 |
| InteropAtlas 自身实践 | 项目事实 | Data / Schema / Graph / Renderer 高频共同变化、现有路径耦合 | IA-specific evidence |

主要来源：
- GitHub Community Health: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file
- GitHub PR standardization: https://docs.github.com/en/pull-requests/reference/managing-and-standardizing-pull-requests
- GitHub Rulesets: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
- REUSE 3.3: https://reuse.software/spec/
- OpenSSF Best Practices: https://openssf.org/projects/best-practices-badge/
- W3C browser-specs: https://github.com/w3c/browser-specs
- MDN BCD: https://github.com/mdn/browser-compat-data
- CNCF Landscape: https://github.com/cncf/landscape
- SPDX License List: https://github.com/spdx/license-list-XML
- Diátaxis: https://diataxis.fr/
- Docs as Code: https://www.writethedocs.org/guide/docs-as-code/

## 3. 核心决策

### RS-D1 — 当前采用 Layered Monorepo

**Decision: ACCEPTED FOR v0.1.**

InteropAtlas 当前 **SHOULD** 继续保持单仓，但在仓库内部建立明确逻辑层；现在不拆成 data / engine / site / specification 多仓。

理由：
- 项目仍处于 Pre-Alpha；
- Canonical Data、Schema、Graph、Validator、Renderer 仍高频共同演化；
- 原子 PR 可以同时修改 Data Contract 与实现；
- 当前拆仓会提高 Issue / PR / Agent context 的协调成本；
- 成熟先例表明“先单仓共同演化、合同稳定后抽离”是可行路径。

### RS-D2 — Canonical Data 使用一个显式逻辑边界

**Decision: ACCEPTED IN PRINCIPLE.**

目标结构采用 `data/` 作为 Canonical Atlas Object 的候选根目录。物理迁移尚未执行。

具体路径：

```text
data/
  standards/
  capabilities/
  implementations/
  organizations/
  scenarios/
  reference-projects/   # 名称未来可能随 #15 演化
  relations/
  gaps/
  maps/
```

`data/` 这个名字是 IA Profile 选择，不是国际标准要求。

### RS-D3 — IA 自产 Specification 与普通知识文档分离

**Decision: ACCEPTED IN PRINCIPLE.**

目标采用独立 `specs/` Zone。`specs/` 是候选短名，迁移前允许在 migration review 中改成 `specifications/`，但 Specification Artifact 与 ordinary docs 的逻辑分离已确定。

### RS-D4 — Research 与 Specification 分离

**Decision: ACCEPTED IN PRINCIPLE.**

Prior Art、Options、Audit、Fit Test 等研究性产物目标进入 `research/` Zone，不与规范要求混在同一平铺目录。

### RS-D5 — Engine 当前不拆仓

**Decision: ACCEPTED.**

先通过目录、API、Data Contract 建立 extraction-ready boundary；只有 Engine 出现独立 release / ownership / compatibility contract 后再评估拆仓。

### RS-D6 — Generated Site / Export 永不成为第二事实源

**Decision: ACCEPTED.**

GitHub Pages、HTML、Markdown、JSON/RDF export 等 Generated Views 必须从 Canonical Facts / Contracts 生成；Generated Artifact 不得成为 competing source of truth。

### RS-D7 — AGENTS.md 属于 Repository Agent Instructions，而非项目定义

**Decision: ACCEPTED.**

未来可在 root 使用 `AGENTS.md`，但内容必须由 Open Collaboration Profile 约束。它不得替代 README、CONTRIBUTING、Governance 或领域 Specification。

## 4. Artifact Taxonomy

仓库 Artifact identity 与物理路径是两个维度。

| Artifact Class | 主要职责 | Canonical Fact? | 典型生命周期 |
|---|---|---:|---|
| Canonical Data Object | 对现实互操作知识对象的结构化事实 | 是 | active / deprecated / superseded |
| Schema / Contract | 定义数据和接口允许的结构 | 否 | draft → stable → revised |
| Specification / Profile | IA 自产、可实现和可验证的规范要求 | 否 | draft → candidate → stable → superseded |
| Methodology / Guide | 推荐的方法和操作方式 | 否 | note → guide → revised |
| Research / Prior Art | 调研、Fit Test、方案比较、证据汇总 | 否 | living / point-in-time / archived |
| Architecture Reference | 系统结构、边界、数据流解释 | 否 | provisional → revised |
| Decision Record | 重要选择、理由和替代方案 | 否 | proposed → accepted → superseded |
| Experiment Record | 可复现探索、fixture、prototype、结果 | 否 | planned → completed / abandoned |
| Audit / Conformance Report | 对某规范/实现版本的阶段性检查 | 否 | point-in-time |
| Governance Policy | 角色、授权、生命周期、治理约束 | 否 | draft → adopted → revised |
| Community / Contribution Guide | 参与、求助、提交和 Review 方式 | 否 | living |
| Implementation / Tool | Engine、Validator、Renderer、CLI、CI | 否 | versioned software |
| Generated Artifact / View | 网站、export、报告、索引 | 否 | regenerated |

### Artifact identity invariant

Artifact identity **MUST NOT** 只依赖目录位置。未来移动文件时，其 stable ID、规范身份、版本、状态和语义 **SHOULD** 保持可追踪。

## 5. Target Repository Zones

v0.1 的目标逻辑结构：

```text
/
  README.md
  CONTRIBUTING.md
  LICENSE.md
  LICENSES/
  [future CODE_OF_CONDUCT.md]
  [future SECURITY.md]
  [future SUPPORT.md]
  [future AGENTS.md]

  .github/
    workflows/
    [future ISSUE_TEMPLATE/]
    [future PULL_REQUEST_TEMPLATE.md]
    [future CODEOWNERS or supported location]

  data/
    standards/
    capabilities/
    implementations/
    organizations/
    scenarios/
    reference-projects/
    relations/
    gaps/
    maps/

  schemas/
  engine/
  tools/
  tests/

  specs/
    repository-structure/
    knowledge-object-classification/
    human-interface/
    open-collaboration/
    ...

  research/
    prior-art/
    fit-tests/
    audits/
    options/

  docs/
    architecture/
    project/
    tutorial/
    how-to/
    reference/
    explanation/

  governance/
  experiments/
  examples/
```

### 重要说明

- 这是**目标 Zone Map**，不是要求一次创建所有空目录。
- 某个 Zone 只有出现真实 Artifact 后才 SHOULD 创建。
- `docs/` 的 Diátaxis 子目录只适用于真正面向用户/贡献者的文档；Specification、Research、Governance 不应仅因为是 Markdown 就进入 `docs/`。
- `reference-projects/` 的具体名称受 #15 Non-normative Knowledge Object Model 影响，迁移前不得冻结。

## 6. Normative Requirements

### IA-RS-001 — Root 是公开项目入口

Root **MUST** 优先服务第一次进入仓库的人类贡献者和通用工具。

Root **SHOULD** 只保留项目入口、社区健康、法务和少量一等逻辑 Zone；**MUST NOT** 演化成 Agent 私有状态或临时工作文件集合。

Basis: GitHub Community Health + Human-first principle.

### IA-RS-002 — Canonical Data 必须有唯一显式边界

所有 Canonical Atlas object families **MUST** 属于同一个逻辑 Data Root。

Loader **MUST NOT** 依赖“某几类对象恰好散落在 root”作为长期数据模型。

Basis: W3C browser-specs / MDN BCD / IA current loader evidence.

### IA-RS-003 — Data、Schema、Implementation 必须可区分

Canonical Facts、Schema/Contract 与 Engine/Tooling **MUST** 是不同 Artifact zones。

Schema **MUST NOT** 被视为事实实例；Engine **MUST NOT** 成为隐藏事实源。

### IA-RS-004 — Source of Truth 与 Generated Projection 必须分离

Generated HTML、site、export、indexes **MUST NOT** 与 Canonical Facts 竞争事实源身份。

Generated artifacts **SHOULD** 可删除并从源重新生成。

Basis: SPDX source/generated pattern + existing IA Pages pipeline.

### IA-RS-005 — Specification 与 Research 必须区分

带 BCP 14 Requirements 的 IA Specification / Profile **MUST** 与 Prior Art、Options、Working Notes、Fit Test、Audit 等 Research Artifact 可区分。

Research result **MUST NOT** 因与 Specification 同在一个 `docs/` 目录而被误认为规范要求。

### IA-RS-006 — Governance 与 Agent Instructions 不得取代公共贡献合同

AGENTS.md **MUST NOT** 替代 README / CONTRIBUTING / Governance / Specification。

任何只有 Agent 能看到或理解的任务规则 **MUST NOT** 成为开放协作的唯一真实规则。

Basis: AGENTS.md role + Open Collaboration Profile.

### IA-RS-007 — Community Health 应采用平台原生位置

GitHub 能原生识别的 Community Health / Issue / PR 文件 **SHOULD** 使用 GitHub 支持的位置和格式，而不是 IA 自创平行目录。

Basis: GitHub official docs.

### IA-RS-008 — License layout 应优先兼容 REUSE

若项目采用 REUSE 3.3，则 License Files **MUST** 按 REUSE 规范位于根级 `LICENSES/`，且该目录 **MUST NOT** 混入其他文件。

当前 `LICENSES/` 方向保留。

### IA-RS-009 — Tests 是一等验证 Artifact

随着 Validator、Query、Specification Conformance、Site E2E 出现，测试 **SHOULD** 具有明确可发现位置和职责。

是否 root `tests/` 或 component-local tests 可以按测试类型 Profile；但测试 **MUST NOT** 只存在于聊天说明或不可复现人工步骤中。

### IA-RS-010 — 迁移必须保持语义不变量

Canonical path migration **MUST** 可验证。

对于 `data/` 迁移，至少保持：
- object count 不因移动改变；
- relation count 不变；
- resolved graph edge count 不变；
- `reference_issues = 0`；
- stable object IDs 不变；
- generated public URL 不因 source physical path 被强制改变。

### IA-RS-011 — 路径合同必须集中化

Loader / CI / Tooling **SHOULD** 通过一个明确 Data Root / repository contract 获取路径，不应在多个文件重复硬编码全部 object-family root paths。

### IA-RS-012 — Internal links 与索引必须可验证

Specification、Research、Docs 的 internal links / navigation indexes **SHOULD** 进入自动检查，避免物理路径与手工导航长期漂移。

### IA-RS-013 — Monorepo 必须保持未来可抽离

当前单仓结构 **SHOULD** 通过清晰目录和接口边界保持 extraction-ready。

只有出现独立 release、治理、ownership、兼容性或部署需求时，才 SHOULD 拆出独立 repository。

### IA-RS-014 — 不创建空分类以追求形式完整

Target Zone **MUST NOT** 被解释为“一次性创建所有目录”。没有真实 Artifact 的 Zone MAY 不存在。

### IA-RS-015 — Task context 必须能够指向 Artifact contract

公开 Work Item / Issue **SHOULD** 能引用其修改的 Artifact class、上位 Specification 和允许作用域，使 Human / Agent 无需依赖某个聊天窗口理解仓库边界。

Basis: Open Collaboration Profile shared interface.

## 7. Community Health / Collaboration Target Set

Profile 只定义目标，不在本阶段创建内容。

| File / Mechanism | 目标职责 | 来源 |
|---|---|---|
| `README.md` | 项目是什么、入口在哪里 | GitHub convention |
| `CONTRIBUTING.md` | Human-first 通用贡献合同 | GitHub Community Health |
| `CODE_OF_CONDUCT.md` | 社区行为边界 | GitHub Community Health |
| `SECURITY.md` | 漏洞报告与安全流程 | GitHub Community Health / OpenSSF |
| `SUPPORT.md` | 支持与非任务问题入口 | GitHub Community Health |
| `.github/ISSUE_TEMPLATE/` | 标准化 Work Item / Bug / Proposal 输入 | GitHub native |
| PR template | 目的、Issue、Evidence、Test、AI disclosure、Review checklist | GitHub native |
| `CODEOWNERS` | 责任区域与 Review routing | GitHub native |
| Ruleset / Required Review | main 的合并保护 | GitHub native |
| `AGENTS.md` | Agent-specific repository instructions | AAIF / AGENTS.md；受 #19 约束 |

## 8. Migration Plan

### Phase M0 — Contract first（当前阶段）

完成：
- Artifact Taxonomy；
- Target Zones；
- Repository Requirements；
- Open Collaboration boundary。

**不移动文件。**

### Phase M1 — Decouple paths

在任何 `data/` 迁移前：
1. Loader 引入显式 `data_root` contract；
2. object-family registry 集中定义；
3. CI path filter 来源集中化或减少重复；
4. 建立 migration regression test；
5. 建立 internal-link audit baseline。

### Phase M2 — Move Canonical Data

一次可审计迁移：root object dirs → `data/*`。

必须通过 IA-RS-010 invariants。

### Phase M3 — Classify non-data artifacts

在 #15 / #14 / #19 模型稳定后，再迁移：
- Specification → `specs/`；
- Prior Art / Fit Test / Audit → `research/`；
- Architecture / Project docs → `docs/*`；
- Governance → `governance/`。

### Phase M4 — Community surface implementation

根据 Open Collaboration Profile 实现：
- CONTRIBUTING update；
- templates；
- CODEOWNERS / rulesets；
- AGENTS.md；
- task/project fields。

### Phase M5 — Extraction review

只有在真实需求出现时评估 Engine / stable specification / generated distribution 是否拆仓。

## 9. Conformance Checklist

一个仓库结构变更在 Merge 前 SHOULD 回答：

- [ ] 变更对应哪个 Artifact class？
- [ ] 是否违反 Root public surface？
- [ ] 是否产生第二事实源？
- [ ] Specification / Research 身份是否清楚？
- [ ] 是否引入重复路径合同？
- [ ] 是否保持 stable IDs / Graph invariants？
- [ ] Internal links 是否验证？
- [ ] 是否让 Agent-only instruction 覆盖了 Human contract？
- [ ] 是否真的需要新 Zone / 新 repo，而不是为了形式整齐？

## 10. v0.1 结论

Repository Structure v0.1 的核心不是目录树，而是：

```text
Public Entry Surface
        ↓
Explicit Artifact Identity
        ↓
Canonical Data / Contracts / Implementations / Specs / Research / Governance 分层
        ↓
Generated Views 可再生
        ↓
Human-first, Agent-compatible collaboration
        ↓
Testable migration
        ↓
Extraction-ready, not prematurely split
```

**当前接受 Layered Monorepo 作为目标架构；物理迁移留给后续实施阶段。**
