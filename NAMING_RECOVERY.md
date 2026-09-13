# Naming Recovery

InteropAtlas Naming Workstream 的稳定单一恢复入口。更换对话或执行者时，Owner不需要重述历史或管理内部步骤。

## 1. 当前目标与优先级

**第一目标：减少 Owner 为完成任务付出的总注意力。第二目标：尽快形成足够大的及格候选池。达到及格后，再提高优秀程度、效率与降低成本。** 当前主线仍使用既有复杂命名系统；Simple 不替代主线。

当前执行目标仍是：形成几十个经过实际筛选、可供 Owner 集中判断的名称；40 个待审名称／累计 30 个 Owner-OK 是 Agent 对“几十个”的执行化，不是 Owner 原话数字或已达成结果。

Owner 已授权**时间／深度再平衡**：保留既有筛选类别，但不把每个草案都做成近乎 finalist 级尽调。整体节奏和候选供给优先，筛查深度由 Controller 根据候选价值、风险信号和时间成本自适应控制。不能因为“还可以继续查”就无限加深，也不能为了速度完全不查。

## 2. 当前筛查分层

### A. 内部大池：快速生成与本体淘汰

优先扩大候选空间。先检查组织尺度、语义／身份质量、明显读音／拼写问题、跨语言负担、视觉轮廓软偏好和批次同质化。明显不合格者直接内部退出；不为它们做昂贵现实查询。

### B. Owner Exposure 前：全类别覆盖，但采用实用初筛深度

准备展示的候选必须覆盖：

- exact／明显 near identity；
- exact `.com` 的直接注册状态或明显取得障碍；
- 商标风险的**初步公共查询**；
- 语言、组织尺度、批次差异性复核。

这里的“筛完”是**足够支持审美比较的 practical screening complete**，不是四辖区逐库穷尽、律师级 clearance 或每个名字都出专业报告。商标使用正常可访问的官方／可信公共来源做合理查询；无明显 material signal、并记录查询范围与不确定性，可标 `preliminary_pass_with_uncertainty`。不得写“法律可注册／绝对无冲突”。

若查询通道反复超时、登录、验证码或自动化不稳定，边际收益很低，则停止无限重试，换来源或保留不确定性。只有出现具体高风险 lead，才继续深挖后决定是否进入展示池。

### C. Owner 认可后：把深度尽调集中到高价值候选

Owner 标记 OK／喜欢或进入 finalist 后，再做更深的近似身份、美国／欧盟／中国／WIPO-Madrid 商标核查、域名取得路径和必要的专业数据库／法律意见。

**这不是把筛选后移给 Owner。** 展示前仍完成所有筛选类别；变化的是深度和时间预算，不把明显风险或原始待查项直接交给 Owner。

## 3. 时间复盘与节奏判断

已有留痕显示筛查深度曾明显失衡：第一池只为一个候选验证商标访问，5 个浏览器任务的 provider-reported duration 合计约 4317 秒（约 72 分钟），仍没有完成四范围候选级商标结论。这类投入不再作为普通候选默认成本。

节奏原则：

1. **先增加候选供给，再按价值逐级增加筛查成本。**
2. 普通候选出现明确 red signal，立即停止后续昂贵检查；没有明显风险时，达到实用初筛证据后停止继续深挖。
3. `.com` 不可直接注册时，普通候选先 hold，不立即研究 aftermarket；只有本体质量足够强再投入取得路径调查。
4. Markify／Questel 继续作为效率选项，但不再是交付前硬依赖；已发询价保留，收到回复再判断。
5. 不恢复模型 benchmark、Reviewer 校准、通用 gate 研究或降本实验。

## 4. 当前断点

**累计原始生成 132 项：001 = 48、002 = 36、003 = 48。** 尚未正式展示新一批候选，也没有把原始生成数冒充 Owner-ready 数量。

第三池已按新节奏推进：

- 冻结原始48项：`organization-naming-411-delivery-003.json`，commit `e4ade16e72245331912f0799f0e37aecedd044b6`。
- 实际 candidate flag 进入快速现实筛查35项（原始文件 counts 写34是算术元数据错误；候选行未改写，筛查记录已显式纠正）。
- 14项因明显现实 exact/material identity 直接退出当前交付路径，不再继续商标深查。
- 21项进入 `.com` 快速检查；其中 only `eachfold.com` 与 `anewfold.com` 可直接注册。
- Anewfold 随后发现活跃的巴西设计／软件公司与 Studio Anewfold，退出当前路径。
- Eachfold 当前为 `preliminary_pass_with_uncertainty`：快速 exact identity 查询未见实质同名组织／软件；`.com` 可直接注册；轻量公共商标方向搜索未发现实质候选记录。它**不是法律 clearance，也尚未单独向 Owner 展示**。
- 第三池筛查记录：`organization-naming-411-delivery-003-screening.json`，commit `4a7e6e71934bc9cd7e91b29a90493ffa9e364d01`。

第一、第二池历史结果继续保留，不因节奏调整重写。按需读取：

- `03_Evolution/01_Research/03_Tests/organization-naming-411-owner-preferences.zh-CN.md`
- `organization-naming-411-delivery-001*.json`
- `organization-naming-411-delivery-002*.json`
- `organization-naming-411-delivery-003*.json`

Markify 询价已获 Owner 授权并发送；目前只收到自动工单确认 #431418，尚无人工报价／试用开通。无需等待回复暂停候选工作，也不自动购买或开户。

**下一主动作：继续扩大候选池，并用同样的快速分层筛查积累 practical-screened 候选；不为普通草案做四辖区深度商标尽调。** 当 practical-screened 候选数量足以形成有意义的整批比较时，再集中交付 Owner。

## 5. 自主执行、请示与接管

每个小单元完成或中断即写入已有 Primary Home：完成内容、候选／筛选真实计数、未完成项、下一动作和阻塞。内部小步不等于每步向 Owner 请示，也不等于零碎展示名字。

只有三类事项升级：必须由 Owner 决定的价值／战略事项；实质影响目标完成率的事项；对效率有极大影响的事项。请示带依据、影响、推荐方案和最小决策问题；已回答内容不重问。

普通淘汰、低保留率、查询来源切换、筛查深度控制和可逆局部修复由 Controller 自主处理。后继 Agent 沿本入口恢复，不需要重跑旧实验、重新连接已连接工具或重新初始化 Naming Job。
