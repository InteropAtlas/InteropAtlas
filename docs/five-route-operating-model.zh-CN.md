# InteropAtlas 五路线协同模型（暂定参考）

> 状态：Provisional Reference（暂定参考）。用于组织当前建设工作，不代表冻结架构。

InteropAtlas 不应被理解成“一个数据仓库 + 一个网站”。随着实践展开，当前更合适的整体模型是：两条核心使用路线，加三条横向支撑路线。

## 五条路线

### 1. Human Route（人类可读路线）

回答：**人如何发现、理解、探索并使用 InteropAtlas？**

阶段：

`Visible → Readable → Navigable → Connected → Mappable → Explorable → Understandable → Actionable`

即：

看得到 → 看得懂 → 找得到 → 看懂关系 → 形成地图 → 可探索 → 理解方案空间 → 辅助行动与决策。

详细路线见 `human-readable-route.zh-CN.md`。

### 2. Machine Route（机器可用 / 可维护路线）

回答：**机器如何稳定读取、验证、解析、查询、分析和维护 InteropAtlas？**

阶段：

`Loadable → Validatable → Resolvable → Graphable → Queryable → Analyzable → Maintainable → Observable → Evolvable → Interoperable`

详细路线见 `machine-readable-maintainable-route.zh-CN.md`。

### 3. Curation / Contribution Route（收录与贡献路线）

回答：**一条知识、一个标准、一个实现或一条关系如何进入 Atlas？**

暂定流程：

```text
发现候选
  ↓
Prior Art / 来源调查
  ↓
识别对象性质与边界
  ↓
建模
  ↓
收集 Evidence / Source
  ↓
建立关系
  ↓
Validator / Resolver
  ↓
Review
  ↓
Merge / Publish
  ↓
后续更新与监控
```

这条路线决定 Atlas 如何生长。未来需要逐步明确收录门槛、最小证据要求、去重、版本更新和贡献流程。

### 4. Evidence / Provenance / Trust Route（证据、溯源与可信路线）

回答：**为什么相信 Atlas 中的一个事实或判断？**

长期需要把事实与其来源连接起来：

```text
Claim / Fact
   ↓
Evidence
   ↓
Source
   ↓
retrieved_at / version / context
   ↓
authority / confidence / review history
```

核心目标：事实可验证、来源可追踪、上下文不丢失、历史可审计。

这条路线既服务人类，也服务机器。结构化但错误、过时或无出处的数据不能被视为高质量 Atlas。

### 5. Governance / Standardization Route（治理与标准化路线）

回答：**InteropAtlas 自己产生的方法、规范、标准和 Skills 如何产生、成熟、版本化和演进？**

暂定原则：

- 不把所有内部方法都立即称为 Standard；
- 先区分 Note / Experiment、Methodology / Guide、Specification、Standard / Profile；
- Skill 是方法或规范的可执行实现，不等同于方法论本身；
- 新规范之前必须进行 Prior Art Check；
- ID、版本、发布日期、URL、仓库名应视为不同问题，不急于混成一个编号；
- “一个标准一个仓库”只是候选方案，不是当前规则。

详细方向见 `project-generated-methods-standards.zh-CN.md`。

## Open Collaboration 不是第六条路线

近期实践已经把“多 Agent 怎么一起工作”的问题重新定义为更一般的 **Open Collaboration（开放协作）** 问题。

当前不把它升级为第六条 knowledge-system route。更合适的定位是 **cross-cutting operating layer（横向协作运行层）**：

```text
Open Collaboration
   ↓
谁发现任务？
谁接手？
如何避免重复？
谁执行？
谁 Review / Oversight？
谁最终授权？
```

它主要横向补强：

- **Curation / Contribution Route**：谁贡献、如何接手、成果如何进入 Review；
- **Governance / Standardization Route**：执行者、Reviewer、Maintainer / Approver 如何分工；
- Human 与 AI / Agent 尽量共享同一公开协作语义。

当前 V0 优先复用 GitHub 原生机制：Issue、Assignee、Projects / Fields、Sub-issues / Dependencies、Pull Request / Review、CODEOWNERS、Required Review、activity / stale。

Agent-specific Lease / Heartbeat / Scheduler 只属于潜在实现机制，不改变普通贡献者理解项目的方式；只有真实实践证明原生机制不足时才新增 IA 自有能力。

详见：
- `human-ai-open-collaboration-prior-art.zh-CN.md`；
- `open-collaboration-route-v0-notes.zh-CN.md`；
- Issue #19。

## 五条路线不是五个独立项目

它们共享同一事实基础：

```text
                    Sources
                       ↓
               Curation Route
                       ↓
            Evidence / Provenance
                       ↓
               Canonical Facts
                       ↓
        Validator / Resolver / Graph
                       ↓
                    Engine
                 ↙          ↘
          Human Route     Machine Route

       Governance / Standardization
       约束上述方法如何长期演进

       Open Collaboration
       横向约束谁做、如何接手、Review 与授权
```

Human Route 与 Machine Route 是主要消费路线；Curation、Trust 和 Governance 是保证系统能够长期生长且不失控的横向路线；Open Collaboration 是参与者如何共同运行这些路线的协作层。

## 双向驱动原则

### Human Need → Machine Capability

如果网站需要显示可信 backlinks，而 Renderer 只能临时扫描全部对象，这说明 Human Route 暴露了 Machine Route 缺少 Graph / Backlink Index。

### Machine Capability → Human Experience

如果 Engine 已能计算路径、覆盖率或替代方案，人类路线应考虑如何把这些能力投影成可理解的路径视图、比较页或地图，而不是只提供 JSON 输出。

### Practice → Model / Method Feedback

真实使用暴露的问题，应允许反向修改 Schema、Relation vocabulary、Renderer、Engine、Curation 规则甚至治理方法。

### Collaboration Practice → Coordination Feedback

如果 GitHub 原生 Issue / Assignee / PR / Review 已经足够，就不创造 Agent-only 任务系统；只有多人 / 多 Agent 实践持续暴露重复执行、失联任务或授权问题，才研究 Lease / Heartbeat / Scheduler 等新机制。

## 当前阶段的重点

近期不平均推进五条路线。当前主闭环已经从早期的“先把页面和 Graph 做出来”收敛为：

```text
Human:
IA-HI Specification
      ↓
Object Page Shell
      ↓
Browser / Accessibility Acceptance

Machine:
Graph / Resolver clean
      ↓
Validator / Schema correctness
      ↓
Query correctness

Trust / Curation:
Minimum Evidence + Prior Art + 收录规则
```

Governance / Standardization 已经开始通过 Human Interface 实践运行 **轻量 Specification Loop**：Prior Art → Draft Specification → Requirement → Audit → Implementation → Feedback；仍不建设重型标准组织。

Open Collaboration 当前保持 P1：先使用 GitHub 原生机制运行真实任务，再判断是否需要 IA-specific coordination。

最新阶段判断见 `route-alignment-audit-2026-09-01.zh-CN.md` 与 `roadmap.zh-CN.md`。
