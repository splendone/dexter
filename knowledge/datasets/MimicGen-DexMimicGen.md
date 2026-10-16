# MimicGen / DexMimicGen(程序化合成数据路线)

- 级别:知识卡片(闲时菜单 B2)| 建档:2026-09-28 | 起草:Dexter | 状态:初版
- 论文(均已在项目页/arXiv 核实):
  - MimicGen:A Data Generation System for Scalable Robot Learning using
    Human Demonstrations(arXiv:2310.17596,CoRL 2023)
  - DexMimicGen:Automated Data Generation for Bimanual Dexterous
    Manipulation via Imitation Learning(arXiv:2410.24185,ICRA 2025)
- 类型:程序化演示合成系统(非"数据集"而是"数据引擎"——给少量人演,
  自动扩增海量合法演示)
- 规模口径(项目页原文,2026-09-28 抓取):
  - MimicGen:**<200 条人类演示 → 50,000+ 条自动生成**,18 任务,跨多
    仿真器与真机;新物体场景 10 条人演 → 1000 条(12 种马克杯);跨本体
    10 条 Panda → 各 1000 条(Sawyer/IIWA/UR5e)
  - DexMimicGen:**60 条人演 → 21K 条双臂灵巧演示**(论文 abs 页口径;
    项目页写 "20,000+",2026-09-28 复核后以 **21K** 为准),9 任务,
    Real2Sim2Real 管线;BC 训练成功率 69.3%(穿线)~97.3%(码罐)
- 采集方式:源演示 → 轨迹适配(场景/复位分布/物体/本体)自动重放生成
- 获取:MimicGen github.com/NVlabs/mimicgen_environments(2024-07 发布);
  DexMimicGen github.com/NVlabs/dexmimicgen/
- 许可:两个项目页均未标明代码许可 → 待核(NVlabs 仓库需逐个查)
- 透镜关系(这是判断):④"合成路线"的代表——与真机采集(DROID/AgiBot)
  构成本方向数据路线之争的两端;对灵巧手(双臂)的专门化版本说明
  合成路线已覆盖到本方向核心。
- 置信度与待核点:高(逐字来自项目页);生成演示的质量上限与人演最少
  需求量在不同任务域的敏感性,综述时需展开。
