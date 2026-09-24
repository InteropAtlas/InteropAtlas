# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-24T23:59:00+08:00
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
知识视角与访问建设
  +
系统运维与自我进化
```

### 知识积累

持续发现、收录、验证和连接标准、协议、方法、实现、组织、能力、场景、关系、证据与开放缺口，让 IA 的知识地图不断增长并保持可追溯、可验证。

仓库中的 `01_State` 主要承载这一方向形成的当前知识状态，包括对象、关系与待处理的 Inbox / Candidate。

### 知识视角与访问建设

建设同一知识世界的不同呈现方式与访问方式。

当前重点包括：

- **适人化呈现**：建设适合人类阅读、理解、比较和使用知识的呈现方式；Wiki 是最基础的形式，后续可继续增加时间线、关系图、比较、地图等不同表达。
- **机器可读访问**：建设结构化读取、查询、遍历、验证和操作能力，使软件、Agent 与其他机器系统能够直接调用同一知识底座。

两类方式共享同一个 Canonical knowledge world，不各自建立事实源。仓库中的 `02_Runtime` 主要承载让这些呈现与访问能力真正运行起来的 Engine、Tools 与 Outputs。

### 系统运维与自我进化

负责 IA 自身的持续运行、维护、治理、质量控制和演化，包括仓库与自动化维护、数据质量、Freshness / Revalidation、规则修正、研究、实验与决策沉淀。

这一方向不仅保证系统能够长期运行，也负责通过真实问题、失败和反馈不断发现并修正 IA 自身。仓库中的 `03_Evolution` 主要承载 Research、Experiments 与 Decisions。

Agent structured access、Candidate Write 等高影响能力仍需 Human Owner 明确授权后才能进入施工。

## 3. 当前任务如何进入注意力

仓库可以存在大量 Open Issues，但 **Open 不等于当前要做**。

当前只使用两个注意力状态：

- **Focus**：当前真正推进、需要占用注意力的任务；
- **Inbox**：其余所有仍值得保留、但当前不占用注意力的任务。

任务在需要时从 Inbox 提取到 Focus；完成后关闭。Focus 任务也可以在暂时不值得继续投入时退回 Inbox。

Issue 的任务类型直接对应上面的三条运行方向：

- **知识积累**
- **知识视角与访问建设**
- **系统运维与自我进化**

Waiting 只在任务确实存在等待条件时附加，不形成新的任务空间。

详细规则见 [`GitHub Issue 运行治理`](docs/03_Operation/02_Governance/github-issue-governance.zh-CN.md)。

## 4. 我可以从哪里参与

| 我想做什么 | 去哪里 |
| --- | --- |
| **发现地图空缺、补充新的标准 / 协议 / 方法 / 实现** | 从 [`Candidate Pool`](01_State/Inbox/candidates/) 查看候选与覆盖情况，再进入与当前激活 intake 相关的 Issue / PR |
| **审核 Candidate，判断能否进入 Canonical** | 从 [`Inbox`](01_State/Inbox/) 查看待处理材料，并按 [`知识系统规范`](docs/02_System/01_Knowledge/) 审查 |
| **改善 Human 阅读、浏览、比较与 Workspace** | 从 [`Human Interface`](docs/02_System/02_Interface/) 理解现有设计，再确认是否存在当前激活 Work Item |
| **改善机器可读、查询、验证与 Agent 能力** | 从 [`Runtime`](02_Runtime/) 与 [`System`](docs/02_System/) 进入；高影响能力仍遵守 Owner Gate |
| **研究项目大方向、提出新的能力或路线** | 先形成一个可继续推进的具体任务，再创建 Issue；研究可以发生在任何任务中 |
| **领取当前任务** | 从 Focus 中进入 |
| **查看其余待办** | 从 Inbox 中选择；需要时再提取到 Focus |

### 如果我的想法还不是一个任务

还没有形成可推进任务的想法、方向或材料，不要求机械创建 Issue。可以先进入合适的仓库文档、Candidate / Inbox 或其他持久位置；当它形成明确任务后，再创建 Issue。

多个 Work Item 的组织使用 GitHub Project；稳定、长期有效的规则 / 设计 / 知识进入 Repository。

私人聊天不是项目状态源。如果 Human / Agent 对话产生会影响后续工作的稳定结论，应在结束前进入公共持久位置。

---

**最短参与路径：** `README → PROJECT_STATE → Focus / Inbox Issue → Repository`；Project 负责组织多个事项，不作为第二事实源。

本文件只在项目方向、当前运行边界、稳定参与入口或重大授权边界发生变化时更新；普通任务进度不要求同步修改本文件。
