# 既有领域导航、实现关系与字段恢复的跨域审计

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Fixed-Baseline Audit
Document Created At: 2026-11-05T13:53:00+00:00
Document Updated At: 2026-11-05T13:53:00+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / advance_coverage_basemap
  Reviewer: Independent Agent — OpenAI / dot / review_broad_coverage_audit
  GitHub Actor: ff6962757
-->

## 问题与结论

[既有领域证据研究](../domain-evidence-actions-2026-11-05.zh-CN.md)已经连接 20 个导航领域的代表问题，CloudEvents 适配检验进一步发现 capability 选择与 notes-only assessment 的边界。本次把检查扩大到**全部现有种子导航成员及全部已录 implements 关系**，检验三个问题：导航身份能否恢复？能力筛选能否代替精确标准关系查询？未记录某个字段能否直接解释为知识缺口？

结论是：当前导航身份链可恢复，未发现需要补录的已接纳导航目标；能力筛选、标准关系查询和字段投影回答不同问题，不能互换。审计发现的缺字段及未选中记录，大多需要保留原角色和范围，而不是自动补标签、补来源或更新核验日期。下文的例外和决定均可由[一次性复算配方](reproduce.py)及[机器可读结果](findings.json)恢复。

固定基线为 `8c53fd278a595c7918833363cf63473fa46f3a61`。这不是对象/关系完整清单、当前地图更新或旧快照的替代物；输出仅包括有限遍历的诊断汇总、影响判断的例外、来源与恢复路径。没有修改 Canonical、Runtime、选择合同、分类、关系语义、页面/显示或维护方式。没有重新查询全部上游，也没有把计数当作全球覆盖率、质量分数或完整性证明。

## 一、导航身份：接纳事件与编辑成员是两个层次

