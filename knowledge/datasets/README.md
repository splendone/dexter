# 数据集卡片库(闲时菜单 B2)

> 目标 8 张,首批 **2026-09-28 建成**;**2026-09-30 补 5 张**(GRAB / UMI /
> Ego4D / Ego2Robot / UVTA)**→ 现 12 张**(G1 判据收束轮)。每张卡片:官方页 /
> 论文(arXiv 页核实)/ 规模口径(逐字来自官方页或论文,注明抓取时点)/
> 采集方式 / 许可 / 透镜关系(标"这是判断")/ 置信度与待核点。

| 数据集 | 状态 | 规模口径(一句话) | 许可 | 卡片 |
|---|---|---|---|---|
| Open X-Embodiment | ✅ | 1M+ 轨迹 / 22 本体 / 60 数据集聚合 | 待核 | Open-X-Embodiment.md |
| DROID | ✅ | 76k 轨迹 / 350h / 564 场景 / Quest2 遥操作 Franka | 待核 | DROID.md |
| ALOHA / Mobile ALOHA | ✅ | 10 分钟演示 80-90% 成功率;50 演示/任务 | 待核 | ALOHA-Mobile-ALOHA.md |
| BridgeData V2 | ✅ | 60,096 轨迹 / 24 环境 / WidowX 遥操作 | **CC BY 4.0** | BridgeData-V2.md |
| RH20T | ✅ | 110k+ 序列 / 40TB / 含触觉音频多模态 | CC BY-SA + BY-NC 分卷 | RH20T.md |
| AgiBot World(智元) | ✅ | 1,003,672 轨迹 / 100 机器人 / 43.8TB | **CC BY-NC-SA 4.0** | AgiBot-World.md |
| MimicGen / DexMimicGen | ✅ | <200 人演→50k 合成;60 人演→20k 双臂灵巧 | 待核 | MimicGen-DexMimicGen.md |
| **GRAB** | ✅ 09-30 | **10 受试者 × 51 物体**;动捕全身抓取 + 接触标注 | **研究用途**(禁商用) | GRAB.md |
| **UMI** | ✅ 09-30 | **采集框架**(手持夹爪+腕部相机),**规模不可得** | 开源(类型待核) | UMI.md |
| **Ego4D** | ✅ 09-30 | **3,670h 自中心人视频** / 931 佩戴者 / 74 地 9 国 | 待核(通常研究用途) | Ego4D.md |
| **Ego2Robot** | ✅ 09-30 | **18,561h** / 15 本体;人视频→机器人合成 | 待核 | Ego2Robot.md |
| **UVTA** | ✅ 09-30 | **5 任务 / 1,000 人演示 + 每任务 150 机器人演示**(触觉) | 待核 | UVTA.md |

三路线速览(这是判断):
- **聚合**:OXE(1M+,跨本体泛化基座)
- **真机遥操作**:DROID / BridgeData V2 / RH20T / AgiBot World(百万级产业线)
- **合成**:MimicGen / DexMimicGen(60 条人演 → 2 万条灵巧演示)
- **人演示(免遥操作)**(2026-09-30 补):**GRAB**(动捕,带接触标注)、
  **UMI**(手持夹爪 + 腕部相机,免标定、机器人无关)、**Ego4D**(纯人自中心视频,
  **最上游**)、**Ego2Robot**(人视频→机器人合成,18,561h)、**UVTA**(人+机器人
  **触觉**演示)——与 ALOHA(自采单机)、DROID(分布式遥操作)并列的**多条采集
  形态**(详见分图④路线 A/B)。**数据源谱系(从左到右越靠"人")**:
  Ego4D(纯人视频)→ Ego2Robot(合成)→ UMI/GRAB(人采集)→ ALOHA/DROID(机器人遥操作)。
- 触觉数据:RH20T(指尖触觉,仅 7 号构型)、AgiBot World(视觉触觉)是②
  透镜唯二有触觉模态的大库;**GRAB 有接触标注但无触觉传感信号**(几何计算,
  勿混淆)。

使用建议:
1. 做④数据引擎调研:按 聚合 → 真机 → 合成 三卡组读,路线之争证据已同步
   进 knowledge/maps/controversies.md 账本二。
2. **许可(2026-09-28 并行子任务核查完毕,详见 license-check.md)**:
   宽松 = BridgeData V2 / OXE 数据(CC BY 4.0,代码 Apache-2.0)/
   ALOHA 系代码(MIT)/ MimicGen 系数据(CC BY 4.0);**禁商用传染** =
   RH20T-NC(CC BY-NC 4.0)/ AgiBot World(CC BY-NC-SA 4.0);
   **有坑** = NVIDIA 系代码为自定义许可(非 OSI,勿当 MIT 用)、
   **DROID 官方代码无许可文件(实际不可复用;数据 CC BY 4.0 为中置信)**;
   OXE 内 60 个子数据集原始许可未逐查。商用边界属法律问题,按宪法转介。
3. 精读候选:AgiBot World 技术报告(2503.06669,产业线最近的教学案例)。
