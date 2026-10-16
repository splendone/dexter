# 具身智能领域级图谱 · Phase 2 深挖:分支①(感知)+⑤(本体)+⑥(仿真基建)+⑦(评测)· v0.1

**性质**:领域级综述图谱的 **Phase 2 深挖件(剩余四支)**(黄色产物,草稿制)。
**版本**:v0.1;**未走会签前自查复核、未签发、不入 `final/`**。
**起草**:Dexter,2026-10-15(主会话汇总 + 2 路异路径子 agent 全文级深挖)。
**触发**:委托人 2026-10-15 指令"继续完成整理具身智能机器人更大视角研究路径图,参考
karpathy/autoresearch,自动续到积分不足"。**autoresearch 可迁移原则已采纳**:研究过程即
markdown 软件可迭代 / 单一可审查主文件 / 单一可比指标(→ 本件 §6 分支成熟度记分卡)/ 自主循环。
**承接**:`具身智能领域级图谱-v0.1.md`(骨干)+ `...Phase2-路线④⑤深挖-v0.1.md`(操作支)+
`...Phase2-分支②③b深挖-v0.1.md`(认知/运动)。**本件补齐剩余四支(①⑤⑥⑦),至此领域级
七分支全部深挖。** 证据纪律:venue 核不到标"未核实"绝不编造;**两处 venue 冲突已一手核定**;
数字带位置;ID 错配据实更正。

---

## §0 范围 + 分支成熟度记分卡(借 autoresearch"单一可比指标")

**记分卡 6 维**(每支 0-2 分:0=缺/1=骨干/2=深挖完成):venue 已核代表作数(≥6)/ 全文级锚点数(≥2)/
子分支结构 / 演进·分歧·开放问题 / 权威性检验 / 与操作支衔接。

| 分支 | venue 已核 | 全文锚点 | 子分支 | 演进分歧 | 权威检验 | 衔接 | 合计/12 | 状态 |
|---|---|---|---|---|---|---|---|---|
| ①感知 | 2(25 篇) | 2(FoundationPose/MT3栈) | 2(①a-e) | 2 | 0(待) | 2 | **10** | Phase 2 深挖✅ |
| ②认知 | 2 | 2(5 篇) | 2(②a-e) | 2 | 0(待) | 2 | **10** | Phase 2 深挖✅(前轮) |
| ③a操作 | 2(30+) | 2(15 篇) | 2(七路线) | 2 | 0(待) | 2 | **10** | 放大图谱✅ |
| ③b运动 | 2 | 2(3 篇) | 2(③b1-5) | 2 | 1(假设检验) | 1 | **10** | Phase 2 深挖✅(前轮) |
| ④学习范式 | 2 | 2 | 2(=操作七路线) | 2 | 0(待) | 2 | **10** | 经操作支✅ |
| ⑤本体 | 2(20+) | 1(HumanPlus) | 2(⑤a-e) | 2 | 0(待) | 2 | **9** | Phase 2 深挖✅ |
| ⑥仿真基建 | 2(21) | 1(3DGS) | 2(⑥a-e) | 2 | 1(venue 冲突定论) | 2 | **10** | Phase 2 深挖✅ |
| ⑦评测 | 2(12) | 2(3 篇) | 2(⑦a-e) | 2 | 0(待) | 2 | **10** | Phase 2 深挖✅ |

**七分支全部深挖完成(合计 79/96)**;**唯一全支共缺 = 权威性检验(≥3 处跨源定案)与会签前
自查复核**——这是签发 v1.0 前的最后两步(Round 2)。

---

## §1 分支① 感知(Perception)

**核心问题**:机器人如何从传感器理解世界(物体/场景/位姿/可供性/主动感知/多模态)?是操作支的上游。

### 1.1 子分支(①a-①e,venue 已核优先)

- **①a 3D 视觉/场景理解**:PointNet(1612.00593,**CVPR 2017**)、PointNet++(1706.02413,**NeurIPS 2017**)、
  3DSSG(2004.03967,**CVPR 2020**,语义场景图)、Hydra(2201.13360,**RSS 2022**,实时分层 3D 场景图)、
  ConceptGraphs(2309.16650,**ICRA 2024**,开放词汇图,批 per-point 特征图不 scale)、NLMap/OVS(2209.09874,**ICRA 2023**)。
- **①b 位姿估计(操作支真正上游)**:DPOD(1902.11020,**ICCV 2019**)、GDR-Net(**CVPR 2021**,
  DOI 10.1109/cvpr46437.2021.01634,**无 arXiv 预印本**;⚠️ 任务给的 2102.12149 是错配)、
  MegaPose(2212.06870,**CoRL 2022**)、**FoundationPose(2312.08344,CVPR 2024,全文卡见 §1.2)**、
  SAM-6D(2311.15707,**CVPR 2024**)。
- **①c 可供性(affordance)**:Gibson(1979 专著)、Aksoy(**IJRR 2011**)、AffordanceNet(1709.07326,**ICRA 2018**)、
  3D AffordanceNet(2103.16397,**CVPR 2021**,23k shapes/18 affordance 类)、Where2Act(2101.02692,**ICCV 2021**)、
  VRB(2304.08488,**CVPR 2023**,人类视频学 where&how 接 4 种学习范式)、BusyBox(2602.05441,预印本,物理基准)。
- **①d 主动/交互感知**:Bajcsy Active Perception(**Proc. IEEE 1988**)、Revisiting Active Perception
  (**Autonomous Robots 2017**)、Bohg Interactive Perception(**IEEE T-RO 2017**,DOI 10.1109/TRO.2017.2721939;
  IP 两收益:交互创造信号 + 传感×动作联合空间规律)。
- **①e 开放词汇/多模态(VLA 感知底座)**:CLIP(2103.00020,**ICML 2021**)、OWL-ViT(2205.06230,**ECCV 2022**)、
  SAM(2304.02643,**ICCV 2023**,>1B masks/11M images)、Grounding DINO(2303.05499,**ECCV 2024**,
  Crossref+MT3 ref[26] 双源)、XMem(2207.07115,**ECCV 2022**,comment+MT3 ref[6] 双源)。

### 1.2 全文级锚点卡

- **FoundationPose(2312.08344,NVIDIA,CVPR 2024,全文)**:统一 model-based(给 CAD)与 model-free
  (~16 张参考图);无 CAD 时神经隐式表示做新视角合成,下游位姿模块两设定同构。评测 5 数据集
  (LINEMOD/Occluded-LINEMOD/YCB-Video/T-LESS/YCBInEOAT)。**Table 1(YCB-Video model-free,16 ref,
  finetune-free)MEAN ADD/ADD-S:Ours 97.4/91.5 vs FS6D-DPM 88.4/42.1、PREDATOR 71.0/24.3**。
  **⚠️ 全文未给 FPS/运行时间(grep 无命中),引用不得补。**
