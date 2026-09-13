# Naming Recovery

InteropAtlas Naming Workstream 的稳定恢复入口。更换对话或执行者时，Owner 不需要重述历史或管理内部步骤。

## 1. 当前目标与权威规则

第一目标：减少 Owner 总注意力。第二目标：提高真实命名产出效率，而不是靠大规模低质量生成 + 末端筛选补救。

主观质量由 Owner 决定：`喜欢 / OK / 不要` 与自然语言理由就是训练标签，Controller 不另设“真正优秀”标准。

当前母组织 Owner-visible 形态规则：优先单词 / 连写专名；多词短语和短句不进入当前审阅批次，除非 Owner 后续改变。

展示前采用 practical screening，但**现实筛查只花在生成端已经值得推进的名称上**。

## 2. 直接 Owner 反馈与生成端故障

历史 DELIVERY-001~007 累计原始生成 300 项，历史记录不改写。Owner 对旧单词/连写审阅批次的直接反馈：整体“不太行”；Morrowrange 为明确正向例外，Elsehorizon“看起来也还行”；其他整体“不太像名称”，主要问题是词太简单、组合太简单、有“小学生想出来的词汇”感。

Owner 随后明确要求先优化**生成方法**，而不是继续增加筛选；并指出此前总结的 Transformation Operators 没有被实际使用。

Owner-positive 名称只允许抽象潜在品质，不得作为 Generator 的词根、后缀、音节、拼写或表面模板。

## 3. 根因与修复

根因已确认：**State Recovery 成功，但 Generation Capability Recovery 失败。**

近期交付批次恢复了目标、偏好、候选池、筛选计数和 reality 阻塞，但真正生成前没有强制恢复 / 调度 Workflow Pattern Scheduler、Construction / Operator Scheduler、`word-formation-strategies.md`、Transformation Operators 与 prior-art 已提炼组件。

DELIVERY-411-005 的 `Each/Common/Else/Many + trace/grain/arc/relay/...` 是直接证据。故障分类：`scheduler_bypass / method_underuse / construction_mode_collapse / generation_capability_recovery_failure`。

“不要恢复 G0–G8 benchmark”只禁止恢复已停止 benchmark；不禁止使用已提炼进 Adaptive Naming 的 Lexicon / Catchword / Igor / River+Wolf / Siegel+Gale / NameStormers 方法组件。

## 4. Adaptive Naming Skill v0.4.1

`02_Runtime/02_Tools/adaptive_naming/SKILL.md`  
提交：`7e2629a67c90a99b4bdce97b26a16c6a9d093289`

v0.4.1 新增 **Generation Capability Recovery Gate**：任何 `generate` 前必须先恢复生成能力包并创建 Generation Contract；缺少 workflow patterns 或 construction portfolio 时不得生成。

配套合同：

`02_Runtime/02_Tools/adaptive_naming/references/generation-capability-recovery-contract.md` v0.2  
提交：`6dab4c2811ed1757d9dd2d09b61a2d689a7f24ab`

Focused control regression：

`02_Runtime/02_Tools/adaptive_naming/evals/generation-capability-recovery-regression.yaml`

当前规则重点：

- ordinary exploration 默认至少3个真正不同 construction family；
- 换前缀 / 后缀 / 第二普通词不算不同方法；
- Transformation Operators 可用于 exploration + rescue；
- transformation 默认 `strong prototype → bounded transformation`；
- simple natural compound 在 #411 降低预算；
- pure sound-led opaque route 因 person/fantasy 风险降权；
- generation integrity fail 时停止 reality cost，先修生成。

## 5. Generation regressions

三轮无现实成本回归均完成：

- `organization-naming-411-generation-regression-001.md`：恢复 lexical transfer、root-derived、telescoping/fusion、bounded transformation、sound-led 五 family；simple-word matrix 消失。
- `organization-naming-411-generation-regression-002.md`：加入 Prototype→Transformation、Phonetic Character Brief；实际调用 Lexicon / Igor / River+Wolf / Catchword / NameStormers 已提炼组件；pure sound-led 当前任务降权。
- `organization-naming-411-generation-entry-regression-003.md`：从 Skill v0.4.1 入口重新执行，Generation Contract 在候选前触发；入口控制通过。

这些都不是 Owner 质量验收或独立 Reviewer；回归名不计正式候选池。

## 6. 第一批 v0.4.1 真实 production：DELIVERY-411-008

Raw：`organization-naming-411-delivery-008.json`  
提交：`befb1a25d7362e334b5109c7b38e89639d0f0271`

Intrinsic review：`organization-naming-411-delivery-008-intrinsic-review.md`  
提交：`93302a3311715f35b1ad2c66e28733505f2d7271`

结果：18项中11项在本体层面值得 reality budget，7项在任何现实查询前 hold；ordinary simple compound 0/18。

随后对11项做低成本 `.com` 观察：**11/11 exact `.com` 均不可直接注册。** 同时公开搜索对多项发现 material exact identity / adjacent software/organization use。结论不是“方法失败”，而是成熟 lexical/concept surfaces 的现实命名空间高度拥挤。

