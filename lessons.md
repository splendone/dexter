# 教训档案

每周复盘时(以及每次发现明显失误时)追加。格式:

```
## YYYY-MM-DD · 教训一句话
- 发生了什么:…
- 根因:…
- 修正案:改了哪条守则/技能的哪一处(或建议怎么改)
```

教训不重复记;同类教训第二次出现时,必须升级为守则/技能的明文修正。

---
(暂无,等第一次复盘填入)

## 2026-09-28 · 编辑共享档案前先取现状,不凭记忆构造 old_string
- 发生了什么:重负载班整合并行子任务结果时,凭记忆构造 agenda.md 与
  datasets/README.md 的 old_string 连续三次失配(把不同轮次的措辞、
  缩进混叠),浪费三轮编辑。
- 根因:同一天多轮编辑同一文件,记忆中混叠了多个历史版本;Edit 失败
  后仍用回忆而非读文件。
- 修正案:对当日已编辑过 ≥2 次的档案,先 bash sed/grep 取准确现状,
  再构造 old_string。

## 2026-10-09 · zsh 下批量 curl 用 `for x in $VAR` 会触发 `Malformed input`,不是渠道故障
- 发生了什么:dexter-radar 子任务首次批量抓 arXiv abs 页,把 16 个 ID
  存进 `$IDS` 后写 `for id in $IDS; do curl ".../abs/$id"; done`,首个
  curl 立即报 `curl: (3) URL rejected: Malformed input to a URL
  function`。第一反应是"arXiv 又抽风了"、准备走内置浏览器降级——
  排查后才发现是 shell 方言坑,与源无关。
- 根因:**zsh 不对未加引号的 `$VAR` 做词分割**(与 bash 不同,bash 下
  `for x in $VAR` 会按 IFS 拆开)。所以 zsh 里 `$IDS` 展开为**一个整串**,
  curl 把整串当单个 URL 传入,ID 里的空格让 URL 语法非法,直接拒绝。
  → 这是**语言实现差异**,不是渠道故障,不该触发降级到浏览器/代理;
  → 也是**为什么第一次报错误导判断**——`Malformed input` 的字面意思
  像"源返回了脏数据",实际是"我们自己传了脏 URL"。
- 修正案:
  - **首选:在 for 中直列 ID**——`for id in 2610.12345 2610.67890 ...; do ...`
    (最稳,不依赖任何 shell 特性);
  - **zsh 强制分词语法**:`for id in ${=IDS}; do ...`;
  - **管道分词**(bash/zsh 通用):`echo $IDS | tr ' ' '\n' | while read id; do curl ...; done`;
  - **显式走 bash**:`bash -c 'for id in '"$IDS"'; do ...; done'`。
  - **规程落地**:已入 `dexter-radar` v1.1.0 §7 规则与 §8 常见错误;核心
    `radar` 规程同步补入(见 SKILL.md v1.1.0)。**分流规则**:shell 方言坑
    **不入 `knowledge/sources.md`**(不是源故障),入本档 `lessons.md`。
  - **诊断口诀**:批量 curl 首条即报 `Malformed input` → **先 `echo "$VAR"`
    看是不是整串**(而非逐个 ID),再决定是否降级。

## 判例 · arXiv comment ≠ venue(2026-10-15,领域级图谱 Phase 2 ①⑤⑥⑦ 深挖)

- **情境**:核论文"发表于哪个顶会顶刊"时,两路子 agent 对 Isaac Gym(2108.10470)与 HumanPlus(2406.10454)
  给出冲突结论——一路报"NeurIPS 2021 D&B / CoRL 2024"(查 S2+DBLP / GitHub+OpenReview),另一路报
  "venue 未核实(arXiv comment 仅 tech report / project website,Crossref 误配)"。
- **定论(一手核定)**:Isaac Gym = **NeurIPS 2021 Datasets & Benchmarks Track(Round 2)**(nips.cc 官方录用列表 +
  OpenReview id=fgFBtYgJQX_);HumanPlus = **CoRL 2024**(PMLR v270 fu25a,pp.2828-2844 + Best Paper Finalist)。
  **"未核实"结论错在只查 arXiv。**
