# 争论账本(闲时菜单 C1)

> 路线之争的正反证据账本。只记**已核实**来源(abs 页/官方页/论文原文),
> 每条注明出处与日期;结论性判断标"这是判断"并给置信度。新证据随雷达追加。
> 建立:2026-09-28。

## 账本一:端到端 VLA vs 分层/双系统 vs Agentic 程序合成

- [端到端] RT-X / OXE(arXiv:2310.08864):跨本体聚合 1M+ 轨迹训练
  端到端模型(RT-1-X/RT-2-X 55B),规模化是路径本身。(卡片库,
  2026-09-28)
- [分层/双系统] LiMA(arXiv:2609.28431):慢系统长程意图 + 快系统高频
  运动精修,Latent Schrödinger Bridge 耦合,推理延迟较 Cosmos-Policy
  降 45.8%;六项双臂灵巧任务 70.8%。(2026-09-27)
- [分层/双系统] Rolling-WAM(arXiv:2609.30247):World Action Model
  滚动去噪,滑窗错峰噪声级,4.5× 重规划提速;LIBERO/RoboTwin/Unitree G1
  真机。(2026-09-28,abs 页)
- [Agentic] WAA(arXiv:2609.29964):VLM 多智能体 + 动作排练工作区,
  LIBERO-Pro 75.6% SOTA;轨迹蒸馏给 Qwen3.5-9B,域外 1.7%→43.3%。
  (2026-09-28,abs 页)
- [Agentic] Robo-Harness K1(arXiv:2609.29389):感知做成 VLM 可调用工具,
  LIBERO-Pro 77.8%(Gemini 3.7 Flash)/88.9%(Astra);107 教师轨迹蒸馏
  学生 44.2% vs OpenVLA 30.2%。(2026-09-28,abs 页)
- [Agentic] RAPID(arXiv:2609.30249):单条视觉人演 → 编码代理循环生成/
  验证/精修机器人程序,8 项接触富集非抓取任务 + LIBERO-Pro,真机 Franka;
  MIT 组(Mao/Kaelbling/Lozano-Pérez)。(2026-09-28,abs 页)
- [端到端] GAM / Grounded Action Model: 3D Grounding as a Foundation for
  Robotics(arXiv:2609.23863,2026-09-20):以 3D grounding 为基底的
  机器人基础模型范式,LIBERO-Pro 均值 **61%**(基线 π0.5 53%),
  16 扰动设定;另 RoboTwin 2.0 55.3%。(2026-09-28 子任务核实 +
  主会话 abs 页复核一致,置信度高)
  - 续班补全(abs 页 2026-09-28,置信度高):RoboTwin 2.0 **55.3% vs
    Spatial Forcing 52.0%**,场景随机化下 47.6% vs Abot-M0 30.4%
    (策略仅用干净场景演示训练);**真机**:双臂 YAM 视觉漂移下
    **17/20 vs π0.5 4/20**,与 Molmo2 规划器组合在 Franka 上长程
    **ID 64.7% / OOD 49.8%** 步完成率。可作高层规划器下的低层控制器
    ——即"端到端基底 + 可组合"的中间形态,不纯属任一极。
  - 机构补核(GitHub README 作者上标逐字,2026-09-28):NWU ×2(Zhang、
    Yiyan Peng)、UW ×2(Weikai Huang、Ranjay Krishna)、NUS ×2
    (Shailesh、Jiafei Duan)——abs 页未显示机构,此为本轮补核,置信度高。
  - 代码状态(GitHub API 核实,2026-09-28):**未放出**——仓库
    GehaoZhang6/Grounded-Action-Model(★26,建仓 09-22,末推 09-25)
    根目录仅 README.md + assets/,README 明写 "Code coming soon"
    (训练/推理代码、预训练权重、真机 setup 待放)。转滚动盯仓。
- [端到端·改进] 2606.27663:GR00T-N1.6/π0.5 上加 3D 点注入 MLP 模块,
  任务扰动 31.2→77.5 分、位置扰动 28.1→60.2 分。(2026-09-28 主会话 abs 页复核一致,置信度高)
  ✏️ **2026-10-09 轴标更正**:两数即 **LIBERO-PRO 平均成功率**(原文 "average success rate",
  "points" = 百分点单位),**不是「扰动分」这种独立分数轴**;v2(2026-10-01)另增真机实验
  表述 + `comment` = "Accepted at CoRL 2026"(单源)。详见本账本下方「观察 v2 更正之再更正」。
- [端到端·改进] SynthDemo-RL(arXiv:2609.21650):LIBERO-PRO Position/
  Task 轴 **97.8%/97.1%**(已入账本二,此处补账本一)。(双源一致:
  API feed + 子任务 abs 核实,置信度高)
- [Agentic·补充] RACaP(arXiv:2609.29394,2026-09-24):ReAct 调冻结
  策略 API,LIBERO-Pro 零样本 45.0%。(2026-09-28 主会话 abs 页复核一致,置信度高)
- [Agentic·harness] AdaHVLA(arXiv:2609.29204,2026-09-24):把"任务
  harness"(代码化协调策略)经机器人经验自适应精修——解耦多智能体适配
  把证据分析/修订/行为评估分置于不同工作上下文,有状态修订图保留备选
  harness 与适配记忆;NaVILA-LH 平均测试成功率 **22.5%→57.5%**,三个
  VLA 主干上操作测试成功率较初始 harness 最高 **+30.8 个百分点**,
  含真机分阶段执行。(续班 abs 页 2026-09-28,置信度高)
- [Agentic·分层] ADM-Planner(arXiv:2609.29212,2026-09-24):LLM 引导
  长程规划 + 注意力增强动态记忆——持久工作区知识与物体级状态分离、
  有界检索器只暴露影响下一步决策的条目、失效即重规划;1,500 回合仿真
  **100% vs 静态记忆 62%**,上下文规模代理较未过滤动态记忆降 **95.8%**;
  60 试 PyBullet 100% vs 50%;室内外**移动操作**真机。(续班 abs 页
  2026-09-28,置信度高)——注意:场景是移动操作,非灵巧手。
- [Agentic·程序合成] Coding Agents for TAMP(arXiv:2609.30233,
  2026-09-24):编码代理在固定预算内合成跨实例泛化程序;Claude Code
  (Opus 5)与 Codex(GPT-5.6 Sol / GPT-6 Astra)在 28 个 KinDER/
  PDDLStream 环境、980 个程序 × 100 保留实例 = **98,000 回合**;均值
  成功 **56%–95% vs 手写规划器 47%**(16 个有规划器可用的环境),对象
  数增大时维持更高成功率且每实例算力低一个数量级;开源全部代码与提示。
  (续班 abs 页 2026-09-28,置信度高)
- **观察 v2(这是判断,置信度中→高)**:2026-09-28 并行子任务打开
  12 个 abs 页后修正本账本:端到端阵营**并非未报 LIBERO-Pro**——数字
  存在且不弱(97.8 / 61 / 77.5),但全部落在"VLA 内部改进"轴(数据/
  接地/微调/RL/执行层),9 篇摘要无一与 agentic 三篇同表对撞。原
  "主战场"表述**降格为:同基准、未对撞**——对撞缺席本身是发现。
  π0.5 被多篇用作共同基线(53%),可作两阵营数字换算锚点。局限:
  arXiv all: 只索元数据,正文报 LIBERO-Pro 而摘要不提的工作会漏检。
