# 具身智能领域级图谱 · Phase 2 深挖:分支②(认知/世界模型)+ 分支③b(运动)· v0.1

**性质**:领域级综述图谱的 **Phase 2 深挖件**(黄色产物,草稿制)。
**版本**:v0.1;**未走会签前自查复核、未签发、不入 `final/`**。
**起草**:Dexter,2026-10-14(主会话汇总 + 2 路异路径子 agent 全文级深挖 + 假设检验)。
**触发**:委托人 2026-10-14 指令"领域级 Phase 2:深挖分支②(认知/世界模型,与操作支
路线④⑤的 WAM/agentic 直接衔接)+ 分支③b(运动,验证'数据瓶颈分支特异'洞察)"。
**承接**:`reports/drafts/具身智能领域级图谱-v0.1.md`(Phase 1 骨干稿)——本件把骨干稿
§2 的分支②与③b 从"奠基锚点"深挖到**子分支 + 全文级锚点 + venue 核实 + 演进/分歧/开放问题**,
并对 §3 的"数据瓶颈分支特异"判断做**假设检验**(结论:部分成立,须修正,已回流 §3)。
**证据纪律**:两路子 agent 共**全文级精读 8 篇**(保留 `<math alttext>` 提取)、摘要级核实其余;
venue 核不到标"未核实",绝不编造;**假设检验平衡找支持+反驳证据,判定可推翻原判断**。

---

## §0 本件与骨干图谱的关系 + Phase 2 范围

- **骨干图谱(Phase 1)**:七分支各有 venue 已核奠基锚点;分支③a(操作)已有放大图谱
  (`领域科研路径图谱-v0.1.md` + `...Phase2-路线④⑤深挖-v0.1.md`)。
- **本件(Phase 2)**:深挖**分支②(认知/世界模型)与分支③b(运动)**(委托人指定);
  **其余分支(①感知/③a 操作[已有]/⑤本体/⑥仿真/⑦评测)的深挖排后续轮。**
- **两项核心增量**:① 分支② 的子分支结构 + **②→③a 的向下衔接**(世界模型→WAM 系→操作路线④;
  LLM 规划→agentic→操作路线⑤);② 分支③b 的**假设检验**——对骨干图谱 §3"数据瓶颈分支特异"
  判断做证据检验,**结论:部分成立、须修正**(详见 §2.5,已回流骨干图谱 §3)。

---

## §1 分支② 认知 / 世界模型 / 推理规划(深挖)

**核心问题**:机器人如何**预测行动后果、规划任务、推理、记忆**——具身智能的"大脑/认知"层。
与分支③(行动/控制,产生运动)相对:②是"想",③是"动"。

### 1.1 子分支结构(②a-②e)

#### ②a 世界模型 / 基于模型的 RL(预测行动后果,在"想象"中规划/训练)
- **核心命题**:学环境动力学模型,在想象/模拟中规划或训练策略以提样本效率。
- **代表作(venue 已核)**:
  - **World Models**(Ha & Schmidhuber,arXiv:1803.10122,**NeurIPS 2018**;⚠️ **题名/ID 陷阱**:
    1803.10122 是交互式预印本《World Models》,NeurIPS 正式版题名《Recurrent World Models
    Facilitate Policy Evolution》= arXiv:1809.01999,引用须注双题名/双 ID):三件套
    V(VAE 压帧成 latent z_t)+ M(MDN-RNN 预测 z_{t+1})+ C(小控制器,CMA-ES 进化训练);
    CarRacing 首个达 solve 阈值(900/100 trials,Sec3),VizDoom 全程梦中训练再迁回(~900 步,Sec4.3)。
  - **PETS**(Chua et al.,arXiv:1805.12114,**NeurIPS 2018**,comment 逐字 "NIPS 2018"):
    概率集成(PE,捕认知+偶然不确定性)+ 轨迹采样(TS)+ MPC/CEM 在线规划;
    half-cheetah 比 SAC 少 **8×**、比 PPO 少 **125×** 样本(摘要+Sec7.1)。
  - **Dreamer 系**:Dream to Control(arXiv:1912.01603,**ICLR 2020**,mlanthology+iclr.cc 核)、
    DreamerV2(arXiv:2010.02193,**ICLR 2021**,comment 逐字 "Published at ICLR 2021"——
    **由 Phase 1 的"低置信仅作者自述"升为 comment 实证**)、**DreamerV3**(arXiv:2301.04104,
    **Nature** 640:647-653,2025-04-02,DOI 10.1038/s41586-025-08744-2,⚠️ 官方题名
    《Mastering diverse control tasks through world models》):RSSM + symlog/two-hot/free bits
    鲁棒化,单配置跨 **150+** 任务,**首个从零采到 Minecraft 钻石**(摘要)。
  - **Model-based RL 综述**(Moerland et al.,*FnT in ML* 16:1-118,2023,DOI 10.1561/2200000086)。
