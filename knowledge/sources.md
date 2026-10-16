# 信息源清单

> 冷启动初版(2026-09-27)。跑两周后按信噪比增删;新增源随手入册,失效源标 ⚠️。
> 抓取优先序:ego-browser(复用登录态)→ 内置网页检索;个别源失败如实记录,不编造。

## Tier 1 · 每日班必扫

### 论文源
| 源 | 入口 | 窗口期用法 |
|---|---|---|
| arXiv cs.RO 最新 | https://arxiv.org/list/cs.RO/recent | 按提交日过滤窗口期;盯 manipulation/dexterous/tactile/teleoperation/data 关键词 |
| arXiv API 检索 | https://export.arxiv.org/api/query?search_query=cat:cs.RO+AND+all:%22dexterous%22&sortBy=submittedDate&sortOrder=descending&max_results=15 | 结构化,适合自动化班次;四透镜各跑一条查询 |
| 顶会窗口 | CoRL / RSS / ICRA / IROS / CVPR 官网 | 只在投稿/放榜窗口期加扫 |

### 开源源
| 源 | 入口 | 窗口期用法 |
|---|---|---|
| GitHub 检索 | https://github.com/search?q=topic%3Arobotics+dexterous&type=repositories&s=updated&o=desc | 按 created/updated 排序,窗口期内新仓库 |
| HuggingFace | https://huggingface.co/papers (robotics 相关) + collections | 新 model/dataset 卡 |

## Tier 2 · 每日班轮扫(每周至少各两次)

### 中文产业源
| 源 | 入口 | 备注 |
|---|---|---|
| 机器之心 | https://www.jiqizhixin.com | 论文解读与产业动态并重 |
| 量子位 | https://www.qbitai.com | 产业动态 |
| 知乎机器人话题 | https://www.zhihu.com/topic/19588747/hot | 一手从业者讨论,置信度中 |

### 海外社区
| 源 | 入口 | 备注 |
|---|---|---|
| Physical Intelligence 博客 | https://www.physicalintelligence.company/blog | 操作方向风向标 |
| 实验室页 | Stanford IRIM / Berkeley AIR / CMU RI(官网 news) | 窗口期扫 |
| Reddit r/robotics | https://www.reddit.com/r/robotics/ | 低置信度线索源,须回溯原始出处 |

## Tier 3 · 周报级

- 政策与标准:工信部/标委会公开页,只记影响研究方向选择的信号。
- X/Twitter 研究者动态:按需人工触发,不进每日班(信噪比)。

## 失效与降级记录

- **2026-09-28 06:43 渠道修复(委托人提供本地代理)**:内置抓取失败时,
  优先用 **bash + curl 走本地代理**重试:
  `curl -sS -m 12 -x http://127.0.0.1:7890 <url>`
  (socks5 同端口:`all_proxy=socks5://127.0.0.1:7890`)。
  - **HuggingFace:已恢复**——网页版对程序化客户端 429,改用 API 端点
    `https://huggingface.co/api/daily_papers`(经代理可达)。开源雷达的
    HF 源以此为准。
  - **Physical Intelligence 博客:可达但 429**(拒绝程序化客户端)→
    改用 ego-browser(真实浏览器)访问,或经搜索引擎找转载;不硬磕。
- **教训(09-28 凌晨)**:arXiv 主查询 DNS 故障为瞬时,单次失败先重试
  再降级;arXiv 存在**索引滞后**,同一查询次日会出新条目,晨报次日复核。
