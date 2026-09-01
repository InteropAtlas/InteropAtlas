# InteropAtlas Repository Structure — Prior Art & Options v0.1

> 状态：Research / Decision Input（研究与决策输入）
>
> 关联：Issue #21 `Repository Structure & Artifact Taxonomy v0.1`
>
> 本文件**不执行目录迁移**。目的只是先研究成熟方案、审计当前结构、定义 Artifact Taxonomy，并比较候选结构。

## 1. 问题不是“目录怎么摆得好看”

InteropAtlas 同时具有多种性质：

1. **Canonical Knowledge Dataset** — standards / capabilities / implementations / relations 等结构化事实；
2. **Schemas / Contracts** — 数据结构和验证合同；
3. **Deterministic Engine / Tooling** — Resolver、Graph、Query、Renderer 等；
4. **Specifications / Profiles** — IA 自己形成的 Human Interface、Open Collaboration 等规范；
5. **Research / Prior Art** — 外部标准、方法、参考实现调查；
6. **Documentation** — 面向贡献者、用户和维护者的解释、参考和操作说明；
7. **Governance / Collaboration** — CONTRIBUTING、Review、Decision、生命周期和项目治理；
8. **Reference Implementations / Generated Views** — GitHub Pages、Markdown / HTML 输出等。

因此 Repository Structure 是项目架构的一部分，而不是清理文件。

核心要求：

> **仓库首先必须像一个开放标准地图项目；同时对 Human、Agent、CI 和长期治理可理解。**

---

# 2. Prior Art

## 2.1 GitHub Community Health：根目录不是所有协作信息的唯一位置

GitHub 官方 Community Health 机制识别一组标准文件：

- README；
- CONTRIBUTING；
- CODE_OF_CONDUCT；
- SECURITY；
- SUPPORT；
- Issue templates；
- Pull Request templates。

对可存在多处的 Community Health 文件，GitHub 使用 `.github/` → root → `docs/` 的查找优先级；Issue templates 则有明确的 `.github/ISSUE_TEMPLATE/` 位置。

这说明：

- `.github/` 是 GitHub 平台集成层，不是普通项目知识目录；
- CONTRIBUTING / SECURITY 等属于公开项目协作合同；
- Issue / PR templates 可以标准化贡献输入，而不需要 IA 自造任务格式。

参考：
- https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file
- https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates

## 2.2 REUSE 3.3：许可证结构也可以机器可读

REUSE Specification 3.3 明确定义：

- 每个实际使用的 License 都应在根级 `LICENSES/` 目录存在对应 License File；
- 文件级 licensing information 可通过 comment header、`REUSE.toml` 等方式关联；
- `LICENSES/` 只承担许可证文本职责。

IA 已经存在 `LICENSES/`，说明当前方向与成熟方案兼容；后续应评估是否完整采用 REUSE，而不是重新设计文件级版权 / License 机制。

参考：https://reuse.software/spec/

## 2.3 W3C Specification Repositories：Specification 是独立、可贡献、可追踪的产物

W3C 多个规范仓库通常把以下内容保持为清晰的一等入口：

- README；
- CONTRIBUTING；
- CODE_OF_CONDUCT；
- LICENSE；
- specification source；
- 工作组 / spec metadata（例如 `w3c.json`）。

规范贡献通过 fork / branch / pull request 工作流进行，并明确贡献的知识产权 / Patent Policy 边界。

对 IA 的启示：

- **Specification 应被视为一种明确 Artifact，而不是普通设计笔记。**
- 未来稳定的 IA Specification 可以单独版本化甚至孵化为独立仓库，但这不意味着 Pre-Alpha 阶段就“一规范一仓库”。

参考：
- https://github.com/w3c/wcag
- https://github.com/w3c/rdf-primer
- https://github.com/w3c/sparql-query

## 2.4 W3C browser-specs：Data + Schema + Tooling + Test 可以共同存在于一个仓库

`w3c/browser-specs` 是一个机器可读 Web specification catalog。其仓库同时包含：

- `.github/`；
- schema；
- source / scripts；
- tests；
- machine-readable spec list；
- CONTRIBUTING / LICENSE / README；
- package / generated distribution outputs。

它证明：对于仍在共同演化的数据集、Schema 和工具链，**结构清晰的 Monorepo 完全可以是成熟方案**。

参考：https://github.com/w3c/browser-specs