- **MT3 感知栈逆向(2511.10110v1,全文)**:首帧 **Grounding DINO** 按任务描述模板解析物体名分割;
  后续帧 **XMem** 传播(处理遮挡);RGB-D→目标点云。alignment = **CoRL 2023 回归位姿
  ([46] = Vitiello, Dreczkowski & Johns,「One-Shot Imitation Learning: A Pose Estimation Perspective」,
  CoRL 2023,PMLR 229:943-970,arXiv:2310.12077 —— 原记『STRAP』系张冠李戴,已更正)+
  Open3D Generalised ICP([38]=Segal RSS 2009,DOI 10.15607/rss.2009.v.021)精修 + motion planning**。
  **⚠️ 结构性发现:MT3 不用 FoundationPose/MegaPose;其感知瓶颈被作者自指为
  位姿配准("pose estimator... predominantly focused on global geometry, occasionally misregistering
  small yet task-critical features",水壶壶嘴例),而非分割。**

  > **⚠️ 更正记录(2026-10-15 Round 2c 回流,依 `reports/drafts/领域级图谱-权威性检验记录-v0.1.md` §2 N7)**
  > 本节原把 MT3 的参考文献 **[46] 认定为 STRAP**,并加注 "PMLR v229 已核"。
  > **"PMLR v229 已核"这半句是对的,错的是论文身份**——v229 里那篇是 Vitiello 的 One-Shot IL,**不是 STRAP**。
  > 属 **ID/归属张冠李戴**(宪法「证据纪律」死刑级错误类型),**幸而在签发前捕获、未外流**(图谱系列均为 draft),
  > 已录 `honor.md`。**外部原始来源(三源一致,置信度高)**:
  > ①**MT3 v1 全文程序化检索**(`arxiv.org/html/2511.10110`,HTTP 200 / 383,679 B;去标签正文 4,941 行)——
  > **"Memmel" 命中 0 / "STRAP" 命中 0 / "Sub-Trajectory"·"sub-trajectory" 命中 0 / "Vitiello" 命中 2**;
  > ②**参考文献条目逐字**:"[46] P. Vitiello, K. Dreczkowski, and E. Johns (2023) One-Shot Imitation Learning:
  > A Pose Estimation Perspective . In Conference on Robot Learning , Cited by: §1 , §1 , §2.2.1";
  > 正文三处引用位置均指位姿估计/运动规划("For alignment, past research has explored using **pose estimation
  > [22, 46]**"、"we perform alignment through **pose estimation [22, 46]**"、"reaches this pose using
  > **motion planning [46]**");
  > ③**PMLR v229(CoRL 2023)官方论文集页** `proceedings.mlr.press/v229/vitiello23a.html`(HTTP 200)确证
  > 该文属 CoRL 2023 / **PMLR 229:943-970**。
  > **STRAP(= arXiv:2412.15182,ICLR 2025 Poster,子轨迹检索)在 MT3 v1 全文中零出现**;
  > STRAP 是**检索策略学习**,与"回归位姿"本就不相干——**这一不相干本身就是识别该错配的线索**。
  > **结构性结论不受影响、且更强**:MT3 位姿上游 = **CoRL 2023 位姿估计谱系(Vitiello et al.)+
  > Generalised ICP(Segal RSS 2009)**,**不是 FoundationPose/MegaPose 谱系**;原结论**指向正确,只是把论文名认错了**。
  > **更正后的谱系表述**:"MT3 对齐 = 引 [46](Vitiello et al., CoRL 2023:把单示范模仿形式化为
  > trajectory transfer + **unseen object pose estimation**)的位姿估计路线 + [38](Segal et al., RSS 2009)
  > Generalised ICP 精修 + motion planning"。**注:MT3 与 Vitiello et al. 同门**(Dreczkowski/Vitiello/Johns
  > 为共同作者;MT3 题名 "Learning a Thousand Tasks in a Day",Imperial College London Robot Learning Lab),
  > 引自家 CoRL 2023 前作做位姿对齐,**谱系自洽**。**根因**:子 agent 二手转述 + 主会话未回原文核 ref 编号。
  > **预防(硬规则)**:凡把"论文 A 的 ref[n] = 论文 B"写进产物,**必须回原文 grep 参考文献条目**,
  > 不得由子 agent 口述或凭"同门/同主题"推断。**⚠️ 深度边界(诚实)**:2310.12077 与 2412.15182 本轮
  > **只读 abs 页、未读全文**,技术内容与实验数字一律未核;N6/N7 只对"ID↔题名↔作者↔venue↔ref 归属"定案。

### 1.3 与操作支衔接(全文/DOI 级证据)

1. **分割→操作**:MT3 §4.1 明写 Grounding DINO+XMem;感知质量决定检索的"几何相似度"输入。
2. **位姿→alignment**:MT3 上游是**相对位姿回归 + ICP(CoRL 2023 谱系),不是 FoundationPose 谱系**
   → **"FoundationPose 作可替换但未被采用的候选"是明确研究缺口**(图谱新发现)。
3. **affordance→操作**:VRB 证明 affordance 可接 4 种学习范式,但 MT3 分解不含 affordance 层
   → **affordance 与"分解式免训练检索"的融合尚无人做**(缺口)。
4. **开放词汇→VLA**:Grounding DINO/CLIP/SAM 是 VLA 感知底座;LIBERO-Plus"模型 tend to ignore
   language instructions"说明**语言侧感知接地未真正生效**——感知支与评测支的共同裂缝。

### 1.4 演进/分歧/开放问题

- **演进**:几何原生(PointNet/++)→ 语义结构化(场景图 2020-22)→ 基础模型接管(2023-:CLIP/SAM/
  Grounding DINO 提供开放词汇+分割,位姿走 novel-object 免微调)。位姿子线:稠密对应(DPOD)→直接回归
  (GDR-Net)→render&compare(MegaPose)→统一基础模型(FoundationPose)→分割驱动(SAM-6D)。
- **分歧**:表示之争(per-point 特征图 vs 图结构,ConceptGraphs 批前者不 scale);assumption 之争
  (instance-level 高精度 vs novel-object 少假设);affordance 来源之争(仿真标注 vs 人类视频 vs 物理基准);
  主动感知是否必要(IP 综述主张交互创造信号 vs VLA 主流被动 RGB-D)。
- **开放问题**:小尺度任务关键特征的位姿配准(MT3 自陈失效);遮挡下长时程分割漂移(XMem 误差未评测);
  开放词汇误检如何进入策略;affordance"物理正确性"缺统一判据;主动感知在 VLA 时代几乎空白。

---

## §2 分支⑦ 评测/安全/泛化(横切;对撞层在此)

**核心问题**:怎么知道进步了?基准、鲁棒性、安全、泛化、可复现/可比性危机。

### 2.1 子分支(⑦a-⑦e,venue 已核优先)

- **⑦a 操作基准**:RLBench(1909.12271,**RA-L 2020**,100 任务)、CALVIN(2112.03227,**RA-L**)、
  ManiSkill(2107.14483,**NeurIPS 2021 D&B**;⚠️ 任务给的 2107.04125 错配)、ManiSkill2(2302.04659,**ICLR 2023**)、
  LIBERO(2306.03310,**NeurIPS 2023 D&B**,papers.nips.cc 核)、RoboCasa(2406.02523,**RSS 2024**)、
  RoboCasa365(2603.04356,**ICLR 2026**)、**SimplerEnv(2405.05941,CoRL 2024,PMLR v270;⚠️ 不是 NeurIPS)**、
  BiGym 2.0(2610.07594,预印本)。
- **⑦b 鲁棒性/泛化评测**:LIBERO-PRO(2510.03827,全文卡)、LIBERO-Plus(2510.13626,**7 扰动维,95%→<30%**)、
  LIBERO-VPro(2609.24350,12 类/96 settings/3,296 cases,~196k 仿真+200 真机)、RoboTwin-Phys(2609.26292,
  technical report,13 物理属性,>5,000 演示)、RoboTwin(2504.13059,**CVPR 2025 Highlight**)、AGNOSTOS(2505.15660,预印本)。
- **⑦c 安全评测**:SafeVLA-Bench(2606.00773,预印本;STL 不变式+VSI;**15 个 >90% 成功策略仍有 18-28%
  unsafe-episode;RoboCasa-365 成功 rollout 中 38-56% 违反至少一条 safety clause**)。
- **⑦d 可复现/对撞层**:RoboArena(2506.18123,全文卡)、vla-eval(2603.13966,全文卡)、RoboDojo(2607.04434,
  42 仿真+18 真机/5 维/30 策略)、RoboEval(2507.00435,**ICRA 2026**)、BiGym 2.0(2610.07594)。
- **⑦e 泛化理论/口径**:OXE(2310.08864,**ICRA 2024**,22 robots/21 机构/527 skills/160,266 tasks)、
  Generalization in Transfer Learning(**Robotica 2022**)。**四轴口径(新实例/新任务/新本体/新环境)可从已核基准反推**。

### 2.2 全文级锚点卡