- **演进/分歧**:显式重建+梦中训练(World Models)→ 不确定性集成+在线 MPC(PETS,不学策略)→
  潜想象+actor-critic(Dreamer)→ 离散表征+鲁棒化单配置(V2/V3)。分歧:**规划时建模**(PETS 在线 MPC)
  vs **想象中训策略**(Dreamer);重建式 vs 重建无关(JEPA/LeCun 一系,本轮未深挖)。

#### ②b VLA / VLM 通用认知大脑(把语言-视觉-推理-动作压进一个端到端模型)
- **代表作(venue 已核)**:**PaLM-E**(arXiv:2303.03378,**ICML 2023**,PMLR v202/driess23a;
  视觉+连续状态+文本交织的具身多模态 LM,PaLM-E-562B)、**RT-2**(arXiv:2307.15818,**CoRL 2023**,
  PMLR v229/OpenReview dddU8UlJPm;actions-as-text-tokens 共微调,6k 试验,涌现语义推理与 CoT,
  泛化 ~2× 于 RT-1/MOO、~6× 于其他,Sec4.1/H.1)、**π0**(arXiv:2410.24164,**RSS 2025**,comment 逐字)、
  **π0.5**(arXiv:2504.16054,**CoRL 2025[二手一致,置信度中]**;异构 co-training + 高层语义子任务预测,
  首次端到端在全新家庭做长程灵巧任务)。
- **演进/分歧**:传感器嵌入 LM(PaLM-E)→ 动作当 token 共微调(RT-2)→ flow/diffusion 头做
  高频连续控制(π0)→ co-training 开放世界泛化(π0.5)。分歧:**离散动作 token**(RT-2)vs
  **连续 flow 头**(π0)。

#### ②c LLM/VLM 任务规划与推理(高层分解/排序/常识,底层技能另给)
- **代表作(venue 已核)**:**SayCan**(arXiv:2204.01691,**CoRL 2022**,PMLR v205/ichter23a;
  LLM 提议 + 预训练技能 value function 做 affordance grounding)、**Inner Monologue**
  (arXiv:2207.05608,**CoRL 2022**,PMLR v205;闭环语言反馈重规划)、**Code as Policies**
  (arXiv:2209.07753,**ICRA 2023**,IEEE 10160591;LLM 写策略代码 LMP,HumanEval 39.8%)、
  **ProgPrompt**(arXiv:2209.11302,**ICRA 2023**,IEEE 10161317 + 期刊版 *Autonomous Robots* 2023
  DOI 10.1007/s10514-023-10135-3;program-like 规格,VirtualHome SOTA)。
- **演进/分歧**:LLM 提议+affordance 打分(SayCan)→ 闭环反馈重规划(Inner Monologue)→
  规划外化为可执行程序/代码(CaP/ProgPrompt)。分歧:**自然语言规划** vs **程序/代码外化**(与⑤交叠)。

#### ②d 记忆与状态跟踪(长程任务的跨时间记忆)
- **代表作(venue 未核实,预印本)**:**ReCAT**(arXiv:2609.35200;指令条件编码器 + Mamba-2 循环记忆 +
  因果注意力 + flow-matching 解码;LIBERO 95.3%/RMBench 62.4%,真机三任务 66.7% vs 短史基线 8.3%;
  **反直觉发现:机器人记忆规律≠高效序列建模——additive 更新宜计数/计时、delta-rule 宜空间回忆**)、
  **ADM-Planner**(arXiv:2609.29212;注意力增强动态记忆分离 workspace 知识与 object 状态 + 有界检索 +
  失效即重规划;1500 sim 集 14-container 噪声动态 100% vs 静态 62%,上下文代理 -95.8%)。
- **分歧**:**隐式循环记忆**(ReCAT 压进 policy)vs **显式结构化记忆**(ADM-Planner 外化状态+检索)。

#### ②e 操作支世界模型落地(WAM 系;②a 向 ③a 的延伸)
- **核心命题**:把②a"预测行动后果"落到操作——video/tactile world model 同时预测未来并生成动作
  (World Action Models)。
