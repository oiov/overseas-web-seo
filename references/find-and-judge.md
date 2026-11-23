# 找词与判词

## 目录

- 新词的定义与判断
- 三条找词路线
- 判断一个词值不值得马上做
- 量化：搜索量估算、KGR、kdroi、KD
- 长尾词来源
- 小词起步：保小图大
- 判词结论模板

## 新词的定义与判断

- 哥飞的定义：**出现时间不超过 12 个月的词**。
- 判断出现时间：Google Trends 地区选全球，时间范围拉长（如 2022-01-01 至今），看曲线从哪一周开始有值；再缩小范围可精确到天。
- 曲线形态：新词是"陡升 → 缓降"的尖峰；老词是平稳线或规律的季节性波动。
- 新词不等于竞争小。社群里很多人会抢同一个新词，所以还要看 SERP 和 KGR。
- 新需求的常见来源：老需求 + AI（`ai image editor` 这类在增长的蓝海词）、新模型/新产品发布、社交媒体爆梗、年份词（`2026 calendar` 每年都是新词）。

## 三条找词路线

### 1. Trends 词根法（新手首选，简单高频）

1. 在 Trends 输入词根（如 `ai`、`ai image`、`ai video`、`game`，或工具类词根），地区全球，时间选过去 7 天或 30 天。
2. 看「相关查询」→ 切到「搜索量上升 / Rising」。`Breakout` 表示增幅超过 5000%。
3. 重点盯从第二页爬上来、排名一天内连续上升的生词。
4. 把第一轮拿到的上升词当新词根再查一次，挖二级长尾。
5. TrendsBar 插件能批量导出相关查询、对比 GPTs 热度、查看相关域名注册情况；没有插件也可以手工做。

工具类词根（哥飞 51 个，可直接维护成自己的词根表，再加上自己关注的领域词根）：

Translator, Generator, Example, Convert, Online, Downloader, Maker, Creator, Editor, Processor, Designer, Compiler, Analyzer, Evaluator, Sender, Receiver, Interpreter, Uploader, Calculator, Sample, Template, Format, Builder, Scheme, Pattern, Checker, Detector, Scraper, Manager, Explorer, Dashboard, Planner, Tracker, Recorder, Optimizer, Scheduler, Converter, Viewer, Extractor, Monitor, Notifier, Verifier, Simulator, Assistant, Constructor, Comparator, Navigator, Syncer, Connector, Cataloger, Responder（按"养网站防老第 1 步"的完整列表）。哥飞 SEO Agent 找新词时另加 AI、AI Image、AI Video、Game 四个词根。

常见组合模式：`[功能] generator`、`[格式A] to [格式B] converter`、`[行业] calculator`、`[大牌工具] alternative`（带他人品牌，注意法律和定位风险）、`[游戏名] unblocked / online / wiki`、`[主题] simulator`。

### 2. 站找词（看别人靠什么词吃流量）

- Similarweb / Semrush / Ahrefs 看竞品的自然搜索关键词和高流量内页；重点看非品牌词和增长异常值。
- 免费托管子域名（`*.github.io`、`*.vercel.app`、`*.pages.dev`）上的高流量页面，常常是还没被独立站承接的需求。
- 看任何网站都养成习惯：流量多少、来源分布、搜索流量来自哪些词。

### 3. 社交媒体先发信号

X、Reddit、科技博主先出现的爆款玩法不一定已经形成搜索共识，必须用 Trends 7 天/30 天曲线验证后再动手。

## 判断一个词值不值得马上做

四个问题全部满足就当天上站：

1. **在飙升**：出现在 Trends「搜索量上升」里，曲线仍在往上走。
2. **体量够**：与对标词（默认 GPTs）对比，热度追平或接近。
3. **SERP 没被专门站占住**：前两页主要是 YouTube 教程、新闻、Reddit/X/Quora 讨论、大站内页，没有专门做这个词的独立站；官方站很新或很弱也算机会。
4. **域名能买**：首选完全匹配关键词的 `.com`；被占就选 `.app`、`.net`、`.org`、`.io` 或贴合用途的后缀。不要用特别小众或特别便宜的后缀，`.ai` 很贵。可用 query.domains 批量查后缀。

