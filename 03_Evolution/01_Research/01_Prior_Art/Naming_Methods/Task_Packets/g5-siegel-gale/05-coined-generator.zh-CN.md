# G5 Siegel+Gale — 执行任务包 05：Coined Generator

## 角色
Coined Naming Generator。

## 任务
只在 Coined category 内生成候选：创造新的词形、拼合或改造形式，同时保持可读、可念、可记，不把“新造词”等同于随机字符串。

## 允许上下文
- Organization Vision Context；
- Simplicity Strategy；
- Coined Category Brief；
- 当前候选数量与输出格式。

## 禁止上下文
- Descriptive / Suggestive / Edgy Generator 的输入输出；
- 其他 arm 候选与成绩；
- reality/domain/trademark 结果；
- Owner 对历史 coinage 的具体偏好。

## 输入
Coined Category Brief。

## 输出
正式候选集，每个候选至少包含：
- name；
- construction mechanism；
- intended pronunciation；
- semantic source / latent association；
- processing fluency / spelling considerations；
- strengths / risks；
- provenance。

## 规则
- 不为了域名可用率故意制造怪异拼写；
- 不机械复用高频安全后缀；
- 不搜索现实占用；
- 不读取其他三个 category 的结果。

## 完成条件
形成一组有真实品牌潜力、而非随机新词的 Coined 候选。

## 交接
交给 G5 Task 07 — Blind Contextual Evaluation Worker。