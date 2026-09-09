---
name: adaptive-naming
description: 自适应品牌、组织、项目与产品命名。先建立目标与边界，再通过探索、评价、现实验证、诊断、搜索完整性检查与状态更新循环寻找高质量且现实可采用的名称；适用于需要 Agent 自主决定下一步、保留探索地图并避免局部搜索坍缩的命名任务。
version: 0.2.0
---

# Adaptive Naming Skill v0.2

## 1. 目标

本 Skill 不是固定流水线，也不是一次性名字生成器。它给 Agent 一套稳定方法、搜索方向和判断边界，同时允许 Agent 根据当前状态自主决定下一步。

核心原则：

> **目标明确，边界稳定，路径开放，经验累积，方法进化。**

本 Skill 负责“怎么思考与行动”；单次任务产生的地图、候选、证据和局部经验写入独立状态文件，不写回本 Skill。

v0.2 额外要求：**搜索多样性和搜索完整性是控制器责任，不依赖生成模型自行保持。**

## 2. 使用边界

适用于：

- Organization / umbrella organization；
- brand / company；
- product / project / service；
- open-source project / public initiative；
- 需要长期扩展、现实可采用或多轮探索的 Naming Job。

不适用于变量、函数、普通文件名等纯工程标识。

正式商标法律意见不属于本 Skill 能力；现实筛查只能作为研究与决策支持。

## 3. 稳定不变量

运行过程中不得为了“得到结果”随意改变以下原则：

1. 先明确被命名对象、长期目标、硬约束和成功定义。
2. **名称本身质量**与**现实可用性**分开观察、分开记录。
3. 域名可注册不代表名字好；现实撞名不自动代表创意质量差。
4. 不把多维质量默认压成一个平均总分。
5. 可使用严格帕累托支配淘汰明显被全面支配的候选。
6. 候选可以退出 active pool，但其 provenance、诊断与学习信号不得丢失。
7. 单个失败不得直接升级为普遍规则；策略变化要基于诊断与足够证据。
8. `unknown / error` 不得伪装成现实可用。
9. Owner 偏好与一般命名质量分开；前期权重低，收敛期权重可提高，最终采用权属于 Owner。
10. 若已有上下文足够，不要求 Owner 重复回答；只有缺失信息会实质改变下一步时才询问。
11. **探索阶段不得让当前 strongest / survivor 候选成为隐性生成模板。** 比较用候选与生成用上下文必须分离。
12. **现实幸存结果不得直接塑造同批或紧邻批次的词形模板。** 现实结果先进入控制器诊断，再决定是否改变区域或策略。
13. **微循环是内部执行单位，不是用户交互单位。** 只要存在明确下一动作且不需要 Owner，Agent 应继续自主执行。
14. 搜索完整性问题不得用“某个候选单独解释得通”掩盖；必须检查语义、词形和构词来源是否发生集中或坍缩。

## 4. 运行前：建立 Naming Job

在首次生成候选前，建立或补全状态文件。至少确认：

- 被命名对象及其长期尺度；
- 主要受众与使用语境；
- 应表达 / 应避免的概念、气质和联想；
- 语言、发音、拼写、长度、架构等硬约束；
- 必要现实条件，例如目标 TLD、商标/组织/项目名称冲突；
- Owner 已知偏好，但不得把偏好伪装成普遍质量标准。

同时建立一张**初始命名空间地图**：竞争者/相邻对象如何命名、哪些类别明显拥挤、哪些语义或构词区域值得探索。初始地图是先验，不是假定完整事实。

状态中还应建立 `search_control`，至少记录当前搜索模式、已探索语义覆盖、近期词形/语义/构词家族集中度、当前 comparison-only 候选和必要 cooldown。

## 5. 搜索模式：Exploration 与 Exploitation 必须显式区分

每次生成前明确当前 `search_mode`：

### Exploration｜探索

目标是扩大或修复搜索空间覆盖，而不是围绕当前最强名字爬山。

探索阶段：

