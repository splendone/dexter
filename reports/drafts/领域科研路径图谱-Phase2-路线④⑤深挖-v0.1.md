# 领域科研路径图谱 · Phase 2 深挖:路线④(结构先验/检索)+ 路线⑤(agentic 资产外化)· v0.1

**性质**:G3 里程碑④ 关联的**综述级文献地图深挖件**(黄色产物,草稿制)。
**版本**:v0.1 **Phase 2 深挖稿**;**未走会签前自查复核、未签发、不入 `final/`**。
**起草**:Dexter,2026-10-13(主会话汇总 + 2 路异路径子 agent 全文级深挖)。
**触发**:委托人 2026-10-13 第六轮指令"继续推进 Phase 2,先深挖路线④和⑤"。
**承接**:`reports/drafts/领域科研路径图谱-v0.1.md`(Phase 1 骨干稿)——本件把骨干稿
§3.4(路线④)与 §3.5(路线⑤)从"每路线 2-4 篇代表作"**深挖到子分支结构 + 10-18 篇 +
核心锚点全文级 + venue 核实 + 演进/分歧/开放问题**。
**证据纪律**:两路子 agent 共**全文级精读 15 篇**(保留 `<math alttext>` 提取)、
摘要级核实其余;**venue 核不到一律标"未核实(仅 arXiv 预印本)",绝不编造会议名**;
数字带原文位置;**ID/venue 错误据实更正**(见 §3)。

---

## §0 本件与骨干图谱的关系 + Phase 2 范围

- **骨干图谱(Phase 1)**:七路线各 2-4 篇 venue 已核代表作 + 顶层瓶颈 + MT3 三向坐标 + 演进时间线。
- **本件(Phase 2)**:只深挖**路线④与⑤**(委托人指定;这两支与 MT3 复现基础、已裁决的
  "对撞层"最相关)。**其余五路线(①②③⑥⑦)的深挖排后续轮。**
- **深挖增量**:①子分支结构(④a-④e / ⑤a-⑤e);②每支扩到 10-18 篇;③核心锚点**全文级**
  (不只摘要);④venue 核实(已核 vs 未核实分列);⑤补核 Phase 1 遗留的不确定 ID
  (VINN/TP-Flow/Res-HIL/双臂 one-shot/PaLM-E);⑥演进/分歧/开放问题带全文证据;
  ⑦**对撞层证据逐字核实**(BiGym 2.0 / RoboDojo agentic 缺席)——直接支撑骨干图谱的
  对撞层节点与综述/立场文章"对撞缺席"分层重写重审。

---

## §1 路线④ 结构先验 / 检索式模仿学习(MT3 所属路线)

**押注的瓶颈子维度**:**数据结构/复用**——不靠喂更多数据,而靠结构先验(分解/相位/
位姿估计)与检索(测试时调演示)省数据、得泛化。

### 1.1 子分支结构(④a-④e)

#### ④a 策略表示基座(强学习器,检索/分解的对照与底座)
- **核心命题**:用强参数化策略从演示直接学;是免训练检索的**对照基线**与**可替换底座**。
- **代表作**:
  - **ACT/ALOHA**(2304.13705,**RSS 2023**,Crossref DOI 10.15607/rss.2023.xix.016):
    低成本双臂遥操 + 动作分块 Transformer,毫米级精细双臂(穿扎带/装电池)。
  - **Diffusion Policy**(2303.04137,**RSS 2023 + IJRR 扩展**,comment 逐字):
    视觉运动策略 = 条件去噪扩散,预测动作序列处理多模态;**12 任务/4 基准平均 +46.9%**(摘要);
    全文 §9 局限、§3.4 迭代去噪推理慢。
- **关键张力(全文级)**:MT3 全文称 "challenging the assumption that complex neural
  policies are necessary",**但其 interaction 阶段仍用 ACT(MT-ACT+)**——**强学习器未被
  抛弃,而是被检索包起来**。这是路线④内部"检索 vs 训练"分歧的实质。

#### ④b one-shot 位姿估计 + 轨迹迁移(One-Shot IL(Vitiello)→MT3→ODIL/POIL 谱系)
- **核心命题**:单演示下把模仿化为"未见物体位姿估计 + 刚性轨迹迁移",免训练免采数。
- **代表作**:
  - **One-Shot Imitation Learning: A Pose Estimation Perspective(Vitiello/Dreczkowski/Johns)**(2310.12077,**CoRL 2023**,PMLR 229:943-970;MT3 位姿对齐上游):one-shot IL =
    trajectory transfer + unseen object pose estimation;**8 个位姿估计器 vs DOME,
    10 真实任务/~1500 rollouts,该文平均超 DOME 22%(全文)**;Sawyer 平台。
    **自陈局限(全文 §5)**:不处理类内实例、依赖标定、需静态场景、不适用两物体相对位姿任务。(⚠️ 待核:本条 2310.12077 先前被误标为「STRAP」并称「MT3 同门前身」;「同门 / 规模化版」表述须对 MT3 全文重新核实二者关系,不得再作既定事实断言。)
  - **MT3**(2511.10110,**Science Robotics 2025**):见 §1.2 全文锚点卡。
  - **ODIL / One-Shot Dual-Arm Imitation Learning**(2503.06831,**ICRA 2025**,comment 逐字
    "Accepted at ICRA 2025"):单演示双臂,三阶段视觉伺服(3-VS)精对齐后回放轨迹;
    = MT3 对齐/交互思想的**双臂版**(MT3 引为 [48])。**⚠️ 更正:先前记 ICRA 2024,实为 ICRA 2025。**
  - **POIL**(2609.30404,**venue 未核实**):点基 one-shot + 稳定动力系统,功能部位 3D 点集
    同时用于迁移与**闭环执行**,多模态 LLM grounding。
