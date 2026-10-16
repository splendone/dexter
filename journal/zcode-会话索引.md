# zcode 历史会话索引（Dexter 项目）

> 生成时间：2026-09-28 09:1x ｜ 来源：`~/.zcode/cli/db/db.sqlite`（只读查询）
> 说明：本文件是工具流水类索引，供查档用；不含会话正文。

## 结论先说

**Dexter 文件夹本身不保存会话记录。** 该文件夹下与 zcode 有关的只有 `.zcode/{config.json, hooks/, skills/}`——那是**项目配置**（钩子 + 三班技能），不是历史。

zcode 把会话集中存放在用户主目录：

| 位置 | 是什么 |
|---|---|
| `~/.zcode/cli/db/db.sqlite` | **主会话库**（SQLite）。表：`session` / `message` / `part` / `session_entry` / `tool_usage` 等 |
| `~/.zcode/cli/agents/<session_id>/agent_*/` | 子任务的产物：`metadata.json` / `output.txt` / `task.output` |
| `~/.zcode/cli/artifacts/<session_id>/` | 会话过程产物（文件快照等） |
| `~/.zcode/cli/rollout/model-io-<session_id>.jsonl` | 模型 IO 流水（近期的三个：无会话 / 14593813 / 子任务 b913975f） |
| `~/.zcode/cli/log/zcode-YYYY-MM-DD.jsonl` | 按天的运行时日志（09-24 ~ 09-28） |
| `~/.zcode/cli/exec/<session_id>/` | 会话内的 bash 执行记录 |

**Dexter 的项目 ID**：`proj_users-splendone-documents-9--dexter`
（父目录"数字专家"的项目 ID：`proj_users-splendone-documents-9`）

## 会话清单

按 `session.directory` 过滤"数字专家"路径，共 **15 条**（主会话 3 + 子任务 12）。

### 一、主会话（3 条）

| 会话 ID | 类型 | 目录 | 标题 | 起止 | message / part / tool |
|---|---|---|---|---|---|
| `sess_5fa0f727-3bef-461e-aca9-9e84b3f6fd69` | interactive | 数字专家 | 每日8点具身智能晨报 | 09-27 22:06 → 09-28 08:13 | 41 / 205 / 72 |
| `sess_14593813-8e28-4955-ad68-f84a5fde6b15` | fork（父=5fa0f727） | 数字专家 | **Dexter每周五17点复盘班** | 09-27 22:14 → 09-28 08:50 | 132 / 677 / 246 |
| `sess_5da85850-0218-45a9-9ba4-00dfca0c5122` | fork（父=14593813） | 数字专家 | Fork of Fork of 自然人与AI Agent的本质差异 | 09-27 22:35 | 13 / 30 / 0 |

> `sess_14593813` 是**干活的会话**——Dexter 的主要研究班次都跑在这里，12 个子任务全部挂在它名下。
> 三条主会话的首条用户输入都是同一段"自然人与 AI Agent 的本质差异"文本，说明它们是从更早那次对话 fork 出来的（fork 会把父会话上下文作为种子带过来）。

### 二、子任务会话（12 条，全部由 `sess_14593813` spawn）

目录均为 `/Users/splendone/Documents/非凡/9-项目/数字专家/Dexter`。

| 会话 ID（后缀） | 子任务 | 时间 | message / part / tool |
|---|---|---|---|
| `…fa3e095e` | 争论账本缺口一：端到端阵营在 LIBERO-Pro 上的同期数字 | 07:30 → 07:35 | 9 / 37 / 8 |
| `…02d118c4` | LIBERO-Pro 基准核查 | 07:30 → 07:31 | 4 / 8 / 2 |
| `…405e2dee` | 数据集许可核查 | 07:30 → 07:30 | 4 / 8 / 2 |
| `…fbf0fe28` | 同路线竞品盯仓 + PolyUMI 定位 | 07:30 → 07:37 | 20 / 98 / 30 |
| `…c4777126` | π0 全文精读草稿 | 07:30 → 07:31 | 4 / 9 / 3 |
| `…d26437ff` | 争论账本缺口三：触觉的边际价值 + 触觉×合成数据空白 | 07:30 → 07:35 | 9 / 41 / 12 |
| `…70f887aa` | LIBERO-Pro 基准核查（第二轮） | 07:38 → 07:44 | 18 / 80 / 19 |
| `…bb0c81ef` | 数据集许可核查（第二轮） | 07:38 → 07:42 | 10 / 47 / 15 |
| `…3e85c38c` | π0 全文精读草稿（第二轮） | 07:45 → 07:49 | 12 / 51 / 14 |
| `…8bfd50d6` | 会签前复核 | 08:08 → 08:20 | 26 / 124 / 33 |
| `…c519cc7d` | 会签前复核（短） | 08:08 → 08:09 | 4 / 8 / 2 |
| `…b913975f` | 会签前复核 | 08:22 → 08:35 | 15 / 71 / 24 |

> 完整 ID 前缀为 `sess_subagent_agent_`。子任务的产出同时落在 `~/.zcode/cli/agents/sess_14593813-…/agent_<id>/output.txt`。

## 查档方法

```bash
# 列出 Dexter 项目下的全部会话
sqlite3 ~/.zcode/cli/db/db.sqlite \
  "SELECT id, datetime(time_created/1000,'unixepoch','localtime'), title
   FROM session WHERE directory LIKE '%数字专家%' ORDER BY time_created;"
```

会话正文不在 `message.data` 里，而在 `part` 表（`type='text'` 的 `text` 字段）；
`message` 只存 role / 时间 / 模型 / token 等元数据，两表用 `message_id` 关联。

## 未纳入本次索引

- **当前这次会话**（`CODEBUDDY_SESSION_ID=f59c46fc-…`，即"画像定格 / 建专家包"那次）**尚未落库**——查询时库里查不到，应在会话结束后写入。
- 父目录"数字专家"下其他项目的会话未列出（本索引只覆盖 Dexter 相关）。