- strongest / finalist / survivor 候选默认只用于评价比较，不用于生成提示；
- 检查 semantic coverage，优先补采样长期目标中被忽略的区域；
- 检查词根、前后缀、语义家族和构词模板是否过度集中；
- 同一批先完成名称本身比较，再做现实筛查；
- 现实筛查结果不得回灌同批生成，也不得被压缩成“这个词形更容易活下来”直接交给 Generator；
- 如需围绕某一强区域继续，应先通过搜索完整性检查，再显式切换到 exploitation。

### Exploitation｜深挖

目标是验证一个已经有独立证据支持的强区域或结构。

深挖阶段允许局部变体、相邻词根和结构对照，但必须：

- 明确记录为什么值得深挖；
- 设定有限范围或退出条件；
- 不把“现实更容易存活”单独作为进入深挖的理由；
- 若候选家族越来越相似而新信息下降，应退回 exploration。

不能在状态中写着 exploration，实际却围绕一个 incumbent 持续生成同族变体。

## 6. 核心循环：先判断“当前最值得做什么”

不要机械执行固定 Step 1 → Step 2 → Step 3。每一轮先读取当前状态，然后选择信息价值最高的下一动作。

允许动作包括：

- `map`：补充竞争 / 语义 / 构词空间地图；
- `generate`：在选定区域生成；
- `evaluate_quality`：评价名称本身质量；
- `verify_reality`：查询现实碰撞、域名或其他 namespace；
- `diagnose`：解释观察意味着什么；
- `check_search_integrity`：检查覆盖率、家族集中、incumbent 锚定、策略忠实度和幸存者反馈；
- `update_state`：更新地图、假设、候选与偏好；
- `ask_owner`：只在人的判断能明显改变结果时询问；
- `stress_test`：把强候选放入长期品牌/组织架构语境；
- `change_strategy`：换语义区、构词法、搜索模式、探索深度或评价重点；
- `stop`：达到停止条件。

批量大小不是固定配额：

- 新区域或搜索空间重置时，可一次生成约 **6–10 个轻量内部候选**，用于提高地图信息密度；
- 已知区域的精细探索或 exploitation，通常 **3–5 个**；
- 若当前最大未知不是“缺候选”，可以生成 **0 个**。

```text
读取完整状态
  ↓
搜索完整性检查 + 判断最大未知
  ↓
选择 search_mode 与下一动作
  ↓
若需生成：形成 sanitized Generation Brief
  ↓
获得新观察
  ↓
诊断
  ↓
更新状态
  ↓
自动继续 / 换方向 / 真正需要时问 Owner / 停止
  ↺
```

## 7. 生成：控制器与 Generator 隔离

生成前按需读取 [`references/word-formation-strategies.md`](references/word-formation-strategies.md)。

Agent 应知道至少存在这些路线：

- 现成词 / 语义迁移；
- 复合词；
- 拼词 / 混成词；
- 词根组合；
- 完全新造词；
- 受控改写拼写；
- 重复 / 双写字母；
- 主体词 + 单字母；
- 前缀 / 后缀；
- 截短 / 短语压缩 / 缩略；
- 声音先行；
- 从相邻领域、物体、动作、自然现象、职业、空间和隐喻寻找材料。

这些是可选搜索路径，不是永久配额。Agent 可以创造列表之外的新构词策略；新策略要在状态中记录其做法、目的和观察结果。

### Sanitized Generation Brief

控制器可以读取完整任务状态，但 Generator 在 exploration 阶段默认只接收压缩后的生成 Brief。Brief 应包含：

- 当前目标与硬约束；
- 本轮要探索的语义区域；
- 应覆盖或尝试的构词方向；
- 已知语言/尺度风险；
- task-local cooldown 家族；
- 本轮要回答的搜索问题。

默认**不向 Generator 暴露**：

- strongest / survivor / finalist 的具体名称；
- 它们成功的具体词根、词尾或音形模式；
- 域名可用、现实撞名、商标等幸存结果；
- Owner 对具体 incumbent 的喜欢/接受程度。