- **张力**:位姿估计误差→成功率链条;**刚性迁移(One-Shot IL(Vitiello)/ODIL/MT3)vs 稳定动力系统鲁棒
  闭环(POIL)**。

#### ④c 检索式少样本(度量演进是主线)
- **核心命题**:从大先验库检索相关样本增强少样本目标策略,**关键在检索度量**。
- **代表作(按度量演进排序)**:
  - **VINN**(2112.01511,**RSS 2022**,Crossref 10.15607/rss.2022.xviii.010;
    正题《The Surprising Effectiveness of Representation Learning for Visual Imitation》,
    VINN 是其最近邻方法,Mobile ALOHA ref[63] 逐字确认):几何最近邻视觉模仿(非参数)。
  - **Behavior Retrieval**(2304.08742,**RSS 2023**,Crossref 10.15607/rss.2023.xix.011):
    查询无标注集,态-动作相似检索离线数据。
  - **FlowRetrieval**(2408.16944,**CoRL 2024**,PMLR v270/lin25a + OpenReview FHnVRmeqxf):
    见 §1.2 全文锚点卡;光流引导度量解耦视觉/任务相似。
  - **IWR / Data Retrieval with Importance Weights**(2509.01657,**CoRL 2025**,comment):
    指常用度量 = 先验点到目标集最小距离(等价于高斯 KDE 极限、高方差最近邻),改用重要性加权。
  - **DARP / Difference-Aware Retrieval Policies**(2606.09758,**ICLR 2026**,comment):
    半参数,把 IL 重参数化为 **k 近邻局部邻域结构**而非 state→action 映射。
  - **ROSER**(2603.01474,**ICLR 2026 DATA-FM Workshop**,comment):少样本序列检索,
    从长日志抽可复用片段,学时序窗任务无关度量。
  - **HSR / Hierarchical Skill Retrieval**(2608.24042,**venue 未核实**):层级技能检索
    (长程任务完整匹配稀有、可复用技能丰富)。
  - **TP-Flow**(2609.27780,**venue 未核实,匿名评审中**):任务原型引导流匹配,相位级原型 token;
    **LEROBOT-ARM-SO101,1/4/6-shot 66.8/79.6/82.1%,75.5% AUC(摘要,与既有锚点逐字一致)**。跨 ④c/④d。
- **度量演进主线**:几何最近邻(VINN)→ 态-动作(BR)→ 光流(FlowRetrieval)→
  重要性加权(IWR)→ kNN 邻域(DARP)→ 层级技能(HSR)→ 时序片段(ROSER)。
  **这条演进线是路线④最清晰的内部脉络。**

#### ④d 任务/相位分解
- **核心命题**:把长程/接触轨迹分解为可复用子单元,**分解本身即省数据的结构先验**。
- **代表作**:
  - **MT3**:alignment(跨任务一致)+ interaction(任务特异)两阶段。
  - **ManiLong-Shot**(2512.16302,**AAAI 2026**,comment):围绕**物理交互事件**组织,
    化为排序交互感知基元,VLM 推理或规则驱动;长程多步 +22.8% over SOTA(摘要)。
  - **PHASE**(2609.30889,**IROS 2026**,comment):接触插入按相位(search→insert),
    **柔顺腕触觉/力信号揭示相位并指导检索**;peg-in-hole 五几何,+13pp over 最强非相位感知基线。
- **粒度分歧**:两段固定(MT3)vs 变长交互事件(ManiLong-Shot)vs 力/触觉相位(PHASE)
  vs 时序片段(ROSER)。**MT3 全文自陈代价**:"decomposition prevented this beneficial
  representation sharing"(分解破坏跨任务表示共享)。

#### ④e MT3 下游延伸(闭环 / 跨本体 / 触觉)
- **核心命题**:攻 MT3 四个自陈缺口。
- **代表作**:
  - **BPC**(2609.30134,**venue 未核实**,Stanford/Schwager,arXiv 2026-09-24):见 §1.2 全文锚点卡;闭环。
  - **RTCF**(2608.04527,**venue 未核实**):免训练测试时校正冻结 VLA,"检索哪段经验"与
    "迁移其动作哪部分"分离,Progressive Memory Alignment 因果对齐 + 频域校正;LIBERO-Long 61.6%→68.6%。
  - **Retrieve-Don't-Retrain**(2606.15631,**venue 未核实**,项目页 recap-robot.github.io):见 §1.2;跨本体。
  - **EmbodiSteer**(2606.12965,**venue 未核实**):免训练,把 Cartesian 策略推理时扩散采样
    经正向运动学提升到目标关节空间,零样本本体感知部署。
  - **POIL**(闭环)、**PHASE**(触觉)见上。