- **代表作(venue 未核实,预印本)**:**VT-WAM**(arXiv:2607.02503;非对称 MoT 注意力 + 接触门控 AVTAG;
  6 真机接触任务 71.67%,超 Fast-WAM 26.67%/OmniVTLA 35.84%)、**TacWAM**(arXiv:2607.28391;
  SAF 触觉编码器 + 锚引导三模态注意力,让未来触觉监督训练但不被动作支直读;4 真机任务 75.0%、+37.5pp)、
  **DexTacWAM**(arXiv:2609.24976;见 §1.2 全文卡)、**Rolling-WAM**(arXiv:2609.30247,comment "Under review";
  滚动想象:错位噪声滑窗分布式联合去噪,稳态重规划 **4.5×** 加速)。
- **演进**:视觉 future WAM → **视触** future(VT/Tac/DexTacWAM 把力/形变/slip 纳入 world state)→
  推理加速(Rolling-WAM)。基线家族 FastWAM/OmniVTLA。

### 1.2 分支②全文级锚点卡(5 篇读全文)

- **World Models(1803.10122,NeurIPS 2018)**:机制见上。**自陈局限(Sec4.5「Cheating the World Model」
  + Sec7)**:agent 会发现**对抗策略**骗过 M(让怪物永不发射火球),梦中好、真环境败——因访问了模型
  错误(远离数据)的状态。**这是"长程 rollout 误差累积/模型被策略钻空子"的最早一手证据。**
- **PETS(1805.12114,NeurIPS 2018)**:概率集成捕认知不确定性 + 轨迹采样 + MPC/CEM;
  half-cheetah 比 SAC 少 8×、比 PPO 少 125× 样本;核心论点 = 用 uncertainty-aware 动力学
  弥合 model-based 样本效率与 model-free 渐近性能的 gap。
- **DreamerV3(2301.04104,Nature 2025)**:RSSM + symlog/two-hot/free bits(KL<1 nat≈1.44 bits 裁剪,
  防表征塌缩);单配置跨 150+ 任务,首个从零采到 Minecraft 钻石。
- **RT-2(2307.15818,CoRL 2023)**:co-fine-tune PaLI-X/PaLM-E 于机器人轨迹+互联网 VQA;动作表达为
  text token;6k 试验,泛化 ~2×/~6×,涌现 CoT(石头当锤、累的人给能量饮料)。
  **⚠️ 自陈局限(Sec5,②≠③ 的关键证据)**:"web 预训练只提升语义/视觉泛化,**机器人不获得任何
  新运动能力**,物理技能仍限于机器人数据分布,只是'以新方式部署旧技能'";大 VLA 实时推理算力成本高。
  **→ 这直接证明:②b 的"认知"无法打破③的"运动数据瓶颈"——VLA 的互联网知识只换语义泛化,
  不换新运动能力。这是数据瓶颈谱系链(领域级图谱 §1 L2)在 VLA 上的一手佐证。**
- **DexTacWAM(2609.24976,预印本,22 页)**:多指触觉编码器→指/位姿感知触觉压缩器(5:1)→
  注入视频扩散世界模型做联合视触世界建模→per-modality K/V 归一化动作专家;持续 vision-to-touch
  (冻结视觉 VAE、~100 demos/任务、4h 适配,Sec3.5)。**6 个接触富集灵巧任务(22-DoF 双臂)均 70.6
  vs 最强基线 38.0(Sec4.1);去掉触觉世界建模→四任务均 74.7 跌至 26.6(Sec4.2)——证明增益来自
  "把接触演化作为预测世界状态的一部分",非单纯触觉条件**。**Sec2.1 明确自归「World Models and WAMs」
  谱系**,定义 WAM = "预测行动条件未来 + 经学习潜动力学生成动作"。**自陈局限(Sec1)**:纯视觉 WAM
  "建模场景如何演化,但不建模隐藏物理交互状态如何演化",而接触富集操作成败取决于接触/slip/抓取稳定
  等相机只能部分观测的量。

### 1.3 分支② venue 核实汇总

**已核实**:World Models=NeurIPS 2018(⚠️ 双题名/双 ID:1803.10122 预印本 / 1809.01999 正式版);
PETS=NeurIPS 2018(comment);Dreamer=ICLR 2020(mlanthology+iclr.cc);DreamerV2=ICLR 2021(comment 逐字,
**由低置信升实证**);DreamerV3=Nature 2025(Crossref DOI,官方题名不同);Moerland 综述=FnT ML 2023(Crossref);
RT-2=CoRL 2023(mlanthology+OpenReview);π0=RSS 2025(comment);PaLM-E=ICML 2023(PMLR v202);
SayCan=CoRL 2022(PMLR v205);Inner Monologue=CoRL 2022(PMLR v205);Code as Policies=ICRA 2023(IEEE);
ProgPrompt=ICRA 2023(IEEE + 期刊版 Autonomous Robots)。
**未核实/仅预印本**:π0.5(CoRL 2025 仅二手一致,置信度中)、ReCAT、ADM-Planner、DexTacWAM、
VT-WAM、TacWAM、Rolling-WAM(comment "Under review")——2026 新 ID 经 arXiv API 确认标题/作者真实存在,非编造。

