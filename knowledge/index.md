# 知识总索引(knowledge index)

> **本索引是什么**:`knowledge/` 的**检索层**——把散在 `papers/`、`datasets/`、
> `maps/`、`repos/` 的卡片按**四透镜**(相关性锚点,见 `identity.md`)重新组织,
> 使"某方向有哪些论文 / 数据集 / 基准 / 开源"**一屏可查**。
> **补的缺口**:2026-10-08 优化方案甲档 A1(评审:"知识体系是卡片堆,缺乏结构化索引")。
> **一行一条、可跳转**;维护纪律见文末。**新增卡片必须同时登记本索引**(否则视为未入库)。

---

## 透镜① 泛化与数据效率

- **分图**:`reports/final/文献地图-透镜①-泛化与数据效率-v1.md`(**v1.0.1**,14+2 篇;✏️ v1.0.1 = 2026-10-09 透镜③体检联动:补 2606.27663 轴标 + 首次同步 09-30「不应并列」更正 + 首次登记 5 项脆弱点;**16 篇语料全量体检仍逾期**,原定 2026-10-05)
- **论文/经典**:`papers/classics.md`——ALOHA·ACT、Mobile ALOHA、RT-1、RT-2、
  OpenVLA、π0、π0.5、Diffusion Policy、DROID、Open X-Embodiment
- **精读**:`reports/final/精读-2410.24164-pi0.md`
- **数据集**:`datasets/ALOHA-Mobile-ALOHA.md`、`datasets/BridgeData-V2.md`、
  `datasets/Open-X-Embodiment.md`、`datasets/DROID.md`、`datasets/AgiBot-World.md`
- **基准**:`maps/benchmarks.md`(LIBERO / LIBERO-Pro / RoboCasa365 / ManiSkill3 / RLBench)

## 透镜② 触觉与多模态传感

- **分图**:`reports/final/文献地图-透镜②-触觉与多模态传感-v1.md`(**v1.0.2**,13 篇唯一条目=12 工作+1 方法论模板;**v1.0.2 = 2026-10-09 OpenViTac 全文级证据触发重审,脆弱点「触觉边际价值无规模化受控对撞」的「无」字证伪→分层改写**)
- **基准专卡**:`maps/benchmark-openvitac.md`(**2026-10-09 新增**,OpenViTac 2610.10384 全文核实:统一视触基准 11 仿真+8 真实任务;⚠️ intro 最强 WAM 53.3/48.5 与自身 Table 37.4/29.0 矛盾,不得作外部锚点)
- **精读**:`reports/final/精读-2609.28660-Morphometric-Imitation.md`、
  `reports/final/精读-2609.30127-RMFP.md`、`reports/final/精读-2609.28431-LiMA.md`
- **数据集**:`datasets/RH20T.md`(指尖触觉)、`datasets/AgiBot-World.md`(视觉触觉)、
  `datasets/GRAB.md`(接触标注,**无触觉信号**)、`datasets/UVTA.md`(人+机器人触觉演示)
- **开源/竞品**:`repos/AnyDexRetarget.md`、`repos/competitors-watch.md`
  (TopoRetarget / DemoMimic / PolyUMI)

## 透镜③ 语言条件长程操作

- **分图**:`reports/final/文献地图-透镜③-语言条件长程操作-v1.md`(**v1.1.1**,24 篇 / 6 路线;✅ **2026-10-09 补做逾期体检**:24/24 ID 经 arXiv 官方 API 外部核验仍解析、标题逐条吻合、0 撤回,4 篇出 v2 经摘要 diff 确认无口径漂移;**⚠️ 体检捕获本所「77.5/60.2 = 扰动分」轴标归因误读 → ✏️ 更正自身错,升 v1.1.1**,并联动更正总图/分图①/综述/立场文章/账本一共 5 件;下次体检 2026-10-16)
- **争论**:`maps/controversies.md` 账本一(端到端 vs agentic vs 程序合成)

## 透镜④ 数据采集与合成

- **分图**:`reports/final/文献地图-透镜④-数据采集与合成-v1.md`(30 篇 / 6 路线 A–F)
- **选型**:`maps/dataset-selection-matrix.md`(12 数据集 × 许可 × 可复现性 × 透镜适用)
- **数据集**:全 12 张(见下「数据集卡库」);路线 A 真机遥操作 / B 人演示→机器人 /
  C 程序化仿真 / D Real2Sim2Real / **E 数据翻新** / **F 异构语料工程**

