# 术语表

> 首现术语随手入册(中文 + 原文 + 一句话解释);按字母/拼音序追加。

- **VLA(Vision-Language-Action)**:视觉-语言-动作模型,端到端机器人策略的基础模型路线。
- **Diffusion Policy**:用扩散模型表示动作分布的策略学习路线。
- **灵巧手(Dexterous Hand)**:多自由度末端执行器,操作方向的核心硬件载体。
- **遥操作(Teleoperation)**:人类示范驱动数据采集的主流方式(如 ALOHA 系)。
- **视触融合(Visuo-tactile)**:视觉与触觉(如 GelSight 类传感器)联合感知。
- **Sim2Real**:仿真训练到真实部署的迁移问题。
- **世界模型(World Model)**:可预测环境动力学的生成模型,用于规划与数据生成。
- **行为克隆(Behavior Cloning,BC)**:从示范直接监督学习策略的基线方法。
- **少样本泛化(Few-shot Generalization)**:从极少演示泛化到新物体/新场景。
- **长程任务(Long-horizon)**:需多步规划与子任务组合的操作任务。
- **流匹配(Flow Matching)**:学习速度场的生成范式,策略学习中替代扩散的路线。
- **MeanFlow**:流匹配的加速变体,可少步/单步网络求值生成动作序列。
- **世界动作模型(WAM,World Action Model)**:联合生成动作与预测未来视频的操作模型。
- **Latent Schrödinger Bridge**:熵正则概率传输桥,用于稀疏意图与稠密动作轨迹的对齐(LiMA)。
- **移动操作(Loco-Manipulation)**:腿式/移动底盘与机械臂协同的"边走边操作"任务族。
- **In-the-Wild**:非受控实验室环境下的真实场景采集/部署(DROID 的核心卖点)。
- **LIBERO-Pro**:LIBERO 的增强评测版;2026-09 起成为 agentic/harness 路线的主要基准(见争论账本一)。
- **残差强化学习(Residual RL)**:在冻结的基础策略之上仅学习修正动作的范式;人类纠正可同时监督残差并塑形此前自主行为的奖励(Res-HIL,arXiv:2609.30023)。
- **本体感觉(Proprioception)**:机器人对自身关节状态/位姿的感知,与视觉、触觉等外感受相对;可作为稀疏传感信号对齐的锚点(PROPRA,arXiv:2609.29822)。