- **分歧**:免训练/冻结+检索能否替代学策略?BPC/RDR/RTCF/EmbodiSteer 均主张可,
  **但都自陈受检索库覆盖约束**(BPC 全文:"behavior far from the demonstrated states may
  require recovery actions absent from the bank")。

### 1.2 路线④全文级锚点卡(6 篇读全文)

- **MT3(2511.10110,Science Robotics 2025)**:免训练检索 + alignment/interaction 两阶段分解
  (§4.2 hierarchical retrieval:4.2.2 对齐/4.2.3 交互);Sawyer + Robotiq 2F-85 + 单相机。
  数字:3,450 rollouts/70 物体;1,000 任务 <24h、每任务单演示;400+ 物体;**per-task <10 演示时
  分解较单片学习数据效率提升一个量级,检索持续胜行为克隆(全文)**。**自陈局限(全文)**:
  ①"decomposition prevented this beneficial representation sharing"(Appendix A diversity-efficiency Pareto);
  ②"open-loop retrieval-based interaction often failed since it treated novel objects exactly
  as training instances"(开环检索不能插值);③依赖物体分割(透明/杂乱失效);④双臂需扩展。
- **One-Shot IL(Vitiello/Dreczkowski/Johns,2310.12077,CoRL 2023,PMLR 229:943-970)**:超 DOME 22%,~1500 rollouts;§4.1 标定/位姿误差敏感性;§5 局限四条。
- **FlowRetrieval(2408.16944,CoRL 2024)**:指现有检索两极——要么依赖视觉相似的精确行为
  (不现实),要么靠高层语言语义(太抽象,捕捉不到 turns/twists 等低层运动);用**光流表征
  解耦视觉相似与任务相似**做检索增强;**平均超最佳先验检索法 27%(+10% sim/+19% real),
  超各域最佳基线 14%(摘要)**。与 MT3:同为检索省数据,但 FlowRetrieval 检索增强**参数策略**,MT3 免训练。
- **BPC(2609.30134,venue 未核实)**:免训练行为克隆 = action-aware 检索度量 + **Hankel 动作
  延拓先验(行为系统论)+ 闭式单步残差校正**;Table III 仿真桌面 300 rollouts/任务,Table V
  灵巧(DexArt)120 rollouts/任务;**匹配训练式 BC(部分超越),策略拟合从数小时→数秒(消费级 GPU),
  闭环 ≥75Hz(全文)**。与 MT3:同免训练检索,BPC 加**闭式残差校正求闭环**;MT3 开环。
  **自陈局限(§VI)**:"Retrieval cannot resolve ambiguities caused by missing task information,
  and behavior far from the demonstrated states may require recovery actions absent from the bank";
  非负平均不能重构检索凸包外的 query。
- **Retrieve-Don't-Retrain(2606.15631,venue 未核实)**:检索增强策略**训练一次**(目标本体 query +
  廉价本体 pool 如人手视频)后冻结;新任务靠往检索池追加 pool 演示;Retrieval-Augmented WAM 骨干,
  对 WAM 增益更大;**RoboTwin 2.0 上超跨本体基线;目标本体遥操演示"慢、受硬件约束、约 18× 贵于
  人手视频"(全文)**。与 MT3:同"检索替代重训",RDR 主攻**跨本体**(人手视频→机器人)。
- **Diffusion Policy(2303.04137,RSS 2023+IJRR)**:+46.9%,§9 局限,§3.4 推理加速。

### 1.3 路线④ venue 核实汇总

**已核实**:MT3=Science Robotics 2025(journal_ref+DOI);One-Shot IL(Vitiello)=CoRL 2023(PMLR 229:943-970);
DP=RSS 2023+IJRR(comment);ACT=RSS 2023(Crossref DOI);Behavior Retrieval=RSS 2023(Crossref);
VINN=RSS 2022(Crossref);FlowRetrieval=CoRL 2024(PMLR v270+OpenReview);IWR=CoRL 2025(comment);
ODIL 双臂=ICRA 2025(comment);ManiLong-Shot=AAAI 2026(comment);DARP=ICLR 2026(comment);
ROSER=ICLR 2026 DATA-FM Workshop(comment);PHASE=IROS 2026(comment)。
**未核实(仅 arXiv 预印本)**:BPC(2609.30134)、RTCF(2608.04527)、Retrieve-Don't-Retrain(2606.15631)、
EmbodiSteer(2606.12965)、HSR(2608.24042)、POIL(2609.30404)、TP-Flow(2609.27780,匿名评审中)。

### 1.4 路线④演进 / 分歧 / 开放问题

- **演进**:学策略(ACT/DP,2023 RSS)→ one-shot 位姿估计轨迹迁移(One-Shot IL,Vitiello,2023 CoRL)→
  检索库规模化+两阶段分解(MT3,2025 Sci Robotics)→ 闭环/跨本体/触觉延伸(2026:BPC/RTCF/
  RDR/EmbodiSteer/PHASE/POIL/ManiLong-Shot)。检索度量并行演进(见 ④c)。
- **分歧**:①检索 vs 训练(免训练检索能否替代学策略?MT3 挑战"复杂神经策略必需"但自身
  interaction 仍用 ACT;BPC 仅"部分"超越训练式 BC);②分解的代价(MT3 自陈破坏跨任务表示共享);
  ③分解粒度(两段/变长事件/触觉相位/时序片段);④检索度量之争;⑤开环 vs 闭环
  (One-Shot IL(Vitiello)/MT3 开环刚性回放遇 novel 物体失败,BPC/RTCF/POIL 推闭环)。
