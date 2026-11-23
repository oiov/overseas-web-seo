---
name: overseas-web-seo
description: 面向海外用户的网站 SEO + GEO 实战流程（哥飞方法论、新词站与养老站两种打法、2026 实盘复盘与 Google 现行政策）。用于：找新词/词根挖词、判断一个关键词值不值得做、新词站上线 SOP、养老站（老词长期站）选词建站与维护、品牌实体定义与主题地图规划、让内容更易被 AI 搜索检索引用、外链与站外主题网络、广告与订阅变现、诊断流量或排名下滑。适用于任何出海工具站/AI 站/内容站/游戏站项目；不用于国内百度/微信搜一搜优化，也不用于纯付费投放。
---

# 出海网站 SEO + GEO

把搜索需求变成能拿到流量和收入的网站。核心判断来自哥飞公众号方法论、公开的出海实盘复盘，以及 Google 现行政策文档；细节放在 references 里，按任务读取。

## 先记住的六条判断

1. **搜索量来自共识。** 很多人用同一种说法搜同一件事，才有搜索量。自己起的品牌名没人搜；社交媒体刚爆的玩法会在几天内形成新共识，这就是新词窗口。
2. **每个关键词都是一张独立排行榜。** 只跟这个词首页和前 20 名的页面比，不跟全网比，也不拿别人做的另一个词的指标来比。
3. **新手追新词，老手做难而正确的事。** 新词参与竞争的页面少，3–5 天内 GSC 就该有数据，3–5 周内该有排名。老词要靠持续的外链、内容和时间，周期以月和年计。
4. **用户要什么就做什么页面。** 要信息给图文，要功能给工具，要游戏给能玩的页面，要文件给下载。博客只是其中一种，不是默认答案。
5. **速度先于完美，但质量不能缺。** 新词站首页可以当天只是一个页面；但文案、FAQ 和长尾内页必须能回答用户的问题，因为 Google 排名和 AI 引用都看这一点。
6. **机器要先认识你，才谈得上排你和引用你。** 你是谁（实体定义）、你讲什么（主题地图）、答案在哪（可检索内容）、凭什么信你（站外主题网络）都会降低搜索系统的判断成本；内容量不能替代这四件事，见 [references/entity-and-topic-map.md](references/entity-and-topic-map.md)。

## 先选打法

- **新词站**：需求刚爆、SERP 还空，比的是速度，红利期可能只有一周。适合新手练手、快速拿正反馈。
- **养老站**：长期平稳的老需求，比的是内容深度、内链、外链和时间，常见 2–4 个月才有稳定点击。适合积累长期资产。
- 两者可以衔接：有新词做新词，没新词做老词；新词站站稳后转为养老站维护。不确定时先问清用户的目标（练手、快速变现还是长期资产）和可投入的时间。

## 实时性要求（每次都遵守）

- 结论必须基于**当次实时查询**：Google Trends（写明时间范围、地区、查询日期）、Google 搜索结果页、域名可注册情况。不要凭记忆或文章里的旧数字下结论。
- 不编造搜索量、KD、点击、收入。拿不到数据就说拿不到，并说明影响。估算值要标"估算"，并写出对标词和计算方式。
- 已知的数据滞后：Google Ads 关键词规划的月搜索量通常滞后 1–2 个月；Trends 最后一个点往往是没过完的一天/一周，不要读成"热度在掉"；Trends 最近两天的全球数据可能还没稳定。
- 社群经验里的数字有时效。用作对标前，先用 Keyword Planner 里一个当月已知搜索量的词重新校准，见 [references/find-and-judge.md](references/find-and-judge.md)。
- 有浏览器工具时实际打开页面核对；本机若装了哥飞 SEO Agent 插件（seo.web.cafe），可用来取 Trends、GSC、Ahrefs 数据，但最终结论仍要写明数据来源和日期。
- 涉及 Google 政策、算法更新、AdSense 规则时，以官方页面当前内容为准（Search Status Dashboard、Search Central 垃圾内容政策、AdSense 帮助中心）。社群早年有效的做法（站群抓取、买老域名、每页 3 个广告位）可能已经违规或过时，见 [references/sources.md](references/sources.md)。
- **自动化的强度要和站点权重匹配。** 域名和内容都还弱的时候，不要一上来就上极致自动化，否则站点容易在一次算法更新里突然消失。先用人工把需求和内容做对，再逐步放大效率。

## 按任务读取

| 任务 | 读取 |
| --- | --- |
| 找新词、用词根挖词、判断一个词值不值得做、估算搜索量、给一批词排序 | [references/find-and-judge.md](references/find-and-judge.md)，批量打分用 `scripts/score_keywords.py` |
| 新词站：已选好词，规划首页/内页、上站节奏、埋点、登录支付、定价、留存 | [references/launch-sop.md](references/launch-sop.md) |
| 养老站：老词选词、AI Overviews 时代的选词过滤、站点结构、程序化 SEO 边界、长期维护、广告/联盟变现、站点矩阵 | [references/evergreen-site.md](references/evergreen-site.md) |
| 让 ChatGPT / Perplexity / Gemini 等 AI 搜索引用或推荐网站 | [references/geo.md](references/geo.md) |
| 内容写了不少但没人引用、品牌被不同来源描述成不同东西、已有站要规划主题结构与入口页 | [references/entity-and-topic-map.md](references/entity-and-topic-map.md) |
| 外链、老词长期优化、流量或排名下滑诊断、已上线站的 SEO 改造 | [references/growth-and-diagnosis.md](references/growth-and-diagnosis.md) |
| 从增长案例提炼做法、用 GSC 数据排优先级、外链发现与结果核验 | [references/evidence-led-growth.md](references/evidence-led-growth.md)；批量投递用配套仓库 [backlink-submission-kit](https://github.com/oiov/backlink-submission-kit) |
| 需要核对某条经验的出处、日期和适用条件 | [references/sources.md](references/sources.md) |

## 输出习惯

- 判词结论用"马上做 / 观察 / 放弃"，并标明按新词站还是养老站来做；每个结论附一句理由和对应证据（Trends 截图描述、SERP 前几名是什么、域名情况）。
- 新词站建议按天给出（D0、D1–D2……）；养老站建议按周和月给出里程碑与复查日期。每一步写清楚"做什么、不做什么、看哪个数决定下一步"。
- 诊断问题先区分"需求退潮"还是"排名下降"，再给动作。
- 明确提醒运气成分：新词站能不能出单有很大偶然性，可靠的做法是多上站、把每一步做对、做复盘。
