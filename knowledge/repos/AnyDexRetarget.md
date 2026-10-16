# AnyDexRetarget(开源档案 B3 首单)

- 建档:2026-09-28(06:5x 班)| 起草:Dexter | 档案类型:开源工具
- 仓库:github.com/qqsq12321/AnyDexRetarget | ★87 / 11 forks | master,51 commits
- 许可:**MIT(页面明示)**——可自由使用与二次开发
- 是什么:人手→灵巧手的实时重定向系统(遥操作核心件),MuJoCo 仿真 +
  真机双路;两种优化器(adaptive 捏合感知 / vector 关键向量),解析梯度
  + NLopt SLSQP,**约 2ms/帧**
- 输入设备:Apple Vision Pro、Meta Quest 3、Pico 4(直连/中继)、Noitom
  PNS-G 手套(Axis Studio)、笔记本相机/RealSense(MediaPipe)、录制回放
- 支持灵巧手(13 种):Shadow、Wuji、Allegro、Inspire、Ability、Leap、
  SVH、LinkerHand L21/L20、ROHand、Unitree Dex5、Sharpa、Gaia Hand20
- 真机驱动:Wuji(TCP)、Shadow(TCP 桥)、Inspire(串口)、Gaia(官方 SDK);
  含标定工具(缩放/旋转/捏合)与骨架调试器;macOS 需 mjpython
- 与论文的关系(这是判断):与 2609.28660(Morphometric Imitation)同属
  "人手→机器人手"家族,但定位互补——本项目是**实时遥操作工具**,
  论文是**离线数据重定向→策略训练**管线;前者可当委托人实验室的
  采集基建候选。
- 试用评估结论(这是判断,置信度中):工具成熟度信号良好(多设备、
  多手型、MIT、活跃);**是否试用取决于委托人手头设备**(是否有
  Vision Pro/Quest 3/Pico 4/RealSense)与目标灵巧手是否在 13 种之列。
  待委托人确认硬件后决定;不入正式工具链前保持观察。
- 待核点:star 曲线与维护节奏(单次快照,尚无趋势);真机延迟实测口径。
