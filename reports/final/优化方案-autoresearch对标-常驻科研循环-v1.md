# 优化方案 · 对标 autoresearch 的工程解析(常驻科研循环侧)v1.0

> **状态**:**✅ 已签发 v1.0**(2026-10-16,Dexter 自审签发,委托人授权)——**活文档**,
> 重审见文末。**签发前会签自查复核:独立子任务 Verdict=FAIL → 6 处实质问题全部修正
> (4 计数/措辞 + 2 归属错)→ 结论方向零改动**(详见文末「复核记录」)。
> **署名链**:起草 = Dexter(2026-10-16)| 复核 = **会签前自查复核**(独立子任务 +
> 异检索路径 jsDelivr 镜像 + 外部交叉源 `/license` API,见文末)| 签发 = **Dexter
> (2026-10-16,委托人授权自审签发)**。
> **甲档已同批落地**:`journal/rounds.tsv`(新建)+ `heartbeat.md`(增两处);
> **乙档 P-015~P-018 已入 `proposals.md` 待批**。
> **触发**:委托人 2026-10-16 指令——「工程解析 `github.com/karpathy/autoresearch`,
> 参考这个项目,优化本地 Dexter 这个全天候自动科研智能体」。
> **上位依据**:`AGENTS.md`(v1.4)、`goals.md`、`proposals.md`、
> `reports/final/优化方案-外部对标与自我诊断-v1.md`(2026-10-08)、
> `designs/检索式策略设计空间自主搜索与可信测量-规格书-v0.1.md`(2026-10-15)。
> **产出性质**:本件是**制度层**的诊断与优化方案,**不是**文献/技术产物;
> 其宪法与技能级改动一律走 `proposals.md` 待批,**不在本件内自行生效**。
>
> **⚠️ 与既有工作的边界(先读,防重复劳动)**:
> - 2026-10-15 的 G2 第二份规格书**已**把 autoresearch 的**三文件分工 / harness 冻结 /
>   固定预算 / keep-discard**用于**实验侧**——即「Dexter 将来要跑的那个自主搜索实验
>   该怎么搭」。本件处理的是**组织侧**——「Dexter 自己这个常驻科研循环该怎么改」。
>   **两者对象不同、不重复**;本件对实验侧的机制不再复述,只引用。
> - 2026-10-08 优化方案对标的是 `system_prompts_leaks`(Agent 系统提示词),
>   已提炼 M1–M10 十条机制并落地甲档 5 项、乙档 P-006~P-010。本件**新增的机制
>   若已被上述两条覆盖,一律标注「已覆盖」而不重复立提案**(见 §2 判定列)。

---

## 0. 摘要与结论

- **autoresearch 的真正价值不在"AI 自己跑实验"这个口号,而在四个**代码级**的
  工程决策**:①**固定预算作为控制变量**(不只是超时上限——所有学习率/权重衰减
  调度都以 `progress = 已用训练时间 / TIME_BUDGET` 归一化,见 `train.py` L555);
  ②**冻结的评测与固定的验证分片**(`prepare.py` 的 `evaluate_bpb` 标 "DO NOT CHANGE",
  验证集固定为最后一个分片且从训练集剔除);③**二元判定 + git 回退**(改进则
  advance,否则 reset);④**上下文卫生**(输出重定向到文件,只 grep 关键两行回读)。
