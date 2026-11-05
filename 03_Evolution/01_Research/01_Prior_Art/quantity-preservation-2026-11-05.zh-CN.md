# 共享 JSON 之后：SenML 与 FHIR Quantity 的量值保留条件

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Source-Bound Quantity Comparison
Document Created At: 2026-11-05T16:42:13+00:00
Document Updated At: 2026-11-05T16:42:13+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / finish_wot_evidence
  Reviewer: Independent Agent — OpenAI / dot / review_quantity_preservation
  GitHub Actor: ff6962757
-->

## 问题与结论

两种记录都使用 JSON 数字，并不表示同一次解析、字段复制或重序列化能保留相同的量值含义。一个直接的差异是：RFC8428 §5 明确 SenML 的 `1.1` 与 `1.10` 有完全相同的语义；FHIR R4 则要求 decimal 保留原表示的精度用于展示，虽不强制据此改变计算。把尾零去掉，不能在两个合同下都无条件称作“无损”；尾零也不自动构成测量误差或不确定度。

本研究把 industrial/measurement 的 SenML、health 的 FHIR Quantity 与 syntax 的 JSON 放在一组明确交接问题下，比较五件需要分别保留的内容：Pack 继承上下文、单位依据、界限限定词、表示精度，以及缺值/约束。它不是一个传感器接入医疗系统的设计，也没有创建 SenML→FHIR 技术关系、通用转换器、临床适用结论或新分类。

固定 IA 基线为 `508c596ef40f67f568238456ebb3ea6a218415eb`。[机器可读证据与原始输入](quantity-preservation-2026-11-05-evidence.json)选择已有 `senml_rfc8428`、`fhir_r4_4.0.1`、`json_rfc8259` 和两个有限实现先例；两条既有 uses 只各自说明 JSON 表示范围。选择按稳定 ID 和完整原关系恢复，不依赖 capability/notes 是否存在，不进行图路径闭包。既有 [SenML 四表示比较](senml-representation-coverage-2026-10-31.zh-CN.md)与 [FHIR 五种交换方法研究](fhir-r4-exchange-evidence-2026-10-31.zh-CN.md)保留原问题与基线，本研究不替代它们或任何历史快照。

## 用有限输入区分实际需要保留的内容

以下均是源条文推导，不是上游库、转换器、validator 或服务器执行结果。JSON 原文保存在证据文件中；FHIR 对象只是 Quantity 片段，不能宣称完整资源/Profile 通过。合成 SenML 名称使用 example.org，占位名称不证明真实设备、测量对象或全局唯一性。

| 问题与输入 | 固定来源支持的解释 | 交接时仍缺什么 |
|---|---|---|
| S1：三条记录的数字都为20，活动 bu=Cel，第二条 u=K | 源解释依次20 Cel、20 K、20 Cel；本条 u 不改变后续 bu。 | 不能当成三个相同量值或一次温标换算；抽离记录需保留/应用源上下文。 |
| S2：bv=20 后数值1、2，再显式 bv=0 后数值2、3 | 源数值依次21、22、2、3，单位保持活动 bu。 | v 字段不是每条最终数值；显式零与没有 base 字段不同。这里不是校准或误差修正声明。 |
| S3、FQ1/FQ3：无单位、显式比率、FHIR显示 g、FHIR编码 g | 它们提供的单位证据不同；display-only 不自动变成 UCUM 编码，缺单位不自动变成比率。 | 需单位来源及应用上下文；同样字符串不证明跨注册表映射已成立。 |
| FQ1/FQ2：2.00 g 与小于2.00 g | 没有 comparator 是点值；有 comparator 的界限不得被忽略。 | 只复制数值和单位不保留该限定词。何种目标表示能承载它仍未决定。 |
| S4 与 FQ1/FQ6：尾零 | SenML 数值语义不区分1.1/1.10；FHIR展示精度区分2.00/2.0。 | 需先明确目标合同和保留目的；不能反向从 SenML 尾零补造精度承诺。 |
| S5、FQ4/FQ5：字符串 v、code 无 system、缺 value | 前两者分别违反所引字段/qty-3 规则；后者没有数值，不能填0。 | JSON语法、数据类型规则、完整资源与临床解释不是同一项检查。 |

