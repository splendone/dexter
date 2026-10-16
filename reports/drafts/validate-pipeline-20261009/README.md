# 论文流水线全链验证运行(dry-run)· 2026-10-09

> **性质**:`paper-autopilot` 十段流水线的**验证运行**,非真实可投稿论文。
> **选题方向**:透镜③ 语言条件长程操作 —— LIBERO-Pro 上「端到端 VLA vs agentic harness vs code-as-policy」三路线**同口径公平对照**。
> **工作目录**:Dexter 现有 workspace(委托人 2026-10-09 选定)。

## 硬边界(诚实条款,先读)

1. **占位数据水印**:④ 仿真训练与 ⑤ 真机采集**未真实执行**(AI 无 GPU/真机)。⑥–⑩ 使用的一切实验数字均为**明确标注的占位值(PLACEHOLDER)**,仅用于验证诚实闸、衔接与门控机制,**不可用于真实投稿**。凡占位数字处均标 `【占位·非真实结果】` 或 LaTeX `\audittodo{}`。
2. **不触碰真实里程碑**:G3 里程碑④「研究论文」在 `agenda.md` 中**硬阻塞**于 G2 实验数据(「反馈到达前不启动」)。本验证运行**隔离于本命名空间**,**不修改** goals.md / agenda.md 的真实里程碑状态,不声称论文线已启动。
3. **红色事项不执行**:⑩ 只做投稿**备料** + 授权门演示,**不投稿、不署名、不发送**;真机 ⑤ 只出协议清单,**AI 不碰硬件**。
4. **真实 vs 占位分界**:①②③(选题/综述/方法设计)产出**真实档案**,grounding 在 workspace 已四源核实的 LIBERO-Pro 素材 + 真实 arXiv 核查;④⑤ 出**真实备料**(config/协议,不执行);⑥–⑩ 用**占位数据**验证机制。

## 十段产物索引

| 段 | Agent | 门控 | 产物 | 真实性 |
|---|---|---|---|---|
| ① | GapScout | 🟡 | `01-gap/gap-candidates.md` | 真实(实抓 arXiv) |
| ② | SurveyWeaver | 🟢 | `02-survey/survey.md` | 真实(复用已签透镜③图) |
| ③ | MethodArchitect | 🟡 | `03-method/method-spec.md` | 真实设计 |
| ④ | SimRunner | 🟢 | `04-sim/exp-VP01/` + check_freeze 输出 | 真实备料·未执行 |
| ⑤ | RealBotOperator | 🔴 | `05-realexec/protocol.md`(本题纯仿真,标可选) | 真实备料·未执行 |
| ⑥ | ResultsAuditor | 🟡 | `06-audit/results.json`(占位)+ `results-audit.md` + significance.py 输出 | **占位数据** |
| ⑦ | FigureSmith | 🟡 | `07-figures/figure-spec.md` | 占位数据可视化 |
| ⑧ | PaperScribe | 🟢→🟡 | `08-paper/`(latex-skeleton 实例) | 占位数字 \audittodo |
| ⑨ | RedTeamReviewer | 🟢 | `09-redteam/mock-review.md`(独立子agent) | 真实审稿预演 |
| ⑩ | SubmissionPilot | 🔴 | `10-submission/`(选刊+合规+包+授权门) | 真实备料·不提交 |

## 验证目标(本次要证明什么)

- [ ] 每段产物落在正确位置,消费上游产物(衔接链通);
- [ ] 门控生效:⑥ 诚实闸拦占位数字进正文、⑨ 独立子agent 抓弱点、⑩ 授权门拦住自动投稿;
- [ ] 工具可跑:`check_freeze.py`(④)、`significance.py`(⑥)实跑通过;
- [ ] 调度制:重活派子agent(①、⑨),主会话轻量验收(双向核验);
- [ ] 诚实纪律:占位全程水印、真实/占位分界清晰、不假称已执行/已投稿。

---
发起 = {{INSTANCE_NAME}}(2026-10-09 21:06 CST)| 性质 = dry-run 验证 | 署名 = 不署名 | 投稿 = 不投稿