如果运行环境没有独立 subagent，也应先由控制器写出 sanitized brief，再只基于该 brief 生成；不要在生成时回看 incumbent 名称和现实结果。

只有显式进入 exploitation，且状态记录了理由时，才允许把被深挖的结构性特征有限提供给 Generator。

## 8. 搜索完整性 / 防坍缩检查

以下检查不是要求平均分配，而是用于判断搜索是否失真。

### 语义覆盖

观察长期目标的主要语义区域是否被持续低采样。某一区域胜出不自动说明其他区域已经充分探索。

### 形态与语义家族集中

不要只检查 exact substring。识别共享词根、前后缀、同义/近义代理、声音骨架和构词模板是否在 recent / active / promising 候选中异常集中。

例如 `plural / plur- / pluri- / poly- / multi- / many-` 可能属于同一任务中的 multiplicity 家族；具体家族必须由当前任务诊断，不建立永久黑名单。

### Incumbent anchoring

如果 strongest candidate 的词根、语义代理、音形或结构持续出现在新候选中，检查它是否从评价基准泄漏为生成模板。

发现泄漏时：

1. 将 incumbent 标为 `comparison_only`；
2. 从 Generator 上下文移除具体名称和成功词形；
3. 必要时对其语义/形态家族设置 task-local cooldown；
4. 恢复被低采样区域。

### Strategy fidelity

每批完成后比较：**声称探索的方向**与**实际生成/入选候选**是否一致。

若计划探索 A/B/C，却最终仍回到旧家族 X，不能把该轮记作“A/B/C 已失败”；应记录为策略执行失败，并重新生成或调整生成合同。

### Survivorship feedback

现实筛查大量淘汰某些路线后，剩余路线可能只是“更容易占用”，不一定“创意更好”。

探索阶段将现实结果与下一批 Generator 隔离。现实可用性只能通过控制器更新 crowding / feasibility，不得直接形成“多生成这种词形”的提示。

## 9. 双轨评价

### A. 名称本身质量

按任务需要从以下维度观察，不默认求平均分：

- 独特性；
- 发音自然度；
- 拼写 / 听写负担；
- 记忆性；
- 语义契合；
- 语义空间与延展余量；
- 对当前对象尺度的适配；
- 长期性；
- 象征 / 意义压缩能力；
- 跨场景使用能力；
- 品牌架构延展；
- 视觉感受；
- 必要时的跨语言 / 文化联想。

对候选比较可使用严格帕累托支配：若 A 在所有当前重要质量维度都不差于 B，且至少一个维度严格优于 B，则 B 可以退出 active pool。退出原因必须保留。

不要仅因一个候选“均衡”就优先，也不要把主观偏好偷偷变成统一分数。

### B. 现实可用性

单独记录：

- 同名 / 近名公司、组织、产品、项目与软件；
- 域名；
- 商标导向风险；
- 必要的平台名称 / handle / package namespace；
- 查询不确定性与证据来源。

现实碰撞只能更新可行性和命名空间地图，除非它同时暴露了独特性等内在问题，否则不要反向改写质量评价。

## 10. 现实验证工具合同

Agent 应使用当前运行环境可用的真实工具，不凭记忆断言可用性。

### 现实身份 / 碰撞

优先进行 exact-name 与 near-name 搜索，并记录：query、对象类型、相关程度、source、observed_at、observation / uncertainty。

### 域名

调用 IA 已验证的统一方法：

[`Domain Availability Verification Method v0.1`](../../../03_Evolution/01_Research/01_Prior_Art/Naming_Methods/Execution/domain-availability-verification-method-v0.1.zh-CN.md)

其核心顺序为：registry authoritative RDAP / official availability → IANA bootstrap resolver → registry RDDS/WHOIS → registrar machine/API → two-registrar corroboration → unresolved。

运行环境只决定 adapter，不改变证据标准。`unknown / error` 永远不能自动转换为 `available`。

## 11. 诊断：失败必须回答“为什么”

出现重要观察或一批候选完成评价后，按需读取 [`references/diagnosis-and-next-action.md`](references/diagnosis-and-next-action.md)。

