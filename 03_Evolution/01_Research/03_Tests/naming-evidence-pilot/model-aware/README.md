# 模型与预算感知命名 · 实验入口 v0.1

状态：v91 已增加连续开发工作流；真实模型尚未接入。不是稳定 Skill，不是模型能力或命名效果已通过验证。方法研究归 #408，实际组织命名归 #411；当前任务状态仍只有一个来源：上级的 `organization-naming-411-state.yaml`。

授权：[本轮记录](https://github.com/InteropAtlas/InteropAtlas/issues/408#issuecomment-5644664522)。执行者：OpenAI / ChatGPT / GPT-6 Astra Pro。用户要求先重构并判断方法是否有用，不继续旧候选主线。本轮只实现协议、配置、离线任务包及确定性测试；无模型调用、无新名称、无现实查询、无付款或方法晋升。

## 1. 两个结果，分别验收

名称交付：负责人明确愿意采用，并完成约定的现实核查与实际取得条件。准备2–3项只是决策辅助，不为凑数保留弱候选。对象按Owner最新描述为IA之上的上上层长期组织；不把它改成IA项目或互操作性工具品牌，也不自行发明中间组织层。

方法交付：在至少一种实际可负担的本地或低成本配置上，与强而简洁的基线比较，报告有效产出、成本、误杀和适用范围。未实测的配置标为未验证；大参数、高价格或通用榜单不是本任务能力证明。

现有v0.4.0冻结在提交 `64b973c5c21e4a13accbbf79bf5ad619996f8dcb`，并保留原字节；它可作B组对照，不能被悄悄改成弱基线。G0–G8不恢复。本目录不是新命名任务，也不覆盖历史证据。

## 2. 默认小核心

**理解与校准 → 独立提案 → 独立选择与误杀抽查 → 分级核查/负责人反馈 → 使用判断。**

简报由已有来源整理：命名对象/用途、使命与名称职责、明确约束、偏好证据与未知。不要求Owner重复讲使命；只集中校准会改变身份理解的差异。Owner长期认同是交付目标，不只作同分决胜项；未经证实的“偏好原因”才应降权。原话、选择倾向、执行者假设分别保存。

提案默认少数互相隔离的上下文，差异来自身份理解/材料/语义关系，不靠细分构词标签凑多样性。独立不要求同时运行；同一模型不同上下文仍是同源，不宣称统计独立或无共同偏差。没有独立环境时，记录顺序自审，不能叫独立Reviewer。

选择先看名称、后看等长简短解释；解释不自然或可随意互换不算独特适配证据。允许不确定、并列和分歧。每轮按预先规则抽查淘汰项，包含边界样本与随机样本；抽查不自动重新放行。共享候选池的选择实验单独记录，不和生成能力混在一起。

方向校准默认只用身份与表达方向，不展示未经筛查的拟采用名称。诊断材料如确有必要，须单独授权并明确不是推荐。候选讨论需相应初筛；最终采用需约定的详细核查。沿用#411的.com实际可取得、商标前景要求和.org次要用途；不把已注册等同永不可得，不假设收购预算。事实必须来自工具或原始来源。

复杂搜索地图、多层调度和跨任务自我演化暂不作为默认必需项。确定性程序保留版本、去重、实际输入输出与来源；语言模型只处理当前有价值的认知任务。

## 3. 能力与成本是配置，不是模型等级神话

[experiment.json](experiment.json)保留三种运行模式：`local_only`、`hybrid`、`reference`。默认本地优先且云端预算与升级调用数均为0。没有云端额度时禁止自动升级或暗中重试；可有界继续本地工作、集中报告不确定性，不要求购买会员才能使用流程。

每个运行配置记录精确deployment ID、权重/版本、量化、框架版本、上下文上限、输入计数器、输出上限、推理模式、采样配置和逐角色实测状态。生成、选择、事实整理的能力分别判断。未校准角色可以在明确授权的诊断实验中测试，不可因此标为已支持生产。

用户举例 `qwen3.6-30b-a3b` 仅保存为原始写法，当前部署身份未解析；本轮不自动换成相邻型号。参数标签不用于能力或硬件可运行性结论。未连接目标本地推理服务，未下载任何权重。

单任务包只包含确认后的简报、当前问题、允许使用的材料、输出合同及停止条件。控制者历史候选、失败样例、排名、排除表不得随整个state灌入生成包。任务包采用字段白名单，但自然语言中是否夹带偏好锚点仍需审读；编译成功不等于隔离成功。

强模型可用于理解、生成或复核，不能先验规定只负责最后审核。后续诊断可比较“本地/本地、本地/参考、参考/本地、参考/参考”；生成池中没有的好候选不能靠评审创造。升级只响应已定义的失败/矛盾/敏感性信号或预先随机抽查，不只相信模型自报信心。

## 4. 最小方法×模型实验

同一冻结简报和反馈分别给A简洁基线、B原v0.4.0、C本重构，在本地与参考配置上比较。核心2×2为A/C×本地/参考；B在相同任务/预算条件下作为扩展对照。混合角色比较与校准信息的增益单独开展，不偷偷给C更多信息。

先开发、后留出：配置预留2个开发任务、4个留出任务，每格2次运行。它们只是未绑定任务槽位，不是已经有真实负责人或真实数据。先用核心矩阵进行开发试验；确认公平性与资源可行后再启用扩展B组和留出阶段，不机械耗尽全部组合。该数量是探索设计，不是充分功效保证。

任务是统计比较单位，候选不是独立重复实验。评审隐藏方法来源和生成者排名；随机化执行/显示顺序，同时保存随机种子。同一负责人不能遗忘前次曝光，重复任务的污染需记录；优先独立任务负责人或平衡顺序。隔离运行与独立语义审查分开声明。

记录全部失败、超预算和未完成核查。采用意愿、核查完成、实际采用分别报告；模拟任务没有真实负责人时不得报告采用成功。记录开发费、每任务准备费、模型/工具费、本地时长、人工分钟与未知项。不得把成功样本的平均成本当全流程成本，也不把API费用0称总成本0。

若C没有明确收益证据，默认选简单流程作为工程决定，不将“不确定”写成“等效已证明”。只有某类型有效就限定适用范围；先比较完整方案，再针对最可能有效的组件做一次删减对照。不得把本地模型换成更强模型又把收益全算给方法。

## 5. 四个独立状态

- `authorization`：当前可做什么；最新暂停优先，程序不能授予权限。
- `evidence`：本次材料是否留全；原始、重建、合成分开。
- `screening`：各候选核查阶段、未解决和冲突；完整记录允许得到“不合格”。
- `validation`：工程测试/本地实测/独立语义审查/跨任务效果，分别记录。

当前#411的旧process_review/audit_recovery属于兼容历史层，不再通过例外注释解释当前权限；新增`model_aware_rebuild`明确路由本轮动作。新证据不补过去，历史缺口不自动污染新任务。真正依赖未知的动作仍须等待该证据。

## 6. 已实现工具和真实边界

`protocol.py`只在本地编译单任务包、检查投递条件、登记运行回执和汇总；**不会调用模型，不联网，不启动工作者，不自动执行收费或仓库写入**。这是可接入本地运行器的协议，不是完整模型Adapter。v90新增的本地执行端见第8节；离线协议本身仍不联网。真实模型效果与独立复核仍未验证。

```bash
P=03_Evolution/01_Research/03_Tests/naming-evidence-pilot/model-aware
python "$P/protocol.py" matrix --config "$P/experiment.json" --output /tmp/matrix.json
python "$P/protocol.py" packet --config "$P/experiment.json" --task /tmp/task.json --profile local --method redesign --role generate --output /tmp/packet.json
python "$P/protocol.py" preflight --config "$P/experiment.json" --packet /tmp/packet.json --usage /tmp/usage.json
python "$P/protocol.py" capture --packet /tmp/packet.json --response /tmp/raw-output.txt --receipt /tmp/receipt.json --output /tmp/run.json
python "$P/protocol.py" summarize /tmp/run.json
python "$P/test_protocol.py" --output /tmp/model-aware-tests.json
```

`task.json`合同：`id`、`record_kind`（real/synthetic）、`brief`（仅object/mission/name_jobs/non_jobs/constraints/confirmed_preferences）、`question`、`materials`及`context`（actual_level/evidence_ref）。材料限当前角色所需，生成包不自动复制其他字段。real任务必须由任务来源授权，不能把用户账户/设备可达性当授权。

投递预检输入是一次运行的配置、任务包和已用预算。已用预算必须包含calls、cloud_calls、cloud_spend、output_tokens；未知费用阻止收费动作。输入token数必须使用已确认计数器，不用字符数冒充。预算比较包含拟调用的成本上限；本工具不进行并发全局额度预留，实际多worker运行器必须另行实现共享账本与预留。

回执必须声明真实或synthetic、执行引用、模型精确运行指纹、起止时间、输入token数、输出token数、付费额（或明确未知）、结果状态及分开计量的准备/人工/本地时间。输出无效、失败和超预算仍保留；输出为空只允许失败/取消。`capture`核验元数据和字节，不证明供应商真的执行、不验证模型答案。合成回执永不计入模型效果；成功输出也不等于命名可采用。

当前所有真实模型单元为`not_run`。默认授权只包括方法重构/离线程序测试，原#411生成和付费调用关闭。配置缺失时预检退出2并报告阻塞；非法数据退出1。任务包是草案也可以保存，但不能据草案发起调用。输出文件拒绝覆盖已有证据。

## 7. 迁移、回退与验收

保留旧Skill与校验器字节、旧案例与结果；不用改变旧期望值制造回归通过。新入口和配置为实验v0.1，#416保持Draft，main不修改。所有新工作先在原分支完成普通提交，遇并发head变化重新对账，不强推。

本轮工程结束点：方案/配置/接口落库、反例测试及旧回归运行、远端读回、恢复入口同步。模型效果的结束点另列：至少一个真实可负担配置的运行证据、独立质量复核和公平比较；本轮不提前报告通过。

最重要的剩余不是再次扩展框架，而是绑定实际本地部署与开发任务，取得第一份真实模型运行回执。缺少真实环境时保留`not_run`，不把本次同作者确定性测试伪装成已适配Qwen。


## 8. v90：本地执行器，不再只有离线任务包

授权：[本轮边界](https://github.com/InteropAtlas/InteropAtlas/issues/408#issuecomment-5645154433)。`local_runner.py` 增加以下实际代码路径：

- `probe` 只读取指定回环地址的模型列表；支持 LM Studio 和 Ollama，只读探测不调用模型。
- `prepare` 只绑定显式授权的虚构开发任务：读取精确已加载实例，调用官方 LM Studio SDK 的 prompt template 与 tokenizer，保存完整输入、分词依据和实际传输请求。不存在的模型不会被主动下载；已加载检查与SDK获取之间仍有竞态，SDK本身可能加载刚卸载的实例，不能声明绝对无加载行为。
- `run --execute` 对已冻结包使用 LM Studio `/v1/completions` 发送已渲染的原文，避免再次套 chat template；调用前后复查加载配置。服务器报告输入计数与预检不一致、输出超限或截断时保留材料并标为无效，不悄悄通过。
- SQLite 在投递前预留调用和最大输出额度；同一 run-root 的合作调用者共享账本。失败、断连或崩溃的预留不自动退回，也不自动重试；避免不知道请求是否执行时又重复消耗。

**实现范围**：首个实际推理后端是 LM Studio。Ollama仅实现列表/版本发现，没有冒称其推理与分词已接通。本轮没有实际 LM Studio/Qwen；测试调用真实本地HTTP栈，但服务与分词器均是明确的测试替身。`test_local_runner.py` 的通过不是模型兼容性或命名效果通过。

### 8.1 在实际运行模型的电脑使用

脚本支持Python 3.10+；准备实际LM Studio任务还需要官方 `lmstudio` Python SDK。探测、任务导出和模拟测试不依赖该SDK。不自动安装SDK或下载任何模型。当前版本未实现认证令牌传递；认证服务器将返回失败，不应为此关闭已有安全配置或开放公网端口。

从仓库根目录执行，下列服务地址是本机示例，不是已确认的Owner部署：

```bash
P=03_Evolution/01_Research/03_Tests/naming-evidence-pilot/model-aware
python "$P/local_runner.py" probe --endpoint http://127.0.0.1:1234 --output /tmp/naming-local-probe.json
python "$P/local_runner.py" tasks --output-dir /tmp/naming-dev-tasks
# 使用已加载列表中的完整实例ID；revision与runtime-version需由操作者提供真实值。
python "$P/local_runner.py" prepare --config "$P/experiment.json"   --task /tmp/naming-dev-tasks/DEV-01.json --endpoint http://127.0.0.1:1234   --model "$MODEL_ID" --revision "$WEIGHTS_REVISION" --runtime-version "$RUNTIME_VERSION"   --method simple --role generate --authorize-local-diagnostic --output /tmp/naming-prepared
python "$P/local_runner.py" run --prepared /tmp/naming-prepared   --run-root ./local-naming-runs --run-id DEV01-simple-r1 --execute
```

`prepare` 需要显式的 `--authorize-local-diagnostic`；仅在新输出包的配置中开启虚构开发诊断权限，不改变仓库默认配置或IA授权。`run` 仍须 `--execute`，没有默认自动调用。所有输出目录/运行ID拒绝覆盖；重复执行请使用有意义的新运行ID，不可靠删账本重置预算。

输出保存request、response原始字节、output文本、tokenization、调用意图、模型前后元数据与protocol回执。它们可能包含模型内容，应留在本地审查；不会自动上传仓库。不要把API原始日志中的私密信息随意公开。内部模型推理文本不是本任务要求的留痕材料。

### 8.2 仍需诚实保留的限制

精确实例、量化及已加载上下文来自服务；`revision`与运行软件版本仍是操作者声明，不是服务已测得的权重校验和。程序不能只凭实例ID证明磁盘权重未变；真实比较前应另行核实版本。服务器默认推理方式不被伪装为受控开关：本执行器冻结实际模板与请求，未显式覆盖的推理行为记录为限制。

回环地址和本地声明不能证明服务没有转发云端。执行者须确认该实例在本机推理；本工具不控制服务出站网络。当前仅接受字面回环IP、拒绝代理/重定向/公网地址，既不扫描Owner内网，也不让聊天访问Owner电脑的127.0.0.1。

账本的额度范围沿用实验配置：每个任务/方法/模型单元。全研究总预算、多机全局账本和完整多工作者调度尚未实现；本地多个run-root不共享额度。超时是网络I/O等待上限，不保证服务器立即停止已提交推理；未知用量保留，不报零。

这仍是**单任务传输与诊断路径**，不是完整A/B/C流程。`simple/redesign`任务包差别不能冒充整套方法对照，完整独立提案与两阶段选择仍须由后续编排实现。

### 8.3 开发任务与证据分类

`development-tasks.json`提供两个执行者编写的虚构开发任务：地方影像保存教育组织、离线字幕对照产品。均不是IA主线、真实客户或留出样本；没有真实负责人，所以不得报告采用成功。配置仅绑定开发任务材料，留出任务仍未绑定且禁止执行。

真实服务执行虚构任务时，同时记录 `record_kind=synthetic`（任务性质）与 `execution_kind=local_service_attempt_on_synthetic_task`（执行性质）；测试替身则记录 `mock_transport_test`。原协议汇总继续排除synthetic采用证据，但原始回执仍保留真实服务调用及成本，不把它们抹成从未执行。`backend_model_execution_confirmed`只表示成功返回的服务响应条件，不是第三方远程证明。

本轮实际结果及源代码哈希见 `transport-validation.json`。程序18项传输测试和旧25项协议测试通过；实际模型调用0。当前容器的1234与11434端口连接拒绝，只说明本执行环境无相应服务，不说明Owner电脑是否在运行。

### 8.4 主要API依据

实现参考官方接口，不引用第三方兼容性猜测；这些文档不替代目标部署实测。

- [LM Studio模型列表](https://lmstudio.ai/docs/developer/rest/list)
- [LM Studio分词与模板](https://lmstudio.ai/docs/python/tokenization)
- [LM Studio模型访问](https://lmstudio.ai/docs/python/manage-models/loading)
- [LM Studio兼容接口](https://lmstudio.ai/docs/developer/openai-compat)
- [Ollama只读模型列表](https://docs.ollama.com/api/tags)


<a id="workflow-v91"></a>

## 9. v91：无需外部助手控制的开发流程

本轮授权见 #408 中的 v91 实施记录。新增 [实验 Skill](SKILL.md) 和 `workflow.py`：程序负责阶段转换，用户选定的同一个本地模型负责提案与判断。不再以“识别后把结果发回ChatGPT”作为运行依赖。

### 9.1 已串联的实际路径

输入为已整理、冻结的开发简报。简洁组一次直接提出最多6项；重构组将同样生成输出上限分到关系、变化和独立身份三条请求，每条最多2项。上述视角与数量是v91实验切片，不是通用最佳方案。程序保留原文并精确去重，将同一个候选池先做真正不含说明的名称评审，再以独立请求审阅说明，随后抽查淘汰项。评审只见匿名ID与当前必要材料，不见路线及生成者排名；同一模型不同请求仍不是独立专家。

`advance`连续执行一轮，最多6次调用（简洁组最多4次）；有错误、预算不足或实质证据缺失才停止，不等待每步“继续”。缓存校验输入和输出，已完成步骤不重复调用。执行锁冲突、源码/计划变化、错误JSON、漏评或ID变化均保持阻塞，不把结构失败悄悄补写为成功。计划中的总预算是上限，不保证每个任务或第二轮一定有足够余额。

反馈由用户或获授权的本地Agent录入，保存原话与来源。下一轮只使用明确`next_instruction`，不把偏好理由自动泛化；已授权的`brief_patch`可纠正使命/名称职责等软表示，但不能改对象与硬约束。所有轮次仍使用同一本预算账本。原始简报、各轮结果和反馈不回改。

### 9.2 运行与证据接口

沿用v90本机服务限制、加载实例和SDK要求；无需向这个聊天传probe结果。模型部署信息由实际使用者/Agent在本机一次绑定。命令示例不代表目标部署已核实：

```bash
P=03_Evolution/01_Research/03_Tests/naming-evidence-pilot/model-aware
python "$P/local_runner.py" tasks --output-dir ./naming-dev-tasks
python "$P/workflow.py" init --config "$P/experiment.json" --task ./naming-dev-tasks/DEV-01.json \
  --workdir ./naming-session --endpoint http://127.0.0.1:1234 --model "$MODEL_ID" \
  --revision "$WEIGHTS_REVISION" --runtime-version "$RUNTIME_VERSION" --method redesign
python "$P/workflow.py" advance --workdir ./naming-session --execute
```

`--diagnostic-preview-authorized`只能在init时明确开启，允许查看本次虚构任务的诊断材料，不增加现实采用权限。默认没有候选展示，先等待筛查证据。没有外部查证执行器时停在`awaiting_screening_evidence`，不是让生成模型把unknown改成pass，也不是已完成全自动现实尽调。

`report.json`是可重建的当前投影；`plan.json`、`steps/`、`calls/`、`round-N.json`与追加的反馈/筛查记录是原始执行依据。结构出错时report写blocked且不再保留旧可展示列表。路径内可能有敏感模型输出，不自动上传仓库。

证据文件通过`screening --workdir ... --file ...`接入，含当前`round_digest`、候选ID、status、reviewer_ref、scope及evidence（本地file、sha256、source_ref、checked_at）。校验源字节与试行7天新鲜度窗口，不代表核查范围充分或结论正确。可追加更正版本，原记录不覆盖。接入外部查询工具的实际执行与认证仍未实现。

反馈通过`feedback --workdir ... --file ...`接入，再运行advance。反馈含当前`round_digest`、source_ref、verbatim、action（continue_search/stop/accept_for_research）、candidate_ids。继续时另需next_instruction；修改简报另需brief_change_authorized=true和brief_patch。错误反馈在落库前拒绝，不占用唯一反馈位置。accept_for_research必须引用已获准展示的候选，仅完成研究意见采集，不登记实际采用。

### 9.3 本轮验证与剩余边界

`test_workflow.py`在真实回环HTTP栈上使用明确的模拟服务与分词器，覆盖两组阶段顺序、评审输入分离、淘汰抽查、证据检查点、反馈续接、保留原简报、预算耗尽及断点不重发。所有TEST_ONLY条目只是程序夹具。实际语言模型调用0，真实语义质量/可采用性与跨任务效果均未测试。

本轮修改local_runner只增加“请求可降低输出上限”和“冻结采样seed”两个可选参数；旧默认行为和预算上限保留。首轮新增测试随报告行为修改出现一条期待不一致：新程序已经写入blocked报告，旧期待仍要求没有report文件。已改为明确检查blocked且display为空，失败输出保留在本轮证据中，不隐去。

当前不是全部方案已经完成：自动理解自然语言并校准简报、由模型提出并比较探索路线、真实域名/身份/商标查询适配、完整A/B/C跨模型试验及独立语义复核仍未完成。B旧方法未被压缩成simple组；当前A/C运行器切片也不代表整套新旧方法验证。程序已有连续调用与本地反馈接口，没有开发者补救这一默认节点。

复跑新测试：`python "$P/test_workflow.py" --output /tmp/workflow-tests.json`。这是同作者工程验证，正式方法效果须以真实模型与真实评价另行报告。


## v94：简单默认与选择证据边界

实验Skill为0.2.0，冻结的正式研究Skill仍0.4.0。新任务不传`--method`时为simple；三路线显式选择，不作为默认必需。生成者意图以未核实提案进入评审，risk原文只留在待查登记，不提供质量许可。

priority仅表示值得优先投入核查，hold保留但不自动安排核查/作为推荐展示；已查证现实条件不自动解决语义分歧。不能因所有项待定而强行填足优先队列。`format_adapter.py`只处理完整且唯一的结构差异，保留模型原文和转换记录，不补名字、理由或决定。

旧工作目录的实现哈希会拒绝新代码。复跑001/002/003必须checkout各自冻结源码；不要直接以新默认、新提示或新包装层改写旧结果。

本次选择对照及回执位于`selection-pilot/`，只复用003候选，不新增名称。它检验已暴露缺陷，不是独立盲评、留出任务或方法已普遍有效的证明。