- **对 Dexter 的净增量 = 6 条机制**(由 §2 表里 **10 条缺口**收敛而来;其中
  **2 条高价值**),落到 **4 条提案(P-015~P-018)+ 1 件甲档产物(A1)**:
  - **高** —— **①轮次二元判定与"在制"到期**(直击当前最大风险面:图谱系列 9 件
    持续"在制"而无交付)→ P-015;**②卡住时的升级阶梯**(补"有目标但卡住"这一
    **当前无规则覆盖**的中间态——Dexter 只有"无目标 → 停工",没有"有目标但推不动
    → 怎么办")→ P-016。
  - **中** —— ③结构化轮次账 → 甲档 A1;④判据版本钉(让自审签发的"评分标准"
    可审计)→ P-018;⑤上下文卫生 + fast-fail + 影响面控制 → P-017;
    ⑥硬/软约束显式分级 + 简洁性判据 → P-017。
- **不采纳 3 条**(附理由,§3 丙档 N1/N2/N5):**单一标量指标**(研究价值不可
  标量化 + Goodhart 风险——这是与 autoresearch **最本质的分歧**,不是能力不足)、
  **NEVER STOP 的"永不停"**(与价值门冲突,Dexter 保留停工权)、
  **复制其代码**(许可不明)。**另 2 条不适用**(N3 分支隔离 / N4 依赖冻结,
  无对应工作面)。
- **一句话结论**:autoresearch 可迁移的是**"如何让一个自主循环不骗自己"的结构**,
  不可迁移的是**"用单个数字度量进度"的做法**。Dexter 该学它的**纪律与账本**,
  不该学它的**指标**。

---

## 1. 工程解析:autoresearch 到底是什么(一手源码级,2026-10-16 实抓)

### 1.1 仓库事实

| 项 | 值 | 来源 |
|---|---|---|
| 仓库 | `karpathy/autoresearch` | GitHub API |
| 星标 / fork | **98,011★ / 13,585 fork** | GitHub API `stargazers_count` / `forks_count`(2026-10-16 实抓) |
| 创建 / 最后推送 | 2026-03-06 / **2026-03-26**(此后停更) | GitHub API `created_at` / `pushed_at` |
| 默认分支 | **`master`**(非 `main`) | GitHub API `default_branch` |
| 体积 | 530 KB | GitHub API `size` |
| 跟踪文件 | **10 个**:`.gitignore` / `.python-version` / `README.md` / `analysis.ipynb` / `prepare.py` / `program.md` / `progress.png` / `pyproject.toml` / `train.py` / `uv.lock` | Git Trees API `?recursive=1`(`truncated:false`) |
| **许可** | **README 正文写 "MIT",但仓库内无 `LICENSE` 文件;GitHub `/license` API 返 404、元数据 `license: null`** | 两处实抓交叉 |

> **⚠️ 许可警示(承 10-15 轮,本轮复核确认)**:**不得断言"MIT 已核实"**——
> MIT 只出现在 README 文本里,**没有许可证文件承载**。任何人复用其代码前须先向
> 作者确认。本件**只取机制、不复制代码**,故不受此限,但该事实必须写明。
> **本件的"星标 98,011"与 10-15 轮记录的 97,940 一致增长**(同一仓库,不同时点)。

**⚠️ 文件清单的一处澄清(复核补正)**:README 称"只有**三个**文件要紧",但仓库
**实际跟踪 10 个文件**——除三件外还有 `analysis.ipynb`(8,208 B,结果分析笔记本)、
`progress.png`(252,961 B,结果图)、`pyproject.toml` / `uv.lock`(依赖)、
`.gitignore` / `.python-version`。**"三文件"是叙事简化,不是仓库实况**;
§1.2 的"三分权限"只覆盖那三件,**不意味着仓库只有三件**。

### 1.2 三个文件与权限边界

README 称"只有三个文件要紧",实际**权限是三分的**(`program.md` L11–L31 逐字规定):

| 文件 | 体量 | 谁改 | 内容 | 执行约束 |
|---|---|---|---|---|
| `prepare.py` | 15,043 B | **谁都不改** | 常量、数据下载、BPE 分词器、dataloader、**评测函数** | program.md:「**Modify `prepare.py`.** It is read-only」+ 函数头 `# Evaluation (DO NOT CHANGE — this is the fixed metric)` |
| `train.py` | 26,230 B(630 行) | **agent 唯一可改** | GPT 模型、Muon+AdamW 优化器、训练循环、调度 | 「Everything is fair game」 |
| `program.md` | 7,039 B | **人改** | 给 agent 的指令(README 称"essentially a super lightweight skill") | 「This file is edited and iterated on by the human」 |

**⚠️ 工程诚实点(本件新增的观察,10-15 轮未提)**:`prepare.py` 的"只读"**是约定,
不是机制**——代码里**没有任何校验**(无 SHA256、无 checksum、无文件权限、无只读挂载;
独立复核对 `prepare.py` / `train.py` 跑 `grep -niE "sha256|checksum|hashlib|chmod|read.?only"`
**零命中**)。防线只有一条:agent 遵守 `program.md` 的文字指令。
**⚠️ 而 README 的 Quick start 更把这条防线主动撤掉**——逐字要求使用者
"Simply spin up your Claude/Codex or whatever you want in this repo (**and disable
all permissions**)"。**即:平台层被要求关闭技术防线,只靠 agent 守约**。
**换言之,autoresearch 的防作弊保证是社会的,不是技术的**——这比"代码里没写校验"
是更硬的证据。Dexter 的 G2 规格书已提出"harness 冻结 + SHA256 校验"
(规格书 L101)——**这是对 autoresearch 的改进,而非照抄**;本件在组织侧同样建议
"版本钉"(§3 乙档 P-018)而非"信任约定"。

