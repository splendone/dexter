# 方法规格书 · LIBERO-Pro 三路线中立对照(R3-NeuTraL)· v0.1(dry-run 验证)

> **③ MethodArchitect 产物 · dry-run 验证运行 · 2026-10-09 · 🟡 级(草稿,未签发)**
> **上游**:① gap-candidates(Gap-1 骨架 + Gap-2 metric 内核)、② survey(口径分歧账本 + 让位边界)。
> **硬边界**:纯仿真研究,④ 不真实执行(无 GPU);本规格书是**可交真人落实的设计**,数字锚点全为占位。
> **红线自检**:无人身安全/大额采购/危险操作(纯 sim + 公开基准 + 闭源 API 调用费须人批预算 🔴)。

## 要件① 方案(What & Why)

**工作名**:R3-NeuTraL(Routes×Recovery, Neutral Third-party, Aligned-caliber on LIBERO-Pro)。
**一句话**:在 LIBERO-Pro 官方扰动类目分层抽样的**公开冻结子集**上,把端到端 VLA / agentic harness / code-as-policy 三臂在**同一分母、同一 50 回合/任务协议、同一成功判据、同一 LLM 调用预算与 token 计量**下并列评测,并新增**恢复率 + 成本双轴**,产出中立路线剖面 + 可复跑协议工件。
**差异化(让位后仍守住的,回指 ②§3)**:①中立第三方(非同群自我对照)②官方 1,648 变体分母(非私有子集)③含训练式 VLA 平等臂(补 `t08NEb8pTY` 缺口)④恢复/成本双轴(Gap-2,与最强在投威胁正交)。**不声称同口径方法论首创**(让位 `t08NEb8pTY`)。

## 要件② 选型(三臂骨干口径 — 回应 ①待核#7「同骨干物理不可通约」)

| 臂 | 骨干 | 可训练? | 口径处理 |
|---|---|---|---|
| A 端到端 VLA | π₀.₅ / OpenVLA(开权重) | 是 | 冻结评测 + 报告微调版(若有) |
| B agentic harness | 同代最强可用前沿 VLM(公开身份,如 GPT-6 Astra 级) | 否(闭源) | 固定骨干版本 + 公开身份 + 记 API 成本 |
| C code-as-policy | 同 B 的 VLM 作 planner + 公开 primitive 库 | 否 | 同 B |

**工程结论(诚实条款)**:跨路线「同骨干」**物理不可行**(A 开权重可训练、B/C 依赖闭源前沿 VLM)。→ 「同口径」**重定义**为:同代最强可用骨干 + 公开骨干身份与版本 + 统一报告 LLM 调用数/token/墙钟成本。此重定义须写进论文 limitation,是审稿风险点(交 ⑨ 预演)。

## 要件③ 冻结子集抽样规则(回应 ①待核#8 — 否则自己变成第 10 种分母)