### 1.4 分支② 演进 / 分歧 / 开放问题

- **演进**:2018 ②a 奠基(World Models 梦中训练 + PETS 不确定性集成+MPC)→ 2020-21 ②a 成熟
  (Dreamer/V2 潜想象+actor-critic、离散表征)→ 2022 ②c LLM 规划兴起(SayCan/Inner Monologue/CaP/ProgPrompt,
  与⑤交叠)→ 2023 ②b VLA 通用大脑(PaLM-E/RT-2)+ ②a 单配置跨域(DreamerV3 arXiv)→ 2025 ②a 登 Nature、
  ②b 走向开放世界(π0/π0.5)→ 2025-26 ②a 向 ③a 操作支落地为 ②e WAM 系 + ②d 记忆专题化。
- **三种"认知"路线的分歧(核心)**:
  1. **世界模型(②a,显式预测)**:强=样本效率(PETS 8-125×)、可预演;弱=长程误差累积、
     **模型被策略钻空子**(World Models Sec4.5 对抗策略一手证据)。
  2. **VLA(②b,隐式端到端)**:强=继承互联网语义、涌现推理(RT-2 CoT);弱=认知黑箱不可单独推理、
     **RT-2 自陈 web 预训练不带来新运动(Sec5)——②b 的"认知"与③的"行动"仍受机器人数据分布锁死**、高算力。
  3. **agentic(②c/⑤,符号/程序外化)**:强=可组合/可读/可复用/闭环反馈;弱=**幻觉/可靠性**
     (ProgPrompt 为治"计划含不可行动作"提出 situated 约束;SayCan affordance grounding、
     Inner Monologue 闭环反馈补洞,均未根治)。
- **认知该不该与行动解耦**:解耦/分层(②c SayCan/CaP;②a PETS 规划 vs 执行;π0.5 高层语义+低层动作)
  vs 端到端耦合(②b RT-2/π0;②e WAM 联合去噪)。**张力点:DexTacWAM 实证耦合优于解耦**——
  把接触演化作为预测世界状态的一部分(74.7)远胜单纯触觉条件(26.6);而 RT-2 实证端到端 VLA 的
  "认知"无法独立产生新行动。
- **开放问题**:①世界模型预测保真度/长程 rollout 误差累积与模型利用;②VLA"认知"是否可解释/可推理
  (RT-2 CoT 是初步,黑箱,认知-行动耦合难分离评估);③agentic 可靠性/幻觉(三套补丁未根治);
  ④记忆显式 vs 隐式(ReCAT 发现机器人记忆规律≠序列建模规律);⑤接触动力学能否纳入 world model
  (②e 核心:视觉 future 不含力/形变/slip 监督);⑥WAM 实时性(Rolling-WAM 滚动想象 4.5×,闭环响应仍瓶颈)。

### 1.5 分支② 如何向下衔接操作支(本件核心价值之一)

- **②a(世界模型)→ ③a 操作支路线④(WAM 系)**:WAM = 世界模型思想在操作上的**直接落地**。
  DexTacWAM Sec2.1 明确自归「World Models and WAMs」谱系。**与②a 经典的区别**:②a
  (World Models/Dreamer)的 world model 主要用于"想象中训策略"或"在线 MPC 规划",预测**低维 latent/状态**,
  world model 与策略**可分离**;WAM 系预测**高维 video/tactile future**,且 world model 与动作生成
  **耦合**(joint denoising / flow matching)直接产出操作动作。**视触 WAM**(VT/Tac/DexTacWAM)把②a
  "预测行动后果"命题从视觉**扩展到接触动力学**(力/形变/slip)。
  **谱系链:②a 世界模型 → ②e 视触 WAM → ③a 操作支路线④。**