---

## 横向实体(跨透镜)

| 主题 | 文件 |
|---|---|
| 文献地图总图 | `reports/final/文献地图-v0.1.md`(**v1.1.1**,含 ⚠️ 口径更正;✏️ v1.1.1 = 2026-10-09 透镜③体检联动,更正「77.5 为扰动分」误读 + 标题版本 stale 校正;**22 篇语料全量体检仍逾期**,原定 2026-10-07) |
| 基准地图 / 专卡 | `maps/benchmarks.md`、`maps/benchmark-libero-pro.md`、`maps/benchmark-openvitac.md`(2026-10-09 新增) |
| 争论账本 | `maps/controversies.md`(账本一/二/三) |
| 重审账本 | `maps/review-ledger.md`(版本 / 签发日 / 脆弱点 / 待重审) |
| 数据集三维选型 | `maps/dataset-selection-matrix.md` |
| **假设账本** | `maps/assumptions.md`(2026-10-08 新增) |
| **产物依赖图** | `maps/artifact-dependencies.md`(2026-10-08 新增) |
| **SCI 论文能力映射表** | `maps/sci-paper-capability-map.md`(2026-10-09 新增,六层能力 × 自动化分级 × 四道人闸) |
| 术语表 | `glossary.md` |
| 技术版图 | `landscape.md` |
| 信息源清单 | `sources.md` |
| 数据集卡库 | `datasets/README.md`(12 张 + 许可核查 + 数据源谱系) |
| 许可核查 | `datasets/license-check.md` |

### 数据集卡库(12 张)

聚合:`Open-X-Embodiment` · 真机遥操作:`DROID`、`BridgeData-V2`、`RH20T`、
`AgiBot-World`、`ALOHA-Mobile-ALOHA` · 合成:`MimicGen-DexMimicGen` ·
人演示:`GRAB`、`UMI`、`Ego4D`、`Ego2Robot`、`UVTA`。
**数据源谱系**(这是判断):Ego4D(纯人视频)→ Ego2Robot(合成)→ UMI/GRAB(人采集)
→ ALOHA/DROID(机器人遥操作)。

---

## 产物索引(黄档 / 设计档)

- **`reports/final/`(15 件)**:文献地图总图 **v1.1.1** + 四透镜分图(①**v1.0.1**/②**v1.0.2**/③**v1.1.1**/④v1.0)+ 精读 ×4(**均 v1.0.1**,2026-10-09 21:2x 批量补做逾期体检:π0/LiMA/RMFP PASS[with notes]、**Morphometric FAIL**[版本 stale,v2 于签发前 3 天已发布 → 150fps 删/匹配阈值 5→4.5mm/89.3% 加「On a Sharpa hand」限定/补 v2 显著性保留],录 honor + 起草 P-014)+
  教程《数据引擎六路线》v1.0 + 综述《四透镜×三股力量》**v1.0.2** +
  **立场文章《从路线站队到资产工程》v1.0.2**(2026-10-09 M4 签发 v1.0 → 18:5x 证据触发重审 v1.0.1[脆弱点⑦ 闭合]→ **19:5x 体检联动重审 v1.0.2**[✏️ 更正守则框「77.5 = 扰动分」轴标误读,处置零改动],8 项脆弱点见 `maps/review-ledger.md`)+
  **制度层三件**:优化方案《外部对标与自我诊断》v1.0(2026-10-08)+ 优化方案《对标 autoresearch·常驻科研循环》v1.0(2026-10-16)+ **优化方案《对标 system_prompts_leaks·观察者与复核分档》v1.0(2026-10-16,同库第二遍:解析 8 条→甲档 2 项已落地 + 乙档 P-019~P-023 待批)**
