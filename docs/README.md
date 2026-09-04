# InteropAtlas 正式文档地图

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-08-30T17:51:02+08:00
Document Updated At: 2026-09-04T19:53:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

`docs/` 保存 **今天进入 InteropAtlas 时仍需要理解或遵守的长期文档**。

本索引按“设计尺度”组织，而不是按文件创建时间平铺。研究、实验和历史变更过程分别进入 `03_Evolution/01_Research`、`02_Experiments`、`03_Change`。

## 0. 第一次进入项目：先读什么

### Human / 项目理解

```text
README.md
→ interopatlas-master-design-v1.0.zh-CN.md
→ knowledge-philosophy-and-principles-v1.0.zh-CN.md
→ public-commons-and-personal-knowledge-space-v0.1.zh-CN.md
→ PROJECT_STATE.md
```

### Agent / Maintainer

```text
AGENTS.md
→ PROJECT_STATE.md
→ README.md
→ interopatlas-master-design-v1.0.zh-CN.md
→ current Phase / Issue / Contract
```

不要把某一份 Phase Plan、旧五路线模型、某个 Workspace 或某个 P6 Issue 当成整个 InteropAtlas。

## 1. L0–L1：使命、哲学与总设计

这些文件定义项目最高层方向。

- [`interopatlas-master-design-v1.0.zh-CN.md`](interopatlas-master-design-v1.0.zh-CN.md) — **当前 Master Design**。解释 Atlas-first、Shared / Personal / Experience、Knowledge Operation Space、Human+Agent、成长循环，以及 P1–P6 的正确位置。
- [`knowledge-philosophy-and-principles-v1.0.zh-CN.md`](knowledge-philosophy-and-principles-v1.0.zh-CN.md) — 长期产品哲学与不应被局部实现静默改写的原则。
- [`interopatlas-definition-and-scope-v0.2.zh-CN.md`](interopatlas-definition-and-scope-v0.2.zh-CN.md) — 项目定义、互操作问题边界和收录范围。

四条长期哲学：

> Knowledge belongs to the commons.  
> Perspective belongs to the individual.  
> Representation should adapt to cognition.  
> Personalization must remain reversible and transparent.

## 2. L2：知识空间与长期产品架构

- [`public-commons-and-personal-knowledge-space-v0.1.zh-CN.md`](public-commons-and-personal-knowledge-space-v0.1.zh-CN.md) — 公共知识共同体 + 个人知识空间；内容个性化、表达个性化、反信息茧房、隐私与可互操作个人空间。
- [`knowledge-workspace-design-principles-v1.0.zh-CN.md`](knowledge-workspace-design-principles-v1.0.zh-CN.md) — `Canonical → Perspective / Selection → Projection → Workspace` 设计基线，以及 Wiki/Browse、Timeline、Graph、Compare、Evidence 等 Workspace 原则。
- [`human-agent-access-architecture-v1-draft.zh-CN.md`](human-agent-access-architecture-v1-draft.zh-CN.md) — V1 Human / Agent access、权限和 Candidate Write 架构草案。
- [`flat-graph-and-dynamic-maps.zh-CN.md`](flat-graph-and-dynamic-maps.zh-CN.md) — Flat Objects + Rich Relations + Dynamic Maps 的建模原则。

`architecture-v0.1.zh-CN.md` 是 2026-09-02 总体设计升级之前的历史架构基线，**不再作为当前 Master Architecture 入口**。保留它用于理解演化历史；当前方向以 Master Design + V1 architecture drafts 为准。

## 3. L3：成长、运行与演化机制

- [`practice-feedback-loop.zh-CN.md`](practice-feedback-loop.zh-CN.md) — Atlas ↔ Runtime / practice 的反馈机制。
- [`project-development-principles.zh-CN.md`](project-development-principles.zh-CN.md) — 项目建设原则与最小治理规则。
- [`five-route-operating-model.zh-CN.md`](five-route-operating-model.zh-CN.md) — **历史/局部 operating model**：Human、Machine、Curation、Trust、Governance。它仍可作为协作/运行参考，但不再代表项目总设计或总 Roadmap。

长期成长循环见 Master Design：

```text
KNOW → USE → DISCOVER → CONTRIBUTE → KNOW
                         +
                       MATCH
```

## 4. L4：Roadmap 与当前 Foundation Cycle

- [`interopatlas-long-term-roadmap-v1.0.zh-CN.md`](interopatlas-long-term-roadmap-v1.0.zh-CN.md) — **当前长期 Roadmap**；明确 P1–P6 只是第一轮 V1 Foundation / Architecture Revalidation Cycle。
- [`../PROJECT_STATE.md`](../PROJECT_STATE.md) — 当前项目断点、当前 Phase、Resume Here 和 Gate。
- 当前/历史 Phase Plan、Migration Plan、Transition materials 位于 [`../03_Evolution/03_Change/`](../03_Evolution/03_Change/)。

