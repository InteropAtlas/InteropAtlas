# 命名留痕试行合同 v0.1

> **v89 当前路由**：方法重构与低成本模型适配从[模型与预算感知实验入口](model-aware/README.md)进入；配置和运行协议在该目录。旧Skill和本合同v0.1/v0.2章节保留为历史兼容与证据工具，不作为新实验的完整默认流程。当前不继续旧IA候选生成。
>
> 当前授权、记录完整性、候选核查与方法验证在state的`model_aware_rebuild`分别表达。本地优先、付费上限0；未绑定实际部署时不声称已支持Qwen。新协议只编译任务包/检查声明/登记回执，无模型或网络调用。真实模型比较、独立语义评审和跨任务效果均未执行。
>
> 本轮仅经批准扩展独立实验路由，未放宽旧候选的展示或采用门槛；方向校准与候选推荐严格分开。不要将旧修复模式的限制当成所有未来方法的固有规则，也不要绕过它修改原历史事实。

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


## v0.2 任务内操作入口：可执行防线，不是稳定 Skill

从 v87 起，更新状态使用 `control_gate.py state`，整理批次记录使用 `control_gate.py record --operation audit`，拟展示前使用 `--operation expose`。旧 `validate_evidence.py` 保持原字节，仍用于历史记录结构兼容；不能把旧校验器单独通过当作新展示许可。

```bash
P=03_Evolution/01_Research/03_Tests/naming-evidence-pilot
# 先检查候选状态；审计可保留已明确列出的未知，不允许无来源清空未知。
python "$P/control_gate.py" state /tmp/proposed-state.yaml --previous /tmp/current-state.yaml --repository .
# 本地应用前重复校验并比较旧字节；锁内原子替换。GitHub提交仍需旧blob校验。
python "$P/control_gate.py" state /tmp/proposed-state.yaml --previous /tmp/current-state.yaml --repository . --write-to 03_Evolution/01_Research/03_Tests/organization-naming-411-state.yaml
# 展示前检查；该命令不展示、不生成，也不进行外部查询。
python "$P/control_gate.py" record /tmp/batch.json --operation expose --repository .
python "$P/test_controls.py" --repository . --output /tmp/control-results.json
```

输出 `block` 表示矛盾/无效/越权；`review` 表示缺口或语义风险须处理；`pass` 仅表示本组结构条件通过。记录命令退出码分别1/2/0。状态审计允许保留旧未知，此时 `write_allowed=true`、退出码0，但 `generation_ready=false` 不变。CLI不会联网或输出真实名称。写入口只保护使用该入口且尊重文件锁的本地写入；任意绕过入口的修改不是它能物理阻止的。GitHub分支CI提供自动发现，未配置required check，不能宣称服务器已强制拦截所有直写。

新增记录字段仅为完成这些检查所需：

- `feedback.observation_type` 区分 ranking / explicit_reason / explicit_constraint；`claim_type` 区分 ranking / reason / constraint。排序后的原因解释必须是 inference + interpretation_status:hypothesis；硬约束不能靠复用排序原句取得授权。
- `candidate_features` 以候选ID映射 `form_family`、`evidence_ref`、`classification_status`。这些标签需要实际依据与语义审查，程序不会证明分类正确。缺分类时暂缓，不臆测多样性。
- 查询记录保留 `evidence_ref` 指向实际产物和 `outcome`（clear / blocked / unknown）；无原始材料或结果未解决不用于放行，时间必须可解析且带时区。可解析时间不证明查询真的发生或仍然新鲜。
- 产物可带sha256；本地原始产物还应带file，程序核对范围内文件字节。外部URL未回取只进入待复核，不自动视为真实来源。
- `focus_contract` 为有意同族探索记录输入出处及原句、form_family、正整数budget、rationale、exit_condition。仅声明exploitation不足以获得例外。全部同形的多项展示触发复核，不按固定五类或固定比例宣布坏名字；预算内且有输入合同的同族探索可通过结构检查。

各阶段的集中观察由候选集合和已声明分类计算。`first_recorded_concentration_stage` 仅定位最早记录到集中的阶段，**不是失败原因**；阶段资料缺失时不允许归因于生成。`semantic_and_reality_clearance` 永远为not_assessed。

状态维护模式保持当前任务、商业门槛、偏好、候选、使命模型和名称职责；旧字段可以迁移为可回取且内容等效的精确引用，不能用任意非空对象代替。真正修改这些内容需要另行带证据的变更审查，不通过本轮repair-only入口偷偷完成。

<a id="live-trial"></a>

## 真实试行准备与恢复条件

当前只有工具与程序防线完成，真实名称生成仍暂停。授权恢复后，不需 Owner 逐步批准内部技术动作：先冻结一个当次计划（任务内建议内部最多8项，不是永久方法配额）；将历史未知与新的计划/实际执行严格分开；根据真实可用能力选择隔离方式；保存实际输入、原始输出、每次筛选和反馈；展示前运行结构防线并作语义及现实证据复核；任一重要缺口或矛盾未解决即不展示、不扩大批次。

真实试行验收分别看：过程是否忠实、错误是否复发、候选是否有用、Owner判断成本与留痕成本。程序测试不替代这些结果；没有独立评审时必须标同一执行者审读。没有必要为每个技术步骤再次询问 Owner，但恢复生成、实际购买/注册、最终名称采用和稳定方法晋升不能从修复授权自动推导。
