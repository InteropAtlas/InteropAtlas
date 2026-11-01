# Prior Art → Adaptive Naming 采用图 v0.4.0

本文件回答：哪些能力直接采用、哪些经过改造、哪些属于 InteropAtlas 的综合 / Agent-native extension。详细证据仍以 Naming Research #407 / #408 与历史 Method Profiles 为准。

## 1. 从“方法来源”到“可组合机制”

v0.4 不把 G1–G8 当作必须完整执行的八条流程，而是拆成两类可调度资源：

- **Workflow Patterns**：怎么组织认知、研究、生成、评价与反馈；
- **Construction Operators**：名字具体怎么形成。

Controller 根据当前 diagnosis 组合机制，这一组合本身才是 IA 自己的方法。

| 来源 | 直接采用 / 保留 | 在 Adaptive Naming 中的改造 |
| --- | --- | --- |
| Lexicon / G1 | 先明确名称要完成的工作；Creative Framework；Creative 与 Linguistic Engineering 并行；高价值决策降低锚定 | Mission / Value → Name Job → Decision Criteria；抽取 `creative_linguistic_parallel` pattern；Decision Hygiene；Linguistic Engineering 可按需独立 Worker |
| Catchword / G2 | Discovery / Brief；Project Vocabulary / Territories；high-volume divergence；shortlist；现实与语言文化筛查 | Territory Research；`territory_expansion` / `divergence_burst` patterns；Validation Contract；high-volume 不再固定，而成为可调 search cadence |
| Igor / G3 | Positioning；竞争命名空间、taxonomy、white space 前置；contextual presentation | `white_space_mapping` pattern；Search Landscape 作为 prior map，并由 G8 online evidence 持续更新 |
| River + Wolf / G4 | Character / Communication / Construction / Continuum；参数变化改变输出 | Communication 拆为 Name Job / Communication Load；Construction 进入 operator scheduler；Character / Continuum 进入按需 Expression Profile |
| Siegel+Gale / G5 | 多 naming category 并行；contextual evaluation；警惕 voting / consensus；陌生名字需要消化 | `category_parallel` pattern；Decision Hygiene；Temporal Evaluation；不以简单投票代替质量判断 |
| Tungsten / G6 | Pivot Point；evergreen umbrella；brand architecture extensibility；criteria priority | Name Job / Value Model 吸收 enduring logic；`architecture_stress` pattern；Decision Criteria roles |
| NameStormers / G7 | Lightning / Brainstorm；Pitch in context；Feedback / Test；Refinement | `feedback_refinement` 与 bounded `divergence_burst` patterns；Owner 只在高信息节点参与；feedback 结构化回流到新 context |
| IA G0 | 低约束创造、叠字、拼词、词根、新造词、word + letter 等实战构词路线 | 汇入 Construction Operator toolbox；部分 operator 可进入 bounded Transformation Rescue |
| IA G8 | region-first；现实观察；状态更新；explore/exploit；move/stay；隔离 raw survivor 信号 | `online_observe_update` 作为核心 pattern；与 G3 合并成 Search Landscape = prior map + online learning；Reality feedback 仍不得直喂 Generator |
| SkillMedev Brand Naming | criteria-before-generation；多维评价不压成总分；语言 / 记忆 / 语境检查 | intrinsic / value / reality 三轨；Decision Criteria 标 gate / optimize / prefer / observe + provenance |
| Brand Naming Studio | `SKILL.md + references + templates/scripts`；按需读取 | Progressive Disclosure；薄 Controller；复杂能力按 trigger 加载 |
| fcoury Brand Naming | 竞争地图、利益 / 意义探索、词源、隐喻、相邻领域、声音生成 | Territory Research + Search Landscape；研究材料与候选生成隔离 |
| Quaere Naming | 工具验证现实可用性；不足时回退；blocked 不猜测 | Reality Screening Contract；reality 不冒充 intrinsic quality；强原型可 bounded Rescue |
| VeyraLabs Naming Suite / modular skill patterns | 地图、生成、审计等能力可模块化 | 不拆成大量固定 Skill；用 Controller + workflow patterns + optional workers + Runtime Adapter |
| self-improving skill patterns | 错误 / 人类反馈 / 更好做法可积累并改进 Skill | 分成 per-job experience 与 Cross-task Experience Registry；method hypothesis 经 evidence + regression 才可 promote |

## 2. IA 自己的核心综合

Adaptive Naming v0.4 的核心不是上述任一单独方法，而是以下组合：

1. **Mission / Value → Name Job → Decision Criteria**：把上游战略理解显式化；
2. **Search Landscape = G3 prior map + G8 online learning**；
3. **Workflow Pattern Scheduler + Construction Operator Scheduler**：方法组织与造词手段分离；
4. **Search Cadence 自适应**：micro probe、portfolio、divergence burst、focused exploitation、validation only；
5. **Quality / Value / Reality 分轨**；
6. **Controller-only exclusions + positive brief + post-filter + truthful isolation**；
7. **Runtime Adapter**：逻辑角色与实际单对话 / fresh context / sub-agent / shell 环境解耦；
8. **Method Evolution Outer Loop**：experience → registry → hypothesis → counterevidence → regression → promote/reject/supersede。

这些机制共同构成 IA 自己的 Agent-native Naming Method，而不是“选出 G1–G8 里的赢家”。

## 3. 公开 prior art 与隐性工作的边界

公开方法经常只披露阶段、原则和客户可见 deliverables，真实内部 SOP 可能包含更多 tacit work。没有证据时不得把推断写成某家公司的既定流程。

- 多家公开线索支持 → `research synthesis`；
- 单家公开明确机制 → 标明来源，不擅自补内部阈值；
- 合理但未披露的专业隐性工作 → `Agent-native operationalization / hypothesis`；
- IA 在真实任务中发现的控制故障 → `live-fit evidence`；
- 单次任务经验 → 先进入 Experience Registry，不自动升级通用规则。

## 4. “进化”不等于自由改写

系统可以自主提出 method hypothesis，但稳定方法升级需要：

- 跨任务一致证据，或严重控制缺陷例外；
- counterevidence 检查；
- regression；
- version / provenance；
- rollback 或 supersede 路径。

因此目标是 **controlled self-evolution（受控自我进化）**，不是 uncontrolled self-modification。