- **②(认知/推理)→ ③a 路线⑤(agentic/资产外化)的边界厘清**:SayCan/CaP/ProgPrompt/Inner Monologue
  是 **②c(LLM 规划)与路线⑤(agentic)的交叠区**。**边界:②"认知/推理"= 认知过程**(想什么、怎么分解、
  怎么推理、怎么记忆);**⑤"资产外化"= 认知的产物形态**(把认知固化成可复用、可执行的外部资产:
  代码/程序/skill 库/affordance 价值函数)。交叠典型:**Code as Policies 与 ProgPrompt** 既是②c
  (LLM 推理规划),又把规划**外化为可执行程序**;**SayCan** 的 affordance value function 是把"我能做什么"
  外化成可查询技能资产。**一句话:②是"想的过程",⑤是"把想的结果固化成可执行/可复用资产";
  二者在 CaP/ProgPrompt/SayCan 处重合。**

---

## §2 分支③b 运动控制(Locomotion)(深挖 + 假设检验)

**核心问题**:机器人如何**产生运动**——足式行走/奔跑/越障、人形全身控制、导航。
与③a 操作相对:③a 是"用手操作物体",③b 是"移动身体本身"。

### 2.1 子分支结构(③b-1 ~ ③b-5)

- **③b-1 足式运动 RL**(四足/双足,并行仿真→真机):Hwangbo ANYmal(*Science Robotics* 2019,
  DOI 10.1126/scirobotics.aau5872,仿真 RL + **actuator net** 迁真机)、Lee ANYmal(arXiv:2010.11251,
  *Science Robotics* 2020 V5 I47 eabc5986,教师-学生,无先验地图崎岖地形)、**Rudin "Learning to Walk
  in Minutes"**(arXiv:2109.11978,**CoRL 2021**,平坦<4 min/不平 20 min)、Miki 野外感知行走
  (arXiv:2201.08117,*Science Robotics* 2022 V7 I62)、Walk These Ways(arXiv:2212.03238,**CoRL 2022 Oral**,
  行为多态可调)。演进:能走→崎岖无图→分钟级→野外感知→可调泛化。
- **③b-2 parkour/敏捷运动**:Robot Parkour(arXiv:2309.05665,**CoRL 2023 Oral**,两阶段 RL + DAgger
  蒸馏单一视觉策略,A1/Go1)、Extreme Parkour(arXiv:2309.14341,**ICRA 2024**,DOI 10.1109/icra57147.2024.10610200)。
- **③b-3 人形全身控制**:ExBody(arXiv:2402.16796,**RSS 2024**,DOI 10.15607/rss.2024.xx.107,
  **venue 由 Phase 1 单源中置信升为 Crossref 高置信**;Unitree H1 19DoF,上身模仿 CMU MoCap ~780 段)、
  HumanPlus(arXiv:2406.10454,**venue 未核实**)、Humanoid Locomotion as Next Token Prediction
  (arXiv:2402.19469,**NeurIPS 2024**,DOI 10.52202/079017-2518,自回归 token 预测步态)。
- **③b-4 sim2real 与大规模并行仿真**(运动的数据引擎):Domain Randomization(arXiv:1703.06907,
  **IROS 2017[中置信,comment 仅 "submitted to"]**)、Isaac Gym(arXiv:2108.10470,**⚠️ venue 未核实**——
  comment 仅 "tech report",Crossref 误配,通称 NeurIPS 2021 D&B 但本轮未一手核到)、
  Zhao sim2real 综述(arXiv:2009.13303,**SSCI 2020** pp.737-744,journal_ref)。
- **③b-5 导航**:Habitat(arXiv:1904.01201,**ICCV 2019**,comment)、Matterport3D(arXiv:1709.06158,
  **3DV 2017**,DOI 10.1109/3dv.2017.00081)。

### 2.2 分支③b 全文级锚点卡(3 篇读全文)

- **Rudin "Learning to Walk in Minutes"(2109.11978,CoRL 2021,全文)**:
  - **训练范式**:大规模并行仿真。Isaac Gym 单 GPU 端到端(仿真+PPO 全在 GPU);基线 n_robots=20000→
    batch 1M(Sec4.1),最佳权衡 2048-4096 机器人;game-inspired 自动课程,训练 1500 iterations(Sec3)。
  - **数据来自仿真还是真机**:**训练数据全部来自仿真**(程序生成 5 类地形);真机仅用于**验证迁移**
    ("transfer the policies to the real robot to validate",Abstract)。**但**:ANYmal 串联弹性执行器
    "complex dynamics, **hard to model in simulation**",故用 **LSTM actuator net** 从关节位置指令算力矩
    (Sec3)——该 actuator net 沿用 Hwangbo 方法,**需真实电机数据做系统辨识**。
  - **关键对比数字(Sec1,操作 vs 运动的一手旁证)**:"OpenAI's block reorientation task was trained for
    up to **14 days** and their Rubik's cube solving policy took **several months**",而运动
    "train a perceptive policy in **under 20 minutes**";此前 blind 策略 12h、感知+最优控制 82/88h、
    全学习 120h。