- **教训(可复用,入证据纪律)**:**arXiv 的 `comment`/`journal_ref` 字段 ≠ venue 真值**。NeurIPS D&B track、
  CoRL/ICRA camera-ready 滞后、技术报告类论文,其录用信息**常不写进 arXiv comment**(Isaac Gym comment 仅
  "tech report on isaac-gym";HumanPlus comment 仅 "project website")。**不能以"arXiv 无 journal_ref"推定
  "venue 未核实"**——必须查官方论文集:nips.cc / papers.nips.cc(D&B track 有独立列表)/ proceedings.mlr.press(CoRL/AISTATS)/
  roboticsproceedings.org(RSS)/ IEEE Xplore(ICRA/IROS)/ OpenReview(ICLR/NeurIPS)/ Crossref DOI。
- **预防**:①venue 核实须**多源**(arXiv comment + 官方论文集 + Crossref/OpenReview),单一 arXiv 不足以定"未核实";
  ②两路子 agent venue 冲突时,**不硬断言也不简单降置信,而是查官方论文集一手核定**;③"未核实(仅 arXiv 预印本)"
  这一标注**只在查遍官方论文集仍无录用证据时才用**,否则会误把已发表论文标成预印本(Isaac Gym/HumanPlus 即此误)。
- **同源**:与"提缺口前先检索新颖性"(2026-10-13 honor)、"轴标断言须附原文逐字引句"(P-013)、
  "签发前必核 arXiv 最新版本号"(P-014)同属证据纪律——**都是"未核即写/单源即断"的变体**。

## 判例 · Crossref `total-results:0` ≠ 未发表(2026-10-15,领域级图谱 Round 2 权威性检验;上一条判例的**对称规则**)

- **情境**:承上条判例("arXiv comment ≠ venue")做 Round 2 权威性检验时,把 venue 核实扩展到 Crossref——
  结果 **Crossref 对 RoboArena、STRAP、vla-eval 三者均返回 `"total-results":0,"items":[]`**
  (`api.crossref.org/works?query.title=…&query.author=…`,HTTP 200 / 186 B;书目模糊检索亦只返回同题无关条目)。
  **若照"上条判例的反面"推理(即"arXiv 无 journal_ref + Crossref 无 DOI ⇒ 未发表"),就会把三篇均已录用的
  论文一并误标为预印本**——事实上图谱 Phase2-分支①⑤⑥⑦ §2.3 正是这样推出了"对撞层没有一篇经同行评审正式发表"
  的**全称断言**,并被本轮证伪。
- **定论(一手核定,两个及以上独立外部源)**:
  - **RoboArena(2506.18123)= CoRL 2025(The 9th Conference on Robot Learning)Oral,PMLR 305:336-364, 2025**。
    **Crossref 返回 0**,但 **PMLR 官方论文集** `proceedings.mlr.press/v305/atreya25a.html`(HTTP 200 / 19,660 B)
    逐字给出卷页,**OpenReview** id=`cpmwi3Xwcr` 给出 `venue: CoRL 2025 Oral` +
    venueid=`robot-learning.org/CoRL/2025/Conference` + invitations 含 `Spotlight_And_Camera_Ready`。
  - **STRAP(2412.15182)= ICLR 2025 Poster**(OpenReview id=`4VHiptx7xe`,invitations 含 `Camera_Ready_Revision`,
    bibtex booktitle "The Thirteenth International Conference on Learning Representations");Crossref 同为 0。
    另有两个 **CoRL 2024 工作坊** Poster(MRM-D / X-Embodiment)→ **这也解释了先前"PMLR v270 检索无 Memmel/
    Sub-Trajectory"的负向结果:工作坊不进主会论文集,检索为负是预期,不是"未发表"**。
  - **vla-eval(2603.13966)= ICRA 2026 工作坊 "From Data to Decisions" Poster**(OpenReview id=`IpKQsHWaYS`,
    **venueid 明含 `Workshop`**);Crossref 同为 0,arXiv abs 页 `comment`/`journal_ref` **两字段均无**。