### 1.3 源码里真正在起作用的设计(README 只给结论,实现细节在代码里)

以下 8 条**全部以代码行为锚**。**说明(复核补正)**:其中 (a)(c)(d) 的**结论**
README 确有提及(固定 5 分钟预算 / val_bpb 词表无关),本节的增量是**实现细节**
——即"这件事是**怎么**做到的、少哪一步就不成立"。

**(a) 固定预算 = 控制变量,不是秒表。**
`train.py` L555:`progress = min(total_training_time / TIME_BUDGET, 1.0)`;
**学习率 warmup/warmdown(L518–525)与权重衰减(L531–532)都是 `progress` 的函数**。
**⚠️ 但 Muon 动量不是**——L527–529 `get_muon_momentum(step)` 只依赖 `step`,
不随预算归一化(循环内 L557 亦以 `step` 调用)。
→ **预算归一化了主要调度(学习率与权重衰减),但不是全部**;核心洞察仍成立:
"5 分钟跑完"不是时间限制,而是**把不同配置压到同一坐标轴上比较**。
这是整个设计里最关键、也最容易被读漏的一步。

**(b) 时间会计排除编译预热。**
`train.py` L578–579:`if step > 10: total_training_time += dt`——前 10 步不计入预算
(注释 L602 明写 "so we don't count compilation")。→ 预算测的是**稳态训练时间**,
不是进程墙钟。**没有这一步,固定预算就不可比**。

**(c) 冻结评测 + 固定验证分片。**
`prepare.py` L31 `TIME_BUDGET = 300`、L32 `EVAL_TOKENS = 40 * 524288`;
L43 `VAL_SHARD = MAX_SHARD`(钉死最后一个分片);
L260–261 训练集**显式剔除**该分片(`parquet_paths = [p for p in ... if p != val_path]`);
L344–365 `evaluate_bpb` 用**固定 `MAX_SEQ_LEN`** 保证跨配置可比。
→ **"可比的度量"需要三件事同时成立**:评测函数冻结、验证集固定且不泄入训练、
序列长度固定。少一样,比较就失效。