- **⚠️ 2026-10-09 19:5x 全库轴标更正(5 件联动)**:arXiv:2606.27663 的 **77.5 / 60.2 不是「扰动分」,而是 LIBERO-PRO 平均成功率**(原文 v1+v2 双版本均作 "average success rate",骨干 GR00T-N1.6)。原误读自 2026-09-29 起扩散至 **总图 v1.1.1 / 分图① v1.0.1 / 分图③ v1.1.1 / 综述 v1.0.2 / 立场文章 v1.0.2 + 账本一**,已逐件 append-only 更正。**处置零放宽:77.5 仍不作为数据引用、仍不与 GAM 61% 并列**(理由改为「扰动协议不同 + 骨干不同」);是否放宽属高风险锚点数字升级门,已提请委托人。**凡引用 77.5 / 60.2 或复用 P-004 三守则者,一律以更正后口径为准。** 详见 `maps/review-ledger.md`「按需重审履行记录」2026-10-09 19:5x 行 + `honor.md` 2026-10-09 条 + 提案 **P-013**(待批)。
- **⚠️ 2026-10-09 21:2x 精读 ×4 批量补做逾期体检(1 PASS / 2 PASS with notes / 1 FAIL)**:派 1 个异路径独立子 agent 打包(自行从四件正文提取编号与锚点、不采信主会话转述)+ 主会话独立 curl 复验(守 P-010)。**RMFP PASS**(v1 最新、全部锚点与轴标逐字吻合;RDP-xx→RDP-$x$ 笔误 + 60 演示出处补图注)、**π0 PASS with notes**(v4 最新、7 本体确证、待核点④ 关闭[arXiv comment 直证 "Published in RSS 2025"]、登记 RSS 25 作者 vs v4 24 人 + 元数据 "zero shot" vs 正文 "direct prompting")、**LiMA PASS with notes**(v1 最新、「六任务全胜或平」限定 SR 轴[PSR 2 格落后])、**⚠️ Morphometric FAIL**(**版本 stale 新失败模式首现**:据 v1 签发而 v2 于签发前 3 天[09-25]已发布;150fps 已删、匹配阈值 5mm→4.5mm、89.3% 须加「On a Sharpa hand」单手限定、v2 新增 bootstrap 显著性保留未载;**表格数字 v1=v2 全一致无张冠李戴**;核心结论未推翻、未外流)。**四件均升 v1.0.1、体检钟重置 2026-10-16**;Morphometric 录 `honor.md` 2026-10-09 条 + 起草 **P-014**(签发/重审前必核 arXiv 最新版本号,与 P-013 同源[外部体检打破本地自我确认]但根因不同[P-013 治轴标失真、P-014 治版本过期])。
- **⚠️ 逾期未体检队列(2026-10-09 21:2x 更新:精读 ×4 已清,剩 4 件;详见 `maps/review-ledger.md`「逾期未体检队列」表)**:透镜②(10-05,13 篇全量)/ 透镜①(10-05,16 篇全量)/ 教程(10-07,含 9 外部入口)/ 总图(10-07,骨架件最低优先)。**注**:总图 v1.1.1 与分图① v1.0.1 属「定点联动更正」,**不重置体检钟**(P-013 拟明文化)。
- **`designs/`(4 件 .md + README)**:`G2-选题依据-v0.1.md`、`桌面操作数据引擎-规格书-v0.1.md`(内部 **v1.0 已签发**)、
  `桌面操作数据引擎-规格书-v1.1-待改清单-v0.1.md`(流转中间件,不签发)、
  **`检索式策略设计空间自主搜索与可信测量-规格书-v0.1.md`(draft,未签发)**
- **`reports/drafts/`(16 件 .md + 2 个 `.mermaid`)**:含综述/立场文章/论文思路/图谱系列等
  **在制件**;立场文章正文与综述正文**已签发移入 `final/`**,drafts 内不再存正文件
- **⚠️ 本节计数已于 2026-10-16 校正**(原写 final 13 / designs 3 / drafts 5,均已过时);
  **完整策展待周五复盘**(P-009 记忆策展条)
- 依赖关系见 `maps/artifact-dependencies.md`;版本/重审见 `maps/review-ledger.md`。

---

## 维护纪律(借 consolidate-memory 纪律)

1. **一行一条,每条 <150 字**;索引**体积 ≤ 200 行 / ~25KB**。
2. **每周复盘策展**:合并重叠、删"易重得"的、把过期条目移除或折进耐久条目。
3. **新增卡片必须同步登记本索引**;未登记 = 视为未入库(下次复盘补)。
4. **本索引不是内容的副本**——只放**指路指针**,内容仍在各卡片。