诊断至少区分：

1. 候选级：这个名字发生了什么？
2. 批次 / 区域级：是否出现重复模式？
3. 搜索完整性级：是否发生语义、形态、构词或 incumbent 坍缩？
4. 策略级：这些重复模式是否足以改变下一步或 search_mode？

先诊断，再优化。不得从单个候选直接跳到永久策略结论。

## 12. 状态与学习

每个 Naming Job 使用独立状态文件，结构见：

[`templates/naming-state-template.yaml`](templates/naming-state-template.yaml)

每轮至少更新与本轮有关的：

- 新观察；
- 候选状态；
- 现实证据；
- 区域 / 构词策略认识；
- 搜索模式与搜索完整性状态；
- 诊断；
- 当前最大未知；
- 下一动作及理由。

### 任务内经验

可以直接影响当前任务，例如“当前语义区拥挤”“某种结构在本任务中过于产品化”“某个形态家族暂时需要 cooldown”。

### 跨任务经验

若发现 Skill 中没有的新方法或反复出现的经验，不直接无审核修改本 Skill。先记录为 `experience_candidate`，至少包含 observation、scope、evidence_count / supporting jobs、possible generalization、counterexample / risk、confidence、proposed change。

只有跨任务证据稳定后，再通过独立 review / PR 提升为 Skill 或 reference 的新版本。

## 13. Owner 反馈与自主执行

减少人的工作量。通常先由 Agent 做地图、生成、质量评价、现实筛查和内部策略切换，只把少量高信息价值候选或决策问题交给 Owner。

**不要因为完成一个微循环而停止当前用户回合。**

只要同时满足：

- 当前状态存在明确 `next_action`；
- 不需要新的 Owner 判断；
- 没有无法绕过的工具/证据阻塞；
- 尚未达到收敛或预算/时间边界；

Agent 就应自主进入下一微循环，并持续维护状态。

适合暂停并询问 Owner 的情况：

- 两个或少数强候选客观上难区分；
- 新方向的主观气质需要校准；
- 需要确认偏好是否稳定；
- 重大目标或硬边界不清楚；
- 已进入最终收敛；
- 预算/时间边界需要 Owner 决定是否继续。

重大**内部搜索策略**变化通常不需要 Owner 批准；应记录诊断后自主执行。Owner preference 仍与一般命名质量分开，最终采用权属于 Owner。

## 14. 长期架构压力测试

对强候选，根据对象类型放进真实语境，而不是只看裸名字。对于 umbrella organization，可测试例如：

```text
[Name]
[Name] Research
[Name] Commons
[Name] Tools
[Name] / [Project]
A project by [Name]
```

若候选在架构语境中暴露问题，记录为诊断事件，不只判断文字是否顺口；还要判断它呈现出的组织身份是否符合长期尺度。

## 15. 停止条件

满足下列任一情况时可以停止当前循环：

- 已有足够数量的高质量、现实可推进候选进入 Owner 最终决策；
- 当前继续探索的信息增益很低，且已有候选满足任务目标；
- 关键现实验证被环境阻塞，需要明确 handoff；
- Naming Brief / 目标本身出现实质矛盾，必须回到 Owner；
- 预算 / 时间边界达到，需输出当前地图、最强候选和未解决问题，而不是假装完成。

若尚无足够强候选，不得为了凑数量降低质量或现实证据门槛；应诊断失败分布与搜索完整性后换区域、换构词方式、切换 search_mode 或重新检查目标。

## 16. 最小输出合同

任务中途可只输出必要的 Owner-facing 内容；完整收敛时至少给出：

- 当前 Naming Job / 关键约束；
- 已探索区域与主要学习；
- 当前 search_mode 与重要搜索完整性诊断；
- 2–5 个当前强候选（或明确说明为何尚无）；
- 每个候选的名称本身质量摘要；
- 独立的现实可用性摘要；
- 主要风险 / 未知；
- 下一步或停止理由。

不要把内部海量 working pool 机械倾倒给 Owner。