表格定位：RFC8428 §§4–4.6、§5、§12.1；FHIR R4 datatypes 的 Quantity/precision、datatypes-definitions 的 Quantity 各成员，以及 json decimal。逐项行段、原始字节身份与输入绑定均见证据文件，不把研究判断改写为新的标准条文。

## SenML：JSON 数字之外仍有继承状态、单位和解释边界

固定 RFC 8428（2018-08 原始出版物），未整合 RFC 9100 或勘误。既有 `senml_rfc8428 → json_rfc8259 uses` 只证明两种 JSON 表示的文献级编码使用，不证明量值等价、完整验证或无损转换。本节新增的是数值/单位路径证据，不重述既有四种表示报告。

- **继承不是逐条自足。** base 字段作用于本条及后续记录，直到同名 base 被替换；常规字段只作用于本条。缺 `u` 时用活动 `bu`，本条 `u` 覆盖它但不改写后续记录的缺省单位（§4、§4.1、§4.5.2；原始 TXT L328–357、L521–526）。`bv + v` 给出数值；`bv:0` 显式替换既有 base，省略 `bv` 不等于重置。每个演示数值记录明确保留 `v`，不把缺字段补零规则扩张为任意记录都合法（§4.2 L380–386；§4.5.4 L594–596）。抽离记录前需应用原 Pack 的 base；本节的推导值不是完整 resolved Record 输出（§4.6 L623–645）。
- **未声明单位不等于无量纲。** 无 `u` 且无活动 `bu` 是允许的，但需要的单位信息依赖应用上下文；`u:"/"` 才是此处显式的比率单位示例。原版注册表中 `Cel` 为 degrees Celsius，`C` 为 coulomb，大小写有意义；这只标识固定 SenML 单位，不证明自动 UCUM 映射或任意单位互换（§4.5.2 L523–526；§12.1 L1705–1713、L1750–1779、L1870–1880）。
- **尾零语义必须按格式分别看。** §5 明确 `1.1` 和 `1.10` 在 SenML 中有完全相同的语义，测量的有效数字数目不相关（L745–754）。可与主报告中另有固定来源的 FHIR R4 decimal 展示精度规则作这一点的精确对照；不能因此声称格式间精度信息已经保留，也不能将 FHIR 的展示精度或这里的尾零解释为测量准确度、不确定度或临床意义。SenML §4.5.4 本身指出统计特征如 accuracy 的表达很复杂（L598–601）；静态元数据常在带外（§4.7 L652–655）。
- **数值表示与测量证据分开。** §5 要求接收系统处理 IEEE 双精度可表示的数值范围，未因此承诺任意十进制文本精确往返。`v` 是 JSON Number，字符串 `"20"` 不能仅因 JSON 可解析就成为合法数值 `v`（§4.3 L411–429；§5 L735–754）。名称、时刻、被测对象及应用上下文的等价也不能由相同数字证明。

固定 `farshidtz_senml` v2.0.0 / commit `320c4746a311e331e1d1b616d3dc5ad2d53e820d` 的新增静态证据限于：`BaseValue`/`Value` 为 `*float64`（senml.go L33–48），数值路径按非 nil 判断 base 是否出现，因此能在该分支用显式零替换活动 base（L99–109）；单位路径保留非空 base，缺本条单位才取它，不执行单位换算（L123–130）。这是源码阅读，不是运行结果，不扩为完整库符合性或精度保证。

配套证据文件 有五个精确 raw JSON：单位继承/局部覆盖、数值 base 重置、缺单位与显式比率、1.1/1.10、合法 JSON 但错误 v 类型。全部 `UNEXECUTED`、`actual_result:null`，仅按条文推导解释。未安装、导入、编译或执行上游代码；没有通用转换器、温标换算、真实测量验证或临床断言。示例名称为合成占位名称，实际应用必须满足全局唯一命名要求。

来源原始字节、字节数、SHA-256、发布日期、抓取日期、逐项行号及已验证 section anchors 见主报告的机器可读证据文件。原版 §12.1 L1838 的 `T0 = 275.15 K` 原样保存在证据中；本节不使用其数值推导任何换算，不静默修订或声称已核验勘误。

