# WoT 描述、表示与 MQTT 交互证据的跨域对照

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Prior Art Comparison
Document Created At: 2026-11-05T05:32:33.298829+00:00
Document Updated At: 2026-11-05T05:35:24.767450+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / advance_coverage_basemap
  Reviewer: Agent — OpenAI / dot / review_wot_crossdomain (independent)
  GitHub Actor: ff6962757
-->

## 问题与结论

IA 中，node-wot 连接 WoT Thing Description（TD）1.1；TD 又连接 JSON、JSON-LD、URI、JSON Pointer 和语言标签；node-wot、Paho 和 Mosquitto 还连接 MQTT 5.0。这些记录是否已经组成一条已验证的设备交互链？

**没有。现有边把文献依赖、有限描述处理、显式配置的绑定路径、客户端发布订阅和 broker 的单段处理连到了同一知识地图，但没有共同的端到端执行证据。** 特别是 node-wot 的 `MqttBrokerServer` 名称不能直接当作 MQTT broker 身份：所录路径连接的是外部 broker。Paho 和 Mosquitto 的记录也不能被自动填入它的已测依赖链。

本文在既有领域入口之间解释一个有限连接区域，帮助找出哪些问题已经有记录、哪些仍需证据；不是完整领域底图、全球目录、覆盖率、系统选型或部署建议，也不改变关系语义。记录基线固定为 [`ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1`](https://github.com/InteropAtlas/InteropAtlas/tree/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1)。只读现有对象和关系，保留其版本、条件、历史运行范围与贡献元数据。

## 既有领域入口，而非新分类

基线的 [intake 编辑导航](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/Inbox/relations/intake-coverage-20260913.yaml) 已把 node-wot、Paho、Mosquitto 放在 `industrial`；JSON、URI、JSON Pointer 在 `syntax`；JSON-LD 在 `semantics`；BCP47 在 `metadata`。MQTT 和 TD 的该导航引用仍标为 `surface: candidate`，同 ID 的正式对象也已经存在。下方读取保留这个 surface，不把它改写成新的 Canonical membership，也不把两者当两个现实技术。

这些是当前 intake 导航成员，不是技术依赖或互斥的世界分类。本文讨论 MQTT 网络角色，但不据此给它增加 `transport` 成员；对象没有顶层 domains 字段也不等于未收录。各领域中的数量不用于判断完整度。

## 四处需要保留的边界

| 问题 | 已记录的事实与范围 | 仍未建立的组合证据 |
| --- | --- | --- |
| **描述能否被读取？** | `node_wot_implements_wot_td_1_1` 限 node-wot 0.9.2 的 core 描述解析/序列化、consume/produce。parseTD 补全与归一化、面向 ExposedThingInit 放宽的 schema、缺 security 时的 nosec 序列化行为都保留。历史 15 个无网络 core 示例只是该记录的补充证据。 | 成功返回不证明完整 TD、完整 JSON-LD、安全配置或真实设备交互；本研究没有重跑历史示例，也不把 nosec 当建议。 |
| **表示与语义依赖是否实现？** | TD 的五条 `uses` 分别指向 JSON、JSON-LD、URI、JSON Pointer、BCP47。JSON/JSON-LD 处理选择、URI base 的排除项、Pointer 的三个不同根、多语言 Map 的条件均有各自 context。 | 不沿 `node_wot implements TD uses X` 推导 `node_wot implements X`；解析 JSON 不证明 JSON-LD 展开或远程 context 获取；语言标签不是语言匹配或翻译能力。 |
| **Thing 暴露路径是否选对 MQTT 版本与角色？** | `node_wot_uses_mqtt_5_0` 仅限可选绑定的 `MqttBrokerServer`，显式 `protocolVersion=5`、`selfHost=false`、连接 MQTT5 外部 broker。记录中的锁定 MQTT.js 5.13.0 与 MQTT 协议5.0是不同版本维度；其默认协议值是4。 | 不是 core、默认消费端、所有绑定或内嵌 Aedes 均使用 MQTT5。不能从 TD 引用或类名推导 MQTT5 broker 实现；没有本次网络互通证据。 |
| **客户端与 broker 能否共同完成业务？** | Paho Python2.1.0 的边限显式 `protocol=MQTTv5`、broker 连接及网络循环的客户端路径；默认3.1.1不覆盖它。Mosquitto2.1.2的边限已有 active MQTT5 会话的 SUBSCRIBE 检查、登记、构造 SUBACK 并入队。 | Paho 的回调/会话条件、Mosquitto 的配置/ACL/插件/资源条件仍需满足。SUBACK入队不是网络送达。没有证明 node-wot↔该 broker、Paho↔该 broker 或三者共同的主题/负载/QoS/安全兼容。 |

这不是按四行新建能力分类，而是对一个既有连接区域的四个实际问题。下列原始 context 是判断依据，表格不能取代它们。

## 具体边与文献身份

- [WoT 实现关系文件](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/02_Relations/wot-implementations.yaml)：按 `node_wot_implements_wot_td_1_1` 与 `node_wot_uses_mqtt_5_0` 分别读取。后一条的贡献元数据仍写 `reviewer: pending independent review`；本研究只报告该字段，不据此重写历史评审状态，也不替该记录补签认证。
- [表示依赖关系文件](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/02_Relations/protocol-data-representation.yaml): `wot_td_1.1_uses_json`、`wot_td_1.1_uses_json_ld`、`wot_td_1.1_uses_uri_rfc3986`、`wot_td_1.1_uses_json_pointer_rfc6901`、`wot_td_1.1_uses_bcp47_rfc5646`。
- [MQTT 实现关系文件](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/02_Relations/mqtt-implementations.yaml)：`paho_mqtt_python_implements_mqtt_5.0` 与 `eclipse_mosquitto_implements_mqtt5_subscribe_path`，不是同一角色或同一检查范围。

TD 目标身份为 W3C Recommendation 2023-12-05；其依赖对象分别为 RFC8259、JSON-LD1.1 Recommendation 2020-07-16、RFC3986、RFC6901和RFC5646。BCP47 这一条不覆盖 RFC4647 语言匹配。MQTT 目标为 OASIS MQTT5.0 OS，不以 MQTT.js 软件大版本替代协议版次。本文不宣称这些是最新发行版本。

## 本次直接核对的一手依据

- [固定 TD1.1 §6](https://www.w3.org/TR/2023/REC-wot-thing-description11-20231205/#sec-td-serialization)明确允许 raw JSON 或 JSON-LD1.1 processor 处理同一表示。因此 JSON-LD 语法的文献依赖与某个实现执行语义处理仍是不同证据。
- [node-wot wot-impl.ts 93–120](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/packages/core/src/wot-impl.ts#L93-L120)将按 URI scheme 选择 client 获取 TD 与 consume 的 parseTD/ConsumedThing 构造分开；[serdes.ts](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/packages/core/src/serdes.ts)和 [helpers.ts](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/packages/core/src/helpers.ts)保留记录中的默认处理和宽松初始化校验边界，不新增完整校验判断。
- [MqttBrokerServer 44–89](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/packages/binding-mqtt/src/mqtt-broker-server.ts#L44-L89)实现 WoT ProtocolServer，而其 broker 字段是 mqtt.MqttClient；[361–395](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/packages/binding-mqtt/src/mqtt-broker-server.ts#L361-L395)在 selfHost=false 时不调用 startBroker，随后 connectAsync 连接外部 broker。这直接说明为何不能把“暴露 Thing 的 server binding”与“MQTT broker”合并。
- [配置类型](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/packages/binding-mqtt/src/mqtt.ts#L53-L63)、[CLI 转交](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/packages/cli/src/cli-default-servient.ts#L125-L150)及 [MQTT.js 固定 client.ts](https://github.com/mqttjs/MQTT.js/blob/1eb17d0e318095dafd3a3ad94c4c62c615deb288/src/lib/client.ts)分别支持允许值、传参及默认值/协议映射。依赖范围、锁文件版本和实际安装是三个不同事实；本次只读锁文件，不声称安装或运行 MQTT.js。
- [Paho client.py](https://github.com/eclipse-paho/paho.mqtt.python/blob/af64a4365c6ac5a7a4d339e7b00f44df91353b35/src/paho/mqtt/client.py#L662-L681)及 connect 说明区分 MQTTv5、默认3.1.1与网络循环处理 CONNACK 的条件；这不是已完成连接的观察。
- [Mosquitto handle_subscribe.c](https://github.com/eclipse-mosquitto/mosquitto/blob/99fa50f30e325609394c324c8ff71cfbbe95d8ab/src/handle_subscribe.c)和 [send_suback.c](https://github.com/eclipse-mosquitto/mosquitto/blob/99fa50f30e325609394c324c8ff71cfbbe95d8ab/src/send_suback.c)支持选中 active-session 路径与 packet__queue 终点。本文不从这几份源码扩张为完整 MQTT 规范审计。

这些是新读取的固定文本证据；历史测试的次数与结论仍只来自原 Canonical 记录，没有被本次重跑或重新认证。

## 可复查的机器读取

在固定提交的干净 checkout 上运行下面的临时查询，使用已有 loader 与 relation normalizer。它选取五个问题主体的相邻关系，再读取实际端点，不推断新边。输出包含完整对象、完整关系与原 navigation ref；它是查询结果，不是第二套 Canonical 数据或新增 API。集合断言只是这次观察的重现检查，不是新 CI gate 或完备率。

```python
from pathlib import Path
import sys,json,yaml
root=Path('/path/to/checkout-at-ff6ac83a').resolve()
sys.path.insert(0,str(root/'02_Runtime/01_Engine'))
from bootstrap_query import load_atlas,index_objects
from relation_model import normalize_relation
objects,relations=load_atlas(root)
index=index_objects(objects)
subjects={'node_wot','wot_td_1.1','mqtt_5.0','paho_mqtt_python','eclipse_mosquitto'}
expected={'node_wot_implements_wot_td_1_1','node_wot_uses_mqtt_5_0','paho_mqtt_python_implements_mqtt_5.0','eclipse_mosquitto_implements_mqtt5_subscribe_path','wot_td_1.1_uses_json','wot_td_1.1_uses_json_ld','wot_td_1.1_uses_uri_rfc3986','wot_td_1.1_uses_json_pointer_rfc6901','wot_td_1.1_uses_bcp47_rfc5646'}
selected=[row for row in relations if normalize_relation(row).source_id in subjects or normalize_relation(row).target_id in subjects]
assert {row['id'] for row in selected}==expected
ids=subjects|{normalize_relation(row).source_id for row in selected}|{normalize_relation(row).target_id for row in selected}
nav=yaml.safe_load((root/'01_State/Inbox/relations/intake-coverage-20260913.yaml').read_text())
memberships=[row for row in nav['memberships'] if row['ref']['id'] in ids]
print(json.dumps({'objects':[index[key] for key in sorted(ids)],'relations':selected,'navigation_memberships':memberships},ensure_ascii=False,indent=2,default=str))
```

当前输出的10个端点对象、9条选中关系和10项导航引用，仅标识这次查询的边界；不表示这些领域只有这么多知识。`context`、`evidence` 和 provenance 不能被路径数量替代。没有匹配到某个组合关系，也不能推出世界上不存在兼容实现。

## 下一步问题与停止边界

若要进一步证明一条实际链，至少需要固定被选 node-wot 角色、绑定配置、MQTT协议版本、broker实例与授权、主题/负载约定、认证/ACL以及具体成功/失败观察点。当前研究没有选择部署，也没有要求新增关系或运行该测试。

可单独研究的未知包括：TD 中某个 form 与实际绑定行为的对应、约定负载能否被参与者一致解释、SUBACK对应的过滤器/理由码如何到达调用方，以及实际 PUBLISH/会话/QoS条件。它们是缺少本次组合证据，不是软件缺功能的判定。既有 JSON-LD、URI、Pointer、多语言边的条件同样不能因为 MQTT 通信成功而自动被验证。

没有安装、构建、导入或执行上游，没有启动 broker、监听器或设备，也没有发送 MQTT 消息。只执行 Atlas 自身的读取与检查。本研究不替代其他领域的底图工作，也不把本区域或此前 Syslog 切片当作整体覆盖完成。

## 来源与文件指纹

下表为本次实际读取文件的 SHA256，GitHub URL 固定提交；W3C URL 固定出版版次。指纹用于识别输入，不把源码阅读变成运行或安全审计。第三方全文不镜像进仓库。

| 一手文件 | SHA256 |
| --- | --- |
| [node-wot/packages/core/src/serdes.ts](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/packages/core/src/serdes.ts) | `3f46b944d127b86aa9d52662ba60de2d017e5b831ba194d1db9412c3af5c837d` |
| [node-wot/packages/core/src/wot-impl.ts](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/packages/core/src/wot-impl.ts) | `ac48245c3ce6889ccac8bbc486ce258ac221f070917b7b4e619c631feedc5d59` |
| [node-wot/packages/core/src/helpers.ts](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/packages/core/src/helpers.ts) | `a10e33c9d9c09c5668b0d803f3f60782948718568ac27b2d92de9053efbf7481` |
| [node-wot/packages/binding-mqtt/src/mqtt.ts](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/packages/binding-mqtt/src/mqtt.ts) | `88bd91c7f56a13e4139139d5e67010824c3c9ca03e2c54460f0311e620f64812` |
| [node-wot/packages/binding-mqtt/src/mqtt-broker-server.ts](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/packages/binding-mqtt/src/mqtt-broker-server.ts) | `502a9f47e986a943ee21b6557e080e1b7e9fa2035f591f4adda34e8ed04523a8` |
| [node-wot/packages/cli/src/cli-default-servient.ts](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/packages/cli/src/cli-default-servient.ts) | `c265ceca476651b00af111785e9aa82515446a7c75a88d092f38ae645c4bc9e7` |
| [node-wot/package-lock.json](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/package-lock.json) | `ea3ad71643a262614f06bed6da8813edc6c019821a273edb1c6d40895c4ddf09` |
| [paho.mqtt.python/README.rst](https://github.com/eclipse-paho/paho.mqtt.python/blob/af64a4365c6ac5a7a4d339e7b00f44df91353b35/README.rst) | `7da00ef07909e616e308fe0d6d17791904c42a0add7e8161c91f975192739ef5` |
| [paho.mqtt.python/src/paho/mqtt/client.py](https://github.com/eclipse-paho/paho.mqtt.python/blob/af64a4365c6ac5a7a4d339e7b00f44df91353b35/src/paho/mqtt/client.py) | `5a3f0f73b344541828586a90f79a6beecb8e4396d8b81064bc2920c1a853618a` |
| [mosquitto/src/handle_subscribe.c](https://github.com/eclipse-mosquitto/mosquitto/blob/99fa50f30e325609394c324c8ff71cfbbe95d8ab/src/handle_subscribe.c) | `286efed89e029ee3e1c71dd958d6e9f35cbc5e30831c5f00ff083922ed16d4fb` |
| [mosquitto/src/send_suback.c](https://github.com/eclipse-mosquitto/mosquitto/blob/99fa50f30e325609394c324c8ff71cfbbe95d8ab/src/send_suback.c) | `28272ff38546753cc49368a0109ee42416438f7adc0a78890d7228c74c2ca14f` |
| [mosquitto/src/subs.c](https://github.com/eclipse-mosquitto/mosquitto/blob/99fa50f30e325609394c324c8ff71cfbbe95d8ab/src/subs.c) | `95b3e8e4c16ce5bc1404573207aff8f0e46d0fbe6238586066f647ca4703ffed` |
| [MQTT.js/src/lib/client.ts](https://github.com/mqttjs/MQTT.js/blob/1eb17d0e318095dafd3a3ad94c4c62c615deb288/src/lib/client.ts) | `953aef75f270916a7e182fbb6c0ef8e812c03259bdb2f7ffaeb8fa0ac8fb0a98` |
| [w3c-td11.html](https://www.w3.org/TR/2023/REC-wot-thing-description11-20231205/) | `db4517d82699840edfcd331ab064b17de569e4f9568c18c3d27a40cb411cf856` |

下表 Canonical 与编辑导航文件均固定在上述 IA 基线。关系文件含多条记录时，按前文 ID 选取；整文件指纹不扩张被选关系的范围。

| IA 输入 | SHA256 |
| --- | --- |
| [01_State/01_Objects/bcp47-rfc5646.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/01_Objects/bcp47-rfc5646.yaml) | `7da0bbd31e3065bdbc93c8d502023b7396b7fb8f81dafb7344cf6e4bc9e2e978` |
| [01_State/01_Objects/eclipse_mosquitto.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/01_Objects/eclipse_mosquitto.yaml) | `5b354d82705faf4d16df1383f149207229bd08632d49c025e6a9cbf79e202165` |
| [01_State/01_Objects/json-ld-1.1.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/01_Objects/json-ld-1.1.yaml) | `b423a12595a2e3416daaca1b4fb435dbd725077988370c7b21462c6818a4c254` |
| [01_State/01_Objects/json-pointer-rfc6901.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/01_Objects/json-pointer-rfc6901.yaml) | `38026593f9020a7106847505983571e1fadc9efb14c19313e438205020385270` |
| [01_State/01_Objects/json-rfc8259.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/01_Objects/json-rfc8259.yaml) | `7f67b0c5f18a98e50d9a14156bb45fa99e2b95080b35ccbc3874453c16351d2e` |
| [01_State/01_Objects/mqtt_5.0.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/01_Objects/mqtt_5.0.yaml) | `bdb35c24aa016f0165ddaaf844d00d6558a1a576df179b939a07d4c5df3f8804` |
| [01_State/01_Objects/node_wot.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/01_Objects/node_wot.yaml) | `d0afb14496a64077b14febee4119f37fd875e834ff160ce0a8448544bf05ffb3` |
| [01_State/01_Objects/paho_mqtt_python.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/01_Objects/paho_mqtt_python.yaml) | `1c14ee4d8a3015401bed4589b2ff254a6be48c356b08c04baec858726ec98ee7` |
| [01_State/01_Objects/uri-rfc3986.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/01_Objects/uri-rfc3986.yaml) | `941b7ab26ce0e70f120ca38f8d8c4cda3351e8b0c8a44ee855874a65cf45c13f` |
| [01_State/01_Objects/wot_td_1.1.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/01_Objects/wot_td_1.1.yaml) | `ddfe9ecd6fa68d78e7c7cdddbcef808284e0d33a942d1952d56296b32d968a13` |
| [01_State/02_Relations/mqtt-implementations.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/02_Relations/mqtt-implementations.yaml) | `c45cba62d0e10313f27faf5c2bdf10af9c358f8a447d28e49fed0f3cd127680b` |
| [01_State/02_Relations/protocol-data-representation.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/02_Relations/protocol-data-representation.yaml) | `480c477ce97168cb6589c62fbca0ed005196c7af8397291ff820b513dc07417f` |
| [01_State/02_Relations/wot-implementations.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/02_Relations/wot-implementations.yaml) | `7b477c2876faa541b505fd56e0847afe11d0f9118719823122d3edfc91dca263` |
| [01_State/Inbox/relations/intake-coverage-20260913.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/ff6ac83a2e5ad2ae1fdb87dd44c2d6980919f3e1/01_State/Inbox/relations/intake-coverage-20260913.yaml) | `45d0270be0bdfed6609b0ac17ae2fe985804d598e9f99a21bdcfc87c9c796efc` |
