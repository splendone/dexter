# Gap 候选 · 透镜③ 语言条件长程操作 · 2026-10-09

> **① GapScout 产物 · dry-run 验证运行 · 2026-10-09 · 选题方向经委托人 2026-10-09 选定(透镜③)· 价值裁决 🔴 待委托人拍板**

- **产物层级**:🟡 黄档草稿(`reports/drafts/`),未签发。
- **本文件职责**:出候选 + 三判据评估 + 真实核查台账。**选题价值生死由委托人(🔴)拍板**,GapScout 不拍板(gap-heuristics §1 硬规则、§7 末条)。
- **委托人已定方向**(本文不重选方向,只把方向坐实成合格 gap):在 **LIBERO-Pro** 扰动基准上,对「端到端 VLA vs agentic harness vs code-as-policy」三路线做**同口径公平对照**。
- **核查日期**:2026-10-09(`date` 实跑:`Fri Oct 9 21:11:29 CST 2026`)。
- **核查方式**:`curl -sL` 实抓 arXiv 官方 API(`export.arxiv.org/api/query`)+ arXiv abs 页 HTTP 200 校验 + OpenReview API v2(`api2.openreview.net/notes/search`)。**全程未用 WebFetch**(承 gap-heuristics §5:WebFetch 核 arXiv 常超时)。
- **输入**:基准卡 `knowledge/maps/benchmark-libero-pro.md`(2026-09-30 版)、`gap-heuristics.md`、`four-lenses.md` 透镜③段。
- **纪律**:下文【事实】= 我今日实抓原文所见(逐字或直译);【判断】= 我的推论,标置信度。未核到者一律标「待核」,不猜不编。

---

## 0. 真实 arXiv / OpenReview 核查台账(证据纪律)

### 0.1 基准卡关键条目复核(5 个指定条目 + 3 个附带,全部核到)

| 简称 | arXiv ID | 实抓标题(API 逐字) | 提交日 | 基准卡数字 vs 原文 | 核对方式 |
|---|---|---|---|---|---|
| **WAA** | `2609.29964v1` | World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal | 2026-09-24 | ✅ **吻合**。原文:"On LIBERO-Pro, WAA with skills evolved only from LIBERO-90 reaches a state-of-the-art **75.6%** average success, outperforming end-to-end VLAs, code-as-policy agents, and a visual-harness baseline with the same backbone" | curl API;abs 页 HTTP 200(SIZE 44800),`<title>` 与 API 一致 |
| **Robo-Harness K1** | `2609.29389v1` | Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation | 2026-09-24 | ✅ **吻合(三个数字全对)**。原文:"On **matched** LIBERO-PRO tasks, Gemini 3.7 Flash with K1 reaches **77.8%** accuracy, surpassing GPT-6 Astra's **61.1%** with an RGB-only harness; K1 further improves Astra to **88.9%**" | curl API |
| **HarnessPAI** | `2609.29166v1` | HarnessPAI: An Evolving Harness for Physical AI | 2026-09-24 | ✅ **吻合**。原文:"a **61.6-point** gain over π₀.₅ on LIBERO-PRO";"fine-tuning π₀.₅ on collected expert data lifts success rate on LIBERO-PRO by **38.8 points**" | curl API |
| **RACaP** | `2609.29394v1` | RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning | 2026-09-24 | ✅ **吻合**。原文:"achieves **54.4%** success on LIBERO-90, **45.0%** on zero-shot LIBERO-PRO, and 46.0% on LIBERO-Long";"On LIBERO-PRO, it achieves **2.5 times** the success rate of CaP baselines" | curl API |
| **SynthDemo-RL** | `2609.21650v1` | SynthDemo-RL: Breaking the Zero-Reward Barrier in VLA Adaptation with LLM-Guided Synthetic Demonstrations | 2026-09-18 | ✅ **吻合**。原文:"On LIBERO-PRO, a public benchmark of perturbed LIBERO tasks for which no demonstrations exist, **27 of 57 scored tasks** are at exactly **0% success** for a pi_0.5 policy fine-tuned on the original LIBERO tasks … SynthDemo-RL … **rescues all 27**" | curl API |
| LIBERO-Pro 基准论文 | `2510.03827` | LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization | v1 2025-10-04 / v2 updated 2026-05-25 | ✅ **吻合**(标题、v1/v2 日期、8 位作者全名单与基准卡逐字一致:Zhou/Xu/Tie/Y.Chen/G.Zhang/Chu/Pan Zhou/Lichao Sun) | curl API |
| GeoAAC | `2609.20776v1` | GeoAAC: Geometry-Based Adaptive Action Chunking from Denoising Trajectories in VLA Policies | 2026-09-17 | ✅ ID 存在、标题吻合(数字未逐条核,非本 gap 承重项) | curl API |
| CounterAlign | `2608.21740v1` | CounterAlign: Counterfactual Supervision for Vision-Language-Action Models | 2026-08-22 | ✅ ID 存在、标题吻合(同上) | curl API |

**小结(事实)**:指定 5 个条目 **5/5 全部核到且数字逐字吻合**,无一「待核」;附带 3 条亦核到。基准卡在这一点上**经受住了复核**。

**副产物 1(事实)**:SynthDemo-RL 原文确含基准卡待核点③所引措辞 "a public benchmark of perturbed LIBERO tasks for which no demonstrations exist" → 基准卡待核点③中「该措辞来自使用方转述」**转述准确性已证实**(但「LIBERO-Pro 原论文是否自定义『零成功任务』」仍未核,维持开放)。

**副产物 2(事实)**:HarnessPAI 与 Harness VLA(见 §0.2)**只报增量、不报绝对值**。HarnessPAI 摘要全文无自身 LIBERO-Pro 绝对成功率。→ 基准卡「+61.6pp」记录方式正确,但**跨论文比较时这两条无法与绝对值论文并列**,这正是本 gap 的口径痛点之一。

### 0.2 新颖性异源检索(硬约束,承 P-007 / gap-heuristics §5)

**检索路径 4 条,均今日实跑**:

1. **arXiv API** `cat:cs.RO AND all:"LIBERO-Pro"`,`sortBy=submittedDate` descending,`max_results=40` → **命中 40 条,时间跨度 2026-06-26 → 2026-10-08**。
2. **arXiv API** `cat:cs.RO AND (all:"LIBERO-Pro" OR (all:"long-horizon" AND all:"vision-language-action"))` → **totalResults = 401**(委托人指定的检索式,原样跑通)。
3. **arXiv API** `all:"code as policies" AND all:"LIBERO" AND all:"agentic"` → 9 条;`all:"LIBERO-Pro" AND (all:"code-as-policy" OR all:"code as policies")` → 8 条;`cat:cs.RO AND (ti:"empirical study" OR ti:"rethinking" OR ti:"revisiting" OR ti:"towards a unified") AND all:"manipulation"` → 42 条;`cat:cs.RO AND (all:"embodied harness" OR all:"physical harness" OR all:"robot harness")` → 10 条。**逐条读标题,对 9 篇高威胁者实抓摘要**(下表)。
4. **OpenReview API v2** `term=LIBERO-Pro` → **count = 90**,取回前 25 条元数据,对 4 篇高威胁者取回完整摘要。**其中 ICLR 2027 在投工作构成实质新颖性威胁(见下)**。

