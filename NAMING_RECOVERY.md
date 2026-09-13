# Naming Recovery

InteropAtlas Naming Workstream 的稳定恢复入口。更换对话或执行者时，Owner 不需要重述历史或管理内部步骤。

## 1. 当前目标与权威规则

第一目标：减少 Owner 总注意力。第二目标：提高真实命名产出效率，而不是靠大规模低质量生成 + 末端筛选补救。

主观质量由 Owner 决定：`喜欢 / OK / 不要` 与自然语言理由就是训练标签，Controller 不另设“真正优秀”标准。

当前母组织 Owner-visible 形态规则：优先单词 / 连写专名；多词短语和短句不进入当前审阅批次，除非 Owner 后续改变。

展示前采用 practical screening，但**现实筛查只花在生成端已经值得推进的名称上**。

## 2. 直接 Owner 反馈与生成端故障

累计历史原始生成 300 项（001=48、002=36、003=48、004=48、005=48、006=48、007=24），历史记录不改写。

原40项 Owner Review Batch 去掉多词短语后剩16项。Owner 直接反馈已写入 #411 comment `5654581018`：

- 整批整体“不太行”；
- #12 **Morrowrange** 是本批明确正向例外；
- #13 **Elsehorizon** “看起来也还行”；
- 其余整体“不太像名称”；
- 批次级主要问题：词用得太简单、组合太简单，有“小学生想出来的词汇”感。

Owner 随后明确要求先优化**生成方法**，而不是继续增加筛选；并指出此前总结的 Transformation Operators 没有被实际使用。

Owner-positive 名称只允许抽象潜在品质，不得作为 Generator 的词根、后缀、音节、拼写或表面模板。

## 3. 根因与修复

根因已确认：**State Recovery 成功，但 Generation Capability Recovery 失败。**

交付批次恢复了目标、偏好、候选池、筛选计数和 reality 阻塞，但真正生成前没有强制恢复 / 调度：

- Workflow Pattern Scheduler；
- Construction / Operator Scheduler；
- `word-formation-strategies.md`；
- Transformation Operators；
- prior-art 已提炼组件。

DELIVERY-411-005 的 `Each/Common/Else/Many + trace/grain/arc/relay/...` 是直接证据。故障分类：`scheduler_bypass / method_underuse / construction_mode_collapse / generation_capability_recovery_failure`。

“不要恢复 G0–G8 benchmark”只禁止恢复已停止的 benchmark；不禁止使用已经提炼进 Adaptive Naming 的 Lexicon / Catchword / Igor / River+Wolf / Siegel+Gale / NameStormers 方法组件。

## 4. Adaptive Naming Skill 已升级到 v0.4.1

`02_Runtime/02_Tools/adaptive_naming/SKILL.md`

提交：`7e2629a67c90a99b4bdce97b26a16c6a9d093289`

v0.4.1 新增 **Generation Capability Recovery Gate**：

> 任何 `generate` 前必须先恢复生成能力包，并创建 Generation Contract；缺少 workflow patterns 或 construction portfolio 时不得生成。

配套合同：

`02_Runtime/02_Tools/adaptive_naming/references/generation-capability-recovery-contract.md` v0.2  
提交：`6dab4c2811ed1757d9dd2d09b61a2d689a7f24ab`

主要规则：

- ordinary exploration 默认至少3个真正不同的 construction family；
- 换前缀 / 后缀 / 第二普通词不算不同方法；
- Transformation Operators 可用于 exploration + rescue；
- transformation 默认 `strong prototype → bounded transformation`；
- #411 的 simple natural compound 降低预算；
- 纯 sound-led opaque route 因 person/fantasy 风险降权，优先 semantic/morpheme anchor + phonetic engineering；
- generation integrity fail 时停止 reality cost，先修生成。

Focused control regression：

`02_Runtime/02_Tools/adaptive_naming/evals/generation-capability-recovery-regression.yaml`

## 5. 三轮无现实成本的生成回归

### REG-411-GEN-001

`organization-naming-411-generation-regression-001.md`

18项；恢复 lexical transfer、root-derived、telescoping/fusion、bounded transformation、sound-led 五个 family；simple-word matrix 消失。暴露 root/classical 过度学术、sound-led fantasy、弱 seed transformation 问题。

### REG-411-GEN-002

`organization-naming-411-generation-regression-002.md`

加入 Prototype→Transformation、Phonetic Character Brief，并实际调用 Lexicon / Igor / River+Wolf / Catchword / NameStormers 的已提炼组件。结果 pass with routing change；纯 sound-led 当前任务降权。

### Entry Regression 003

`organization-naming-411-generation-entry-regression-003.md`

在 Skill v0.4.1 更新后从生成入口重新执行；Generation Contract 在候选前触发，三个 construction family 可追溯，无 simple compound matrix。**v0.4.1 入口控制通过。**

以上都不是 Owner 质量验收或独立 Reviewer；回归名不计正式候选池，不做 reality 查询。

## 6. 第一批 v0.4.1 真实 production 已启动：DELIVERY-411-008

Raw：

`03_Evolution/01_Research/03_Tests/organization-naming-411-delivery-008.json`  
提交：`befb1a25d7362e334b5109c7b38e89639d0f0271`

18项真实生产候选在 reality 前冻结，Generation Contract 明确使用：

- lexical concept prototype；
- prototype-first transformation；
- morpheme-grounded fusion / derivation。

Intrinsic generation review：

`organization-naming-411-delivery-008-intrinsic-review.md`  
提交：`93302a3311715f35b1ad2c66e28733505f2d7271`

同一 Controller 严格本体审查结果：

- **11 / 18 advance 到 reality-budget consideration**；
- **7 / 18 在任何现实查询前 hold**；
- ordinary simple compound：0 / 18；
- 未触发 scheduler / construction collapse。

这不是“11个 Owner-OK”，只是证明生成端现在能产生值得进一步核查的 material，不再依赖 100→1 的极端筛选漏斗。

## 7. 当前下一动作

只对 DELIVERY-411-008 的 11 个 advance 候选执行**低成本 reality triage**：

1. exact / material identity；
2. exact `.com`；
3. lightweight public trademark signal；
4. 明确 red 立即停止该候选。

若一批 intrinsic strong names 大量现实碰撞，优先使用 Transformation Rescue 保存强原型价值，而不是回到简单重新生成。

仍不恢复大规模100级别 generation；先观察 v0.4.1 首批真实生产的 reality yield。

## 8. 接管规则

后继 Agent 在任何 `generate` 前必须读取：

1. 本 `NAMING_RECOVERY.md`；
2. `02_Runtime/02_Tools/adaptive_naming/SKILL.md`；
3. `references/word-formation-strategies.md`；
4. `references/generation-capability-recovery-contract.md`；
5. 当前任务直接 Owner 反馈 / Name Job 必要上下文。

只恢复状态、不恢复生成能力，不得开始生成。

请示只在三类情况：必须由 Owner 决定的价值 / 战略事项；实质影响目标完成率；对效率有极大影响。普通 method schedule、operator portfolio、内部 regression、Transformation Rescue、可逆修复由 Controller 自主执行。

不要恢复旧 G0–G8 benchmark、Reviewer 校准、SEM-408-006、本地模型测试或成本研究。不要重新初始化 Naming Job。

核心原则：**聊天可以丢上下文，仓库不能丢方法；恢复不仅要知道“做到哪”，还必须知道“怎么做”。**