## 2.5 MDN Browser Compat Data：领域数据可以在统一 Data Contract 下按对象域组织

MDN BCD 把 compatibility data 按 API / CSS / JavaScript / HTTP 等领域组织，并有独立 Schema 文档、验证和 tooling。

对 IA 的启示：

- 数据目录内部按 object family / domain 组织是合理的；
- 关键不在于目录是不是根级，而在于这些目录是否明确属于同一个 Canonical Data contract；
- Schema / validator 应能描述数据结构，而不是让目录位置本身承担全部类型语义。

参考：https://github.com/mdn/browser-compat-data

## 2.6 CNCF Landscape：Data Repository 与 Generator 可以分仓

CNCF Landscape 主仓库主要保存 landscape data 与 assets；生成软件位于独立 `landscape2` 仓库。

这个模式适合：

- 数据合同已经相对稳定；
- Generator 可以作为独立产品演化；
- 不需要大量 data + schema + generator 原子修改。

对 IA 当前阶段的判断：**可以作为未来 extraction pattern，但现在过早。**

参考：https://github.com/cncf/landscape

## 2.7 SPDX License List：Authoritative Source 与 Generated Multi-format Outputs 可以分离

SPDX License List 把 authoritative XML source 与生成的 JSON / JSON-LD / RDF / HTML / text outputs 分在不同仓库。

关键启示不是“必须多仓”，而是：

> **Source of Truth 与 Generated Projection 必须在结构和治理上明确分离。**

IA 当前 GitHub Pages 已经是 CI-generated artifact，没有把 HTML 回写成第二事实源，这一点应继续保持。

参考：
- https://github.com/spdx/license-list-XML
- https://github.com/spdx/license-list-data

## 2.8 Diátaxis + Docs as Code：文档按用户需求组织，不按“都是 Markdown”混在一起

Diátaxis 区分：

- Tutorial；
- How-to；
- Reference；
- Explanation。

Docs as Code 则强调：Documentation 与代码一样使用 version control、review、issue tracking 和 automated tests。

对 IA 的启示：

- `docs/` 不能长期只是“所有 Markdown 都放这里”；
- 但 Diátaxis 是**用户文档功能分类**，不能取代 Specification / Research / Governance 等 Artifact identity；
- 因此需要同时区分“这是什么 Artifact”和“这份文档服务什么用户任务”。

参考：
- https://diataxis.fr/
- https://www.writethedocs.org/guide/docs-as-code/

---

# 3. 当前 IA 仓库结构审计

当前根级主要包含：

```text
.github/
CONTRIBUTING.md
LICENSE.md
LICENSES/
README.md

standards/
capabilities/
implementations/
organizations/
scenarios/
reference-projects/
gaps/
relations/
maps/

schemas/
engine/
docs/
experiments/
```

## 3.1 当前结构的优点

- Canonical object families 非常直观；
- YAML 文件容易手工定位；
- Engine / Schemas / Docs 已经物理分离；
- Generated Pages 不在仓库维护第二份事实；
- Pre-Alpha 改动成本低。

## 3.2 当前结构的问题

### Root namespace 被 Canonical Data object families 占据

新增 object family 就继续增加根目录；项目入口、协作、规范、研究和数据之间没有一眼可见的层级。

### `docs/` Artifact identity 混合

当前 `docs/` 同时包含：

- Architecture；
- Roadmap；
- Methodology；
- Specification；
- Conformance Audit；
- Prior Art Research；
- Working Notes；
- Experiment records；
- Implementation Plan。

这些文件生命周期、规范强度和用户任务不同，但目录结构没有表达这种区别。

### Community Health 不完整

当前 `.github/` 主要只有 workflows；CONTRIBUTING 也仍主要描述数据贡献。

待 Foundation 规范完成后应评估：

- CODE_OF_CONDUCT；
- SECURITY；
- SUPPORT；
- Issue Forms；
- PR Template；
- CODEOWNERS；
- Rulesets / Required Review；
- AGENTS.md。

### 路径已经成为隐式 Contract

当前 `engine/bootstrap_query.py` 把以下 object directories 硬编码为根级路径：

```text
standards
capabilities
scenarios
organizations
implementations
reference-projects
gaps
relations
maps
```

两个 GitHub Actions workflows 也逐个监听这些目录。

因此把数据迁入 `data/` 不是 kosmetics（视觉整理），而是 Canonical Data location contract migration。