**⚠️ 检索式说明(诚实标注)**:委托人给的检索式 `cat:cs.RO AND (all:"LIBERO-Pro" OR all:"long-horizon" AND all:"vision-language-action")` 因 AND/OR 优先级,arXiv 实际执行为 `LIBERO-Pro OR (long-horizon AND VLA)`(返回 401 条,含大量与 LIBERO-Pro 无关的长程 VLA 论文)。我**加跑了路径 1(纯 `cat:cs.RO AND all:"LIBERO-Pro"`,40 条)作为收窄主检索**,新颖性结论以路径 1 + 3 + 4 为准,路径 2 仅作覆盖面兜底。

#### 高威胁最近邻实抓摘要台账(9 篇 arXiv + 4 篇 OpenReview)

| 工作 | ID / 来源 | 提交日 | LIBERO-Pro 数字(原文逐字) | 是否做「同口径路线对照」? |
|---|---|---|---|---|
| **Frontier Models for Robotic Manipulation: Rethinking Interaction and Scaffolding** | OpenReview `t08NEb8pTY`(ICLR 2027 在投;keywords 逐字:"Robotics Policy; **Agentic Pipeline: Code as Policy**") | 待核(在投,无 arXiv 版可核) | "GPT-6 achieves 100% success on LIBERO, **95.0% on LIBERO-Pro**, and 88.0% on RoboCasa365 Target50";"increasing the refinement budget from one to eight turns raises LIBERO-Pro success **from 45% to 94%**" | 🔴 **最强威胁**。原文:"comparing **two interaction paradigms**: execution-time decision making … and executable-policy synthesis";"vary the refinement budget and the amount of human-designed scaffolding **with the model, interface, and environment fixed**" → **这就是「固定模型/接口/环境的同口径对照」方法论本身**,已覆盖 agentic harness 与 code-as-policy **两**路线 + 预算轴 + 脚手架量轴。**唯一缺口:未含「训练出来的端到端 VLA」这一臂**。 |
| **Chain-of-Primitives Shapes Robot-Agent Adaptation**(PrimitiveSuite / CoP) | OpenReview `xrcN6ePkAS`(ICLR 2027 在投) | 待核 | "GPT-6 Astra reaches **82.4%** success on LIBERO-Pro";"outperforming representative **VLA, coding-agent, and VLM-harness baselines**" | 🟠 **强威胁**。三臂对照,但三臂是**接口抽象层级**(direct control / geometric specification / semantic invocation),**不是**三路线;VLA/coding-agent/VLM-harness 被当**基线**而非平等臂。核心结论 "no single interface is consistently best" 与本 gap 预期结论部分重叠。 |
| **LIBERO-Pro: A Benchmark for Evaluating the Robustness of Embodied Foundation Models** | OpenReview `6xlHe08ZsL`(ICLR 2027 在投,primary_area: **datasets and benchmarks**) | 待核 | 无自身路线数字;报 "the evaluated models suffer an average performance drop of **25.9 percentage points**, with individual drops reaching **32.5 points**" | 🟠 **基准自身的扩容版**(与 arXiv `2510.03827` 同名不同副标题,见 §3 待核项)。原文:"defines **22 static perturbations and 20 runtime interventions**, resulting in **1,648 validated perturbation variants**";"We evaluate **11 representative robot policies** spanning vision-language-action models, world-action models, and robustness-oriented policies" → **多范式评测已存在,但三类均为「策略族」,不含 agentic harness / code-as-policy**。 |
| **RoboAware: Learning to Coordinate Embodied Skills from Counterfactual Outcomes** | arXiv `2610.11480v1` | **2026-10-08**(昨日) | "**73.8%** on diverse LIBERO-Pro task clusters";"100 tasks" | 🟠 **强威胁(最新)**。原文:"builds on coding agents' skill orchestration";"**State-Locked Counterfactual Branching (SCB)**, which restores the same training state to generate and execute a code block **from each admissible family**" → **同状态跨策略族反事实对照已被实现**,但用作**训练协调器的信号**,且只在 100 任务子集;结论是「学会按状态选族」而非「中立报告三路线剖面」。 |
| **OpenRUA: Robot-Use Agents Are Zero-Shot Visuomotor Policies** | arXiv `2610.02459v1` | 2026-10-01 | "**87.0%** on LIBERO-PRO"(Claude Code + Claude Opus 5)、99.0% on CaP-Bench | 🟡 中威胁。原文自设问题:"**Is such additional harness engineering necessary?**" → 「极简 harness vs 工程化 harness」轴已被占。单路线(纯 coding agent),无三路线对照。 |
| **Fewer Tokens, Better Action**(PyRUA-Lean) | arXiv `2610.01939v1` | 2026-10-01 | "Across **700 simulated task instances from LIBERO-PRO, RoboTwin 2.0, and RoboCasa365** … increases overall success from **63.1% to 71.7%**" | 🟡 中威胁但**可借用**。原文:"we compare PyRUA-Lean with a tool-calling baseline **using the same GPT-6 Astra planner and underlying robot primitives**";"**Under equal LLM-call budgets**";"49% fewer LLM calls and 65% fewer input tokens" → **「同骨干 + 等 LLM 调用预算 + token 计量」方法论已成立**,但只在 agentic 内部两变体间对照。本 gap 的成本轴应直接沿用此口径(降低方法学风险)。 |
| **Zetta ζ: An Efficient Closed-Loop Embodied Harness** | arXiv `2608.16590v1` | 2026-08-17 | "state-of-the-art success on LIBERO-Pro … reaching **90.8%** … **under our current rollout budget**; with an **11.1x inference speedup**" | 🟡 数字威胁(高于基准卡所记 88.9% 上限)。单路线;自陈 budget-dependent。 |
| **MotorMind: Scaffolding General VLMs for Zero-Shot Robot Manipulation** | arXiv `2609.38078v1` | 2026-09-29 | "**66.7%** success on the base LIBERO-PRO suites and **53.8%** under perturbations, compared with **at most 13.3% and 19.2%** … for the prior zero-shot methods we evaluate" | 🟡 口径证据。同论文内**拆两套分母**(base suites / under perturbations),且「prior zero-shot methods」的基线值(≤13.3%)与他篇冻结策略基线(12.8%/17.5%)互不一致。 |
| **DynaHarness: A Dynamic Physical Harness** | arXiv `2609.40306v1` | 2026-09-30 | "**75.2%** on **800 newly sampled initial states**, compared with **17.5%** for the frozen policy";"full dynamic execution reaches 74.0% versus 63.9% under nominal one-step replanning" | 🟡 口径证据。分母显式为「800 个新采样初始状态」,与他篇不可并列。 |
| **Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives** | arXiv `2607.08448v5` | 2026-07-09 | "improves over the strongest relevant baselines by **38.6** and 25.4 percentage points on LIBERO-Pro and RoboCasa365" | 🟡 只报增量;且原文自陈其定位**本身就是三路线混血**("exposes a **frozen VLA** as a retryable contact-rich primitive and composes it with a small fixed library of **analytic primitives**" + "LLM coding agents") → **路线边界在实作中已互相渗透**,「纯三路线」二分法可能被审稿人质疑(见 §2 新意栏风险)。 |
| **Addressing the Orchestration Gap in Generalist Robots via Physical Agency**(Pigey) | arXiv `2607.21725v1` | 2026-07-23 | "On LIBERO-PRO, Pigey advances the state-of-the-art by over 4x (**12.8% -> 53.3%**) with no task-specific fine-tuning" | 🟡 口径证据(关键)。其**冻结策略基线 12.8%**,与 DynaHarness 的 **17.5%**、MotorMind 的 **≤13.3%** 三值互不相同 → **连「同一个冻结 VLA 基线」在论文之间都不可比**。 |
| **Are Frontier VLM Agents Ready to Be Robot Generalists?**(Embodied Agent Arena) | arXiv `2610.00854v2` | 2026-10-01(v2 2026-10-05) | 无 LIBERO-Pro 主数字(1,000 cases / 32 sources + GeoProbe) | 🟡 方法学邻接:7 个 VLM agent × 5 能力轴,「A **minimal harness** preserves source observations and operations while leaving perception, reasoning, and action selection to the model」+ "allotted time and **interaction budgets**"。比的是**模型**不是**路线**。 |
| SCOPE: Selective Certification of Program Edits | OpenReview `xQLW4Y2mei`(ICLR 2027 在投) | 待核 | "On LIBERO-PRO and Robosuite, it achieves mean success rates of **80.66%** and 84.48%, with respective gains of **6.51** and 3.48 percentage points" | 🟢 弱威胁(单路线方法论文),但**又一个不可对齐的分母**(未说明 "mean" 的任务集)。 |

