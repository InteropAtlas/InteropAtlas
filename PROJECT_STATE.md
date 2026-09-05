# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-05T18:45:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> Status: Living Project Checkpoint（持续更新的项目断点）
>
> Purpose: 这是 Human Owner 与新 Agent 查看“现在主线是什么、做到哪里、从哪里继续”的首要入口。历史阶段编号、旧建设周期和已经完成的迁移过程不再占据 Owner View。

## 1. 项目长期目标

InteropAtlas 是一个面向全人类的、开放、机器可读、可持续分析与演化的 **互操作方案空间（Interoperability Solution Space）公共知识基础设施**。

长期系统坚持：

> **知识属于公共共同体，视角属于个人。**

核心知识世界保持公共、可验证、可追溯；Human 与 Agent 在同一知识世界上，通过选择（Selection）、视角（Perspective）、投影（Projection）和工作空间（Workspace）完成发现、比较、验证、组合、使用与贡献。

## 2. Owner View：当前主线

当前主线只保留三个需要长期并行推进的方向：

```text
知识地图持续成长
    +
可运行的知识基础设施
    +
Human / Agent 真实使用与反馈
```

### 知识地图持续成长

持续发现和收录标准、协议、方法、实现、组织、能力、场景、关系、证据与开放缺口。Candidate Pool 是入口；Candidate 不等于 Canonical；普通收录必须经过 identity / dedup、验证、语义审查和明确接受边界。

当前已具备可运行的持续收录链路，具体执行入口见当前 Intake Work Item。

### 可运行的知识基础设施

继续把已经形成的知识模型、来源追踪、关系、生命周期、查询、验证、迁移和投影能力变成稳定的运行能力。实现应由真实数据和真实使用驱动，不再以一次性的阶段编号作为项目主线。

### Human / Agent 真实使用与反馈

Human 与 Agent 应逐步共享同一知识底座和可恢复的 Selection / Projection / Workspace 机制。Human 侧已经有 Compare / Evidence 的第一批真实切片；Agent 结构化读取、查询、遍历和 Candidate Write 仍属于高影响后续能力，未获得明确授权前不得自动启动。

## 3. 当前实际状态

已经具备：

- 共享 Canonical knowledge world 的基本结构；
- 稳定身份、Evidence / Provenance、Fact ≠ Assessment 等核心边界；
- Candidate → Validation → Review / Acceptance 的生产收录路径；
- Legacy → 当前知识结构的可回滚迁移实践；
- Human Compare / Evidence 对共享 Selection / Projection 合同的真实使用；
- GitHub-native 协作、维护和 Agent continuation 基础设施；
- Repository 当前结构：`01_State / 02_Runtime / 03_Evolution / docs`。

仍需持续推进：

- 扩大知识覆盖与方案空间覆盖；
- 用真实收录继续校验知识模型；
- 补齐 Relation / Evidence / Lifecycle 等现实数据迁移与表达；
- 扩展 Human Workspace；
- 在 Owner 明确授权后推进 Agent structured access + Candidate Write；
- 让 Coverage、Freshness、Revalidation、Open Gap 等维护能力逐步进入长期运行；
- 之后再由真实需求决定 Personal Knowledge Space、动态 Perspective、MATCH、Federation 等长期能力何时进入施工。

## 4. 当前执行入口

对 Human Owner：默认只看本文件，不需要记忆历史阶段编号或内部任务树。

对 Agent：

1. 先读 `AGENTS.md`；
2. 再读本文件；
3. 检查 main / Issue / PR 是否出现更新；
4. 进入当前处于 Ready / In Progress 的具体 Issue；
5. 不从历史阶段名称推断当前授权。

当前持续收录入口由现行 Continuous Intake Work Item 承担。

当前仓库长期维护由 Repository Maintenance Project 与其具体维护 Issue 承担；它是维护工作，不是产品主线。

Agent structured access 相关工作仍需 Owner 明确提升后才可执行。

## 5. 规划与命名规则

### 不再使用项目级版本号描述当前计划

InteropAtlas 的长期项目本身、总体路线、Living Documents 和当前主线不使用 `V1 / V2` 作为规划框架。Git 历史、提交、Issue、PR 和文档 provenance 负责记录演化。

版本号仍可用于现实中本来具有版本身份的对象、外部标准版本、兼容契约、Schema / Protocol 等必须明确版本边界的制品；这与“给整个项目计划编号”是两回事。

### 历史 P1–P6 不再作为现行路线

过去的 P1–P6 只作为历史建设周期留在 Git history / closed Issues / Evolution 记录中，不再作为 Owner View、长期 Roadmap 或新任务命名体系。

新 Work Item 使用 GitHub Issue Number 作为稳定身份，并以清晰任务标题、Status、Type、Priority、Workstream 表达当前意义，不再添加新的 `P1 / P2 / P6` 阶段前缀。

## 6. 长期路线的阅读方式

长期方向不是固定阶段流水线。当前使用四层关系理解：

```text
长期使命 / 产品哲学
        ↓
长期能力域
        ↓
当前主线
        ↓
可执行 Work Item
```

长期能力域见：`docs/01_Foundation/03_Direction/interopatlas-long-term-roadmap.zh-CN.md`。

只有真实需求、真实数据、真实使用和明确授权共同支持时，长期方向才进入当前施工。

## 7. Owner escalation boundary

以下事项仍需 Human Owner 明确判断：

- 项目定义、长期方向或 Scope 的实质变化；
- Public Canonical ↔ Personal State / privacy 边界；
- identity merge / split 或不可逆身份决策；
- destructive migration / major deletion；
- material security / permission boundary；
- stable specification / governance promotion；
- formal release 或其他重大不可逆决策；
- 仍处于 Draft / Future 的高影响能力被提升为当前工作。

普通技术实现、可机械验证的迁移、常规 intake 和维护工作不需要把内部细节持续呈现给 Owner。