- **2026-10-09 · arXiv 公告批次机制(承上条"索引滞后",细化到口径级)**:
  arXiv 以**每日 UTC 公告批次**入库,而非以提交时刻实时可查。API 返回的
  "最新条目"时间戳反映的是**已被索引的最新提交**,不等于**查询当日的所有
  提交**——举例:若窗口起点为 CST 08:00 = UTC 00:00,恰在批次公告时刻
  附近,则本轮 API 命中的可能是**昨日批次**的公告内容。
  → 硬规则(已入 `dexter-radar` v1.1.0 §1.6 与核心 `radar` 规程):
  ①每日简报**开头必写「⚠️ 窗口口径(诚实前置,先看这条)」小节**,先于
  任何论文条目;②小节内明确本轮口径是「窗口内新公开」还是「窗口内当日
  提交」,注明**最新 API 条目时间戳**与**批次公告时间估算**;③窗口起点
  紧邻 UTC 00:00 时,**当日 CST 08:00 后补一次 API 复核**(即本条"晨报
  次日复核"的机制化);④措辞禁区:不得把「窗口内新公开」表述为「今日
  提交 / 当日新论文 / X 月 X 日新出」。
  → 触发实证:2026-10-09 晨班 dexter-radar 子任务实测 arXiv API 最新
  条目为 `2026-10-07T17:59:41Z`,10-08 UTC 全天无新提交被索引;本轮
  16 篇均为「窗口内新公开」而非「10-08 当日提交」,若混称即口径失真。
- **2026-09-28 08:1x 渠道复核(A1,08:00 自动班)**:
  - **arXiv 主查询:✅ 直连已恢复**(实测 52KB/Top20 正常)——确认前日
    DNS 故障为瞬时;主查询恢复为第一入口,透镜备用查询保持第二。
  - **本地代理 127.0.0.1:7890:未启动**(curl exit=5)。arXiv 与 GitHub
    API 直连均可用;代理目前仅 HF 官方站刚需,不开也可工作(见下条)。
  - **HuggingFace:官方站直连超时维持;hf-mirror.com/api/daily_papers
    镜像可达(实测 50 条)→ 定为 HF 标准入口**。注意镜像列表为推荐位
    日期(非提交日),窗口期判断仍以 arXiv 提交日为准。
  - **Physical Intelligence 博客:09:1x 续班实测纠正**——
    `physicalintelligence.company/blog` 实际服务 `pi.website/blog`,
    **内置网页抓取直连可达**(实测取到完整博文索引,**未需 ego-browser**;
    官方站对程序化客户端 429 的旧结论据此降级)。**最新博文 = π0.7
    (2026-04-16)**,其前为 RL Token(03-19)、MEM 长短期记忆(03-03)。
    **无 2026-09 新动态**。上一班"最新可核 = 2026-02"的断言有误,
    已录 honor.md 并在此更正。→ 本渠道状态:**可达,列为 Tier 2 常扫**。
- **2026-09-29 补班渠道复核(协议口径)**:
  - **arXiv API:区分协议!**——**`https://export.arxiv.org/...` 可用**(实测 60 条
    正常);**`http://` 出口超时**(upstream connect failed)。→ 前条"直连可用"
    须补**协议限定:一律用 https**。
  - **`arxiv.org/abs/<id>` 页:可用**(本班 19 篇全部取到原始 HTML,复核 24 篇
    亦走此入口)。
  - **PDF 全文抽取(2026-09-30 新增)**:系统 `pdftotext` **已损坏**
    (dyld: missing libtiff)→ 改用 **venv 的 pypdf**:
    `/Users/splendone/.workbuddy-ai/binaries/python/envs/default/bin/python3`
    (已装 pypdf);`PdfReader('x.pdf')` 逐页 `extract_text()`。**抓 PDF 用
    `https://arxiv.org/pdf/<id>`**(与 abs 页同域,https 通)。
  - **GitHub API:可用**;**HF `hf-mirror.com/api/daily_papers` 可用**(镜像列表
    为推荐位日期,非提交日;本轮由它发现 2609.33378)。
  - **Physical Intelligence 博客:`https://pi.website/blog` 返回 429**
    (09-28 曾可达,本轮回退)→ 状态改记"**不稳定,时通时 429**";
    **机器之心:首页 JS 渲染,直连 HTML 无正文**(3.2KB 壳)。
    按宪法,**未取到即写"未获取",不写"最新为 X"**(09-28 PI 漏报教训的直接适用)。
- 新增发现渠道:**Awesome-Dexterous-Manipulation**
  (github.com/chang-xinhai/Awesome-Dexterous-Manipulation,**★24 元清单**
  [2026-10-09 主会话 curl GitHub API 实测 `stargazers_count:24`,
  `pushed_at:2026-10-05`;由 ★20 升,雷达子任务实测值经外部源核实],
  覆盖 dexterous manipulation / tactile sensing)——每周扫一次增量。
- 备忘:委托人将另开会话监察工作并调整部署,一切状态以 latest.md 与
  journal 落盘为准。