#### 检索得出的三条硬结论

**结论 A(事实):「同口径对照」的方法论已在投,但三臂不全。**
OpenReview `t08NEb8pTY` 已明确做到「model, interface, and environment **fixed**」的两范式对照 + 预算轴 + 脚手架量轴。**本 gap 不能再声称「首次提出同口径对照方法论」**——该声称已被在投工作占据(🔴 新颖性实质削弱,如实报)。**尚存的缺口**:该工作两臂皆为「前沿模型侧」(execution-time decision making / executable-policy synthesis),**不含训练出来的端到端 VLA 臂**;且其结论域是「交互设计」,不是「路线裁决」。

**结论 B(事实):「已有人做同口径三路线对照」= 否,但已有三篇做了「部分路线对照」。**
逐篇核对:**WAA**(`2609.29964`)摘要原文自称 "outperforming **end-to-end VLAs, code-as-policy agents, and a visual-harness baseline with the same backbone**" → **WAA 自己就报了三路线对照**;**HarnessPAI**(`2609.29166`)原文 "improves on both **pure action models and code-as-policy baselines**" → 两路线;**RACaP**(`2609.29394`)原文 "achieves **2.5 times the success rate of CaP baselines**" → 对 CaP。
→ **三路线对照并非无人做过,而是「每篇各做一遍、各用自己的骨干/子集/基线」**。**这恰恰是本 gap 的立论基础,也是它的新颖性天花板**:差异化只能落在「**中立、单一冻结口径、共享分母、含成本与恢复轴**」,不能落在「首次对照」。

**结论 C(事实,本 gap 价值的最强证据):LIBERO-Pro 数字已扩散到 12.8%–95.0%,且至少 7 种互不兼容的分母/报告约定并存。**

*数字跨度(全部今日核到,绝对值口径)*:12.8%(Pigey 冻结基线)· 17.5%(DynaHarness 冻结基线)· 45.0%(RACaP zero-shot)· 53.3%(Pigey)· 53.8/66.7%(MotorMind 扰动/base suites)· 63.1→71.7%(PyRUA-Lean,700 混合实例)· 73.8%(RoboAware)· 75.2%(DynaHarness)· 75.6%(WAA)· 77.8 / 88.9%(K1)· 80.66%(SCOPE)· 82.4%(PrimitiveSuite+Astra)· 87.0%(OpenRUA)· 90.8%(Zetta ζ)· 95.0%(Frontier Models+GPT-6)。
→ **委托人动机所述「45%–88.9%」已被今日核查证实为**过时且偏窄**:真实跨度是 **12.8%–95.0%**(基准卡建档于 2026-09-27/30,其后 9 天内新增 ≥5 篇 LIBERO-Pro 工作)。**这是事实层面的修正,不是判断。**

*分母/口径分歧(逐字摘自各摘要)*:①"matched LIBERO-PRO tasks"(K1)②"800 newly sampled initial states"(DynaHarness)③"57 scored tasks"(SynthDemo-RL)④"base LIBERO-PRO suites" vs "under perturbations" 两套分母(MotorMind)⑤"700 simulated task instances from LIBERO-PRO, RoboTwin 2.0, and RoboCasa365" 跨基准混合(PyRUA-Lean)⑥"100 tasks" / "diverse LIBERO-Pro task clusters"(RoboAware)⑦"1,648 validated perturbation variants" 官方口径(OpenReview `6xlHe08ZsL`)⑧只报增量不报绝对值(HarnessPAI +61.6pp;Harness VLA +38.6pp)⑨显式 budget-dependent(Zetta ζ "under our current rollout budget";Frontier Models "45%→94%" 随 refinement turns 变动)。
→ **无任何两篇共享同一分母**(事实)。

**结论 D(事实,新发现,基准卡未记):LIBERO-Pro 高分段数字高度集中于单一作者群。**
今日实抓作者名单并做集合运算(可复现):
- **WAA(`2609.29964`)∩ K1(`2609.29389`)= 12 位共同作者**(WAA 共 16 位、K1 共 15 位):Zexi Li, Yehang Zhang, Haojian Huang, Yifan Chang, Bohan Zhou, Chenxu Wang, Tianyi Zhang, Yangkai Wei, Wenqian Li, Shiyuan Deng, Yinchuan Li, Ying-Cong Chen。
- **K1 ∩ RACaP(`2609.29394`)= 13 位共同作者**(上述 12 位 + Kaiwen Zhou + James Cheng,减 Shiyuan Deng/Yifan Chang 等微调)。
- **K1 ∩ RACaP ∩ Embodied Agent Arena(`2610.00854`)= 8 位共同作者**:Haojian Huang, Kaiwen Zhou, Wenqian Li, Yangkai Wei, Yehang Zhang, Yinchuan Li, Ying-Cong Chen, Zexi Li。
→ **【事实】** WAA 75.6%、K1 77.8/88.9%、RACaP 45.0% 三个数字出自**高度重叠的同一作者群**;而 WAA 摘要所称「胜过 end-to-end VLAs、code-as-policy agents」中的 code-as-policy 对手,**极可能就是同群的 RACaP**(【判断】,置信度:中——依据是 RACaP 自陈 "Code as Policies (CaP) methods" 定位 + 同群 + 同日提交 2026-09-24;未核 WAA 正文实验表,**留待核**)。
→ **【判断,置信度:高】** 当前 LIBERO-Pro「排行榜」在很大程度上是**同群内部的自我对照**,而非跨团队可比的路线裁决。**这直接强化本 gap 的价值判据**(缺的是「中立第三方 + 单一冻结口径」),**同时也构成新颖性时间窗风险**:该群已握有全部三路线实作与基建,随时可能自行发出同口径对照(其 `2610.00854` Arena 论文显示其已在做「跨模型能力轴 + 预算」型中立评测)。