- **开放问题**:①检索不能插值(BPC/MT3 全文原话);②位姿-几何张力(刚性迁移受位姿误差链约束);
  ③**跨本体免训练仍开着**(RDR/EmbodiSteer 多在仿真/RoboTwin,真机证据薄);④**scaling 交叉点未测**
  (MT3 只给 diversity-efficiency Pareto,未给"检索 vs 训练"随数据/任务规模的交叉);
  ⑤触觉×检索仅 PHASE 单点,未成体系;⑥分解效率与表示共享如何调和(MT-ACT+ 部分缓解,未解决)。

---

## §2 路线⑤ agentic / 资产外化

**押注的瓶颈子维度**:**数据结构/复用**——把长程能力外化成可复用中间资产(技能库/工具接口/
程序/playbook),VLM/LLM 做高层 harness,**演化期生成、部署期调用**,几乎不依赖策略训练数据。
**与路线④的区别**:④检索的是"演示轨迹",⑤外化的是"程序/技能/工具"这类符号或半符号资产。

### 2.1 子分支结构(⑤a-⑤e)

#### ⑤a LLM 高层规划 / 接地奠基(2022-2023,venue 均已核实)
- **核心命题**:LLM/VLM 提供高层程序性知识,但须"接地"到物理可执行性;资产 = 预训练技能 +
  其价值函数 / 可调用 API / 生成的程序。
- **代表作**:
  - **SayCan**(2204.01691,**CoRL 2022**,OpenReview 7Ti96LhnF2):LLM 提议 × 技能价值函数接地;
    打分 = P(LLM:技能助于指令)× P(affordance:当前状态可成功);资产 = pretrained skills + value functions(§3)。
  - **Code as Policies**(2209.07753,**ICRA 2023**,IEEE Xplore 10160591):LLM 写机器人策略代码(LMP),
    处理感知输出(开放词汇检测器)+ 参数化 control primitive API,可递归生成未定义函数(§1/Fig.1);
    首次让 LLM **直接进入感知-动作反馈回路**;自陈局限:代码执行前无法验证物理可行性(被 WAA 继承为动机)。
  - **Inner Monologue**(2207.05608,**CoRL 2022**,OpenReview 3R3Pz5i0tye):环境反馈作"内心独白"重规划。
  - **ProgPrompt**(2209.11302,**ICRA 2023**,IEEE Xplore 10161317 + NVIDIA singh2023progprompt):
    情境化任务计划即程序(带前置断言的 Python 式计划)。
  - **PaLM-E**(2303.03378,**ICML 2023**,PMLR v202/driess23a):具身多模态 LM(连续传感嵌入语言),正向跨任务迁移。
- **演进/分歧**:技能+价值接地(SayCan)→ 代码即策略(CaP)→ 反馈重规划(Inner Monologue)→
  情境程序(ProgPrompt)→ 多模态具身(PaLM-E)。分歧:符号计划 vs 可执行代码;接地靠学习价值函数 vs 感知 API。

#### ⑤b 资产/技能库演化(2025-2026,均为未核实预印本)
- **核心命题**:把编码/技能生成移到**演化期**(offline/experience),部署期只调用**冻结资产**
  → 降延迟 + 解耦"可复用机制"与"任务决策"。**这是与⑤a 的关键区别。**
- **代表作**:
  - **WAA**(2609.29964,**venue 未核实**,comment "Working in progress"):见 §2.2 全文锚点卡;
    多模态技能库 + 视觉动作工作区;LIBERO-Pro **75.6%**。
  - **Robo-Harness K1**(2609.29389,**venue 未核实**,comment "preprint"):见 §2.2;感知即工具;
    **⚠️ 77.8%/88.9% 是 18 例匹配子集,全量 139/180=77.2%**。
  - **RACaP**(2609.29394,**venue 未核实**):冻结 typed Policy APIs + ReAct harness + 经验记忆
    ("moves coding to evolution");LIBERO-PRO **2.5× CaP 成功率 + 1.9× 中位策略时间加速**;
    蒸馏 Qwen3-VL-8B **13.2× 单决策推理加速、物理调用 16→4(全文 §4)**。
  - **Recursive Harness Distillation(RHD)**(2609.33378,**venue 未核实**):playbook(干预知识)+
    观测/干预 VLA 接口;强体蒸馏给轻体、递归精炼;**真机 37.3%→64.0%;SimplerEnv Bridge 轻体+playbook
    66.7%(无 playbook 41.7→43.8),强体+playbook 79.2%(全文 §4-5)**。
  - **RAPID**(2609.30249,未核实):单个视觉人类演示→自动生成/验证/精炼机器人程序(摘要级)。
  - **DexAgent**(2609.35318,未核实):自演化工具库;agentic Human2Sim2Robot(摘要级)。
  - **AdaHVLA**(2609.29204,未核实):自适应 harness,通过机器人经验精炼 code-based 协调策略(摘要级)。
  - **Coding Agents for TAMP**(2609.30233,未核实):coding agent 合成跨 TAMP 实例泛化的程序(摘要级)。
