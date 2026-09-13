# Naming Recovery

InteropAtlas Naming Workstream 的稳定恢复入口。更换对话或执行者时，Owner 不需要重述历史或管理内部步骤。

## 1. 当前目标与权威规则

第一目标：减少 Owner 总注意力。第二目标：提高真实命名产出效率，而不是靠大规模低质量生成 + 末端筛选补救。

主观质量由 Owner 决定：`喜欢 / OK / 不要` 与自然语言理由就是训练标签，Controller 不另设“真正优秀”标准。

当前母组织 Owner-visible 形态规则：优先单词 / 连写专名；多词短语和短句不进入当前审阅批次，除非 Owner 后续改变。

展示前仍采用 practical screening；但**现在暂停扩大筛选与新候选现实查询，先修生成端。** 现实筛查不是当前最大未知。

## 2. 最新 Owner 反馈：Batch 001 暴露生成端故障

累计历史原始生成 300 项（001=48、002=36、003=48、004=48、005=48、006=48、007=24），历史记录不改写。

原40项 Owner Review Batch 去掉多词短语后剩16项。Owner 最新直接反馈已写入 #411 comment `5654581018`：

- 整批整体“不太行”；
- #12 **Morrowrange** 是本批明确正向例外；
- #13 **Elsehorizon** “看起来也还行”；
- 其余整体“不太像名称”；
- 批次级主要问题：词用得太简单、组合太简单，有“小学生想出来的词汇”感。

这说明当前问题不是再增加 `name-likeness` 末端筛选，而是生成机制本身退化。

重要边界：Morrowrange / Elsehorizon 以及更早的 Reloa / Merosophy / Multifinality 等 Owner-positive 名称只能用于抽象潜在品质；不得作为 Generator 的词根、后缀、音节、拼写或表面模板。

## 3. 根因：State Recovery 成功，但 Generation Capability Recovery 失败

最近交付批次恢复了：目标、Owner 偏好、候选池、筛选计数、域名 / 商标阻塞；但真正生成前没有强制重新加载和调度：

- Workflow Pattern Scheduler；
- Construction / Operator Scheduler；
- `word-formation-strategies.md`；
- Transformation Operators；
- prior-art 中已提炼进 Adaptive Naming 的生成组件。

执行因此从：

`diagnose → schedule workflow → schedule operators → generate → integrity check`

退化为：

`需要更多候选 → 简单语义词根矩阵拼接 → reality/domain 筛选`。

DELIVERY-411-005 的 `Each/Common/Else/Many + trace/grain/arc/relay/...` 等批量矩阵是直接证据。主要故障分类：`scheduler_bypass + method_underuse + construction_mode_collapse`。

“不要恢复 G0–G8 benchmark”仍有效，但只禁止恢复已停止的 benchmark 实验；**不禁止使用已经提炼进入 Adaptive Naming 的 Lexicon / Catchword / Igor / River+Wolf / Siegel+Gale / NameStormers 等方法组件。**

## 4. 当前方法修复：Generation Capability Recovery Contract

新增 provisional control fix：

`02_Runtime/02_Tools/adaptive_naming/references/generation-capability-recovery-contract.md`

提交：`e69d1301360a923abf99d2e781deed49be0c8949`

核心规则：

> **任何新的 candidate generation 前，必须先恢复 Generation Capability Packet，并留下 Generation Contract。不得从 `generate N names / 补一批 / 扩大候选池` 直接跳到生成。**

Generation Contract 至少明确：

- question / biggest unknown / Name Job focus；
- workflow patterns；
- construction operator portfolio；
- territory material；
- Transformation Operators 用于 exploration / rescue 的方式；
- cadence / runtime isolation；
- anti-collapse checks；
- stop condition。

普通探索默认至少使用 3 个真正不同的 construction family；“换前缀 / 换后缀 / 换第二普通词”不算不同 family。

Transformation Operators 明确恢复为普通 exploration 与 rescue 都可调用：controlled spelling mutation、meaningful affix、clipping / telescoping、light blend、segmentation 等；同时可并行 root-derived、morpheme-grounded coinage、sound-led、opaque proper-name construction、lexical/metaphorical transfer。

这份合同目前是 **provisional**，不冒充已经验证成功的稳定 Skill 升级。

## 5. 当前唯一下一动作：小规模 Generation Regression

**暂停大规模生成，暂停域名 / 商标 / reality 筛查。**

下一步先用新的 Generation Contract 生成 **15–20 个内部回归样本**：

- 不查询域名；
- 不查询商标；
- 不查询现实撞名；
- 不作为正式 Owner 候选展示；
- 不用 Owner-positive 名称当模板；
- 只验证生成机制是否真正覆盖多个 operator family，以及是否显著减少简单拼词 / 小学生式组合并恢复成熟 proper-name 感。

若内部回归仍明显失败：继续修生成方法，**不进入现实筛查**。

若回归显示方法机制恢复：再决定是否把 Generation Capability Recovery Contract 吸收到 `SKILL.md` / regression cases，并恢复批量候选生成。

## 6. 接管规则

后继 Agent 在任何 `generate` 前必须读取：

1. 本 `NAMING_RECOVERY.md`；
2. `02_Runtime/02_Tools/adaptive_naming/SKILL.md`；
3. `references/word-formation-strategies.md`；
4. `references/generation-capability-recovery-contract.md`；
5. 当前任务直接 Owner 反馈 / Name Job 必要上下文。

只恢复状态，不恢复上述生成能力，不得开始生成。

请示只在三类情况：必须由 Owner 决定的价值 / 战略事项；实质影响目标完成率；对效率有极大影响。普通 method schedule、operator portfolio、内部 regression、可逆修复由 Controller 自主执行。

不要恢复旧 G0–G8 benchmark、Reviewer 校准、SEM-408-006、本地模型测试或成本研究。不要重新初始化 Naming Job。

核心原则：**聊天可以丢上下文，仓库不能丢方法；恢复不仅要知道“做到哪”，还必须知道“怎么做”。**
