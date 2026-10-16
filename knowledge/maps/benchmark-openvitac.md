# 基准卡 · OpenViTac(视触操作统一仿真—真实基准)

> **建卡**:2026-10-09,透镜② OpenViTac(arXiv:2610.10384)**全文级按需重审**时建立
> (承 A-018 证据触发 + G4 前置门第 4 项 + 立场文章 v1.0 脆弱点⑦ 三处下游指向)。
> **核实方式(外部交叉源硬规则)**:派异路径子 agent `curl -sL arxiv.org/html/2610.10384`
> 读 **LaTeXML 全文(369,552 字节,去标签正文 70,808 字节 / 2,442 行,§1–§5 + Appendix A–E)**
> + abs 页(44,168 字节)+ 官方 API `export.arxiv.org/api/query?id_list=`;
> **主会话独立 curl 复验**关键句逐字命中(不轻信子 agent)。
> **纪律**:只录实际读到的原文;未读到的标「未核 / 原文未提」;事实与判断分离。

## 著录(三源逐字一致:官方 API + abs `citation_*` + HTML `<title>`)

- **arXiv ID**:`2610.10384v1`(published = updated = **2026-10-07T16:43:29Z**,无修订版)
- **标题**:*OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework*
- **作者(17 人,API 顺序)**:Yifan Wu, Qin Li, Nan Min, Guojin Zhong, Haoyu Zhao, Zhiyuan Li,
  Houze Xu, Shengqi Xu, Xingyao Lin, Zijie Diao, Zhaoxiang Liu, Shiguo Lian, Shunlin Lu,
  Shihao Zhao, Ziyi Ye, Zuxuan Wu, Yu-Gang Jiang
  (Wu/Li/Min = equal contribution;Zhong/Zhao = project leaders,HTML 脚注)
- **机构(6,HTML 页眉)**:复旦大学 / 上海多模态具身智能重点实验室 / 合肥工业大学 /
  新加坡国立大学 / Neote AI / 中国联通
- **主分类**:`cs.RO`(唯一);**DOI**:无;**项目页**:`https://fvl-repo.github.io/OpenViTac/`(**未访问,内容未核**)
- **命名澄清**:「OpenViTac」是**论文自命名的基准名**(在标题里),非本所代号;
  论文另有一个独立命名的**方法** **OpenVTLA**(触觉增强框架)——**两者不可混用**。

## 规模口径(原文直接陈述,高置信)

| 维度 | 数值 | 出处 |
|---|---|---|
| 任务 | **11 仿真任务 + 8 成对真实任务**(4 能力维度) | §3 / §3.1 |
| 4 能力维度 | Property Perception(PP)/ Fragility-Aware(FA)/ Contact-Rich(CR)/ Precision Manipulation(PR) | §3.1 Task suite |
| 仿真数据 | **1,300 episodes / ≈918K frames**(per sensor config) | Appendix B.3 |
| 真实数据 | **2,400 demonstrations / ≈2.1M frames**(per sensor config,8 任务) | Appendix B.3 |
| 触觉传感器 | **3 种**:GelSight / Xense / NeoteAI | Appendix B.2 |
| 夹爪 | **2 种**:Franka Hand / Robotiq(**平行夹爪,无灵巧手**) | Appendix B.2 |
| 仿真后端 | NVIDIA Isaac Sim 5.1.0 + Isaac Lab 2.3.0;触觉仿真 = TacEx | Appendix B.2 |
| 被评测策略 | **11 个**(6 VLA + 3 WAM + 1 既有 VTLA + 自家 OpenVTLA) | §4.1 |
| 真实评测试次 | **20 trials/任务**(In-B v2 = 30)→ 每模型约 170 次真实试验 | §4.4 / Table 3 |
| 跨域一致性 | 8 共享任务、7 方法:Pearson **r = 0.967**、MMRV = 0.006(遵 SIMPLER「保相对序不保绝对值」) | §4.2 |