读取[既有 draft / editorial_navigation_only 导航](https://github.com/InteropAtlas/InteropAtlas/blob/8c53fd278a595c7918833363cf63473fa46f3a61/01_State/Inbox/relations/intake-coverage-20260913.yaml)，按 Canonical 直接引用或 accepted event 的 `accepted_canonical_id` 恢复目标，而不是用 Candidate ID 猜 Canonical ID。

- 现有 20 类共 301 个成员：267 个 Canonical 直接引用、26 个已接纳 Candidate 引用、8 个未解析为 Canonical 的既有 identity_risk 引用。293 个已解析成员对应 271 个去重目标；类别可以重叠。
- 163 个 accepted 目标都出现在这张导航中，未发现重复的 `(category, resolved target)` 或遗漏的 accepted 目标。这只检查现有接纳与种子导航，不证明所有应收录知识都已被发现。
- 8 条接纳链的 Candidate ID 与 Canonical ID 不同，涉及 HLS、SRTP、HTTP/3、RTP、RTSP、SDP、Opus、FFV1。它们**当前均通过 Canonical 直接导航**，不是 8 个损坏的 Candidate 导航链接。事件连接仍是恢复接纳历史的正确依据。
- `p6-slice0-bcp47-rfc5646` 是 duplicate-only，没有 accepted event；其已有目标 `bcp47_rfc5646` 直接位于 metadata 导航。不能为补一个查询结果而制造第二次接纳。
- 8 个未解析引用对应 IEEE802.3 家族、SI、OPC UA 家族、NMOS IS04/IS05、OpenEXR、ACES、OTIO 的既有身份边界。本次保留，不将其改写为正式对象或无证据条目。这也不是全部旧 hold 的清单。

当前记录连接与冻结历史检查分开进行。既有 [`intake_coverage_audit.py`](https://github.com/InteropAtlas/InteropAtlas/blob/8c53fd278a595c7918833363cf63473fa46f3a61/02_Runtime/01_Engine/intake_coverage_audit.py) 已在该基线实际执行，163 个冻结接纳路由通过，输出为 `PASS / STRUCTURAL AND REFERENCE CHECKS ONLY`。它检查冻结候选及基线一致性，不自动证明独立语义审核或所有接纳判断正确。研究配方验证这份单独执行结果的字节摘要，不冒充自己重新执行了冻结审核。

## 二、实现选择：同一能力不等于同一标准的已录实现边

使用既有 loader、kind registry、关系 normalizer、graph 与 workspace selector。此处的 implementation profile 是现有 registry 的角色判断，不是新增 `type: implementation` 或新分类。

全图当前有 47 条显式 implements 记录、44 个不同 source；其中 46 条来自 43 个 implementation-profile 记录，另一 source 是 RDF Turtle 标准。26 条边的 23 个 source 没有 capabilities 字段。它们并不因此缺少已录实现边，也不因此应自动补 capability 注释。

下面六组对照中的 capability 都是目标记录实际已有的值；没有据此推断任何 source 应具备它。所谓“无该边”只指当前没有所选精确目标的记录，不是技术不支持或未实现的判断。每条正面边仍受自己的版本、条件与证据约束。

| 精确目标 | 已录有界 implements 选择 | 同一 capability 的既有实现选择为何不同 |
| --- | --- | --- |
| CBOR RFC8949 | libcbor、python_cbor2、TinyCBOR 各自的有限切片 | data_serialization 选择遗漏未注释的 TinyCBOR，又包含其他表示/协议的记录，不能当作 CBOR 查询 |
| HTTP/3 RFC9114 | aioquic 的既有有界边 | web_resource_transfer 的实现选择为 h11/httpx，并不是该目标边的 source 集 |
| Git protocol v2 | Git 的 ls-refs 切片 | version_control 选择 Dulwich，不能由同能力替换精确版本/操作关系 |
| JSON Schema 2020-12 | python_jsonschema 的既有边 | schema_validation 还选出 pyshacl、python_xmlschema；共同能力不产生该精确标准关系 |
| CommonMark 0.31.2 | cmark 的既有边 | document_representation 还选出 cmark_gfm、python_html5lib；它们不是这条精确边的同义替代 |
| RDF 1.2 Concepts | 已录 RDF Turtle→RDF Model 关系 | source 是标准，CLI implementation-profile 过滤会排除它，而 workspace 能力选择可包含标准；不能把所有 implements source 都叫软件 |

机器结果保留各组精确集合、关系 ID、原 context 哈希和恢复路径，以及所选条目的 scope 来源；没有生成排名或互换性结论。原始 source/target 来源是**记录级来源**，不是自动证明每个比较字段的独立证据。对象 capability 字段与关系 `context.capabilities` 也分别保留，三处已录差异不被自动补齐。

### RDF 例外：原始 evidence 缺失不等于关系没有来源

`rdf_turtle_implements_rdf_model` 的原始 `evidence` 字段缺失，现有 normalize_relation 也不输出 evidence；但这条历史关系保留了自己的 legacy `sources`，另有 source/target 对象来源。三者必须分别恢复，不能把“normalized evidence 为空”写成“关系没有依据”，也不能把对象来源升级为该边的充分证明。

本次只检验[现有记录及读取行为](https://github.com/InteropAtlas/InteropAtlas/blob/8c53fd278a595c7918833363cf63473fa46f3a61/01_State/02_Relations/linked-data-and-hypertext.yaml)，不重新确认这条旧 implements 的语义、置信度或当前规范状态；也不从另一个已澄清的 provides 边传递结论到 implements/maps_to。没有更改 normalizer 或关系数据。

## 三、字段缺失：先保留角色和恢复路径

在 271 个已解析导航目标上，以现有 `project_field` 检查十个字段：version、capabilities、中英 description/scope、last_verified_at/by、sources、notes_zh。共检查 2,710 个字段投影的原值、状态及恢复对象/字段；这是恢复路径测试，不是 2,710 个互操作案例，也不证明来源逐字段充分。

- 返回 sources-not-recorded 的 22 个目标，恰为 21 个 capability 记录与 IA 自有的 `interopatlas_fact_source` scenario，不是缺少来源的标准或实现集合。因此没有依据把这 22 项转成标准证据修复队列。
- 73 个已导航 implementation-profile 记录都有 sources 与 description_zh；全部没有 notes_zh，其中 51 个另有 scope_notes_zh。notes-only assessment 的 not_recorded 不能被读成“对象没有任何条件、限制或评估”。本次不改变现有投影或显示文字。
- 这 73 项有 44 个未记录 capabilities。另有 github_actions、forgejo_actions 两个既有 implementation-profile 记录位于种子导航之外。前者不意味着能力缺失，后者也不自动证明导航错误；该导航本来就不是全库分类。
- 对某个字面字段（尤其 last_verified_at）的缺失，不能推断从未核验；旧载体和其他时间字段可能承担不同作用。本配方没有合并日期，没有用 accessed、Git 时间或研究时间补成核验日期，也没有刷新外部事实。

所有字段仍可按结果中的固定提交、物理文件、稳定 ID 和字段名回源。读取已存在的描述/范围是恢复材料，不是将它们改名为外部权威证据。

## 四、这次审计支持的具体决定

这些是针对固定输入的研究判断，不是新的项目维护规范：

1. 保留当前导航、8 个身份边界及 duplicate-only BCP47；没有发现需要补写的已接纳导航目标。
2. 问某个精确标准的已录实现关系时，先恢复它的显式边与完整原 context，分别读取 relation evidence、legacy relation sources 与 endpoint sources；能力选择只作为另一个问题的结果，不能代替。
3. 不根据来源字段或 notes-only assessment 的缺失自动补来源/注释；先核原角色、描述、范围与具体证据。
4. 不根据本审计补 capabilities、传播关系、更新日期、认定替代方案或宣布覆盖完成。

本研究比代表样本更广，但仍没有定义现实世界的完整标准/实现全集，没有验证所有上游状态、所有版本组合或真实交换。当前未建立任何 Canonical 数据缺陷，因此本次交付是可复现的判断依据，而不是为了增加修改数量制造数据修复。

## 复算与验证边界

工件：[reproduce.py](reproduce.py) · [findings.json](findings.json)。配方仅在固定基线运行，要求 tracked 输入干净，并拒绝消费区的额外未跟踪输入；已有 build 输出和普通 Python 字节码不作为数据输入。它只读、只向 stdout 输出，不创建新 Runtime API、CI gate 或自动更新任务。

准备一个完整历史的基线 checkout，将以下 `$REPRODUCE` 指向本工件中的 reproduce.py，`$BASELINE` 指向该 checkout。使用该版 Engine 已有依赖即可；本次实际环境是 Python 3.12.14 / PyYAML 6.0.3 / jsonschema 4.26.0。没有安装新依赖或运行上游实现。

```bash
set -e
PYTHONDONTWRITEBYTECODE=1 python "$BASELINE/02_Runtime/01_Engine/intake_coverage_audit.py" --root "$BASELINE" > /tmp/ia-intake-audit.json
PYTHONDONTWRITEBYTECODE=1 python "$REPRODUCE" --root "$BASELINE" --intake-result /tmp/ia-intake-audit.json > /tmp/ia-domain-findings.json
```

省略 `--intake-result` 时，结果明确标为 `NOT_RUN_BY_THIS_RECIPE`，不冒称冻结历史检查已完成；这种输出与随附的含 receipt 结果不同。`--intake-result` 验证的是先前单独执行输出的精确 SHA256，不是独立性或语义正确性的证明。

完整 intake 输出 69251 字节，SHA256 `d93e9e94d478707c26936fdcfcc201fdcc6bf0162e58a6083e46e443aeb98185`，未在此重新发布完整导航清单。配方 SHA256 为 `bcb7159f21a3d5c12f597190995779971ab7f1264e63f0f9f118d438700983ef`；随附 findings.json 共 83127 字节，SHA256 为 `2355fccf6eb8c264aa400dcb1b6ad573aa43d9fbb4bf8783036f7bc0922b79ca`。作者与独立审核分别执行了该全历史检查及研究配方，并核了 selector 集合、上下文字段恢复及 source 角色差异；适用仓库检查另行记录。所有旧 hold、历史快照和未完成操作保持不变。
