# DROID

- 级别:知识卡片(闲时菜单 B2)| 建档:2026-09-28 | 起草:Dexter | 状态:初版
- 官方页:https://droid-dataset.github.io
- 论文:DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset
  (arXiv:2403.12945)
- 类型:大规模真机遥操作数据集(in-the-wild,分布式采集)
- 规模口径(官方页原文,2026-09-28 抓取):76,000 条示范轨迹;350 小时;
  564 场景;86 任务;50 名采集员 / 13 机构 / 12 个月;95% 成功轨迹有语言
  标注(75k 条);36k 条已更新标定
- ⚠️ **任务数口径(2026-09-28 查原始文本定案)**:本卡"86 任务"与**论文正文**
  (HTML v2 摘要/Intro/§III/Table I)一致;**唯一写 84 的是 arXiv abs 页的
  元数据摘要**(孤例)。→ **采用 86**;引用须标来源,并说明论文把 tasks 定义为
  "语言指令去重后的 unique verbs 数"(Table I 列名 "# Verbs")。
- 论文正文补充数字(HTML v2):**52 buildings、18 robots、13 institutions、
  1417 相机视角**;约 **16k 条 "not successful"** 轨迹一并发布但不计入 76k。
- 采集方式:Oculus Quest 2 遥操作 Franka Panda 7 自由度臂;双 Zed 2 相机 +
  腕部 Zed Mini;可移动升降桌(in-the-wild 场景)
- 获取:TFDS(`gs://gresearch/robotics`);HuggingFace(KarlP/droid);
  官方页含 Colab 快启、可视化器与策略学习代码
- 许可:项目页未标明 → 待核(查 GitHub 仓库 LICENSE / HF 数据卡)
- 透镜关系(这是判断):④ 遥操作规模采集的当前标准范式(低成本标准化
  rig + 分布式人力);语言标注密度使其同时是③语言条件操作的训练与
  评测候选。
- 置信度与待核点:规模数字为高(逐字来自官方页);许可与"更新标定"的
  版本口径待核。