- ⚠️ **观察 v2 更正(2026-09-29,透镜③起草+独立复核时发现)**:v2 括注的
  "端到端数字不弱(97.8 / 61 / 77.5)"**口径混装**——**97.8 是
  SynthDemo-RL 的 LIBERO-PRO 轴成绩(见账本二),与 LIBERO-Pro 成功率
  不同源**;**77.5 是 2606.27663 的"扰动分",非成功率**。三者**不同轴,
  不应并列**。**同轴可并列的仅**:GAM LIBERO-Pro 16 扰动设定 **61%
  vs π0.5 53%**、GAM RoboTwin 2.0 五十任务 **55.3% vs Spatial Forcing
  52.0%**(均为成功率)。观察 v2 的**结论(未对撞)不变**,但引用的数字
  须按此更正。(录 `honor.md` 2026-09-29 条)
- ⚠️⚠️ **观察 v2 更正之再更正(2026-10-09 19:5x,透镜③逾期体检;append-only,上条原文不删)**:
  上条内**「77.5 是 2606.27663 的『扰动分』,非成功率」「三者不同轴」两处定性系误读原文**,
  现更正如下——
  1. **原文证据(外部/原始来源,主会话独立 curl 实抓双版本)**:arXiv:2606.27663 的
     **v1(2026-06-26,http=200 / 44,280 字节)与 v2(2026-10-01,http=200 / 43,222 字节)**
     摘要均作 "On LIBERO-PRO, our method improves the **average success rate** of
     GR00T-N1.6 from 31.2 to 77.5 under task perturbation and from 28.1 to 60.2 under
     position perturbation"(v1 另有 "(gains of 46.3 and 32.1 points)" 与 "points" 单位,
     v2 删去)。**即 77.5 与 60.2 就是 LIBERO-PRO 平均成功率**(骨干 GR00T-N1.6),
     **"points" 是百分点单位,不是另一种分数轴**。
  2. **更正后的正确定性**:97.8(SynthDemo-RL,LIBERO-PRO **Position 轴**)、61(GAM,
     LIBERO-Pro **16 扰动设定均值**)、77.5(2606.27663,LIBERO-PRO **task perturbation
     单项**)**三者同为「LIBERO-Pro 家族成功率」= 同轴**,但**分属三种不同扰动协议/设定、
     三种不同骨干**,故**仍不可直接并列**——**「口径混装、不应并列」的指认与处置成立,
     「不同轴」的定性改为「同轴、不同设定/不同骨干」**。
  3. **须与真正的同号冲突严格区分**:2610.10526 的 **97.8**(π0.5 + LIBERO **非 Pro**
     in-finetune)与 SynthDemo-RL 的 **97.8**(LIBERO-PRO Position 轴)才是**同号不同源**;
     2610.10526 的 **61**(π0 措辞**摆动幅度**)与 GAM 的 **61%**(**成功率**)才是
     **同号不同轴**。**这两组隔离零改动、继续有效。**
  4. **观察 v2 的结论(「同基准、未对撞」)不变,且证据被加强**:更正后 LIBERO-Pro 上的
     可比数字由「四数三设定」变为「**五数四设定**」(新增 77.5),**「评测口径不统一」
     与「对撞缺席」两条判断的证据更强**。
  5. **⚠️ 本条错误的扩散范围(诚实登记)**:该误读自 2026-09-29 分图③复核记录起,经
     **总图 v1.1 更正框 → 本账本 → 综述 §4.1.2/§4.3.2/§5.1/附录 A.1·A.2 → 立场文章 §4
     守则框**层层复用达 **5 件已签发产物**;分图① 分歧 1 的三元组更**从未同步 09-30 更正**
     (另一处 live stale)。**这是宪法「自审签发与滚动重审」第 4 点所警惕的本地库自我确认
     循环的实例**——期间任何一次「本地互证」都只会互相确认,**只有外部原文级体检能打破**。
     2026-10-09 已逐件 append-only 更正(总图 **v1.1.1** / 分图① **v1.0.1** /
     分图③ **v1.1.1** / 综述 **v1.0.2** / 立场文章 **v1.0.2**)。录 `honor.md` 2026-10-09 条。
  6. **根因**:2026-09-29 复核时把 v1 摘要的 "points" 读成「另一种分数轴」,且**未回原文
     复核该归因**即写入复核记录 → 后续各件**引用的是本所的轴标结论,而不是原文**。
     **预防(已写入立场文章脆弱点⑧ 与分图③ 脆弱点④⑤)**:**任何「轴标」断言
     (某数是成绩 / 幅度 / 分数 / 增量)必须附原文逐字引句,不得只写结论**——轴标是本所
     自赋的解释,不是原文标签。
  7. **⚠️ 使用政策未放宽(升级门)**:更正后 77.5 在技术上已是「同轴但不同协议/骨干的
     LIBERO-PRO 成功率」,**是否允许日后带完整口径标签把它作为端到端阵营数据点引用**,
     属**高风险锚点数字升级门**,**已提请委托人裁决**(`goals.md` 待裁段 🟡);
     **本轮各件一律维持「不并列、不作为数据引用」的更严格处置——只更正理由,不放宽使用。**
  8. **顺带新登记事实(单源,置信度中)**:2606.27663 **v2 的 `arxiv:comment` =
     "Accepted at CoRL 2026"**、摘要新增 "We further validate the practical applicability
     with **real-world experiments**."、"backbone-agnostic" 收紧为 "backbone-agnostic
     across VLAs with **diffusion-based action heads**";篇名定案 = *Direct Action-Head
     Injection of A Grounded 3D Point Unlocks Spatial and Task Generalization*(Tsai 等)。
     **CoRL 接收仅据 arXiv comment 字段,未核官方名单。**
  9. **同批体检另登记(与 77.5 无关,但属账本一语料状态)**:分图③ 的 24 篇中
     **4 篇在 2026-09-29 后出 v2**——2609.30247 Rolling-WAM(v2 2026-10-05)、
     2609.35318 DexAgent(v2 2026-10-02)、2609.34911 Action Upcycling(v2 2026-09-29T05:34Z)、
     2606.27663(v2 2026-10-01);**逐条 v1↔v2 摘要 diff:前三篇被引数字与表述逐字未变,
     2606.27663 摘要重写但被引四数未变** → **无口径漂移,账本一相关条目无需改写**。
     **24/24 编号今日仍解析、标题逐条吻合、0 撤回。**
- **观察 v3(这是判断,置信度中→高,2026-09-29 透镜③)**:路线 C(agentic)
  内部正形成**新分工线**——不是"agent 直接控机器人",而是"**agent 生产
  可复用的中间资产**":WAA 演化技能库、K1 造工具接口、RAPID 造程序、
  DexAgent 造技能+验证器、Recursive Harness Distillation 造 playbook。
  五件的共同点是"**资产**"而非"**动作**"——产出物从"这一回合怎么做"
  变成"以后都这么做"。**但"资产质量"目前无度量**(无复用率/跨任务迁移率),
  是新提出的缺口。
