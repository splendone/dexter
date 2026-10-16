# 基准卡 · LIBERO-Pro(专项核实卡)

> 建档:2026-09-27 LIBERO-Pro 专项核查班。核实方式:arXiv API 检索 + abs 页
> + HTML 全文 + 官方 GitHub README,三个来源交叉。格式对齐 `benchmarks.md`
> 规则:数字逐字来自来源页,出处随行标注。本卡建立后 `benchmarks.md` 中
> "LIBERO-Pro ⏳ 待核" 条目即可销项(销项动作留给下次改地图时一并做)。

## LIBERO-Pro ✅(置信度:高——abs 页/HTML 全文/官方 README/**v2 PDF 全文**四源交叉)

### 论文信息(abs 页 arxiv.org/abs/2510.03827 逐字)

- 论文:**LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action
  Models Beyond Memorization**(arXiv:2510.03827,cs.CV 主分类 + cs.RO;
  v1 提交 2025-10-04,v2 修订 2026-05-25;"10 pages, 7 figures, 0 tables")
- 作者:Xueyang Zhou, Yangming Xu, Guiyao Tie, Yongchao Chen, Guowen Zhang,
  Duanfeng Chu, Pan Zhou, Lichao Sun
- 机构(README 作者上标逐字):华中科技大学(5 人:Zhou/Xu/Tie/Zhang/Pan Zhou)、
  武汉理工大学(Duanfeng Chu)、Lehigh University(Lichao Sun);
  Yongchao Chen 两源不一致 → 待核点 ①(README 标 Harvard+MIT,arXiv HTML v2
  标 "College of AI, Tsinghua University")
- 与原 LIBERO(arXiv:2306.03310,UT Austin, Liu et al.)**不是同一工作**:
  作者团队不同;官方仓库自述 "an evaluation extension of the original LIBERO
  benchmark"(github.com/Zxy-MLlab/LIBERO-PRO About)

### 定义口径(abs + 全文 §4.3 + README 逐句)

- **是什么**:LIBERO 的扩展评测基准——在原 LIBERO 任务上施加"合理扰动"
  (reasonable perturbations),检验 VLA 是真泛化还是死记训练集的动作序列与
  环境布局;即插即用(plug-and-play),扰动可经 YAML 组合配置。
- **扰动维度**:abs / Introduction / §4.1 列**四维正交维度**——被操作物体、
  初始状态、任务指令、环境;§4.3 与 Fig.6 列**五类扰动**——Object(改外观/
  颜色/尺度)、Position(物体换位)、Semantic(指令改写:"Grasp the mug"→
  "Pick up the cup")、Task(重设计任务逻辑与目标:"Pick up the mug"→
  "Pick up the butter")、Environment(换桌面/背景/光照)。**口径不一致系论文
  自身**(形式化记号只含 O/R/L/E 四维,Task 单列);§4.3 明确:任务级扰动
  **不参与跨类组合**(防不可行组合)。→ 2026-09-28 已复抓全文核实,见
  "核实记录"。
- **核心发现**(abs 页原文):现有模型标准 LIBERO 评测 >90% 成功率,在
  LIBERO-Pro 泛化设置下**坍缩到 0.0%**;物体换成无关物品仍执行抓取,
  指令换成乱码输出不变——暴露"背诵式记忆"而非任务理解。
- **任务构成**:建立在原 LIBERO 四套件(Goal/Spatial/10/Object)之上;
  README 评测代码常量给出**每类扰动 × 每套件**的任务数:Goal 300、
  Spatial 220、10 520、Object 280(代码中 LAN/OBJECT/SWAP/TASK/ENV 各类
  重复此数);评测协议沿用原 LIBERO:**每任务 50 回合**(全文 §5.1)。
  **官方总任务数在 abs / HTML v2 / README / v2 PDF 四源均未声明 → 定案"官方总数
  不可得"(2026-09-30)**;上述 300/220/520/280 是**代码常量**(每类扰动×每套件),
  **不是官方总数**——引用时不得相加冒充总数。
