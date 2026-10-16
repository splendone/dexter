---
name: radar
description: Dexter 论文雷达与开源雷达规程。扫描 arXiv cs.RO 与 GitHub/HuggingFace 中与操作与灵巧手(四透镜)相关的最新论文与项目,产出带出处、相关性与置信度的雷达条目。当执行每日班、委托人说"跑雷达/看看今天有什么新论文新项目"时使用。
---

# 论文雷达 + 开源雷达规程

先读 `identity.md` 的相关性锚点(操作与灵巧手 + 四透镜),再开扫。
**本规程的生死线:只报实际打开过原文摘要的条目;摘要内容逐句忠于原文;
宁可少报,不可报错。**

## 1. 论文雷达

1. **定窗口**:读 `journal/latest.md`,窗口期 = 自上次班次以来。
2. **抓取**:优先 arXiv API(结构化、可重复):
   `https://export.arxiv.org/api/query?search_query=cat:cs.RO+AND+(all:"dexterous"+OR+all:"manipulation"+OR+all:"tactile"+OR+all:"teleoperation")&sortBy=submittedDate&sortOrder=descending&max_results=20`
   四透镜各跑一条查询(泛化/language-conditioned/data collection 另出)。
   **内置抓取失败时,用 bash + curl 走委托人本地代理重试**:
   `curl -sS -m 12 -x http://127.0.0.1:7890 <url>`(详见 sources.md 失效记录);
   HuggingFace 一律走 API 端点 `/api/daily_papers`。个别源失败如实记录,
   换替代入口,不编造。
3. **打开摘要**:候选逐条打开 abs 页核对——摘要要点、作者、机构、日期。
   **凭标题不确定内容的一律不开进简报**(进待核区,写明需要打开确认)。
4. **判相关性**:对照四透镜给 高/中/低 + 一行理由。判"这是判断",
   与摘要内容分开写。
5. **限额**:高相关 ≤3 条置顶详写,总条数 ≤8;超出的合并一行带链接,
   不凑数灌水。

## 2. 开源雷达

1. GitHub:`topic:robotics` + dexterous/manipulation/tactile,按 created/
   updated 排序取窗口期内;HuggingFace papers 页 robotics 相关新条目。
2. 每条:仓库/数据集名 | 链接 | 干什么(读 README 一段,不脑补)|
   活跃度(star/最近提交,标注读取时间)| 相关性 + 理由。≤3 条。
3. 值得深挖的 → 写入 `agenda.md` 待办池(发现问题 → 立项是常规职责)。

## 3. 落盘

- 按 `journal/README.md` 模板写入当日 `journal/daily/YYYY-MM-DD.md`;
- 高相关论文中,委托人可能要精读的 → 在简报"交接班"里列"建议精读清单",
  **不自行开写精读**(保守档);委托人点名后走 `deep-read` 技能;
- 收工走 `shift-start` 第 4 步。

## 质量门

- 每条带链接;摘要转述与"我的判断"分段;
- 抓取失败的源写明 URL 与原因,换替代入口,不编造;
- 待核区条目必须写清:卡在哪、需要什么才能核实。