**⚠️ 原文未披露的规模要件(全文 grep 确认,复现关键)**:
- **仿真评测的 rollout/episode 数**——原文未提(Table 2 只给百分比)。
- **随机种子数 / 训练重复次数 / 标准差 / 置信区间 / 显著性检验**——`seed` 0 命中、`±` 0 命中,**全部未提**。
- **Table 2/3/4 头号结果用哪一种触觉传感器**——原文未提(仅说数据在 3 种配置各采一份)。
- **代码 / 数据 / 环境的发布状态与许可**——正文**无任何发布声明**(grep `open-source`/`release`/`github`/`available at`/`will be made` 仅命中 arXiv UI 文本、页眉 URL、一条参考文献标题)→ **许可:未核**。

## 「触觉边际价值」受控对撞(本卡最关键判定)

**结论:OpenViTac 确实做了「加触觉 vs 不加触觉」的同骨干受控对撞**(不是只收集/评测数据):
- §3.2:「all variants start from the **same pretrained π₀.₅ backbone**」;Appendix C:「OpenVTLA uses the **same implementation as π₀.₅**」;Table S4:π₀.₅ 与 OpenVTLA 同 **20k steps / batch 64**。
- §4.2:「On the eight tasks shared across simulation and the real world, **OpenVTLA improves over π₀.₅ by 13.6 and 13.5 percentage points**, respectively.」(**子 agent 从 Table 2/3 原始分数独立复算通过,主会话 curl 复验原句命中**:仿真 46.16→59.75=+13.59;真实 41.0→54.6=+13.58)。
- §4.4:对 vision-only π₀.₅ 做平行对照(0/250/500 仿真示范 × 2 任务 × 20 试验,Table 5)。
- Appendix D:两项**只改一个因子**的受控消融(触觉预训练 AnyTouch2 68.7% vs random-init 56.5%;时序上下文 68.7% vs repeated-frame 58.4%)。
- **并报告了负/零结果**(非单向宣传):§4.2「On Contact-Rich (CR) tasks, strong VLAs remain competitive」「PR … tactile sensing alone is insufficient」;Table 3 真实:PD 上 OpenVTLA 12/20 = π₀.₅ 12/20(零增益)、In-B v1 上 3/20 **低于** π₀.₅ 5/20。增益集中在 PP(RC 10/20→19/20、ECS 10/20→17/20)。

**「触觉表征 × 整合策略」设计空间(Fig. 3)——但不是全因子交叉**:
- 表征维度 **4 水平**:SigLIP / T3 / Sparsh / AnyTouch2(§4.3:同 token-level concat 接口下,AnyTouch2 均值最高 **68.7%** > Sparsh 64.7% > SigLIP 59.5% > T3 58.1%;逐任务数值只在雷达图 PNG,**未读取→未核**)。
- 整合维度 **5 水平**:① token-level concat ② feature-level modulation(FiLM)③ action-level conditioning ④ tactile-driven expert ⑤ tactile-guided refinement(§4.3 + Table 4:① concat 均值最高 68.7)。
- **⚠️ 方法学限制(原文自承 + 子 agent 核)**:两个维度是**两个独立单因子扫描,非 4×5 全因子**;Table 4 的 5 行里 **Representation 列不恒定**(①③⑤ 用 AnyTouch2、② 用 Sparsh、④ 用 T3+FTP-1)→ **仅 ①③⑤ 三行表征受控,交互效应无法估计**;原文措辞已收缩为「Among the AnyTouch2-based variants…」。Appendix C 另明示:「cross-family results compare complete policies rather than isolating the effect of a single training choice」(**跨家族比较不构成受控**)。

## ⚠️ 高风险锚点数字警告(原文内部不一致,子 agent 发现 + 主会话 curl 复验)

