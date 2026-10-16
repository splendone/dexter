# 聚焦综述 · LIBERO-Pro 三路线同口径对照 · v0.1(dry-run 验证)

> **② SurveyWeaver 产物 · dry-run 验证运行 · 2026-10-09 · 🟢 级**
> **上游**:① `01-gap/gap-candidates.md`(18 篇已今日 curl 逐字核实)。本段**不重抓**,只做组织(路线 taxonomy + 口径分歧账本),所有数字回指 ① 的核查台账。
> **诚实标注**:①遗留 6 条邻接工作摘要未抓(ManiUnit/MIKASA/RESETTLE/Recova/EvoMem/Divide-and-Remember)→ 本综述标「待核」,不下「无人做过」定论;Google Scholar/元清单两条异源未跑。

## TL;DR

LIBERO-Pro(扰动版 LIBERO)已暴露 VLA「背诵而非理解」(标准 >90% → 扰动坍缩)。3.5 个月内 40 篇工作在此刷分,绝对数字跨度 **12.8%–95.0%**,≥9 种互不兼容分母,**无两篇共享分母**。三路线(端到端 VLA / agentic harness / code-as-policy)各已被对照过,但**每篇各用自己的骨干/子集/基线**,且高分段集中于单一作者群(同群自我对照)。**缺的是:中立第三方 + 官方 1,648 变体分母 + 含训练式 VLA 平等臂 + 恢复/成本双轴的同口径对照。**

## 1. 路线 taxonomy(按三股力量组织,数字回指 ①§0.2)

### 路线 A · 端到端 VLA(训练式策略)
- 代表:π₀.₅ / OpenVLA 级冻结策略。
- LIBERO-Pro 表现:作为**基线**出现,冻结 VLA 基线值互不一致——Pigey 12.8% / DynaHarness 17.5% / MotorMind ≤13.3%(①§0.2 结论 C)。
- 局限:无内建恢复机制;SynthDemo-RL 证「57 计分任务 27 个恰 0%」(①来源5)。

### 路线 B · agentic harness(前沿 VLM + 编排)
- 代表:Robo-Harness K1(77.8→88.9%)、HarnessPAI(+61.6pp,只报增量)、Zetta ζ(90.8%,budget-dependent)、OpenRUA(87.0%)、MotorMind(66.7/53.8%)、DynaHarness(75.2%)、Embodied Agent Arena。
- 特征:依赖闭源前沿 VLM(GPT-6 Astra/Claude Opus 5/Gemini 3.7 Flash);推理级重规划;数字随预算变动(Frontier Models:refinement 1→8 turns 使 45%→94%)。

### 路线 C · code-as-policy / 程序合成
- 代表:RACaP(45.0% zero-shot,2.5× CaP baselines)、WAA(75.6%,自称胜过三路线对手)、SCOPE(80.66%)、PrimitiveSuite/CoP(82.4%,按接口抽象层级对照)。
- 特征:程序产物可验证/可复跑(SCOPE stateful API replay;RACaP recover without modifying source code)。

### 混血(路线边界已互相渗透)
- Harness VLA(2607.08448v5):frozen VLA 当可重试 primitive + analytic primitives + LLM coding agents → 「纯三路线」二分法可能被审稿人质疑(①§0.2)。

## 2. 口径分歧账本(本综述的核心贡献,回指 ①§0.2 结论 C)

| 分歧轴 | 各篇口径(逐字摘 ①) | 后果 |
|---|---|---|
| 分母 | matched tasks(K1)/ 800 new init states(DynaHarness)/ 57 scored(SynthDemo-RL)/ base vs perturbation 两套(MotorMind)/ 700 跨基准混合(PyRUA-Lean)/ 100 tasks(RoboAware)/ 1648 官方(6xlHe08ZsL) | 无两篇可比 |
| 报告方式 | 绝对值 vs 只报增量(HarnessPAI +61.6pp / Harness VLA +38.6pp) | 增量不可跨篇聚合 |
| 预算依赖 | budget-dependent(Zetta ζ / Frontier Models 45→94%) | 不控预算则路线效应与预算效应混淆 |
| 基线 | 冻结 VLA 基线 12.8% / 17.5% / ≤13.3% 三值冲突 | 连基线都不可比 |
| 作者群 | WAA∩K1=12 人、K1∩RACaP=13 人(①§0.2 结论 D) | 高分段=同群自我对照 |

## 3. 与最强在投工作的让位(新颖性,回指 ①§0.2 结论 A/B)

- **`t08NEb8pTY`(Frontier Models,ICLR2027 在投)**:已做「model/interface/environment fixed」两范式对照 + 预算轴 + 脚手架轴 → **本工作不得声称同口径方法论首创**,须显式让位。缺口:不含训练式端到端 VLA 臂。
- **`xrcN6ePkAS`(PrimitiveSuite)**:三臂是接口抽象层级,非路线;结论「no single interface best」与本工作预期部分重叠 → 须以「扰动类目×路线交互效应」粒度区分。
- **`6xlHe08ZsL`(官方扩容版)**:评 11 个策略族(VLA/world-action/robustness),**不含 agentic harness 与 code-as-policy** → 本工作补这两族,差异最硬。
- **`2610.11480`(RoboAware,昨日)**:同状态跨族反事实(SCB)已实现,但用作**训练信号** + 100 任务子集;本工作用作**测量装置**、不学任何东西 → 差异清晰,最易守。

## 4. 开放问题(回指 four-lenses.md 透镜③ + ①)

1. 路线效应 vs 预算效应,谁主导?(可能 null result:「路线不重要,预算才重要」——①Gap-1 价值栏风险)
2. 长程失败的机制差异(错误累积/恢复率)能否被终局成功率单一指标表达?(→ Gap-2,本工作差异化血肉)
3. 跨路线「同骨干」物理不可通约(开权重 VLA vs 闭源前沿 VLM)→「同口径」须重定义为「同代最强 + 公开骨干身份 + 报告骨干成本」(①待核#7,交 ③)。

## 5. 语料清单 / 回指表

18 篇今日实抓条目见 ①`gap-candidates.md` §0.2 表(arXiv 14 + OpenReview 4,每条带 ID/提交日/逐字数字/核对方式)。**待核 6 条**(仅标题级)见 ①§3#1。本综述未新增未核条目。

## 6. 置信度与交接

- **置信度:中-高**(路线 taxonomy 与口径分歧基于 ① 今日逐字核实的事实;不确定项集中在 6 条未抓摘要 + 3 篇 OpenReview 在投工作作者身份)。
- **保留项(不把没查到说成没问题)**:Scholar/元清单未跑;`6xlHe08ZsL` 与 `2510.03827` 是否同工作未定(影响基准卡 re-review)。
- **交接 ③**:本综述的「口径分歧账本」+「让位边界」+「三开放问题」是 method-spec 的输入;③ 须把「冻结子集抽样规则、三臂骨干口径、恢复/成本双轴 metric」写成硬约束(回应 ①待核#7#8)。

---
起草 = {{INSTANCE_NAME}}(2026-10-09)| 复核 = 待 ⑨ 独立子任务 | 状态 = v0.1 dry-run(占位于验证命名空间,不签发 final/)
