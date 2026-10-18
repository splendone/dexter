# 产物依赖图

> **本图是什么**:把产物之间**隐含的依赖关系**显式化——每件产物的**上位依据**
> (它从哪来)与**下游产物**(它被谁引用),用于**重审时快速评估影响范围**:
> 改了 A,哪些 B/C/D 需要跟着重审?
> **补的缺口**:2026-10-08 优化方案甲档 A4(评审:"各产物之间的关系是隐含的")。
> **直接呼应既有过失**:`honor.md` 记录过"97.8 错误**先经总图 v1.0 再入分图**"
> ——正是**缺依赖图**导致影响范围评估失准。本图即为修此根因。
> **用法**:重审某产物前,先在下表查它的**下游**——下游须一并标记"待重审"。

---

## 依赖表

| 产物 | 上位依据(从哪来) | 下游产物(谁引用它) | 若更正 → 连带重审 |
|---|---|---|---|
| `reports/final/文献地图-v0.1.md`(总图 v1.1) | 四透镜分图 + 争论账本 | **G3 综述**(候选)、对外引用 | 四透镜分图(若总图口径改);下游综述 |
| `reports/final/文献地图-透镜①~④-v1.md` | 争论账本 + 数据集卡 + 经典书单 + 精读 | 总图、`designs/` 规格书、G3 教程/综述 | 总图 + 引用该透镜的规格书/稿件 |
| `reports/final/精读-*.md`(×4) | 各文 abs 页 / 全文 | 分图、争论账本 | 引用该精读的分图/账本 |
| `reports/final/教程-数据引擎-六路线-v1.md` | 分图④ + `license-check.md` + `dataset-selection-matrix.md` | 对外(委托人评估投稿)、**G3 综述/立场文章**(配比主张 A-017) | 教程内数字若改 → 回核分图④ |
| `reports/final/综述-四透镜×三股力量-v1.md`(v1.0) | 四分图 + 总图 v1.1 + 教程 + 争论账本三本 + 12 数据集卡 + 5 基准卡 | **G3 立场文章**(背景/分类框架)、G4(缺口指认)、对外(委托人评估投稿) | 综述内数字若改 → 回核四分图;下游立场文章 |
| `reports/final/立场文章-资产工程-v1.md`(**v1.0 已签发**,2026-10-09 M4) | 立项书 v0.1 + 大纲 v0.2 + 综述 v1.0.1(§2 分类框架底座)+ 账本一观察 v2/v3(6 件 agentic 资产线)+ 账本二缺口二 + 2610.10526(M3 全文核实六数)+ 2310.08864(R1 来源)+ 5 篇跨域/相邻域前人工作 | **G4 前置门第 4 项**(§6 两个缺口指认:资产质量度量 / 同预算受控对比范式)、**G3 里程碑④ 论文**(度量方案与受控对比协议)、对外(委托人评估是否投 arXiv 预印本) | **⚠️ 上位综述若更正 → 本文 §2 底座须重审**;支1 六件工作数字若被证伪 → §4 支1 + §5 R3 回应须重审;2610.10526 若有原文更正 → 支2 全节 + R1 回应须重审(六数已全文核实,属高价值锚点);跨域框架若被委托人否定 → 文首前置发现框 + §3 + §7 新颖性段须改写升版 |
| `reports/drafts/立场文章-资产工程-立项书-v0.1.md`(立项件,未签发) | 综述 v1.0 + 教程 v1.0 + 账本一(2610.10526/观察 v2·v3)+ A-017/A-018 | **✅ G3 里程碑③ 立场文章正文 v1.0 已签发**(M1-M4 全走完) | **⚠️ 核心主张已于 16:48 批复解除升级门(默许推进)**;主张若被委托人否定 → 立场文章 v1.0 须走重审升版(活文档) |
| `reports/drafts/立场文章-资产工程-大纲-v0.2.md`(M1 结构骨架,未签发) | 立项书 v0.1 + 账本一观察 v2/v3(6 件 agentic 资产线 ID)+ 2610.10526 + 账本二缺口二 | **✅ 已被立场文章 v1.0 取代**(8 节结构骨架全部落实为正文) | 结构若改 → 仅影响历史骨架件,不影响已签发 v1.0(v1.0 自身升版走重审记录) |
| `knowledge/maps/dataset-selection-matrix.md` | `license-check.md` + 12 数据集卡 | 规格书 §5、教程 | 规格书选型 / 教程许可段 |
| `knowledge/maps/controversies.md` | 各 abs 页 / 使用案例 | 四透镜分图、总图 | 引用该账本条目的分图 |
| `knowledge/datasets/*.md`(×12) | 官方页 / 论文 abs | 分图、选型表、规格书 | 选型表 + 规格书 |
| `knowledge/maps/benchmarks.md`、`benchmark-libero-pro.md` | 官方页 / 论文全文 | 分图①③、规格书验收 | 规格书验收目标值 |
| `designs/G2-选题依据-v0.1.md` | 分图③④ | `designs/` 规格书 | 规格书定题段 |
| `designs/桌面操作数据引擎-规格书-v0.1.md` | 分图④② + 选题依据 + 选型表 | 真人执行(采购/制作/实验) | 实测反馈回来 → 升版本 |
| `knowledge/maps/assumptions.md` | 各产物"待核点" | 重审触发(证伪 → 触发下游重审) | 受影响产物 |
| `knowledge/index.md` | 全部卡片 | 检索 | (索引本身不承载结论) |
| `reports/final/优化方案-autoresearch对标-常驻科研循环-v1.md`(**v1.0**,2026-10-16) | `github.com/karpathy/autoresearch` 源码(Contents API 起草 + jsDelivr 镜像复核)+ 10-08 优化方案 v1.0 + 10-15 G2 规格书 v0.1 + `AGENTS.md`/`heartbeat.md`/`proposals.md` | **`proposals.md` P-015~P-018**(待批)、`journal/rounds.tsv`(甲档 A1)、`heartbeat.md`(甲档 A2) | **P-015~P-018 若获批 → `AGENTS.md` v1.5 + `shift-start`/`goal-loop`/`re-review` 须同步**;autoresearch 若补 LICENSE 或改机制 → 本件 §1 须重审 |
| `journal/rounds.tsv`(轮次账,**2026-10-16 新建**) | 各轮 `journal/daily/` + `journal/latest.md` + `goals.md` 产出账 | 空转率 / 交付率 / revert 率统计、周报复盘 | (账本本身不承载结论,列为**结构性资产**) |
| `reports/final/优化方案-对标system_prompts_leaks-观察者与复核分档-v1.md`(**v1.0**,2026-10-16) | `github.com/asgeirtj/system_prompts_leaks`(Contents API 起草 + `git/blobs`/网页版复核;**同库第二遍对标**)+ `reports/final/优化方案-外部对标与自我诊断-v1.md`(**去重基线**,M1–M10 不得重取)+ `proposals.md`(P-018 为现有最大号)+ `AGENTS.md`/`heartbeat.md`/`agenda.md`/`identity.md`/`goals.md`/`promises.md` | **`proposals.md` P-019~P-023**(待批)、`heartbeat.md`(甲档 A2:未销账核对 + 档案路由头规则)、`identity.md`/`goals.md`/`agenda.md`/`promises.md`(甲档 A1:路由头) | **P-019~P-023 若获批 → `AGENTS.md` v1.5 + `shift-start`/`goal-loop`/`re-review` 须同步**;⚠️ **本件与 `优化方案-外部对标与自我诊断-v1.md` 同源同库**——若该件重审(如 P-006~P-010 被否)→ 本件 §1.0 去重对照须一并复核;外部库若改 `code-review` 档位公式或 `reminders` 声明结构 → 本件 §1.1/§1.4 逐字引文须重核 |
| `reports/final/优化方案-对标全天候科研智能体族-v1.md`(**v1.0**,2026-10-16) | **arXiv:2608.05179 综述**(WebFetch 起草 + arXiv API/`curl` HTML 复核)+ **7 个外部系统原文/仓库页**(AgentRxiv 2503.18102 / SakanaAI-AI-Scientist-v2 / DeepMind Co-Scientist 博客 / EvoScientist / research-town / Auto-Research-Skills)+ **本所前三件对标产物**(§1.0 去重基线,M1–M10 + 两件 10-16 件的全部条目不得重取)+ `AGENTS.md`/`heartbeat.md`/`agenda.md`/`proposals.md`/`review-ledger.md` | **`proposals.md` P-024~P-028**(待批)、`heartbeat.md`(**甲档 A1**:产物审计披露七维 + 检查点第 7 步)、`agenda.md`(**甲档 A2**:立项记录承接声明 + 在制件卡点) | **P-024~P-028 若获批 → `AGENTS.md` v1.5 + `shift-start`/`goal-loop`/`re-review`/`deep-read`/`weekly-review` 须同步**;⚠️ **与前三件「同层不同源」**——若 `优化方案-外部对标与自我诊断-v1.md`(10-08,M1–M10 来源)被重审 → 本件 §1.0 去重表须一并复核;若 10-16 两件(autoresearch / system_prompts_leaks)被重审 → 同理;外部综述若出 v2 或 `venue` 落定 → §1.2 逐字引文与 §1.3 自定位判据须重核;**P-026 若获批 → `identity.md` 增自主性自评段,届时本件 §1.3 成为其上位依据** |

## 两条硬规则

1. **改一件,查下游**——重审/更正任一产物前,先按本表列出其**下游**并标记"待重审";
   更正记录须写明"已核对下游 X 件"。
2. **上位总图优先核**——`honor.md` 的教训:"未流入已签发产物"类断言**必须逐件核对
   全部 `final/` 产物,尤其上位总图**;错误可能**先经总图再入分图**(传播方向与
   直觉相反)。**故核总图的下游 = 核全部分图。**

## 维护

- 新增产物 → 在本表加一行(上位依据 + 下游);
- 产物升版本 → 更新本表"上位依据"的版本标注;
- `reports/README.md`、`designs/README.md` 各有一行指针指向本图。
