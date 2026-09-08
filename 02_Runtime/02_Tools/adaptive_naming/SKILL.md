---
name: adaptive-naming
description: 自适应品牌、组织、项目与产品命名。先建立目标与边界，再以小批探索、双轨评价、现实验证、诊断和状态更新循环寻找高质量且现实可采用的名称；适用于需要 Agent 自主决定下一步、保留探索地图与失败经验的命名任务。
version: 0.1.0
---

# Adaptive Naming Skill v0.1

## 1. 目标

本 Skill 不是固定流水线，也不是一次性名字生成器。它给 Agent 一套稳定方法、搜索方向和判断边界，同时允许 Agent 根据当前状态自主决定下一步。

核心原则：

> **目标明确，边界稳定，路径开放，经验累积，方法进化。**

本 Skill 负责“怎么思考与行动”；单次任务产生的地图、候选、证据和局部经验写入独立状态文件，不写回本 Skill。

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

## 4. 运行前：建立 Naming Job

在首次生成候选前，建立或补全状态文件。至少确认：

- 被命名对象及其长期尺度；
- 主要受众与使用语境；
- 应表达 / 应避免的概念、气质和联想；
- 语言、发音、拼写、长度、架构等硬约束；
- 必要现实条件，例如目标 TLD、商标/组织/项目名称冲突；
- Owner 已知偏好，但不得把偏好伪装成普遍质量标准。

同时建立一张**初始命名空间地图**：竞争者/相邻对象如何命名、哪些类别明显拥挤、哪些语义或构词区域值得探索。初始地图是先验，不是假定完整事实。

## 5. 核心循环：先判断“当前最值得做什么”

不要机械执行固定 Step 1 → Step 2 → Step 3。每一轮都先读取当前状态，然后选择信息价值最高的下一动作。

允许动作包括：

- `map`：补充竞争 / 语义 / 构词空间地图；
- `generate`：在选定区域小批生成；
- `evaluate_quality`：评价名称本身质量；
- `verify_reality`：查询现实碰撞、域名或其他 namespace；
- `diagnose`：解释观察意味着什么；
- `update_state`：更新地图、假设、候选与偏好；
- `ask_owner`：只在人的判断能明显改变结果时询问；
- `stress_test`：把强候选放入长期品牌/组织架构语境；
- `change_strategy`：换语义区、构词法、探索深度或评价重点；
- `stop`：达到停止条件。

默认微循环：每轮生成 **3–5 个**候选；若当前最大未知不是“缺候选”，下一步可以完全不生成。

```text
读取状态
  ↓
判断当前最大的未知 / 问题
  ↓
选择下一动作
  ↓
获得新观察
  ↓
诊断
  ↓
更新状态
  ↓
继续 / 换方向 / 问人 / 停止
  ↺
```

## 6. 生成：把构词方法当作工具箱，不当作配额

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

这些是**可选搜索路径**，不是必须平均覆盖的清单。Agent 可以创造列表之外的新构词策略；新策略要在状态中记录其做法、目的和观察结果。

## 7. 双轨评价

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

## 8. 现实验证工具合同

Agent 应使用当前运行环境可用的真实工具，不凭记忆断言可用性。

### 现实身份 / 碰撞

优先进行 exact-name 与 near-name 搜索，并记录：

- query；
- 对象类型；
- 相关程度；
- source；
- observed_at；
- observation / uncertainty。

### 域名

调用 IA 已验证的统一方法：

[`Domain Availability Verification Method v0.1`](../../../03_Evolution/01_Research/01_Prior_Art/Naming_Methods/Execution/domain-availability-verification-method-v0.1.zh-CN.md)

其核心顺序为：registry authoritative RDAP / official availability → IANA bootstrap resolver → registry RDDS/WHOIS → registrar machine/API → two-registrar corroboration → unresolved。

运行环境只决定 adapter，不改变证据标准。`unknown` / `error` 永远不能自动转换为 `available`。

## 9. 诊断：失败必须回答“为什么”

出现重要观察或一批候选完成评价后，按需读取 [`references/diagnosis-and-next-action.md`](references/diagnosis-and-next-action.md)。

诊断至少区分：

1. **候选级**：这个名字发生了什么？
2. **批次 / 区域级**：是否出现重复模式？
3. **策略级**：这些重复模式是否足以改变下一步？

先诊断，再优化。不得从单个候选直接跳到永久策略结论。

## 10. 状态与学习

每个 Naming Job 使用独立状态文件，结构见：

[`templates/naming-state-template.yaml`](templates/naming-state-template.yaml)

每轮至少更新与本轮有关的：

- 新观察；
- 候选状态；
- 现实证据；
- 区域 / 构词策略认识；
- 诊断；
- 当前最大未知；
- 下一动作及理由。

### 任务内经验

可以直接影响当前任务，例如“当前语义区拥挤”“某种结构在本任务中过于产品化”。

### 跨任务经验

若发现 Skill 中没有的新方法或反复出现的经验，不直接无审核修改本 Skill。先记录为 `experience_candidate`，至少包含：

- observation；
- scope；
- evidence_count / supporting jobs；
- possible generalization；
- counterexample / risk；
- confidence；
- proposed change。

只有跨任务证据稳定后，再通过独立 review / PR 提升为 Skill 或 reference 的新版本。

## 11. Owner 反馈

减少人的工作量。通常先由 Agent 做地图、生成、质量评价和现实筛查，只把少量高信息价值候选或决策问题交给 Owner。

适合询问 Owner 的情况：

- 两个或少数强候选客观上难区分；
- 新方向的主观气质需要校准；
- 需要确认偏好是否稳定；
- 即将做重大策略转向；
- 已进入最终收敛。

Owner preference 记录为独立信号，可随阶段调整影响力：探索早期防止过拟合；收敛后提高权重；最终采用由 Owner 决定。

## 12. 长期架构压力测试

对强候选，根据对象类型放进真实语境，而不是只看裸名字。对于 umbrella organization，可测试例如：

```text
[Name]
[Name] Research
[Name] Commons
[Name] Tools
[Name] / [Project]
A project by [Name]
```

若候选在架构语境中暴露问题，记录为诊断事件，不只扣分。

## 13. 停止条件

满足下列任一情况时可以停止当前循环：

- 已有足够数量的高质量、现实可推进候选进入 Owner 最终决策；
- 当前继续探索的信息增益很低，且已有候选满足任务目标；
- 关键现实验证被环境阻塞，需要明确 handoff；
- Naming Brief / 目标本身出现实质矛盾，必须回到 Owner；
- 预算 / 时间边界达到，需输出当前地图、最强候选和未解决问题，而不是假装完成。

若尚无足够强候选，不得为了凑数量降低质量或现实证据门槛；应诊断失败分布后换区域、换构词方式或重新检查目标。

## 14. 最小输出合同

任务中途可只输出必要的 Owner-facing 内容；完整收敛时至少给出：

- 当前 Naming Job / 关键约束；
- 已探索区域与主要学习；
- 2–5 个当前强候选（或明确说明为何尚无）；
- 每个候选的名称本身质量摘要；
- 独立的现实可用性摘要；
- 主要风险 / 未知；
- 下一步或停止理由。

不要把内部海量 working pool 机械倾倒给 Owner。