- **Robot Parkour(2309.05665,CoRL 2023 Oral,全文)**:两阶段 RL + DAgger 蒸馏成单一视觉 GRU 策略;
  **无参考动作数据、简单奖励**;训练在仿真,真机(A1/Go1)部署;sim2real gap 主要在**视觉外观**
  (depth 渲染 vs 真实相机,Sec3.3),物理动力学 gap 可由蒸馏桥接("distillation training...can bridge
  the sim-to-real gap in physical dynamics properties such as terrain friction and mass",Sec3.3)。
  **自陈局限(Sec5,对假设检验极关键)**:"the current system **requires the simulation environments to be
  manually constructed**...new skills can only be learned when new environments...are added";
  未来"construct diverse simulation environments **automatically from large-scale real-world data**"。
- **ExBody(2402.16796,RSS 2024,全文)**:massively parallel Isaac Gym;Unitree H1 19DoF;
  **依赖真实人类动作数据——CMU MoCap ~780 段参考动作**(Sec III),retarget 到机器人骨架后做目标条件 RL;
  上身模仿参考、下身放松仅跟随速度;**因硬件 DoF/增益比 graphics 动画低一个数量级(Sec II),
  直接迁移动画动作不可行**,故放松约束;自陈无法实现"significant environmental interactions"的动作。

### 2.3 分支③b venue 核实汇总

**已核实(高置信)**:Hwangbo=Science Robotics 2019(Crossref DOI);Lee=Science Robotics 2020(journal_ref);
Miki=Science Robotics 2022(journal_ref);Rudin=CoRL 2021(comment);Walk These Ways=CoRL 2022 Oral(comment);
Robot Parkour=CoRL 2023 Oral(comment);Extreme Parkour=ICRA 2024(Crossref DOI);ExBody=RSS 2024
(Crossref DOI,**由单源升 high**);Humanoid Next-Token=NeurIPS 2024(Crossref);Zhao sim2real 综述=SSCI 2020
(journal_ref);Habitat=ICCV 2019(comment);Matterport3D=3DV 2017(Crossref DOI)。
**中/低置信或未核实**:Domain Randomization=IROS 2017(**中**,comment 仅 "submitted to");
**Isaac Gym=venue 未核实(低)**——comment 仅 "tech report",Crossref 误配,通称 NeurIPS 2021 D&B
本轮未一手核到(**⚠️ 与 Phase 1 子 agent 的"S2+DBLP 核到 NeurIPS 2021 D&B"结论冲突,须复核**);
**HumanPlus=venue 未核实(低)**——Crossref 误配,comment 仅网站(通称 CoRL 2024,**与操作支图谱
路线③子 agent 的"CoRL 2024 via GitHub+OpenReview"结论冲突,须复核**)。

### 2.4 分支③b 演进 / 分歧 / 开放问题

- **演进**:model-based 最优控制 → 学习 blind 行走(Hwangbo/Lee)→ **GPU 大规模并行把训练压到分钟级
  (Rudin,分水岭)** → 野外感知(Miki)→ 视觉敏捷 parkour(Zhuang/Cheng)→ 人形全身/表达性控制
  (ExBody/HumanPlus/Next-Token)。③b-4(并行仿真+sim2real)是贯穿全线的"数据引擎"。
- **分歧**:(a)blind vs perceptive;(b)专用技能 vs 单一端到端策略(parkour 内部);(c)人形是否需人类
  动作先验(ExBody/HumanPlus 依赖 MoCap/遥操 vs Next-Token 自回归);(d)模仿约束强度(ExBody 反直觉
  主张"放松下肢更鲁棒")。
- **开放问题(带原文出处)**:①仿真环境需**手工构建**,难自动扩到真实多样性(Parkour Sec5);
  ②执行器/接触动力学难仿真,依赖 actuator net 等真实数据组件(Rudin Sec3);③人形硬件 DoF/增益远低于
  graphics 动画(ExBody Sec II),限制动作迁移;④长时间鲁棒性、动态扰动、能源、跨本体泛化仍活跃。

### 2.5 假设检验专节(本件核心价值之二;判定可推翻原判断)

**原假设(骨干图谱 §3)**:"数据瓶颈是分支特异的——③b 运动的数据问题已被'刚体仿真+大规模并行'
**基本解决**,③a 操作没有(接触/形变/触觉难仿真),故'数据瓶颈'文献集中在操作支,是**物理决定**的。"

**支持证据(带原文逐字句+出处)**:
- **S1** 运动靠并行仿真、训练数据来自仿真:Rudin "capable of simulating thousands of robots in a single
  simulation"(Sec2),平坦<4 min/不平 20 min(Abstract),真机仅 "to validate the approach"。
- **S2(最强一手旁证)** 同篇给出操作 vs 运动算力/数据对比:Rudin Sec1 "OpenAI's block reorientation
  task was trained for up to **14 days** and their Rubik's cube solving policy took **several months**",
  而运动 "under 20 minutes"。→ 直接支持"操作数据/算力代价远高于运动"的非对称。
- **S3** 刚体腿-地接触相对易仿真:Parkour 的 sim2real gap 主要在**视觉外观**,物理动力学 gap 可由蒸馏
  桥接(Sec3.3)。→ 间接支持刚体接触较易处理。
- **S4** 操作支 sim2real 仍高度活跃:大量 "Closing the Reality Gap...Dexterous..." 类论文
  (**注:多为未开原文的预印本,仅作旁证,非逐字证据**)。

**反驳/修正证据(带原文逐字句+出处)**:
- **R1** 运动并非"纯仿真自造数据"——需真实数据组件:Rudin Sec3 ANYmal "series elastic actuators with
  fairly complex dynamics, which are **hard to model in simulation**",故用 actuator net(训练依赖
  Hwangbo 的**真实电机数据**系统辨识)。→ "刚体仿真即可"被削弱。