- **分歧(资产该是什么)**:程序/代码(RAPID/RACaP APIs/CaP-for-TAMP)vs 技能库(WAA)vs
  工具库(K1/DexAgent)vs playbook(RHD)vs 协调策略代码(AdaHVLA)。**共同点:演化期生成、部署期冻结调用。**

#### ⑤c harness 包冻结策略(2026 主流,均未核实预印本)
- **核心命题**:冻结 VLA/基础模型,harness(agent+tools+memory+prompts)**包裹**它,
  **组合取胜——不取代端到端策略**。
- **代表作**:
  - **Harness VLA**(2607.08448 v5,未核实):记忆引导 agent 把冻结 VLA 操舵成可靠 primitive,
    抗部署扰动(语义重定向/目标重绑/布局偏移)。
  - **COAP / Embodied Turing Machines**(2610.12369,未核实):Code-Only-as-Policy,磁带=机器人+环境状态,
    决策**全写进代码**(对照 Agent-as-Policy/Harness VLA 运行时查 VLM)。
  - **Scale and Selection**(2609.39304 v2,未核实):研究自动 harness 演化何以致效;optimizer agent
    改 prompts/tools/控制规则;每轮 rollout 数量主导成效。
  - **PhysEvo**(2610.08995,未核实,全文核):单冻结模型上的物理 RSI;task agent 执行,meta-agent
    诊断/改工具+技能/可改自身诊断工具;**42 RoboDojo 任务 62.00%(全文)**。
  - **EmbodiedRSI**(2610.10498,未核实):自演化 harness,假设引导共演化。
  - **AR-WAM**(2609.23578 v2,未核实):视觉条件 agent-ready 世界动作模型,取代歧义自然语言指令接口。
  - **Encore**(2609.37359,未核实):少样本 agentic 策略发现,给 agent 少量演示作**证据阅读**(非训练数据)。
- **⑤c 内部分歧**:COAP 主张**纯代码、运行时不查 VLM** vs Harness VLA/WAA/K1/RACaP **包裹冻结
  VLA/VLM(2026 主流=包裹/组合)**。PhysEvo/EmbodiedRSI 是 harness 的 RSI 自演化。

#### ⑤d 部署期生成 / 自改进(跨支)
- **DREAM**(2608.29078,未核实,摘要级):部署期演示生成 real-to-sim——重建工作区,LLM 把指令译成
  符号目标+成功判据,TAMP 生成可行轨迹,跨随机配置增广、按判据验证→为预训练 VLA 产微调数据,
  **无需任务专用人类演示**。**边界提示**:DREAM 产出"动作标注演示数据"(近路线④产物类型),
  但生成方式是 agentic;⑤d 与⑤c 高度重叠,图谱宜标"跨支"。

#### ⑤e 对撞层与评测
- **BiGym 2.0**(2610.07594 v2,未核实,全文核):**唯一预算配平的 VLA/IL/demo-RL/coding-agents 对撞**(详见 §4)。
- **LIBERO-Agent**(2609.39507,未核实):agent-native 基准,agent 选观测/用自带工具/发 native 动作命令
  (**刻意不用程序/技能**);200 任务、30 任务主套件;逐字证实 "pronounced reliability gap: agents
  perform well on perception and easy short-horizon tasks, [but] performance degrades substantially
  on hard short-horizon and long-horizon tasks"。
- **RoboDojo**(2607.04434 v3,未核实,全文 grep):42 仿真+18 真机任务、5 维、30 策略同表公开榜;
  **全文 0 处 agentic**(详见 §4)。

### 2.2 路线⑤全文级锚点卡(5 篇读全文)

- **SayCan(2204.01691,CoRL 2022)**:资产 = 预训练低层技能 + 每技能价值/affordance 函数;
  无"演化期",部署时 LLM 逐句提议、价值函数逐步打分;关键句(§3)"SayCan grounds LLMs via
  value functions of pretrained skills";局限:依赖已有技能集与价值函数,**不能生成新技能**。
- **Code as Policies(2209.07753,ICRA 2023)**:资产 = LLM 生成的策略代码(LMP),调用感知 API +
  control primitive API;可递归生成未定义函数;首次让 LLM 直接进入感知-动作反馈回路;
  自陈局限:代码执行前无法验证物理可行性。
- **WAA(2609.29964,未核实预印本)**:资产 = 多模态技能库(seed skills 由 Codex/GPT-5.5 从 harness API
  写出,经"证据审阅"从专家视频+人类教学演化)+ 视觉动作工作区(contact views 自动选取、action rehearsal 预演)。
  **演化-部署两期**:演化期用 Learner 等 agent 角色(GPT-5.5 驱动)从 LIBERO-90 视频演化技能,
  **评测前冻结**("no LIBERO-Pro or robosuite rollout, failure log, or label updates skills");
  部署期 VLM(Gemini 3.7 Flash)在工作区内调用技能;交互轨迹蒸馏进 9B VLM 学会"驾驶同一 harness"。
  **关键数字**:LIBERO-Pro **75.6%** 均值(§4,> ASPIRE 72.0%,胜过端到端 VLA/code-as-policy/同 backbone
  视觉 harness),迁移 robosuite 无需再学。**自陈局限**:"actions cannot be tried before they are taken /
  physical actions are irreversible";"A program cannot inspect whether a specific pose is appropriate
  before it runs"(Spatial 分裂上厘米级放置受限);技能进化 "does not read the existing skill text"。
