# 同路线竞品盯仓(Morphometric Imitation 关联三项目)

- 建档:2026-09-28(07:0x 班)| 起草:Dexter | 档案类型:竞品盯仓
- 触发:精读 arXiv:2609.28660(Morphometric Imitation,UC Berkeley,
  人手捕重定向→零样本灵巧操作策略)时,TopoRetarget 与 DemoMimic 两个
  同路线竞品当时未放代码;本次复查三项目现状(2026-09-27 UTC 快照,
  arXiv API + GitHub API + 项目页原始 HTML,均实际打开核实)。
- 参照系:Morphometric Imitation = "形态学优化重定向(MMO)→ 残差 RL
  → 蒸馏成视觉运动策略",三手型十 HOI,真机 300 次 89.3% 零样本成功
  (arXiv:2609.28660 摘要原文,已核)。

## 1. TopoRetarget

- 论文:**arXiv:2606.16272**,"TopoRetarget: Interaction-Preserving
  Retargeting for Dexterous Manipulation"(v1 2026-06-15,v2 2026-06-22,
  arXiv API 记录已核)。作者 Jielin Wu、Shenzhe Yao、Guanqi He、
  Xiaohan Liu、Zhaoqing Zeng、Xiangrui Jiang、Han Yang、Wentao Zhang、
  Hang Zhao;非官方复现 README 称"Tsinghua University"(单源,中置信)。
- 代码状态:**官方未开源**。GitHub 组织 TopoRetarget2026 仅存项目页仓库
  (github.com/TopoRetarget2026/TopoRetarget,★2,推送 2026-09-17);
  项目页 HTML 无任何代码链接(仅 CSS);arXiv comment 只给项目页
  toporetarget2026.github.io/TopoRetarget/。组织仓库描述自称
  "CoRL 2026 submission"(自述,单源)。
- 非官方生态(活跃度信号):yijie21/toporetarget_reimp(**★18**,MIT,
  2026-09-10 建,MANO→Wuji 重定向可视化);0iui0/toporetarget(★15,
  无许可,README 自称 Unofficial);另有 Key-Zzs/TopoRetarget-Repro(★2)、
  Hydrofoooil/TopoRetarget(★0)。零星复现而无官方码,说明关注在涨。
- 与 Morphometric 的关系(这是判断):**同路线、同阶段正面竞品**——都做
  "人手 HOI 捕捉 → 保接触重定向 → RL/策略";TopoRetarget 押注重定向段
  (交互图+距离加权拉普拉斯变形保接触拓扑,供 PPO 参考跟踪,Wuji Hand
  零样本上真机),正对位 Morphometric 三阶段中的 MMO 段,选它当对比
  baseline 的概率高。
- 置信度:高(论文与仓库状态多源直接核实);作者机构=清华为中。

## 2. DemoMimic

- 论文:**arXiv:2609.01938**,"One Demonstration, Many Objects:
  Generalizing Manipulation via Local Contact Geometry"(v1 2026-09-01,
  v2 2026-09-03,arXiv API 记录已核)。摘要原文:"We propose DemoMimic
  (Dexterous Motion Mimic)"——即 DemoMimic 本尊,非同名异物。作者
  Satvik Sharma、Samrat Sahoo、Huang Huang、Fei-Fei Li、Jiajun Wu、
  Dorsa Sadigh、Jeannette Bohg;项目页外链 Stanford 主页(Bohg、Fei-Fei)
  ,Stanford 归属由此佐证。
- 代码状态:**未开源**。项目页 demomimic.github.io 无代码链接(外链仅
  arXiv、作者主页、论文 PDF);GitHub 全站检索无同名代码仓库;项目页
  仓库 demomimic/demomimic.github.io(★0,推送 2026-09-04)只是网页;
  一作 GitHub(Satvik1701)名下无此项代码。论文 9 月初才挂出,未放码
  属正常节奏,继续盯。
- star/活跃度:无代码仓库可计;项目页 0★。
- 与 Morphometric 的关系(这是判断):**同路线、不同杠杆**——同样
  "人手演示先验 + sim-to-real RL + 接触感知奖励",但 DemoMimic 主打
  单条演示经"接触点局部几何"泛化到形状/尺度/质量/摩擦不同的多物体
  (16 物体 4 任务 2 手型 71%),与 Morphometric 的"重定向→残差 RL
  →蒸馏"管线在数据效率叙事上直接竞争。
- 置信度:高(摘要、项目页、GitHub 三处直接核实)。

## 3. PolyUMI

- 论文:**arXiv:2609.29760**,"PolyUMI: Accessible Visual-Tactile-Audio
  Data Collection for Object Inference and Manipulation"(v1 2026-09-24,
  arXiv API 记录已核)。作者 Conor W. Hayes、Rickmer Krohn、
  Aravind/Anunth Ramaswami、Nils Dengler、Kevin M. Lynch、
  J. Edward Colgate、Georgia Chalvatzaki、Matthew L. Elwin。
- 代码状态:**已开源**。仓库 github.com/polyumi/PolyUMI-platform
  (arXiv 摘要给项目页 polyumi-vista.github.io,页面 "Code" 按钮指此仓库
  ,已核)。**MIT 许可**;★0 / 0 fork;建仓 2026-09-15,末推 2026-09-16。
  仓库描述自称"为评审目的复制到匿名账号、无提交历史"——即**匿名评审版
  开源**(疑似在审,单源),非正式发布形态;star/活跃度暂无参考价值,
  正式接收后需重盯。
- 与 Morphometric 的关系(这是判断):**不同路线,数据端互补**——
  PolyUMI 是 UMI 式便携采集平台(手持无线夹爪,腕相机+光学触觉+接触
  音频+本体感知同步记录,传感指可原样移到机器人端保几何一致,配
  VisTA 多模态策略),不经过人手重定向;对 Morphometric 是"演示数据
  从哪来"的替代答案,也可能成为其上游数据源。
- 置信度:高(论文、项目页、仓库直接核实);匿名评审性质为中(仅仓库
  自述)。

## 盯仓结论(这是判断)

- TopoRetarget:等 CoRL 2026 结果与官方放码;其交互图重定向若开源,
  应作为 Morphometric MMO 段的首选对比件纳入复现清单。
- DemoMimic:放码前只做文献跟踪;其"局部接触几何"奖励设计与
  Morphometric 的接触信息残差 RL 值得并读。
- PolyUMI:采集平台已可动手(MIT),但匿名评审版无提交历史,克隆评估
  前先等正式版;对委托人价值在"多模态数据采集基建"备选。