- **教训(可复用,入证据纪律)**:**Crossref 的"没有记录"不是"没有发表"的证据。**
  **PMLR 系(CoRL / AISTATS / UAI 等)与 OpenReview 系会议(ICLR / NeurIPS)多数不注册 Crossref DOI**;
  Crossref 只对**有 DOI 的 IEEE / RSS / 期刊**有效(RSS 有 `10.15607/rss.*`)。
  → **一般化的根因:缺席证据(argument from absence)只在"该源确实覆盖此类出版物"时才成立;
  当该源本就不覆盖此出版物时,缺席证据完全失效,且失效方式是"静默的"(返回 0 看起来像查过了)。**
  → 这与上条判例是**同一错误的两个方向**:上条是"arXiv 没写 ⇒ 没发表",本条是"Crossref 没有 ⇒ 没发表";
  **两者都是把'某单一源的沉默'当成'世界的否定事实'**。
- **venue 核实的正源顺序(按证据力排序,⚠️ 不得跳级用弱源否证强源)**:
  1. **arXiv `comment` / `journal_ref`** —— **线索级**,常缺,**既不能证实也不能否证**;
  2. **官方论文集站** —— `proceedings.mlr.press`(**卷号 + 卷页**;卷号对照表在站首页,如
     v229=CoRL 2023 / v270=CoRL 2024 / **v305=CoRL 2025**)/ `papers.nips.cc`(NeurIPS,**D&B track 有独立列表**)/
     `roboticsproceedings.org`(RSS)/ **IEEE Xplore**(ICRA/IROS);
  3. **OpenReview** —— 看 `venue`/`venueid` 字段;**invitations 里出现 `Camera_Ready` /
     `Spotlight_And_Camera_Ready` / `Camera_Ready_Revision` = 强录用信号**;
     **⚠️ 必看 `venueid` 是否含 `Workshop`——工作坊 ≠ 主会,不得径写会议名**(否则会与同会议主会论文构成
     "同标签不同层级"混淆,如 vla-eval 的 ICRA 2026 Workshop vs RoboEval 的 ICRA 2026 主会);
  4. **Crossref DOI** —— **仅对有 DOI 的 IEEE/RSS/期刊有效**;**返回 0 只证明"Crossref 没这条"**;
  5. **DBLP** —— 可用时用;**⚠️ 本轮 4 次请求 3 次 HTTP 202(排队返回非 JSON)+ 1 次 HTTP 429(限流),
     未取得任何数据 → 交叉源缺位必须如实登记,不得当作"查过了没有"**。
- **预防**:
  ①**任何"未发表/未核实"结论都必须是"查遍正源顺序 2-3 级仍无录用证据"的结论**,不得由单一弱源(arXiv comment
  或 Crossref)的沉默推出;
  ②**"未核实" ≠ "未发表"**——两者必须分开标注;"未核实"只表示本所尚未查证,**不携带任何发表状态的断言**;
  ③**全称/多数断言("无一…"、"全部是…")风险最高**:一个反例即整体崩塌(RoboArena 即为反例)→
  **凡对一批论文作发表状态的全称断言,必须逐个走 OpenReview + 官方论文集,否则改写成分层表述
  (已发表 / 仅工作坊 / 未逐一核实)**;
  ④**反向也要防**:既然"Crossref 0 + arXiv 无 journal_ref"的 RoboArena 实际已 CoRL 2025 Oral,
  **其余标"未核实"的条目同样可能低估其发表状态**——"未核实"不是安全港,是待办。
- **同源**:与"arXiv comment ≠ venue"(2026-10-15,上条)、"提缺口前先检索新颖性"(2026-10-13 honor)、
  "轴标断言须附原文逐字引句"(P-013)、"签发前必核 arXiv 最新版本号"(P-014)同属证据纪律。
  **⚠️ 按本档规则"同类教训第二次出现须升级为明文修正":这是"单源沉默即断言"型错误的第二次出现
  (第一次 = arXiv comment)→ 建议把上述"venue 正源顺序 + 全称断言禁令"升格为 `re-review` /
  `deep-read` 技能的明文条目(修宪/修技能须经委托人批准,提案走 `proposals.md`)。**
- **落点**:`reports/drafts/领域级图谱-权威性检验记录-v0.1.md` §1 D 本轮补注 + §2 N3 方法论扩展 + §4.2;
  `reports/drafts/具身智能领域级图谱-v0.1.md` §8.5 方法论段(对称规则 + 正源顺序);
  `knowledge/maps/controversies.md`「补充:N1–N7 新增定案」节末方法论扩展;
  `reports/drafts/领域科研路径图谱-Phase2-分支①⑤⑥⑦深挖-v0.1.md` §2.3 更正记录 / §5.3 / §6。
