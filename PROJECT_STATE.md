# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-24T23:39:00+08:00
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
> 第一次认识项目先读 [`README.md`](README.md)；准备参与、判断当前方向或寻找下一项工作时，从本文件进入。不要从完整 Issue backlog 开始。

## 1. 我们在做什么

InteropAtlas 研究互操作，并持续连接、整理和验证人类已经形成的互操作知识，逐步映射完整的 **互操作方案空间（Interoperability Solution Space）**。

最终目标是形成开放、机器可读、持续演化、能够被 Human 与 Agent 使用的 **互操作公共知识基础设施**。

项目同时把自身作为互操作实践场：持续探索不同视图、表达形式、Human / Agent 接口和机器可读形式之间的转换与协同。

需要理解项目边界时进入 [`项目定义与范围`](docs/01_Foundation/01_Definition/interopatlas-definition-and-scope.zh-CN.md)；需要理解长期设计时进入 [`总体设计（Master Design）`](docs/01_Foundation/01_Definition/interopatlas-master-design.zh-CN.md)。

## 2. 当前运行方向

当前建设保持三条长期并行方向，并与仓库的 `01_State / 02_Runtime / 03_Evolution` 三块形成直接对应：

```text
知识积累
  +
知识视角建设
  +
系统运维与自我进化
```

### 知识积累

持续发现、收录、验证和连接标准、协议、方法、实现、组织、能力、场景、关系、证据与开放缺口，让 IA 的知识地图不断增长并保持可追溯、可验证。

仓库中的 `01_State` 主要承载这一方向形成的当前知识状态，包括对象、关系与待处理的 Inbox / Candidate。

### 知识视角建设

建设不同主体调用和呈现同一知识世界的方式。

当前重点包括：

- **适人化视角**：建设适合人类阅读、理解、比较和使用知识的呈现方式；Wiki 是最基础的视角，后续可继续增加时间线、关系图、比较、地图等不同表达。
- **适 Agent 化视角**：建设适合 Agent 使用的结构化读取、查询、遍历、验证和操作能力。

两类视角共享同一个 Canonical knowledge world，不各自建立事实源。仓库中的 `02_Runtime` 主要承载让这些视角真正运行起来的 Engine、Tools 与 Outputs。

### 系统运维与自我进化

负责 IA 自身的持续运行、维护、治理、质量控制和演化，包括仓库与自动化维护、数据质量、Freshness / Revalidation、规则修正、研究、实验与决策沉淀。

这一方向不仅保证系统能够长期运行，也负责通过真实问题、失败和反馈不断发现并修正 IA 自身。仓库中的 `03_Evolution` 主要承载 Research、Experiments 与 Decisions。

Agent structured access、Candidate Write 等高影响能力仍需 Human Owner 明确授权后才能进入施工。

## 3. 当前工作与长期候选如何区分

仓库当前存在较大的历史 backlog。**开放 Issue 不等于当前优先任务。**

当前优先关注的是：

1. **正在运行的 intake / coverage 工作**：例如 Candidate Pool、#146 及其仍在推进的具体收录 PR；
2. **当前仍有真实活动的研究线**：例如 #433 多 Agent / 多模型互操作研究；
3. **需要明确收口的进行中工作**：例如仍开放的 PR #431、#432，以及单独管理的 Naming PR #416。

其余大量 P6 长期 Issue、长期循环、未来能力和研究命题，当前统一视为 **长期候选 / backlog**。只有在被明确重新激活、获得具体 Work Unit 和完成边界后，才视为当前工作。

> **规则：不要因为 Issue 是 open 就自动执行。先确认它是否属于当前激活工作。**

## 4. 我可以从哪里参与

| 我想做什么 | 去哪里 |
| --- | --- |
| **发现地图空缺、补充新的标准 / 协议 / 方法 / 实现** | 从 [`Candidate Pool`](01_State/Inbox/candidates/) 查看候选与覆盖情况，再进入与当前激活 intake 相关的 Issue / PR |
| **审核 Candidate，判断能否进入 Canonical** | 从 [`Inbox`](01_State/Inbox/) 查看待处理材料，并按 [`知识系统规范`](docs/02_System/01_Knowledge/) 审查 |
| **改善 Human 阅读、浏览、比较与 Workspace** | 从 [`Human Interface`](docs/02_System/02_Interface/) 理解现有设计，再确认是否存在当前激活 Work Item |
| **改善机器可读、查询、验证与 Agent 能力** | 从 [`Runtime`](02_Runtime/) 与 [`System`](docs/02_System/) 进入；高影响能力仍遵守 Owner Gate |
| **研究项目大方向、提出新的能力或路线** | 使用 Research Issue 承载尚未收敛的问题与方案探索；形成明确交付边界后，再拆出或转成具体 Work Issue |
| **领取明确任务** | 从明确标记为当前激活的 Issue / PR 进入，不从完整 backlog 随机挑选 |
| **查看长期候选与历史规划** | GitHub Issues / Projects；它们是候选与组织视图，不等于当前执行队列 |

### 如果我的想法还不是一个任务

当前优先按以下方式分流：

```text
尚未收敛的问题 / 方向 / 方案讨论
→ Research Issue

已经明确、有完成边界的工作
→ Issue / PR

多个 Work Item 的长期组织与进度
→ Project

已经稳定、长期有效的规则 / 设计 / 知识
→ Repository
```

私人聊天不是项目状态源。如果 Human / Agent 对话产生会影响后续工作的稳定结论，应在结束前进入上述公共持久位置。

---

**最短参与路径：** `README → PROJECT_STATE → Research Issue / Work Issue → Repository`；Project 负责组织多个事项，不作为第二事实源。

本文件只在项目方向、当前运行边界、稳定参与入口或重大授权边界发生变化时更新；普通任务进度不要求同步修改本文件。
