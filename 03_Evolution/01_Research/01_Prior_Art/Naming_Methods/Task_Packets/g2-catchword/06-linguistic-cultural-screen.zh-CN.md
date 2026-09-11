# G2 Catchword — 执行任务包 06：Linguistic / Cultural Screening

## 角色
Linguistic / Cultural Worker。

## 任务
对 shortlist 做语言、发音、拼写、跨语言与文化风险检查。此步骤关注理解成本、误读、负面联想、目标市场适配，不负责现实公司/商标冲突，也不决定最终名字。

## 允许上下文
- shortlist candidate strings；
- 目标语言 / 市场信息；
- 必要的语言学与文化资料。

## 禁止上下文
- 其他 arm 候选和成绩；
- reality/domain screening 结果；
- Owner 对历史名字的偏好；
- 生成新的候选作为替代。

## 输入
G2 Task 04 输出的 shortlist。

## 输出
每个候选的：
- pronunciation / likely pronunciation variants；
- spelling / recall risks；
- semantic associations；
- cross-language concerns；
- cultural / social concerns；
- Clear / Yellow / Red（仅语言文化维度）；
- confidence 与需要母语专家复核的事项。

## 规则
- 不把机器推断冒充母语者验证；
- 对未覆盖语言明确标注 unknown；
- 不因个人审美淘汰；
- 不搜索或评价商业占用，除非某语言意义本身需要查证。

## 完成条件
shortlist 中每个候选都有语言文化维度的可追溯结论。

## 交接
交给 G2 Task 07 — Contextual Evaluation Worker。