- **是否分布外设计**:是——这是判断:基准以"扰动泛化、Beyond
  Memorization"为立意,训练集未覆盖扰动后的任务;使用方 SynthDemo-RL
  (arXiv:2609.21650)转述其为 "a public benchmark of perturbed LIBERO tasks
  **for which no demonstrations exist**"(无示范任务的扰动 LIBERO 基准)。

### 已知使用案例(数字均核自今日 API feed 摘要原文,2026-09-27)

- **WAA**(arXiv:2609.29964):仅由 LIBERO-90 演化技能的 WAA 在 LIBERO-Pro
  达 **75.6% 平均成功率**,自称 state-of-the-art,胜过端到端 VLA、
  code-as-policy 与同骨干视觉 harness 基线。
- **Robo-Harness K1**(arXiv:2609.29389):匹配 LIBERO-PRO 任务上
  Gemini 3.7 Flash + K1 **77.8%**,胜过 RGB-only harness 的 GPT-6 Astra
  61.1%;K1 把 Astra 进一步提到 **88.9%**。
- **SynthDemo-RL**(arXiv:2609.21650):在 LIBERO-PRO 上,原 LIBERO 任务
  微调过的 pi_0.5 策略 **57 个计分任务中 27 个恰为 0% 成功**;其方法救回
  全部 27 个(定义"reward coverage"指标即基于此)。
- **HarnessPAI**(arXiv:2609.29166):较 π0.5 在 LIBERO-PRO 提升 **61.6 个
  百分点**;π0.5 用其收敛程序采集专家数据再微调可再涨 38.8 个百分点。
- **RACaP**(arXiv:2609.29394):zero-shot LIBERO-PRO **45.0%**(LIBERO-90
  上 54.4%)。
- 另有 GeoAAC(arXiv:2609.20776)、CounterAlign(arXiv:2608.21740)将其
  用作主评测之一;CounterAlign 称其为 "robustness-focused"。

### 与原 LIBERO 的关系

- 扩展而非替代:沿用原 LIBERO 四套件与每任务 50 回合协议(全文 §5.1
  "Consistent with the original LIBERO protocol");官方 README 要求**同时
  引用 LIBERO 与 LIBERO-PRO** 两篇。
- 原 LIBERO 卡见 `benchmarks.md`;两者口径互补——原版测"学过的任务",
  LIBERO-Pro 测"扰动后的任务"(这是判断)。

### 资源与许可

- 代码:github.com/Zxy-MLlab/LIBERO-PRO(GitHub API:**MIT**;328 stars;
  建仓 2025-08-23,最后推送 2026-07-17)
- 数据:HuggingFace zhouxueyang/LIBERO-Pro(bddl + init 文件,README 称
  支持快速并行评测);README 许可表:**数据集 CC BY 4.0**
- 项目主页:zxy-mllab.github.io/LIBERO-PRO-Webpage/(README 链接,未打开)

### 待核点

1. **Yongchao Chen 隶属**:~~两源冲突~~ → **✅ 已定案(2026-09-30,以 v2 PDF 作者块为准)=
   College of AI, Tsinghua University**。三源对照:README 标 Harvard+MIT;arXiv HTML v2
   标 Tsinghua;**v2 PDF 作者块逐字**"Xueyang Zhou¹ Yangming Xu¹ Guiyao Tie¹
   **Yongchao Chen²** Guowen Zhang¹ Duanfeng Chu³ Pan Zhou¹ Lichao Sun⁴ / ¹Huazhong
   University of Science and Technology **²College of AI, Tsinghua University**
   ³Wuhan University of Technology ⁴Lehigh University"——**2 源(Tsinghua)对 1 源
   (Harvard+MIT)**,以论文 PDF 为准。README 的 Harvard+MIT 为孤例(或为旧版/协作关系,
   未证实,不作断言)。
