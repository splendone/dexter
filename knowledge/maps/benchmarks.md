# 基准与仿真地图(闲时菜单 B4,5/5 核实完毕 2026-09-28)

> 建档:2026-09-28 重负载班。规则同数据集卡片:数字逐字来自官方页/
> 论文 abs 页/API feed,未核实标待核。背景:09-24 单日三篇 agentic 工作
> 共用 LIBERO-Pro 主基准——基准格局本身就是领域信号。

## LIBERO ✅

- 论文:LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot
  Learning(arXiv:2306.03310,v2 2023-10)| UT Austin 等(LARG/RPL/统计学习组)
- 口径(abs 页原文):面向终身机器人学习(LLDM)的基准,**四个任务
  套件共 130 任务**,带人类遥操作示范数据;研究主题含陈述性/程序性
  知识迁移、任务顺序鲁棒性、预训练影响;页面上未列各套件名称与
  分套件数 → 待核(查论文正文)。
- 许可:未显示(查 GitHub)。

## LIBERO-Pro ✅(2026-09-28 并行子任务结案,详见 benchmark-libero-pro.md)

- 论文:LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-
  Language-Action Models Beyond Memorization(arXiv:2510.03827,v2
  2026-05-25)| 华中科技大学团队;代码 MIT、数据 CC BY 4.0(GitHub
  Zxy-MLlab/LIBERO-PRO,328 stars)
- 定义(abs 页 + HTML v2 全文,主会话 2026-09-28 亲核):LIBERO 的
  **独立扩展评测基准**——在原四套件任务上施加扰动,**四维正交维度**
  (物体外观/初始位置/指令改写/环境)+ **Task 作第五类扰动且不入跨类
  组合**(论文摘要说"四维"、§4.3/Fig.6 说"五类",系论文自身口径;
  2026-09-28 复抓全文已核实并调和,详见专卡"核实记录"),每任务 50
  回合,分布外泛化设计;VLA 标准 LIBERO >90% → 扰动下 0.0% 崩塌,
  系"背诵式记忆"。
- 核心发现(原文):现有 VLA 在标准 LIBERO 上 >90%,扰动下**坍缩至
  0.0%**——"背诵式记忆"而非任务理解。
- 已核使用案例:WAA 75.6%、K1 77.8%/88.9%、SynthDemo-RL 27/57 零成功、
  RACaP 45.0% 零样本、HarnessPAI +61.6pt、**GAM 61%(vs π0.5 53%,
  16 扰动设定;abs 页续班复核 2026-09-28)**。
- 余项:作者隶属两源冲突(README: Harvard/MIT vs arXiv HTML v2: 清华,
  2026-09-28 复抓再确认);官方总任务数未声明(仅见正文引用的 Tables,
  HTML 未展开);"零成功任务"一词系使用方转述。

## RoboCasa / RoboCasa365 ✅

- 论文:RoboCasa(arXiv:2406.02523,RSS 2024);**RoboCasa365
  (arXiv:2603.04356,ICLR 2026)**——365 版已中 ICLR,评测底座换代
- 口径(官方页原文):365 日常任务 / 2,500 厨房环境;600+ 小时人类
  示范 + 1,600+ 小时合成示范;3,200+ 物体、150+ 类;原版 120 场景,
  365 版新增 50 布局 + 50 风格;65 个原子任务覆盖十种基础技能
- 生成工具:GPT-4 定复合任务、MidJourney 纹理、Luma AI 文生 3D 资产、
  Objaverse 1.0 / LightWheel 资产
- 许可:页面未显示(查 GitHub)。

## ManiSkill3 ✅

- 论文:ManiSkill3: GPU Parallelized Robotics Simulation and Rendering
  for Generalizable Embodied AI(arXiv:2410.00425,v2)
- 口径(API feed 原文):开源 GPU 并行机器人仿真器,接触富集物理,
  较其他平台**快 10-1000×、显存省 2-3×**,最高 **30,000+ FPS**;
  12 个任务域,百万级示范帧,附 RL/模仿学习基线。
- 使用事实:Morphometric 残差 RL 阶段在 ManiSkill 中训练(其论文 §V)。
- 许可:未在 feed 中显示 → 查 GitHub。

## RLBench ✅

- 论文:RLBench: The Robot Learning Benchmark & Learning Environment
  (arXiv:1909.12271,2019-09)
- 口径(API feed 原文):**100 个人工设计的独立任务**,视觉+本体感觉
  观测,**不限量的运动规划器生成示范**;支持 RL/模仿/少样本研究。
- 二手事实:RH20T 任务集含"RLBench 48 任务"。
- 许可:未显示 → 查 GitHub。

## 选型速记(这是判断,置信度中)

- 评测 agentic/harness 路线 → LIBERO-Pro(四维正交扰动 + Task 第五类不入
  组合;引用数字前先读原文口径);
- 评测端到端 VLA 泛化 → RoboCasa365(最新底座)+ LIBERO 原版;
- 仿真采数据/域随机化 → ManiSkill3(30k+ FPS GPU 并行,Morphometric 在用);
- 少样本/任务泛化老牌 → RLBench(100 任务 + 规划器无限示范);
- 复现注意:LiMA 揭示的基线训练步数偏离(GR00T 50K vs 推荐 2K)提示
  **引用任何对比数字前先查基线训练口径**。