- ⚠️ **方法论警告(2026-09-29,透镜③,arXiv:2609.34684)**:VLA 内部表征
  **自然轨迹上解码准确率高,可与"受控目标态响应弱"并存**;须把
  **预测准确率 / 目标态响应性 / 上下文稳定性**三者分开评估,**互不替代**。
  → 对读一切"VLA 理解状态"类结论的通用警告。
- **[端到端·脆弱性 + agentic·规则资产] 2610.10526(Rephrase Before You Act;2026-10-09 雷达锚点,curl 实抓 abs 页 http=200 逐句核对)**:
  ①**端到端语言脆弱性新证据**——VLA **不继承**其所基于 VLM 的语言鲁棒性;一个词的改动移动成功率数十点(π0.5 对 "switch on the stove" 100% 开灶、对 "switch on the hot plate" 2%;π0 rephrase 增强微调 checkpoint 仍摆动达 61 点);②**"规则作为语言侧资产"新形态**——把敏感性表达为显式规则(LLM 把多措辞证据蒸馏成 10-20 条改写规则,部署时对每条指令改写一次),**免重训、免逐步验证、零样本适用**,冻结 π0 在 12 个 held-out 任务相对提升 16-27%,π0.5+LIBERO in-finetune 93.6%→97.8%;③**呼应观察 v3**:规则是"语言侧的可复用资产"(对应 v3 的"agent 生产可复用中间资产",但资产形态是改写规则而非技能/工具/程序)。
  **⚠️ 口径警示**:本件 97.8/61 与账本内同号数字**不同轴**(97.8=π0.5+LIBERO in-finetune,非 SynthDemo-RL LIBERO-PRO 轴;61=π0 措辞摆动幅度,非 GAM LIBERO-Pro 成功率),严禁并列(详见分图③ v1.1 分歧 4「同号不同轴警示」+ P-004 守则)。
  **对账本一的意义(这是判断,置信度中)**:为"端到端 vs agentic"提供**新对撞维度**——端到端把语言压进权重导致措辞脆弱,轻量规则改写(免训练)可缓解,暗示"语言鲁棒性"可能是端到端路线的系统性短板、agentic/程序化(规则外化)是补位;**但本件仍是"端到端内部改进 + 轻量规则",非完整 agentic harness,同基准对撞仍缺席**(承观察 v2/v3 结论不变)。

