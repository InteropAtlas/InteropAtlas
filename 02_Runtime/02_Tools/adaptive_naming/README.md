# Adaptive Naming

这是 InteropAtlas Naming Research 的可执行方法包 v0.1。

最小结构：

```text
Agent
├─ SKILL.md                         稳定方法与运行边界
├─ references/                     按需读取的方法工具箱
└─ templates/naming-state-template.yaml
                                   单次任务运行时状态模板
```

当前版本刻意保持轻量：不引入数据库、图数据库或固定工作流引擎。Agent 负责根据状态自主决定下一步；真实使用暴露规模或并发问题后，再考虑升级底层状态存储。

## 入口

- [`SKILL.md`](SKILL.md) — 核心自适应命名方法
- [`references/word-formation-strategies.md`](references/word-formation-strategies.md) — 构词 / 搜索策略工具箱
- [`references/diagnosis-and-next-action.md`](references/diagnosis-and-next-action.md) — 诊断与状态转移规则
- [`templates/naming-state-template.yaml`](templates/naming-state-template.yaml) — 运行时地图 / 状态模板

域名验证不复制实现，复用 IA 已验证的统一方法：

- [`Domain Availability Verification Method v0.1`](../../../03_Evolution/01_Research/01_Prior_Art/Naming_Methods/Execution/domain-availability-verification-method-v0.1.zh-CN.md)

## 数据边界

- **Skill**：稳定方法、评价、诊断、策略选项；
- **State**：单个 Naming Job 动态产生的地图、候选、证据、局部经验；
- **Experience candidates**：可能跨任务成立、但尚未升级为稳定方法的经验候选。

核心 Skill 不因单次任务结果自动改写。跨任务稳定经验通过 review / PR 进入后续版本。

## v0.1 验证方式

不另造 benchmark / dry-run。直接用当前真实 Organization Naming Job 作为 Fit Test：

```text
建立初始 state
→ 小批探索
→ 质量评价 + 现实验证
→ 诊断
→ 更新地图
→ 自主选择下一动作
→ 收敛到现实可推进 finalists
```

真实运行中发现的结构性问题反馈到本包，再决定 v0.1 是否可以稳定化。
