# InteropAtlas Foundation First Phase v0.1

> 状态：Working Plan / 暂定阶段计划
>
> 目的：纠正“基础规范尚未形成，却过早推进具体网站实现”的路线偏移。当前阶段先定义项目怎样组织知识、怎样设计人类界面、怎样让人类与 AI / Agent 协作、怎样组织仓库与贡献流程；Reference Implementation（网站、自动化交互等）在这些基础达到最小可用后再继续。

## 1. 当前判断

InteropAtlas 已经有可工作的数据、Graph、Renderer 和 GitHub Pages，也已经形成若干 Human Interface 与 Open Collaboration 研究材料。

但当前存在明显的不对称：

- Human Interface 已经有 `IA-HI v0.1` 草案，却仍是一个较大的综合文件，Information Architecture、Information Presentation、Interaction、Visual、Accessibility、Conformance 等子规范尚未形成清晰模块与完成门槛；
- 设计 Prior Art 中大量 Method / Guideline / Heuristic / Design System 仍缺少合适的 Atlas 对象模型；
- Open Collaboration 只有 Prior Art 与 Working Notes，尚未形成可审计的 AI / Human Collaboration Profile；
- CONTRIBUTING 仍主要描述数据贡献，没有统一的“找任务 → 接手 → 工作 → PR → 独立 Review”流程；
- 仓库根目录仍是历史演进结果，尚未经过面向开放贡献者、Agent、规范产物和 Canonical Data 的结构审计；
- `.github/` 当前只有 workflows，尚未建立 issue / PR templates、CODEOWNERS 等协作结构；
- 当前没有仓库级 AGENTS.md，但在协作规范完成前也不应直接添加；
- 网站 Object Page 已开始按照 IA-HI 草案改造，说明 Reference Implementation 的推进速度已经超过底层 Specification / Collaboration / Repository Architecture。

因此当前阶段改为：

> **Foundation First：先建立规范与项目运行结构，再继续实现。**

## 2. 当前四个基础工作包

### F1 — Repository Structure & Artifact Taxonomy

先回答：**这个开源仓库本身应该怎样被人、Agent 和工具理解？**

需要形成一个暂定 Repository Structure Profile，至少定义：

- Root 层只放哪些“项目入口 / 社区健康 / 法务”文件；
- Canonical Data、Schemas、Engine、Tests、Tools、Specifications、Methodology、Research、Experiments、Governance、Examples 分别放在哪里；
- `docs/` 是否继续作为所有文档的单一平铺目录；
- Standard / Specification / Methodology / Research Note / Experiment / Decision / Plan 的文件身份与生命周期；
- 哪些内容属于项目本体，哪些属于 Agent 工作说明；
- 是否保留 `standards/`、`capabilities/` 等对象目录在根目录，还是统一进入 `data/`；
- 迁移路径与兼容策略。

原则：

> **仓库首先应像一个开放标准地图项目，而不是某个 Agent 的工作目录。**

在规范形成前，不大规模移动目录。

Prior Art 优先：GitHub community health conventions、OpenSSF、REUSE、成熟开放规范仓库、Diátaxis / docs-as-code、IETF / W3C 规范项目结构等。

### F2 — Human Interface Standards Package

先回答：**IA 面向人的信息到底应该怎样组织、传递和交互？**

当前 `IA-HI v0.1` 保留为综合草案，但下一阶段需要把它拆成可审计的模块或 Profile：

1. Information Architecture Profile
   - 用户任务；
   - Entry Points；
   - 信息分类 / 命名 / 关系；
   - Resource Page / Index / Search / Map 的职责；
   - 不把导航树当成知识模型本体。

2. Information Presentation Profile
   - Summary / Context / Facts / Relationships / Evidence / Machine View 的信息顺序；
   - 信息密度；
   - 渐进披露；
   - 标签与术语；
   - 表格 / 列表 / 图 / 文本分别何时使用。

3. Interaction Profile
   - Link / Button；
   - selection / filter / expand / recenter；
   - navigation state / history；
   - keyboard contract；
   - predictable behavior / recoverability。

4. Visual Presentation Profile
   - hierarchy；
   - grouping；
   - typography / spacing；
   - semantic color / status / relation encoding；
   - light / dark equivalence；
   - Design Tokens。

5. Accessibility / Conformance Profile
   - WCAG target；
   - semantic HTML；
   - ARIA 使用边界；
   - browser E2E；
   - automated / manual conformance checks。

每个模块必须记录：
- 用户任务；
- 上游标准与 Prior Art；
- Adopt / Profile / Extend / Invent；
- BCP 14 Requirements；
- 可验证验收方法。

在这套 Package 达到最小 Draft coverage 之前，不继续增加网站功能。

### F3 — Open Collaboration / Human–AI Collaboration Profile

