# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-05T19:00:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> **这是参与 InteropAtlas 建设的统一入口。**
>
> 第一次认识项目先读 [`README.md`](README.md)；准备参与、判断当前方向或寻找下一项工作时，从本文件进入。这里不复制完整任务列表，而只保存长期稳定的方向和导航入口。

## 1. 我们要去哪里

InteropAtlas 是一张关于“人类已经如何解决互操作问题”的开放知识地图，并逐步建设成为面向全人类、开放、机器可读、可持续分析与演化的 **互操作方案空间（Interoperability Solution Space）公共知识基础设施**。

长期坚持：

> **知识属于公共共同体，视角属于个人。**

Human 与 Agent 使用同一个可验证、可追溯的公共知识世界，通过不同的选择、视角、投影和工作空间完成发现、比较、验证、组合、使用与贡献。

需要理解项目边界时进入 [`项目定义与范围`](docs/01_Foundation/01_Definition/interopatlas-definition-and-scope.zh-CN.md)；需要理解长期设计时进入 [`总体设计（Master Design）`](docs/01_Foundation/01_Definition/interopatlas-master-design.zh-CN.md)；需要展开长期能力方向时进入 [`长期路线`](docs/01_Foundation/03_Direction/interopatlas-long-term-roadmap.zh-CN.md)。这些是深入材料，不是参与项目的前置必读。

## 2. 我们现在在建设什么

当前建设不是固定阶段流水线，而是三条共享同一知识底座、长期并行的方向：

```text
知识地图持续成长
        +
可运行的知识基础设施
        +
Human / Agent 真实使用与反馈
```

### 知识地图持续成长

持续发现标准、协议、方法、实现、组织、能力、场景、关系、证据与开放缺口；让 Candidate 经过 identity / dedup、验证、语义审查与明确接受边界后进入 Canonical Knowledge。

### 可运行的知识基础设施

持续完善知识模型、Relation、Evidence、Provenance、Lifecycle、查询、验证、迁移、Coverage / Freshness / Revalidation 等能力。真实数据和真实使用负责暴露模型缺口，再决定底层怎样演化。

### Human / Agent 真实使用与反馈

Human 侧持续改善浏览、理解、比较、证据检查与 Workspace；Machine / Agent 侧持续改善结构化读取、查询、遍历、验证和自动化。两条使用路线共享同一个 Canonical knowledge world，不各自建立事实源。

Agent structured access + Candidate Write 等高影响能力仍需 Human Owner 明确授权后才能进入施工。

## 3. 我可以从哪里参与

不要从完整 Issue backlog 开始。先选择自己想参与的工作类型，再进入对应的稳定入口寻找当前 Work Item。

| 我想做什么 | 去哪里 |
| --- | --- |
| **发现地图空缺、补充新的标准 / 协议 / 方法 / 实现** | 从 [`Candidate Pool`](01_State/Inbox/candidates/) 查看候选与覆盖情况，再从 [当前开放 Issues](https://github.com/InteropAtlas/InteropAtlas/issues?q=is%3Aissue%20state%3Aopen) 查找可执行的 intake / coverage 工作 |
| **审核 Candidate，判断对象 / 关系 / 证据能否进入 Canonical** | 从 [`Inbox`](01_State/Inbox/) 查看待处理材料，并按 [`知识系统规范`](docs/02_System/01_Knowledge/) 进行 identity、evidence、relation 与 acceptance 审查 |
| **改善 Human 阅读、浏览、比较与 Workspace** | 从 [`Human Interface`](docs/02_System/02_Interface/) 理解现有设计，再到 [开放 Issues](https://github.com/InteropAtlas/InteropAtlas/issues?q=is%3Aissue%20state%3Aopen) 寻找当前 Human-facing 工作 |
| **改善机器可读、查询、验证与 Agent 能力** | 从 [`Runtime`](02_Runtime/) 和 [`System`](docs/02_System/) 理解当前能力，再到 [开放 Issues](https://github.com/InteropAtlas/InteropAtlas/issues?q=is%3Aissue%20state%3Aopen) 寻找当前 Machine / Agent 工作；高影响能力仍遵守 Owner Gate |
| **研究项目大方向、提出新的能力或路线** | 先参考 [`长期路线`](docs/01_Foundation/03_Direction/interopatlas-long-term-roadmap.zh-CN.md)；尚未收敛的问题进入 [GitHub Discussions](https://github.com/InteropAtlas/InteropAtlas/discussions)，形成明确交付边界后再成为 Issue |
| **领取一个已经明确的具体任务** | 进入 [GitHub Issues](https://github.com/InteropAtlas/InteropAtlas/issues)；Issue 是具体 Work Item 的执行事实源 |
| **查看多项工作的组织、优先级和进度** | 进入 [GitHub Projects](https://github.com/orgs/InteropAtlas/projects)；Project 负责组织和投影，不替代 Issue 中的执行上下文 |
| **维护仓库、自动化和长期卫生** | 进入 [`仓库长期维护 Project`](https://github.com/orgs/InteropAtlas/projects/4) |

### 如果我的想法还不是一个任务

项目允许自然语言讨论先于任务结构。不要因为一个讨论里出现很多想法，就机械创建几十个 Issue。

```text
尚未收敛的问题 / 方向 / 方案讨论
→ Discussion

已经明确、有完成边界的工作
→ Issue

多个 Work Item 的长期组织与进度
→ Project

已经稳定、长期有效的规则 / 设计 / 知识
→ Repository
```

私人聊天不是项目状态源。如果一轮 Human / Agent 对话产生了会影响后续工作的方向、问题或任务，在结束前应把它们分流到上述公开持久位置，而不是依赖参与者记住聊天内容。

---

**最短参与路径：** `README → PROJECT_STATE → 选择参与方向 → Discussion / Issue / Project / 对应资料`。

本文件只在项目使命、当前建设方向、稳定参与入口或重大授权边界发生变化时更新；具体 Issue 的增删、普通任务进度和日常维护不要求同步修改本文件。
