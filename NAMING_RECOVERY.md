# Naming Recovery

InteropAtlas Naming Workstream 的稳定恢复入口。更换对话或执行者时，Owner 不需要重述历史或管理内部步骤。

## 1. 当前目标与权威规则

第一目标：减少 Owner 总注意力。第二目标：提高真实命名产出效率，而不是靠大规模低质量生成 + 末端筛选补救。

主观质量由 Owner 决定：`喜欢 / OK / 不要` 与自然语言理由就是训练标签，Controller 不另设“真正优秀”标准。

当前母组织 Owner-visible 形态规则：优先单词 / 连写专名；多词短语和短句不进入当前审阅批次，除非 Owner 后续改变。

展示前仍采用 practical screening；但**现在暂停大规模生成与现实筛查，先完成生成方法修复的接入。**

## 2. 最新 Owner 反馈：Batch 001 暴露生成端故障

累计历史原始生成 300 项（001=48、002=36、003=48、004=48、005=48、006=48、007=24），历史记录不改写。

原40项 Owner Review Batch 去掉多词短语后剩16项。Owner 直接反馈已写入 #411 comment `5654581018`：

- 整批整体“不太行”；
- #12 **Morrowrange** 是本批明确正向例外；
- #13 **Elsehorizon** “看起来也还行”；
- 其余整体“不太像名称”；
- 批次级主要问题：词用得太简单、组合太简单，有“小学生想出来的词汇”感。

Owner 随后进一步指出：应先优化**生成方法**，而不是继续提高末端筛选强度；特别追问此前总结的“变形方法”为何没有使用。

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

DELIVERY-411-005 的 `Each/Common/Else/Many + trace/grain/arc/relay/...` 等批量矩阵是直接证据。主要故障分类：

- `scheduler_bypass`
- `method_underuse`
- `construction_mode_collapse`
- `generation_capability_recovery_failure`

“不要恢复 G0–G8 benchmark”仍有效，但只禁止恢复已停止的 benchmark 实验；**不禁止使用已经提炼进入 Adaptive Naming 的 Lexicon / Catchword / Igor / River+Wolf / Siegel+Gale / NameStormers 等方法组件。**

## 4. 当前方法修复：Generation Capability Recovery Contract v0.2

当前 provisional control fix：

`02_Runtime/02_Tools/adaptive_naming/references/generation-capability-recovery-contract.md`

当前提交：`6dab4c2811ed1757d9dd2d09b61a2d689a7f24ab`

核心规则：

> **任何新的 candidate generation 前，必须先恢复 Generation Capability Packet，并留下 Generation Contract。不得从 `generate N names / 补一批 / 扩大候选池` 直接跳到生成。**

Generation Contract 至少明确：

- question / biggest unknown / Name Job focus；
- workflow patterns；
- construction operator portfolio；
- territory material；
- prototype stage；
- Transformation Operators 用于 exploration / rescue 的方式；
- sound-led 时的 phonetic character brief；
- cadence / runtime isolation；
- anti-collapse checks；
- stop condition。

普通探索默认至少使用 3 个真正不同的 construction family；“换前缀 / 换后缀 / 换第二普通词”不算不同 family。

Transformation Operators 明确恢复为普通 exploration 与 rescue 都可调用。使用 transformation 时默认 `Prototype discovery → bounded transformation`，弱 seed 不因“还没用过某 operator”而被机械变形。

当前 #411 中 simple natural compound 降为低预算路线；纯 sound-led opaque route 也因 fantasy / personal-name 风险降权，优先 `semantic / morpheme anchor + phonetic engineering`。

## 5. 已完成两轮无现实查询 Generation Regression

### REG-411-GEN-001

证据：

`03_Evolution/01_Research/03_Tests/organization-naming-411-generation-regression-001.md`

结果：provisional pass。

- 18项内部样本覆盖 lexical transfer、root-derived、telescoping/fusion、bounded transformation、sound-led 五个 family；
- 简单普通词矩阵显著减少；
- Transformation Operators 有真实 lineage，不再只存在于文档；
- 暴露问题：root-derived 可能过度学术化；sound-led 可能 fantasy 化；弱 seed transformation 仍弱。

### REG-411-GEN-002

证据：

`03_Evolution/01_Research/03_Tests/organization-naming-411-generation-regression-002.md`

结果：pass with routing change。

- Prototype → Transformation 两阶段改善变形自然度；
- Lexicon / Igor / River+Wolf / Catchword / NameStormers 的已提炼组件实际进入 Generation Contract；不是恢复 benchmark；
- simple compound 未重新主导；
- pure sound-led 虽有 Character Brief 仍容易人名 / fantasy 化，因此当前任务继续降权。

两轮都是 same-context Controller regression，**不是 Owner 质量验收，也不是独立 Reviewer 证据。** 回归中的名称不计入正式候选池，不做现实查询，不要求 Owner 评价。

聚焦控制回归已新增：

`02_Runtime/02_Tools/adaptive_naming/evals/generation-capability-recovery-regression.yaml`

提交：`b4ec35ddafa27696ab3007bca1d141dd1ad0ca89`

## 6. 当前下一动作

**还不恢复100级别批量生成，也不恢复域名 / 商标筛查。**

当前先完成方法接入：

1. 把 Generation Contract before `generate` 作为 Adaptive Naming 生成入口的显式控制规则；
2. 保留 focused regression，防止换上下文后再次只恢复状态而丢失方法；
3. 记录这是严重 control-layer defect 的 provisional fix，保留 rollback / supersede；
4. 接入后再跑一轮小型真实 generation（仍先不做现实查询），确认入口本身会触发 contract，而不是靠当前对话记忆。

只有生成端连续通过后，才恢复真实候选批量 production + practical screening。

## 7. 接管规则

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
