# InteropAtlas 正式文档入口

`docs/` 保存 **InteropAtlas 当前有效、需要被理解或遵守的项目文档**。

这里不再承担“所有 Markdown 都放进来”的职责。研究、实验和项目变更过程已经分别进入 `03_Evolution/`：

- [`03_Evolution/01_Research/`](../03_Evolution/01_Research/) — 为什么这样判断：研究、既有方案调查、审计、验证、参考依据；
- [`03_Evolution/02_Experiments/`](../03_Evolution/02_Experiments/) — 怎样试过：原型、实验、试运行、适配验证；
- [`03_Evolution/03_Change/`](../03_Evolution/03_Change/) — 接下来怎样改变：路线图、阶段计划、迁移、未来方向与历史工作笔记。

简单判断：

> 一个新的贡献者今天进入项目，为了正确理解或参与当前 InteropAtlas，是否应该阅读这份文件？
>
> 如果答案是“是”，它通常应该位于 `docs/`；如果主要记录研究、实验或变化过程，则进入 `03_Evolution/`。

## 建议从这里开始

- [`interopatlas-definition-and-scope-v0.2.zh-CN.md`](interopatlas-definition-and-scope-v0.2.zh-CN.md) — 当前项目定义、问题边界与收录范围。
- [`architecture-v0.1.zh-CN.md`](architecture-v0.1.zh-CN.md) — 当前总体架构。
- [`repository-structure-profile-v0.1.zh-CN.md`](repository-structure-profile-v0.1.zh-CN.md) — 仓库结构与“物理存储 ≠ 知识分类 ≠ 索引/视图”的结构规则。
- [`project-development-principles.zh-CN.md`](project-development-principles.zh-CN.md) — 当前项目建设原则与最小治理规则。
- [`five-route-operating-model.zh-CN.md`](five-route-operating-model.zh-CN.md) — Human、Machine、Curation、Trust、Governance 的当前协同模型。

## 当前规范、Profile 与政策

### 知识与数据模型

- [`knowledge-object-classification-specification-v0.1.zh-CN.md`](knowledge-object-classification-specification-v0.1.zh-CN.md) — 知识对象分类规范草案。
- [`flat-graph-and-dynamic-maps.zh-CN.md`](flat-graph-and-dynamic-maps.zh-CN.md) — Flat Objects + Rich Relations + Dynamic Maps 的建模原则。

### Human Interface

- [`human-interface-profiles-v0.1.zh-CN.md`](human-interface-profiles-v0.1.zh-CN.md) — Gate B Human Interface Standards Package 模块入口。
  - [`human-interface-information-architecture-profile-v0.1.zh-CN.md`](human-interface-information-architecture-profile-v0.1.zh-CN.md) — Information Architecture Draft Profile。
  - [`human-interface-information-presentation-profile-v0.1.zh-CN.md`](human-interface-information-presentation-profile-v0.1.zh-CN.md) — Information Presentation Draft Profile。
  - [`human-interface-interaction-profile-v0.1.zh-CN.md`](human-interface-interaction-profile-v0.1.zh-CN.md) — Interaction Draft Profile。
  - [`human-interface-visual-presentation-profile-v0.1.zh-CN.md`](human-interface-visual-presentation-profile-v0.1.zh-CN.md) — Visual Presentation Draft Profile。
  - [`human-interface-accessibility-conformance-profile-v0.1.zh-CN.md`](human-interface-accessibility-conformance-profile-v0.1.zh-CN.md) — Accessibility / Conformance Draft Profile。
- [`human-interface-specification-v0.1.zh-CN.md`](human-interface-specification-v0.1.zh-CN.md) — 当前综合规范草案；Gate B Audit 前继续作为 umbrella source 与既有 Requirement ID 来源。
- [`human-readable-interaction-baseline.zh-CN.md`](human-readable-interaction-baseline.zh-CN.md) — 当前人类可读交互基线。

相关研究依据已经迁入 [`03_Evolution/01_Research/`](../03_Evolution/01_Research/)，包括 Human Interface 外部标准基线、Reference Map、符合性审计、五 Profile consolidation audit 与参考依据入库审计。

### Open Collaboration / Human–AI 协作

- [`open-collaboration-profile-v0.1.zh-CN.md`](open-collaboration-profile-v0.1.zh-CN.md) — 当前开放协作 / Human–AI Collaboration Profile。
- [`collaboration-task-system-v0.1.zh-CN.md`](collaboration-task-system-v0.1.zh-CN.md) — 当前任务、认领、交接、Review 等运行规则。
- [`task-reference-seeding-profile-v0.1.zh-CN.md`](task-reference-seeding-profile-v0.1.zh-CN.md) — 任务发布时的参考依据预装规则。

相关 Prior Art、试运行审计和被正式 Profile 替代的早期工作笔记分别保存在 Research 与 Change 中。

### 项目政策与长期机制

- [`language-policy.zh-CN.md`](language-policy.zh-CN.md) — 当前语言政策。
- [`practice-feedback-loop.zh-CN.md`](practice-feedback-loop.zh-CN.md) — Atlas ↔ Runtime 的长期实践反馈机制。

## 架构与运行模型

- [`architecture-v0.1.zh-CN.md`](architecture-v0.1.zh-CN.md) — 总体架构。
- [`repository-structure-profile-v0.1.zh-CN.md`](repository-structure-profile-v0.1.zh-CN.md) — 仓库结构 Profile。
- [`five-route-operating-model.zh-CN.md`](five-route-operating-model.zh-CN.md) — 五路线协同模型。
- [`flat-graph-and-dynamic-maps.zh-CN.md`](flat-graph-and-dynamic-maps.zh-CN.md) — 图模型与动态视图原则。

## Evolution：研究、实验与变更历史

当前项目的过程材料不再混放在 `docs/`：

```text
03_Evolution/
├── 01_Research/      研究、Prior Art、Audit、Verification
├── 02_Experiments/   Prototype、Experiment、Dry Run、结果
└── 03_Change/        Roadmap、Route、Proposal、Migration、Future Direction
```

具体索引见：

- [`Research README`](../03_Evolution/01_Research/README.md)
- [`Experiments README`](../03_Evolution/02_Experiments/README.md)
- [`Change README`](../03_Evolution/03_Change/README.md)

## 文档状态

除非文件明确标注为已冻结或正式发布，否则当前 Specification / Profile / Architecture 仍可根据真实实践演化。

但“可以演化”不代表“研究过程和当前规则混为一谈”：

- 当前有效规则应留在 `docs/`；
- 形成规则的依据和审计进入 Research；
- 尝试与验证进入 Experiments；
- 下一步变化与历史迁移进入 Change。

本目录中的原创说明文档默认使用 **CC BY 4.0**，除非文件另有说明。