## FHIR R4 4.0.1：数值、展示精度与单位身份分开判断

本节只做固定版规范比较，不是 FHIR 实现复测，也不建立 SenML→FHIR 转换或新的关系。官方 HTML 原字节、检索日期、SHA-256、字节数和行定位见主报告的机器可读证据文件。基线 HEAD 只读核对为 508c596ef40f67f568238456ebb3ea6a218415eb。

- **数值不等于完整保留。** Quantity.value 为 decimal；FHIR JSON 必须使用 JSON number，而不是把数字改成字符串。2.00 与 2 或 2.0 的算术大小可相同，但表示的精度不同。R4 要求保留原有精度用于展示，并明确不强制据此采用不同的计算方法；json.html 专门警告原生 JavaScript 浮点解析会丢尾零。因此，数值相等不能单独证明交接完整；反过来，也不能把尾零自动解释为测量不确定度、置信区间、精度误差限或 ±0.005 g。这里确认的是规范规定的隐含展示精度，不是测量学不确定度模型。（datatypes.html#precision，原 HTML 440–448 行；json.html#primitive，266–268 行；#decimal，282–291 行。）
- **显示文本不等于编码身份。** unit 是可读的单位表示；system 指定编码系统，code 才是机器可处理的单位形式。即使 unit 文本恰好为 g，也不能由此断言它是 UCUM 编码。qty-3 要求存在 code 时同时存在 system，但没有要求每个基础 Quantity 都必须有 UCUM code。规范建议能以 UCUM 编码且提供 code 时采用 UCUM；上下文或 profile 可加严约束。（datatypes.html#Quantity，1922–1941 行；#Quantity-inv，1935 行；datatypes-definitions.html#Quantity.unit 至 #Quantity.code，551–582 行。）
- **边界不等于点值。** 没有 comparator 时 value 是点值；有 “<” 时描述小于所示数值的实际值，不能忽略 comparator 后仍称语义保留。comparator 标记为 modifier；这不等于 modifierExtension，也不是一个新精度字段。（datatypes.html#Quantity，1918–1919 行；datatypes-definitions.html#Quantity.comparator，539–548 行。）
- **缺省不补造。** 基础 Quantity 的 value、unit、system、code 各为 0..1，并受 qty-3 等约束；缺 value 不等于 0，只有单位不能产生数值大小。缺 unit 但有 system+code 不等于缺编码单位；缺全部单位字段也不能凭空推断单位、比例尺或单位换算。完整资源与特定 profile 可能另有要求，这些片段不能宣称通过其验证。（datatypes-definitions.html，528–582 行。）
- **固定 FHIR 版不等于固定 UCUM 版。** R4 的 UCUM 页面使用无版本 URI http://unitsofmeasure.org，并要求大小写敏感的符号；其 1.9 只是版本举例，不是指定本比较采用 UCUM 1.9。Quantity 本身没有 version 字段。当前证据没有锁定独立 UCUM 出版版本，不把该 URI 当出版版次，也不新引入 UCUM 项目 intake。（ucum.html#4.3.4.1，121–129 行。）



## 实现先例与未知分别保留