先回答：**这个开放项目怎样让人类和 AI / Agent 使用同一套可理解、可监督的协作流程？**

当前 Prior Art 已有：
- ISO/IEC Human-Machine Teaming；
- ISO/IEC 5339；
- NIST AI RMF；
- Linux Foundation AAIF / AGENTS.md；
- GitHub Issue / PR / Review / Coding Agent；
- Open Collaboration V0 Notes。

下一阶段不是先开发 Lease Server，而是形成 `IA Open Collaboration Profile v0.1`，至少定义：

1. Participant Roles
   - Contributor / Executor；
   - Reviewer / Overseer；
   - Maintainer / Approver；
   - Automation Infrastructure；
   - Human / Agent 可以承担哪些角色、哪些组合需要限制。

2. Task Lifecycle
   - Available / Ready；
   - Claimed / Assigned；
   - In Progress；
   - Blocked / Handoff；
   - Review；
   - Done / Released。

3. Claim / Lease Semantics
   - “租赁式认领”首先定义语义，而不是先开发服务；
   - 当前 GitHub Assignee + activity / stale 能表达多少；
   - 什么时候需要 timeout / release / heartbeat。

4. Review / Oversight / Authorization
   - 执行者与 Reviewer 默认分离；
   - AI 生成内容如何标识；
   - 什么改变需要 Maintainer / Human 最终授权；
   - CODEOWNERS / Required Review 如何映射。

5. Handoff / Continuity
   - 人 ↔ Agent；
   - Agent ↔ Agent；
   - 任务上下文如何公开保存；
   - 不能依赖某个聊天窗口的隐式记忆。

6. Repository Agent Instructions
   - AGENTS.md 的职责；
   - 与 README / CONTRIBUTING / Specification 的边界；
   - 不绑定单一 Agent 产品。

Profile 完成后，再把规则投影到 GitHub Issues / Projects / PR / Review / AGENTS.md。

### F4 — Curation / Evidence / Machine Correctness

Human Interface 与 Collaboration 不是唯一基础。Canonical Data 的可信建设还需要并行补：

- Curation / Contribution minimum workflow；
- Evidence / Provenance minimum model；
- Validator / Schema correctness；
- Query correctness + regression tests；
- Reference / relation integrity。

这条线继续并行，但不把新网站功能作为验证它们的唯一方式。

## 3. Reference Implementation 的新定位

当前 GitHub Pages、Renderer、Local Map、Engine Bootstrap 都保留，但角色改变为：

> **Reference Implementation / Test Bed（参考实现 / 试验场）**

它们用于验证 Specification 是否可实现、是否存在缺口，不再决定 Specification 应该是什么。

因此：

- 已完成且符合上游规范的语义修正无需回滚；
- #17 Object Page Shell 暂停继续扩展；
- #13 Browser E2E 保留，但在 Interaction / Conformance Profile 更清楚后继续；
- 新 UI、首页重构、Local Map 功能、Visual Tokens 实现暂缓。

## 4. Foundation Gate

只有满足以下最小条件后，Human-readable Website 才恢复为 P0 实现工作：

### Gate A — Repository Structure
- Repository Structure Profile v0.1 已形成；
- Artifact taxonomy / lifecycle 可解释；
- 是否迁移目录已有明确 Decision；
- CONTRIBUTING / community files 的目标结构已定义。

### Gate B — Human Interface
- Information Architecture Draft；
- Information Presentation Draft；
- Interaction Draft；
- Visual Presentation Draft；
- Accessibility / Conformance Draft；
- 各模块有上游依据与最小 Requirement IDs。

### Gate C — Open Collaboration
- Open Collaboration Profile v0.1 已形成；
- participant roles / task lifecycle / review / handoff / claim semantics 明确；
- GitHub-native mapping 明确；
- AGENTS.md 的职责与边界明确。

Gate 不要求这些文档已经成为成熟 Standard，但要求它们已经足够指导实现，而不是由实现反向临时决定规则。

## 5. 当前执行顺序

```text
F1 Repository Structure / Artifact Taxonomy
        ↓
F2 Human Interface Standards Package
        ↓
F3 Open Collaboration / Human–AI Profile
        ↘
         同时与 F4 Curation / Evidence / Validator 互相校验
        ↓
Foundation Gate Review
        ↓
Reference Implementation resumes
```

F1 / F2 / F3 可以部分并行研究，但物理仓库迁移和具体 UI 实现都应等待相应规范先形成。

## 6. 采用原则

继续遵守：

> **Reuse Before Invent**
>
> **Adopt → Profile → Extend → Invent**

仓库结构和 AI 协作也属于互操作问题，因此同样必须先研究成熟方案，而不是把它们当成“项目内部随便约定的小事”。
