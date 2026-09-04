# InteropAtlas 正式文档地图

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-08-30T17:51:02+08:00
Document Updated At: 2026-09-05T03:51:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

`docs/` 保存**今天进入 InteropAtlas 时仍需要理解或遵守的长期文档（Living Documents）**。

本索引按“设计尺度”组织，而不是按文件创建时间平铺。研究、实验和历史变更过程分别进入 `03_Evolution/01_Research`、`03_Evolution/02_Experiments`、`03_Evolution/03_Change`。

Living Documents 的版本历史由 Git 提供，文件路径本身不再携带 `v0.1`、`v1.0` 等版本号。只有当版本号属于协议、Schema、标准对象、兼容契约或历史制品身份的一部分时，才保留在文件名中。

中文文档以自然中文为主阅读语言，首次出现的重要项目概念可保留规范英文锚点。项目的语言与翻译规则见 [`语言政策`](language-policy.zh-CN.md)，跨语言概念绑定见 [`术语登记表`](terminology-registry.md)。

## 0. 第一次进入项目：先读什么

### 人类贡献者 / 项目理解（Human）

```text
README.md
→ interopatlas-master-design.zh-CN.md
→ knowledge-philosophy-and-principles.zh-CN.md
→ public-commons-and-personal-knowledge-space.zh-CN.md
→ PROJECT_STATE.md
```

### 智能体 / 维护者（Agent / Maintainer）

```text
AGENTS.md
→ PROJECT_STATE.md
→ README.md
→ interopatlas-master-design.zh-CN.md
→ 当前阶段 / Issue / 契约（Current Phase / Issue / Contract）
```

不要把某一份阶段计划（Phase Plan）、旧五路线模型、某个工作空间（Workspace）或某个 P6 Issue 当成整个 InteropAtlas。

## 1. L0–L1：使命、哲学与总体设计

这些文件定义项目最高层方向。

- [`interopatlas-master-design.zh-CN.md`](interopatlas-master-design.zh-CN.md) — **当前总体设计（Master Design）**。解释地图优先（Atlas-first）、共享 / 个人 / 体验（Shared / Personal / Experience）、知识操作空间（Knowledge Operation Spaces）、人与智能体（Human + Agent）、成长循环，以及 P1–P6 的正确位置。
- [`knowledge-philosophy-and-principles.zh-CN.md`](knowledge-philosophy-and-principles.zh-CN.md) — 长期产品哲学，以及不应被局部实现静默改写的产品与建设原则。
- [`interopatlas-definition-and-scope.zh-CN.md`](interopatlas-definition-and-scope.zh-CN.md) — 项目定义、互操作问题边界和收录范围。

InteropAtlas 的核心产品哲学压缩为一个相互依存的命题：

> **知识属于公共共同体。视角属于个人。**  
> *Knowledge belongs to the commons. Perspective belongs to the individual.*

其动态展开是知识流动模型（Knowledge Flow Model）：

> **发现（Discover）→ 连接（Connect）→ 传递（Transmit）→ 转化（Transform）→ 复用（Reuse）→ 创造（Create）→ 公共共同体（Commons）↺**

个性化透明 / 可控 / 可逆、地图优先、先有证据再有断言、先选择再呈现、真实使用塑造本体模型，以及“采用 → 配置 → 扩展 → 发明（Adopt → Profile → Extend → Invent）”属于产品与建设原则，不再与核心哲学并列。

## 2. L2：知识空间与长期产品架构

- [`public-commons-and-personal-knowledge-space.zh-CN.md`](public-commons-and-personal-knowledge-space.zh-CN.md) — 公共知识共同体（Public Knowledge Commons）+ 个人知识空间（Personal Knowledge Space）；内容个性化、表达个性化、反信息茧房、隐私与可互操作个人空间。
- [`knowledge-workspace-design-principles.zh-CN.md`](knowledge-workspace-design-principles.zh-CN.md) — `规范知识 → 视角 / 选择 → 投影 → 工作空间（Canonical Knowledge → Perspective / Selection → Projection → Workspace）` 设计基线，以及百科式浏览、时间线、关系图、比较、证据（Wiki / Browse, Timeline, Graph, Compare, Evidence）等工作空间原则。
- [`human-agent-access-architecture-draft.zh-CN.md`](human-agent-access-architecture-draft.zh-CN.md) — V1 人 / 智能体访问（Human / Agent Access）、权限和候选写入（Candidate Write）架构草案。
- [`flat-graph-and-dynamic-maps.zh-CN.md`](flat-graph-and-dynamic-maps.zh-CN.md) — 扁平对象 + 丰富关系 + 动态地图（Flat Objects + Rich Relations + Dynamic Maps）的建模原则。