**未覆盖的检索源(诚实标注)**:Google Scholar、GitHub README 全文、元清单(Awesome-Dexterous-Manipulation)**本轮未跑**(gap-heuristics §5 列的 5 条异源路径中,本轮完成 arXiv API + OpenReview 两条)。→ **标「待外部核实」**,不下「无人做过」的定论。

---

## 1. Gap-1(主候选)

### Gap-1:在 LIBERO-Pro 上,端到端 VLA / agentic harness / code-as-policy 三路线**未在任一共享分母、共享骨干预算与共享成功判据下被同时评测过**,导致「哪条路线真正解决长程泛化」不可判定

- **透镜映射**:
  - **透镜③ 语言条件长程操作**。直接命中 `four-lenses.md` 透镜③「核心问题」末条(逐字):"**Agentic 路线(如 LIBERO-Pro 上的 harness)vs 端到端 VLA,谁更强?**";并命中「关键分歧」首条:"**端到端 vs Agentic vs 程序合成:三股力量的对撞**"。
  - **三股力量对位格**:本 gap **不落在单格,而落在透镜③列的三格之间**(端到端派=强 / agentic 派=强 / 程序合成派=**中**)。
  - ⚠️ **§7 红旗自检(诚实自报)**:gap-heuristics §3 要求「优先弱/中格」,§7 明列 ❌「**挤在强格**」为常见错误。**透镜③ 是 agentic 派的主场(four-lenses.md 末判断逐字:"透镜③ 是 agentic 派的主场,端到端派在追赶"),且今日核查显示这是当前最拥挤的赛道**(路径 1 检索 40 条 LIBERO-Pro 论文,跨度仅 3.5 个月;其中 5 篇集中在 2026-10-01→10-08 的 8 天内)。**本 gap 在「格子拥挤度」上不合格**。
  - **【判断,置信度:中】缓解**:唯一勉强落在中格的是**程序合成派 × 透镜③(中,"语言到程序")**——即把 code-as-policy 臂从「被当基线」提升为「平等臂」,并要求其**程序产物可验证/可复跑**(SCOPE `xQLW4Y2mei`、STeP `2607.18580` 正在此格)。若委托人要把本 gap 从强格挪向中格,**切口应收窄到「三路线的程序性产物与失败恢复的可对照性」**,而非「三路线刷分对照」(见 Gap-2)。

- **来源**(从哪篇精读的局限转化;每条均已实抓 abstract 原文,承 radar 生死线):
  1. `arXiv:2609.29964`(WAA)—— **作者自述局限的反面**:其摘要自称已胜过三路线对手,但**未声明共享分母**;且据 §0.2 结论 D,其对手疑为同群工作。→ 局限:「对照存在但口径不中立」。
  2. `arXiv:2609.29389`(K1)—— 摘要用 "**matched** LIBERO-PRO tasks"(匹配子集),分母未定义 → 局限:子集选择未公开约束。
  3. `arXiv:2609.29166`(HarnessPAI)—— **只报 +61.6pp 增量,不报绝对值**,无法与他篇并列 → 局限:增量口径不可跨论文聚合。
  4. `arXiv:2609.29394`(RACaP)—— 报 45.0% zero-shot,但同篇另报 LIBERO-90 54.4% / LIBERO-Long 46.0%,**三个 LIBERO 变体分母不同** → 局限:变体间不可比。
  5. `arXiv:2609.21650`(SynthDemo-RL)—— **提供了本 gap 最有力的口径工具**:摘要自陈 "We study **reward coverage**, the fraction of tasks for which at least one success is observed **under the fixed evaluation protocol**, **as a complement to the average success rate**",并给出「57 计分任务中 27 个恰为 0%」→ 局限揭示:**平均成功率掩盖了任务级全灭**,必须补分布型指标。
  6. `arXiv:2607.21725`(Pigey)—— 提出 "**orchestration gap**"(冻结技能单独 vs 在 agentic 循环内的差值)概念,但其基线 12.8% 与他篇 17.5% / ≤13.3% 冲突 → 局限:**连基线都未对齐**。
  7. `arXiv:2610.01939`(PyRUA-Lean)—— 提供可借用的**等预算口径**("Under equal LLM-call budgets", "49% fewer LLM calls and 65% fewer input tokens")→ 局限:只在 agentic 内部两变体间用,未跨路线。
  8. OpenReview `t08NEb8pTY`(Frontier Models,ICLR 2027 在投)—— **提供已成立的同口径方法论 + 缺失的第三臂**(见 §0.2 结论 A)。

- **价值**:**判据:高**。理由(全部基于今日核到的事实):
  1. **痛点可量化**:LIBERO-Pro 绝对数字跨度 **12.8%–95.0%**(§0.2 结论 C),**≥9 种互不兼容的分母/报告约定**,**无任何两篇共享分母**。任何「X 路线更强」的断言在当前文献下都不可验证。
  2. **痛点已被领域自陈**:`t08NEb8pTY` 摘要自问 "how these capabilities should be exposed to a robot";`2610.02459`(OpenRUA)摘要自问 "**Is such additional harness engineering necessary?**";`four-lenses.md` 透镜③核心问题亦自陈 "Agentic 路线 vs 端到端 VLA,谁更强?" → **三方(在投工作 / 已发工作 / 本地透镜账本)独立指向同一未决问题**,非自造痛点。
  3. **中立性缺口**:§0.2 结论 D 显示高分数字集中于单一作者群,当前对照多为**同群自我对照** → 独立第三方对照有制度性价值。
  4. **谁会在意**:所有以 LIBERO-Pro 为主评测的工作(今日核到 ≥16 篇)都需要一个可引用的公共口径;审稿人需要它来评判路线声称;基准方(`6xlHe08ZsL`)需要它来验证 1,648 变体口径下的路线排序是否稳定。
  5. **反面风险(诚实标注)**:`t08NEb8pTY` 已给出部分答案——「**refinement budget 单独就能把 LIBERO-Pro 从 45% 抬到 94%**」。若预算效应远大于路线效应,**本 gap 的结论可能是「路线不重要,预算才重要」**,即证成的是 null result。【判断,置信度:中】这**不削弱价值**(null result 对口径混乱的领域同样有价值,且可证伪),但**削弱「卖点」**,须在立项时预先接受。

