# 接纳事件（Acceptance Events）

本目录保存 V1 收录的明确审查/决策证据，不是第二套正式对象库。候选经过机器预检、独立语义审核和适用的权限判断，才能记录接纳事件并物化正式对象。

## 决策边界

- `accepted` 需要真实的 `review_required` 前置路由和独立 Reviewer；同一候选不能通过不同 event_id 重复接纳。
- `duplicate` 只是指向既有主体的观察，不执行合并，也不是第二次物化。
- `identity_review_required` 和 `deferred` 不能进入普通接纳路径。
- M2/M3 仍需非普通授权路径及明确批准人；本轮程序没有扩大该权限。
- CI 通过是验证证据，不是语义 Reviewer，更不证明两个角色名代表独立上下文。

## 冻结证据的实际复算

`intake_coverage_audit.py` 对所有验收文件中的 accepted 事件执行同一检查，不再限定首批文件名。正式对象的 `intake_provenance` 应回指 `acceptance_event_id`、`candidate_id`，并保存：

```yaml
reviewed_candidate_blob: <原始候选文件的完整 Git blob SHA>
reviewed_against_commit: <当时用于预检的完整 Git commit SHA>
candidate_executor: <原始候选里的实际 Executor>
```

程序从本地 Git 对象库读取冻结原稿和冻结底库；核对原稿确实位于该提交的候选目录，唯一匹配 candidate_id，再用原始身份状态及当时 Canonical 标识索引复算。不得把当前候选改成 `new` 来虚构历史预检。当前保留候选、正式对象和冻结原稿的外部标识也必须对应；当前仍阻塞的候选不能被事件文字强行接纳。

这是确定性的证据一致性检查，不替代对 Reviewer 身份、上下文独立性、来源充分性或实际授权的审核。Git 仍是完整历史来源，不复制一份冻结对象库。

运行需要包含所引用历史的 Git checkout；浅克隆或不带 `.git` 的源码压缩包不能完成此历史核验，缺证据时返回失败而不猜测。P6 CI 使用 `fetch-depth: 0` 获取历史；程序自身不自动联网拉取。

Schema 保持 `acceptance-event.v1.schema.json` 不变。普通 accepted 事件绑定的新增元数据使用正式对象既有的 provenance 扩展，不重新解释其他高影响接纳合同。
