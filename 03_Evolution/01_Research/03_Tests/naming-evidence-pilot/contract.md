# 命名留痕试行合同 v0.1

状态：#411 任务内试行；尚未晋升为稳定 Skill。主入口为当前任务 state 的 evidence_pilot 字段。本目录保存可重复的验证资产，不是新的任务事实源。

## 何时使用

在新批次进入用户展示前，以及更新持久状态前检查。仅研究、证据修复和已暂停任务允许保留未知；未知必须影响就绪判断，不能伪装成完整。历史重建不得回填原始执行。

## 批次最小记录

采用 JSON；实际原始内容可内嵌，或由可解析产物 ID 引用。每项 artifact 保存 id、kind（original / reported / reconstructed / synthetic）、text。外部原文应摘录必要片段并带 source_url 或 commit/path；不要求保存隐藏思维链。

本地当次执行产生的内嵌原文使用 origin: local_execution 与 execution_ref（可追踪的运行/工具调用/会话记录标识），不要求伪造外部 URL。外部原文或来源未分类的 original 必须有 URL 或 commit/path。标识存在不证明来源真实，人工审查仍需回取核对。

- batch_id、purpose（exploration / exploitation / validation）、method_ref、runtime 与阶段。
- inputs、outputs：实际使用的输入和原始输出产物 ID。运行环境限制如实记录；保存简报不等于证明隔离。
- stages：按 generated、intrinsic、reality、exposed 保存候选 ID 集合。每个丢弃项对应 from/to/candidate_id/reason；救援或新变形使用新批次与 ID。
- feedback：source_artifact、quote、interpretation、basis（direct_reason / inference / reported）、role（prefer / gate）、gate_authorization_quote。排序反馈不自动成为原因；历史转述保持 reported。gate 必须有用户明确授权原句，解释是否忠实仍由语义审查判断。
- screenings：candidate_id、claim、observed_at、queries；每项查询有 intent、source、result。availability 声明至少含 identity、public_tm、domain 三种查询意图；这只是结构下限，不替代现有 Reality Screening Contract。
- batch_review：各阶段形态变化观察、原因假设、证据引用与探索目的。校验器不按固定类数拒绝同族探索；语义审查负责判断分类和集中是否合理。

batch_review 使用 stage_observations、assessment、evidence_refs；assessment 写原因假设或明确原因未知，探索目的复用 batch.purpose。screenings.claim 必须明确；unknown / not_assessed / error 可如实保存，但产生未完成缺口。

## 状态更新合同

recovery 对 mission_value_model、name_job_model、search_landscape、scheduler_state、generation_runtime_evidence、candidate_reality_evidence_links 分别记录 status。present 必须有非空 value；referenced 必须有 commit（40位SHA）、path 和 section；unknown 必须说明 reason 并阻止恢复生成。旧状态已有条目，新状态不能静默丢失。

## 校验器边界

validate_evidence.py 检查引用存在、阶段集合与去留记录、原始证据类型、反馈字段分离、筛查记录下限、恢复条目和状态迁移。输出 errors、gaps、capture_complete。即使 capture_complete=true，也不是候选质量、语义忠实、域名可用、商标可注册或生成许可的证明；用户暂停始终优先。

命令：python validate_evidence.py record.json [--previous old-record.json]。有结构错误返回1；无结构错误但不完整返回2；记录结构完整返回0。不会联网、生成名字或写外部状态。

运行合成测试：python test_evidence.py。样例只是匿名 ID 和明确标注的合成材料，不计入 #411 候选。结果应记录实际执行输出。跨任务晋升、生成效果与用户效率仍需另外验证。
