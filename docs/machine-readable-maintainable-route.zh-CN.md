# InteropAtlas 机器可用 / 可维护路线（暂定参考）

> 状态：Provisional Reference（暂定参考）。用于与人类可读路线并行指导近期实践，不代表冻结架构。

## 目标

机器路线不是“让 Python 能读 YAML”这么简单，而是让 InteropAtlas 的事实、关系、规则与评估结果能够被稳定读取、验证、解析、建图、查询、分析、维护、观测、演进，并最终被外部系统和 Agent 使用。

## 路线

1. **Loadable（能稳定读取）**
   - 可靠发现并加载对象与关系文件。
   - 支持多 YAML document、source metadata、重复 ID 检测、解析错误和加载统计。
   - 逐步形成稳定的 Canonical Representation（规范化内部表示）。

2. **Validatable（能验证）**
   - YAML 语法、JSON Schema、必填字段、类型约束、唯一 ID、引用合法性和语义一致性。
   - 验证结果应逐步区分 Error / Warning / Notice / Unknown，而不是只有通过/失败。

3. **Resolvable（能解析引用）**
   - 将 capability、organization、standard、implementation、relation 等 ID 从普通字符串解析成真实对象引用。
   - 检测不存在对象、类型不匹配、非法引用等问题。

4. **Graphable（能形成关系图）**
   - 建立 forward edges、reverse edges、typed edges 和 backlinks。
   - 支持关系的场景、能力、条件、证据、置信度和时间等上下文。
   - Renderer 不应长期自己扫描全部对象来模拟 Graph / Backlink Index。

5. **Queryable（能确定性查询）**
   - 提供稳定的基础查询：对象检索、邻居、反向引用、某能力对应的标准/实现、替代方案、依赖关系等。
   - 相同输入与相同数据应得到确定性结果。

6. **Analyzable（能计算与分析）**
   - Pathfinder、Coverage Analyzer、Gap Analyzer、Comparator、Dependency Audit、Openness Analyzer、Trend Monitor、Constraint Evaluator 等。
   - 严格区分 Fact（事实）与 Assessment（评估/计算结果）。

7. **Maintainable（能辅助维护 Atlas 自身）**
   - 发现孤立对象、无效引用、疑似重复对象、过时版本、失效来源、缺失 Evidence、分类异常、关系冲突等。
   - 逐步形成 Atlas Linter（地图检查器）。

8. **Observable（Atlas 自身可观测）**
   - 统计对象数、关系数、断裂引用、缺失 Evidence、孤立对象、陈旧标准、人类可读覆盖率、关系覆盖率等。
   - 形成 Atlas Health（地图健康状态）。

9. **Evolvable（数据模型可长期演进）**
   - Schema、relation vocabulary、object types 与字段可以版本化并迁移。
   - 必要时引入 schema_version 和自动迁移机制，避免旧数据逐步不可维护。

10. **Interoperable（InteropAtlas 自身可互操作）**
    - Canonical Model 可投影为 JSON、JSON-LD、RDF、CSV、Graph Export、API、Agent interface 等。
    - 坚持“概念兼容、实现不绑定”，不把事实源锁死到单一数据库或图技术。

## 机器路线内部层次

```text
Sources / YAML
      ↓
Loader
      ↓
Validator
      ↓
Reference Resolver
      ↓
Canonical Objects
      ↓
Graph / Index
      ↓
Query / Analysis Engine
      ↓
API / Export / Agent / Views
```

## 与人类可读路线并行

```text
       人类可读路线                     机器可用路线

Visible 看得到                     Loadable 能读取
      ↓                                ↓
Readable 看得懂                    Validatable 能验证
      ↓                                ↓
Navigable 找得到                   Resolvable 能解析
      ↓                                ↓
Connected 看关系        ←→          Graphable 能建图
      ↓                                ↓
Mappable 成地图         ←→          Queryable 能查询
      ↓                                ↓
Explorable 可探索       ←→          Analyzable 能分析
      ↓                                ↓
Understandable 能理解   ←→          Maintainable 能维护
      ↓                                ↓
Actionable 能决策       ←→          Observable / Evolvable
                                       ↓
                                 Interoperable
```

前段可以相对独立推进，但从 Connected / Graphable 开始，两条路线会越来越紧密。

## 双向反馈原则

不要分别建设“机器系统”和“人类网站”。两者共享同一套事实与关系基础，并彼此暴露缺口。

```text
             Canonical Facts
                   ↓
          Validator / Resolver
                   ↓
              Graph / Engine
              ↙           ↘
     Human-readable      Machine API
            ↓                ↓
       人类实际浏览        Agent / 工具实际查询
            ↓                ↓
          发现问题          发现问题
              ↘           ↙
            Data / Model Feedback
                   ↓
                改 Atlas
```

原则：
- Data 不负责展示。
- Renderer 不发明事实。
- Engine 负责确定性查询与计算，不负责替代语义推理。
- 网页不维护第二份事实数据库。
- Agent 应尽量通过结构化事实、查询和分析能力工作，而不是绕开基础层猜测。

## 当前近期重点

机器路线近期最关键的基础仍是：

1. Reference Resolver；
2. Validator；
3. Graph / Backlink Index。

它们既提升机器可靠性，也直接为人类可读路线中的 Connected（看关系）和后续 Mappable（成地图）提供基础。