`architecture.zh-CN.md` 是 2026-09-02 总体设计升级之前的历史架构基线，**不再作为当前总体架构（Master Architecture）入口**。保留它用于理解演化历史；当前方向以总体设计 + V1 架构草案为准。

## 3. L3：成长、运行与演化机制

- [`practice-feedback-loop.zh-CN.md`](practice-feedback-loop.zh-CN.md) — 知识地图 ↔ 运行 / 实践（Atlas ↔ Runtime / Practice）的反馈机制。
- [`project-development-principles.zh-CN.md`](project-development-principles.zh-CN.md) — 项目建设原则与最小治理规则。
- [`five-route-operating-model.zh-CN.md`](five-route-operating-model.zh-CN.md) — **历史 / 局部运行模型（Operating Model）**：人类（Human）、机器（Machine）、策展（Curation）、信任（Trust）、治理（Governance）。它仍可作为协作 / 运行参考，但不再代表项目总体设计或总路线图（Roadmap）。

## 4. L4：路线图与当前基础建设周期

- [`interopatlas-long-term-roadmap.zh-CN.md`](interopatlas-long-term-roadmap.zh-CN.md) — **当前长期路线图（Long-term Roadmap）**；明确 P1–P6 只是第一轮 V1 基础建设 / 架构重新验证周期（Foundation / Architecture Revalidation Cycle）。
- [`../PROJECT_STATE.md`](../PROJECT_STATE.md) — 当前项目断点、当前阶段（Phase）、恢复入口（Resume Here）和门禁（Gate）。
- 当前 / 历史阶段计划、迁移计划和过渡材料（Phase Plan / Migration Plan / Transition Materials）位于 [`../03_Evolution/03_Change/`](../03_Evolution/03_Change/)。

实时施工状态始终以 `PROJECT_STATE.md` + GitHub Issue / PR + 更新的 Git 证据为准。

## 5. L5：V1 契约 / 规范 / 配置规范（Contracts / Specifications / Profiles）

### 规范知识 / 收录 / 迁移（Canonical / Intake / Migration）

- [`canonical-contract-architecture-draft.zh-CN.md`](canonical-contract-architecture-draft.zh-CN.md)
- [`canonical-write-intake-contract-architecture-draft.zh-CN.md`](canonical-write-intake-contract-architecture-draft.zh-CN.md)
- [`canonical-migration-architecture-draft.zh-CN.md`](canonical-migration-architecture-draft.zh-CN.md)
- [`knowledge-object-classification-specification.zh-CN.md`](knowledge-object-classification-specification.zh-CN.md)

### 人类界面（Human Interface）

- [`human-interface-profiles.zh-CN.md`](human-interface-profiles.zh-CN.md) — 人类界面配置规范（Human Interface Profile）总入口。
- [`human-interface-information-architecture-profile.zh-CN.md`](human-interface-information-architecture-profile.zh-CN.md)
- [`human-interface-information-presentation-profile.zh-CN.md`](human-interface-information-presentation-profile.zh-CN.md)
- [`human-interface-interaction-profile.zh-CN.md`](human-interface-interaction-profile.zh-CN.md)
- [`human-interface-visual-presentation-profile.zh-CN.md`](human-interface-visual-presentation-profile.zh-CN.md)
- [`human-interface-accessibility-conformance-profile.zh-CN.md`](human-interface-accessibility-conformance-profile.zh-CN.md)
- [`human-interface-specification.zh-CN.md`](human-interface-specification.zh-CN.md)
- [`human-readable-interaction-baseline.zh-CN.md`](human-readable-interaction-baseline.zh-CN.md)

### 开放协作 / 人机协作（Open Collaboration / Human–AI）

