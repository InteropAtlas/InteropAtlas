# UBL Invoice：XSD 有效与空元素约束的边界实验（2026-10-21）

<!-- InteropAtlas Document Metadata v0
Document Status: experiment_record
Document Created At: 2026-10-21T07:20:21.891382+00:00
Document Updated At: 2026-10-21T07:20:21.891382+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot
  Reviewer: Independent Agent — OpenAI / dot / main-session experimental review
  GitHub Actor: ff6962757
-->

## 结论先行

固定 UBL 2.3 Invoice 官方模式闭包与 xmlschema 4.3.2 后，5 个可信合成输入复现了三个不同层次：

1. 空 `cac:AccountingSupplierParty` 容器、空 `cbc:Note` 文本元素都可以 **XSD 验证有效**，却违反 UBL 2.3 §4.4 的 IND5 空元素约束。
2. 非法日期字符串仍是良构 XML，但 XSD 验证不符合；`validate` 抛出 `XMLSchemaDecodeError`。
3. XML 结束标签不匹配是 `XMLResourceParseError`，并非普通 XSD 不符合报告。

非空参考例只说明这个库对这个模式闭包返回有效，**不宣称完整 UBL 符合性**。实验没有建立通用 IND5 验证器、软件兼容关系、精确规范 `implements`、安全性保证或 IA 采用结论，也不形成长期测试或维护义务。

## 与现有底图的联系