- **可验证**:**判据:合格(可证伪,量化口径明确)**。
  - **benchmark**:LIBERO-Pro,**公开 sim 基准**。资源今日经基准卡复核:**代码 github.com/Zxy-MLlab/LIBERO-PRO(MIT,328 stars,最后推送 2026-07-17);数据 HuggingFace zhouxueyang/LIBERO-Pro(bddl + init);数据集 CC BY 4.0**(以上数字引自基准卡 2026-09-27 记录,**本轮未重抓 GitHub/HF,标待核**)。
  - **metric**:①各扰动类型成功率(基准卡核实口径:**四维正交维度 + task 作第五类、不入组合**);②**任务级全灭率 / reward coverage**(借 SynthDemo-RL 口径);③**等 LLM 调用预算下的成功率 + token 成本**(借 PyRUA-Lean 口径);④长程分段成功率 + 恢复率(见 Gap-2)。
  - **共享分母候选(事实)**:OpenReview `6xlHe08ZsL` 给出官方规模口径 "**22 static perturbations and 20 runtime interventions** … **1,648 validated perturbation variants**",扰动覆盖 "scene configurations, object properties, visual observations, robot states, temporal conditions, task instructions, and runtime execution states" → **本 gap 应锚定此口径**,而非基准卡所记「官方总数不可得」。
  - **评测协议(事实,基准卡已核 v2 PDF §5.1 逐字)**:"Consistent with the original LIBERO protocol, we set the number of evaluation episodes to **50 per task**"。
  - **⚠️ 可验证性的真实风险(诚实标注)**:①三路线的**骨干不可通约**——端到端 VLA 是训练出来的策略(π₀.₅/OpenVLA),agentic harness 与 code-as-policy 依赖闭源前沿 VLM(GPT-6 Astra / Claude Opus 5 / Gemini 3.7 Flash),**「同骨干」在跨路线时物理上做不到**;退而求其次只能固定「同代最强可用骨干 + 公开报告骨干身份」,这会引入审稿风险。②**算力**:1,648 变体 × 50 回合 × 3 路线 × 多骨干 ≈ 25 万+ rollout,含闭源 API 调用费用。→ 【判断,置信度:高】**全量不可行,必须先做「冻结子集」设计**(如按官方扰动类目分层抽样至 ~200–400 变体),这本身须写进方法档并公开抽样规则,否则又变成新的「私有分母」。

- **新意**:**判据:待核(中,须收窄后方可合格)**。与最近邻的实质差异:
  - vs **`t08NEb8pTY`(Frontier Models)**:差异 = **第三臂(训练出来的端到端 VLA)+ 跨团队中立性 + 官方 1,648 变体分母**;**非差异** = 「固定模型/接口/环境的同口径对照」方法论本身(该工作已有)、预算轴(该工作已有)、脚手架量轴(该工作已有)。→ **本 gap 不得声称方法论首创。**
  - vs **`xrcN6ePkAS`(PrimitiveSuite/CoP)**:差异 = 对照单位是**路线**(学习式策略 / agentic 编排 / 程序合成)而非**接口抽象层级**;**重叠风险** = 其结论 "no single interface is consistently best" 与本 gap 预期结论「无单一路线全胜」在语义上接近,须以**扰动类目 × 路线交互效应**的粒度做出区分。
  - vs **`2610.11480`(RoboAware)**:差异 = 本 gap **不学协调器、不做方法**,只出中立剖面与可复跑协议;RoboAware 把跨族对照当**训练信号**并在 100 任务子集上出方法。→ 差异清晰,**这是最容易守住的区分**。
  - vs **WAA / HarnessPAI / RACaP**:差异 = 中立第三方 + 共享分母 + 含成本轴;**非差异** = 「对照三路线」这一动作本身(三篇各已做过一遍)。
  - vs **`6xlHe08ZsL`(基准官方扩容版)**:差异 = 官方只评「策略族」(VLA / world-action / robustness-oriented),**不含 agentic harness 与 code-as-policy**;本 gap 补的正是这两族 + 与训练式 VLA 的同口径并列。→ **这条差异最硬**(基准方自己不做,且其 primary_area 是 datasets and benchmarks,无动机做路线裁决)。
  - **🔴 换皮风险自检(gap-heuristics §1「只改了形容词」)**:若本 gap 最终产出仅为「把已发表的 15 个数字抄进一张表」,则**是换皮,不合格**。要成立,必须交付**新实验数据**(至少一条路线在冻结子集上重跑)+ **可复跑协议工件**(抽样规则 / 成功判据 / 预算计量 / 种子)。这一条须在 ③方法设计档写成硬约束。

- **新颖性异源核对**:
  - **已核最近邻清单(13 条,全部今日 2026-10-09 实抓摘要原文)**:arXiv `2609.29964`(WAA)、`2609.29389`(K1)、`2609.29166`(HarnessPAI)、`2609.29394`(RACaP)、`2609.21650`(SynthDemo-RL)、`2610.02459`(OpenRUA)、`2610.01939`(PyRUA-Lean)、`2610.11480`(RoboAware)、`2608.16590`(Zetta ζ)、`2609.38078`(MotorMind)、`2609.40306`(DynaHarness)、`2607.08448v5`(Harness VLA)、`2607.21725`(Pigey)、`2610.00854v2`(Embodied Agent Arena);OpenReview `t08NEb8pTY`(Frontier Models)、`xrcN6ePkAS`(PrimitiveSuite/CoP)、`6xlHe08ZsL`(LIBERO-Pro 扩容版)、`xQLW4Y2mei`(SCOPE)。
  - **检索路径**:arXiv 官方 API(6 个不同检索式,见 §0.2)+ OpenReview API v2(count=90,取回 25 条元数据 / 4 篇完整摘要)。**未跑**:Google Scholar、GitHub README 全文、Awesome-Dexterous-Manipulation 元清单 → **标「待外部核实」**。
  - **在投工作是否覆盖**:**部分覆盖(🔴 实质威胁)**。ICLR 2027 在投的 `t08NEb8pTY` 已覆盖「同口径对照方法论 + 两路线 + 预算轴」;`xrcN6ePkAS` 已覆盖「三接口对照 + 无单一最优结论」;`6xlHe08ZsL` 已覆盖「官方多范式评测(策略族)」。**未被覆盖的交集**:训练式端到端 VLA 与 agentic/CaP 在**同一官方 1,648 变体分母 + 等预算 + 含恢复/成本轴**下的中立并列。
  - **时间窗【判断,置信度:高】**:该交集窗口**正在快速关闭**——2026-10-01→10-08 的 8 天内新增 ≥5 篇 LIBERO-Pro 工作,且 `2610.11480`(RoboAware)与 `t08NEb8pTY` 均已逼近该交集。若立项,**须在 2–3 周内锁定冻结子集并出首批数字**,否则新颖性大概率被在投工作吃掉。

