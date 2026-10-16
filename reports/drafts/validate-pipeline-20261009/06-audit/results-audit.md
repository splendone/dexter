# 结果审计 · exp-VP01 · 2026-10-09(dry-run 验证)

> **⑥ ResultsAuditor 产物 · dry-run 验证运行 · 🟡 诚实闸**
> ## ⚠️⚠️ 全篇占位水印:被审数据 `results.json` 标 `data_status: PLACEHOLDER_NOT_REAL`。以下所有「数字」均为编造占位,仅验证诚实闸机制。**签发结论 = ❌ 不放行**(占位数据不得进 ⑧ 正文)。真实运行须 ④ 在 GPU 实跑后重审。

## 0. 审计范围
- 被审:`04-sim/exp-VP01/results.json`(PLACEHOLDER)+ config.yaml(冻结,check_freeze.py PASS)
- 前置:查 `honor.md` 同类过失 → 命中「选择性引用/单双臂口径/off-by-one/声明代替修改」四条,逐条设为检查项
- 将进入:⑧ 论文正文(占位数字用 `\audittodo{}` 占位,**不写死**)

## 1. 待审数字清单(全口径,含不利数字)
| 数字 | 值(均值±std) | seed | 来源 config_id | 配置口径 | 全口径核对 | 备注 |
|---|---|---|---|---|---|---|
| R3_vla_frozen 成功率 | 31.0±1.6【占位】 | 5 | exp-VP01/R3_vla_frozen/s0-4 | 单臂·LIBERO-Pro·N300 | ✅ | 臂A |
| R3_harness 成功率 | 57.8±1.9【占位】 | 5 | exp-VP01/R3_harness/s0-4 | 同 | ✅ | 臂B |
| R3_cap 成功率 | 52.0±1.6【占位】 | 5 | exp-VP01/R3_cap/s0-4 | 同 | ✅ | 臂C |
| baseline_align_pi05 | 13.6±1.1【占位】 | 5 | exp-VP01/baseline_align_pi05/s0-4 | 同 | ✅ | 基线对齐检验 |
| R3_no_recovery_axis | 46.6±1.1【占位】 | 5 | exp-VP01/R3_no_recovery_axis/s0-4 | 同 | ✅ | 消融 |

- 不利数字在场:✅(占位集含 baseline 13.6% 低值、消融;真实运行须含失败/NaN)
- cherry-pick:✅ 否(5 seed 全列,未挑最优)

## 2. 显著性与方差(significance.py 实跑输出粘贴)
**对比:R3_harness(臂B)vs R3_vla_frozen(臂A),配对 n=5**
```
method 57.8±1.9 / baseline 31.0±1.6;均值差 +26.8pp;Cohen's d=15.2(巨大)
置换检验(配对,精确枚举)p=0.0625
⚠️ 检验力告警:n=5 配对最小可达 p=0.0625≥0.05 → 即便差异完全一致也无法达 p<0.05
判定:comparable / no significant difference(禁用比较级)
```
**审计结论(关键)**:尽管占位效应巨大(+26.8pp,d=15.2),**配对 n=5 检验力不足,不得写「harness 显著优于 VLA」**。→ 措辞降级为「描述性差异,需补 seed 至 n≥6 方可做显著性声称」。**这演示了诚实闸拦住「大效应但欠功效」的过度声称。**(呼应 significance-recipes.md §4「显著当重要」陷阱 + 配对小样本 p 下限)

## 3. 外部锚点完整口径(此处引 ① 已核真实数字,非占位)
| 锚点 | 引用值 | 完整口径 | 来源 | 抓取日 | 选择性引用? |
|---|---|---|---|---|---|
| LIBERO-Pro 数字跨度 | 12.8%–95.0% | ①今日 curl 核 15 个绝对值,≥9 种分母 | ①§0.2 结论C | 2026-10-09 | 否(全跨度,含最低12.8) |
| Frontier Models 预算效应 | 45%→94% | refinement 1→8 turns,模型/接口/环境固定 | OpenReview t08NEb8pTY | 2026-10-09 | 否(引完整区间) |
- WebFetch 超时项已改 curl 实抓:✅(①全程 curl,未用 WebFetch)

## 4. 跨配置迁移检查
| 数字 | 声明配置 | 锚点配置 | 匹配 |
|---|---|---|---|
| 三臂成功率 | 单臂(unimanual)·LIBERO-Pro·N300冻结子集 | 同 | ✅ |
- 跨 benchmark 版本比?否(全 LIBERO-Pro 1648-variants 口径)
- 单臂当双臂?否(embodiment=unimanual 全链一致,config/results 双处核)
- ⚠️ 保留:N=300 冻结子集 ≠ 官方全量 1648 → 结论域须限定「子集内」,不得外推全量(交 ⑧ limitation)

## 5. 基线对齐性检验(①Gap-1 最小实验,占位演示)
- 同一冻结 π₀.₅:R3_vla_frozen=31.0% vs baseline_align_pi05=13.6%【占位】→ **同骨干不同口径差 17.4pp**;
- 对照真实文献冲突值:Pigey 12.8% / DynaHarness 17.5% / MotorMind ≤13.3%(①§0.2,真实);
- **审计判断(占位演示)**:若真实跑出同骨干跨口径 ≥2 值不可同时逼近,则「连基线都不可比」被证实——这是本工作最硬的一张图(交 ⑦)。

## 6. 双向 Grep(本段为新建产物,无修正类旧串;占位水印核查)
- 新串「PLACEHOLDER_NOT_REAL / 占位」命中:✅(results.json + 本审计 + README 三处)
- 旧串「真实结果/已执行」残留:✅ 无(未声称真实执行)

## 7. 状态诚实核对
- 本审计未触发上游正文修正(新建);④ config/results 与本审计数字一致(31/57.8/52/13.6/46.6 逐条对results.json)✅
- 无「声明代替修改」:本段所有结论均可回指 results.json 或 ① 台账

## 8. 不利数字与保留项(不把没查到说成没问题)
- **保留项**:①数据为占位,非真实;②N=300 子集结论域受限;③配对 n=5 功效不足,显著性声称须补 seed;④跨路线同骨干不可行(③要件②),「同口径」是重定义;⑤ ①遗留 6 条邻接摘要 + 3 篇 OpenReview 作者身份未核。

## 9. 签发
- 五查:全口径✅ / 显著性✅(已降级措辞)/ 外部锚点✅ / 跨配置✅ / 双向Grep✅
- **但数据 = PLACEHOLDER → 全口径已核 = ❌ 不放行**
- **放行去向**:⑧ PaperScribe 只可用 `\audittodo{exp-VP01}` 占位,**不得写死任何占位数字**;⑦ 图表须标「占位数据」。
- 审计人 = {{INSTANCE_NAME}} 自查(2026-10-09);真实运行须 ④ 实跑后由独立子任务重审。

---
**诚实闸演示结论**:本段验证了 ⑥ 的两个拦截能力——(a)占位/未审计数据签发 ❌,挡在 ⑧ 正文之外;(b)大效应但欠功效(d=15.2 但配对 n=5 p 下限 0.0625)被 significance.py 拦为「禁用比较级」。两闸均生效。