2. **官方总任务数**:**✅ 已定案(2026-09-30)= 论文未声明**。复抓 **v2 PDF 全文
   (arXiv:2510.03827v2,7 页)**逐页检索:全文**无任何"总任务数"声明**;论文只给
   ①"每任务 **50** 回合"评测协议(§5.1 逐字:"Consistent with the original LIBERO
   protocol, we set the number of evaluation episodes to 50 per task")与②"see
   **Tables 7**"(§5.2,但该表**未在 PDF 正文中出现/未展开**,与 v1 标注"0 tables"
   一致)。→ **官方总数不可得**;可引用的规模口径只有**代码常量**(每类扰动×每套件:
   Goal 300 / Spatial 220 / 10 520 / Object 280,见下"任务构成")。**引用时不得把
   代码常量相加当作官方总数**。
   ~~v2 摘要"四维"与 §4.3/README"五维"口径出入~~ → **✅ 已解决,见下"核实记录"**。
3. **"零成功任务"的官方定义**:该词组来自使用方转述(SynthDemo-RL);
   原始论文是否定义同名概念未核(原论文的对应表述是"泛化设置下坍缩到
   0.0%")。
4. v1(2025-10-04)与 v2(2026-05-25)的差异未逐条比对(排行榜数字以 v2 为准)。

### 核实记录(活文档)

#### 2026-10-15 · Round 2 权威性检验 N1:扰动维度定案细化(触发:领域级图谱签发前置,跨源定案回流)

- **来源**:`reports/drafts/领域级图谱-权威性检验记录-v0.1.md` §2 **N1**(定案全文 + 逐字引句)与 §0 抓取日志
  (`https://arxiv.org/abs/2510.03827` HTTP 200 / 43,388 B;`https://arxiv.org/html/2510.03827` HTTP 200 /
  127,339 B,**v2** LaTeXML 全文,去标签 34,316 B / 343 行,**59 个 math 标签 alttext 全保留 59**)。
  **与本卡 2026-09-28 / 09-30 两次独立核实结论一致,无矛盾**;N1 在此基础上**新增两条原文级细节**。
- **细节① · 形式化记号自身即"声明四维、定义五算子"(k=T 是论文正式定义的第五个算子,不是图注口误)**:
  §4.1 先写 "we design a perturbation-based framework that introduces controlled variations across **four
  orthogonal dimensions: object attributes, initial spatial configurations, task instructions, and environments**
  … we generate perturbed variants `T^(k)=φ_k(T)`, where **`k∈{O,R,L,E}`**",**紧接的算子枚举却在四个之外
  另定义了第五个**:
  - "Object attribute perturbation ( `k=O` ) modifies non-essential visual attributes of objects…"
  - "Initial configuration perturbation ( `k=R` ) alters the absolute and relative positions of objects…"
  - "Instruction perturbation ( `k=L` ) includes both semantic- and task-level variations…"
  - "**Task perturbation ( `k=T` ) modifies the target object or action while remaining within the training
    distribution. The perturbed task is `T^(T)=(l,e,G^(T))`.**" ← **带自己的公式,是正式定义的算子**
  - "Environment perturbation ( `k=E` ) modifies the visual environment context…"
  **`k=T` 被显式排除在跨类组合之外**(两处原文):
  - **Figure 6 图注**逐字:"Figure 6: Overview of LIBERO-PRO. LIBERO-PRO extends LIBERO with **five
    perturbation types: object, configuration, instruction, task, and environment**. … **To ensure feasibility,
    task perturbations are excluded from cross-type combinations**, while the other perturbation types can be
    freely composed."
  - **§4.3** 逐字:"…**task-level perturbations are excluded from cross-type compositions**, while the remaining
    perturbation types may be freely combined to construct diverse evaluation settings."
  → **即 `k∈{O,R,L,E}` 与同节的 `k=T` 算子定义自相矛盾,这是论文自身的形式化不一致(不是本地转述错误)。**
- **细节② · "四维"的具体命名在论文内有四种措辞(论文未声明哪一组是权威口径)**:
  | 出处 | 逐字命名 |
  |---|---|
  | 摘要(abs) | "four dimensions: **manipulated objects, initial states, task instructions, and environments**" |
  | Introduction | "four orthogonal dimensions—**manipulated objects, initial states, task instructions, and environments**" |
  | §4.1(形式化) | "four orthogonal dimensions: **object attributes, initial spatial configurations, task instructions, and environments**" |
  | §5.1 | "four perspectives: **object properties, initial positions, task instructions (covering both semantic and structural variations), and environments**" ← **把 task 折进 instruction 维** |
  | §5.2 | "four dimensions: **objects, goals, spatial configurations, and task sets** (see Tables 7)" |
  → **引用必须带脚注说明命名不统一**;**"哪一组是权威口径"论文未声明 → 本所只给"最稳引用写法",不判定论文
  哪一处为误**(置信度标注:命名不统一 = 原文事实,高;"哪组为正" = 不可判定)。
- **本卡「定义口径 · 扰动维度」条的引用写法据此更新(定案,置信度高)**:
  **"四个正交扰动维度(物体属性 / 初始空间构型 / 任务指令 / 环境)+ task 作第五类扰动、被显式排除在跨类组合
  之外"**,并加脚注说明"四维"命名在论文内有四种措辞。
  **⚠️ 不得径写"五维正交"**(与摘要及形式化记号 `k∈{O,R,L,E}` 冲突);
  **⚠️ 也不得径写"仅四维、无 task 扰动"**(§4.1 确实定义了 `k=T` 算子与 `T^(T)=(l,e,G^(T))` 公式,
  Figure 6 与 §4.3 均列五类)。
- **⚠️ 横向对比护栏(新增)**:凡把"扰动维度数"当可比指标横向对比 **LIBERO-PRO(4+1)/ LIBERO-Plus(7)/
  LIBERO-VPro(12 类)** 的表格,**必须显式注明各家维度定义不同轴、不可直接比数**。
- **附带再确认(与既有卡片一致,非新定案)**:§5.2 逐字 "Pi0.5 achieves a **0.38** success rate in the
  libero-goal task under position changes, compared to **0** for OpenVLA and Pi0";摘要逐字 "although existing
  models achieve **over 90%** accuracy under the standard LIBERO evaluation, their performance **collapses to
  0.0%** under our generalized setting";§5.1 逐字 "we set the number of evaluation episodes to **50 per task**";
  **全文仍无总任务数声明**(本轮 v2 HTML 全文再次确认)→ **维持待核点 ② 的定案"官方总数不可得"**,
  代码常量 300/220/520/280 **不得相加冒充总数**。
- **⚠️ venue 仍未核实(不编造)**:arXiv **comment 只有版面信息**(逐字 "10 pages, 7 figures, 0 tables")、
  **无 venue 信息、无 journal_ref**;Crossref 书目检索(HTTP 200 / 9,502 B)**无该文 DOI**(只返回同领域他文,
  如 "LIBERO-X: Robustness Litmus for VLA" in *Robotics: Science and Systems XXII*,DOI `10.15607/rss.2026.xxii.097`
  —— **那是另一篇,不是 LIBERO-PRO**);OpenReview `term=LIBERO-PRO`(HTTP 200 / 266,641 B,count=79)返回一条
  **题名近似但不同**的 "LIBERO-Pro: A Benchmark for Evaluating the Robustness of Embodied Foundation Models"
  (`venue: ICLR 2027 Conference Submission`,id=`6xlHe08ZsL`,在投匿名)——**题名与 arXiv v2 不同 → 本轮不采信、
  不据此作任何 venue 或身份结论**(守宪法"非公开信息(未公开论文评审)不碰";仅登记为**线索**,留待其正式录用后再核)。
  → **LIBERO-PRO venue = 未核实**。**⚠️ 但"未核实"≠"未发表"**:RoboArena 已被证为
  "Crossref 0 记录 + arXiv 无 journal_ref 却已 CoRL 2025 Oral",故本条**同样可能低估其发表状态**
  (判例见 `lessons.md`:「arXiv comment ≠ venue」+ 对称规则「Crossref `total-results:0` ≠ 未发表」)。
- **本卡状态**:待核点 ①②**维持已关闭**;③(零成功任务官方定义)与 ④(v1/v2 差异)维持开放(低优先);
  **新增待核点 ⑤ = venue(未核实,须走 OpenReview + 官方论文集;Crossref/arXiv comment 不足以否证)**。
  **另注**:本轮**未复核官方 GitHub README**(既有代码常量 300/220/520/280 出自 README)→
  N1 的"总任务数未声明"仅据论文全文,**未与 README 二次交叉**,如实登记。

#### 2026-09-30 · 复抓 v2 PDF 全文(触发:G1「权威性检验」判据收束,清待核点 ①②)

- **来源**:`https://arxiv.org/pdf/2510.03827`(pypdf 抽取全文;PDF 页脚逐字
  "**arXiv:2510.03827v2 [cs.CV] 25 May 2026**"→ 确认抓的是 v2;7 页)。
- **待核点 ①(隶属)定案**:PDF 作者块**逐字**给出四机构上标(见上"待核点 1")
  ——**Yongchao Chen = ²College of AI, Tsinghua University**。→ **三源中 2 源
  (arXiv HTML v2 + v2 PDF)对 1 源(README)**,以论文 PDF 为准,**定案 Tsinghua**。
- **待核点 ②(总任务数)定案 = 论文未声明**:全文 7 页逐页检索,**无任何总任务数
  声明**;§5.1 只给"每任务 **50** 回合"协议(逐字确认),§5.2 引"see **Tables 7**"
  但 PDF 正文**未含该表**(与 v1"0 tables"标注一致)。→ **官方总数不可得**;
  规模口径只可用代码常量(300/220/520/280,每类扰动×每套件)。**这是"官方口径
  缺失"型定案,非"两源冲突"型**——如实标注。
- **附带确认**:§5.2 原文另给一个可引用数字——Pi0.5 在 libero-goal 的**位置扰动**下
  成功率 **0.38**,而 OpenVLA 与 Pi0 为 **0**(论文口径,可作"模型间差异被标准
  基准掩盖"的例证)。
- **本卡状态**:待核点 ①②**已关闭**;③(零成功任务官方定义)与 ④(v1/v2 差异)
  维持开放(低优先)。

#### 2026-09-28 · 复抓 arXiv HTML v2 全文(触发:latest.md"下一轮必做"②)

- **四维 vs 五维 = 论文自身的口径不一致,非本地转述错误**。逐句核对 HTML v2:
  - 摘要 / Introduction / §4.1 / §4.2 一律写 **four orthogonal dimensions**:
    manipulated objects(object attributes)、initial states(spatial
    configurations)、task instructions、environments;
  - §4.3 与 Figure 6 caption 写 **five perturbation types**: object、
    configuration、instruction、**task**、environment;
  - **调和规则(§4.1 形式化 + §4.3 原文)**:形式化记号只定义
    k ∈ {O, R, L, E}(四个),任务扰动 k=T 单列;§4.3 明确
    "**task-level perturbations are excluded from cross-type
    compositions**"(任务级扰动不参与跨类组合,防不可行组合)。
  → **结论(置信度高)**:引用时用"**四维(正交维度)+ 任务作第五类、
  不入组合**"最稳;单说"五维"与摘要冲突,单说"四维"漏掉 §4.3 的 task
  扰动类型。
- **总任务数**:HTML v2 正文仍无总数;文中引用 "Tables [7]" 承载任务表,
  HTML 版未展开表格 → 维持"未证实",改从 PDF 附录再核(下轮)。
- **Yongchao Chen**:HTML v2 作者块再确认 "College of AI, Tsinghua
  University";与 README 的 Harvard+MIT 仍冲突 → 维持待核点 ①。
- **本卡自身**:复核确认本卡原判("abs 四维 / 正文五维,口径出入待核")
  **与原文一致,无本地错误**——当日简报速记"扰动五维"是省略,不是错误。