- **Robo-Harness K1(2609.29389,未核实预印本)**:资产 = 感知即工具(标定深度、持久视觉锚点、
  空间测量、抓取假设),agent 查询后选择生成动作;偏部署期工具调用(非离线演化库)。
  **⚠️ 关键数字口径(勿误用)**:头条 **77.8%/88.9% 出自预算受限、类别配平的 18 例匹配子集**
  (K=1,N=8;Fig.1/Table 7 按 Spatial/Object/Goal/Average 分列:K1+Gemini 66.7/100/66.7→77.8;
  K1+Astra 83.3/100/83.3→88.9;RGB+Astra 33.3/83.3/66.7→61.1);**全量 180 例 Gemini+K1=139/180=77.2%**
  (子集与全量差 0.56pp,作者自陈为一致性检验)。自陈局限:抓取假设"does not execute a grasp or
  certify feasibility";缩放工具"does not move a camera or reveal an occluded surface";"API budget
  constraints limit Astra"(故用匹配子集)。
- **BiGym 2.0(2610.07594,未核实预印本)**:见 §4 对撞层逐字核实。

### 2.3 路线⑤ venue 核实汇总

**已核实(外部权威源逐字)**:SayCan=CoRL 2022(OpenReview 7Ti96LhnF2);Inner Monologue=CoRL 2022
(OpenReview 3R3Pz5i0tye);Code as Policies=ICRA 2023(IEEE Xplore 10160591);ProgPrompt=ICRA 2023
(IEEE Xplore 10161317);PaLM-E=ICML 2023(PMLR v202/driess23a)。
**未核实(仅 arXiv 预印本,journal_ref=NONE、comment 无 venue)——共 19 篇**:WAA(2609.29964)、
K1(2609.29389)、RAPID(2609.30249)、RACaP(2609.29394)、DexAgent(2609.35318)、RHD(2609.33378)、
AdaHVLA(2609.29204)、Coding-Agents-TAMP(2609.30233)、Harness VLA(2607.08448)、Scale-and-Selection(2609.39304)、
COAP(2610.12369)、PhysEvo(2610.08995)、EmbodiedRSI(2610.10498)、AR-WAM(2609.23578)、Encore(2609.37359)、
BiGym 2.0(2610.07594)、LIBERO-Agent(2609.39507)、RoboDojo(2607.04434)、DREAM(2608.29078)。
**如实标注:2025-2026 agentic 前沿几乎全为预印本,venue 无从核实,不编造会议名。**

### 2.4 路线⑤演进 / 分歧 / 开放问题

- **演进**:LLM 做高层规划/接地(SayCan/CaP,2022-23,资产=技能+价值/生成代码,运行时生成)→
  **把编码移到演化期、部署期调冻结资产**(WAA/K1/RACaP/RHD,2025-26,⑤b 核心创新)→
  **harness 包冻结策略的组合形态**(Harness VLA/COAP/PhysEvo/Encore,2026,⑤c,主流=包裹非取代)→
  **预算配平对撞评测**(BiGym 2.0,2026,⑤e)。
- **分歧**:①资产形态(程序 vs 技能库 vs 工具接口 vs playbook vs 协调策略代码,尚无收敛);
  ②取代 vs 包裹(COAP 纯代码运行时不查 VLM vs 主流包裹冻结 VLA;BiGym 2.0 证实无单一赢家);
  ③编码发生在何时(CaP 运行时生成有延迟 vs RACaP/WAA 演化期生成部署冻结);④LLM 可靠性
  (LIBERO-Agent 逐字 reliability gap + cross-stage interference)。
- **开放问题(带证据)**:
  1. **资产质量无评测口径(关键缺口)**:复用率/跨任务迁移率无标准。**证据**:BiGym 2.0 明确只做
     "cold-start policy synthesis **per task**",把 "cumulative skill reuse" 列为 future work;
     WAA 冻结技能库却只报任务成功率、不报复用率。**连唯一对撞基准都未度量"资产复用"本身。**
  2. **agentic↔策略共享榜受控缺席 + 同基准口径分裂**:RoboDojo 30 策略同表、最佳仅 8.80%,
     **全文 0 处 agentic**;PhysEvo 自报同 42 任务 62.00% 但口径不同(per-task retained deployment
     versions + held-out-layout + 五维等权),**62/8.80≈7× 口径分裂,不可直接同表比较**。
  3. **长程失败恢复刚起步**:BiGym 2.0 "cross-workspace stacking, which neither method solves in
     more than 1% of episodes";K1 抓取假设不认证可行性;WAA 动作不可预演/不可逆;RHD playbook
     专攻失败干预(37.3→64.0)属早期。

---

## §3 ID 与 venue 更正(Phase 2 补核结果)