- **[观察 v4 · 「对撞缺席」分层更正] 2026-10-14 证据触发重审(承委托人 2026-10-13 16:1x 裁决「殊途同归 + 一个对撞层兜底」;append-only,观察 v2/v3 原文不删)**:2026-10-13 批判性核查(委托人指令「拿事实说话、重新审核」)检索到跨范式对撞基建集群,经**主会话独立 curl 复验**(守 P-010,不轻信子 agent)——BiGym 2.0(arXiv:2610.07594v2,全文 1,333,060 字节,grep 逐字命中「interaction budget of online reinforcement learning」「same onboard views...whole-body controller for every method」「matched observation and action interfaces」「cumulative skill reuse」)+ RoboDojo(arXiv:2607.04434v3,全文 180,322 字,grep「agentic/agent/harness/coding agent/vlm」全 0、「robodojo」=218、「policy」=189 证内容完整)。**对观察 v2/v3「三派同基准未对撞」的分层更正**:
  1. **端到端 ↔ 分层:已硬对撞**——RoboDojo 30 策略同表(π0/π0.5/OpenVLA-OFT/ACT/SmolVLA/GO-1 与 Spatial Forcing/X-WAM/Fast-WAM/GR00T-N1.7)、RoboCasa365 官方榜 18 模型、RoboTwin-Phys「WAMs and VLAs 鲁棒性差」。**观察 v2/v3「未对撞」在此腿被证伪。**
  2. **agentic ↔ 策略:非「全称缺席」,而是「共享榜缺席 + 孤立基准已有 + 自报口径分裂」**——① BiGym 2.0 **确做了**预算配平的 VLA/IL/demo-RL/**coding-agents** 对撞(同观测/同控制器/同预算,结论「按任务分裂、无单一赢家」,π0.5 九任务均值最高、coding agents 胜所有 demo-driven RL、cross-workspace stacking 三路 <1%),**故「agentic 从未被对撞」不成立**;② 但 agentic 在**共享榜**(RoboDojo/RoboCasa365)**缺席**(全文 grep=0);③ agentic 自报数有 **5-8 倍口径分裂**(PhysEvo 自称 RoboDojo 同 42 任务 62.00% vs 官方榜 8.80%;EmbodiedRSI 自称 RoboCasa365 77.0% vs 官方 64.4)——**不对撞不仅拼不出真表,还生产假表**。
  3. **核心主张「对撞缺席 = 度量缺口」幸存且被加强**——BiGym 2.0(唯一真对撞)**只做 per-task cold-start 合成、把「cumulative skill reuse」列为 future work**;WAA 冻结技能库却只报任务成功率不报复用率:**连唯一的预算配平对撞都未度量「资产复用」本身** → 立场文章「资产质量度量缺口」主张被强化。
  **净定案**:账本一核心裁决由「三派同基准未对撞(全称)」**分层重写**为「**端到端↔分层已对撞;agentic↔策略共享榜缺席、孤立基准(BiGym 2.0)已有但自报口径分裂;资产复用度量仍缺**」;「对撞缺席本身是发现」在 **agentic↔策略 + 资产复用度量**层面仍成立,在**端到端↔分层**层面不再成立;「最该做的增量是更诚实的对撞」被**更强支持**(2025-06 后对撞基建 vla-eval/RoboArena/RoboDojo/LIBERO-PRO/BiGym 2.0 全拿顶会与公共治理位)。**根因教训**:观察 v2 的「未对撞」系**摘要级 + arXiv `all:` 元数据检索**结论(账本一/综述 §2.2 已自陈此局限),未及检索 2025-06 后井喷的对撞基建——**这正是「缺席证据(argument from absence)」的固有风险:「未观察到」可能只是「未检索到」;缺席证据须随检索面扩大而重审**。**联动**:综述 v1.0.2→**v1.0.3** + 立场文章 v1.0.2→**v1.0.3**(均 append-only 分层重写,核心主张零改动/被加强)+ review-ledger 销账(部分:综述/立场文章已改,**透镜③分图 v1.1.1/总图 v1.1.1 仍带旧全称断言,待续下一轮**)+ decisions.md 2026-10-13 裁决条。**未外流**(综述/立场文章均不署名/不投稿/不对外)。

## 账本二:真机数据 vs 合成数据

- [真机规模化] DROID(arXiv:2403.12945):76k 轨迹/350h/564 场景,
  标准化低成本 rig 分布式采集。(卡片库,2026-09-28)
- [真机规模化] AgiBot World(arXiv:2503.06669):100 台机器人/103 万条
  轨迹/43.8TB,含触觉与 6-DoF 灵巧手。(卡片库,2026-09-28)
- [合成] MimicGen(arXiv:2310.17596):<200 条人演 → 50k+ 生成,18 任务,
  跨本体。(卡片库,2026-09-28)
- [合成] DexMimicGen(arXiv:2410.24185):60 条人演 → 20k+ 双臂灵巧演示,
  BC 69.3-97.3%;Real2Sim2Real。(卡片库,2026-09-28)
- [合成] SynthDemo-RL(arXiv:2609.21650):LLM 引导合成演示破 VLA 零奖励
  屏障,LIBERO-PRO 27 个零成功任务全救活(直接 PPO 仅 10)。(2026-09-27)
- [合成] Real-to-Sim-to-Real(arXiv:2609.18293):重建资产免遥操作生成
  合成演示,零样本部署。(2026-09-27)
- **观察(这是判断,置信度中)**:合成路线的量级(60→20k)已能覆盖
  双臂灵巧;争论焦点正从"能不能生成"移向"生成数据的分布覆盖与真实
  接触物理差距"——需要找受控对比实验(同策略同预算下真机 vs 合成),
  账本缺口二。
- [合成·高保真] PhyVisGen(2609.25653):IPC 臂-夹爪耦合 + 路径追踪,
  纯合成演示训练的策略在 **5 项真机任务 65–95%**(无真机演示、无微调)。
  (2026-09-30,abs 页)
- [合成·动态] DynaForge(2609.25631):规划引导残差生成**动态**演示,
  九仿真任务生成成功率 **41.30%→78.37%**;DP3 用其数据 **49.11% vs
  DOMINO 7.07%**;真机 **30–60% vs 0–10%**。(2026-09-30,abs 页)
- [合成·免源轨迹] DEXTERA(2609.21045):**单张 RGB 图** → real2sim2real;
  sim-only 零样本,sim-real 共训 **29.2%→61.9%**。ZeroBot(2609.34010):
  **单视图 + 目标位姿**、零人演示/零预训练/零物体模型,**87% / 119 秒**。
  (2026-09-30,abs 页)——**合成门槛骤降**。
- [人演示·规模化] Ego2Robot(2608.02580):自中心人视频 → 机器人数据,
  **18,561 小时 / 15 本体**(自称最大 ego-to-robot);UMR(2609.34256):
  统一动作表示,**每任务 ~10 分钟人演示、无机器人演示**达 **91.7% vs
  HumanEgo 60.8%**。(2026-09-30,abs 页)——**per-task 够用 vs 规模化**之争。
- [语料工程] InternW0-Δ(2609.31394):异构语料(机器人 + UMI + 自中心
  人演示 + Ego2Robot)**>20K 小时**,自称最大开源语料;WB-WAM(2609.34199):
  **1,880.2 小时**部分标注视频与运动,HumanoidArena **81.9%** / 真机
  **84.0%**。(2026-09-30,abs 页)
- [翻新·反丢弃] **Kintsugi-VLA**(2609.31048):失败 rollout → 恢复数据,
  SmolVLA 恢复 **34.6%/38.4%**(较均匀采样 +5.8/+6.7pp);**ε4P**
  (2609.26672):翻新低精度 + 错配数据,**+31.7 个百分点**,可替换等量
  高质量数据仅降 **4.2 个百分点**。(2026-09-30,abs 页)——**"坏数据含信息"**。
- **观察 v2(这是判断,置信度中→高,2026-09-30 透镜④)**:账本二在
  2026-09-30 出现**两个新维度**,原"真机 vs 合成"二分已不够用:
  ①**"翻新"维度**——数据的价值不在"成功与否",而在"**噪声级 / 状态分布上的
  信息量**"(Kintsugi / ε4P);②**"语料"维度**——规模化从"数据集"抬到
  "**异构源对齐到统一表示**"(InternW0-Δ / WB-WAM)。**缺口二(同预算真机 vs
  合成受控对比)仍未填**,且现在**多了一个更难的问题:混合配比 + 翻新数据
  应如何共同优化**。

## 账本三:触觉的边际价值

- [正方] PROPRA(arXiv:2609.29822):指尖触觉+近觉按本体感觉段对齐做
  预训练,IL 成功率优于纯视觉与图像锚定基线。(2026-09-27)
- [正方] PolyUMI(arXiv:2609.29760):视-触-听采集平台,实验称触觉与
  音频揭示视觉之外的任务相关信息;RH20T 卡片:唯一含指尖触觉@200Hz
  的多模态大库(7 号构型)。(2026-09-27/28)
- [反方] Real-Time Force Regulation(arXiv:2609.30082):全手接触纯几何
  估计,不用触觉传感,真机 27-DoF 上实现抓取保持与恢复——"不用触觉"
  路线的正面证据。(2026-09-28,abs 页;注意其模拟为无重力设定)
- [受控对比·正方] **When Does Touch Matter?**(arXiv:2609.24068,
  2026-09-21):同一杂乱灵巧抓取任务族,固定演示/视觉/动作空间/柔顺
  控制,逐模态加减:组合 **24/25 vs 纯视觉 14/25**,三个狭窄条件
  **15/15 vs 6/15**;自称首个此类分离评估。(并行子任务核实
  2026-09-28,主会话未复核原文,置信度中)
- [正方·WAM 系] **DexTacWAM**(2609.24976):**六任务**均值 70.6 vs 最强基线
  38.0(22-DoF 双臂);去触觉世界建模 **四任务**均值 74.7→26.6。
  **VT-WAM**(2607.02503):**六任务**均值 **71.67%**,**较 Fast-WAM 高 26.67
  分**、较 OmniVTLA 高 35.84 分。**TacWAM**(2607.28391):**四任务**均值
  **75.0%**,较最强基线高 37.5 分;去触觉历史一致退化。
  (2026-09-28 逐条重开 abs 页复核,置信度高)
  - ⚠️ **更正(2026-09-28,重开 abs 页时发现)**:旧记"VT-WAM 71.67% vs
    Fast-WAM 26.67%"系**误读**——原文为 "outperforming Fast-WAM **by**
    26.67%",即**高出 26.67 分**,**不是** Fast-WAM 的成绩。另 DexTacWAM 的
    74.7→26.6 消融是**四任务**均值、与六任务主数 70.6 不同轴,旧记未区分。
    已改并录 `honor.md`。
- [正方内嵌反方] TACIT(2609.24507):TACIT 66.7/73.3 vs 纯视觉 DP3
  20.0/43.3;但输入匹配的 3D 视触融合仅 10.0/20.0——**naive 融合可
  拖累纯视觉基线**。(2026-09-28 主会话 abs 页复核一致,置信度高)
- [反方·绕开硬件] GIFT(2609.14173):无触觉硬件,电流残差估计力,
  力输入有无均 25/25 成功,差异只在握力中位 1.20N vs 2.55N。
  (2026-09-28 主会话 abs 页复核一致,置信度高)
- [触觉×合成] SBLR(2608.15897):免触觉仿真的触觉 Sim2Real(oracle
  触觉+潜空间对齐),零样本 85-97.5%,超物理触觉仿真基线 7.5-15 分
  (主会话 abs 页复核一致,置信度高);Tacchi 2.0(2503.09100):触觉
  仿真器路线存在(子任务核实,置信度中)。关键词检索 tactile+
  MimicGen 式演示生成 **零命中**——"触觉×演示合成"空白大体成立
  (检索级证据,非穷尽)。
- **观察 v2(这是判断,置信度中→高)**:缺口三已被 2609.24068 正面
  填上——同任务族、固定其余变量、逐模态加减,触觉的受控优势首次有
  实证;WAM 系三篇同架构消融再加三票。但反方未消失:naive 融合可
  负收益(TACIT)、特定任务可绕开触觉硬件(GIFT)。触觉×演示合成
  为空白,且 SBLR 显示部分工作在**主动绕开**触觉仿真——空白可能是
  选择而非无人问津。对委托人:2609.24068 的任务族设计是透镜②
  "受控增量"实验的方法论模板,建议列入精读候选。

---

## 图谱权威性检验定案(2026-10-15,领域级科研路径图谱签发前置;deep-read §3:≥3 处跨源定案引外部来源)

> 承 `具身智能领域级图谱-v0.1.md` §8.5 权威性检验(8 处定案)。本节登记其中**本轮新定案 4 处**
> (#1/#2/#6/#7);#3/#4/#5(DROID 86/OXE 21·60/LIBERO-Pro 未声明)已在账本一与综述 §5.4,
> #8(OpenViTac 53.3·48.5 vs Table 2·3)已在 `benchmark-openvitac.md`,此处交叉引用不重复。

- **#1 Isaac Gym venue 冲突 → 定案 = NeurIPS 2021 D&B Track(Round 2)**:Phase 1 子 agent 报 NeurIPS 2021
  D&B(S2+DBLP)vs Phase 2 ②③b 子 agent 报"未核实(arXiv comment 仅 tech report,Crossref 误配)"。
  **外部来源**:nips.cc 官方《NeurIPS 2021 D&B Accepted Papers》列表(作者 Makoviychuk...State 全匹配)+
  OpenReview id=`fgFBtYgJQX_`(venueid=NeurIPS.cc/2021/Track/Datasets_and_Benchmarks/Round2)。
  **定案(高置信)**:= NeurIPS 2021 D&B。**根因**:arXiv comment 仅 "tech report on isaac-gym"、无 journal_ref,
  单查 arXiv 会误判"未核实"。**教训已录 lessons.md:arXiv comment ≠ venue。**
- **#2 HumanPlus venue 冲突 → 定案 = CoRL 2024**:操作支路线③子 agent 报 CoRL 2024(GitHub+OpenReview)
  vs Phase 2 ③b 子 agent 报"未核实(Crossref 误配,comment 仅网站)"。**外部来源**:PMLR v270(CoRL 2024
  Munich)官方论文集 `fu25a`,pp.2828-2844 + 作者站 "Best Paper Award Finalist (top 6) at CoRL 2024"。
  **定案(高置信)**:= CoRL 2024。**根因**:arXiv comment 仅 "project website"。
- **#6 LIBERO-Pro 扰动维度内部口径不一 → 定案 = 4 正交维 + task 作第 5 类不参与交叉**:摘要/§4.1 写
  "四个正交维度(manipulated objects/initial states/task instructions/environments)"vs Figure 6 图注写
  "five perturbation types: object/configuration/instruction/task/environment"。**外部来源**:LIBERO-PRO
  (2510.03827v2)全文,Phase 2 ⑦ 子 agent 读全文核。**定案(中-高)**:= 4 正交维 + task 作第 5 类但
  **不参与自由交叉组合**;引用须说明此口径,不得径写"5 维"。**这是论文自身内部不一致,非跨论文分歧。**
- **#7 RoboArena episode 数两个口径 → 定案 = 600(成对 A/B)与 4284(累计采集)不可混用**:摘要">600 成对
  真机 episodes"vs 正文"4284 evaluation episodes"。**外部来源**:RoboArena(2506.18123v2)全文,Phase 2 ⑦
  子 agent 读全文核。**定案(高)**:= 600 是排名实验的成对 A/B 数,4284 是累计采集 episodes,**二者不同
  口径,严禁混用**(引"对撞规模"须明确是哪个)。

**方法论(承账本一/综述 §5.4)**:跨源分歧优先采论文正文口径;官方未声明者如实标"未声明";
**venue 须查官方论文集(nips.cc/PMLR/roboticsproceedings/IEEE/OpenReview/Crossref),不以 arXiv 无
journal_ref 推定"未核实"**;定案均引外部/原始来源,非本地库互证(守宪法"重审交叉源必须含外部来源")。
**关联**:8 处定案是领域级图谱系列(骨干 + Phase2 ④⑤/②③b/①⑤⑥⑦)**会签前自查复核 → 签发 v1.0** 的
权威性检验前置(deep-read §3),已满足"≥3 处跨源定案引外部来源"判据。

---

### 补充:N1–N7 新增定案(2026-10-15 Round 2 权威性检验)

> **来源件**:`reports/drafts/领域级图谱-权威性检验记录-v0.1.md` §2(定案全文 + 逐字引句)与 §0(抓取日志:
> **24 次 HTTP 200 `curl` 实抓**;DBLP 4 次请求 3 次 HTTP 202 + 1 次 HTTP 429,**未取得数据 → 交叉源缺位如实登记**)。
> **本节只补上面「图谱权威性检验定案」节所缺**:上文已登记 **#1/#2**(Isaac Gym / HumanPlus venue)与
> **#6/#7 的基础版**(LIBERO-Pro 扰动维度、RoboArena 两口径);此处 **N1/N2 是对 #6/#7 的细化与升级(只记新增
> 实质,不重复上文)**,**N3–N7 为全新定案**。骨干图谱 §8.5 表已由 8 处扩为 **12 处**(#9=N3 / #10=N5 /
> #11=N6 / #12=N7;**N4 未单列表行,已回流 Phase2-分支①⑤⑥⑦ §2.2 RoboArena 卡,表 #9 内附指引**)。
> **⚠️ 本轮权威性检验额外产出 2 处对既有 draft 结论的更正/证伪**:**N3 证伪** Phase2-分支①⑤⑥⑦ §2.3 的
> 全称断言「对撞层无一经同行评审正式发表」、**N7 更正** 同件 §1.2 的 MT3 ref [46] 归属(张冠李戴,已录 `honor.md`)。

- **N1 · LIBERO-PRO(2510.03827v2)扰动维度 —— 细化上文 #6,新增两条原文级细节**:
  ①**形式化记号自身即"声明四维、定义五算子"**——§4.1 写 `k∈{O,R,L,E}`(四个)却紧接枚举出**第五个算子**
  "Task perturbation ( `k=T` ) modifies the target object or action while remaining within the training
  distribution. The perturbed task is `T^(T)=(l,e,G^(T))`" → **`k=T` 是论文正式定义的算子(带自己的公式),
  不是图注口误**;Figure 6 图注逐字 "To ensure feasibility, **task perturbations are excluded from
  cross-type combinations**",§4.3 逐字 "To avoid infeasible combinations, **task-level perturbations are
  excluded from cross-type compositions**"。②**"四维"的具体命名在论文内有四种措辞**(摘要 "manipulated
  objects / initial states / task instructions / environments";§4.1 "object attributes / initial spatial
  configurations / task instructions / environments";§5.1 "object properties / initial positions / task
  instructions(covering both semantic and structural variations)/ environments"——**把 task 折进 instruction 维**;
  §5.2 "objects / goals / spatial configurations / task sets")→ **论文未声明哪一组是权威口径,引用必须带脚注**。
  **外部来源**:arXiv abs(HTTP 200 / 43,388 B)+ LaTeXML 全文 v2(HTTP 200 / 127,339 B;59 个 math alttext
  全保留)。**定案(高)**:**= 四个正交扰动维度(物体属性 / 初始空间构型 / 任务指令 / 环境)+ task 作第五类扰动、
  被显式排除在跨类组合之外**;**不得径写"五维正交"**(与摘要及 `k∈{O,R,L,E}` 冲突),**也不得径写"仅四维、
  无 task 扰动"**。**⚠️ 横向对比护栏**:LIBERO-PRO(4+1)/ LIBERO-Plus(7)/ LIBERO-VPro(12 类)
  **各家维度定义不同轴、不可直接比数**。**落点**:骨干图谱 §8.5 表 #6、`benchmark-libero-pro.md` 核实记录、
  Phase2-分支①⑤⑥⑦ §2.2 LIBERO-PRO 卡。
- **N2 · RoboArena(2506.18123v2)episode 数 —— 由上文 #7 的『两口径』升级为『三口径』**:
  ①**612** = 成对 A/B 比较场次数(§1 逐字 "a total of **612 pairwise comparisons**");②摘要的
  "**more than 600**" 是 **612 的取整表述**——**"600" 不是独立数字**;③**4,284** = 累计 policy rollouts
  (§5.1 逐字 "asking evaluators to score **the remaining five policies** after each A/B evaluation on the
  same task. In total, we use **4284 evaluations** to compute this oracle ranking")。
  **三者严禁混用**。**⚠️ 算术闭合(本所推算,非原文直述,引用须标『推算』)**:**612 × 7 policies = 4,284**,
  与原文两处措辞自洽 → 可作"两口径同源"的硬证据。**外部来源**:arXiv abs(HTTP 200 / 47,837 B)+ LaTeXML
  全文 v2(HTTP 200 / 343,748 B;236 math alttext 全保留)。**定案(高)**:引用应写
  "**612 场成对 A/B 比较(摘要作 >600)、累计 4,284 条 policy rollouts(=612×7,用于 oracle 排名)**"。
  **⚠️ 横向对比护栏**:任何"评测规模"比较(RoboDojo 42 仿真+18 真机 / vla-eval 2,000 episodes)
  **必须带口径标签**(成对场次 vs rollouts vs 文献聚合条数),否则构成"不同轴并列"(honor 2026-10-09 类型)。
- **N3 · RoboArena venue = CoRL 2025 Oral,PMLR 305:336-364 → 证伪图谱的全称断言**:
  **外部来源(两个独立源)**:①**PMLR 官方论文集** `proceedings.mlr.press/v305/atreya25a.html`
  (HTTP 200 / 19,660 B,逐字 "Proceedings of The 9th Conference on Robot Learning , **PMLR 305:336-364, 2025**")
  + 卷索引 `v305/`("RoboArena" 1 命中、"Atreya" 3 命中)+ 卷号对照页(v229=CoRL 2023 / v270=CoRL 2024 /
  **v305=CoRL 2025**);②**OpenReview** id=`cpmwi3Xwcr`(HTTP 200 / 25,699 B)`venue: **CoRL 2025 Oral**`、
  venueid=`robot-learning.org/CoRL/2025/Conference`、invitations 含 `Submission1011/-/**Spotlight_And_Camera_Ready**`。
  **反证式核查**:arXiv comment 仅 "Website: …"、**无 journal_ref**;Crossref `query.title=RoboArena&
  query.author=Atreya` = `"total-results":0,"items":[]` → **单查这两源必然维持"未发表"误判**。
  **定案(高)**:**= CoRL 2025(The 9th Conference on Robot Learning)Oral,PMLR 305:336-364, 2025;
  已同行评审并正式发表**。**连带证伪**:Phase2-分支①⑤⑥⑦ §2.3 的**全称断言「对撞层无一经同行评审正式发表」
  被证伪**(至少 RoboArena 一例),已按 N3 **分层重写**(RoboArena 已发表 / vla-eval 仅 ICRA 2026 Workshop
  Poster / 其余 8 项 venue 未逐一核实)。**替代论断**:原「"事实上的权威"先于"正式发表"」的强形式不成立,
  **须收缩为「发表滞后于事实权威」(判断,置信度中,只有两例支撑)**。**⚠️ 附带定案 · 作者数须带版本口径**:
  **arXiv v2 abs = 32 人** / **PMLR v305 camera-ready = 26 人**(v2 独有 7 人、PMLR 独有 1 人,32−7+1=26 ✓;
  "Edward Hu/Edward S. Hu"、"Roberto Martin-Martin/Roberto Martín-Martín" 为同人异写已排除)→
  **不得径写"32 位顶级作者"当既成事实**;差异成因(v2 扩列贡献者?)= **推断,置信度低,不作断言**。
  **⚠️ 方法论扩展已入 `lessons.md`**:既有判例"arXiv comment ≠ venue"须加对称规则
  **"Crossref `total-results:0` ≠ 未发表"**(PMLR / OpenReview 系会议多不注册 Crossref DOI)。
- **N4 · RoboArena 排名算法与策略池:"EM 非 BT"须精确化**:图谱原写"排名用 EM(非 Bradley-Terry)"**易被读成
  "完全弃用 BT"**。**外部来源**(arXiv LaTeXML 全文 v2,HTTP 200 / 343,748 B,逐字):§3.2 "**Extending BT**
  The Bradley-Terry model … **assumes that each pairwise comparison in the preference dataset takes place under
  identical conditions. This assumption is not satisfied in the setting of A/B robot policy evaluations**";
  拟合小节标题 "An EM algorithm for approximate MLE"(clipped Newton 更新);Appendix B "We test instantiations
  of RoboArena with standard ranking algorithms, namely **Elo [61] and Bradley-Terry ("BT", [60])**, and our
  **task-aware ranking approach introduced in Section 3.2 ("TASK")** … leads to **more accurate rankings than
  both standard Elo computation and the conventional Bradley-Terry model**"、"again invoking the **Davidson
  extension of the Bradley-Terry model**"。**定案(高)**:**排名算法 = 自家 "task-aware" 模型,即 BT 的任务感知
  扩展(含 Davidson 平局项),用近似 MLE 的 EM 算法拟合;BT/Elo 是论文用来对比并击败的基线,不是被弃用的框架**
  → **不得写"用 EM 非 BT"**。**策略池(高)**:7 策略**确为 π0(2)/ PaliGemma(5)家族的 DROID 微调变体,
  非跨厂商明星对撞**(§5.1 逐字 "there are seven such policies, **based off PaliGemma [66] or π0 [41] base
  models**";准入标准 "all publicly available generalist DROID policies that … **work out of the box**");
  **单本体(DROID)局限系论文自陈**(§4.2 "the experimental evaluations in this paper have focused on the DROID
  platform … Future work should investigate how RoboArena can be extended to diverse robot embodiments")→
  "generalist 对撞名不副实"这一**判断**可保留,但**须注明跨本体是论文自陈的 future work**。
  **⚠️ 未回流项(登记)**:N4 影响② 要求 Phase2-分支①⑤⑥⑦ §2.4 衔接段"RoboArena double-blind 协议适配
  '检索库 vs 训练型策略'对撞"这一判断**补一条前提**(池的准入是"公开可用 + DROID 开箱即用",MT3 类免训练检索
  策略**要进池须先满足 DROID 本体适配**;判断,置信度中)——**检验记录 §5 回流清单未列入,本轮未代改,标『待同步』**。
- **N5 · vla-eval(2603.13966v3)657 条口径 + venue = ICRA 2026 工作坊 Poster**:
  **外部来源**:arXiv abs v3(HTTP 200 / 42,972 B;**`comment` 与 `journal_ref` 两字段均无**)+ LaTeXML 全文
  (HTTP 200 / 140,959 B)+ **OpenReview** id=`IpKQsHWaYS`(HTTP 200 / 9,761 B)`venue: ICRA 2026: From Data
  to Decisions Poster`、**venueid=`IEEE.org/ICRA/2026/Workshop/From_Data_to_Decisions`(明含 `Workshop`)**、
  bibtex booktitle "**ICRA 2026 Workshop**: From Data to Decisions: VLA Pipelines for Real Robots";
  **反证式核查** Crossref `total-results:0`。**定案(高,除机构归属)**:
  ①**657 = "从 1,704 篇论文中聚合出的已发表结果条数"(文献聚合量),不是复现量**;复现验证范围**只有**
  "six VLA codebases × three simulation benchmarks"——**两个量级不可混用**;
  ②**引用 657 必带三重 caveat**:文献聚合非复现 / **抽取与归一化由 AI agent 完成**(原文逐字 "An AI agent
  (**Claude Code with Opus 4.6**) reviewed 1,704 papers via **MCP tool integrations (arXiv, Semantic Scholar,
  PDF reader)** to extract and normalize results")/ 作者自陈 "Leaderboard results are extracted from published
  papers, **not independently verified**";
  ③**"47×" 限 LIBERO,不得写成通用加速倍数**(原文 "up to 47× wall-clock speedup, completing **2,000 LIBERO
  episodes** in ~18 minutes",~14h → ~18min;**CALVIN = 16×**、**SimplerEnv = 12×**);
  ④**"0%→59.7%" 必须带 −8.0 pp 尾巴**(原文逐字 "brought GR00T on SimplerEnv (Google Robot) **from 0% to
  59.7%, with a −8.0 pp gap to the reported score remaining**";表格作 "59.7 ( −8.0) ‡")→ **修好暗参数后仍未
  追平已发表分数**;只写"0%→59.7%"会把未追平写成追平(**数字-结论错配高危型**);
  ⑤**多口径不得混称**:**14**(harness 集成的仿真基准,Fig.1 图注 "14 benchmarks (**3** with full
  cross-codebase reproduction validation)")/ **17**(leaderboard 追踪)/ **6**(model servers:CogACT、OpenVLA、
  OpenVLA-OFT、π0/π0-FAST、GR00T N1、X-VLA);另有 "**six** published VLA codebases"(复现验证对象:OpenVLA、
  π0.5、OpenVLA-OFT、GR00T N1.6、DB-CogACT、X-VLA)——**两个"six"名单不同,不得混称**;
  **509+ 在原文既作 "509+ configurations" 又作 "509+ models"(Fig.5 段)→ 论文自身口径摇摆、正口径未定**;
  ⑥**venue = ICRA 2026 工作坊 "From Data to Decisions: VLA Pipelines for Real Robots" Poster,不是 ICRA 2026
  主会** → **不得径写"ICRA 2026"**(会与 §2.1 ⑦d 的 RoboEval(2507.00435,**ICRA 2026 主会**)构成同标签
  不同层级混淆);**⚠️ 未排除项**:本轮**未查 IEEE Xplore**,"是否另有 ICRA 2026 主会记录"未排除;
  ⑦**机构 = AllenAI 系据 leaderboard URL `allenai.github.io/vla-evaluation-harness/leaderboard`(Fig.4 图注逐字)
  间接推断**,abs/HTML 作者块机构串未逐字核到 → **置信度中,引用须标"据 leaderboard URL 推断"**;
  arXiv v3 作者 7 人,主分类 cs.AI(单一);
  ⑧**协议不可比性获原文逐字支撑(置信度由中升高)**:"Evaluation protocols vary across papers: **SimplerEnv
  spans three incomparable robot configurations; CALVIN ABC→D and ABCD→D splits are not comparable; LIBERO
  papers report 4 or 5 suites.**";
  ⑨**⚠️ 分层护栏**:vla-eval 的"暗参数"效应(单一未记录参数使结果偏移 tens of pp)是**独立于 LIBERO-PRO 的
  第二方证据**,但**层级不同**(参数敏感性 ≠ 训练集泄漏)→ **引用须分层,不得合并成"两篇都证明泄漏"**。
- **N6 · STRAP ID 冲突定案:STRAP(子轨迹检索)= 2412.15182,venue = ICLR 2025 Poster;2310.12077 不是 STRAP**:
  **冲突**:Phase 2 早期记 STRAP = **2310.12077(CoRL 2023)** vs 另一子 agent 记 **2412.15182(RSS 2024)** vs
  Phase2-分支①⑤⑥⑦ §5.3 "负向核实不在 CoRL 2024(PMLR v270 全文检索无 'Memmel'/'Sub-Trajectory')"→ venue 悬置。
  **外部来源**:`arxiv.org/abs/2310.12077`(HTTP 200 / 40,295 B)题名 "**One-Shot Imitation Learning: A Pose
  Estimation Perspective**"、作者 "**Pietro Vitiello, Kamil Dreczkowski, Edward Johns**"、comment "Published at
  the 7th Conference on Robot Learning (CoRL 2023)";`arxiv.org/abs/2412.15182`(HTTP 200 / 44,433 B)题名
  "**STRAP: Robot Sub-Trajectory Retrieval for Augmented Policy Learning**"、作者 "**Marius Memmel, Jacob Berg,
  Bingqing Chen, Abhishek Gupta, Jonathan Francis**"、comment 仅 "Project website at …"(**无 venue 信息**);
  **PMLR v229(CoRL 2023)官方论文集** `vitiello23a.html` 逐字 "**PMLR 229:943-970**";**OpenReview**
  `term=STRAP`(HTTP 200 / 362,978 B,count=139)**三条同作者串记录**:id=`4VHiptx7xe` **`venue: ICLR 2025
  Poster`**(venueid `ICLR.cc/2025/Conference`,invitations 含 `Submission11830/-/**Camera_Ready_Revision**`,
  bibtex booktitle "The Thirteenth International Conference on Learning Representations")、id=`EWfN9upi72`
  **CoRL 2024 Workshop MRM-D Poster**、id=`MXNoOqBNLZ` **CoRL-X-Embodiment-WS 2024 Poster**;
  **反证式核查** Crossref `query.title=STRAP&query.author=Memmel` = `total-results:0`。
  **定案(高)**:①**STRAP = arXiv:2412.15182,主 venue = ICLR 2025 Poster**(另有两个 CoRL 2024 **工作坊**
  Poster,均非主会)→ Phase2 §5.3 的"负向核实不在 CoRL 2024"**结论正确且现已得到解释**:STRAP 在 CoRL 2024
  **只有工作坊位、不在主会论文集**,故 PMLR v270 检索为负是**预期结果,不是"未发表"**;
  **"RSS 2024"之说本轮无任何外部来源支持 → 判为误记,不采用**,结论应表述为"**已确证 ICLR 2025 Poster;
  RSS 2024 之说无源**"(本轮**未穷尽** RSS 2025/2026 与 ICRA 各年);②**2310.12077 = One-Shot IL
  (Vitiello/Dreczkowski/Johns),CoRL 2023,PMLR 229:943-970 —— 它不是 STRAP**,把它记作 STRAP 属 **ID 张冠李戴**;
  ③**图谱引用规则**:谈"子轨迹检索 / test-time retrieval"引 **2412.15182**;谈"单示范模仿 + 未见物体位姿估计"
  引 **2310.12077**;**两者不可互换、不可共用"STRAP"标签**。**⚠️ 深度边界(诚实)**:两篇本轮**只读 abs 页、
  未读全文** → 技术内容与实验数字一律未核;N6 只对"ID↔题名↔作者↔venue"定案,**不对其结论定案**。
- **N7 · ⚠️ MT3(2511.10110v1)ref [46] 归属更正:是 Vitiello et al.(CoRL 2023),不是 STRAP
  (张冠李戴,死刑级错误类型;签发前捕获、未外流,已录 `honor.md`)**:
  **冲突**:Phase2-分支①⑤⑥⑦ §1.2 原写 "alignment = CoRL 2023 回归位姿(**[46]=STRAP,PMLR v229 已核**)"——
  **"PMLR v229 已核"这半句对,论文身份错**。**外部来源(三源一致)**:①**MT3 v1 全文程序化检索**
  (`arxiv.org/html/2511.10110`,HTTP 200 / 383,679 B;去标签正文 4,941 行)——**"Memmel" 命中 0 / "STRAP" 命中 0 /
  "Sub-Trajectory"·"sub-trajectory" 命中 0 / "Vitiello" 命中 2**;②**参考文献条目逐字**"**[46] P. Vitiello,
  K. Dreczkowski, and E. Johns (2023) One-Shot Imitation Learning: A Pose Estimation Perspective . In Conference
  on Robot Learning**",正文三处引用位置均指位姿估计/运动规划("pose estimation [22, 46]" ×2、
  "motion planning [46]");③**PMLR v229 官方页**确证 CoRL 2023 / PMLR 229:943-970。
  **定案(高)**:**[46] = Vitiello, Dreczkowski & Johns (2023),CoRL 2023,PMLR 229:943-970 = arXiv:2310.12077**;
  **STRAP(2412.15182)在 MT3 v1 全文中零出现**。**结构性结论仍成立且更强**——MT3 位姿上游 = **CoRL 2023
  位姿估计谱系(Vitiello et al.)+ Generalised ICP(Segal RSS 2009)**,**不是 FoundationPose/MegaPose 谱系**;
  原结论**指向正确,只是把论文名认错了**(**STRAP 是检索策略学习,与"回归位姿"本就不相干,这一不相干本身就是
  识别该错配的线索**)。**注:MT3 与 Vitiello et al. 同门**(Dreczkowski/Vitiello/Johns 为共同作者;MT3 题名
  "Learning a Thousand Tasks in a Day",Imperial College London Robot Learning Lab),引自家 CoRL 2023 前作
  做位姿对齐,**谱系自洽**。**根因**:子 agent 二手转述 + 主会话未回原文核 ref 编号。
  **预防(硬规则,已入 `honor.md`)**:**凡把"论文 A 的 ref[n] = 论文 B"写进产物,必须回原文 grep 参考文献条目,
  不得由子 agent 口述或凭"同门/同主题"推断。**

**方法论扩展(2026-10-15 Round 2 · N3;已入 `lessons.md`)**:既有判例"arXiv comment ≠ venue"须加**对称规则**——
**"Crossref `total-results:0` ≠ 未发表"**(PMLR 系 CoRL/AISTATS/UAI 与 OpenReview 系 ICLR/NeurIPS **多数不注册
Crossref DOI**;**缺席证据在"该源本就不覆盖此出版物"时完全失效**)。**venue 核实的正源顺序**(按证据力排序,
**不得跳级用弱源否证**):①arXiv `comment`/`journal_ref` = **线索级,既不能证实也不能否证**;②**官方论文集站**
(`proceedings.mlr.press` 卷号+卷页 / `papers.nips.cc` / `roboticsproceedings.org` / **IEEE Xplore**);
③**OpenReview**(`venue`/`venueid`;invitations 里出现 `Camera_Ready`/`Spotlight_And_Camera_Ready`/
`Camera_Ready_Revision` = **强录用信号**;**⚠️ 必看 `venueid` 是否含 `Workshop`——工作坊 ≠ 主会**);
④**Crossref DOI**(**仅对有 DOI 的 IEEE/RSS/期刊有效**,RSS 有 `10.15607/rss.*`;**返回 0 只证明"Crossref 没这条"**);
⑤**DBLP**(本轮不可用,交叉源缺位须如实登记)。

**⚠️ 本补充节的残余不确定性(承检验记录 §4,不重复其全文)**:①**N3/N5/N6 的 venue 定案只有 1-2 个外部源,
均未达"三源一致"**(DBLP 缺位)→ 建议后续补 DBLP 或会议官网虚拟站二次确认;②**LIBERO-PRO venue 仍未核实**
(Crossref 无 DOI;OpenReview `term=LIBERO-PRO` 返回的 "LIBERO-Pro: A Benchmark for Evaluating the Robustness
of Embodied Foundation Models"(ICLR 2027 在投,匿名)**题名与 arXiv v2 不同 → 不采信、不作任何 venue 或身份
结论**,守宪法"非公开信息(未公开论文评审)不碰",仅登记为线索);③**对撞层其余 8 项 venue 未逐一核实**
(RoboDojo / BiGym 2.0 / LIBERO-PRO / LIBERO-Plus / LIBERO-VPro / SafeVLA-Bench / RoboTwin-Phys / AGNOSTOS),
**且 RoboArena 一例已证明"未核实"可能低估发表状态**;④**图谱系列其余数字锚点本轮一律未外部复核**
(RoboDojo 42+18/30 策略、BiGym 2.0 自报数 5-8 倍口径分裂、SafeVLA-Bench 18-28%/38-56%、LIBERO-Plus
95%→<30%、LIBERO-VPro 12 类/96 settings/3,296 cases)→ **会签前自查复核的必查清单**;
⑤**OpenReview 附带命中两篇 ICLR 2027 在投匿名稿**("Correlation Is Not Selection: Validating Automatic
Evaluators for Robot Policies"、"Success Rates Are Not Model Properties: Controlled Diagnostics for VLA
Evaluation")主题与"对撞层/评测可比性"高度相关,**本轮不读其内容、不引其结论**,仅记为**监控哨候选**(录用后再核)。