- [`open-collaboration-profile.zh-CN.md`](open-collaboration-profile.zh-CN.md)
- [`collaboration-task-system.zh-CN.md`](collaboration-task-system.zh-CN.md)
- [`task-reference-seeding-profile.zh-CN.md`](task-reference-seeding-profile.zh-CN.md)
- [`agent-onboarding-context-continuity-profile.zh-CN.md`](agent-onboarding-context-continuity-profile.zh-CN.md)
- [`agent-attribution-contribution-identity-profile.zh-CN.md`](agent-attribution-contribution-identity-profile.zh-CN.md)
- [`agent-continuation-bridge.zh-CN.md`](agent-continuation-bridge.zh-CN.md)

### 来源追踪 / 研究 / 治理（Provenance / Research / Governance）

- [`provenance-traceability-profile.zh-CN.md`](provenance-traceability-profile.zh-CN.md)
- [`research-governance.zh-CN.md`](research-governance.zh-CN.md)
- [`task-authority-governance-draft.zh-CN.md`](task-authority-governance-draft.zh-CN.md)

### 仓库 / 政策（Repository / Policy）

- [`repository-structure-profile.zh-CN.md`](repository-structure-profile.zh-CN.md)
- [`language-policy.zh-CN.md`](language-policy.zh-CN.md) — 中文优先阅读、英文国际版本、翻译与语言标签规则。
- [`terminology-registry.md`](terminology-registry.md) — 核心概念的规范英文身份、中文首选词和跨语言别名登记。

## 6. 演化材料：过程文件放在哪里

```text
03_Evolution/
├── 01_Research/      成熟先例 / 研究 / 审计 / 验证（Prior Art / Research / Audit / Verification）
├── 02_Experiments/   原型 / 实验 / 试运行（Prototype / Experiment / Dry Run）
└── 03_Change/        路线图历史 / 阶段计划 / 提案 / 迁移（Roadmap History / Phase Plan / Proposal / Migration）
```

- [`研究目录说明（Research README）`](../03_Evolution/01_Research/README.md)
- [`实验目录说明（Experiments README）`](../03_Evolution/02_Experiments/README.md)
- [`变更目录说明（Change README）`](../03_Evolution/03_Change/README.md)

研究结论不能因为“很有启发”就自动成为稳定架构；历史变更（Change）文件也不能因为仍在仓库里就被当成当前路线。

## 7. 文档层级规则

```text
使命 / 哲学（Mission / Philosophy）
        ↓
总体设计（Master Design）
        ↓
架构 / 长期方向（Architecture / Long-term Directions）
        ↓
路线图 / 阶段（Roadmap / Phase）
        ↓
契约 / 规范 / 配置规范（Contract / Specification / Profile）
        ↓
Issue / PR / 实现（Implementation）
```

发生冲突时，不要机械按文件名判断。先判断它们是否属于同一层，再检查文档状态（Document Status）、更新时间、Git 历史、`PROJECT_STATE.md` 和明确的项目所有者决策（Owner Decision）。

高层设计改变需要人类项目所有者 / 维护者（Human Owner / Maintainer）授权；低层实现不得静默改写高层使命。

## 8. Living Document 路径与版本规则

对于持续维护的正式文档：

- 文件路径保持稳定，不携带内容版本号；
- 版本历史由 Git commit / tag / release / provenance 留痕承担；
- `draft`、`historical`、`superseded` 等生命周期状态可保留，因为它们不是版本号；
- Schema、协议版本、标准编号、兼容契约和历史实验制品可继续在文件名中携带版本或日期；
- 若需要引用一个不可变历史版本，应引用 commit SHA、tag、release 或 `03_Evolution` 中的历史制品，而不是复制新的 `-v2` Living Document。

## 9. 清理政策（Cleanup Policy）

为了避免再次出现“总体设计散落后丢失”的问题：

- 不再为每次聊天 / 阶段创建大量检查点（Checkpoint）文档；
- 一个长期方向优先维护一个明确、持久的正式文档（Durable Artifact）；
- 被新总体设计替代的旧文件优先标记为历史 / 已取代（Historical / Superseded），而不是直接删除历史；
- 真正临时、重复且没有独立历史价值的文件再进入清理；
- 删除具有历史设计价值的文档属于高影响清理，应先确认替代关系和 Git 可恢复性。

本目录原创说明文档默认采用 **Creative Commons Attribution 4.0 International（CC BY 4.0）**，除非文件另有说明。