- **可证伪实验设想**:
  > **若**在 LIBERO-Pro 官方扰动类目分层抽样的冻结子集(规则公开、种子固定)上,把「训练式端到端 VLA(π₀.₅ / OpenVLA 级)」「agentic harness」「code-as-policy」三臂在**同一子集、同一 50 回合/任务协议、同一成功判据、同一 LLM 调用预算与 token 计量**下并列评测,**则**:(a) 三臂的**排序会随扰动类目翻转**(即不存在单一路线全胜)→ gap 成立;(b) 且**任一臂的绝对成功率都无法复现其原论文自称的数字**(偏差 > 10pp)→ 证实「现有 12.8%–95.0% 跨度主要由口径而非能力差异驱动」。**反之,若**三臂排序在所有扰动类目上一致**且**各臂能复现原论文数字,则本 gap 不成立(口径混乱只是表象,路线优劣已可判定),应丢弃。
  - **前置可证伪的最小实验(建议 ③方法档采用)**:先只做「**基线对齐性检验**」——取三篇论文共用的同一个冻结 VLA(π₀.₅),在同一子集上重跑,看能否同时逼近 Pigey 的 12.8%、DynaHarness 的 17.5%、MotorMind 的 ≤13.3%。**若三值中 ≥2 个无法同时逼近,则「连基线都不可比」被证实**,这是成本最低、最硬的一张图。

- **三判据结论**:☐ 合格候选 ☒ **待核** ☐ 丢弃
  - **价值 = 合格(高)**;**可验证 = 合格(可证伪,但全量算力不可行,须冻结子集)**;**新意 = 待核(中)**。
  - **按 gap-heuristics §1 硬规则「三判据任一不过 → 不立项」,本 gap 现判为「待核」而非「合格候选」。** 转「合格」的**三个必要条件**(缺一即应判丢弃):
    1. **放弃方法论首创声称**,把贡献重述为「**中立第三方 + 官方 1,648 变体分母 + 训练式 VLA 平等臂 + 成本/恢复双轴**」,并在 related work 中显式让位给 `t08NEb8pTY`(方法论)与 `6xlHe08ZsL`(官方口径);
    2. **交付新实验数据 + 可复跑协议工件**(不得只是文献数字汇总表,否则触发 §7「换皮」红旗);
    3. **公开的冻结子集抽样规则**(否则本 gap 自己会变成第 10 种分母,自我反驳)。
  - **【判断,置信度:中】** 三条均可在 ③方法设计档落实,**不构成不可逾越障碍**;但第 1 条会显著压缩论文的「首创」叙事空间,是否接受属**价值取舍 → 🔴 委托人裁决**。

- **置信度**:**中**。
  - **高置信部分**:5 个指定条目 arXiv ID / 标题 / 数字 100% 吻合;数字跨度 12.8%–95.0%;≥9 种分母并存;作者群重叠(集合运算可复现);`t08NEb8pTY` 已占方法论——**以上皆为今日实抓事实**。
  - **待核点(见 §3)**:①WAA 正文实验表中 code-as-policy 对手是否确为 RACaP;②OpenReview 三篇在投工作的作者身份与是否与 arXiv 版重复;③`6xlHe08ZsL` 与 arXiv `2510.03827` 是否同一团队的扩容版(副标题不同);④GitHub/HF 资源可用性本轮未重抓;⑤Google Scholar / 元清单两条异源路径未跑;⑥三臂「同骨干」的物理可行性须由 ③方法档给出工程结论。

- **委托人裁决(🔴)**:价值/选题生死由人拍板,GapScout 只出候选。**需委托人明确回答的三问**:
  1. 是否接受「放弃同口径对照方法论首创、改以中立性 + 第三臂 + 双轴为贡献」这一收窄?
  2. 是否接受「结论可能是 null result(预算效应 > 路线效应)」这一风险?
  3. 是否接受「须 2–3 周内锁定冻结子集」的时间窗压力,还是转 Gap-2?

---

## 2. Gap-2(备选候选)

### Gap-2:三路线在长程扰动下的**错误累积曲线与失败恢复率**从未被量化对照——现有全部 LIBERO-Pro 数字都是**终局二值成功率**,丢弃了「在哪一步崩、能否自己爬回来」这一路线判别信息

- **透镜映射**:
  - **透镜③ 语言条件长程操作**。命中 `four-lenses.md` 透镜③「开放问题」第 2 条(逐字):"**长程任务的错误累积与恢复?**"
  - **直接命中 gap-heuristics §2 透镜③ gap 模式首条(逐字)**:"**长程任务的错误累积与恢复未量化**";并命中其「可验证抓手」(逐字):"**长程任务的分段成功率 + 恢复率**"。
  - **三股力量格**:**程序合成派 × 透镜③ = 中格**(four-lenses.md 对位表,"语言到程序")。理由【判断,置信度:中】:恢复能力在三路线上的机制差异最大——程序合成派的恢复是**代码级重规划/程序修补**(可验证、可复跑:SCOPE `xQLW4Y2mei` 的 "stateful API replay";RACaP 的 "recover from failures without modifying source code"),agentic 派是**推理级重规划**(Zetta ζ 的 "closed-loop … evolves code-based runtime critics and recovery skills **online**"),端到端 VLA **几乎没有内建恢复机制**(Harness VLA 摘要自陈端到端 VLA "often fail under deployment perturbations";SynthDemo-RL 的「27/57 任务 0%」正是无恢复能力的表现)。→ **中格 + 机制差异明确 = 比 Gap-1 更靠近 gap-heuristics §3 的「gap 富矿」。**

- **来源**(均已实抓 abstract):
  1. `arXiv:2609.21650`(SynthDemo-RL)—— **最强来源**。摘要原文:"27 of 57 scored tasks are at **exactly 0% success**";"Direct PPO from this policy … rescues **10 of these 27** tasks and leaves **17 at 0%**";"SynthDemo-RL … **rescues all 27**";并自陈 "**reward coverage** … as a **complement to the average success rate**"。→ **作者亲证:平均成功率不足以刻画失败结构,须补任务级分布指标。**
  2. `arXiv:2608.16590`(Zetta ζ)—— 摘要原文:"existing harnesses remain **largely open-loop**, following fixed skills during rollout and **reflecting only after an episode completes**. Such **post-hoc reflection cannot govern execution as it unfolds**" → **作者自述局限:恢复的时间尺度本身是路线差异变量,但从未被当作评测轴。**
  3. `arXiv:2609.40306`(DynaHarness)—— 摘要原文:"**episode-level failures provide limited guidance on which system component should be revised**";"**Failure attribution** localizes faults in these records" → 失败归因已被提出为**内部机制**,但**未成为跨路线公共 metric**。
  4. `arXiv:2607.08448v5`(Harness VLA)—— 摘要列举扰动类型 "**semantic retargeting, goal re-binding, spatial-layout shifts, and unstable local contacts**",并自陈 "purely analytic primitives struggle with **irregular grasping, constrained placement, and articulated-object interaction**" → **不同路线在不同扰动类目上的失败模式互补,但无人在同一子集上对照过失败模式。**
  5. `arXiv:2610.11480`(RoboAware)—— 摘要原文:"effective composition requires **anticipating which policy family will succeed in the current physical state**";其 SCB "restores the same training state to generate and execute a code block from each admissible family, **exposing outcomes that selected-branch experience leaves unobserved**" → **「同状态跨族反事实」工具已存在,可直接借用为恢复率的测量装置**(这是 Gap-2 相对 Gap-1 的可验证性优势:不必自建口径,可复用已发表装置)。
  6. `arXiv:2610.00854v2`(Embodied Agent Arena)—— 摘要原文:"They often make **partial progress without satisfying all task goals** within allotted time and interaction budgets";"Separate measures of **metric precision, functional grounding, and native goal completion**" → **「部分完成」已被承认为独立于「成功」的信号,但仅在 VLM 模型间比,未在路线间比。**
  - **另注(事实)**:路径 1 检索命中 `2610.12185`(RESETTLE, "Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control")与 `2610.01178`(Recova, "Agent-Guided Failure Recovery for Autonomous Robotic Manipulation"),二者均为 **2026-10-01/08 的恢复类方法论文**(仅读标题,**摘要未抓,标待核**)→ 恢复赛道正在升温,但其为**方法**而非**跨路线对照**。

