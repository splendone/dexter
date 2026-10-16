# BridgeData V2

- 级别:知识卡片(闲时菜单 B2)| 建档:2026-09-28 | 起草:Dexter | 状态:初版
- 官方页:https://rail-berkeley.github.io/bridgedata/
- 论文:BridgeData V2: A Dataset for Robot Learning at Scale
  (arXiv:2308.12952,CoRL 2023)
- 类型:大规模低成本真机数据集(单臂,桌面场景为主)
- 规模口径(官方页原文,2026-09-28 抓取):60,096 条轨迹 = 50,365 条遥操作
  示范 + 9,731 条脚本化 pick-and-place 策略 rollout;24 个环境;13 种技能;
  平均轨迹长 38 步
- 采集方式:WidowX 250 六自由度臂,VR 手柄遥操作,5Hz 控制;肩置固定
  RGBD + 两个随机位姿 RGB + 腕部 RGB,640×480
- 获取:rail.eecs.berkeley.edu 直下(JPEG,遥操作/脚本数据分卷);代码
  github.com/rail-berkeley/bridge_data_v2(含训练评测与预训练权重)
- 许可:**CC BY 4.0(页面明示)**——四张卡里许可最宽松
- 透镜关系(这是判断):①泛化研究的常用底料(大规模 + 场景多样性 +
  脚本/遥操作混合,便于做数据配比消融);对④的意义是"低成本单臂流水线
  的参照系"。
- 置信度与待核点:高(逐字来自官方页);下载带宽与镜像现状未测。