固定知识基线为 [`327f78113d94c647dc587d6ee09fd6784f3464db`](https://github.com/InteropAtlas/InteropAtlas/commit/327f78113d94c647dc587d6ee09fd6784f3464db)。[UBL 精确 XML/XSD 引用](https://github.com/InteropAtlas/InteropAtlas/pull/486)和[xmlschema 实现先例](https://github.com/InteropAtlas/InteropAtlas/pull/487)使现有导航、能力查询和关系证据能找到相关资料。这里检验一个实际断点：找到 XSD 验证库，并不能把 XML/XSD 层的通过提升为 UBL 文档或业务层的通过。

依据是固定 [UBL 2.3 OASIS Standard（2021-06-15）§4.4](https://docs.oasis-open.org/ubl/os-UBL-2.3/UBL-2.3.html#S-EMPTY-ELEMENTS)：IND5 不允许无内容元素；即使某容器的全部子项在模式中可选，容器仍须有内容。§4.1 和 §6.1 将模式之外的文档约束保留在符合性范围内。上述正文原始字节 SHA256 为 `5ed4e54d64e84871f317c972a1c56d734411f50703c686dab8b3e310ac2c4d97`，复用本轮此前固定来源核查，不将发布时间冒充新核查时间。

本实验是一次性、可独立重现的分层验证反例，具有解释价值；不是日常任务日志、实时覆盖快照或新的查询接口。不修改 State、Runtime、旧实验、页面、CI、规范或目录入口。

## 冻结资产与实际结果

- [验证脚本](ubl-xsd-probe-20261021.py)：只使用固定 manifest 和可信合成内存实例，显式要求来源目录、两个 manifest 与新的输出目录。
- [16 个官方模式的 manifest](ubl-xsd-sources-20261021.json)：固定 URL、版本、SHA256、Git blob、原始字节数及 import/include 闭包。共 3,572,869 字节，不在仓库再分发原始模式。
- [6 个随包元模式的 manifest](ubl-xsd-meta-20261021.json)：只允许实际需要的固定安装文件，解析前比对 SHA256；这些是官方注册表安装包的局部字节观察，不冒充完整上游源码或供应链审计。
- [冻结结果](ubl-xsd-result-20261021.json)：含全部 5 个输入 XML、输入哈希、逐项结果、环境版本、源 manifest、每次资源读取及拒绝记录。

| 合成输入 | XML 良构 | XSD 结果 | 本实验可说明的边界 |
|---|---|---|---|
| 非空参考例 | 是 | 有效 | 没有声称所有 UBL 或业务条件均已满足 |
| 空 AccountingSupplierParty | 是 | 有效 | 已知空容器与 IND5 不符 |
| 空 Note | 是 | 有效 | 已知空文本元素与 IND5 不符 |
| 非法日期字符串 | 是 | 不符合 | DecodeError，不是 XML 解析失败 |
| 结束标签不匹配 | 否 | 无普通布尔结果 | XMLResourceParseError |

这里的空节点检查仅识别这些输入中“零子节点且无文本”的字面情形，不覆盖空白字符、null、所有语义规则或任意 UBL 文档。币种属性、供应方/客户名称等均为合成占位内容，没有真实业务或身份数据；未做代码表、金额业务规则、税务/法规、数字签名、实体攻击、生产安全或第三方互通验证。

原始最终执行时间为 `2026-10-21T07:16:02.799657+00:00`，环境为 Python **3.12.14**、xmlschema **4.3.2**、elementpath **5.1.4**。只调用 `XMLSchema10` 进行实例验证；库导入时还读取 XSD 1.1 元模式，不等于运行了 XSD 1.1 实例测试。

实际读取 24 次、22 个唯一资源：16 个官方模式和 6 个随包元模式。构建 warning 为零，网络或未列资源尝试为零。下载与解析阶段分开；验证阶段先核字节 SHA256、规范化路径并逐文件匹配，资源加载返回已核内存字节，未知 URL/路径失败关闭，`use_fallback=False`。这只是本次有限可信输入的实验设置，不是对任意不可信输入安全性的证明。

### 准备阶段的纠正与独立复现

初始本地预检把 XML 注释里的 DOCTYPE 字样当成有效声明，后改为只拒绝实际 DOCTYPE/实体声明；某 import 没有 schemaLocation，但同 namespace 已在闭包内，改为显式检查闭包内解析而非外部查找。库的目录 sandbox 在 maindoc 位置限制了 `../common`，最终使用更精确的逐文件字节允许集配合库级 `allow=local`；没有改变平台或系统访问权限，也没有修改官方模式。最初允许集枚举 19 个随包元模式而实际只读 6 个，最终收窄为固定 6 个并重跑，旧观察没有被改写成新限制下的结果。

独立审核者阅读最终本地脚本及元模式 manifest 后，在新的输出目录亲自重跑：5 个输入、结果、依赖、源 manifest 与 22 个唯一资源读集合一致，仅真实执行时间不同。便携发布副本仅增加显式 manifest 参数及固定 manifest 哈希门禁，保留输入、验证算法、断言与原始冻结结果。

## 复现这一固定实验

使用独立、已准备好上述版本的 Python 环境，令 `XMLSCHEMA_PY` 指向其解释器。以下版本是实际实验环境，不是生产推荐或最新版声明。脚本不会安装软件。

在仓库根目录先设置路径与新的临时工作目录：

```bash
EVIDENCE=03_Evolution/02_Experiments/03_Evidence
WORK=$(mktemp -d)
```

下载阶段与验证阶段明确分开。此命令只取固定 manifest 内的 16 个官方 URL，检查最终 URL 和精确 SHA256，并拒绝越界路径；不解析输入、不按未知依赖继续下载：

```bash
"$XMLSCHEMA_PY" - "$EVIDENCE/ubl-xsd-sources-20261021.json" "$WORK/sources" <<'PY_FETCH'
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlsplit
import hashlib, json, sys
manifest = Path(sys.argv[1]).read_bytes()
assert hashlib.sha256(manifest).hexdigest() == 'd79ebccf32b8265dfba5499c8a9a73775b4b39f45143874352c5fa7b059f87da'
items = json.loads(manifest)['schema_files']
assert len(items) == 16
root = Path(sys.argv[2]).resolve()
assert not root.exists(), 'choose a fresh sources directory'
root.mkdir(parents=True)
for item in items:
    url = item['url']
    parts = urlsplit(url)
    assert url.startswith('https://docs.oasis-open.org/ubl/os-UBL-2.3/xsd/')
    assert not parts.query and not parts.fragment
    path = (root / item['path']).resolve()
    assert path.is_relative_to(root)
    with urlopen(url, timeout=60) as response:
        assert response.url == url
        data = response.read()
    assert hashlib.sha256(data).hexdigest() == item['sha256'], item['path']
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
print('16 exact official files acquired; validation has not run')
PY_FETCH
```

然后运行禁止网络与未列资源加载的验证阶段：

```bash
"$XMLSCHEMA_PY" "$EVIDENCE/ubl-xsd-probe-20261021.py"   --sources "$WORK/sources"   --source-manifest "$EVIDENCE/ubl-xsd-sources-20261021.json"   --meta-manifest "$EVIDENCE/ubl-xsd-meta-20261021.json"   --output "$WORK/result"
```

脚本要求输出目录不存在，写入该新目录的 `result.json` 和 5 个 XML，不覆盖仓库冻结资产。缺少参数、manifest 字节不匹配、模式/元模式 hash 不匹配或出现未知资源均停止，不能把失败转成通过。复跑比较仅排除顶层真实 `observed_at`；环境、输入、观察、资源记录或其他字段不同时，应保留差异，不把它称为本次已核结果。

### 四个资产的 SHA256

- `ubl-xsd-meta-20261021.json`: `ce431f9ad037b6dfef180f4c7f4a262fa30bbc256ef03e5fa8599cf7bd628ee1`
- `ubl-xsd-probe-20261021.py`: `537babeab6e2e7b00436d86344841cf895d4e2ebb477a9c182507d9d22026009`
- `ubl-xsd-result-20261021.json`: `6d1e8fec5a10c149358c3d841b2395be0ea0ce7e3e52af9e04ceecd4ea483bdb`
- `ubl-xsd-sources-20261021.json`: `d79ebccf32b8265dfba5499c8a9a73775b4b39f45143874352c5fa7b059f87da`