- 锚定官方口径:22 static perturbations + 20 runtime interventions / 1,648 validated variants(`6xlHe08ZsL`,①§0.2);
- **分层抽样**:按 7 大扰动类目(scene/object/visual/robot-state/temporal/instruction/runtime)分层,每类按比例抽,总量冻结为 **N=300 变体**(算力约束下的可行性折中,①待核#9);
- **规则公开**:抽样种子、每类配额、纳入/排除判据全部写入协议工件并开源 → 可复跑、可审计;
- 每变体 **50 回合/任务**(官方协议,基准卡 v2 PDF §5.1 逐字)。

## 要件④ 接口(评测协议工件)

- 统一成功判据(官方 task goal state);
- 统一 budget 计量:每回合 LLM 调用数 / input+output token / 墙钟,三臂同上限;
- 恢复轴测量装置:**复用 RoboAware 的 State-Locked Counterfactual Branching**(①来源/②§3,已发表装置,不自建基建);
- runtime interventions 类目天然作恢复测试床(主动注入失败→测能否爬回,①Gap-2 可验证性)。

## 要件⑤ 实施步骤(交 ④ SimRunner)

1. 冻结子集生成(种子固定)→ `tests/exp-VP01/`;
2. 三臂 × N=300 × 50 回合 rollout(预算上限统一);
3. 采集:终局成功 / 首次失败步索引 / 恢复率 / 恢复延迟 / 任务级全灭率(reward coverage 补集)/ 成本;
4. 多 seed(≥5)→ results.json;
5. **基线对齐性检验**(①Gap-1 最小实验):同一冻结 π₀.₅ 重跑,看能否同时逼近 12.8%/17.5%/≤13.3% 三值——若 ≥2 个不可同时逼近,「连基线都不可比」被证实(最硬的一张图)。

## 要件⑥ 验收判据(可证伪,回指 ①Gap-1/2 设想)

- **主判据**:三臂排序**随扰动类目翻转**(无单一路线全胜)→ gap 成立;
- **副判据**:任一臂绝对成功率**无法复现其原论文自称数字**(偏差 >10pp)→ 证实「12.8%–95.0% 跨度主要由口径而非能力驱动」;
- **恢复判据(Gap-2)**:B/C 恢复率显著高于 A,但恢复延迟也显著更高;object/position 静态扰动上三臂恢复率差异消失;
- **null-result 预案(诚实)**:若预算效应 >> 路线效应,结论转为「路线不重要,预算才重要」——仍是可发表 null result,但卖点须预先接受(①Gap-1 价值栏风险,🔴 委托人裁决项)。

## 要件⑦ 实验设计(矩阵,交 ④ experiment-matrix)

| variant | role | 臂 | seed | 配置口径 |
|---|---|---|---|---|
| R3_vla_frozen | method(A) | 端到端 VLA 冻结 | ≥5 | sim·LIBERO-Pro·N=300 冻结子集 |
| R3_harness | method(B) | agentic harness | ≥5 | 同子集·同预算 |
| R3_cap | method(C) | code-as-policy | ≥5 | 同子集·同预算 |
| baseline_align_pi05 | baseline | 冻结 π₀.₅ 基线对齐 | ≥5 | 同子集(验 12.8/17.5/13.3 冲突) |
| (消融)R3_*_no_recovery_axis | ablation | 去掉恢复轴 | ≥5 | 证恢复轴的增量信息 |

## 要件⑧ 诚实条款(残余不确定性)

1. 跨路线同骨干不可行 → 「同口径」是重定义,非字面同骨干(审稿风险);
2. N=300 冻结子集是算力折中,非官方全量 1,648 → 结论域限定在子集;
3. 闭源 VLM 骨干版本会漂移 → 须锁版本 + 记调用日期,否则不可复现;
4. ① 遗留 6 条邻接摘要 + 3 篇 OpenReview 作者身份未核 → 新颖性让位边界可能再变;
5. **null-result 风险真实存在**,立项即须接受;
6. **时间窗压力**(①判断,高置信):该作者群已握三路线基建,2–3 周内不出首批数字则新颖性大概率被吃掉。

## BOM / 预算(🔴 须人明示)

- 算力:~N=300×50×3臂×5seed ≈ 22.5 万 rollout(冻结子集已比全量 25 万+ 收窄);
- 闭源 API 调用费:三臂 B/C 依赖前沿 VLM → **云/API 预算锚点须委托人明示**(🔴,一句话批复不覆盖);
- 本 dry-run **不执行**,预算仅估算。

## 交接 ④

要件⑤实施步骤 + 要件⑦矩阵 → ④ SimRunner 据此生成 `tests/exp-VP01/` 冻结目录(config.yaml/seeds/run.sh),用 experiment-runner 的 freeze-template 实例化,跑 check_freeze.py 验证冻结纪律。**④ 不真实训练**(无 GPU),只产真实 config 备料 + 占位 results 交 ⑥。

---
起草 = {{INSTANCE_NAME}}(2026-10-09)| 复核 = 待 ⑨ | 状态 = v0.1 dry-run 草稿(🟡 未签发;真实运行须走 design-spec 会签前自查复核 + 委托人 🔴 裁决 null-result/预算/时间窗)