**(d) 度量选择本身是防作弊设计。**
用 **bits-per-byte 而非 bits-per-token**:分母是**目标字节数**,与词表大小无关
(L346–350 注释逐字:"vocab size-independent evaluation metric … so results are
comparable across configs")。→ 防的是"改小词表把 loss 做好看"这类**度量套利**。
**这是一个直接可迁移的教训:指标必须对"最容易被优化的那个自由度"免疫。**

**(e) fast-fail。**
`train.py` L569–572:`if math.isnan(train_loss_f) or train_loss_f > 100: print("FAIL"); exit(1)`。
→ 明显发散的运行**立刻终止**,不烧完预算。

**(f) keep/discard + git 回退,结果账不入库。**
`program.md` L103–104:改进则 advance,否则 `git reset`;L102 + `.gitignore` L22–23:
`results.tsv` **不 commit**。→ 实验账**与代码历史解耦**:账本记"试了什么、结果如何",
代码历史只留"活下来的那些"。**这两件事分开,是让 `git diff` 保持可读的关键**。

**(g) 上下文卫生:输出重定向,只回读两行。**
`program.md` L99–100:`uv run train.py > run.log 2>&1`,并**逐字**禁止:
"do NOT use tee or let output flood your context";L100 只 `grep "^val_bpb:\|^peak_vram_mb:" run.log`。
→ **长输出不进上下文,只有判决性字段进上下文**。这是**省 token 的工程手段**,
不是风格偏好。

**(h) 超时即失败,崩溃分级处置。**
`program.md` L108:超过 10 分钟(预算 2 倍)→ kill,**当作失败**(discard + revert);
L110:崩溃分两类——"蠢且易修"(typo/import)→ 修了重跑;"想法本身坏了"→ 记 `crash`
跳过。→ **失败被结构化**(crash 是一等状态,不是耻辱),且**有止损上限**。

**另三条组织层设计(README + program.md)**:

**(i) 简洁性判据(反复杂度)。**
`program.md` L37:等效果下更简者胜;「删代码换同等效果 = 一定保留」;
「0.001 提升 + 20 行 hacky 代码 = 不值」。→ 把**维护成本**计入"是否保留"的判据。

**(j) `program.md` 是"研究组织代码",人迭代它而非迭代 agent。**
README 逐字:「you are programming the `program.md` Markdown files that provide
context to the AI agents and **set up your autonomous research org**」;
「it's obvious how one would iterate on it over time to find the **"research org
code"** that achieves the fastest research progress, how you'd add more agents to
the mix」。→ **被优化的对象是"组织本身"**,agent 是执行体。这一条与 Dexter
的处境**高度同构**。

**(k) NEVER STOP + 卡住时的升级阶梯。**
`program.md` L112 逐字:"do NOT pause to ask the human if you should continue …
The human might be asleep … you are autonomous. **If you run out of ideas, think
harder — read papers referenced in the code, re-read the in-scope files for new
angles, try combining previous near-misses, try more radical architectural changes.**"
→ **它给了"没想法"一条四级阶梯,而不是让人去问**。

---

## 2. 差距映射(逐条对 Dexter)

判定三档:**已覆盖**(既有制度/10-08 优化方案已含,不重复)/ **缺口**(本件提议)/
**不可迁移**(对象不同或违反 Dexter 边界)。

| # | autoresearch 机制 | 锚 | Dexter 现状 | 判定 |
|---|---|---|---|---|
| 1 | 冻结评测 + 固定验证分片 | `prepare.py` L339–365 | 有"外部交叉源硬规则"(宪法「自审签发与滚动重审」第 4 点)+ 独立子任务复核(P-007) | **已覆盖(对象层)** |
| 2 | **判据本身可被同一个 agent 修改** | `program.md` L29–31 | **复核标准(`re-review` 技能)与被审对象同属一个 agent;一次复核用了哪版判据不留痕** | **缺口 → P-018 判据版本钉** |
| 3 | 固定预算**归一化**主要调度 | `train.py` L555 | 只有"估算消耗档位(低/中/高)"(P-006),预算是**上限**不是**坐标轴** | **缺口 → P-015 工作量归一化** |
| 4 | 单一可比指标(val_bpb) | `prepare.py` L346–350 | 无单一指标;产出三态**无数量** | **不可迁移 → 以轮次账替代(§3 丙档 N1)** |
| 5 | keep/discard + git 回退 | `program.md` L103–104 | **无 discard**;drafts 只增不减;**图谱系列 9 件持续"在制"** | **缺口(高)→ P-015** |
| 6 | `results.tsv` 结构化实验账 | `program.md` L66–88 | 产出账是散文;轮次记录堆在 `latest.md` 顶部 | **缺口 → 甲档 A1 轮次账** |
| 7 | 上下文卫生(重定向 + grep) | `program.md` L99–100 | **无明文**;大量原始输出直接进上下文 | **缺口 → P-017** |
| 8 | fast-fail | `train.py` L569–572 | 无 | **缺口(轻)→ P-017** |
| 9 | 超时即失败(>2× 预算 → discard) | `program.md` L108 | 有"不硬撑半成品",但半成品仍落 `drafts/` 且**计入进度** | **部分覆盖 → P-015** |
| 10 | **卡住时的四级升级阶梯** | `program.md` L112 | 只有"无目标 → 停工"(价值门);**"有目标但推不动"无规则** | **缺口(高)→ P-016** |
| 11 | `program.md` = 研究组织代码,人迭代 | README | 有 `proposals.md` → `AGENTS.md` 迭代链,但**未把"组织代码"立为一等优化对象** | **部分覆盖 → 本件即其实例** |
| 12 | 单文件改动 / 影响面可控 | README Design choices | P-012 派子 agent,但无"每轮触及文件数"纪律 | **轻量缺口 → P-017** |
| 13 | 硬/软约束显式分级(预算硬 / VRAM 软) | `program.md` L35 | 无分级 | **轻量缺口 → P-017** |
| 14 | 崩溃是一等状态(crash) | `program.md` L110 | `honor.md` 只记**过失**;"失败的尝试"无处登记 | **缺口 → 甲档 A1 轮次账 status 列** |
| 15 | 运行标签 / 分支隔离 | `program.md` L9–10 | 单一工作区,无分支工作流 | **不可迁移** |
| 16 | 依赖冻结(不许装新包) | `program.md` L30 | 无代码依赖面 | **不可迁移** |
| 17 | 简洁性判据(反复杂度) | `program.md` L37 | 有"索引 ≤200 行 / ~25KB"等体积纪律(P-009),**无通用简洁性判据** | **部分覆盖 → P-017 附条** |

**映射后的净结论**:17 条里 **1 条已覆盖**(#1)/ **3 条部分覆盖**(#9 / #11 / #17)/
**10 条真缺口**(#2 #3 #5 #6 #7 #8 #10 #12 #13 #14)/ **3 条不可迁移**(#4 / #15 / #16)。
10 条缺口**收敛为 6 条机制**(见 §0),其中 2 条(**#5 无 discard**、**#10 卡住无阶梯**)
**直击 Dexter 当前最痛的失败模式**。

---

## 3. 优化方案(三档)

### 甲档 · 立即实施(绿色 / 结构性,本件同批落地)

| 编号 | 产物 | 补的缺口 | 验收(怎么算成) |
|---|---|---|---|
| **A1** | `journal/rounds.tsv`(轮次账,制表符分隔) | #6 / #9 / #14 | 表头 **9 列**(见下);**回填最近 6 轮**并各带来源指针;此后每轮检查点追加一行。**✅ 本件同批已落地**(7 行:表头 + 6 轮) |
| **A2** | `heartbeat.md` 增两处:①每日触发点第 5 步追加"轮次账"→②新增「轮次账」与「卡住时升级阶梯(**待批 P-016**)」两节 | #6 / #10 | 触发点读得到;`heartbeat.md` 自有"加一行 = 加一个常态检查项"规则,属其设计内的增行。**✅ 本件同批已落地** |

**`journal/rounds.tsv` 列定义**(借 `results.tsv` 的 5 列结构,扩到 Dexter 的语义):

```
round	date	goal	hypothesis	action	artifact	verdict	cost	note
```

| 列 | 含义 | 取值 |
|---|---|---|
| `round` | 轮次号(自 2026-10-16 起从 001 连续编号) | 整数 |
| `date` | 绝对日期 | `YYYY-MM-DD` |
| `goal` | 本轮推哪个目标 | `G1`–`G5` / `制度` / `—` |
| `hypothesis` | **本轮要验证什么**(写不出 → 不该开轮,反空转硬规则) | 一行 |
| `action` | 做了什么 | 一行 |
| `artifact` | 产出了什么(**路径或"无"**) | 路径 / `无` |
| `verdict` | **二元判定** | `advance` / `revert` / `noop` / `crash` |
| `cost` | 估算消耗档位 | `低` / `中` / `高` |
| `note` | 备注(如"超时未完成,不计进度") | 一行 |

> **为什么是 TSV 而不是 Markdown 表**:借 `results.tsv` 的理由——**可被脚本统计**,
> 从而让"空转率 / 交付率 / revert 率"变成**可算的数**,而不是感觉。

### 乙档 · 立提案待批(宪法 / 技能级,写进 `proposals.md`)

| 编号 | 提案 | 拟改文件 | 对应缺口 |
|---|---|---|---|
| **P-015** | **轮次二元判定与"在制"到期**:每轮检查点必须给本轮**二元判定**(`advance`/`revert`/`noop`/`crash`);**"在制"设到期**(超期未交付须在周报解释并二选一:降级或关项);**超时轮次的产出不得计入进度** | `AGENTS.md`「目标制与产出导向」+ `.zcode/skills/goal-loop` | #5 #9 |
| **P-016** | **卡住时的升级阶梯**(补停工条件):在"无目标可推进 → 停工"**之前**插入中间态处置——**有目标但推不动**时,按四级阶梯升级:①重读本轮 in-scope 原文 → ②组合既往 near-miss → ③换更激进的路径 → ④拆题/改判据。**阶梯用尽仍不动 → 才进价值门** | `AGENTS.md`「常驻循环制」停工条件 + `.zcode/skills/shift-start` | #10 |
| **P-017** | **上下文卫生 + fast-fail + 约束分级**:①长输出**一律落文件**,只回读判决性字段(禁整段读入);②**fast-fail**:本轮过半预算仍无产出 → 中止并记 `crash`,不续烧;③约束**显式分硬/软**(硬:证据纪律、红线、预算;软:篇幅、格式、颗粒度);④**简洁性判据**:等效果下更简者胜,删除换等效 = 保留 | `AGENTS.md`「常驻循环制」+ `.zcode/skills/shift-start` | #7 #8 #12 #13 #17 |
| **P-018** | **判据版本钉**:每次会签前自查复核**须记录所用判据版本**(复核清单 / 验收判据的版本号或哈希),写入复核记录;**判据的修改须走 `proposals.md`**(不得在复核过程中临时放宽) | `AGENTS.md`「自审签发与滚动重审」+ `.zcode/skills/re-review` | #2 |

### 丙档 · 不采纳 / 不适用(附理由,诚实)

| 编号 | 事项 | 处置 | 理由 |
|---|---|---|---|
| **N1** | **单一标量指标**(val_bpb 类比) | **不采纳** | ①Dexter 的产出是**判断、规格、稿件**,其价值**不可标量化**——硬造一个数会把"看起来有进展"当成进展,正是**反空转硬规则要防的**;②任何单一指标一旦成为目标就会被优化(Goodhart),而 Dexter 的指标**没有第二个指标来制衡**;③**但接受其"可比性"意图** → 用**结构化轮次账**(甲档 A1)让轮次**可对照**,而不是让价值**可打分**。**这是本件与 autoresearch 最本质的分歧,是判断而非能力不足。** |
| **N2** | **NEVER STOP 的"永不停"** | **不采纳** | 与宪法价值门**直接冲突**:autoresearch 的"没想法就 think harder"**只在有指标可优化时成立**(val_bpb 永远可以再降一点);Dexter 的"无目标可推进"是**真·无事可做**,此时续轮 = 灌水。**只取其"卡住时升级"部分**(P-016),不取其"永不停"。 |
| **N3** | 运行标签 / 分支隔离 | 不适用 | Dexter 无 git 分支工作流,单一工作区即隔离单元。 |
| **N4** | 依赖冻结(禁装新包) | 不适用 | 无代码依赖面;对应物是"不得自行新增外部工具",已在红线内。 |
| **N5** | 复制其代码 | 不采纳 | **许可不明**(README 写 MIT 但无 LICENSE 文件,§1.1)。本件**只取机制**。 |

---

## 4. 本方案自身的验收判据

1. **甲档**:`journal/rounds.tsv` 存在且含表头 + ≥5 行回填;`heartbeat.md` 可读得到;
2. **乙档**:P-015~P-018 进 `proposals.md`;委托人批准后 **30 天内**在 `AGENTS.md`
   修订史留痕(版本号 + 理由);
3. **效果判据(30 天后复盘)**:
   - ① **空转可算**——`rounds.tsv` 里 `noop` 占比能直接算出(证明轮次账落地);
   - ② **在制不再无限**——任取一件 draft,能说出它的**到期日与处置**(降级/关项);
   - ③ **卡住有路径**——至少 1 轮按 P-016 阶梯升级而非直接停工;
   - ④ **判据可追溯**——抽一次复核,能查出它用的是哪版判据(P-018)。

---

## 5. 残余不确定性(诚实)

1. **机制迁移的效果未经实测**——Dexter 无 A/B 环境;§2 的"判定"与"净增量"是
   **判断,不是测量**。
2. **autoresearch 的机制高度依赖"有一个好指标"**——它的 8 条代码级设计里有 **4 条**
   ((c) 冻结评测与固定分片、(d) bpb、(f) keep/discard、(e) fast-fail)**以"存在可比
   标量"为前提**(注:(c) 的"冻结评测"与"固定验证分片"在 §1.3 里是**同一条**,
   此处不拆分计数)。Dexter **没有**这个前提,故能迁的只有**结构与纪律**,
   不能迁**度量方式**。本件的取舍即由此而来。
3. **"轮次"的边界未定义死**——一轮 = 一次检查点到下一次检查点,还是 = 一个子任务?
   本件按**前者**起草(与 `latest.md` 的轮次条目对齐),若委托人另有定义须调整。
4. **许可事实可能变化**——若作者后续补上 LICENSE 文件,§1.1 的警示应作废重审。
5. **本件未做**:未跑任何实验验证轮次账的实际可用性(它刚建,无历史数据);
   P-015~P-018 的具体条文措辞待批时再细化。

---

## 附录 A · 抓取记录(2026-10-16)

- **入口**:`https://api.github.com/repos/karpathy/autoresearch`(元数据)+
  `/contents/<path>?ref=master`(文件内容,base64 解码)。
- **⚠️ 环境事实(诚实登记)**:本轮 `raw.githubusercontent.com` **直连超时
  (HTTP 000 / exit 28)**,改用 GitHub Contents API 取全文——**内容来源仍是
  GitHub 官方 API,非二手转述**。
- **实抓文件**(字节数):`README.md` 8,039 / `program.md` 7,039 /
  `prepare.py` 15,043 / `train.py` 26,230(630 行)/ `pyproject.toml` 543 /
  `.gitignore` 279 / `.python-version` 5。
- **许可核查**:`/repos/karpathy/autoresearch/license` → **HTTP 404**;
  元数据 `license: null`;仓库文件列表无 `LICENSE`。**与 README 正文 "MIT" 冲突**。

## 附录 B · 机制 → 源码锚(逐条可回查)

| 机制 | 锚点 |
|---|---|
| 常量(预算 / 序列长 / 评测量) | `prepare.py` L27–32 |
| 固定验证分片 + 训练集剔除 | `prepare.py` L43, L258–263 |
| 冻结评测函数 | `prepare.py` L339–365(头注 "DO NOT CHANGE") |
| bpb 与词表无关 | `prepare.py` L346–350 |
| 固定预算归一化调度 | `train.py` L518–532, L555 |
| 时间会计排除编译 | `train.py` L578–579, L602–604 |
| fast-fail | `train.py` L569–572 |
| 摘要输出字段 | `train.py` L621–630 |
| CAN / CANNOT 边界 | `program.md` L26–31 |
| 简洁性判据 | `program.md` L37 |
| 首跑必为 baseline | `program.md` L39 |
| results.tsv 五列结构 | `program.md` L66–88 |
| keep / discard + git | `program.md` L103–104 |
| 上下文卫生 | `program.md` L99–100 |
| 超时 / 崩溃分级 | `program.md` L108–110 |
| NEVER STOP + 升级阶梯 | `program.md` L112 |
| 三文件分工 / 组织代码 | `README.md`(How it works / Design choices) |

---

## 复核记录(会签前自查复核 · 独立子任务,2026-10-16)

**复核方式**:独立子任务(**未参与起草**),任务为"找错,只报实际打开核实过的";
**异检索路径**——起草用 GitHub **Contents API**(base64 解码),复核改用
**Git Trees API(`?recursive=1`)+ jsDelivr 第三方镜像**(`cdn.jsdelivr.net/gh/karpathy/autoresearch@master/…`,
HTTP 200,逐行读原文并记 md5);**外部交叉源 ≥1**(jsDelivr 镜像 + `/license` API);
**四类错误扫描**(数字-结论错配 / 不同轴并列 / 归属错 / 无源数字)。

**Verdict:FAIL**(首轮)。**6 处实质问题全部已修正**:

| # | 类别 | 问题 | 处置 |
|---|---|---|---|
| 1 | 数字-结论错配 | §1.1 写"跟踪文件 **6 个**",却列出 **10 个** | **已改为 10 个**并补"三文件是叙事简化"澄清段 |
| 2 | 数字-结论错配 | §0 称"净增量 6 条"与 §2"7 条真缺口"矛盾 | **已统一**:17 条 = 1 已覆盖 / 3 部分覆盖 / **10 缺口** / 3 不可迁移;10 缺口**收敛为 6 条机制** |
| 3 | 数字-结论错配 | 写"另**两**条组织层设计"却列 **3** 条 | **已改为"另三条"** |
| 4 | 数字-结论错配 | §0 称"**3** 条明确不采纳"与丙档 **N1–N5(5 行)** 集合错配 | **已按正文标签重写**:不采纳 3 条(N1/N2/N5)+ 不适用 2 条(N3/N4) |
| 5 | **归属错** | §1.3(a) 把 **Muon 动量**说成 `progress` 的函数 | **已改**:LR(L518–525)+ 权重衰减(L531–532)是 `progress` 的函数;**Muon 动量(L527–529)是 `step` 的函数**,§2 行 3 同步改"主要调度" |
| 6 | 归属错(轻) | §1.3 标题"(README **没说**、代码做了的)"过强 | **已改**为"README 只给结论,实现细节在代码里",并注明 (a)(c)(d) 结论 README 确有提及 |

**主动探测(复核员提出,已并入正文)**:
1. **补入最硬证据**——README Quick start 逐字要求"**disable all permissions**"
   (平台层主动撤掉技术防线),已补入 §1.2,把 §1.2 的"约定非机制"结论从
   "agent 可能不守约"抬升到"**防线被主动撤除**";
2. **补文件实况**——仓库还带 `analysis.ipynb`(8,208 B)与 `progress.png`(252,961 B),
   已补 §1.1 澄清段;
3. **§5.2 重复计数**——"冻结评测"与"固定验证分片"是同一条 (c),拆开算会把"5 条"
   虚增为"4 条",已合并并加注。

**独立核实为「属实」的关键断言**(供对照):星标 98,011 / fork 13,585 / 创建
2026-03-06 / 最后推送 2026-03-26 / 默认分支 `master` / 体积 530 KB / `license: null`
——**全部与 API 一致**;字节数 README 8,039 / program.md 7,039 / prepare.py 15,043 /
train.py 26,230(630 行)**全部一致**;**许可**——README L90–92 有 "## License / MIT"
但 tree 无 `LICENSE`、`/license` **HTTP 404**、`license: null`(**本件最关键一条,
独立确认成立**);§1.3 全部代码锚点**逐条属实**;**§1.2"只读是约定而非机制"属实**
(独立复核对源码跑 `sha256|checksum|hashlib|chmod|read.?only` **零命中**);
Dexter 侧 `proposals.md` 最新确为 **P-014**、`heartbeat.md:58` 确有增删规则、
`journal/rounds.tsv` **确实不存在**、10-08 优化方案确为**已签发 v1.0**、
`AGENTS.md` 第 4 点确有"外部交叉源硬规则"。

**结论**:复核通过(**修正后**)。**6 处修正中 4 处为计数/措辞精度、2 处为归属错
(已改),0 处涉及结论方向**——§0 的两条高价值缺口(#5 无 discard、#10 卡住无阶梯)、
§3 的 P-015~P-018 与丙档取舍**均未被推翻**。

## 修订记录(活文档)

- **v0.1 → 签发 v1.0(2026-10-16)**:起草 → 会签前自查复核(独立子任务,**Verdict
  FAIL**;异检索路径 = jsDelivr 镜像 + Git Trees API,外部交叉源 = `/license` API)
  → 修正 **6 处**(§1.1 文件计数 6→10;§0 净增量口径与 §2 统一为"17 = 1 已覆盖 /
  3 部分覆盖 / 10 缺口 / 3 不可迁移";"另两条"→"另三条";丙档不采纳集合重写为
  N1/N2/N5 不采纳 + N3/N4 不适用;**Muon 动量归属错**——由 `progress` 函数改为
  `step` 函数;§1.3 标题过强断言收紧)+ 并入 3 条主动探测(README "disable all
  permissions" 硬证据 / `analysis.ipynb` 与 `progress.png` 实况 / §5.2 重复计数合并)
  → 签发。**甲档 A1/A2 同批落地;乙档 P-015~P-018 入 `proposals.md` 待批。**

## 重审记录(活文档)

- 待触发。**触发线**:①本件结论被实际用到(如据 P-015~P-018 改宪法)时先核;
  ②新证据触及本件某条机制归属 / 计数时立即标记"待重审"。
  **重审交叉源须含至少一个外部/原始来源**(不得只靠本地库互证)。
