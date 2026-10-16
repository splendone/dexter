> **⑨ RedTeamReviewer 产物 · 独立子任务(未参与起草)· dry-run · 2026-10-09**

# 红队审稿 · paper-R3-NeuTraL(validate-pipeline-20261009)· 2026-10-09

## 0. 预演元信息

- **被审草稿**:`reports/drafts/validate-pipeline-20261009/08-paper/`(`main.tex` + `sections/*.tex` 7 篇 + `refs.bib` + `traceability.md`)。版本/commit:**不可得** —— `04-sim/exp-VP01/code-commit.txt` 内容为 `NOT-A-GIT-REPO: dry-run placeholder, snapshot 2026-10-09T13:00:00Z`;本目录亦非 git repo。故本草稿**无版本指纹**,审稿结论无法钉到某个 commit(本身即为可复现性缺陷,见 R3-4)。
- **交叉核材料(全部实开文件核到,不信任何自述)**:
  - ☑ ⑥ `06-audit/results-audit.md`(签发 **❌ 不放行**,数据 PLACEHOLDER)
  - ☑ ④ `04-sim/exp-VP01/{results.json, config.yaml, run.sh, seeds.txt, env-lock.txt, code-commit.txt}`
  - ☑ ① `01-gap/gap-candidates.md` ☑ ② `02-survey/survey.md` ☑ ③ `03-method/method-spec.md` ☑ ⑤ `05-realexec/protocol.md` ☑ ⑦ `07-figures/figure-spec.md` ☑ `README.md`
  - ☐ ⑦ `docs/figures/manifest.md`:**不存在**。⑦ 仅在 `figure-spec.md:51` 自称"登记本文件表(即 manifest)";`08-paper/figures/` 目录**不存在**,`method.tex:20` 的 `\includegraphics{pipeline}` 无对应文件。
  - ☐ ② 语料清单:无独立文件,②`survey.md:54` 指回 ①§0.2 表(18 条)。
