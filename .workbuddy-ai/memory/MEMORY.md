# Dexter 项目 · 长期记忆(WorkBuddy 层)

> 本文件是 WorkBuddy 工作区级记忆,**补充**而非替代事务所自身的台账
> (`decisions.md` / `agenda.md` / `goals.md` / `journal/latest.md` 才是权威)。

## 项目性质

- 工作区 = 「Dexter 数字事务所」——具身智能(操作与灵巧手)方向数字技术研究员。
- 模式:**目标驱动的常驻循环**(读 `journal/latest.md` → `goals.md` → `agenda.md`
  → `honor.md` → `promises.md`);目标台账 `goals.md`(G1–G5);制度宪法 `AGENTS.md`。
- **改宪法与技能须走 `proposals.md` 提案、委托人批准后执行**——不自行修改。

## 2026-10-08 新增的项目约定(制度优化)

- **新增 4 件结构性资产**(开工时可用):
  - `knowledge/index.md` —— 知识总索引(**新卡片入库须同步登记**;每周策展压 ≤200 行);
  - `knowledge/maps/assumptions.md` —— 假设账本(假设只登记不删,证伪触发下游重审);
  - `knowledge/maps/artifact-dependencies.md` —— 产物依赖图(**改一件先查下游**);
  - `heartbeat.md` —— 定时触发点清单(含 **noop 折叠** 与简报**信噪比自评**)。
- **`tests/acceptance.md`** 增"自测执行记录"栏;署名链测试、溯源测试**已实跑通过**。
- **待委托人批准**(`proposals.md`):**P-006~P-010**(成本闸 / 复核异源化 /
  前置门灰度 / 记忆策展与索引纪律 / 证据纪律三补);另有 **P-004**(数字并列守则)仍待批。
- 相关报告:`reports/final/优化方案-外部对标与自我诊断-v1.md`。

## 2026-10-16 新增的项目约定(对标 autoresearch,组织侧)

- **新增轮次账 `journal/rounds.tsv`**(9 列:`round / date / goal / hypothesis /
  action / artifact / verdict / cost / note`)。**每轮检查点必须追加一行**,
  `verdict` 必填(`advance`/`revert`/`noop`/`crash`)。**"轮次"口径 = 一次检查点
  到下一次检查点**。用途:让空转率/交付率变成**可算的数**。
- **`heartbeat.md` 增两处**:检查点第 5 步追加轮次账;新增「轮次账」与
  「卡住时升级阶梯(**待批 P-016**)」两节。
- **待批 4 条**(`proposals.md`):**P-015** 轮次二元判定与"在制"到期 /
  **P-016** 卡住升级阶梯(补"有目标但推不动"的中间态)/ **P-017** 上下文卫生 +
  fast-fail + 硬软约束分级 / **P-018** 判据版本钉。
  **批前不生效**;批后 30 天内进 `AGENTS.md` v1.5。
- **关键判断(不采纳)**:autoresearch 的**单一标量指标**(val_bpb 类比)不迁移——
  Dexter 的研究产出不可标量化,硬造指标会诱发 Goodhart;改以**结构化轮次账**替代其
  "可比性"意图。**其"NEVER STOP 永不停"亦不采纳**(与价值门冲突)。
- **仓库事实留档**:`karpathy/autoresearch` **许可不明**(README 写 MIT 但无 LICENSE
  文件、`/license` 404)——**不得断言"MIT 已核实"**;本机 `raw.githubusercontent.com`
  直连超时,`api.github.com` 可达。
- 相关报告:`reports/final/优化方案-autoresearch对标-常驻科研循环-v1.md`。

## 2026-10-16 新增的项目约定(对标 system_prompts_leaks,第二轮)

> **同库二轮**:该库 2026-10-08 已对标过一次(M1–M10 即出自此库)。二轮**只做增量**,
> 先建去重表;两条边界写死:10-08 **已**取 `code-review`/`loop`/`verify` 的 `SKILL.md`;
> **未**触及 `Meta/muse-code/prompts/reminders/`(二轮主攻处)。
> **本件与 10-08 件同源同库**——已在 `artifact-dependencies.md` 登记:10-08 件若重审,
> 去重表须重核。

- **新增「未销账缺陷」纪律**(甲档已落地):`heartbeat.md` 检查点第 **6 步「未销账核对」**
  + 新节「未销账清单」。**上一轮自己点名而未修的问题,逐条给状态(已修/在修/不修并写明
  理由);被自己点名的缺陷不修完,本轮不算完成**;含未销账缺陷的条目只能标**在制**。
- **新增「档案路由头规则」**(甲档已落地):新档案须带 3 行头(`本档管什么 / 不归本档的
  写去哪 / 生长纪律`)。**例外写死**:`AGENTS.md`(宪法)与 `honor.md`(append-only)**不动**。
  已实际给 `identity.md`/`goals.md`/`agenda.md`/`promises.md` 四档补头。
- **待批 5 条新增**(`proposals.md`,累计待批 **11 条 = P-013~P-023**):
  **P-019** 未销账缺陷规则 / **P-020** 复核强度分档(**含高召回档**)/
  **P-021** 观察者校验与提醒契约 / **P-022** 授权隔离与边界声明 /
  **P-023** 不确定性双向默认 + 提问纪律。
  **⚠️ 建议优先批 P-019 与 P-020**——直击最实病灶(缺陷悬挂 / 图谱在制 / 过失史全为"漏")。
- **关键诊断(留档)**:该库复核分档 caps **非单调**——`low ≤4 < medium ≤15 > high ≤10
  < xhigh ≤15 = max ≤15`(档位沿**范围+验证**两轴变,high/xhigh 为保召回显式 `no verify`)。
  本所复核**单档且偏精确**(10-08 的 M2「存疑即 FAIL」),而**过失史全部是"漏"** → 缺高召回档。
- **本所自犯其批评过的毛病**:子代理复核者**有写权限**(只读靠约定),与所批评的
  autoresearch「防作弊是约定而非机制」同构 → **P-022**(声明式 `disallowedTools` 才是机制)。
- **抓取路径留档**:`raw.githubusercontent.com` 超时;`api.github.com`/`cdn.jsdelivr.net`
  仅在 `dangerouslyDisableSandbox: true` 下可达;jsDelivr/ungh **均回 301/302** 到不可达 raw
  → 复核改用 `git/blobs/<sha>` + `github.com` blob 网页页。
- **许可对比留档**:`system_prompts_leaks` = **CC0-1.0,有真 LICENSE 文件**(7,049 字节)、
  `/license` 正常;对照 autoresearch 无 LICENSE、`/license` 404、`license: null`。
- 相关报告:`reports/final/优化方案-对标system_prompts_leaks-观察者与复核分档-v1.md`。