- **§1 Intro 声称**:仿真最强 VLA/WAM/VTLA = **51.5% / 53.3% / 61.2%**;真实 = **43.1% / 48.5% / 51.9%**。
- **但其自身 Table 2/3 与 §4.2 正文矛盾**:WAM 三个(FastWAM/Lingbot-VA/StarVLA-Cosmos)仿真均值最高仅 **37.4**(FastWAM)、真实仅 **29.0**(FastWAM);§4.2 正文亦写「FastWAM obtains 29.0%」「WAMs generally underperform the stronger VLA baselines」。
- **子 agent 多种重算(含按 §4.2「8 共享任务」口径)均无法调和出 53.3%/48.5%**。
- **判定(纪律)**:**「53.3%(仿真最强 WAM)」「48.5%(真实最强 WAM)」两个数字不得作为外部引用锚点**;若需引 WAM 最强值,以 **Table 2/3 的 37.4%(仿真,FastWAM)/ 29.0%(真实,FastWAM)** 为准。VLA(51.5/43.1)、VTLA(61.2/51.9)、OpenVTLA(68.7/54.6)与表格一致,可用。
- **这是判断(置信度中)**:53.3/48.5 更可能是 intro 残留/笔误而非未披露聚合口径,但**无法排除**存在文中未说明的聚合方式;定论需查 PDF 原文或项目页/后续版本。

## 透镜映射

- **透镜②(触觉与多模态传感)= 核心命中**:直接触及脆弱点「触觉边际价值无规模化受控对撞」——
  **「无」字已被本文证伪**(已有单骨干受控对撞),但该脆弱点须**改写为分层表述**(见透镜② v1.0.2 重审记录):
  已有 = 单骨干(π₀.₅)、11 仿真+8 真实任务规模的触觉开/关 + 表征 4 水平 + 整合 5 水平;
  仍缺 = ①多骨干复现 ②表征×整合全因子交叉与交互效应 ③多种子/方差/显著性 ④灵巧手与可变形物体 ⑤仿真评测集规模与主结果传感器披露。
- **G4(共享基建)前置门第 4 项**:本文**压缩了「可指认缺口」清单**——Table 1 已系统对比 7 个既有基准
  (CALVIN/LIBERO/ManiFeel/Tabero/UniVTAC/NeoSim/SoftVTBench)并主张自己六列全 ✓;
  **幸存缺口** = 多骨干 / 因子交叉 / 统计严谨 / **灵巧手本体**(作者 §5 自列 future work)/ 可变形·长时序 / 触觉仿真保真度 / 复现披露。
  **⚠️ 本文不能充当 G4「≥1 轮复现论证」的证据基础**(无种子/无方差/仿真评测集规模未披露/主结果传感器未披露/发布状态未声明 → 第三方当前不可复现)。

## A-018 联动(假设账本)

- A-018「视触操作缺乏跨仿真—真实统一基准 / 现有评测存在明确缺口」——**2026-10-09 全文级重审后:主干已证伪**。
  论文 abstract 逐字以该缺口立论(「there remains a lack of unified benchmarks … **To address this gap, we introduce OpenViTac**」)并交付成对 sim–real 基准。
  **剩余子缺口**(每条有原文出处):灵巧手/更多本体(§5 future work)、触觉仿真保真度(§5 自承 sim–real gap)、可变形·表面交互·长时序家务(§5 future work)、统计严谨性(无种子/方差/显著性)。

## 诚实边界

- **高置信(读到原文确证)**:全部著录、上表规模数字、+13.6/+13.5pp 受控对撞(已独立复算)、§5 灵巧手 future work、内部不一致 53.3/48.5 vs 37.4/29.0。
- **推断(原文未明说)**:Table 4 为纯仿真结果(据 OpenVTLA 行数值可由 Table 2 仿真分组平均复算得出,但 caption 未写 simulation);68.7 vs 64.7 的 4.0pp 可能落在运行间噪声内(**不断言不显著,只指出原文无方差信息可判**);多骨干泛化性未知。
- **未核 / 原文未提**:代码·数据发布状态与许可、仿真评测试次数、主结果传感器配置、Fig.4 逐任务数值(在 PNG 未读)、项目页内容、FTP-1 在 Table 4 是复跑还是引用(倾向复跑)、17 位作者逐人机构对应。
- **术语映射注**:原文**无「marginal value / 边际价值」字样**(0 命中),用的是「the contribution of tactile sensing」「Tactile benefits depend on how touch is incorporated」——**「触觉边际价值」是本所透镜② 的术语映射,非原文用词**。