| 项 | Phase 1/先前的记录 | Phase 2 核实更正 | 依据 |
|---|---|---|---|
| **双臂 one-shot** | 记为 ICRA 2024(Wang & Johns [48]) | **= ODIL(2503.06831),ICRA 2025** | arXiv comment 逐字 "Accepted at ICRA 2025" |
| **VINN** | ID 不确定 | **= 2112.01511(RSS 2022)**,正题《The Surprising Effectiveness of Representation Learning for Visual Imitation》,VINN 是其最近邻方法 | Crossref 10.15607/rss.2022.xviii.010 + Mobile ALOHA ref[63] 逐字 |
| **TP-Flow** | ID 不确定 | **= 2609.27780**(Task-Prototype Guided Flow Matching),venue 未核实(匿名评审中) | arXiv API 标题检索;摘要数字与既有锚点逐字一致 |
| **PaLM-E** | 未列 ID | **= 2303.03378,ICML 2023** | PMLR v202/driess23a |
| **Res-HIL** | 归入路线④(少样本结构化) | **= 2609.30023,但性质是人在环残差 RL(冻结模仿策略上学纠正动作),非检索/结构先验;路线④归属存疑,建议移出或标"少样本+在线 RL 混合"** | 子 agent 摘要核实;"20 演示+10min"未在摘要核到 |

**⚠️ 这些更正须回流**:骨干图谱 v0.1 §3.4/§3.5 与四透镜分图(若引用了 Res-HIL 归④、
双臂 one-shot=ICRA 2024)须按本表更正。**Res-HIL 的路线归属变更属判断,置信度中**
(子 agent 据摘要判定其为残差 RL;若分图①已把 Res-HIL 作"少样本结构化"代表,须复核)。

---

## §4 对撞层证据(逐字核实;直接支撑骨干图谱对撞层节点 + 综述/立场文章重审)

### 4.1 BiGym 2.0(2610.07594)确做了"同预算/同观测/同控制器"对撞——逐字句

- **同预算 + 四方法**:"We benchmark vision-language-action fine-tuning, imitation learning,
  demo-driven reinforcement learning, and cold-start coding agents **given the interaction budget
  of online reinforcement learning**."
- **同观测 + 同控制器**:"**With the same onboard views, proprioception and whole-body controller
  for every method**, vision-language-action fine-tuning has the highest nine-task mean, and
  agent-developed programs outperform every demo-driven reinforcement learning baseline on this
  mean and lead on bimanual reaching."
- **接口配平**:"auditing coding agents (GPT-6 Astra and Claude Opus 5.5) under **matched observation
  and action interfaces (84×84 views, direct joint control, no IK tools)**."
- **按任务分裂、无单一赢家**(结论章 + Table II 九任务):"π₀.₅ has the highest nine-task mean, above
  imitation learning and both coding agents. Both coding agents still beat every demo-driven RL mean
  and rank alongside imitation learning. Opus leads multi-modal reaching. On dual reaching, both coding
  agents stay above every learned policy." 共同失败:"cross-workspace stacking, which neither method
  solves in more than 1% of episodes."
- **自陈局限**:"Both agent interfaces are cold-start";"a cold-start reference rather than the ceiling
  of agent development";cumulative skill reuse 留作 future work。

**判断(置信度高)**:BiGym 2.0 是检索到的**唯一一张真条件表**,其存在条件正是"同预算/同观测/
同控制器对撞"——**直接实证委托人 2026-10-13 裁决"保留一个对撞层作为条件表兜底"的必要性**。

### 4.2 RoboDojo(2607.04434)agentic 缺席核实

对 **182,457 字全文**(保留 math alttext)grep:**"agentic"=0、"agent"=0(不区分大小写)、
"harness"=0**;而 "RoboDojo" 出现 403 次(证内容完整)。其 30 策略、5 维
(Generalization/Memory/Long-Horizon/Precision/Open)、42 仿真+18 真机任务、公开榜(最佳 8.80%)
**不含任何 agentic/coding-agent 条目**。**结论:RoboDojo 榜单 agentic 缺席属实,证据为全文零命中。**

**§4 综合**:端到端↔分层已在 RoboDojo/RoboCasa365 共享榜硬对撞;**真正缺席的是 agentic↔策略**,
且在同基准出现 ≈7× 口径分裂(PhysEvo 62% vs RoboDojo 8.80%)。**这逐字支撑骨干图谱 §6 分歧一
与综述/立场文章"对撞缺席"的分层重写(端到端↔分层已对撞;agentic↔策略缺席)。**

---

## §5 口径警告(引用红线;守 P-004 数字并列守则)

1. **K1 的 77.8%/88.9% 是 18 例匹配子集,全量是 77.2%**——引用须标"匹配子集"口径,
   不得把 77.8/88.9 当全量成绩,也不得与 WAA 75.6%(全量均值)直接并列。
2. **PhysEvo 62% 与 RoboDojo 官方 8.80% 非同口径**(per-task retained deployment + held-out-layout +
   五维等权 vs 单泛化策略榜),**≈7× 分裂,严禁直接对撞或并列**;若引用须各自标完整口径。
3. **BiGym 2.0 只测 cold-start per-task,未测累积复用**——不得据 BiGym 2.0 断言"资产复用已被度量"。
4. **WAA 75.6% 限定"技能仅从 LIBERO-90 演化、评测前冻结"**——引用须带此限定。
5. **Res-HIL 不属路线④**(残差 RL),若分图①已归入须复核更正。

---

## §6 残余不确定性与诚实标注

- **全文级 vs 摘要级**:路线④读全文 6 篇(One-Shot IL(Vitiello)/MT3/FlowRetrieval/BPC/RDR/DP),摘要级 12 篇;
  路线⑤读全文 9 篇(SayCan/CaP/WAA/K1/BiGym 2.0/RoboDojo/PhysEvo/RACaP/RHD),摘要级 15 篇。
  **摘要级篇目的内部表格/局限未核**,数字多来自摘要。