- **价值**:**判据:中-高**。
  - 痛点(事实支撑):当前 15 个 LIBERO-Pro 数字**全部是终局二值成功率的某种平均**,而 SynthDemo-RL 已证明同一策略在同一基准上可以是「平均 60%」也可以是「27/57 任务恰好 0%」——**平均数抹掉了路线间最本质的机制差异(会不会自己爬回来)**。
  - 长程性直接相关:透镜③ 的定义性问题是「长程」,而**错误累积是长程失败的唯一机制**;只测终局成功率等于不测长程。
  - 谁会在意:所有做 recovery / replanning / closed-loop harness 的工作(Zetta ζ、DynaHarness、RESETTLE、Recova、RoboAware)都需要一个公共恢复 metric 才能互比。
  - **减分项(诚实)**:比 Gap-1 更「学术化」,离委托人选定的「三路线公平对照」切口有一步之遥,**须以 Gap-1 的三臂框架为载体**(即 Gap-2 是 Gap-1 的 metric 升级,而非独立选题)。

- **可验证**:**判据:合格(优于 Gap-1)**。
  - **benchmark**:同 LIBERO-Pro(公开 sim,MIT 代码 / CC BY 4.0 数据,基准卡已核)。
  - **metric(gap-heuristics §2 逐字给出的抓手)**:**分段成功率(sub-goal 级)+ 恢复率**。可操作定义【判断,置信度:中,须在方法档定稿】:①**首次失败步索引**(error onset);②**累积偏差曲线**(每步与参考轨迹/子目标状态的偏离);③**恢复率** = 首次失败后仍终局成功的回合占比;④**恢复延迟**(失败到重新进入正轨的步数/墙钟/LLM 调用数);⑤**任务级全灭率**(reward coverage 补集,借 SynthDemo-RL)。
  - **测量装置可复用(关键优势)**:RoboAware 的 **State-Locked Counterfactual Branching** 提供了「恢复同一状态、跨族执行」的已发表装置 → **不必自建反事实基建**。
  - **扰动轴可用官方类目**:OpenReview `6xlHe08ZsL` 的 22 static perturbations + 20 runtime interventions(**runtime interventions 天然就是恢复率的测试床**——「运行时干预」= 主动注入失败,直接测能否恢复)。→ **这是 Gap-2 相对 Gap-1 的决定性优势:官方基准已内建恢复测试所需的扰动类型,而基准卡所记 arXiv v2 版本并无 runtime intervention 维度。**
  - **可证伪性**:高。恢复率是有界量 [0,1],三路线差异可直接做统计检验。

- **新意**:**判据:较 Gap-1 更强(中-高)**。
  - 与 `t08NEb8pTY`(最强威胁)**正交**:该工作对照的是「交互范式 + 预算 + 脚手架量」,**输出仍是终局成功率**;它未测错误累积与恢复。→ **Gap-2 不与在投最强威胁正面碰撞。**
  - 与 RoboAware 的差异:RoboAware 用同状态跨族分支**训练一个协调器**(方法贡献),Gap-2 用它**测量并公开报告三路线的恢复剖面**(评测贡献),不学任何东西。
  - 与 Zetta ζ / DynaHarness / RESETTLE / Recova 的差异:这些**各自提出恢复机制并只与自己的基线比**;Gap-2 把「恢复」提升为**跨路线公共轴**,不提出新机制。
  - 与 `6xlHe08ZsL`(基准官方)的差异:官方报 "average performance drop of 25.9 percentage points"(仍是**平均成功率差值**),**未报恢复率**。→ 差异清晰。
  - **换皮风险**:低。恢复率/错误累积曲线是**新测量,非新形容词**。

- **新颖性异源核对**:
  - 已核清单:同 Gap-1 的 18 条(§0.2),另加标题级命中 `2610.12185`(RESETTLE)、`2610.01178`(Recova)、`2610.12089`(ManiUnit, "A Manipulation Skill Dataset and Benchmark for Long-Horizon Tasks")、`2610.00604`(MIKASA-Robo-VLA, "Benchmarking Memory in VLA Models for Long-Horizon Manipulation")、`2610.05418`(EvoMem-VLA)、`2610.00982`(Divide-and-Remember)——**此 6 条仅读标题,摘要未抓 → 标待核**。其中 ManiUnit / MIKASA-Robo-VLA 是**长程基准**,可能与 Gap-2 的评测轴重叠,**须优先补核**。
  - 检索路径:同 Gap-1(arXiv API 6 式 + OpenReview API)。**未跑**:Google Scholar、GitHub README、元清单 → 待外部核实。
  - 在投工作是否覆盖:**未发现覆盖**(OpenReview 90 条命中中,取回的 25 条元数据内无「跨路线恢复率对照」型标题;`6xlHe08ZsL` 只报平均降幅)。**但检索深度不足(仅取回 90 条中的 25 条),不下「无人做过」定论。**

- **可证伪实验设想**:
  > **若**在 LIBERO-Pro 的 **runtime interventions** 类目(OpenReview `6xlHe08ZsL` 官方 20 类)上,对三臂测量「恢复率 + 首次失败步索引 + 恢复延迟」,**则**预期:(a) **agentic harness 与 code-as-policy 的恢复率显著高于端到端 VLA**(因后者无内建重规划),但 (b) **其恢复延迟(LLM 调用数/墙钟)也显著更高**,且 (c) **在 object/position 类静态扰动上三臂恢复率差异消失**(该类扰动无需推理级恢复)。→ 三条同时成立则 Gap-2 成立(路线差异是**机制性**的,不可由单一成功率表达)。**反之,若**恢复率在三臂间无显著差异,或差异可被「终局成功率」单一指标完全解释,则 Gap-2 不成立,应丢弃。

- **三判据结论**:☐ 合格候选 ☒ **待核(偏向合格)** ☐ 丢弃
  - **价值 = 中-高(合格)**;**可验证 = 合格(优于 Gap-1,官方 runtime interventions 天然适配)**;**新意 = 中-高(合格,且与最强在投威胁正交)**。
  - **判「待核」而非「合格」的唯一原因**:6 条长程/恢复类邻接工作(ManiUnit、MIKASA-Robo-VLA、RESETTLE、Recova、EvoMem-VLA、Divide-and-Remember)**摘要未抓**,新颖性核对未完成(gap-heuristics §7 ❌「未开 abstract 就立 gap」是死刑级,故此处**宁可判待核**)。**补核这 6 条摘要即可转「合格候选」。**