- **审稿人 = 独立子任务(未参与起草)**。**异检索路径(与作者不同源、且更深)**:
  1. arXiv 官方 API `curl -sL export.arxiv.org/api/query`(逐字核 `2510.03827`、`2610.11480`、`2607.21725`、`2609.40306`、`2609.38078` 摘要全文;另跑 `all:"LIBERO-Pro"` descending 30 条 + `all:"LIBERO-Pro" AND all:"runtime interventions"`)。**全程未用 WebFetch**(承 P-007 / gap-heuristics §5)。
  2. OpenReview **`api2.openreview.net/notes/search?term=LIBERO-Pro`** —— 取回**全部 90 条**(85 条有标题),而 ① 只取回 25 条元数据 / 4 篇摘要(①§0.2 line 43)。**这是本次审稿相对作者的深度增量。**
     - ⚠️ 直连 `?id=` / `?forum=` 两个端点均返回 **403 `ChallengeRequiredError`**(api1/api2 皆然),故作者身份字段(`authors`/`authorids`)**未能取回** —— ①§3 待核#2 我**也没能关闭**(见 §7)。
  3. **GitHub 官方 repo 实抓**(作者本轮明确未跑,①§3 待核#5):`api.github.com/repos/Zxy-MLlab/LIBERO-PRO` + `raw.githubusercontent.com` 取 `evaluation_config.yaml`、`perturbation.py`(679 行)、`README.md`(30,752 字节)全文 + branches/tags + `search/repositories`。
  4. **手算复核 ⑥ 全部统计量**(未跑 significance.py,直接从 results.json 25 条原始值重算均值/样本标准差/配对差/pooled-SD Cohen's d/配对置换 p 下限)。
- **本次预演局限(如实声明,不假装全知)**:
  1. **未跑真机、未跑仿真、未跑 GPU**;`check_freeze.py` 与 `significance.py` **均未实跑**,⑥ 的统计量是我**手算复核**的(结论:⑥ 算术全对,见 §2 通过项)。
  2. **未编译 LaTeX**;`\ref`/`\cite` 断链是**静态 label 集 vs ref 集比对**得出(对"未定义引用"是决定性证据,但无法报告其他编译错误)。
  3. **所有外部论文核实均止于摘要层 + repo 层,未开任何 PDF 全文**。F2 中"Pigey/DynaHarness/MotorMind 三个基线的骨干与分母"仍可由全文进一步钉死;我的判据是**草稿从未做这件事**,且**摘要层已足以证明三者分母不同**。
  4. **OpenReview 作者身份 / 双投状态未核到**(403),故 `6xlHe08ZsL` 与 `2510.03827` 是否同团队**我仍无法判定**(但已用 repo 证据从另一侧解决其后果,见 F1)。
  5. §7 列出的 ≥6 篇新命中工作**仅标题级**,按 rubric 纪律**不断言其为威胁**。
  6. HuggingFace 数据集(`zhouxueyang/LIBERO-Pro`)与 CC BY 4.0 许可**未重抓**;GitHub 侧已重抓(MIT / 332 stars / pushed 2026-07-17)。
  7. ① 遗留 6 条邻接摘要(ManiUnit / MIKASA-Robo-VLA / RESETTLE / Recova / EvoMem-VLA / Divide-and-Remember)**我也未抓**;Google Scholar 与 Awesome 元清单**我也未跑**。

---

## 1. Reviewer 1 · 新颖性

- **评分:3 / 10**(锚点 reviewer-rubrics §0:3–4 = reject,大改;"致命弱点存在,需回灌重做某段")

- **意见(每条带草稿位置)**:

  1. **【致命】让位后剩下的四条差异化,有三条在我的独立核查下塌掉。** ③`method-spec.md:12` 把差异化定为:①中立第三方 ②官方 1,648 变体分母 ③含训练式 VLA 平等臂 ④恢复/成本双轴。逐条核:
     - **②塌**:`experiments.tex:11-12` 把 "official 1{,}648 perturbation variants" 挂在 `\cite{liberopro2025}`(= arXiv `2510.03827`)名下。我实抓该文摘要:**不含 "1,648"、不含 "runtime"、不含 "intervention"、不含 "22 static"**,原文自述口径是 **four dimensions: manipulated objects, initial states, task instructions, and environments**。再实抓官方 repo `Zxy-MLlab/LIBERO-PRO`(MIT,master,pushed 2026-07-17):`README.md` 标题为 "**⚙️ Five Core Generalization Dimensions**"、正文 "under **five generalization perturbations** in LIBERO-Pro";`evaluation_config.yaml` 只暴露 **5 个开关**(`use_environment / use_swap / use_object / use_language / use_task` → `env/swap/object/lan/task`);README 关键词命中数 `"1,648"=0 / "1648"=0 / "intervention"=0 / "22 static"=0`;branches = `[codex/pr1-bddl-robustness, master, new]`,tags = `[]`。`api.github.com/search/repositories?q=LIBERO-Pro+runtime+interventions` → **total_count=0**;arXiv `all:"LIBERO-Pro" AND all:"runtime interventions"` → **totalResults=0**。
       → **"22 static + 20 runtime + 1,648" 仅存在于未过审的 ICLR 2027 在投件 OpenReview `6xlHe08ZsL`**(我已独立逐字核实其摘要含该三项),而**该件与 arXiv `2510.03827` 是否同一工作,① 自己在 §3 待核#3 标为 🔴 未决**。草稿把这个未决问题**默认按"是"解决并写进正文首句**,还加了 "**official**" 这个来源不支持的限定词。详见 §5 硬伤 4 与 F1。
     - **④塌**:`results.json:14` 只有一个 `"metric": "success_rate"`,25 条结果**每条只有 `value`**;恢复率/首次失败步/恢复延迟/任务级全灭/token/墙钟 **一个都不存在,连占位都没有**(详见 R2-F4)。更根本:`config.yaml:79-81` 的恢复测试床 `"官方 20 类 runtime intervention"` 在**被 pin 的仿真器里不存在**(见上)。
     - **①未建立**:`related.tex:11-23` 是**未实例化的模板骨架**("Route A: <名称, 如 Imitation Learning for Manipulation>"、`\cite{<key>}`×3、"Positioning. Compared with the above, **MethodName** is distinct in that \ldots")。**全文零条可解析引用**(见 R3-1),故 ①必要条件1 与 ②§3 要求的"显式让位 `t08NEb8pTY`"**在论文里根本没出现**。中立性主张没有任何文本载体。
     - **只剩 ③**(补一个训练式端到端 VLA 臂)。这是对一篇在投工作的**单臂增量**,直接命中 rubric §1 致命信号"增量太小"。

  2. **【重大】让位边界画得太窄:作者对自己的最强威胁做了选择性引用。** ①§0.2 line 51 与 ⑥§3 只引了 `t08NEb8pTY` 的**两个数字**(95.0%;45%→94%),并据此判定"**唯一缺口:未含「训练出来的端到端 VLA」这一臂**"。我独立取回**完整摘要**,其中含一条**台账从未登记的第三结论**(逐字):
     > "**Third, additional imposed structure provides no consistent benefit: predefined skills, abstractions, and heuristic scaffolding do not reliably outperform a minimal interface and can restrict how the model discovers and revises solutions.**"
     
     另有摘要中被漏掉的 "including **75.0% on unseen composite tasks**"(泛化 split)与 "We evaluate on **LIBERO, LIBERO-Pro, and the RoboCasa365 Target50 subset**"(跨基准)。
     → 后果有两层:(a) 草稿预期的头条结论("三臂排序随扰动类目翻转 / 无单一路线全胜",③要件⑥主判据)与该第三结论**部分同域**;(b) 更严重 —— 草稿的**安全网**("若预算效应 ≫ 路线效应,则 null result 仍可发表",③要件⑥ null 预案 + `experiments.tex:79-80` limitation (iv))**被削弱**:预算主导(45→94)**和**脚手架无益**两条都已被该在投件占据**。①line 119 判"这不削弱价值"时,**没有核到该 null result 本身已有人在投**。
     → ⑥§3 外部锚点表把 `t08NEb8pTY` 标为"否(引完整区间)"—— **该锚点并非全口径**,漏了第三结论。这正是 rubric §2 首行 ε4P 半口径模式。

  3. **【重大】"15 篇 / ≥9 种分母 / 无两篇共享分母" 这组 motivation 数字经不起计数核对。** 位置 `experiments.tex:57-60`,且该段**自我认证**为 "These 15 values are externally verified (arXiv/OpenReview, 2026-10-09), **not placeholder**" —— 即它是全篇**唯一会真进印刷版的定量段落**,却含三处问题(逐条见 R2-M1)。对新颖性的直接影响:本文的 motivation 强度**依赖**"口径混乱到无两篇可比"这一最强表述,而该表述在 ①自己的证据下**不成立**(DynaHarness 的 75.2% 与 17.5% 同在 "800 newly sampled initial states" 上,我已逐字核实)。

  4. **【重大】①对基准卡做的"事实层面修正"本身是错的,且是 F1 的源头。** ①§0.2 line 124 建议"本 gap 应锚定此口径(1,648),**而非基准卡所记「官方总数不可得」**"。我的 repo 实抓显示:**基准卡的"官方总数不可得"更接近事实** —— 官方代码库没有 1,648 这个总量,只有 5 个可组合扰动开关。①把一个在投件的自述规模当成了"官方口径",③`method-spec.md:26`、④`config.yaml:16-17`、⑧`experiments.tex:11-12,77` 逐级继承,无人回核 repo。

  5. **【次要】`2609.38078`(MotorMind)与 `2610.11480`(RoboAware)、`2607.08448v5`(Harness VLA)均有 OpenReview 版,作者未登记双版本漂移风险。** 我在 90 条中命中:`9Li4rfsUQm` "Scaffolding General Vision Language Models for Zero-Shot Robot Control"(≈MotorMind)、`jTZo4036Yx` RoboAware、`EiCbKWR16T` Harness VLA。其中 MotorMind 的 **≤13.3% 是 `experiments.tex:51` §V-C 三个承重锚点之一**,RoboAware 的 **SCB 是 `config.yaml:78-79` 恢复轴的唯一测量装置** —— 两个承重源都有"arXiv 版 vs 在投版可能不同"的风险,①§3 待核#2 只覆盖了它已找到的 4 个 ID。

  6. **【次要】MotorMind 已有真机结果,台账未记。** 逐字:"The same interface reaches **95% average success on a real xArm6**"。若草稿后续要加 sim-to-real 外部效度节(⑤§0 提到的审稿人常问项),这是必须先让位的最近邻。

- **补强建议(可操作,标回灌去向)**:
  - **→ ①(必做,前置)**:重抓 `t08NEb8pTY` 完整摘要,把第三结论(scaffolding no consistent benefit)+ 75.0% unseen composite + 跨三基准写入台账;**重画让位边界**;**重估 null-result 安全网的价值**(①line 119 的"不削弱价值"须撤回或改写)。同时把 ①§0.2 line 124 的"应锚定 1,648"改为"1,648 仅见于在投件 `6xlHe08ZsL`,官方 repo 为 5 维,二者不可混用",并**销项 ①§3 待核#3 为"已证不同口径"**。
  - **→ ③**:按 repo 实证口径重写要件③分层抽样(只能用 `env/swap/object/lan/task` 5 轴),并**明确二选一**:(a) 全程锚定官方 5 维 LIBERO-PRO → 删掉 1,648 分母主张、删掉 runtime-intervention 恢复测试床、**Gap-2 需另找载体**;(b) 等 `6xlHe08ZsL` 过审/放码后再做 → 本选题**当前不可执行**。此为 🔴 委托人裁决项。
  - **→ ⑧**:`related.tex` 必须实例化并**真的让位**(点名 cite `t08NEb8pTY` 并写清其三条结论 + 本文只补哪一条);`refs.bib` 必须落 18 条真实条目;删掉 `experiments.tex:11-12` 的 "official 1,648"。
  - **→ ①/②**:补核 §7 列出的 ≥6 篇新命中(CARE-VLA / FIT-MAC / OmniBrain-0 / RoboFoundry / RAPID / Encore 等)**摘要**,再判是否需二次让位。

- **异检索路径核对**:
  - **最近邻是否已发表/在投?** `t08NEb8pTY` = **ICLR 2027 Conference Submission(在投,已独立核实标题/venue/keywords/摘要全文)**;`6xlHe08ZsL` = **ICLR 2027 Conference Submission,primary_area: datasets and benchmarks(已独立核实,含 1,648 / 22 static / 20 runtime / 11 policies / 25.9pp / 32.5)**;`2510.03827v2` = **已发表 arXiv(updated 2026-05-25,官方 repo MIT/332 stars)**;`2610.11480v1` = **已发表 arXiv(2026-10-08,SCB 逐字核实)**。
  - **查了哪些独立源(非作者引用源)?** OpenReview `notes/search`(全 90 条,深于作者的 25 条)、**GitHub API + raw 文件全文**(作者本轮明确未跑)、arXiv API 逐字摘要 + 两个新检索式。
  - **结论:作者确实漏了关键最近邻信息,且其"让位边界"站不住。** 漏的**不是某一篇论文**,而是三类:(1)**深度漏**(90 条只取 25 条 → 漏 ≥6 篇路线/恢复相关工作);(2)**口径漏**(对自己最强威胁只引 2/3 条结论,漏掉直接侵蚀本文安全网的那条);(3)**源漏**(把在投件的规模当官方口径,从未核官方 repo,而 repo 证明是 5 维、无 runtime intervention)。**让位边界"唯一缺口=缺训练式 VLA 臂"不成立**:该在投件还占了预算主导结论与脚手架无益结论,而本文用来补位的另三条差异化分别因 F1/F4/M3 无载体。→ **R1 判 3 分。**

---

## 2. Reviewer 2 · 实验严谨(最严)

- **评分:2 / 10**(锚点 §0:1–2 = strong reject,"结论不成立 / 诚信问题"。**性质说明(不夸大)**:F3 与 M3-6 读起来更像**未清理的模板残留 + 自查表误签**,而非蓄意造假;但对读者的效果与诚信问题等价,且**⑧自己的签发前自查表签了 [x]**,即**闸失效**。同时 F2 使本文自称"最硬的一张图"**结论不成立**,单此一条即落入 1–2 档。若 F1/F2/F3 修好、只剩骨架未实例化,R2 可回到 4–5。)

- **逐条核对**(对照 reviewer-rubrics §2 表 + ⑥ 审计记录):

| 查项 | 命中问题? | 位置 | 证据 |
|---|---|---|---|
| 选择性引用(只报有利) | ☒**是**(2 处) | `experiments.tex:51`;`06-audit/results-audit.md:37` + `01-gap:51` | (a) MotorMind 逐字原文是 "at most **13.3% and 19.2%**, respectively"(base suites / under perturbations 成对),草稿只引 **≤13.3%**,**隐去配对的 ≤19.2%** —— 我实抓 `2609.38078v1` 摘要确认。(b) `t08NEb8pTY` 只引 95.0% 与 45%→94%,**隐去第三结论**(scaffolding no consistent benefit),⑥§3 还把它标为"否(引完整区间)"。 |
| 验收锚点自身达标 | ☒**是(致命)** | `experiments.tex:49-54`;`config.yaml:66-69`;③要件⑤step5;⑥§5 | **F2**:三个对标锚点**分母互不相同** → 检验**先验恒真、不可证伪**。逐字(我实抓):Pigey `2607.21725v1` "advances the state-of-the-art by over 4x (**12.8% -> 53.3%**) with no task-specific fine-tuning"(**分母未述**);DynaHarness `2609.40306v1` "achieves 75.2% on **800 newly sampled initial states**, compared with **17.5%** for the frozen policy"(分母 = **800 个新采样初始状态**);MotorMind `2609.38078v1` "**66.7%** success on the **base LIBERO-PRO suites** and 53.8% under perturbations, compared with at most **13.3%** and 19.2%, respectively"(≤13.3% 是 **base 非扰动套件**值)。→ 一次在单一分母上的重跑**在构造上就不可能同时逼近三者**,"≥2 不可同时逼近"**必然成立**,**零信息量**。①line 59/61 自己已记录 DynaHarness 分母"与他篇不可并列",草稿**把自己的证据反转成了一个不成立的检验**。附加层:三篇摘要**均未指名基线骨干是 π₀.₅**,而 `config.yaml:66-69` 与 ⑥§5 直接假设"同一冻结 π₀.₅" —— **参照物身份未核**;若三者骨干不同,"冲突"直接消解。 |
| 跨配置迁移(单/双臂·版本) | ☒**是(致命,版本维度)** | `experiments.tex:11-12,77`;`config.yaml:16-19,41-44,79-81` | **F1**:单/双臂**无违规**(见下方通过项),但**跨 benchmark 版本命中**:`simulator_version: "LIBERO-Pro-2510.03827v2"`(官方 repo 实证 **5 维、无 runtime intervention**)与 `benchmark_version: "1648-variants-official"` + 注释"官方 22 static + 20 runtime interventions"(仅见于在投件 `6xlHe08ZsL`)**被熔进同一个冻结 config**。后果三条:(i)`frozen_subset.strata` 的 7 类中 **scene / visual / robot_state / temporal / runtime_intervention ≥4 类在被 pin 环境里无对应开关**(`evaluation_config.yaml` 只有 5 个 flag)→ **N=300 分层冻结子集不可构造**,而它正是 ①必要条件3 / ③要件③ 用来避免"自己变成第 10 种分母"的唯一保障;(ii)`recovery_probe.runtime_interventions` 的**测试床不存在**;(iii)`experiments.tex:77` "≠ official full 1,648" 把未证数字称 official。⑥§4 却签"跨 benchmark 版本比?**否** ✅" —— **⑥ 的跨配置闸放行了一个跨版本 config(审计假阴性)**。 |
| 多 seed / 方差 | ☒**是** | `abstract.tex:16`;`experiments.tex:22`;`appendix.tex:12` | n=5 本身合规(③要件⑤step4 "≥5"),但:(a)`abstract.tex:16` 把 n=5 写成 "**multi-seed**" 并据此断 p<0.05(见显著性行);(b)`experiments.tex:22` 的 seed 数是 **空键 `\audittodo{}`**、`appendix.tex:12` "number of seeds $N=$ `\audittodo{}`" —— **seed 数在论文里从未落到 5**,而 `config.yaml:37`/`seeds.txt` 明确是 5,属可立即填实却未填;(c)**方差在正文无处呈现**:Table 1(`experiments.tex:31-39`)只有 Success/Recovery/Cost 三列,**无 ±std 列**,而 ⑦`figure-spec.md:21` 明列"误差棒必画 … 不掩盖波动" → 表格与作图规格不一致,均值无方差即命中 rubric"只报均值不报方差"。 |
| cherry-pick seed | ☐**否(通过)** | `results.json:18-44` | 25 条 = 5 variant × 5 seed **全列**,无挑优;⑥§1 判"✅ 否"**成立**(我逐条数过)。 |
| baseline 公平性 | ☒**是** | `config.yaml:53,59,64`;`experiments.tex:16-20` | (a)"**unified** budget (≤8 LLM calls/episode)" 只对 B/C 落地:`budget` 键**仅出现在 `R3_harness`(:59)与 `R3_cap`(:64)**,臂 A / baseline / ablation **无 budget 键** → "unified" 在 config 层只覆盖 2/3 臂。(b)臂 A 是端到端 VLA,**LLM 调用数恒为 0**,故 Table 1 的 "Cost (LLM calls)" 列是 **0 对上限**的比较 → 成本轴与路线**结构性混淆**,且 8 次上限对 B 可能 binding、对 C 可能不 binding,不等价。(c)`config.yaml:53` `R3_vla_frozen.trainable_backbone: **true**` 与同行 `backbone: "pi0.5 (open-weights, **frozen**)"`、`hyperparams: {eval_only: true}`、`experiments.tex:16` "(A) … ($\pi_{0.5}$ **frozen**)" **自相矛盾**;③要件② 又承诺臂 A "冻结评测 **+ 报告微调版(若有)**",而**微调版在矩阵(`config.yaml:49-64`)与论文中均不存在** → 规格与执行不一致。(d)A 用开权重 π₀.₅、B/C 用闭源前沿 VLM → 路线效应与骨干能力混淆;此点 `experiments.tex:74-76` limitation (i) **已诚实披露,给予肯定**,但披露不等于解决。 |
| 计数/自计一致(off-by-one) | ☒**是**(4 处) | `experiments.tex:57,58,59-60`;`config.yaml:98`;①`:137`;`README.md` 索引 | **M1 + M4**,详见下方逐条。 |
| 显著性 ↔ 措辞对齐 | ☒**是(致命,重点核查项命中)** | `abstract.tex:16`;对照 `06-audit:26-31`;`traceability.md:29` | **F3**:`abstract.tex:16` 写 "an improvement of `\audittodo{delta}` (**\emph{p}<0.05, multi-seed**)"。⑥§2 逐字:"置换检验(配对,精确枚举)**p=0.0625**";"⚠️ 检验力告警:n=5 配对**最小可达 p=0.0625≥0.05** → 即便差异完全一致也无法达 p<0.05";"判定:**comparable / no significant difference(禁用比较级)**";⑥§2 结论"**不得写「harness 显著优于 VLA」**";⑥§9 放行去向"只可用 `\audittodo{}` 占位,**不得写死任何占位数字**"。→ **`p<0.05` 是写死在摘要里的既成断言,不是占位**;且它**比"显著优于"更强**。我手算复核 ⑥ 的 p 下限:配对 n=5 双侧精确置换 = 2/2⁵ = **0.0625 ✅ ⑥ 完全正确** → **摘要越过了 ⑥ 的降级,不是 ⑥ 算错**。同一草稿的 `experiments.tex:42-45` **正确降级**("we \emph{do not} claim statistical significance"),故**摘要与 §V-B 直接矛盾**。**闸失效证据**:`traceability.md:29` 签发前自查勾了 "[x] 比较级已按 ⑥ 显著性降级(无「显著优于」)" —— **该勾为假**。 |
| 数字-结论错配 | ☒**是**(3 处) | `experiments.tex:57-60`;`:49-54`;`intro.tex:23-25` + 全文 | (a)**M1**:"15 reports / ≥9 denominators / no two share" 支撑不了(逐条见下);(b)**F2**:§V-C 的数字支撑不了"even the baseline is not comparable is confirmed / the hardest evidence";(c)**F5**:③要件⑥**主判据**("三臂排序随扰动类目翻转")在论文里**无表、无图、无节**(grep `sections/` 中 `categor|stratif|interaction` 仅命中 `experiments.tex:12` 的 setup 一句),⑦`figure-spec.md:15` 定义了正好证明它的 **Fig.6 扰动类目×路线交互 heatmap,论文从未引用**;`intro.tex:24,25` 的 C2/C3 指向 **未定义 label** `sec:ablation` / `sec:real`;⑥§1 已审计的消融 `R3_no_recovery_axis`(46.6±1.1)**全文零次出现**(grep `ablation` 仅命中 `intro.tex:24` 模板行)。 |

- **补充逐条(M1 / M4 / F4 / F5 / M5 / M6 明细)**:

  - **M1(重大·计数与无源断言)** —— `experiments.tex:57-60`,该段自称"not placeholder":
    1. **"15 recent … reports" 计数错**。核 ①§0.2 line 76 与 ⑦`figure-spec.md:44` 的同一份清单:它是 **15 个 "·" 分隔的条目**,但其中第 5 条(53.8/66.7)、第 6 条(63.1→71.7)、第 10 条(77.8/88.9)**各含 2 个值** → **18 个数值**,出自 **13 篇不同工作**(Pigey×2、DynaHarness×2、RACaP、MotorMind、PyRUA-Lean、RoboAware、WAA、K1、SCOPE、PrimitiveSuite、OpenRUA、Zetta ζ、Frontier Models)。→ "15 reports" **在任何读法下都错**(13 篇 / 15 条 / 18 值)。该错**穿透三个工件**:⑦`:43` "x 轴:15 个工作"、⑥§3 "①今日 curl 核 15 个绝对值"、⑧`:57`,**无一处数过"不同工作数"**。
    2. **"≥9 mutually incompatible denominators" 计数灌水**。①自己的小标题(line 74)写的是"至少 **7** 种互不兼容的**分母/报告约定**";其 ①–⑨ 枚举里 **⑧"只报增量不报绝对值"与 ⑨"显式 budget-dependent" 是报告约定,不是分母**。②`survey.md:33-35` 的表格**正确拆开**了:分母行**恰好 7 项**(matched / 800 init states / 57 scored / base-vs-perturbation / 700 跨基准 / 100 tasks / 1,648)+ 独立的"报告方式"行 +"预算依赖"行。→ **⑧把 "/报告约定" 限定词删掉、把 7 提升为 9**,是**重新贴标签式的计数灌水**。
    3. **"no two reports share a denominator" 未被证实**。三重反驳:(a)**鸽笼** —— 13 篇落进 7 类分母必有共享;(b)**①自己的证据反证** —— DynaHarness 的 75.2% 与 17.5% 我实抓确认**同在 "800 newly sampled initial states" 上**,即**同一篇两个值共享一个分母**;(c)**≥5 篇的分母 ① 从未识别**(WAA 75.6 / Zetta 90.8 / OpenRUA 87.0 / PrimitiveSuite 82.4 摘要未述;SCOPE 80.66 ①line 63 明写"**未说明 "mean" 的任务集**")→ 该全称否定是**从"没查到"推出的"不存在"**,恰是本流水线纪律明令禁止的推理。
  - **M4(重大·计数 + 可执行性)**:
    1. **预算低报 40%(且是 🔴 人批项的输入)**。`config.yaml:98` `est_rollouts: 225000  # 300×50×3臂×5seed` **只数了 3 个 method 臂**;但 `run.sh:31` 的循环列了 **5 个 variant**(`R3_vla_frozen R3_harness R3_cap baseline_align_pi05 R3_no_recovery_axis`)× 5 seed → 实际 = 300×50×**5**×5 = **375,000**,**低报 150,000(+66.7%)**。③`method-spec.md:74` 复述"≈22.5 万 rollout"。此数是 `budget_approved_by_human: false` + `closed_source_api_cost: true` + `cloud: true`(`config.yaml:100-102`)这一 **🔴 门**的决策输入,而**全链无任何 API 金额估算** → 委托人在此数字上**无法负责任地批预算**。`est_gpu_hours: 120` 同样只对 3 臂口径,且 B/C 的真实瓶颈是 API 而非 GPU 时。
    2. **冻结目录不可执行**。`run.sh:37` 调 `run_libero_pro_eval.py`、`:47` 调 `aggregate_results.py`,**两个脚本在 `04-sim/exp-VP01/` 中都不存在**(目录仅 6 个文件:code-commit.txt / config.yaml / env-lock.txt / results.json / run.sh / seeds.txt)。`run.sh:23` 有 `set -euo pipefail` → **首行即 abort**。所谓"真实备料"**跑不起来**。
    3. `run.sh:26` 注释自称"zsh 兼容",但 `:28` 用了 `mapfile`(**bash ≥4 专有,zsh 无**)→ 注释自相矛盾。
    4. `run.sh:19-20` 运行时**覆写冻结目录内的 `env-lock.txt` / `code-commit.txt`**,与 ⑥§0 认证的"config.yaml(冻结,check_freeze.py PASS)"冻结纪律相冲突(冻结目录不应被 run 脚本原地改写)。
  - **F4(致命·贡献点↔实验不对应)**:**恢复/成本双轴 = 本文让位后仅剩的差异化之一,但零数据、连占位都没有。** `results.json:14-16` 只声明 `"metric": "success_rate"` / `"metric_units": "percent"`,25 条记录**每条仅 `value`**;而 `config.yaml:25-32` 声明了 **7 个 secondary metrics**(recovery_rate / first_failure_step / recovery_latency_llmcalls / task_wipeout_rate / llm_calls_per_episode / tokens_per_episode / wallclock_per_episode),`run.sh:35` 也传了 `--probe recovery`。⑥§1 **只审了 5 个数,全是 success_rate** → **恢复/成本从未被审计过任何数字**。然而 `experiments.tex:33` Table 1 开了 "Recovery (%)" 与 "Cost (LLM calls)" **两列**、§V-A`:20-21` 承诺全部 7 个指标、§V-E`:62-66` 讨论恢复率与延迟。**`traceability.md` §1 数字台账 6 行里完全没有恢复/成本** —— 差异化指标**从可回指台账里静默消失**。
    - 附加:`experiments.tex:64-66` **把假设写成了结果句**:"Arms (B)/(C) show `\audittodo{recovery vs A}` recovery rate but `\audittodo{latency}` higher recovery latency; on object/position static perturbations the recovery gap `\audittodo{vanishes?}`" —— 句式**预设了方向**(B/C 恢复率更高、延迟更高、静态扰动上差异消失),与 ③要件⑥"恢复判据"逐字同构;若真实数据反向,**该句无法填**。且 `\audittodo{vanishes?}` 在结果句里带问号。
  - **F5(致命·主判据无载体 + 消融无处安放且定义不成立)**:见上表"数字-结论错配(c)"。补充**消融本身的逻辑问题**:`config.yaml:71-75` `ablate: recovery_and_cost_axes` / note "**只报终局成功率**,对照是否丢失路线判别信息" —— 但**终局成功率本来就是主指标**,去掉恢复轴**在逻辑上不可能改变它**;而占位值 46.6 却落在三臂(31.0 / 57.8 / 52.0)之间,且 `arm: "all_three"` 是**单一聚合值**,**无法与任何单臂对照**。→ 该消融**既未被报告,又在定义上无法产生它想产生的效应**。
  - **M5(重大·诚实作图)**:⑦`figure-spec.md:13` Fig.4 "同一冻结 π₀.₅ 跨口径 12.8/17.5/13.3/**31/13.6** 冲突",标注 "**部分占位**"。其中 12.8/17.5/13.3 是**真实**(我已逐字核实),31.0/13.6 是 **PLACEHOLDER** → **真值与编造值画在同一根轴上,只给一个"部分占位"的整体标注**,读者无法分辨哪些点是假的,不满足 ⑥§9"⑦ 图表须标「占位数据」"的粒度要求。叠加 F2:即便换成真数据,该图仍误导 —— 三个文献点分母各异(其一还是 base 非扰动值),而 31.0/13.6 在 N=300 子集上。另 `figure-spec.md:22` 把占位差 "26.8pp" **写死进了作图规则文本**。
  - **M6(重大·可回指性只实现一半)**:`experiments.tex:35-37` 中 Success 列有源键(`\audittodo{exp-VP01/R3_vla_frozen}` 等),但 **Recovery 与 Cost 两列共 6 个单元格是空键 `\audittodo{}`**;同样空键见 `:22`(seed 数)、`:42`(delta)、`:49-50`、`:64-66`。**空键无法被后续写作者或审计者解析** → ⑥§9 依赖的"每个占位可回指一个被审数字"只落地了一半。`traceability.md` §1 只登记 6 行,**这 6 个空键不在台账内**。

- **通过项(如实记功,不缩小也不夸大)**:
  - **单/双臂口径:全链一致,未发现迁移。** `config.yaml:13` `embodiment: unimanual` + `robot: franka_panda`、`results.json:8` `embodiment: unimanual`、`experiments.tex:13-14` "single-arm (Franka Panda)"、`:28` 表注 "(single-arm, N=300)"、⑤`:16` 要求真机亦单臂、⑥§4 判定一致 → **rubric §2"跨配置迁移(单/双臂)"这一项,本文干净。**
  - **⑥ 的算术我全部手算复核,全对**:vla_frozen (31,29,33,30,32) → 31.0, 样本 SD 1.58≈**1.6** ✅;harness (58,55,60,57,59) → 57.8, SD 1.92≈**1.9** ✅;cap (52,50,54,51,53) → 52.0, SD 1.58≈**1.6** ✅;baseline_align (14,12,15,13,14) → 13.6, SD 1.14≈**1.1** ✅;no_recovery (47,45,48,46,47) → 46.6, SD 1.14≈**1.1** ✅;均值差 **26.8pp** ✅;pooled SD = 1.761 → Cohen's **d = 15.2** ✅;配对 n=5 双侧精确置换 **p 下限 = 2/2⁵ = 0.0625** ✅。**⑥ 的显著性降级判断在技术上完全正确,问题出在 ⑧ 的摘要没有遵守它。**
  - **`experiments.tex:42-45` 的显著性措辞是本次草稿最规范的一段**("with $n{=}5$ paired seeds the permutation test cannot reach $p<0.05$ (min achievable $p=0.0625$), so we \emph{do not} claim statistical significance"),`:28-29` 表注也明写 "All numbers PLACEHOLDER (dry-run); audit signed NOT-CLEARED",`:72-80` limitation (i)–(iv) 诚实(同骨干不可行 / 子集非全量 / 欠功效 / null 风险)。**诚实闸在 §V 生效了,在 §摘要 与 §复现声明 失效了。**
  - **cherry-pick:无**(25/25 全列)。
  - **⑥§3 两个外部锚点的数值本身逐字准确**(12.8–95.0 跨度的两端、45%→94% 区间)—— 问题在**口径不完整**(M1 的 15/9 计数、M2 的漏第三结论),不在数值造假。

- **补强建议(指明补哪个 seed / baseline / 改哪句)**:
  1. **→ ⑧ `abstract.tex:16`**:删除 `(\emph{p}<0.05, multi-seed)`。改为不带显著性的描述式,并在 n 未定前不写 n:例如 "…an absolute difference of `\audittodo{exp-VP01/delta_harness_minus_vla}` percentage points (descriptive; with $n{=}5$ paired seeds the exact permutation test cannot reach $p<0.05$, so no significance is claimed)"。**同句删除 "for the strongest baseline" 的方法-vs-基线框架**(与 `experiments.tex:15` "Three arms (**equal, not baseline-subordinate**)" 冲突),改为三臂中立表述。
  2. **→ ⑧ `experiments.tex:57-60`**:改 "Across **13** recent \textsc{LIBERO-Pro} studies reporting **18** absolute success values, the rate spans 12.8\%--95.0\%, with **7** mutually incompatible denominators plus **2** further incompatible reporting conventions (increment-only; budget-dependent)";把 "\emph{no two reports share a denominator}" 改为 "**we could not identify a common denominator for any pair of studies; for 5 of the 13 the denominator is not stated in the abstract**",并**逐篇列出分母已知/未知**。同步修 ⑦`figure-spec.md:43`(x 轴 15→13)与 ⑥§3。
  3. **→ ⑧ `experiments.tex:51`**:补上 MotorMind 配对的 **≤19.2%**,并把三值改写为**带各自分母**:"12.8\% (Pigey, denominator unstated) / 17.5\% (DynaHarness, 800 newly sampled initial states) / $\leq$13.3\% base-suite and $\leq$19.2\% perturbed (MotorMind)"。**删掉 "verified in Sec.~\ref{sec:related}"**(§II 无任何核实内容,见 R3-1),改为直接 cite 三篇原文。
  4. **→ ③ + ④ `experiments.tex:49-54` / `config.yaml:66-69`**:**重设基线对齐检验**。当前设计不可证伪,必须改为:(a)产出一张**"文献值 × 各自分母 × 各自骨干"的文档化对照表**(纯 meta-analysis,不假装是实验);(b)若要保留实验,**每个目标分母各跑一次**(在 800-init-state 口径上跑一次去对 17.5%,在 base-suite 口径上跑一次去对 ≤13.3%),**且先从全文核实三篇的骨干是否同为 π₀.₅** —— 若骨干不同,该图必须撤。删除 ⑥§5 与 `experiments.tex:54` 的 "hardest evidence / 最硬的一张图" 表述,直到 (b) 成立。
  5. **→ ④ `config.yaml:98` + ③`:74`**:`est_rollouts` 改 **375000**(300×50×**5 variants**×5 seeds),并**新增 `est_api_usd` 区间**(B/C 闭源 VLM,按 max 8 calls × 32k tokens × 300×50×2臂×5seed 估上下界),再交 🔴 人批。
  6. **→ ④ `config.yaml`**:`:53` `trainable_backbone` 改 `false`(或**新增**一个 `R3_vla_finetuned` variant 以兑现 ③要件②);给 **A / baseline / ablation 也加 `budget` 键**,否则把 `experiments.tex:19-20` 的 "unified budget" 改为 "an identical $\leq$8-call cap applied to the two LLM-driven arms (B/C); arm A issues no LLM calls by construction"。
  7. **→ ④**:补 `run_libero_pro_eval.py` 与 `aggregate_results.py`(或明确标 stub 并在 `check_freeze.py` 里判 FAIL);删 `run.sh:26` 的 "zsh 兼容" 或去掉 `mapfile`;`env-lock.txt`/`code-commit.txt` 写到 `logs/` 而非冻结目录根。
  8. **→ ④ + ⑥(补 metric,不是补 seed)**:`results.json` 必须落 `config.yaml:25-32` 声明的 **7 个 secondary metric**(至少 recovery_rate / recovery_latency_llmcalls / llm_calls_per_episode / task_wipeout_rate),否则 **⑧ 必须删掉 Table 1 的 Recovery 与 Cost 两列 + 整个 §V-E**,并把 ③要件① 的差异化④撤回。**在 F1 未解前,恢复轴还缺 runtime-intervention 测试床** → 二选一:改用官方 5 维中的 `swap`(position)扰动做恢复测试床并**改写 Gap-2 的可证伪设想**,或放弃恢复轴。
  9. **→ ④ + ⑧(补主判据载体)**:results.json 增加 **per-stratum(按扰动类目)分解**;⑧ 新增 §V-? "Ranking × Perturbation-Category Interaction" 表 + `\label{sec:interaction}` + 引用 ⑦ Fig.6;`intro.tex:23-25` C1/C2/C3 重写并指向**真实存在的 label**;消融 `R3_no_recovery_axis` 要么按 (8) 重设为**逻辑上能产生效应**的消融(如"去掉恢复机制"而非"去掉恢复指标"),要么删除并把 `experiments.tex` 补一节 `\label{sec:ablation}`。
  10. **→ ⑧ Table 1(`experiments.tex:31-39`)**:增加 `$\pm$std` 列(与 ⑦`:21` 误差棒规格对齐);**所有空键 `\audittodo{}` 补成 `exp-VP01/<variant>/<metric>`**;`traceability.md` §1 台账补齐恢复/成本行与全部占位单元格。

---

## 3. Reviewer 3 · 写作清晰与可复现

- **评分:2 / 10**

- **意见(带位置)**:

  1. **abstract ↔ 正文 ↔ 表格数字一致?☐是 ☒否**。不一致处(穷举):
     | # | abstract | 正文/表格/源真值 | 性质 |
     |---|---|---|---|
     | a | `abstract.tex:16` "(\emph{p}<0.05, multi-seed)" | `experiments.tex:42-45` "we \emph{do not} claim statistical significance";⑥§2 "p=0.0625 … 禁用比较级" | **显著性越级 + 自相矛盾(致命)** |
     | b | `:14-16` "MethodName achieves … versus … for the **strongest baseline**, an **improvement** of …" | `experiments.tex:15` "Three arms (**equal, not baseline-subordinate**)";③要件① 中立第三方 | **框架冲突**:摘要把中立三臂对照写成方法-vs-基线优越性 |
     | c | `:15` `\audittodo{**exp-014** 成功率, 待⑥审计}` | 真实 exp_id = **exp-VP01**(`config.yaml:8`、`results.json:3`);`exp-014` **不存在** | **溯源键指向不存在的实验** → 摘要从未真正接到 ⑥ |
     | d | `:14` "On \textsc{Benchmark} (single-arm)" | `experiments.tex:11` LIBERO-Pro;`results.json:9` `benchmark: LIBERO-Pro` | 基准名未实例化 |
     | e | `:8,11,19` "MethodName" / "\ldots" | `experiments.tex:2` 与 `results.json:4` = **R3-NeuTraL** | 方法名全文未统一(method/intro/related/conclusion/abstract 共 **7 处** "MethodName") |
     | f | `:19` "Code and data are available at \url{<repo, 提交前由人确认>}" | `reproducibility.tex:8` `\url{<repo>}`;`code-commit.txt` = NOT-A-GIT-REPO | **可获取性断言无 URL** |
     - **另:abstract 与 Table 1 无任何共同数字**(Table 1 三格全 `\audittodo{}`)→ 一致性**无法验证**,而非"已一致"。

  2. **method 可复现?☒否 —— 缺几乎全部细节。** `method.tex` **通篇是未实例化模板**:`:11-13` 问题形式化只有 "We consider \ldots. Let $o_t$ denote \ldots";`:17` "illustrates MethodName, which consists of \ldots";`:26,33` "Component 1: **<名称>**" / "Component 2: **<名称>**";`:29` `\mathcal{L} = \ldots`(**空损失函数**);`:38-43` 算法环境只有 `\STATE \ldots`;`:46-47` "Design choices. We emphasize that \ldots is an implementation choice"。**缺**:三臂的具体实现(agentic harness 的提示结构/工具集/重试策略、code-as-policy 的 primitive 库清单与来源、VLA 的推理配置)、成功判据的可执行定义、恢复轴的 SCB 装置参数(`config.yaml:78-79` 只给了论文名)、N=300 的分层配额表、统计检验方法(置换检验的单/双侧、配对方式、效应量口径)。**读者无法照做。** 更严重的是:**本文是"评测协议型"论文,协议本身就是方法** —— method.tex 空掉等于论文的核心贡献没有载体。
     - 补:超参集中处 `appendix.tex:9-14` 同样全是 `\ldots`,且 `:13` "config: \texttt{**tests/exp-<id>**/config.yaml}" 与 `reproducibility.tex:15` "frozen config under \texttt{**tests/exp-<id>**/}" **路径不存在**(实际为 `04-sim/exp-VP01/`;③`:40,80` 也写 `tests/exp-VP01/`)。

  3. **图诚实(无截断轴/自解释 caption)?☒否(规格合格,实现断链)。**
     - **⑦ 的作图规格本身是好的,予以记功**:`figure-spec.md:20-23` 要求矢量 PDF、Okabe-Ito 色盲友好 + 线型/标记冗余编码、**误差棒必画**、**禁截断轴(Fig.2/4 y 轴从 0 起,并明确指出截断会夸大 26.8pp)**、caption 自解释 + 标配置口径;`:37-38` 还明写"图中不得标「显著」星号" —— **这套规则符合 rubric §3。**
     - **但论文里图全是断链**:静态比对 label 集与 ref 集 → **未定义引用 5 处**:`intro.tex:24 \ref{sec:ablation}`、`intro.tex:25 \ref{sec:real}`、`experiments.tex:54 \ref{fig:spread}`、`experiments.tex:59 \ref{fig:spread}`、`experiments.tex:69 \ref{fig:qual}`(已定义 label 全集中**无** `sec:ablation`/`sec:real`/`fig:spread`/`fig:qual`)。全文**没有任何 `figure` 环境**除 `method.tex:18-23` 的 `fig:pipeline`,而它 `\includegraphics{pipeline}` 指向的 `08-paper/figures/` **目录不存在**。
     - `experiments.tex:69` 引用的定性图 `fig:qual` "(placeholder frames; real capture pending stage-4 execution)" —— **⑦ 的图清单(Fig.1–6)里根本没有定性/失败案例图** → 引用了一张 ⑦ 从未规划的图。
     - **M5**:Fig.4 真值与占位值同轴,仅标"部分占位"(详见 §2)。

  4. **无源断言?☒是 —— 列出(穷举)**:
     | # | 位置 | 断言 | 核实结果 |
     |---|---|---|---|
     | 1 | `experiments.tex:11-12` | "LIBERO-Pro~\cite{liberopro2025} (**official 1{,}648 perturbation variants**)" | **来源不含该数**:arXiv `2510.03827v2` 摘要无 "1,648"/"runtime"/"22 static",自述 **four dimensions**;官方 repo README = "**Five** Core Generalization Dimensions"、`"1,648"` 命中 **0** 次。1,648 仅见于在投件 `6xlHe08ZsL`。**误引 + "official" 限定词无据** |
     | 2 | `experiments.tex:57-60` | "**15** recent … reports … **≥9** mutually incompatible denominators … \emph{**no two reports share a denominator**} … These 15 values are **externally verified**, not placeholder" | 三处不成立(13 篇非 15;7 分母 + 2 报告约定非 9;全称否定未证且被 ①自己的 DynaHarness 证据反证)。**且它以"已核实、非占位"自我认证** → 最危险的一类无源断言 |
     | 3 | `experiments.tex:51-52` | 三值 "**verified in Sec.~\ref{sec:related}**" | **假交叉引用**:`related.tex` 全文无任何数字、任何核实内容、任何可解析 cite(只有 `<key>` 与 "Route A/B/C: <名称>") |
     | 4 | `conclusion.tex:10-11` | "Across \textsc{Benchmark} and **real-robot experiments**, it \ldots" | ⑤`:7` "**本选题是纯仿真基准研究 … ⑤ 真机采集逻辑上 N/A**";⑤`:55` "⑤ 标「**可选,未启用**」";③`:5` "硬边界:**纯仿真研究**" → **声称了不存在且未规划的真机结果** |
     | 5 | `intro.tex:25` | "**C3:** **Real-robot results** demonstrating \ldots (Sec.~\ref{sec:real}, 采集条件见附录)" | 同上;且 `sec:real` **未定义**;`appendix.tex:21-31` 整节 "Real-Robot Collection Details" 全是 `\ldots` + "[待人签名]" → **贡献点 C3 无数据、无节、无签名** |
     | 6 | `reproducibility.tex:19-21` | "Numbers in this paper **were produced by frozen configs (commit \texttt{<hash>}) and audited for full-caliber consistency (including unfavorable results) before citation**" | **与 ⑥ 签发直接冲突**:⑥§9 "**❌ 不放行**"、`:66` "数据 = PLACEHOLDER → 全口径已核 = **❌**";`code-commit.txt` = "**NOT-A-GIT-REPO**";`env-lock.txt` 七行全是 "<待记录>"。此文件经 `appendix.tex:35` `\input` **确实进入编译产物** → **既成事实式的审计通过声明,而审计签的是不通过** |
     | 7 | `reproducibility.tex:7-8` | "Our training and evaluation code, **including all configs used to produce the reported numbers**, is available at \url{<repo>}" | 无 URL;且 `run.sh` 依赖的两个脚本**不存在**(M4-2) |
     | 8 | `reproducibility.tex:10` | "**Teleoperated** / simulation data used in this work" | ⑤ N/A、`config.yaml:88` `data_source: "… (no demos for perturbed tasks)"` → **无遥操作数据** |
     | 9 | `reproducibility.tex:17` | "Experiments **were run** on \ldots (approx. \ldots GPU-hours)" | `config.yaml:84` `gpu: "cuda:0 (**dry-run 未执行**)"`;④ 全链未执行 → **过去时态声称已运行** |
     | 10 | `experiments.tex:19` | "**unified budget** ($\leq$8 LLM calls/episode)" | `config.yaml` 的 `budget` 键只在 B/C(见 §2 baseline 公平性) |
     | 11 | `main.tex:25`(注释) | "例:成功率 `\num{87.2}\% \pm \num{1.3}`  % <- tests/**exp-014**, audit 2026-10-09, 单臂·**LIBERO v1**" | **模板残留里的写死数字 + 不存在的 exp-id + 错误的 benchmark 版本(LIBERO v1 ≠ LIBERO-Pro)**。虽在注释中,但它是**给写作者的示范行**,且与 abstract 的 `exp-014` 同源 → 说明 abstract 的键是从这行残留抄来的 |

     - **引用层面:全文零条可解析引用。** 已用 cite 键 = {`<key>`(intro ×3、related ×3)、`liberopro2025`(experiments ×1)};`refs.bib` 仅有 `EXAMPLE2024method`、`EXAMPLE2023journal`,两条都自带 `note = "EXAMPLE ONLY -- arXiv:0000.00000"`。→ **`liberopro2025` 未定义,渲染为 "[?]"**;**①§0.2 已逐字核实的 18 篇最近邻,一条都没进 bib**,故 `related.tex` 在原则上**无法**完成 ①必要条件1 要求的显式让位。

  5. **叙事逻辑:motivation→gap→method→实验 断裂。** (a)`intro.tex:10-18` 全 `\ldots`,**gap 陈述不存在**,而 `related.tex:23` 的 Positioning 却回指 "the gap identified in Sec.~\ref{sec:intro}" → **指向空节**;(b)`intro.tex:23-25` 的 C1/C2/C3 是通用模板文("A method that \ldots" / "An ablation showing \ldots" / "Real-robot results"),**与本文实际贡献(中立三臂评测协议 + 口径账本)完全不对应**,且 C1 自称 "A **method**",而 ③要件① 明写本文**不提方法、只出中立剖面**(①`:131` "本 gap **不学协调器、不做方法**")→ **贡献点与论文性质相矛盾**;(c)method 空 → experiments 的三臂协议无处定义;(d)`experiments.tex:54` 称 Fig.~`fig:spread` 为 "the **hardest evidence** for the caliber-confusion thesis",而 ⑥§5 称基线对齐检验为"**本工作最硬的一张图**" → **两处争抢同一个"最硬"**,叙事优先级不一致。

  6. **模板残留清单(必须清零才可提交)**:`MethodName` ×7(`abstract.tex:11,14`;`intro.tex:18`;`related.tex:22`;`method.tex:17,21,39`;`conclusion.tex:10,14`)、`\textsc{Benchmark}` ×2(`abstract.tex:14`;`conclusion.tex:10`)、`<key>` ×6、`<hash>` ×2(`appendix.tex:13`;`reproducibility.tex:20`)、`<repo>`/`<link>` ×3、`<名称>` ×4(`related.tex:11,15,18`;`method.tex:26,33`)、`tests/exp-<id>` ×2、`main.tex:32-37` 标题与作者块("[署名待委托人确认]",**合规**,但 `main.tex:32` "Paper Title Here" 仍是占位)、`main.tex:46` 关键词含 `\ldots`、`experiments.tex:41` 注释内写死占位差 "**+26.8pp**"(违反 ⑥§9"不得写死任何占位数字";虽不排版,但随 .tex 源码分发,且使 `traceability.md:27` 的 "[x] 占位数字全 `\audittodo{}`,**无写死**" 自查为假)。

- **补强建议**:
  1. **→ ⑧(最高优先)**:`abstract.tex` 重写 —— 方法名统一为 **R3-NeuTraL**;基准名统一为 **LIBERO-Pro**;溯源键 `exp-014` → **`exp-VP01`**;删 `p<0.05`;删"strongest baseline / improvement"框架改三臂中立;删 `\url{<repo, …>}` 或改为 "will be released upon acceptance, subject to author confirmation"。
  2. **→ ⑧**:`refs.bib` 落 **18 条真实条目**(①§0.2 表已给全 ID / 标题 / 提交日 / 逐字数字,可直接转 bib;`2510.03827v2`、`2610.11480v1`、`2607.21725v1`、`2609.40306v1`、`2609.38078v1` 五条我已独立核实标题,可直接用);`liberopro2025` → 指向真实 `2510.03827v2` 条目;删除两条 `EXAMPLE ONLY` 桩。
  3. **→ ⑧**:`related.tex` 按 ②`survey.md:13-27` 的真实 taxonomy 实例化为 **路线 A 端到端 VLA / 路线 B agentic harness / 路线 C code-as-policy / 混血**四小节,每节末写差异,**并新增一段显式让位**(点名 `t08NEb8pTY` 三条结论 + `6xlHe08ZsL` 官方口径 + `xrcN6ePkAS` 接口层级 + `2610.11480` SCB),使 `experiments.tex:52` 的 "verified in Sec.~\ref{sec:related}" 成真。
  4. **→ ⑧**:`method.tex` 重写为 "**Neutral Three-Arm Evaluation Protocol**"(本文的方法就是协议):三臂可执行定义、统一成功判据、N=300 分层配额表、预算计量口径、SCB 恢复探测参数、统计检验规范(配对精确置换、双侧、Cohen's d 口径、n 与检验力下限)。**若 F1 未解,分层表只能按官方 5 维写。**
  5. **→ ⑧**:`conclusion.tex:10-11` 删 "and real-robot experiments";`intro.tex:25` **删 C3**,或改为 "C3: a public, re-runnable protocol artifact (frozen subset sampling rules, budget metering, seeds)" 并指向真实存在的 label;`appendix.tex:21-31` 整节 **删除或明确标 "not performed in this study (pure-simulation)"**,与 ⑤`:7` 一致。
  6. **→ ⑧**:`reproducibility.tex:19-21` **必须改写为诚实版**,例如:"Configs are frozen under `04-sim/exp-VP01/`; in this dry-run the audit gate signed **NOT-CLEARED** because the results are placeholders, and no code version hash exists yet (`code-commit.txt` = NOT-A-GIT-REPO). Numbers will be cited only after ④ real execution and an independent ⑥ re-audit." 同步 `:7,10,15,17`:删 "Teleoperated"、`tests/exp-<id>/` → `04-sim/exp-<id>/`、"were run on" → 条件式。
  7. **→ ⑧**:修 5 处未定义 `\ref`(新增 `\label{sec:ablation}`、`\label{sec:interaction}`;`sec:real` 随 C3 删除而删;`fig:spread`/`fig:qual` 要么建 `figure` 环境要么删引用);建 `08-paper/figures/` 并落 Fig.1/Fig.3(⑦`:50` 判定这两张"结构真实可用")。
  8. **→ ⑧**:`main.tex:25` 的示范注释行改为不带具体数字、且用**正确的 exp-id 与 benchmark 版本**(避免再次污染 abstract);`experiments.tex:41` 注释删掉 "+26.8pp"。
  9. **→ ⑦**:补一张定性/失败案例图(Fig.7)或删除 `experiments.tex:69` 的引用;Fig.4 按 M5 拆分真值/占位面版。

---

## 4. 四类硬伤专查(三审 + meta 都扫)

| 硬伤 | 命中? | 位置 | 严重度 |
|---|---|---|---|
| **数字-结论错配** | ☒**是(3 处)** | ①`experiments.tex:49-54`:三个分母互异的文献值被当作"同一量的三次测量",据此宣称 "even the baseline is not comparable is **confirmed**" / "the **hardest evidence**" → 检验**先验恒真、不可证伪**(F2)。②`experiments.tex:57-60`:"15 reports / ≥9 denominators / no two share" 与 ①源清单实际的 **13 篇 / 18 值 / 7 分母 + 2 报告约定** 不符,且该段自称"externally verified, not placeholder"(M1)。③`intro.tex:23-25` + 全文:③要件⑥**主判据**(排序随扰动类目翻转)**无表、无图、无节**,⑦ Fig.6 从未被引用,已审计的消融 `R3_no_recovery_axis` **全文零出现**(F5)。 | **致命** |
| **abstract 与正文不一致** | ☒**是(6 处)** | `abstract.tex:16` "p<0.05, multi-seed" vs `experiments.tex:42-45` "do not claim statistical significance" + ⑥§2 "p=0.0625,禁用比较级";`abstract.tex:14-16` 方法-vs-"strongest baseline"-improvement 框架 vs `experiments.tex:15` "equal, not baseline-subordinate";`abstract.tex:15` `exp-014`(不存在)vs 真实 `exp-VP01`;`abstract.tex:14` `\textsc{Benchmark}` vs LIBERO-Pro;`abstract.tex:8,11` "MethodName" vs R3-NeuTraL;`abstract.tex:19` 代码可获取断言 vs `code-commit.txt` NOT-A-GIT-REPO。详见 §3-1 表。 | **致命** |
| **无源断言** | ☒**是(11 处)** | 穷举见 §3-4 表(11 行)。最重三条:`experiments.tex:11-12` "official 1,648" 挂错来源(**我实抓 arXiv 摘要 + 官方 repo 双重证伪**);`reproducibility.tex:19-21` "audited for full-caliber consistency … before citation" vs ⑥ 签 **❌**;`conclusion.tex:10-11` + `intro.tex:25` + `appendix.tex:21-31` 真机结果/C3/真机附录 vs ⑤ "N/A、未启用"。**引用层面:全文零条可解析 cite(`liberopro2025` 无 bib 条目,refs.bib 仅两条 EXAMPLE ONLY 桩)。** | **致命** |
| **跨配置迁移** | ☒**是(版本维度)** / ☐否(单双臂维度) | **命中(benchmark 版本)**:`config.yaml:16-19` 把 `simulator_version: "LIBERO-Pro-2510.03827v2"`(官方 repo 实证 **5 维、README 中 "1,648"/"intervention" 命中 0 次**)与 `benchmark_version: "1648-variants-official"` + 注释 "官方 22 static + 20 runtime interventions"(仅见于**在投件** `6xlHe08ZsL`,且其与 `2510.03827` 是否同一工作 = ①§3 待核#3 **🔴 未决**)熔进同一冻结 config;`experiments.tex:11-12,77` 继承并加 "official" 限定词。**三条后果**:`config.yaml:41-44` 的 7 类 strata 中 ≥4 类(scene/visual/robot_state/temporal/runtime_intervention)在被 pin 环境**无对应开关** → N=300 分层子集**不可构造**;`config.yaml:79-81` 的 "官方 20 类 runtime intervention" 恢复测试床**不存在** → Gap-2 无载体;`main.tex:25` 残留示范行还写着 "单臂·**LIBERO v1**"(第三种版本口径)。**⑥§4 却签"跨 benchmark 版本比?否 ✅" → 审计假阴性。**<br>**未命中(单/双臂)**:`config.yaml:13` unimanual + franka_panda / `results.json:8` unimanual / `experiments.tex:13-14,28` single-arm / ⑤`:16` 真机亦要求单臂 / ⑥§4 一致 → **五处全对齐,无单臂当双臂。** | **致命(版本)** |

**附加命中(不在四类之内,但同等严重)**:
- **显著性措辞越级(重点核查项)**:`abstract.tex:16` 越过 ⑥§2 的强制降级 —— 详见 §2 表"显著性↔措辞"行。
- **审计状态虚报**:`reproducibility.tex:19-21` 声称已过全口径审计,⑥ 实签 ❌ —— 详见 §3-4 表 #6。
- **🔴 预算门输入低报 40%**:`config.yaml:98` 225,000 vs `run.sh:31` 实际 5 variant → 375,000,且无 API 金额估算 —— 详见 §2 M4-1。

---

## 5. Meta-review · 综合裁决

- **三审评分:R1 = 3 / R2 = 2 / R3 = 2**
- **综合倾向:☒ reject**(硬规则:任一维度 ≤4 → 综合不得高于 major revision;**本件三维度全 ≤3,且含 2 条诚信级条目(F3 显著性越级 + 自查表误签、M3-6 虚报审计通过),故低于 major revision,判 reject**)
  - ☐ accept ☐ minor revision ☐ major revision ☒ **reject**
  - **性质限定(不夸大)**:reject 的**主要成因不是造假**,而是 (i) 一个**先验恒真的核心检验设计**(F2)、(ii) 一个**跨 benchmark 版本的冻结 config**(F1)、(iii) **四个节仍是未实例化模板**(M3)。这些是**可回灌重做**的,不是不可救的。但作为**投稿物**,当前状态**不可提交**。
  - **对 dry-run 验证目标的裁决(README`:36-40` 的五条验证目标)**:
    | 验证目标 | 本次实测 |
    |---|---|
    | 门控生效:⑥ 诚实闸拦占位数字进正文 | **部分生效**。✅ 拦住:Table 1 三臂成功率、§V-B/V-C/V-E 的占位量**全部**用 `\audittodo{}`,我 grep 遍 `sections/` 未发现任何被 typeset 的占位数值。❌ **漏拦 3 类**:(a)`abstract.tex:16` 的 **`p<0.05` 显著性断言写死进正文**并越过 ⑥ 降级;(b)`reproducibility.tex:19-21` 虚报"已全口径审计";(c)`experiments.tex:41` 与 `main.tex:25` 注释内写死 `+26.8pp` / `87.2±1.3`(不排版,但违反 ⑥§9 字面要求,且使 `traceability.md:27,29` 两个 [x] 自查为假)。 |
    | 门控生效:⑥ 跨配置闸 | ❌ **假阴性**:⑥§4 签"跨 benchmark 版本比?否 ✅",而 `config.yaml:16-19` 正是跨版本熔合(F1)。**⑥ 只核了单/双臂(核对了),没核 benchmark 版本身份(漏了)。** |
    | ⑨ 独立子 agent 抓弱点 | ✅ 本次抓到 5 条致命 + 6 条重大,其中 **F1/F2/M2 是作者全链(①→⑧)未发现的**(依赖异检索路径:GitHub repo 实抓 + OpenReview 全 90 条 + 摘要逐字全文)。 |
    | 诚实纪律:真实/占位分界清晰 | ⚠️ **大体清晰,但有一处高危**:`experiments.tex:57-60` 是**唯一自称"非占位、已外部核实"的定量段落**,而它恰好含三处计数/推论错误(M1)。**"真数字"段落的风险高于"占位"段落** —— 因为占位段有人盯,真值段没人复核。建议流水线增设:**凡标注"not placeholder / 已核"的段落,必须由 ⑨ 或 ⑥ 独立重算计数。** |
  - **对 ⑧ traceability 自查表的裁决**:`traceability.md:27-32` 六个 [x] 中,**两个为假**(`:27` "无写死" — 见 `experiments.tex:41`;`:29` "比较级已降级" — 见 `abstract.tex:16`),**一个为真但覆盖不全**(`:28` 真实数字回指 ① — 回指关系成立,但**①自己的计数错了**,回指不能替代复核),**一个未落实**(`:31` "配置口径全文一致(单臂·N300)" — 单臂确实一致,但**N300 的分层不可构造**,口径"一致"但"不可执行")。`:33` 自报的 bibkey 待核项**如实,予以肯定**。

- **致命清单(不补则拒),每条标回灌去向**:
  1. **[致命] F1 · 跨 benchmark 版本迁移:被 pin 的仿真器不实现论文声称的官方口径。** `experiments.tex:11-12,77` + `config.yaml:16-19,41-44,79-81`。独立证据:arXiv `2510.03827v2` 摘要 = **four dimensions**、无 "1,648"/"runtime"/"22 static";官方 repo README = "**Five** Core Generalization Dimensions"、`evaluation_config.yaml` 仅 5 flag、`"1,648"`/`"intervention"` 命中 **0**;GitHub repo 搜 "LIBERO-Pro runtime interventions" = **0**;arXiv 搜 `"LIBERO-Pro" AND "runtime interventions"` = **0**;22 static/20 runtime/1,648 **仅见于未过审在投件 `6xlHe08ZsL`**,而它与 `2510.03827` 的同一性是 ①§3 待核#3 的 🔴 未决项。→ **N=300 七层分层子集不可构造 + 恢复轴测试床不存在 + "official" 无据**。→ **回灌 ③(重设分层与恢复载体)+ ④(重冻结 config)+ ⑧(改引用与措辞)+ ①(销项待核#3、撤回 line 124 的"应锚定 1,648")+ ⑥(补 benchmark 版本身份检查项)**。**并须 🔴 委托人裁决**:全程改用官方 5 维(Gap-2 需另找载体)还是等 `6xlHe08ZsL` 放码(当前不可执行)。
  2. **[致命] F2 · "最硬的一张图"先验恒真、不可证伪;且三个锚点分母互异、骨干身份未核。** `experiments.tex:49-54`、`config.yaml:66-69`、③要件⑤step5、⑥§5。独立证据(逐字实抓):Pigey 12.8% **分母未述**;DynaHarness 17.5% = "**800 newly sampled initial states**";MotorMind ≤13.3% = "**base LIBERO-PRO suites**"(非扰动),其配对值 **≤19.2%(perturbed)被草稿隐去**。→ 单一分母上的一次重跑**必然**"≥2 不可同时逼近",检验**零信息量**;①line 59/61 已记录该分母不可并列,草稿**把自己的证据反转成了不成立的检验**。→ **回灌 ③(改为"文献值 × 各自分母 × 各自骨干"文档化对照表;若保留实验则每个目标分母各跑一次)+ ①(从全文核三篇基线的骨干与分母)+ ④(重设或删 `baseline_align_pi05`)+ ⑧(重写 §V-C、补 ≤19.2%、删 "hardest evidence" 表述)+ ⑥(把"锚点自身达标"升级为逐锚点分母核对)**。
  3. **[致命] F3 · 摘要写死 `p<0.05`,越过 ⑥ 的强制显著性降级;⑧ 自查表误签为已降级。** `abstract.tex:16` vs ⑥§2("配对 n=5 **最小可达 p=0.0625≥0.05** … 判定 comparable / no significant difference(**禁用比较级**)")与 `experiments.tex:42-45`(正确降级)与 `traceability.md:29`(勾了"[x] 已降级",**为假**)。我手算复核 ⑥ 的 p 下限 = 2/2⁵ = 0.0625 **完全正确** → **是 ⑧ 越级,不是 ⑥ 算错**。同句还含 `exp-014`(不存在的 exp-id)与"strongest baseline / improvement"框架(与 `experiments.tex:15` "equal, not baseline-subordinate" 冲突)。→ **回灌 ⑧(删 `p<0.05`、改 `exp-014`→`exp-VP01`、改三臂中立框架)+ traceability 重签 + 建议在 paper-writer 侧增设"摘要显著性串必须与 ⑥ 判定串做双向 Grep"的硬门**。
  4. **[致命] F4 · 让位后仅剩的差异化之一(恢复/成本双轴)零数据、连占位都没有,且台账静默省略。** `results.json:14-16` 仅 `metric: success_rate`、25 条仅 `value`;⑥§1 仅审 5 个成功率;而 `experiments.tex:33` Table 1 开了 Recovery + Cost 两列、`:20-21` 承诺 7 个指标、`:62-66` 讨论恢复率/延迟、`traceability.md` §1 **完全无恢复/成本行**;`experiments.tex:64-66` 还把假设写成结果句(方向预设 + `\audittodo{vanishes?}`)。叠加 F1 → 恢复轴**既无数据也无测试床**。→ **回灌 ④(落 7 个 secondary metric,或改用官方 `swap` 扰动做恢复载体)+ ⑥(审计之)+ ⑧(否则删 Table 1 两列 + 删 §V-E,并把 §V-E 改写为假设而非结果)+ ③(撤回或重立差异化④)**。
  5. **[致命] F5 · 主判据无表无图无节;已审计的消融全文零出现且定义不成立;C1–C3 与实际贡献不对应且指向未定义 label。** ③要件⑥主判据 vs `sections/` 中 `categor|stratif|interaction` **仅命中 `experiments.tex:12` 的 setup 一句**;⑦`figure-spec.md:15` Fig.6(正是证明主判据的图)**从未被引用**;`intro.tex:24,25` → `\ref{sec:ablation}`/`\ref{sec:real}` **均未定义**;grep `ablation` 全文**仅命中 `intro.tex:24` 模板行** → `R3_no_recovery_axis`(46.6±1.1,⑥§1 已审)**无处安放**;而该消融 `config.yaml:71-75` 的定义("只报终局成功率")**在逻辑上不可能改变主指标**,占位值却落在三臂之间,且 `arm: "all_three"` 是单一聚合值**无法与任一单臂对照**;`intro.tex:23` C1 自称 "A **method**",而 ③要件①/①`:131` 明写本文**不做方法**。→ **回灌 ⑧(新增 per-category 表 + `\label{sec:interaction}` + 引用 Fig.6 + 补 `\label{sec:ablation}` + 重写 C1–C3)+ ④(落 per-stratum 结果)+ ③(把消融重设为逻辑上能产生效应的形式,或删除)**。

- **决定性弱点(最关键 1–2 条)**:
  - **第一决定性:F1(跨 benchmark 版本)。** 它是**上游单点污染、下游全链继承**的典型:①§0.2 line 124 把一个未过审在投件的自述规模当成"官方口径"并"修正"了本来更准确的基准卡 → ③要件③照它设计 7 层分层 → ④把它写进冻结 config 的 `benchmark_version` 与 `strata` 与 `recovery_probe` → ⑥§4 的跨配置检查**只核了单/双臂、没核版本身份,签了 ✅** → ⑦ Fig.3/Fig.6 照它出规格 → ⑧ 把它写进正文首句并加上 "official"。**六段无一回核官方 repo。** 修它必须回到 ①,不能只在 ⑧ 改字。
  - **第二决定性:F2(核心检验不可证伪)。** 因为草稿**两处**(⑥§5、`experiments.tex:54`)把它标为"最硬的一张图"/"hardest evidence",即**本文的说服力峰值恰好落在一个先验恒真的检验上**。而它的不成立不需要任何真实数据 —— **我用三篇摘要的逐字分母就能否掉它**。这也说明:**外部锚点的"数值逐字正确"(⑥§3 确实核对了)不等于"口径可比"(⑥ 没核)**;⑥ 的外部锚点闸需要新增一列"**该锚点的分母/骨干是否与本文对标口径同构**"。

---

## 6. 弱点 → 回灌去向汇总

| 弱点 | 严重度 | 回灌阶段 | 具体补强动作 | 闭环判据(双向 Grep) |
|---|---|---|---|---|
| **F1** 跨 benchmark 版本:`config.yaml:16-19` 熔合 arXiv v2(5 维)与在投件(7 类/1,648);`experiments.tex:11-12,77` 误引 + "official" | 致命 | **①③④⑥⑧** + 🔴 委托人 | ①销项待核#3、撤回 line 124;③按官方 5 维(`env/swap/object/lan/task`)重写要件③分层与恢复载体;④重冻结 config(单一版本口径、strata 只留存在的轴);⑥新增"benchmark 版本身份"检查项;⑧删 "official 1,648"、改引 `6xlHe08ZsL` 为"在投件自述规模" | 旧串清除:`grep -rn "1648-variants-official\|official 1{,}648\|22 static + 20 runtime\|runtime_intervention"` → **0 命中**(或全部改挂在 `6xlHe08ZsL` 且明标"未过审");新串命中:`grep -rn "five generalization dimensions\|env/swap/object/lan/task"` → ≥2 处(`config.yaml` + `experiments.tex`) |
| **F2** `experiments.tex:49-54` / `config.yaml:66-69` 基线对齐检验先验恒真;三锚点分母互异;骨干身份未核;MotorMind ≤19.2% 被隐去 | 致命 | **①③④⑥⑧** | ①从全文核 Pigey/DynaHarness/MotorMind 的**分母与骨干**;③改为"文献值×分母×骨干"对照表,或每分母各跑一次;④重设/删 `baseline_align_pi05`;⑥外部锚点表**新增"分母/骨干是否同构"列**;⑧重写 §V-C、补 ≤19.2%、删 "hardest evidence" | 旧串清除:`grep -rn "simultaneously approached\|hardest evidence\|最硬的一张图"` → 0;新串命中:`grep -rn "19.2\|800 newly sampled initial states\|base LIBERO-PRO suites"` → §V-C 内 ≥3 处 |
| **F3** `abstract.tex:16` 写死 `p<0.05, multi-seed`;`traceability.md:29` 自查误签;`abstract.tex:15` `exp-014` | 致命 | **⑧**(+ paper-writer 硬门) | 删显著性串、改描述式并写明 n=5 的 p 下限;`exp-014`→`exp-VP01`;删 "strongest baseline / improvement" 改三臂中立;`traceability.md` §3 重签;建议新增"摘要显著性串 ↔ ⑥ 判定串"双向 Grep 门 | 旧串清除:`grep -rn "exp-014\|p}<0.05\|p<0.05, multi-seed"` → 0(注意 `experiments.tex:43-44` 的 "cannot reach $p<0.05$" 是**否定式**,应保留 → 用精确串 `(\emph{p}<0.05` 判);新串命中:`grep -rn "cannot reach\|do not claim statistical significance"` → 摘要与 §V-B **各 ≥1** |
| **F4** 恢复/成本双轴零数据(`results.json:14-16` 单 metric);Table 1 两列无源;`traceability.md` §1 静默省略;`experiments.tex:64-66` 假设写成结果句 | 致命 | **③④⑥⑧** | ④落 7 个 secondary metric(或改官方 `swap` 作恢复载体);⑥审计之;⑧否则删 Table 1 两列 + 删 §V-E,并把 §V-E 改为假设式;③撤回或重立差异化④ | 旧串清除:`grep -n "Recovery (%)\|Cost (LLM calls)"` 与 `results.json` 的 metric 集合**二者只能留一**;新串命中:若保留 → `results.json` 中 `recovery_rate`/`llm_calls_per_episode` 等 key **≥4 个存在且各有 5 seed**;若删除 → `experiments.tex` 中 `recovery|latency` 命中 0 |
| **F5** 主判据无表无图无节;Fig.6 从未引用;消融零出现且定义不成立;C1–C3 指向未定义 label | 致命 | **③④⑧** | ④落 per-stratum 结果;⑧新增 interaction 表 + `\label{sec:interaction}` + `\ref{fig:interaction}`(建 figure 环境)+ `\label{sec:ablation}` + 重写 C1–C3;③把消融改为逻辑上能产生效应的形式或删除 | 旧串清除:`grep -rn "ref{sec:ablation}\|ref{sec:real}\|ref{fig:spread}\|ref{fig:qual}"` 中**未在 label 集内**的 → 0;新串命中:`grep -rn "label{sec:interaction}\|label{sec:ablation}"` → 2;`grep -rn "R3_no_recovery_axis"` in `sections/` → ≥1 |
| **M1** `experiments.tex:57-60` "15 reports / ≥9 denominators / no two share";⑦`:43` "15 个工作";⑥§3 "15 个绝对值";①`:137` "13 条"(实为 18) | 重大 | **①⑥⑦⑧** | ⑧改 "13 studies / 18 absolute values / 7 denominators + 2 reporting conventions"、把全称否定改为"未能识别任一对共享分母,其中 5 篇摘要未述分母";①重数并逐篇登记分母(已知/未知);⑥§3、⑦`:43-45` 同步 | 旧串清除:`grep -rn "15 recent\|15 个工作\|15 个绝对值\|geq\$9 mutually\|≥9 种\|no two reports share"` → 0;新串命中:`grep -rn "13 \(studies\|篇\)\|18 \(absolute\|个\)\|7 denominators"` → ≥3 处(⑧⑦⑥) |
| **M2** `t08NEb8pTY` 被选择性引用:漏第三结论(scaffolding no consistent benefit)+ 75.0% unseen composite + 跨三基准;让位边界过窄;null-result 安全网被高估 | 重大 | **①②③⑧** | ①重抓完整摘要、补第三结论、**重画让位边界、撤回 line 119 的"不削弱价值"**;②§3 更新;③要件①④ 把差异化收窄到"per-category×route 交互 + 恢复机制剖面",并**重估 null-result 预案的价值**;⑧ `related.tex` 显式 cite 并让位;⑥§3 该锚点改标"**半口径**" | 旧串清除:`grep -rn "唯一缺口"` → 0 或改为"缺口之一";新串命中:`grep -rn "no consistent benefit\|scaffolding do not reliably\|75.0%\|unseen composite"` → ①/②/⑧ 各 ≥1 |
| **M3** `related/method/intro/conclusion` 未实例化;**全文零条可解析引用**(`liberopro2025` 无 bib 条目,`refs.bib` 仅 2 条 EXAMPLE ONLY);`reproducibility.tex:19-21` 虚报审计通过;`conclusion.tex:11`+`intro.tex:25`+`appendix.tex:21-31` 真机主张 vs ⑤ N/A;路径 `tests/exp-<id>/` 不存在;5 处未定义 `\ref` | 重大(其中"虚报审计通过"与"真机主张"为**诚信级**) | **⑧**(部分 ⑦) | `refs.bib` 落 18 条真实条目;四节实例化;`reproducibility.tex` 改诚实版(明写 ⑥ 签 NOT-CLEARED、commit 不存在);删真机主张/整节或标 "not performed";`tests/exp-<id>/`→`04-sim/exp-<id>/`;修 5 处 `\ref`;建 `08-paper/figures/` | 旧串清除:`grep -rn "MethodName\|<key>\|<hash>\|<repo\|tests/exp-\|EXAMPLE ONLY\|real-robot experiments\|audited for full-caliber consistency"` → **0**;新串命中:`grep -c "@" refs.bib` → **≥18**;`grep -rn "R3-NeuTraL"` in `sections/` → ≥4;编译无 undefined reference/citation |
| **M4** `config.yaml:98` 预算低报 40%(225k vs 375k)且无 API 金额;`config.yaml:53` `trainable_backbone: true` 与 "frozen" 矛盾;budget 键只给 B/C 而正文称 "unified";`run.sh` 依赖的 2 个脚本不存在;`:26` "zsh 兼容" 与 `mapfile` 矛盾;`:19-20` 覆写冻结目录 | 重大 | **③④** | `est_rollouts`→375000 + 新增 `est_api_usd` 区间后再交 🔴 人批;修 `trainable_backbone` 或新增 `R3_vla_finetuned`;给全 variant 加 budget 键或改 `experiments.tex:19-20` 措辞;补/stub 两脚本并让 `check_freeze.py` 判 FAIL;删 zsh 声明;env-lock/commit 写 `logs/` | 旧串清除:`grep -rn "225000\|22.5 万\|3臂×5seed\|zsh 兼容"` → 0;新串命中:`grep -n "375000\|est_api_usd"` → ≥2;`ls 04-sim/exp-VP01/*.py` → ≥2 文件存在(或 run.sh 明标 stub) |
| **M5** ⑦ Fig.4 真值(12.8/17.5/13.3)与占位值(31.0/13.6)**同轴**,仅标"部分占位";`figure-spec.md:22` 写死 "26.8pp" | 重大 | **⑦⑧** | Fig.4 拆真值/占位双面板或用不同标记 + **逐点来源图例**;`:22` 删具体占位数;⑧ 引用时图注标 "contains placeholder values (dry-run)" | 旧串清除:`grep -n "部分占位\|26.8pp" 07-figures/figure-spec.md` → 0;新串命中:`grep -n "逐点来源\|per-point provenance\|placeholder panel"` → ≥1 |
| **M6** `experiments.tex:22,35-37,42,49-50,64-66` 共 **≥10 个空键 `\audittodo{}`** 无源键;`traceability.md` §1 仅 6 行未覆盖 | 重大 | **⑧** | 每个 `\audittodo{}` 补 `exp-VP01/<variant>/<metric>` 键;`traceability.md` §1 补齐全部占位单元格(含 Recovery/Cost 两列与 seed 数) | 旧串清除:`grep -c "audittodo{}" sections/*.tex` → **0**(空键全清);新串命中:`grep -o "audittodo{exp-VP01/[^}]*}"` 计数 = `traceability.md` §1 行数 |
| **N1** `README.md` 十段索引把 ⑥ 产物记为 `06-audit/results.json`(实际在 `04-sim/exp-VP01/results.json`,`06-audit/` 下无该文件) | 次要 | **⑧/流水线** | 改索引路径 | `grep -n "06-audit/results.json" README.md` → 0 |
| **N2** ①`:137` "已核最近邻清单(**13 条**)" 实列 **18** 条(14 arXiv + 4 OpenReview);②`:54` 正确写 18;①`:47` 表头 "9 篇 arXiv + 4 篇 OpenReview"=13 行(该表头本身正确) | 次要 | **①** | `:137` 改 18 条,并注明"其中高威胁表 13 条" | `grep -n "13 条" 01-gap/gap-candidates.md` → 0 或改为"13 行(高威胁表)" |
| **N3** `experiments.tex:41` 注释写死占位差 "+26.8pp";`main.tex:25` 注释写死 "87.2±1.3 / exp-014 / 单臂·LIBERO v1"(第三种版本口径) | 次要(违反 ⑥§9 字面) | **⑧** | 两处注释删具体数字;`main.tex:25` 改用正确 exp-id 与 benchmark 版本作示范 | `grep -rn "26.8pp\|87.2\|LIBERO v1" 08-paper/` → 0 |
| **N4** `experiments.tex:54` "hardest evidence" 与 ⑥§5 "最硬的一张图" 指向两个不同对象 | 次要 | **⑧** | 统一优先级表述(或随 F2 一并删除) | `grep -rn "hardest evidence"` → 0 |
| **N5** OpenReview 双版本漂移未登记:`9Li4rfsUQm`≈MotorMind(§V-C 承重锚点)、`jTZo4036Yx`≈RoboAware(`config.yaml:78` 承重装置)、`EiCbKWR16T`≈Harness VLA | 次要 | **①③** | ①登记双版本并核差异;③ 若 SCB 在两版间不同则重选恢复装置 | 新串命中:`grep -n "9Li4rfsUQm\|jTZo4036Yx\|EiCbKWR16T" 01-gap/` → ≥3 |
| **N6** ≥6 篇路线/恢复相关工作不在 ①的 18 条台账内(仅标题级,**我不断言其为威胁**):OpenReview `YG7dj3ymm0` CARE-VLA、`jwz2gSAcus` FIT-MAC、`HpQRObHLFe` OmniBrain-0、`7yegfIsdbX`/`eTQck74Vh4` RoboFoundry;arXiv `2609.30249` RAPID、`2609.37359` Encore、`2610.02788` Skill2Real、`2610.12424` RoboRSI、`2610.10498` EmbodiedRSI、`2609.32862` RoboFoundry | 次要(待核) | **①②** | 逐条 curl 抓摘要,判是否需二次让位;**优先 CARE-VLA / FIT-MAC / RoboFoundry**(路线边界与恢复轴双相关) | 新串命中:①§0.2 表新增行数 ≥6,且每行带"是否做同口径路线对照"判定 |
| **N7** GitHub stars 漂移:基准卡记 328,实测 **332**(pushed_at 2026-07-17 ✅ 与基准卡一致,MIT ✅) | 次要(可销项) | **①/基准卡** | ①§3 待核#5 的 GitHub 部分**可销项**(HF 部分仍未核) | 基准卡 re-review 记录中 stars 更新为 332 |

---

## 7. 保留项 / 待核项(如实列;本次并非"0 错误",但以下各项**我也没核到**,不得当作"没问题")

1. **OpenReview 作者身份 / 双投状态:未核到。** `?id=` 与 `?forum=` 两个端点在 api1/api2 **均返回 403 `ChallengeRequiredError`**(challenge 验证),我只能通过 `notes/search?term=` 取回 title / venue / abstract / keywords / primary_area / TLDR,**`authors` 与 `authorids` 字段未返回**。→ **①§3 待核#2 我同样未能关闭**:`t08NEb8pTY`、`xrcN6ePkAS`、`6xlHe08ZsL`、`xQLW4Y2mei` 四篇在投件的作者、提交日期、是否与某 arXiv 版重复,**未知**。
2. **`6xlHe08ZsL` 与 arXiv `2510.03827` 是否同一团队:未判定。** 我已证二者**口径不同**(4 维 vs 7 类/1,648;副标题不同;官方 repo 只支持前者),但**"是否同团队的扩容版"仍未知**(需作者名单,见 #1)。→ 我的 F1 结论**不依赖**这一判定(F1 只依赖"被 pin 的 simulator 不实现所声称的口径",已由 repo 实证),但**若二者确为同团队扩容版且将放出 1,648 变体代码,F1 的修法应选"等代码"而非"退回 5 维"** —— 这个分支我无法替委托人决定。
3. **全部外部论文仅核到摘要层,未开任何 PDF 全文。** 具体未核到:Pigey 12.8% 的**确切分母与骨干**、DynaHarness 17.5% 的**骨干是否 π₀.₅**、MotorMind "prior zero-shot methods" 的**具体是哪些方法**、WAA 正文实验表中 code-as-policy 对手是否确为 RACaP(①§3 待核#4)、Zetta 90.8% / OpenRUA 87.0% / PrimitiveSuite 82.4% / SCOPE 80.66% 的**分母**(①line 63 已自认 SCOPE "未说明 mean 的任务集")。→ **F2 的"骨干身份未核"是待核项,不是已证伪项**:我说的是"草稿从未核",不是"三篇骨干一定不同"。
4. **① 遗留的 6 条邻接摘要我也未抓**:ManiUnit `2610.12089`、MIKASA-Robo-VLA `2610.00604`、RESETTLE `2610.12185`、Recova `2610.01178`、EvoMem-VLA `2610.05418`、Divide-and-Remember `2610.00982`。→ **Gap-2(恢复轴)的新颖性核对在作者侧和我侧都未完成**;其中 ManiUnit / MIKASA-Robo-VLA 是长程基准,①自己标"须优先补核"。**我的 F4 结论(恢复轴零数据)不依赖此项,但"恢复轴是否真新"仍未定。**
5. **§6-N6 的 ≥6 篇新命中工作仅标题级。** 我在 90 条中用 5 组正则命中了它们,但**未抓摘要** → 按 rubric §6"苛刻但诚实、不夸大",**我不把它们计为已确认的新颖性威胁**,只列为必须补核的待核项。
6. **Google Scholar / GitHub README 全文检索(除 LIBERO-PRO 一个 repo)/ Awesome-Dexterous-Manipulation 元清单:我也未跑。** ①§0.2 line 90 自认 5 条异源路径只完成 2 条;我完成了 arXiv API + OpenReview + **GitHub repo(1 个)**,**仍未达 5 条** → **新颖性结论在两侧都不完整,任何一方都不得下"无人做过"的定论。**
7. **HuggingFace 数据集未核**:`zhouxueyang/LIBERO-Pro`(bddl + init)与其 **CC BY 4.0** 许可我未重抓。→ 若许可口径有变,`config.yaml:88` `data_source` 与开源合规需重估。GitHub 侧已核(MIT / 332 stars / pushed 2026-07-17 / branches 3 / tags 0)。
8. **`check_freeze.py` 与 `significance.py` 未实跑。** ⑥§0 称 "check_freeze.py PASS"、⑥§2 称 "significance.py 实跑输出粘贴" —— **我无法验证这两个工具真的跑过**(目录内无输出工件、无日志;`04-sim/exp-VP01/` 只有 6 个文件)。我采取的替代核法是**手算复核全部统计量**(结果:⑥ 全对,见 §2 通过项)。→ **"PASS" 与 "实跑输出粘贴" 本身是无工件支撑的自述。**
9. **未编译 LaTeX。** 5 处未定义 `\ref` 与 1 处未定义 `\cite` 由静态集合比对得出(对"未定义"是决定性的),但**其他编译期问题(如 `natbib` + `IEEEtran` + `\bibliographystyle{IEEEtran}` 的兼容性、`siunitx` 的 `\num` 在正文中的可用性、`algorithmic` 与 `algorithm` 的浮动冲突)我未验证**。
10. **Table 1 的 "Recovery (%)" 与 "Cost (LLM calls)" 两列的口径定义未在论文任何处给出**(config 有 metric 名但无定义式),故即便补上数据,**列语义仍不可判**。
11. **`xrcN6ePkAS`(PrimitiveSuite)与 `xQLW4Y2mei`(SCOPE)我只核到"存在于 90 条命中中",未逐字复核其摘要数字**(82.4% / 80.66%)。→ ①对这两条的引用准确性**我未验证**。
12. **`05-realexec/protocol.md` 的安全清单(§2,7 项)与回填模板(§4)全部未勾选/未填**,这是 dry-run 的正确状态;但若将来启用 sim-to-real 节,**⑤ 的 🔴 人签名门必须真过**,不能沿用当前空模板。

---

## 8. 放行判定

- **致命清单全部闭环?☐是 ☒否(回灌)**
- **未闭环项(5 条致命全未闭环)**:
  | # | 致命项 | 当前状态 | 能否只靠改写闭环? |
  |---|---|---|---|
  | F1 | 跨 benchmark 版本(`config.yaml:16-19` / `experiments.tex:11-12,77`) | 未闭环 | **不能**。须回 ① 重判 + ③ 重设分层与恢复载体 + ④ 重冻结 + 🔴 委托人裁决(退回官方 5 维 / 等在投件放码) |
  | F2 | 基线对齐检验先验恒真(`experiments.tex:49-54`) | 未闭环 | **不能**。须 ① 从全文核三锚点分母与骨干 + ③ 重设检验 + ④ 重设/删 variant |
  | F3 | 摘要写死 `p<0.05` 越 ⑥ 降级(`abstract.tex:16`) | 未闭环 | **能**(⑧ 单点改写 + traceability 重签)。**本件唯一可低成本闭环的致命项** |
  | F4 | 恢复/成本双轴零数据(`results.json:14-16` vs `experiments.tex:33,62-66`) | 未闭环 | **不能**。须 ④ 真跑 7 个 metric(且受 F1 制约)+ ⑥ 审计;否则 ⑧ 必须**删除该轴并撤回差异化④** |
  | F5 | 主判据无表无图无节 + 消融无处安放且定义不成立 | 未闭环 | **部分能**(⑧ 补节/补 label/重写 C1–C3),但 per-stratum 数据须 ④ 落盘、消融定义须 ③ 重设 |
- **重大项(6 条,M1–M6)**:M1/M3/M5/M6 **可由 ⑧⑦ 改写闭环**;M2 **须 ①②③ 重判**;M4 **须 ③④ 重算与补脚本**。
- **放行结论:❌ 不放行 ⑩。**
  1. **作为投稿物:reject。** 三审 3/2/2,三维度全 ≤4 触发硬规则;含 2 条诚信级条目(F3 显著性越级 + `traceability.md:29` 误签;`reproducibility.tex:19-21` 虚报"已全口径审计")与 1 条无据的真机主张(`conclusion.tex:11` / `intro.tex:25` / `appendix.tex:21-31` vs ⑤ N/A)。**任何一条在真实评审中都足以触发 integrity 质疑。**
  2. **作为 dry-run 流水线验证:部分成功,且暴露了两个真实的闸缺陷(这正是预演的价值)。**
     - ✅ **成功**:⑥ 对占位数据签 ❌ 且 ⑧ 在 §V **确实**全程 `\audittodo{}`(我 grep 遍 `sections/` 未发现任何被 typeset 的占位数值);⑥ 的统计量**手算复核全对**;单/双臂口径**五处全对齐无迁移**;cherry-pick **无**;⑦ 的诚实作图规格**合格**;⑤ 正确自判 N/A;①/② 的诚实标注(待核项、检索式优先级问题、未跑异源)质量高。
     - ❌ **闸缺陷 1(⑧→⑨ 之间)**:**摘要与复现声明绕过了 ⑥ 的降级**。⑥§9 的放行去向只约束了"数字不得写死",**没有约束"显著性措辞与审计状态陈述"** → `abstract.tex:16` 的 `p<0.05` 与 `reproducibility.tex:19-21` 的"已审计"都溜了过去,而 `traceability.md:27,29` 还把它们**勾成了通过**。**建议:paper-writer 侧新增两道双向 Grep 硬门 —— (a)摘要/正文中任何 `p<`、`significant`、`outperform`、`superior` 串必须与 ⑥§2 的判定串逐一比对;(b)任何 "audited / verified / were run" 完成时态串必须与 ⑥ 签发状态比对。**
     - ❌ **闸缺陷 2(⑥ 的跨配置检查)**:⑥§4 **只核了单/双臂,没核 benchmark 版本身份**,于是签了"跨 benchmark 版本比?否 ✅",放行了 F1。**建议:⑥ 的跨配置表新增两行 —— "benchmark 版本字符串 ↔ 该版本官方实现是否支持所声称的规模/类目"(须核官方 repo,不得只核论文自述)、"外部锚点的分母/骨干是否与本文对标口径同构"。**
     - ❌ **闸缺陷 3(计数无人复算)**:M1 的 15/13、9/7 与 M4 的 225k/375k、N2 的 13/18 —— **四个计数错误分布在 ①④⑥⑦⑧ 五个工件里,无一段做过"重新数一遍"**。而 `experiments.tex:57-60` 还自称"externally verified, not placeholder"。**建议:凡标注"已核/非占位"的定量段落,由 ⑥ 或 ⑨ 独立重算计数(不同工件数,不是重读同一份清单)。**
  3. **回灌顺序建议(有依赖,不可并行乱做)**:**① (销项待核#3、重抓 t08NEb8pTY 全文、补核 ≥6 篇) → 🔴 委托人裁决(F1 二选一 + null-result 安全网重估 + 375k/API 预算) → ③ (重设分层/恢复载体/基线对齐检验/消融) → ④ (重冻结 config + 补脚本 + 落 7 metric + per-stratum) → ⑥ (重审,含新增的两道检查) → ⑦ (Fig.4 拆真/占位、补 Fig.6 与定性图) → ⑧ (实例化四节 + 落 18 条 bib + 修全部 ref/cite + 摘要降级 + 复现声明改诚实版) → ⑨ 复审(本表逐条双向 Grep)。**
     - **注意:F3/M1/M3/M5/M6/N1–N4 可在 ⑧⑦ 立即修,不必等上游**;但**F1/F2/F4/F5/M2/M4 必须先过 ①③④**,否则 ⑧ 只会把同一批错误再写一遍。

---

## 署名链

- **起草(审稿)= ⑨ RedTeamReviewer 独立子任务(未参与本草稿起草)· 2026-10-09(`date` 实跑:`Fri Oct 9 21:56:09 CST 2026`)**
- **交叉核 = ⑥ `06-audit/results-audit.md`(签 ❌)+ ⑦ `07-figures/figure-spec.md` + ① `01-gap/gap-candidates.md` §0.2/§3 台账 + ④ `04-sim/exp-VP01/*` 六个工件 + ③/②/⑤ 全文**
- **异检索路径 = arXiv 官方 API(逐字摘要 5 篇 + 2 个新检索式)· OpenReview `api2 …/notes/search`(**全 90 条**,深于作者的 25 条)· **GitHub API + raw 文件全文(官方 repo,作者本轮未跑)** · 手算复核 ⑥ 全部统计量。全程 `curl -sL`,**未用 WebFetch**。**未达 gap-heuristics §5 要求的 5 条路径**(Scholar / 元清单 / HF 未跑),故新颖性结论**不完整**,不下"无人做过"定论。
- **独立性声明 = 本报告全部结论均可回指我实际打开的文件行号或实际抓取的外部响应;凡未核到者一律列入 §7,未以"没查到"冒充"没问题"。我未修改任何被审文件(仅新建本产物)。**
- **状态 = 预演 v0.x(致命清单 5 条全未闭环;仅 F3 可低成本闭环)· ❌ 不放行 ⑩**