- **venue 未核实**:路线④ 8 篇、路线⑤ 19 篇(均 2025-2026 预印本),已如实标,未编造。
- **可能漏查(子 agent 诚实标注)**:
  - 路线④:其他任务分解工作(RT-H 层级、语言驱动分解)未纳入 ④d;互联网规模演示检索(RoboTok)、
    移动操作检索(ReMoBot)未纳入 ④c;半参数/kNN 策略谱系(SEMPER 等)可能不全;
    未逐条核 MT3 参考文献是否真把 ODIL 引为 [48](未读其 ref list)。
  - 路线⑤:**skill-library 经典前驱未纳入**(Voyager/CaP-X/Playful——WAA 正文引 CaP-X、Playful
    作对照,可补为 ⑤b 谱系上游);TAMP+LLM 程序合成除 Coding-Agents-TAMP 外或有同期工作;
    ⑤d 与⑤c 高度重叠(DREAM 类按跨支处理);未做 WebSearch 广域补新(仅 venue 核实),
    2026-10 最新预印本可能有遗漏。
- **本件未做**:权威性检验(≥3 处跨源口径定案)、会签前自查复核(独立子任务 + 外部交叉源)。
  **故 v0.1 不签发**;签发前须补这两项(候选定案:DROID 84/86、OXE 21/34、LIBERO-Pro 总任务数、
  OpenViTac 53.3/48.5 vs Table 2/3、K1 子集 vs 全量口径)。
- **模型名照录**:原文出现 GPT-6 Astra、Claude Opus 5.5、Gemini 3.7 Flash、GPT-5.5/5.6、π₀.₅、
  Qwen3-VL-8B 等,均逐字忠于原文,未改。

---

## ✏️ 2026-10-15 权威性检验回流更正(STRAP 张冠李戴)

- **错在哪**:本件路线④多处把 arXiv:2310.12077 标注为「STRAP(CoRL 2023)」,并把它作为
  「STRAP→MT3 谱系 / MT3 同门前身 / 规模化版」的起点。经核,**2310.12077 不是 STRAP**——
  张冠李戴(名字错,ID / venue / 所述内容均属实)。
- **核实依据(主会话 2026-10-15 独立 curl arXiv)**:
  - **2310.12077** =《One-Shot Imitation Learning: A Pose Estimation Perspective》,作者
    **Vitiello, Pietro / Dreczkowski, Kamil / Johns, Edward**,2023-10-18,**CoRL 2023,
    PMLR 229:943-970**。所述内容(one-shot IL、位姿估计视角、Sawyer、~1500 rollouts、
    平均超 DOME ~22%、§5 四条局限)都属实,**只有「STRAP」这个名字是错的**。
  - **2412.15182** =《STRAP: Robot Sub-Trajectory Retrieval for Augmented Policy Learning》,
    作者 **Memmel / Berg / Chen / Gupta / Francis**,2024-12-19,**venue = ICLR 2025 Poster**
    (OpenReview 4VHiptx7xe)——**这才是真正的 STRAP**。(注:「STRAP 为 RSS 2024」一说无出处,不予断言。)
- **本件处理方式**:凡「STRAP」指向 2310.12077 处,一律改名为「One-Shot IL(Vitiello et al.,
  CoRL 2023)」或其全称,ID / venue / 内容保留不变(**约 9 处**:④b 小标题谱系、④b 代表作条
  (含「STRAP 平均超 DOME 22%」改为「该文平均超 DOME 22%」)、④b 张力条、§1.2 全文锚点卡、
  §1.3 venue 核实、§1.4 演进条、§1.4 分歧⑤、§6 全文级清单)。本件未出现指向真 STRAP
  (2412.15182)的条目;§1.2 中「FlowRetrieval / BPC / RDR」等其他全文卡与此无关,未改动。
- **谱系表述降级为待核**:原「STRAP→MT3 谱系 / 同门前身 / 规模化版」建立在误标之上。
  **已核实、可保留的**是:MT3(2511.10110)的位姿估计对齐步骤引用 Vitiello et al.(2310.12077)
  作上游。**未核实、已就地标 ⚠️ 待核的是**:「同门 / 规模化版」这一更强表述(见 ④b 代表作条
  末的 ⚠️ 待核注)——须对 MT3 全文重新核实二者关系,不得再作既定事实断言。

---

## 署名链

- **起草**:Dexter(2026-10-13,主会话汇总 + 2 路异路径子 agent 全文级深挖)。
- **性质**:综述级文献地图 **Phase 2 深挖件**(路线④⑤),黄色产物草稿。
- **状态**:**v0.1 草稿,未走会签前自查复核、未签发、不入 `final/`、不署名/不投稿/不发布/不对外**。
- **下一步**:①其余五路线(①②③⑥⑦)深挖排后续轮;②权威性检验(≥3 处跨源定案);
  ③会签前自查复核(独立子任务 + 外部交叉源)→ 与骨干图谱合并签发 v1.0;
  ④§3 更正回流骨干图谱 v0.1 与四透镜分图(Res-HIL 归属 / 双臂 one-shot venue / VINN·TP-Flow·PaLM-E ID)。
- **复核**:______(待会签前自查复核)
- **签发**:______(未签发)
