# Open X-Embodiment(OXE)

- 级别:知识卡片(闲时菜单 B2)| 建档:2026-09-28 | 起草:Dexter | 状态:初版
- 官方页:https://robotics-transformer-x.github.io
- 论文:Open X-Embodiment: Robotic Learning Datasets and RT-X Models
  (arXiv:2310.08864)
- 类型:**聚合数据集**——汇集 34 个研究实验室的 60 个既有数据集
- 规模口径(官方页原文,2026-09-28 抓取):1M+ 真机轨迹;22 种机器人本体;
  527 skills(160266 tasks);配套模型 RT-1-X / RT-2-X(55B)
- ⚠️ **机构数口径(2026-09-28 查原始文本)**:本卡"**34 个实验室 / 60 个
  数据集**"来自**官方页**;而**论文**(abs 页 + HTML v9 正文)一致写
  "**21 institutions**"(正文原句:"22 different robotic embodiments from
  21 different institutions"),**60 datasets** 亦为论文口径。→ **60 datasets
  两源一致**;**机构数 21 vs 34 不一致**,或为"RT-X 协作成员机构"与
  "数据集来源实验室"之别(**未证实**)。**引用须标来源。**
- 采集方式:聚合既有数据集(各子集采集方式不一,遥操作为主,非统一采集)
- 获取:官方 Google Sheet 数据清单;代码 github.com/google-deepmind/open_x_embodiment
- 许可:项目页未显示 → 待核(需查 GitHub 仓库 LICENSE 及各子集授权)
- 透镜关系(这是判断):④ 数据引擎的聚合端基座;跨本体聚合本身就是①泛化
  (跨本体/跨场景泛化)的实验场——RT-X 系列的结论都建立在这份数据上。
- 置信度与待核点:规模数字为高(逐字来自官方页);许可、各子集明细、
  数据清单时效性待核。
