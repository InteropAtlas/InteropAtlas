# SEM-408-003：日志恢复与语义有效性审计（v96）

## 1. 实际执行与可恢复证据

Primary Home：#408；#411 真实组织命名仍暂停，#416 保持 Draft。执行者：OpenAI / ChatGPT / GPT-6 Astra Pro。审计类别：读取原始日志后的 Controller 事后分析，不是新增独立盲评。

原运行 `34737301186` / job `103670853467` 在 2026-09-13 06:20:36 UTC 开始，06:27:44 UTC 结束。源码冻结在 `3b2144413d938bde7cfe1772ec60efd635365e2d`。运行已结束，不再是 queued；六个独立请求均在日志中留下 `review_complete_not_truth` 记录。原日志内六项均为 hold、brief_fit 均 weak；这些是模型输出，不是审计认可的质量标签。

失败发生在后续归档：`AssertionError: branch changed during frozen run`。分支推进保护有效阻止了旧源码基线上的写回；缺陷是此前没有独立 artifact 备份，归档把来源 commit 与投递时 branch head 耦合。原运行 artifacts API 返回 0。本轮保留完整可下载 job log、运行/job/artifact 元数据快照及按行派生的六项记录；不重跑模型，不把后补记录伪装成原 runner workspace。

记录入口：`results/recovery-run-34737301186/recovery.json`；原始留存日志：同目录 `job.log`；重算程序：`recover.py`。日志 SHA256、记录所在行号和原 logged_at 均在 recovery.json；原HTTP响应、渲染后的实际token请求、server.log、plan内GGUF hash等没有从此次运行恢复。可确认声明的模型/固定代码与实际输出，不可补填为逐字完整请求或已核实权重哈希。

## 2. 为什么不能进行可信的跨模型质量比较

下列判断是可复核的 Controller 解释，原文不修改：

| 既有候选ID | 日志中的问题 | 审计意义 |
| --- | --- | --- |
| C001 | 用名称不具备 inherent analytical value 解释弱匹配 | 可能把产品能力当作裸名必须自身具备的属性，违反本次明确的非字面编码边界 |
| C002 | 把 frozen brief、validation 写进名称观察/联想，进而评价 fragmented system | 混淆任务说明、命名对象与候选词形 |
| C003 | 理由为 “It’s a name, not a tool.” | 以“名称不是工具”否定命名，构成任务层级错误 |
| C004 | 用 lacks inherent product features 解释弱匹配；多个联想夹在一个带列表残片的字符串中 | 结构可解析不等于语义或内容表示正确 |
| C005 | 联想含 “a specific type ofal”，其余包含笼统好评 | 联想与理由缺少可依赖的候选级依据，不据此认定名称好或坏 |
| C006 | 观察和最终理由都只是名称包含自身 | 通过包含名称的字符串门槛，仍然是循环陈述 |

`substantive()` 只检查禁用占位短语、包含候选名和字符串长度，能让上述循环陈述通过。因此本轮不能把“canary_passed / review_complete_not_truth”升级为“独立语义验证通过”。这不是以六项都 hold 本身判定失败；依据是具体理由与任务要求的错位。也不据此泛化为 Gemma 家族或所有小模型无效。

Gemma 使用单候选裸名；Qwen-v95 使用批量候选和生成者意图等不同输入。即便未来 reviewer 有效，差异也不能只归因于模型家族。当前不计算名称质量胜率、不让这六项覆盖 Qwen 的 priority/hold、不选择 winner，也不让 ChatGPT 变成隐藏运行时兜底。

## 3. 已完成修复与下一步

恢复采用先写本地证据、再独立上传 artifact、最后受保护投递的顺序。投递使用最新父提交，但要求目标 state 的 blob 与预期相同、新证据路径不存在；不 force、不覆盖别人的新 state。若分支竞争发生，公开 artifact 仍保留，不能为了让任务变绿而改写历史或自动重跑模型。

state 只将 snapshot95 更新为96、替换过时 next_action 并追加本轮来源/限制，其余使命、偏好、候选、Skill v0.4.0、历史计数和实验原判定保留。NAMING_RECOVERY.md 的稳定路径不变，不重复维护第二套状态。

下一动作：先用既有材料冻结一个最小“任务理解”对照，检查 reviewer 是否在评价名称而不是要求名称本身实现产品功能；明确可接受依据、任务错位与循环陈述的停止条件，然后才决定单项真实 canary。不是继续加 selector 规则，也不是立刻再跑六项。当前无新增名称、无新增模型调用、无付费推理API、无现实查询/购买注册、无IA/G0–G8恢复、无合并或稳定晋升。