迁移必须同时处理：

- loader；
- CI path filters；
- tests；
- README / docs links；
- tooling；
- 可能的外部深链接。

## 3.3 一个重要原则

> **Artifact identity MUST NOT depend only on directory location.**

目录用于 discoverability 与 ownership；Artifact 本身还需要明确 kind / status / version / lifecycle metadata。

否则未来文件移动就会改变“它是什么”，这是不合理的。

---

# 4. Artifact Taxonomy v0.1 候选

当前至少需要区分以下 Artifact：

| Artifact | 主要职责 | 是否 Canonical Fact | 是否可能含 BCP 14 | 生命周期示例 |
|---|---|---:|---:|---|
| Canonical Data Object | 外部 / IA 事实对象 | 是 | 否 | active / deprecated |
| Schema / Contract | 数据结构和验证合同 | 否 | 可 | draft → stable |
| Specification / Profile | 可实现、可符合的 IA 要求 | 否 | 是 | draft → candidate → stable → superseded |
| Methodology / Guide | 推荐的方法 / 工作方式 | 否 | 通常否 | note → guide → revised |
| Research / Prior Art | 调研证据、方案比较 | 否 | 否 | living / archived |
| Architecture Reference | 系统结构与边界 | 否 | 可 | provisional → revised |
| Decision Record | 某个重要选择及其理由 | 否 | 否 | proposed → accepted → superseded |
| Experiment Record | 可复现探索 / 实验结果 | 否 | 否 | planned → completed / abandoned |
| Audit / Conformance Report | 某版本对 Requirement 的检查 | 否 | 否 | point-in-time |
| Governance Policy | 项目治理、授权、角色、变更规则 | 否 | 可 | draft → adopted → revised |
| Community / Contribution Guide | 如何参与 / 求助 / 报告问题 | 否 | 可 | living |
| Implementation / Tool | Engine / Renderer / CLI / CI | 否 | 否 | versioned software |
| Generated Artifact / View | HTML / JSON export / site / report | 否 | 否 | regenerated |

### Artifact identity 与文档类型是两个维度

例如：

- `Human Interface Specification` 是 **Specification**；
- 它的某个解释性 companion 文档可以是 Diátaxis **Explanation**；
- `Schema Reference` 是 **Reference documentation**，但 Schema 文件本身是 **Contract Artifact**。

不能用一个维度代替另一个维度。

---

# 5. 三个仓库结构候选

## Option A — Current-like Flat Monorepo

```text
/
  standards/
  capabilities/
  implementations/
  organizations/
  ...
  schemas/
  engine/
  docs/
  experiments/
```

### 优点
- 几乎零迁移成本；
- Object family 一眼可见；
- 现有 Engine / CI 全部兼容。

### 缺点
- Root namespace 持续膨胀；
- “数据层”不是一个显式边界；
- docs Artifact identity 继续混乱；
- 未来 tests / tools / governance / specifications 增加后更杂乱。

### 判断

适合 Bootstrap，**不适合作为当前目标结构直接冻结**。

---

## Option B — Layered Monorepo（当前推荐候选）

```text
/
  README.md
  CONTRIBUTING.md
  LICENSE.md
  LICENSES/
  [future community health files]
  [future AGENTS.md]

  .github/

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
  tests/
  tools/

  specs/
    human-interface/
    open-collaboration/
    repository-structure/
    ...

  docs/
    tutorials/
    how-to/
    reference/
    explanation/
    architecture/

  research/
    prior-art/
    audits/

  experiments/
  governance/
  examples/
```

> 上述名字只是结构候选，不代表现在立即创建全部目录。

### 优点

- `data/` 明确 Canonical Facts boundary；
- `specs/` 明确 IA-produced normative / provisional artifacts；
- `research/` 不再与 Specification 混在一起；
- `docs/` 可以真正服务用户文档，而不是承担所有 Markdown；
- schemas / engine / tests / tools 保持共同演化，适合当前 Pre-Alpha；
- Human / Agent / CI 都容易建立稳定入口。

### 缺点

- 需要一次有计划的数据目录迁移；
- 现有 loader / CI / links 必须更新；
- 目录过多时也可能产生“分类过度”，因此不能一次创建所有空目录。

### 当前判断

**最适合作为 V0.1 目标方向继续验证。**

但当前只接受它作为 Candidate，不在本研究步骤执行迁移。

---

## Option C — Multi-repo / Product Split

