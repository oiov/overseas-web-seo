# 出海 SEO 与 GEO 实战 Skill

给 AI Agent 用的一套**出海网站 SEO + GEO 工作流**：从找词、判词，到新词站当天上线、养老站长期养护，再到 AI 搜索引用、外链与流量诊断。

不是关键词工具，也不是 SEO 软件。它是一份让 Agent 知道**该看什么数据、按什么顺序判断、哪些做法现在有政策风险**的操作手册，附带一个可批量打分的脚本。

```
你不会得到："这个词 KD 23，建议做。"
你会得到："Trends 从 9 月中开始上升、SERP 前两页还没有专门站、.com 被占但 .app 可注册；
         按新词站做，D0 上首页，D3 看 GSC 是否出词，D5 看要不要补低价积分包。"
```

---

## 为什么会有这个仓库

做海外站的人不缺工具，缺的是**判断顺序**：

- 一个词该追还是该放？
- 新站第一周到底该做什么、不该做什么？
- 为什么同样的内容别人被 ChatGPT 引用，你没有被引用？
- 流量掉了，是需求退潮还是排名下降？两者动作完全相反。
- 外链还要不要发？发多少？哪些做法现在会被 Google 判为 link spam？

这份 skill 把哥飞公众号的公开方法论、2026 年的出海实盘复盘、以及 Google 现行的搜索与垃圾内容政策，压缩成 Agent 可以直接执行的判断流程。它不收录任何付费社群的原文，也不复制案例截图和数据——只保留方法、边界和验证方式。

## 能力范围

| 你在做什么 | 它会带你走完 |
| --- | --- |
| 找一个值得做的词 | Trends 词根法、三条找词路线、判词四问、KGR / kdroi / KD 门槛、批量打分 |
| 判断一个词值多少钱 | 搜索意图、CPC、SERP 强弱、域名可注册性、AI Overview 风险 |
| 新词站当天上线 | D0–D5 按天 SOP、页面类型、收录、埋点与支付时机、定价锚定 |
| 养老站（老词长期站） | 选词过滤、站点结构、"分门别类罗列"、程序化 SEO 边界、变现、站点矩阵 |
| 让 AI 搜索推荐你 | GEO 打法、内容按节可检索、站外品牌与主题网络、引用效果衡量 |
| 品牌实体与主题地图 | 实体定义怎么写、主题域怎么分层、为什么内容多却没人引用 |
| 外链与站外推荐 | 冷启动路径、竞品外链逆向、成果按漏斗记录、现行政策红线 |
| 流量或排名下滑 | 需求退潮 vs 排名下降的判别表、算法更新窗口、恢复动作顺序 |

## 快速开始

### Claude Code / Claude Agent

```bash
git clone https://github.com/oiov/overseas-web-seo.git ~/.claude/skills/overseas-web-seo
```

装好后直接用自然语言提问，skill 会被自动加载：

> 帮我看下 "ai headshot generator" 这个词还值不值得做，按新词站还是养老站？

### Codex / 其他支持 AGENTS 类约定的 Agent

把仓库克隆到该 Agent 的 skills 目录，或在项目的 `AGENTS.md` / 系统提示里加一行（路径按你的实际位置改）：

```markdown
涉及海外站 SEO、GEO、找词判词、外链与流量诊断时，先读 <skills 目录>/overseas-web-seo/SKILL.md，再按其中的"按任务读取"表加载对应 references。
```

### 只想当文档看

`SKILL.md` 是总纲，`references/` 下每篇都能单独读。没有 Agent 也能用，只是判词时要自己执行里面的查询步骤。

## 目录结构

```
.
├── SKILL.md                      # 总纲：六条判断、两种打法、实时性要求、任务索引
├── references/
│   ├── find-and-judge.md         # 找词与判词：Trends、词根、KGR、kdroi、域名
│   ├── launch-sop.md             # 新词站 D0–D5、页面类型、收录、埋点、定价、留存、风控
│   ├── evergreen-site.md         # 养老站：选词、结构、程序化 SEO、维护、变现、矩阵
│   ├── geo.md                    # 让 AI 搜索引用或推荐你
│   ├── entity-and-topic-map.md   # 实体定义、主题地图、按节可检索的内容
│   ├── growth-and-diagnosis.md   # 外链、内链、老词优化、下滑诊断、站点改造
│   ├── evidence-led-growth.md    # 从增长案例到可验证的行动、外链成果漏斗
│   └── sources.md                # 每条经验的出处、时间与适用条件
├── scripts/
│   └── score_keywords.py         # 批量判词：kdroi / KGR / Trends 推算搜索量
└── examples/
    └── keywords.sample.csv       # 脚本输入示例
```

## 批量判词

把候选词整理成 CSV（只有 `keyword` 必填），用脚本排序：

```bash
python3 scripts/score_keywords.py examples/keywords.sample.csv --benchmark-daily 5000
```

列含义：

| 列 | 含义 |
| --- | --- |
| `keyword` | 关键词（必填） |
| `volume` | 月搜索量 |
| `kd` | 关键词难度 |
| `cpc` | 每次点击出价 |
| `intitle` | `intitle:"关键词"` 的结果数，用于 KGR |
| `trends_ratio` | 相对对标词的热度倍数，用于推算搜索量 |

脚本只做计算，不取数；`--benchmark-daily` 填你当次校准后的对标词日均搜索量。缺的列留空即可。

## 设计原则

1. **实时数据优先。** 结论必须来自当次查询的 Trends、SERP 和域名状态，不来自记忆或文章里的旧数字。拿不到数据就说拿不到。
2. **不编数字。** 搜索量、KD、收入、转化率，没有就写没有；估算必须标"估算"并写出算法。
3. **案例数字不外推。** 单站的流量和收入只属于那个站、那个时间窗口。仓库里只保留能迁移的判断和节奏。
4. **政策边界写清楚。** 站群抓取、买老域名、批量生成低价值页面、群发外链——早年有效，现在可能直接违规。每条建议都标了现行政策下的适用条件。
5. **先区分问题再给动作。** 需求退潮和排名下降的解法相反；没分清楚就动手，通常越改越差。

## 配套仓库

- **[backlink-submission-kit](https://github.com/oiov/backlink-submission-kit)** —— 外链投递母表、来源整理与提交记录。和本仓库的 `evidence-led-growth.md` 配套使用：本仓库负责判断"该发什么、发完怎么验收"，它负责把投递过程记成可复盘的台账。

## 边界

- 面向海外（英语及多语种）市场，不覆盖百度、微信搜一搜等国内搜索生态。
- 不替代付费关键词工具的数据；它教你怎么用，不替你买数据。
- 不承诺排名和流量。判词有运气成分，仓库里反复强调的做法是：多上站、把每一步做对、做复盘。
- 关于 JS 渲染、AI 爬虫训练与检索的区别，见 `entity-and-topic-map.md` 的"边界"一节。

## English

An opinionated SEO + GEO workflow skill for building overseas websites, written for AI agents. It covers keyword discovery and go/no-go scoring, a day-by-day launch SOP for trend-driven sites, long-term evergreen site operations, AI search visibility (GEO), entity and topic-map planning, backlink strategy, and traffic diagnostics — all anchored to current Google spam policies and public methodology rather than recycled case-study numbers.

```bash
git clone https://github.com/oiov/overseas-web-seo.git ~/.claude/skills/overseas-web-seo
```

Content is in Chinese; the structure and references are self-explanatory enough to follow with any translation layer.

## License

MIT. 使用方法与判断可以自由使用、修改、再分发；转载或改编时保留出处链接即可。