既有 [farshidtz_senml 对象](https://github.com/InteropAtlas/InteropAtlas/blob/508c596ef40f67f568238456ebb3ea6a218415eb/01_State/01_Objects/farshidtz_senml.yaml)仍是静态、有限的专用 Go 库先例，不是已运行的 SenML/FHIR 网关。本轮只补读其固定 `senml.go` 数值与单位分支，未执行 Normalize，也不把 `*float64` 或源码零值分支提升为任意精度、完整 base 处理或无损往返保证。其旧时间/字符串/未知标签范围继续有效。

[既有 python_fhirclient 对象](https://github.com/InteropAtlas/InteropAtlas/blob/508c596ef40f67f568238456ebb3ea6a218415eb/01_State/01_Objects/python_fhirclient.yaml)和 [原接纳 packet](https://github.com/InteropAtlas/InteropAtlas/blob/508c596ef40f67f568238456ebb3ea6a218415eb/01_State/Inbox/review-packets/python-fhirclient-implementation-20261021.yaml)保留原21项合成内存观察及 float-valued Quantity 边界。本次只引用已合并记录，未重新获取/资格核验其源码、重跑模型、改写摘要或推进 held PR672。原实现限制不是新试验，也不能凭此推断所有 FHIR 库都丢失精度。

这次闭合的是有来源的有限判断：为什么单个数字、单位字符串或 JSON 成功不足以认定两份量值等价，以及具体是哪项信息需要保留。仍未闭合的是：目标字段表示的被测量是否相同、名称/时间/主体和方法是否对应、单位编码与版本如何选定、限定词如何承载，以及实际实现是否保留所要求的表示精度。数量类型本身不能提供这些上下文；这些问题也不是注释字段缺失就能判定的“不支持”。

FHIR R4 的无版本 UCUM system URI 不构成独立出版物的版本固定；因此没有为增加数量而新建一个含糊 UCUM 对象。原 SenML 注册表与 FHIR 所用编码的关联只按所查条文保留，未执行 UCUM 服务、单位转换或温标换算。未来任何实际交接仍须选定明确的实现/资源合同和观察点，本报告不授予相关操作许可。

## 一次性机器复核配方

工件：[证据及11个原始JSON输入](quantity-preservation-2026-11-05-evidence.json) · [一次性复核脚本](quantity-preservation-2026-11-05-reproduce.py)。脚本用现有 loader/normalizer 恢复5个既有对象和2条直接关系，输出完整原 context、evidence 与 legacy sources 的字段在场状态，不把端点来源冒充边证据。它同时核对固定输入文件和原始JSON字符串指纹、源引用绑定、UNEXECUTED标记，并用标准库 Decimal 对这组固定值做词法/算术检查。没有抓取网络、调用上游库、遍历任意引用或实现通用转换器。

先准备上述基线 B 的 checkout，将 `$BASELINE` 指向它；把 `$REPRODUCE` 指向本报告随附脚本。使用该基线 Engine 既有依赖即可：

```bash
PYTHONDONTWRITEBYTECODE=1 python "$REPRODUCE" --root "$BASELINE"
```

输出中的成功只表示这个有限证据包的身份、结构和本地算术条件相符，不是11项 SenML/FHIR 测试通过。S5 与 FQ4 故意包含源规则反例，它们仍可通过 JSON 语法检查；`actual_result` 始终为 null。执行结果摘要、实际环境与输出指纹在本节末记录；仓库适用检查与独立复核另见交付 PR，不冒充上游验证。

### 来源边界

官方 RFC8428 TXT/HTML、固定 SenML 源文件与固定 FHIR R4 页面均保留原始字节SHA256和行号；源文件不在仓库镜像。HTML行号按原文件LF分行，不是浏览器显示行号。FHIR R4 页面身份固定为4.0.1，获取日期不是发布日期；UCUM编码系统URI也不是其独立出版版次。RFC9100、勘误、全格式约束、真实测量/临床验证、跨实现交换均未执行或全面审阅。研究未更改 Canonical、Runtime、关系语义、UI、页面、治理或维护规则；全部既有 hold 保持。

### 本次实际复算结果

在干净的基线 checkout 上，以 Python 3.12.14 和既有 Engine 依赖运行上述脚本通过：5个精确对象、2条原关系、11个原始输入及5组比较引用均恢复/核对；固定 S2 的本地 Decimal 加法得到21、22、2、3。该算术结果不是上游 Normalize 执行，也不是任何测量值的真实性证明。YAML来源日期只序列化为原值的ISO文本，不刷新日期。完整 stdout 为 35128 字节，UTF-8 SHA256 `5fc4f614ec9aaa1b3dcc5f03406a057c53a5fc896ab9cfa182b009ab6acd4859`。配方指纹 `a980ee442cbae8de99e56f2e57836c1385aba50efd9944ce209762e66d40609d`；证据文件指纹 `5b8c148c4ecd1f40fc30cf8c1119aea9df2c05aa3c16d401fbe1474927dc476d`。这些校验值描述本次实际运行，不承诺不同 Python/依赖环境产生逐字相同输出。