可能拆成：

```text
interopatlas-data
interopatlas-engine
interopatlas-site
interopatlas-specs
interopatlas-governance
```

或进一步一份正式规范一个 repo。

### 优点

- ownership / release / dependency 边界最清晰；
- 类似 CNCF Landscape data/generator、SPDX source/generated output；
- 稳定 Specification 可独立引用、版本化和治理。

### 缺点

- 当前 data / schema / engine / renderer 仍高速共同演进；
- 大量改动需要跨仓 coordination；
- Issue / PR / roadmap 分散；
- 对早期贡献者和 Agent 增加 discoverability / context 成本；
- 容易过早固化产品边界。

### 当前判断

**不适合 Pre-Alpha 当前阶段。**

但 Option B 应保留未来可抽离边界：

```text
Layered Monorepo
      ↓ contracts stabilize
optional extraction
      ↓
data / engine / stable specification / generated distribution
```

---

# 6. 当前推荐：Option B，但先规范、后迁移

当前暂定推荐：

> **Layered Monorepo now, extraction-ready later.**
>
> 现在使用分层单仓；以后合同稳定后允许按真实治理 / 发布需求拆仓。

理由：

1. IA 当前仍是 Pre-Alpha；
2. Schema、Data、Graph、Validator 互相反馈频繁；
3. 原子 PR 非常有价值；
4. Generated Website 已经不需要和 source 分仓，因为它不回写主仓；
5. 未来 Engine / Specification 的 extraction 可以通过清晰目录边界提前准备，而不必现在付出多仓协调成本。

## 6.1 当前先冻结的不是目录名，而是职责边界

建议先形成以下逻辑边界：

```text
Canonical Data
Schema / Contract
Implementation / Tooling
Specification / Profile
Research / Evidence
Documentation
Governance / Collaboration
Experiment
Generated View
```

具体是叫 `specs/` 还是 `specifications/`、`research/` 是否放进 `docs/`，应在下一轮用真实文件做迁移模拟后再决定。

---

# 7. 对当前仓库的第一组 Decision Candidates

以下只进入 Decision Queue，不立即执行。

## D1 — Canonical Data 是否进入 `data/`

当前倾向：**YES / Candidate**。

理由：使所有 Atlas object families 共享显式 source-of-truth boundary。

迁移前必须先做：
- loader 支持 configurable data root；
- CI 不再手写 9 份路径或集中定义路径；
- regression test；
- links / docs audit。

## D2 — `docs/` 是否继续承载 Specification

当前倾向：**NO / Candidate**。

`IA-HI Specification`、未来 Open Collaboration Profile 与 Repository Structure Profile 应被视为 project-generated Specification artifacts，而不是普通 documentation。

建议研究独立 `specs/` / `specifications/`。

## D3 — Research / Audit 是否继续与 Architecture / Guide 平铺

当前倾向：**NO / Candidate**。

Prior Art 与 point-in-time Audit 适合独立 `research/` 或明确子目录。

## D4 — 是否现在拆 Engine repo

当前倾向：**NO**。

Engine 与 Canonical Data contract 尚未稳定；先建立目录与接口边界即可。

## D5 — 是否现在创建 AGENTS.md

当前倾向：**NO，等待 #19 Profile。**

AGENTS.md 是 Repository Agent Instructions，不应替代 README / CONTRIBUTING / Governance，也不应由单一 Agent 当前习惯反推内容。

## D6 — 是否现在建立 GitHub Community Health files

当前倾向：**先定义职责，随后尽早实现。**

这类文件属于成熟平台原语，风险低，但其具体内容必须与 #19 Open Collaboration Profile、#9 Curation 与项目治理一致。

---

# 8. 下一小步

不迁移目录。

下一步对 **Option B** 做 `Current → Target Mapping`：

1. 把当前每一个根目录 / 重要文档分类到 Artifact Taxonomy；
2. 标出 ambiguous artifacts（例如 roadmap、audit、methodology、specification）；
3. 模拟目标路径，不实际移动；
4. 列出所有会被路径迁移影响的 Loader / CI / links / docs / tooling；
5. 比较 `specs/` vs `specifications/`、`research/` vs `docs/research/` 等少数命名决策；
6. 然后才形成 Repository Structure Profile v0.1 的第一版 BCP 14 requirements。

原则：

> **先定义 Artifact 与 Contract，再移动文件。**
