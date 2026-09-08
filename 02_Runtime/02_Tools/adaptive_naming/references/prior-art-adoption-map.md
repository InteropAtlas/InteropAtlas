# Prior Art → Adaptive Naming v0.1 采用图

本文件只回答：哪些能力直接采用、哪些经过改造、哪些属于 InteropAtlas 的综合 / Agent-native extension。详细证据仍以 Naming Research #407 / #408 与对应历史材料为准。

| 来源 | 直接采用 / 保留 | 在 v0.1 中的改造 |
| --- | --- | --- |
| Lexicon / G1 | 先明确名称要完成的工作；Creative Framework；语言约束与创意并行意识 | 不保留固定阶段流水线，转为状态驱动动作 |
| Igor / G3 | 生成前看竞争命名空间、类别与 white space | 初始地图只是先验；运行中继续更新地图 |
| Catchword / G2 | 广泛词汇、词根、联想和多种构词路线 | 不要求一次性高容量生成；改成 3–5 个微批次、边走边学 |
| River + Wolf / G4 | Character / Communication / Construction / Continuum 等可调参数 | 参数成为状态变量，可被诊断更新 |
| Tungsten / G6 | 长期 Pivot、母品牌 / 架构适配、长期性压力测试 | 变成可按需调用的 `stress_test` 动作，而非固定后段 |
| NameStormers / G7 | 人类反馈与迭代 | Owner 只在高信息价值节点参与；偏好与普遍质量分离，权重随阶段变化 |
| IA G0 | 低约束创造、叠字、拼词、词根、新造词、word + letter 等实战构词路线 | 汇入可选择的构词工具箱，不作为固定配额 |
| IA G8 | 局部区域探索、现实观察、状态更新、继续 / 换区循环；隔离 raw survivor 信号以防生成塌缩 | 提升为核心循环，但上层允许下一动作不是生成，而是 map / evaluate / verify / diagnose / ask / stop |
| SkillMedev Brand Naming | criteria-before-generation；多维评价不压成平均总分；语言 / 记忆 / 语境检查 | 与现实可用性明确拆成双轨；加入 Pareto 与动态状态 |
| Brand Naming Studio | `SKILL.md + references + templates/scripts`；按需读取 | 采用轻量可移植包结构，避免一开始构建重型系统 |
| fcoury Brand Naming | 竞争地图、利益 / 意义探索、词源、隐喻、相邻领域、声音生成 | 高容量 treasure hunt 改为小批高反馈探索 |
| Quaere Naming | 工具验证现实可用性；不足时回退再探索；blocked 不得猜测 | 现实 gate 不反向伪装成名称本身质量；加入诊断层和状态地图 |
| VeyraLabs Naming Suite | 地图、生成、审计等能力可模块化 | v0.1 不拆成多个独立 Skill，先由一个总 Skill 按需调用不同动作，降低工程成本 |

## IA synthesis / Agent-native extension

v0.1 的关键综合不是发明一个新的线性流程，而是把已有优秀机制放进同一个自适应控制框架：

```text
当前状态
↓
判断最大的未知 / 问题
↓
选择最有信息价值的动作
↓
观察
↓
诊断
↓
更新地图与状态
↓
继续 / 换策略 / 问人 / 停止
↺
```

目前最重要的 IA 扩展包括：

1. **双轨评价**：名称本身质量 ≠ 现实可用性；
2. **Pareto + learning preservation**：候选可被支配淘汰，但经验不丢；
3. **诊断先于优化**：观察 → 诊断 → 抽象经验 → 状态变化；
4. **状态驱动下一动作**：系统可决定下一步不是生成；
5. **任务内地图持久化**：新 Agent 不必重新走完本次任务已经走过的路；
6. **低负担 Owner feedback**：人只处理机器难以替代的主观判断；
7. **经验分层**：任务局部经验进入 state，潜在跨任务经验进入 experience candidate，稳定方法才通过 review 升级 Skill。