另外两个检查：

- **搜词知意**：不懂的词先搜 Google 首页并逐个打开，再问 AI"大家搜 xxx 是为了找什么"，两边对照。业务太复杂、涉及法律红线（版权、成人、仿冒）或你交付不了的，直接放弃。
- **能不能往老词靠**：同一需求里挑法律风险低、欧美搜索占比高、将来能扩到"图片生成/视频生成"这类老词的切入点。

注意一个常见结果：新词站实际点击最多的往往不是主词，而是与域名完全匹配的长尾词（例如域名是 `xxx app`，吃到流量的主力就是 `xxx app`），主词排名反而更低。域名和长尾词的匹配度会影响你最终吃到哪些词。

## 量化

### 用 Trends 推算搜索量

Trends 只给相对热度。找一个已知日均搜索量的对标词放进同一张对比图（必须用 Add comparison，分开查的数值不可比），按比例换算。

- 对标词来源：Google Ads 关键词规划工具（账号有消费才显示精确值，否则只有区间）。注意 Ads 会合并近义词，比如 GPTs 会被并进 GPT。
- 哥飞早期给出的对标：GPTs 约 5K+/天。这是旧数据，使用前用当月一个 Ads 精确值已知的词重新校准对标词。
- 主题（Topic）和搜索词（Search term）不要混着比。
- 估算结果只能当数量级参考，必须标明"估算"。

### KGR（新词、蓝海词的竞争度）

`KGR = intitle（或 allintitle）结果数 / 月搜索量`，小于 0.25 视为值得做。新词在 Ahrefs 里还查不到 KD 时，KGR 是可用的量化指标。哥飞建议用 `intitle:"关键词"` 的结果数。原始 KGR 规则只针对月搜索量 250 以下的词，用在更大的词上只能作参考。

### kdroi（老词的优化回报率）

`kdroi = volume × CPC / KD`。在 Semrush/Ahrefs 用词根拉出一批词（如 volume ≥ 600、KD 0–29、CPC > 0.1、排除 near me），导出后按 kdroi 从高到低排，再逐个分析搜索意图。

### KD 门槛

新站、新手优先 KD < 30，越低越好（< 10 基本几个基础外链就能上首页）。Ahrefs 免费 KD 查询：https://ahrefs.com/keyword-difficulty 。

### 批量打分

把候选词整理成 CSV 后运行（在仓库根目录）：

```bash
python3 scripts/score_keywords.py examples/keywords.sample.csv --benchmark-daily 5000
```

CSV 列：`keyword`（必填）、`volume`（月搜索量）、`kd`、`cpc`、`intitle`、`trends_ratio`（相对对标词的热度倍数），缺的列留空即可。`--benchmark-daily` 填你校准后的对标词日均搜索量。脚本只做计算，不取数。

## 长尾词来源

- Google 下拉框（主词 + 空格 + 字母）
- GSC 热门查询（上线 24 小时后就开始有）
- Similarweb 关键词生成器（以主词为种子）
- 竞品获取自然流量的关键词
- Trends 相关查询的二次挖掘
- 竞品的 FAQ、页面结构、定价页

## 小词起步：保小图大

新手可以先做月搜索量约 10K、KD < 29 的小词：一个词一个域名，举全站之力做透（首页解释清楚用户关心的每个问题，每个问题再做内页）。排名稳定后在标题和首页加入兄弟词，再逐步加入父词。权重关系一般是：主域名 > 子域名 > 子目录 > 内页。

## 判词结论模板

```
关键词：xxx（查询日期：YYYY-MM-DD）
结论：马上做 / 观察 / 放弃
趋势：Trends [时间范围/地区]，从 MM-DD 开始上升，当前 [仍在上升/见顶/回落]，约为 GPTs 的 N 倍（估算日均 ~X）
SERP：前 10 名是 [类型]，专门站 [有/无]，最弱的可超越页面是 [域名]
竞争：KGR = x / KD = x（来源）
域名：[可注册的选项]
切入点与长尾：[3–5 个]
风险：[品牌/法律/交付难度/热度寿命]
```