- **R2** 人形全身控制依赖真实人类动作数据:ExBody "we utilize the **CMU MoCap dataset (around 780
  reference motions)**"(Sec III),且硬件 DoF/增益限制使 "direct transfer of graphics techniques onto
  the real robot **infeasible**"(Sec II)。→ 人形运动的数据问题**未**被纯刚体仿真解决。
- **R3** 运动存在环境/多样性数据瓶颈:Parkour Sec5 "requires the simulation environments to be
  **manually constructed**...new skills can only be learned when new environments...are added"。
  → 瓶颈从"动力学数据"转移到"环境/场景多样性数据"。
- **R4** "已解决"仅在受限条件下成立:Rudin 的分钟级针对**四足、结构化/程序生成地形、行走**;
  parkour/人形/感知敏捷/长时鲁棒仍开放。

**对比证据**:未找到单一权威头对头比较 locomotion vs manipulation 数据需求的文献;Zhao sim2real 综述
按**方法**(域随机化/适应/蒸馏/模仿/元学习)组织,**非按任务分支难度**对比。→ 假设中"物理决定的
分支差异"**缺乏一篇直接对比文献支撑**,更多是社区共识/推断;Rudin Sec1 的操作 vs 运动算力对比是
目前最接近的一手旁证。

**判定:部分成立(置信度:中-高)**
- **成立(高置信)**:运动与操作存在**真实的非对称**——四足行走等刚体腿-地任务已能用大规模并行仿真
  高效训练并迁真机,而操作(接触富集/形变/触觉)的 reality gap 明显更大、仍是活跃开放问题
  (Rudin Sec1 的 14 天/数月对比 + 操作侧大量 "closing the reality gap" 文献)。
- **须修正(中置信)**:①"**已被基本解决**"**被夸大**——仅在四足/结构化地形/行走等受限条件下成立;
  parkour、人形、感知敏捷、长时鲁棒、动态扰动均未解决。②"**纯物理决定、刚体仿真即可**"**不准确**——
  运动仍有真实数据入口(执行器辨识 Rudin、人形 MoCap 先验 ExBody ~780 段、环境多样性 Parkour)。
  ③"数据瓶颈"在运动支**不是消失而是转移**——从"动力学/轨迹数据"转到"环境多样性 + 真实执行器/
  人类动作先验"。
- **盲区**:未找到直接对比 locomotion vs manipulation 数据需求的权威单篇;"物理决定论"框架缺一手
  对照实验支撑。

**骨干图谱 §3 应如何改(已回流)**:把"③b 数据问题已解决 / ③a 未解决,物理决定"改为——
"**③b 运动的数据瓶颈在'刚体腿-地 + 结构化地形 + 四足行走'子域已被大规模并行仿真 + 执行器系统辨识
大幅缓解;但环境多样性、感知敏捷、人形全身控制仍依赖真实数据(手工建场景/人类 MoCap/电机辨识),
瓶颈是转移而非消失。③a 操作因接触富集/形变/触觉,仿真 gap 更大,数据瓶颈更重。二者非对称真实存在,
但是光谱而非'已解决/未解决'的二元,且非纯物理决定——真实数据组件仍进入运动支。**"

---

## §3 venue 冲突与更正登记(须复核)