实时施工状态始终以 `PROJECT_STATE.md` + GitHub Issues / PRs + newer Git evidence 为准。

## 5. L5：V1 Contracts / Specifications / Profiles

### Canonical / Intake / Migration

- [`canonical-contract-v1-architecture-draft.zh-CN.md`](canonical-contract-v1-architecture-draft.zh-CN.md)
- [`canonical-write-intake-contract-v1-architecture-draft.zh-CN.md`](canonical-write-intake-contract-v1-architecture-draft.zh-CN.md)
- [`canonical-migration-architecture-v1-draft.zh-CN.md`](canonical-migration-architecture-v1-draft.zh-CN.md)
- [`knowledge-object-classification-specification-v0.1.zh-CN.md`](knowledge-object-classification-specification-v0.1.zh-CN.md)

### Human Interface

- [`human-interface-profiles-v0.1.zh-CN.md`](human-interface-profiles-v0.1.zh-CN.md) — Human Interface Profile umbrella。
- `human-interface-information-architecture-profile-v0.1.zh-CN.md`
- `human-interface-information-presentation-profile-v0.1.zh-CN.md`
- `human-interface-interaction-profile-v0.1.zh-CN.md`
- `human-interface-visual-presentation-profile-v0.1.zh-CN.md`
- [`human-interface-accessibility-conformance-profile-v0.1.zh-CN.md`](human-interface-accessibility-conformance-profile-v0.1.zh-CN.md)
- [`human-interface-specification-v0.1.zh-CN.md`](human-interface-specification-v0.1.zh-CN.md)
- [`human-readable-interaction-baseline.zh-CN.md`](human-readable-interaction-baseline.zh-CN.md)

### Open Collaboration / Human–AI

- [`open-collaboration-profile-v0.1.zh-CN.md`](open-collaboration-profile-v0.1.zh-CN.md)
- [`collaboration-task-system-v0.1.zh-CN.md`](collaboration-task-system-v0.1.zh-CN.md)
- [`task-reference-seeding-profile-v0.1.zh-CN.md`](task-reference-seeding-profile-v0.1.zh-CN.md)
- [`agent-onboarding-context-continuity-profile-v0.1.zh-CN.md`](agent-onboarding-context-continuity-profile-v0.1.zh-CN.md)
- [`agent-attribution-contribution-identity-profile-v0.1.zh-CN.md`](agent-attribution-contribution-identity-profile-v0.1.zh-CN.md)
- [`agent-continuation-bridge-v0.1.zh-CN.md`](agent-continuation-bridge-v0.1.zh-CN.md)

### Repository / policy

- [`repository-structure-profile-v0.1.zh-CN.md`](repository-structure-profile-v0.1.zh-CN.md)
- [`language-policy.zh-CN.md`](language-policy.zh-CN.md)

## 6. Evolution：过程材料放哪里

```text
03_Evolution/
├── 01_Research/      Prior Art / Research / Audit / Verification
├── 02_Experiments/   Prototype / Experiment / Dry Run
└── 03_Change/        Roadmap history / Phase Plan / Proposal / Migration
```

- [`Research README`](../03_Evolution/01_Research/README.md)
- [`Experiments README`](../03_Evolution/02_Experiments/README.md)
- [`Change README`](../03_Evolution/03_Change/README.md)

研究结论不能因为“很有启发”就自动成为稳定架构；历史 Change 文件也不能因为仍在仓库里就被当成当前路线。

## 7. 文档层级规则

```text
Mission / Philosophy
        ↓
Master Design
        ↓
Architecture / Long-term Directions
        ↓
Roadmap / Phase
        ↓
Contract / Specification / Profile
        ↓
Issue / PR / Implementation
```

冲突时不要机械按文件名判断。先判断它们是否属于同一层，再检查 Document Status、更新时间、Git history、`PROJECT_STATE.md` 和明确的 Owner decision。

高层设计改变需要 Human Owner / Maintainer 授权；低层实现不得静默改写高层使命。

## 8. Cleanup policy

为了避免再次出现“总设计散落后丢失”的问题：

- 不再为每次聊天/阶段创建大量 checkpoint 文档；
- 一个长期方向优先维护一个明确的 durable artifact；
- 被新总设计替代的旧文件优先标记为 historical / superseded，而不是直接删除历史；
- 真正临时、重复且没有独立历史价值的文件再进入清理；
- 删除具有历史设计价值的文档属于高影响清理，应先确认替代关系和 Git 可恢复性。

本目录原创说明文档默认 CC BY 4.0，除非文件另有说明。