- **置信度**:**中-高**(事实基础扎实:SynthDemo-RL 的 27/57、Zetta ζ 的 open-loop 自陈、RoboAware 的 SCB 装置、官方 runtime interventions 维度均为今日实抓原文;不确定项集中在 6 条未抓摘要的邻接工作)。
  - 待核点:①6 条长程/恢复邻接工作摘要;②官方 runtime interventions 的 20 类具体清单(`6xlHe08ZsL` 正文,在投版是否可下载 PDF);③「恢复率」是否已有公认定义(若无,本 gap 须自证定义合理性)。

- **委托人裁决(🔴)**:价值/选题生死由人拍板。**建议(仅建议,不拍板)**:将 **Gap-2 作为 Gap-1 的 metric 内核**合并为单一选题——「三路线同口径对照」为骨架(满足委托人已定切口),「错误累积 + 恢复率 + 成本」为差异化血肉(避开 `t08NEb8pTY` 的正面碰撞、脱离「挤在强格刷分」的红旗)。**是否合并、以谁为主,由委托人定。**

---

## 3. 遗留待核项(不丢不猜,交下一段)

| # | 待核项 | 影响 | 建议动作 | 优先级 |
|---|---|---|---|---|
| 1 | **6 条长程/恢复邻接工作摘要未抓**:`2610.12089`(ManiUnit)、`2610.00604`(MIKASA-Robo-VLA)、`2610.12185`(RESETTLE)、`2610.01178`(Recova)、`2610.05418`(EvoMem-VLA)、`2610.00982`(Divide-and-Remember) | **决定 Gap-2 能否从「待核」转「合格」**(§7 死刑级红线) | curl API 逐条抓摘要;重点核 ManiUnit / MIKASA-Robo-VLA 是否已含恢复率轴 | 🔴 高 |
| 2 | **OpenReview 三篇在投工作无 arXiv 版可核**:`t08NEb8pTY`、`xrcN6ePkAS`、`6xlHe08ZsL` 的**作者身份、提交日期、是否双投** | 决定新颖性让位范围;若 `t08NEb8pTY` 与某 arXiv 论文重复则威胁升级 | OpenReview `notes?id=` 取 authors(本轮 `?forum=` 查询返回空,**接口用法待修正**);核 ICLR 2027 双投政策 | 🔴 高 |
| 3 | **`6xlHe08ZsL`(LIBERO-Pro: A Benchmark for Evaluating the Robustness of Embodied Foundation Models)与 arXiv `2510.03827`(…Towards Robust and Fair Evaluation of VLA Models Beyond Memorization)是否同一工作的扩容版** | **直接影响基准卡**:若同一,则基准卡待核点②「官方总任务数不可得」**已被 ICLR 在投版解答为 1,648 validated perturbation variants**,且扰动口径从「四维+task 第五类」扩为「22 static + 20 runtime interventions / 7 大类」 | 比对作者名单与 repo;若确认,**须走 re-review 流程更新基准卡(本轮不改任何他档)** | 🔴 高 |
| 4 | **WAA(`2609.29964`)正文实验表中 code-as-policy 对手是否确为 RACaP(同群工作)** | 决定 §0.2 结论 D「同群自我对照」判断能否从「中置信」升「高置信」 | curl 抓 arXiv HTML/PDF 全文,定位实验表 baseline 段 | 🟡 中 |
| 5 | **GitHub / HuggingFace 资源可用性本轮未重抓**(基准卡记:MIT、328 stars、最后推送 2026-07-17、CC BY 4.0) | 决定 Gap-1/2 的工程可行性与许可合规 | curl GitHub API + HF 页面;**注意基准卡数据为 2026-09-27 记录,已 12 天未复核** | 🟡 中 |
| 6 | **Google Scholar / GitHub README / Awesome-Dexterous-Manipulation 三条异源路径未跑** | gap-heuristics §5 要求 5 条路径,本轮只完成 2 条 → **新颖性结论不完整** | 下一段(②综述)必须补齐,否则不得声称「未被做过」 | 🟡 中 |
| 7 | **三臂「同骨干」物理可行性**:端到端 VLA(π₀.₅/OpenVLA,开权重可训练)vs agentic/CaP(依赖闭源 GPT-6 Astra / Claude Opus 5 / Gemini 3.7 Flash) | **Gap-1 可验证性的根本约束**;若不可通约,「同口径」须重定义为「同代最强 + 公开骨干身份 + 报告骨干成本」 | 交 ③方法设计档出工程结论 | 🔴 高 |
| 8 | **官方 1,648 变体的分层抽样规则**(Gap-1 必要条件 3) | 若抽样规则不公开,本 gap 自己会变成第 10 种分母 → 自我反驳 | 交 ③方法设计档 | 🔴 高 |
| 9 | **算力/API 预算估算**:~25 万+ rollout 全量不可行,须给出冻结子集下的实际预算 | 立项可行性 | 交 ③方法设计档 + ④sim 档 | 🟡 中 |
| 10 | **基准卡所述「45%–88.9%」跨度已被今日核查证伪为过时**(真实跨度 12.8%–95.0%) | **基准卡需更新**(但本轮不改他档) | 记入本文件 §0.2 结论 C,**由 re-review 流程销项** | 🟡 中 |

---

## 4. 附:今日核查对 Dexter 其他档案的回馈(仅记录,本轮不修改任何他档)

1. **`knowledge/maps/benchmark-libero-pro.md`** — 三处需 re-review:①待核点②「官方总任务数不可得」可能已被 ICLR 2027 在投版 `6xlHe08ZsL` 解答(**1,648 validated perturbation variants**,22 static + 20 runtime interventions);②扰动口径可能已从「四维 + task 第五类」扩为 **7 大类**(scene configurations / object properties / visual observations / robot states / temporal conditions / task instructions / runtime execution states);③「已知使用案例」段需补 ≥10 条 2026-09-28 之后的新条目(OpenRUA 87.0%、Zetta ζ 90.8%、DynaHarness 75.2%、MotorMind 66.7/53.8%、RoboAware 73.8%、PyRUA-Lean 71.7%、SCOPE 80.66%、PrimitiveSuite 82.4%、Frontier Models 95.0%、Pigey 53.3%)。**本轮按纪律未改一字。**
2. **`knowledge/controversies`(账本一,透镜③「端到端 vs Agentic vs 程序合成」)** — 今日新增可入账证据:`t08NEb8pTY` 的「**refinement budget 1→8 turns 使 LIBERO-Pro 从 45% 升至 94%**」是**「分歧可能根本不是路线之争,而是预算之争」**的直接证据。此为争议账本级发现,建议下一轮入账。
3. **`four-lenses.md` 透镜③ 代表工作段** — 记 "LIBERO-Pro(2026-09 起):…成为 agentic/harness 路线的主要基准"。今日核查显示该表述仍准确,但**规模已远超「主要基准」**(3.5 个月 40 篇),可考虑升格描述。**未改。**

---

*本文件为 ① GapScout 单段产物,🟡 黄档草稿。门控:GapScout 出候选 + 判据评估(🟡),**选题价值最终裁决属委托人(🔴)**。下一段(②综述)接手前须先清 §3 待核项 #1 #2 #3 #7 #8。*