- **RoboArena(2506.18123v2,venue = CoRL 2025 Oral,PMLR 305:336-364;作者数须带版本口径:
  arXiv v2 = 32 人 / PMLR v305 camera-ready = 26 人,含 Levine/Finn/Liang/Gupta/Daniilidis/Pertsch;全文)**:
  **委托人问的那句逐字核实**——摘要首句 "Comprehensive, unbiased, and comparable evaluation of modern
  generalist policies is **uniquely challenging**"。方案:不标准化任务/环境,众包 **double-blind 成对 A/B**,
  聚合偏好得全局排名;7 学术机构/DROID 平台/**612 场成对 A/B 比较(摘要作 "more than 600")**/7 generalist policies。
  **⚠️ 口径警告(2026-10-15 Round 2c 依 N2 由『两口径』升级为『三口径』)**:
  ①**612** = 成对 A/B 比较场次数(排名实验口径,§1 逐字 "a total of **612 pairwise comparisons**");
  ②摘要的 "**more than 600**" 是 **612 的取整表述**——**"600" 不是独立数字**,引用应写
  "612 场成对 A/B 比较(摘要作 >600)";
  ③**4,284** = 累计 policy rollouts(§1 "4284 evaluation episodes" / §5 "4284 policy rollouts" /
  Fig.5 图注 "4284 evaluation rollouts"),生成机制 = 每场 A/B 的 2 个策略 + 事后为 oracle 排名补评的
  "the remaining five policies"(§5.1 逐字 "asking evaluators to score the remaining five policies after
  each A/B evaluation on the same task. In total, we use 4284 evaluations to compute this oracle ranking")。
  **三者严禁混用**——4284 **不是**成对比较数,612/600 **不是**总 rollout 数。
  **⚠️ 算术闭合(本所推算,非原文直述;引用 4284=612×7 时须标『推算』)**:**612 × 7 policies = 4,284**,
  与原文两处措辞("the remaining five policies" + "7 generalist policies")完全自洽 → 可作"两口径同源"的硬证据。
  **图谱建议写法**:"RoboArena 在 7 所学术机构 / DROID 单本体上做众包 double-blind 成对评测,
  **612 场成对 A/B 比较(摘要作 >600)、累计 4,284 条 policy rollouts(=612×7,用于 oracle 排名)**"。
  7 策略实为 π0/PaliGemma 家族 DROID 变体(**非跨厂商明星对撞**;§5.1 逐字 "there are seven such policies,
  **based off PaliGemma [66] or π0 [41] base models**" = 2 个 π0 系 + 5 个 PaliGemma 系,池的准入标准是
  "all publicly available generalist DROID policies that have been shown to **work out of the box**");
  **排名算法(2026-10-15 Round 2c 依 N4 精确化,原写"排名用 EM(非 Bradley-Terry)"易被读成"完全弃用 BT",已改)**:
  **= 自家 "task-aware" 模型,即 BT 的任务感知扩展(含 Davidson 平局项),用近似 MLE 的 EM 算法拟合
  (clipped Newton 更新);BT/Elo 是论文用来对比并击败的基线,不是被弃用的框架**——
  §3.2 逐字 "**Extending BT** The Bradley-Terry model … **assumes that each pairwise comparison in the
  preference dataset takes place under identical conditions. This assumption is not satisfied in the setting
  of A/B robot policy evaluations**";拟合方法标题即 "An EM algorithm for approximate MLE";
  Appendix B 逐字 "We test instantiations of RoboArena with standard ranking algorithms, namely **Elo [61]
  and Bradley-Terry ("BT", [60])**, and our **task-aware ranking approach introduced in Section 3.2 ("TASK")**
  … our task-aware ranking approach leads to **more accurate rankings than both standard Elo computation and
  the conventional Bradley-Terry model**"、"again invoking the **Davidson extension of the Bradley-Terry model**"。
  → **不得写"用 EM 非 BT"**,应写"**BT 的任务感知扩展(含 Davidson 平局项)用 EM 拟合;BT/Elo 是被击败的对比基线**"。
  Fig.7"100 成对比较内收敛"(正文逐字 "RoboArena converges to high-quality rankings within just **100 pairwise
  comparisons**";**⚠️ 图中曲线数值本轮未读取,仅据正文文字**);自陈局限:仅 DROID 单本体
  (§4.2 逐字 "**the experimental evaluations in this paper have focused on the DROID platform [1]** …
  Future work should investigate how RoboArena can be extended to diverse robot embodiments"
  → **跨本体是论文自陈的 future work,不得读成作者未意识到**)。
  **⚠️ venue 定案(2026-10-15 Round 2 · N3,置信度高)**:**= CoRL 2025(The 9th Conference on Robot Learning)
  Oral,PMLR 305:336-364, 2025;已同行评审并正式发表**。两个独立外部源:①PMLR 官方论文集
  `proceedings.mlr.press/v305/atreya25a.html`(HTTP 200 / 19,660 B,逐字 "Proceedings of The 9th Conference
  on Robot Learning , **PMLR 305:336-364, 2025**")+ 卷号对照(v229=CoRL 2023 / v270=CoRL 2024 /
  **v305=CoRL 2025**);②OpenReview id=`cpmwi3Xwcr`(`venue: **CoRL 2025 Oral**`,
  venueid=`robot-learning.org/CoRL/2025/Conference`,invitations 含 `Submission1011/-/**Spotlight_And_Camera_Ready**`)。
  **反证式核查**:arXiv comment 仅 "Website: …"、**无 journal_ref**;Crossref `total-results:0` →
  **"Crossref 无 DOI" ≠ "未发表"**(PMLR/OpenReview 系多不注册 Crossref DOI;判例见 `lessons.md`)。
  **⚠️ 作者数口径护栏**:arXiv v2 = 32 人 / PMLR camera-ready = 26 人(v2 独有 7 人、PMLR 独有 1 人,
  32−7+1=26 ✓;"Edward Hu/Edward S. Hu"、"Roberto Martin-Martin/Roberto Martín-Martín" 为同人异写已排除)
  → **不得径写"32 位顶级作者"当既成事实**(该数字曾被 §2.3 用作"事实权威"论据),**引用须标版本口径**;
  差异成因(v2 扩列贡献者?)= **推断,置信度低,不作断言**。
  **定案全文见 `reports/drafts/领域级图谱-权威性检验记录-v0.1.md` §2 N2/N3/N4;骨干图谱 §8.5 表 #7/#9。**
- **vla-eval(2603.13966v3,机构 = AllenAI【据 leaderboard URL 推断,机构串未逐字核,置信度中】,
  venue = ICRA 2026 Workshop Poster【非主会,venueid 明含 `Workshop`】,全文)**:
  **委托人数字核实**——"aggregating **657 published
  results** across **17 benchmarks**";源自 1,704 篇论文;14 基准集成(3 个跨代码库完整复现)+ 6 model servers;
  client-server 解耦。
  **⚠️ 自陈局限(须一并引)**:"Leaderboard results are extracted from published papers, **not independently
  verified**"——**657 是文献聚合量,不是复现量**。
  **⚠️ 2026-10-15 Round 2c 依 N5 补五条口径(定案全文见 `reports/drafts/领域级图谱-权威性检验记录-v0.1.md` §2 N5;
  骨干图谱 §8.5 表 #10)**:
  ①**657 的抽取方式须一并披露**——原文逐字 "aggregating **657 results across 17 benchmarks and 509+
  configurations, sourced from 1,704 papers that cite at least one of the tracked benchmarks**"、
  "**An AI agent (Claude Code with Opus 4.6) reviewed 1,704 papers via MCP tool integrations (arXiv, Semantic
  Scholar, PDF reader) to extract and normalize results against these canonical protocols**" →
  **引用 657 必带三重 caveat**:文献聚合非复现 / **AI agent 自动抽取** / 作者自陈 not independently verified。
  复现验证范围**只有** "six VLA codebases × three simulation benchmarks"——**两个量级不可混用**。
  ②**"47×" 限 LIBERO,不得写成通用加速倍数**——原文 "up to **47× wall-clock speedup**, completing **2,000
  LIBERO episodes** in ~18 minutes"(~14h → ~18min);**CALVIN = 16×**(1,000 序列,16 shards,~33 min)、
  **SimplerEnv = 12×**(288 episodes,16 shards,~8.5 min)→ 引用须带 "**LIBERO / up to**" 标签。
  ③**"0%→59.7%" 必须带 −8.0 pp 尾巴**——原文逐字 "Reimplementing the necessary patches brought **GR00T on
  SimplerEnv (Google Robot) from 0% to 59.7%, with a −8.0 pp gap to the reported score remaining**"
  (表格作 "59.7 ( −8.0) ‡")→ **修好暗参数后仍未追平已发表分数**;只写"0%→59.7%"会把未追平写成追平
  (**数字-结论错配高危型**)。另:"GR00T expects end-effector pose as proprioceptive input, but this field
  exists only in an internal simulator fork, not in official SimplerEnv; **without it, scores drop from
  30–55% to 0%**"。
  ④**多口径不得混称(14 / 17 / 6 / 509+)**:**14** = harness 集成的仿真基准(Fig.1 图注逐字 "14 benchmarks
  (**3** with full cross-codebase reproduction validation) and six model servers")/ **17** = leaderboard 追踪的
  基准数 / **6** = model servers(CogACT、OpenVLA、OpenVLA-OFT、π0/π0-FAST、GR00T N1、X-VLA);
  另有 "**six** published VLA codebases"(复现验证对象:OpenVLA、π0.5、OpenVLA-OFT、GR00T N1.6、DB-CogACT、X-VLA)
  → **两个"six"名单不同,不得混称**;**509+ 在原文既作 "509+ configurations" 又作 "509+ models"(Fig.5 段)
  → 论文自身口径摇摆、正口径未定,引用只可写"509+(原文两处分别作 configurations 与 models,口径不一)"**。
  ⑤**venue = ICRA 2026 工作坊 "From Data to Decisions: VLA Pipelines for Real Robots" Poster,不是 ICRA 2026
  主会**——OpenReview id=`IpKQsHWaYS`(HTTP 200 / 9,761 B)`venue: ICRA 2026: From Data to Decisions Poster`、
  **venueid=`IEEE.org/ICRA/2026/Workshop/From_Data_to_Decisions`(明含 `Workshop`)**、bibtex booktitle
  "**ICRA 2026 Workshop**: From Data to Decisions: VLA Pipelines for Real Robots" → **不得径写"ICRA 2026"**,
  否则与 §2.1 ⑦d 的 RoboEval(2507.00435,**ICRA 2026 主会**)构成同标签不同层级混淆;工作坊论文通常非档案性
  论文集。**⚠️ 未排除项(诚实)**:本轮**未查 IEEE Xplore** → "是否另有 ICRA 2026 主会记录"未排除,
  若主会亦录用则应优先写主会。**反证式核查**:arXiv abs 页 `comment` 与 `journal_ref` **两字段均无**、
  Crossref `total-results:0` → **均不得据以推定"未发表"**(见 `lessons.md` Crossref 对称规则)。
  **⑥协议不可比性获原文逐字支撑(§2.4 衔接段①由中升高)**:"Evaluation protocols vary across papers:
  **SimplerEnv spans three incomparable robot configurations; CALVIN ABC→D and ABCD→D splits are not
  comparable; LIBERO papers report 4 or 5 suites.**"
  **⑦"暗参数"效应**:"single undocumented parameters can shift results by **tens of pp**";
  **⚠️ 分层护栏**——这是**独立于 LIBERO-PRO 的第二方证据**,但**层级不同**(参数敏感性 ≠ 训练集泄漏)
  → **引用须分层,不得合并成"两篇都证明泄漏"**(§6"评测污染/训练集泄漏独立证据仅 LIBERO-PRO 单方主张"
  据此补正)。arXiv v3 作者 7 人(Choi/Lee/Park/Kim/Krishna/Fox/Yu),主分类 cs.AI(单一)。
- **LIBERO-PRO(2510.03827v2,全文)**:标准 LIBERO >90% → 扰动下 **collapse to 0.0%**(根因 rote memorization);
  **⚠️ 内部口径不一**:摘要/§4.1 写**四个正交维度**,但 Figure 6 图注写 "five perturbation types"
  (task 不参与自由组合)→ 引用须说明"4 维 + task 作第 5 类不交叉";π0.5 在 libero-goal 位置扰动 0.38,
  OpenVLA 与 π0 均 0("differences masked by standard benchmark scores")。
  **⚠️ 2026-10-15 Round 2c 依 N1 细化(定案全文见检验记录 §2 N1;骨干图谱 §8.5 表 #6;
  `knowledge/maps/benchmark-libero-pro.md` 核实记录)**:①**形式化记号自身即"声明四维、定义五算子"**——
  §4.1 写 `k∈{O,R,L,E}`(四个)却紧接枚举出第五算子 "Task perturbation ( `k=T` ) modifies the target object
  or action while remaining within the training distribution. The perturbed task is `T^(T)=(l,e,G^(T))`"
  → **`k=T` 是论文正式定义的算子(带自己的公式),不是图注口误**;Figure 6 图注逐字 "To ensure feasibility,
  **task perturbations are excluded from cross-type combinations**",§4.3 逐字 "To avoid infeasible
  combinations, **task-level perturbations are excluded from cross-type compositions**";
  ②**"四维"的具体命名在论文内有四种措辞**(摘要 "manipulated objects / initial states / task instructions /
  environments";§4.1 "object attributes / initial spatial configurations / task instructions / environments";
  §5.1 "object properties / initial positions / task instructions(covering both semantic and structural
  variations)/ environments"——**把 task 折进 instruction 维**;§5.2 "objects / goals / spatial configurations /
  task sets")→ **论文未声明哪一组是权威口径,引用必须带脚注说明命名不统一**。
  **不得径写"五维正交"**(与摘要及 `k∈{O,R,L,E}` 冲突),**也不得径写"仅四维、无 task 扰动"**。
  **⚠️ 横向对比护栏**:LIBERO-PRO(4+1)/ LIBERO-Plus(7)/ LIBERO-VPro(12 类)**各家维度定义不同轴、
  不可直接比数**(§2.1 ⑦b 引用扰动协议处同此)。**全文仍无总任务数声明**(v2 HTML 全文再次确认)→
  维持"官方总数不可得",代码常量 300/220/520/280 **不得相加冒充总数**。

### 2.3 ⚠️ 结构性发现(图谱必须写明)

**对撞层成员发表状态分层——RoboArena 已正式发表(CoRL 2025 Oral,PMLR 305:336-364);vla-eval 仅
ICRA 2026 Workshop Poster(非主会);其余成员(RoboDojo/BiGym 2.0/LIBERO-PRO 等)venue 未逐一核实。**
这意味着:
①对撞层中**尚未核实发表状态的那部分**,其结论的**稳定性未经(可查证的)评审检验**;
②但 2025-06 后它们**已拿走顶会正式位、工作坊位与公共治理位**
(RoboArena **CoRL 2025 Oral** + 作者串含 Levine/Finn/Liang/Gupta/Daniilidis/Pertsch
【**作者数须带版本口径:arXiv v2 = 32 人 / PMLR v305 camera-ready = 26 人**,不得径写"32 位顶级作者"】、
vla-eval AllenAI【据 leaderboard URL 推断】+ ICRA 2026 工作坊位、RoboDojo 公共榜)——
**「发表滞后于事实权威」**(RoboArena 2025-06 上 arXiv、2025-11 出 v2、CoRL 2025 才正式发表;
vla-eval 至今只有工作坊位),这本身是评测基建领域的结构性特征(也是可复现性危机的一部分)
——**这是判断,置信度中**(全称断言已被证伪,收缩后的方向性论断只有 RoboArena/vla-eval 两例支撑)。

> **⚠️ 更正记录(2026-10-15 Round 2c 回流,依 `reports/drafts/领域级图谱-权威性检验记录-v0.1.md` §2 N3;
> 本节为实质性重写,原全称断言被外部原始来源证伪)**
> **本节原断言(现整体撤回)**——原文为全称否定句式,**此处按原意转述、不逐字复现**(以免该错误句式再被摘录引用):
> "整个'对撞层'(RoboArena / vla-eval / RoboDojo / BiGym 2.0 / LIBERO-PRO / LIBERO-Plus / SafeVLA-Bench /
> RoboTwin-Phys / AGNOSTOS)**目前没有一篇经同行评审正式发表,全部是预印本/技术报告**",
> 并据此推出 "**'事实上的权威'先于'正式发表'**"。
> **该全称断言已被证伪**:**RoboArena 确已同行评审并正式发表** = CoRL 2025(The 9th Conference on Robot
> Learning)**Oral**,**PMLR 305:336-364, 2025**。两个独立外部源:
> ①**PMLR 官方论文集** `proceedings.mlr.press/v305/atreya25a.html`(HTTP 200 / 19,660 B,逐字
> "Proceedings of The 9th Conference on Robot Learning , **PMLR 305:336-364, 2025**")+ 卷索引 `v305/`
> ("RoboArena" 1 命中、"Atreya" 3 命中)+ 卷号对照页(v229=CoRL 2023 / v270=CoRL 2024 / **v305=CoRL 2025**);
> ②**OpenReview** id=`cpmwi3Xwcr`(HTTP 200 / 25,699 B)`venue: **CoRL 2025 Oral**`,
> venueid=`robot-learning.org/CoRL/2025/Conference`,invitations 含
> `Submission1011/-/**Spotlight_And_Camera_Ready**`,bibtex `@inproceedings{atreya2025roboarena,…}`。
> **误判成因(两处"缺席证据"陷阱)**:RoboArena 的 **arXiv comment 仅 "Website: …"、无 journal_ref**,
> **Crossref `query.title=RoboArena&query.author=Atreya` 返回 `"total-results":0,"items":[]`** →
> **单查这两源必然维持"未发表"误判**。已录两条判例:**"arXiv comment ≠ venue"** 与其对称规则
> **"Crossref `total-results:0` ≠ 未发表"**(PMLR/OpenReview 系多不注册 Crossref DOI),见 `lessons.md`。
> **相应地,"'事实上的权威'先于'正式发表'"的强形式不成立,已收缩为「发表滞后于事实权威」(判断,置信度中)。**
> **⚠️ 未核实项(诚实,不得反向推定)**:N3 的证伪**只覆盖 RoboArena 一例**;其余成员
> (RoboDojo 2607.04434 / BiGym 2.0 2610.07594 / LIBERO-PRO 2510.03827 / LIBERO-Plus 2510.13626 /
> LIBERO-VPro 2609.24350 / SafeVLA-Bench 2606.00773 / RoboTwin-Phys 2609.26292 / AGNOSTOS 2505.15660)
> **本轮未逐一复核 venue,维持"未核实"**。**⚠️ 风险提示**:既然 RoboArena 已被证为
> "Crossref 0 记录 + arXiv 无 journal_ref 却已 CoRL 2025 Oral",**其余成员的"未核实"同样可能低估其发表状态**;
> **本节不得再恢复任何全称/多数表述**,若要作此类断言,**必须逐个走 OpenReview + 官方论文集**
> (PMLR 卷页 / roboticsproceedings.org / papers.nips.cc / IEEE Xplore)。**DBLP 本轮 4 次请求 3 次 HTTP 202
> (排队返回非 JSON)+ 1 次 HTTP 429(限流),未取得数据 → 交叉源缺位如实登记。**
> **另:骨干图谱 `具身智能领域级图谱-v0.1.md` §2「Phase 2 深挖更新」框内 (a) 项仍带同一全称断言**,
> **检验记录 §5 回流清单未列入本轮范围,标『待同步』**(分层表述以本节与骨干图谱 §8.5 表 #9 为准)。

### 2.4 与操作支衔接 + 演进/分歧/开放问题

- **衔接**:①操作支 SOTA 数字**必须带口径**(LIBERO 须注 PRO/Plus/VPro;SimplerEnv 须注三种 robot
  configuration 哪种,vla-eval 明写三者 incomparable);②MT3 类免训练检索策略**不在 RoboArena policy pool**
  (池内全 π0/PG 学习型),但 RoboArena 的 double-blind 成对协议**正好适配"检索库 vs 训练型策略"对撞**
  =委托人保留的对撞层的直接落点;③感知支与评测支裂缝同源(LIBERO-Plus"忽略语言"与 MT3"位姿忽略
  小特征"都是接地失败,一在语言侧一在几何侧);④安全维度与操作支脱钩(MT3 类真机方案无 STL/VSI 口径)。
- **演进**:任务量竞赛(RLBench 100→CALVIN→ManiSkill/LIBERO)→规模+真实性(RoboCasa/SimplerEnv)→
  **扰动/鲁棒性反转**(2025-26:LIBERO-PRO/Plus/VPro/RoboTwin-Phys/AGNOSTOS,共同结论"高分=记忆")→
  **对撞基建**(RoboArena 众包成对/vla-eval 统一 harness/RoboDojo sim+real/BiGym 2.0 把 coding agent 当被测/SafeVLA-Bench 拆安全)。
- **分歧**:标准化的价值(RoboArena 去中心成对 vs vla-eval 统一口径 vs RoboDojo 固定任务——三者对
  "什么叫可比"给互斥答案);仿真能否代真机;指标(成功率 vs 偏好胜率 vs STL 安全裕度 vs VSI);
  谁是被测者(BiGym 2.0 首次把 coding agent 与 VLA 同场)。
- **开放问题**:对撞层发表状态**分层**(RoboArena 已 CoRL 2025 Oral 正式发表;vla-eval 仅 ICRA 2026
  Workshop Poster;其余成员 venue **未逐一核实**,见 §2.3 更正记录)→ **未核实那部分的结论稳定性未知**;
  vla-eval 657 条 not independently verified;
  RoboArena 单本体+策略池同质使其"generalist 对撞"名不副实;LIBERO 系三扰动基准彼此不交叉验证;
  **缺一个把"新实例/新任务/新本体/新环境"四轴形式化的权威综述**(两次检索无对口条目=实质缺口)。

---

## §3 分支⑤ 本体/硬件(Embodiment/Hardware)

### 3.1 子分支(⑤a-⑤e,venue 已核优先)

- **⑤a 灵巧手**:LEAP Hand(2309.06440,**RSS 2023**,Crossref 10.15607/rss.2023.xix.089,低成本拟人学术手标杆)、
  HORA 在手旋转(2210.04887,**CoRL 2022**,仅仿真训零微调迁真机)、Rotating without Seeing(2303.10880,**RSS 2023**,
  纯触觉在手旋转)、DexGraspNet(2210.02697,**ICRA 2023**,仿真合成大规模灵巧抓取)、Dactyl(1808.00177,OpenAI 技术报告无 venue)、
  Rubik's ADR(1910.07113,OpenAI 技术报告,automatic domain randomization)。
- **⑤b 人形**:**HumanPlus(2406.10454,CoRL 2024,全文卡)**、Expressive WBC(2402.16796,**RSS 2024**)、
  OmniH2O(2406.08858,**CoRL 2024**,PMLR v270)、ASAP(2502.01143,**RSS 2025**)、HOVER(2410.21229,**ICRA 2025**)、
  H2O(2403.04436,IROS 2024 本轮未核)。产业(Tesla Optimus/Figure/Unitree H1·G1/Agility Digit)=业界报告无学术 venue。
- **⑤c 软体/柔顺/形态计算**:Rus&Tolley(**Nature 2015**,DOI 10.1038/nature14543,软体奠基综述)、
  Laschi(**Science Robotics 2016**,DOI 10.1126/scirobotics.aah3690)、Hogan 阻抗控制(**ASME JDSMC 1985**,
  DOI 10.1115/1.3140702,柔顺交互奠基)、No-brainer 形态计算(2407.16613,**SAB 2024**)。
- **⑤d 本体-控制协同设计**:Stackelberg PPO(2603.15388,**ICLR 2026**,Schmidhuber 组形态-控制双层联合优化)、
  Kriegman 可重构生物(**PNAS 2020**,DOI 10.1073/pnas.1910837117,演化式形态设计)。
- **⑤e 低成本/可复现本体(操作支硬件底座)**:ALOHA(2304.13705,**RSS 2023**)、Mobile ALOHA(2401.02117,**CoRL 2024**)、
  UMI(2402.10329,**RSS 2024**)、SO-ARM100/SO-100(LeRobot 开源硬件,无专门 venue 论文)。

### 3.2 全文级锚点卡 · HumanPlus(2406.10454,CoRL 2024)

自定义 **33-DoF/180cm** 人形,头部双 egocentric RGB;两层架构:低层 **Humanoid Shadowing Transformer(HST)**
(仿真 RL,AMASS 40 小时/11,000+ 动作序列;输出 19 维关节 setpoint→1000Hz PD,低层 50Hz)+
高层 **HIS**(egocentric 视觉监督 BC);数据闭环:单 RGB 估人体姿态→重定向→shadowing 遥操→克隆。
结果:穿鞋/起立/卸货/叠卫衣/打字等 **60-100% 成功率,≤40 demonstrations**。**意义**:正面回应人形
morphology+actuation gap,把"人类数据→人形"全栈打通;是 ⑤b 学术锚点,又跨 ⑥(shadowing 即数据管线)。

### 3.3 与操作支衔接 + 演进/分歧/开放问题

- **衔接(⑤→③a 路线④缺口③)**:**本体差异=跨本体迁移难题的根源**(DoF/运动学/末端[夹爪 vs 多指手]/
  相机位/底盘移动性各异);OXE/RT-X 证明跨本体正迁移可行但**不均衡**(夹爪数据主导、灵巧手数据稀缺);
  HumanPlus 的 shadowing+retargeting 是"人→人形 morphology gap"的一种解;**灵巧手↔夹爪迁移仍是缺口③核心**。
- **演进**:专用手(Shadow/Allegro)→低成本开源手(LEAP)→触觉在手操作(Rotating/HORA);人形从运动模仿
  (Expressive/H2O)→全栈人类数据系统(HumanPlus/OmniH2O)→敏捷-真实物理对齐(ASAP)。
- **分歧**:形态计算/软体(⑤c⑤d,"身体替控制减负")vs 刚性+大模型控制(规模+RL 硬扛);人形端到端
  shadowing(HumanPlus)vs 分层全身控制(HOVER/ASAP)。
- **开放问题**:灵巧手触觉-视觉融合的真实增益比?协同设计能否规模化(现多为演化/双层 PPO 小规模验证)?
  低成本本体的精度-复现权衡?

---

## §4 分支⑥ 仿真/数据基建(Sim/Data Infrastructure)

### 4.1 子分支(⑥a-⑥e,venue 已核优先)

- **⑥a 物理仿真器**:MuJoCo(**IROS 2012**,DOI 10.1109/IROS.2012.6386109)、**Isaac Gym(2108.10470,
  NeurIPS 2021 D&B,已核定见 §5)**、SAPIEN(2003.08515,**CVPR 2020**)、ManiSkill2(2302.04659,**ICLR 2023**)、
  Orbit/Isaac Lab(2301.04195,**RA-L 2023**,DOI 10.1109/LRA.2023.3270034)。ManiSkill3(2410.00425,venue 未核)、
  Genesis/PyBullet(开源无论文)。
- **⑥b 神经渲染/3DGS real2sim**:**3DGS(2308.04079,SIGGRAPH 2023=ACM TOG 42(4),全文卡)**、NeRF(2003.08934,
  **ECCV 2020 oral**)、Dex-NeRF(2110.14217,**CoRL 2021**)、NeRF2Real(2210.04932,**ICRA 2023**;⚠️ 非 ICLR)、
  D-REX(2603.01151,**ICLR 2026 Poster**)、ArtGS(2507.02600,**IROS 2025**)、SplatSim(2409.10161,**ICRA 2025**)。
- **⑥c 合成数据/数字孪生(操作支路线②整支在此)**:RoboCasa(2406.02523,**RSS 2024**)、MimicGen(2310.17596,
  **CoRL 2023**,~200 演示→50K+/18 任务)、GenSim(2310.01361,**ICLR 2024**,LLM 生成仿真任务)、ZeroBot(2609.34010,
  **RA-L 2026**)。DEXTERA(2609.21045,venue 未核)、RialTo(2403.03949,**不在 CoRL 2024 PMLR v270**,venue 未核)。
- **⑥d 数据集基建**:OXE/RT-X(2310.08864,**ICRA 2024**,60 数据集/22 本体/100万+轨迹)、BridgeData V2(2308.12952,
  **CoRL 2023**,60,096 轨迹/24 环境)、DROID(2403.12945,**RSS 2024**,操作支已核/本轮未独立复核[中])、
  AgiBot World(2503.06669,venue 未核,100万+轨迹/217 任务)。
- **⑥e sim2real gap**:Domain Randomization(1703.06907,**IROS 2017**,Crossref 确证录用[arXiv comment 仅"submitted"])、
  Sim2Real 综述(2009.13303,**SSCI 2020**)、RMA(2107.04034,**RSS 2021**)、Closing Sim-to-Real Loop(1810.05687,**ICRA 2019**)。

### 4.2 全文级锚点卡 · 3DGS(2308.04079,SIGGRAPH 2023)

显式各向异性 3D 高斯(稀疏 SfM 点初始化)+ tile-based 可微 splatting 光栅化;**1080p 实时 ≥30fps** 新视角合成,
质量 equals Mip-NeRF360(SOTA);训练 ~51min 达 SOTA,物体场景 2-4min。**意义**:⑥b 渲染基石——把真实
场景/物体变成**可微、实时、可与物理结合**的高斯表示;实时性让"渲染-in-the-loop 的 sim2real"可行
(Dex-NeRF/NeRF2Real/SplatSim/ArtGS/D-REX 皆建于 NeRF/3DGS 谱系)。

### 4.3 与操作支衔接 + 演进/分歧/开放问题

- **衔接(⑥→③a/④)**:操作支路线②(合成)整支住 ⑥c;⑥b real2sim 是"采集贵→仿真造"的关键杠杆;
  **仿真保真度(接触/形变/触觉)是操作数据瓶颈能否靠合成化解的约束**——运动支已用 ⑥a GPU 并行+⑥e DR
  解决数据瓶颈,操作支因接触富集 sim2real gap 更大(=§3 数据瓶颈分支特异的物理根源,承前轮假设检验修正)。
- **演进**:CPU 物理(MuJoCo)→GPU 并行(Isaac Gym)→统一框架(Orbit/ManiSkill);渲染 NeRF→3DGS→
  real2sim2real 闭环;数据从单机构→跨本体聚合(OXE/DROID/AgiBot)→合成扩增(MimicGen/RoboCasa/GenSim)。
- **分歧**:真机数据规模(OXE/DROID)vs 仿真合成(RoboCasa/MimicGen/ZeroBot);real2sim 渲染保真(3DGS)
  能否补上**接触/形变/触觉**的物理保真缺口。
- **开放问题**:接触富集操作 sim2real 为何远难于运动;合成数据对操作的真实增益边界;数字孪生物理参数标定成本。

---

## §5 venue 冲突定论 + ID 更正 + "arXiv comment≠venue" 教训

### 5.1 两处 venue 冲突(一手核定,高置信)

1. **Isaac Gym(2108.10470)= NeurIPS 2021 Datasets & Benchmarks Track(Round 2)。定论:已核实(高)。**
   依据:① nips.cc 官方《NeurIPS 2021 D&B Accepted Papers》列表含该文(作者 Makoviychuk...State 全匹配);
   ② OpenReview id=`fgFBtYgJQX_`,venueid=`NeurIPS.cc/2021/Track/Datasets_and_Benchmarks/Round2`;
   ③ ACM 论文 ref[9] 引作 "NeurIPS Track on Datasets and Benchmarks, 2021"。
   **先前"未核实/Crossref 误配"结论错在只查 arXiv**(comment 仅 "tech report on isaac-gym"、无 journal_ref/DOI)。
2. **HumanPlus(2406.10454)= CoRL 2024。定论:已核实(高)。**
   依据:① PMLR v270(CoRL 2024 Munich)官方论文集含该文,ID `fu25a`,pp.2828-2844;
   ② 作者站标 "Best Paper Award Finalist (top 6) at CoRL 2024"。arXiv comment 仅 "project website" 故单查 arXiv 会误判。

### 5.2 ⚠️ 可复用教训(录 lessons):**arXiv comment ≠ venue**

NeurIPS D&B / CoRL 等录用信息**常不在 arXiv comment/journal_ref**(尤其 D&B track、camera-ready 滞后);
**不能以 arXiv 无 journal_ref 推定"未核实"**,须查官方论文集(nips.cc / PMLR / proceedings.mlr.press /
roboticsproceedings.org / OpenReview)。本轮 Isaac Gym/HumanPlus 两冲突皆因"只查 arXiv"误判,经官方论文集一手核定。

### 5.3 ID 更正(子 agent 核出,防误引)

- GDR-Net:任务给的 2102.12149 错配(实为 Hinglish 情感分析);正确 = CVPR 2021,DOI 10.1109/cvpr46437.2021.01634,**无 arXiv 预印本**。
- **STRAP(子轨迹检索)= arXiv:2412.15182,venue = ICLR 2025 Poster**(2026-10-15 Round 2c 依 **N6** 定案并
  澄清原表述)。原写 "STRAP(子轨迹检索,**非 MT3 同门 STRAP**):= 2412.15182,**负向核实不在 CoRL 2024**
  (PMLR v270 全文检索无 'Memmel'/'Sub-Trajectory')" —— **"非 MT3 同门 STRAP"这句措辞易生误解,现澄清**:
  **MT3 的上游参考文献 [46] 是 Vitiello et al.(arXiv:2310.12077,CoRL 2023,位姿估计),它与 STRAP 是两篇
  不同的论文;2412.15182 才是真正的 STRAP(Memmel/Berg/Chen/Gupta/Francis,子轨迹检索)。**
  原"负向核实不在 CoRL 2024"**结论正确且现已得到解释**:STRAP 在 CoRL 2024 **只有工作坊位、不在主会论文集**
  (OpenReview 另有 id=`EWfN9upi72` **CoRL 2024 Workshop MRM-D Poster** 与 id=`MXNoOqBNLZ`
  **CoRL-X-Embodiment-WS 2024 Poster**),故 PMLR v270 检索为负是**预期结果,不是"未发表"**。详见下方 N6/N7 两条。
- ManiSkill:任务给的 2107.04125 错配(公共卫生运输算法);正确 = 2107.14483(NeurIPS 2021 D&B)。
- NeRF2Real = **ICRA 2023**(非 ICLR 2023,易记错)。
- 其他错配(子 agent 已校正):2309.10902=VALID 非 LEAP;1808.00032=宇宙学非 Dactyl;2304.10880=Med-Tuning 非 Rotating。

**⚠️ 2026-10-15 Round 2c 追加两条(依 `reports/drafts/领域级图谱-权威性检验记录-v0.1.md` §2 N6 / N7;
骨干图谱 §8.5 表 #11/#12;由主会话 `curl` 实抓外部原始来源核定,非子 agent 转述)**:

- **N6 · STRAP ID 冲突定案:STRAP(子轨迹检索)= 2412.15182,venue = ICLR 2025 Poster;2310.12077 不是 STRAP。**
  ①**STRAP("STRAP: Robot Sub-Trajectory Retrieval for Augmented Policy Learning",作者 Marius Memmel,
  Jacob Berg, Bingqing Chen, Abhishek Gupta, Jonathan Francis)= arXiv:2412.15182**;**主 venue = ICLR 2025 Poster**
  (The Thirteenth ICLR;OpenReview id=`4VHiptx7xe`,`venue: ICLR 2025 Poster`,venueid=`ICLR.cc/2025/Conference`,
  invitations 含 `Submission11830/-/**Camera_Ready_Revision**` = 强录用信号,bibtex
  `@inproceedings{memmel2025strap,…}`);**另有两个 CoRL 2024 工作坊 Poster**(MRM-D / X-Embodiment,**均非主会**)。
  **"RSS 2024"这一说法本轮无任何外部来源支持 → 判为误记,不采用**;结论应表述为
  "**已确证 ICLR 2025 Poster;RSS 2024 之说无源**",而非"STRAP 只在 ICLR 2025"(本轮**未穷尽** RSS 2025/2026
  与 ICRA 各年)。②**2310.12077 = "One-Shot Imitation Learning: A Pose Estimation Perspective"
  (Pietro Vitiello, Kamil Dreczkowski, Edward Johns),CoRL 2023,PMLR 229:943-970 —— 它不是 STRAP**;
  把它记作 STRAP 属 **ID 张冠李戴**(该文摘要主题为 "imitation learning … formulated as a combination of
  trajectory transfer and **unseen object pose estimation**",全文/摘要亦无 "sub-trajectory retrieval" 主张)。
  ③**图谱引用规则**:谈"子轨迹检索 / 部署时检索(test-time retrieval)"引 **2412.15182(ICLR 2025 Poster)**;
  谈"单示范模仿 + 未见物体位姿估计"引 **2310.12077(CoRL 2023)**;**两者不可互换、不可共用"STRAP"标签**。
  **外部来源**:`arxiv.org/abs/2310.12077`(HTTP 200 / 40,295 B)+ `arxiv.org/abs/2412.15182`(HTTP 200 /
  44,433 B)+ **PMLR v229 官方页** `vitiello23a.html`("PMLR 229:943-970")+ **OpenReview** `term=STRAP`
  (HTTP 200 / 362,978 B,count=139,三条同作者串记录);**反证式核查** Crossref
  `query.title=STRAP&query.author=Memmel` = `total-results:0`(ICLR/OpenReview 系不注册 Crossref DOI,
  **再次印证"Crossref 0 记录 ≠ 未发表"**,判例见 `lessons.md`)。**⚠️ 深度边界(诚实)**:两篇本轮**只读 abs 页、
  未读全文** → 技术内容与实验数字一律未核;N6 只对"ID↔题名↔作者↔venue"定案,**不对其结论定案**。**置信度高**。
- **N7 · ⚠️ MT3(2511.10110v1)ref [46] 归属更正:是 Vitiello et al.(CoRL 2023),不是 STRAP
  (张冠李戴,死刑级错误类型;签发前捕获、未外流,已录 `honor.md`)。**
  ①**[46] = Vitiello, Dreczkowski & Johns (2023) "One-Shot Imitation Learning: A Pose Estimation Perspective",
  CoRL 2023,PMLR 229:943-970 = arXiv:2310.12077**;②**STRAP(2412.15182)在 MT3 v1 全文中零出现**
  → 图谱 §1.2 原把 [46] 写成 STRAP 属 **ID/归属张冠李戴**,已就地更正(见 §1.2 更正记录);
  ③**结构性结论仍成立且更强**——MT3 位姿上游 = **CoRL 2023 位姿估计谱系(Vitiello et al.)+ Generalised ICP
  (Segal RSS 2009)**,**不是 FoundationPose/MegaPose 谱系**;原结论**指向正确,只是把论文名认错了**;
  ④**外部来源**:`arxiv.org/html/2511.10110`(MT3 v1 全文,HTTP 200 / 383,679 B;去标签正文 4,941 行)
  程序化检索 **"Memmel" 0 / "STRAP" 0 / "Sub-Trajectory"·"sub-trajectory" 0 / "Vitiello" 2**;
  参考文献条目逐字 "**[46] P. Vitiello, K. Dreczkowski, and E. Johns (2023) One-Shot Imitation Learning:
  A Pose Estimation Perspective . In Conference on Robot Learning**";正文三处引用位置均指位姿估计/运动规划;
  + **PMLR v229 官方页**确证(**三源一致**)。**预防(硬规则)**:凡把"论文 A 的 ref[n] = 论文 B"写进产物,
  **必须回原文 grep 参考文献条目**,不得由子 agent 口述或凭"同门/同主题"推断。**置信度高**。

---

## §6 残余不确定性与诚实标注

- **全文级 vs 摘要级**:分支①读全文 2 篇(FoundationPose/MT3 栈)、⑦读全文 3 篇(RoboArena/vla-eval/LIBERO-PRO)、
  ⑤读全文 1 篇(HumanPlus)、⑥读全文 1 篇(3DGS);**其余均摘要级/metadata 级**,数字取自摘要或 comment,未与正文表格交叉验证。
- **venue 已核实收敛(2026-10-15 Round 2c 依检验记录 §4 更新;原"未核实"项中三项已定案,不再列此)**:
  ①**STRAP 2412.15182 = ICLR 2025 Poster**(另有两个 CoRL 2024 工作坊 Poster;原列于分支① 未核实 4 项 →
  **现剩 3 项**;详见 §5.3 **N6**);②**RoboArena 2506.18123 = CoRL 2025 Oral,PMLR 305:336-364**
  (详见 §2.2 卡与 §2.3 更正记录、**N3**);③**vla-eval 2603.13966 = ICRA 2026 工作坊
  "From Data to Decisions: VLA Pipelines for Real Robots" Poster,非主会**(详见 §2.2 卡、**N5**)。
  **⚠️ 三项均系"arXiv 无 journal_ref + Crossref `total-results:0` 却已录用"** → 判例见 `lessons.md`
  ("arXiv comment ≠ venue" + 对称规则 "Crossref `total-results:0` ≠ 未发表")。
- **venue 仍未核实(如实标,未编造)**:分支① **3 项**(BusyBox/Active Perception Disambiguation/Gibson 初版);
  分支⑦ **对撞层其余 8 项**(RoboDojo 2607.04434 / BiGym 2.0 2610.07594 / LIBERO-PRO 2510.03827 /
  LIBERO-Plus 2510.13626 / LIBERO-VPro 2609.24350 / SafeVLA-Bench 2606.00773 / RoboTwin-Phys 2609.26292 /
  AGNOSTOS 2505.15660)——**⚠️ 原写"13 项(整个对撞层全部预印本——结构性事实,见 §2.3)"已被 N3 证伪并撤回:
  RoboArena 已 CoRL 2025 Oral 正式发表、vla-eval 已有工作坊位,故"全部预印本"不成立;其余 8 项本轮
  未逐一复核 venue,维持"未核实",且"未核实"同样可能低估其发表状态(RoboArena 即为反例),
  复核须逐个走 OpenReview + 官方论文集**;
  分支⑤(H2O/Dactyl/Rubik's/产业人形/SO-ARM100);分支⑥(ManiSkill3/AgiBot/DEXTERA/RialTo/Genesis/PyBullet)。
  **⚠️ 交叉源深度(诚实)**:N3/N5/N6 的 venue 定案**只有 1-2 个外部源**(N3 = PMLR + OpenReview 两源;
  N5 = OpenReview 单源 + arXiv 自述;N6 = OpenReview 三条独立记录 + arXiv abs + PMLR v229 旁证),
  **均未达"三源一致"**;**DBLP 本轮 4 次请求 3 次 HTTP 202(排队返回非 JSON)+ 1 次 HTTP 429(限流),
  未取得任何数据 → 交叉源缺位**;**未查 IEEE Xplore**(故 vla-eval 是否另有 ICRA 2026 主会记录未排除)、
  **未穷尽 RSS 2025/2026 与 ICRA 各年**(故 STRAP 结论只作"已确证 ICLR 2025 Poster;RSS 2024 之说无源")。
  详见检验记录 §4.2/§4.4。
- **中置信(单源/二手)**:OXE ICRA 2024(DOI 经二手+操作支已核)、DROID RSS 2024(操作支已核,本轮未独立复核);
  **新增(Round 2c)**:vla-eval 机构 = AllenAI(**据 leaderboard URL `allenai.github.io` 间接推断,abs/HTML
  作者块机构串未逐字核到**,置信度中)、RoboArena 作者数 32/26 差异成因(**推断,置信度低,不作断言**)、
  RoboArena "4284 = 612×7"(**本所推算,非原文直述**)、vla-eval "509+"(**原文两处分别作 configurations 与
  models,正口径未定**)、LIBERO-PRO "四维"命名(**四种措辞并存,论文未声明哪一组为权威**)、
  "发表滞后于事实权威"(**判断,置信度中**,仅 RoboArena/vla-eval 两例支撑)。
- **可能漏查(子 agent 诚实标注)**:①b 2025-26 最新位姿(GenFlow/BundleSDF/event·visuo-tactile 位姿);①a NeRF/3DGS
  场景表示与语义 SLAM(Kimera/Voxblox);①c 语言驱动 affordance;①e SAM2/DINOv2;⑦ 导航/移动操作评测(Gibson/HM3D)、
  长程记忆专项评测、评测污染/训练集泄漏独立证据(**2026-10-15 Round 2c 依 N5 补正:原写"仅 LIBERO-PRO 单方主张"
  → 现有第二方证据:vla-eval 的"暗参数"效应(单一未记录参数使结果偏移 tens of pp;GR00T on SimplerEnv
  0%→59.7%,仍差 −8.0 pp)。但层级不同(参数敏感性 ≠ 训练集泄漏),引用须分层,不得合并成"两篇都证明泄漏"**);
  ⑤a Allegro/Shadow 原始硬件文献+GelSight 指尖;
  ⑤c 形态计算奠基(Pfeifer&Scheier/Paul 2006,书/老期刊未取 DOI);⑥a Brax/Warp/Drake;⑥b ManiGaussian/2025 real2sim 新作;⑥d RH20T/Ego4D。
- **本件未做**:权威性检验(**2026-10-15 Round 2 已完成**:`reports/drafts/领域级图谱-权威性检验记录-v0.1.md`
  新增定案 **7 处 N1-N7**,远超 ≥3,**全部引外部原始来源**,24 次 HTTP 200 实抓;并汇整此前 6 个具体分歧点 A-D;
  本件 §1.2 / §2.2 RoboArena / §2.2 vla-eval / §2.2 LIBERO-PRO / §2.3 / §5.3 / §6 已按检验记录 §5 回流清单更正)、
  **会签前自查复核仍未做** → **故 v0.1 仍不签发**。
  **签发前必查清单(检验记录 §4.4 末条)**:图谱系列其余数字锚点本轮**一律未外部复核**——
  RoboDojo 42+18/30 策略、BiGym 2.0 自报数 5-8 倍口径分裂、SafeVLA-Bench 18-28%/38-56%、
  LIBERO-Plus 95%→<30%、LIBERO-VPro 12 类/96 settings/3,296 cases;另 RoboArena Figure 6/7 曲线数值
  (PNG,未读取)、vla-eval 14 基准逐名、LIBERO-PRO Table 7(HTML v2 未展开)、各文 v1↔最新版数字差异
  (612/4284/作者数均为 v2 口径,v1 未核)。
  **原列候选定案现状**:Isaac Gym venue[已定 D1]、HumanPlus venue[已定 D2]、Domain Randomization IROS 2017
  [已定 D3]、DROID 84/86[已定 A]、OXE 21/34[已定 B]、LIBERO-Pro 4维vs5类[**已定 N1,细化**]、
  RoboArena 600vs4284[**已定 N2,升级为三口径**]、OpenViTac 53.3/48.5 vs Table 2/3[已定 C]。

---

## 署名链

- **起草**:Dexter(2026-10-15,主会话汇总 + 2 路异路径子 agent 全文级深挖)。
- **性质**:领域级综述图谱 **Phase 2 深挖件(剩余四支①⑤⑥⑦)**,黄色产物草稿。
- **状态**:**v0.1 草稿,未走会签前自查复核、未签发、不入 `final/`、不署名/不投稿/不发布/不对外**。
- **里程碑意义**:**至此领域级七分支(①②③a③b④⑤⑥⑦)全部深挖完成**(记分卡 79/96);
  剩余唯一全支共缺 = 权威性检验 + 会签前自查复核 → 合并签发 v1.0(Round 2)。
- **下一步**:① 权威性检验(≥3 处跨源定案);② 合并主文件(借 autoresearch"单一可审查主文件":
  把骨干图谱 + 三件 Phase 2 深挖[④⑤/②③b/①⑤⑥⑦]合并为一部权威领域级图谱);③ 会签前自查复核
  (独立子任务 + 外部交叉源)→ 签发 v1.0;④ venue 冲突定论(Isaac Gym/HumanPlus)+ ID 更正回流骨干图谱 §8。
- **复核**:______(待会签前自查复核)
- **签发**:______(未签发)