因此没有回到简单重新生成，而是按 v0.4.1 打开 Transformation Rescue。

## 7. Transformation Rescue 001

Raw：`organization-naming-411-rescue-001.json`  
提交：`e1bdba74ff6ad6c5960e5c71a3e33ebd20ff787e`

选择4个 intrinsic strong、主要受现实占用影响的 prototype：Estuary / Aperture / Perspectra / Recensa。每个最多3次变形；使用 clipping/telescoping、light blend/second anchor、controlled spelling/derivational reshape，总计12项。

Screening：`organization-naming-411-rescue-001-screening.json`  
提交：`c191e677b3332199940fcd714551135f73b5afa2`

结果：

- 12项全部批量检查 exact `.com`；
- 3项 direct `.com` available；
- 9项 unavailable 后直接 hold，不查 aftermarket；
- 3项才进入现实身份 follow-up；
- Perscopia：存在历史软件 command exact token，当前 set aside；
- Recenara：是葡萄牙语已有动词变位，当前 hold；
- **Recenvia：当前唯一 internal survivor**；exact web query 未见 substantiated active company/app/software/trademark identity，`.com` 可直接注册；仍不是 Owner-ready 或法律 clearance。

Rescue 001 说明：Transformation Rescue 能提高命名空间存活率，但不是万能。原11项 direct `.com` 为0/11；第一支 rescue 变体为3/12 direct available，最终1项在轻量 follow-up 后内部保留。真正的收益是保存高质量原型价值，而不是重新从简单词开始。

## 8. 当前状态与下一动作

### RESCUE-411-002：低收益，未复现干净 survivor

第二支 bounded Transformation Rescue 已使用不同 strong seeds 完成：

- Raw：`organization-naming-411-rescue-002.json`
- Screening：`organization-naming-411-rescue-002-screening.json`
- 提交：`d4b218be68275d09e8079ec37d718c9ff9693e81`、`4bfdb0b04507126afb9730aecc6f974f06ef5d4c`

8项全部完成 Verisign `.com` authoritative RDAP 观察：7项 registered，1项 authoritative 404 object-not-found。唯一 direct-available 变体在 Level-2 近似身份 / 恢复性检查中被 `Praxis` 高邻接身份簇与 `per axis` 分词风险击中，最终0项 internal survivor。

结论：第一支 rescue 的1个 preliminary survivor 没有在第二支复现。Generation integrity 通过，因此不是 scheduler bypass；诊断为 `rescue_low_yield / mature_semantic_surface_namespace_crowding / near_identity_recoverability_failure`。同类 RESCUE-003 已停止。

### Territory Reset 001 + DELIVERY-411-009

没有加严末端筛选，而是按 v0.4.1 条件分支切换 territory/material/operator：

- Territory Research：`organization-naming-411-territory-reset-001.md`
- Raw + intrinsic review：`organization-naming-411-delivery-009.json`
- Screening：`organization-naming-411-delivery-009-screening.json`
- 提交：`a6e5e2d1f1b1e1eb5167ec22945125ae405a7f8b`、`61da85f503ccbd2ff1b304864bbd9ad1ed4cc3a7`、`f6094266e92cb3bfa5a8f0158aebc697e48d85b8`

新材料来自生态交界、河道分合、commonplace / marginalia 与 spolia。9项中7项通过 generation-side intrinsic advance，说明 concrete structural material 改善了本体产出；但7项 `.com` 仍只有1项 direct available，且因明显个人姓名分词被 set aside。其余强项中：

- 一个透明 aftermarket `.com` 报价为 USD 2,888（最低 offer USD 1,888），但存在历史相邻 B2B technology exact identity 与高度拥挤 near identity，未推进；
- 一项发现 exact pharmaceutical company identity，停止；
- 其他 registered 项未因域名存在就反向提高质量或盲查 aftermarket。

当前仍为0 Owner-visible 新候选；既有 preliminary internal survivor 继续只内部保留，不展示。

### 当前 next_action

下一步不恢复 G0–G8，不扩大量，不重开同 seed rescue：

1. 开一个 **6–9项 morpheme-grounded / more-opaque proper-name micro-probe**，回答能否在保持真实 semantic lineage 的同时摆脱成熟 lexical surface 拥挤；
2. Generation Contract 必须使用改变后的 consonant / stress portfolio，并显式设置 personal-name、fantasy、biotech、generic-tech post-filter；先 intrinsic，后 reality；
3. reality 中把 `direct registration` 与 `transparent realistic aftermarket` 分成两条 feasibility channel；只有本体真正强且 identity 先通过的 registered 名称才允许查价格；
4. 若该 micro-probe 仍为0个 realistically feasible survivor，停止静默生成，并把“名称质量 ↔ exact .com aftermarket budget”作为实质预算边界交给 Owner 判断。

当前 biggest unknown：**更隐性的、morpheme-grounded proper-name construction 能否同时提高名称完整性、非个人读感和现实命名空间存活率；若不能，是否需要为更强名称接受明确的二级市场预算。**

## 9. 接管规则

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