**两路子 agent 对同一论文 venue 结论冲突(须复核,不硬断言)**:
1. **Isaac Gym(2108.10470)**:Phase 1 子 agent 报"NeurIPS 2021 D&B(S2+DBLP)";本轮 ③b 子 agent 报
   "venue 未核实(comment 仅 tech report,Crossref 误配)"。→ **降为"中置信,待复核"**,骨干图谱 §8
   与操作支图谱引用 Isaac Gym venue 时须标"通称 NeurIPS 2021 D&B,本轮未一手核到"。
2. **HumanPlus(2406.10454)**:操作支路线③子 agent 报"CoRL 2024(GitHub+OpenReview)";本轮 ③b 子 agent
   报"venue 未核实(Crossref 误配,comment 仅网站)"。→ **降为"中置信,待复核"**。
3. **Domain Randomization(1703.06907)**:comment 仅 "submitted to IROS 2017" → **中置信**(接收未直接核到)。

**Phase 2 核出的更正/升级**:
- **ExBody(2402.16796)= RSS 2024**(Crossref DOI 10.15607/rss.2024.xx.107,**由 Phase 1 单源中置信升 high**)。
- **DreamerV2(2010.02193)= ICLR 2021**(comment 逐字,**由 Phase 1 低置信升实证**)。
- **World Models 题名/ID 陷阱**:1803.10122(交互式预印本《World Models》)≠ 1809.01999
  (NeurIPS 正式版《Recurrent World Models Facilitate Policy Evolution》),引用须注双题名/双 ID。
- **Lee ANYmal = arXiv:2010.11251**、**Miki = arXiv:2201.08117**、**Walk These Ways = arXiv:2212.03238**、
  **Humanoid Next-Token = arXiv:2402.19469(NeurIPS 2024)**——补核准 ID。

---

## §4 残余不确定性与诚实标注

- **全文级 vs 摘要级**:分支②读全文 5 篇(World Models/PETS/DreamerV3/RT-2/DexTacWAM),摘要级 15 篇;
  分支③b 读全文 3 篇(Rudin/Robot Parkour/ExBody),摘要级 12 篇。**摘要级篇目的内部表格/局限未核。**
- **venue 未核实/中低置信**:分支② 7 篇(π0.5 中 + 6 篇 2026 预印本);分支③b 3 篇(Isaac Gym 低/
  HumanPlus 低/Domain Randomization 中)+ **2 处跨子 agent venue 冲突须复核**(§3)。
- **可能漏查(子 agent 诚实标注)**:分支②——TAMP 经典与 LLM+PDDL(PDDLStream/Evidence-Gated TAMP)、
  MuZero、JEPA/LeCun 重建无关世界模型(②a 重要分歧方)、视频生成式世界模型(Genie 系)、
  其他 VLA(RoboFlamingo/3D-VLA/OpenVLA)、CaP 后续(VoxPoser)、FastWAM/OmniVTLA 未单独开条;
  分支③b——双足/人形 2026 最新("closing the reality gap" 多为 blog/预印本未开原文,列为线索非结论)。
- **假设检验证据强度**:支持/反驳的强证据均来自已开原文的一手论文(Rudin/Parkour/ExBody),逐字可核;
  **对比侧最弱**——缺直接对比 locomotion vs manipulation 数据需求的权威文献;"物理决定论"缺一手对照实验。
- **本件未做**:权威性检验(≥3 处跨源定案)、会签前自查复核(独立子任务+外部交叉源)。
  **故 v0.1 不签发**;签发前须补(候选定案:Isaac Gym venue 冲突、HumanPlus venue 冲突、
  World Models 双 ID、DROID 84/86、OXE 21/34、LIBERO-Pro 总任务数)。

---

## 署名链

- **起草**:Dexter(2026-10-14,主会话汇总 + 2 路异路径子 agent 全文级深挖 + 假设检验)。
- **性质**:领域级综述图谱 **Phase 2 深挖件**(分支②③b),黄色产物草稿。
- **状态**:**v0.1 草稿,未走会签前自查复核、未签发、不入 `final/`、不署名/不投稿/不发布/不对外**。
- **下一步**:①其余分支(①感知/⑤本体/⑥仿真/⑦评测)深挖排后续轮;②§3 venue 冲突复核
  (Isaac Gym/HumanPlus);③权威性检验(≥3 处跨源定案);④会签前自查复核 → 与骨干图谱合并签发 v1.0;
  ⑤骨干图谱 §3 假设修正已回流(见 §2.5)。
- **复核**:______(待会签前自查复核)
- **签发**:______(未签发)
