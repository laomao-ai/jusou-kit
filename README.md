<img src="assets/logo.svg" alt="聚搜GO（Jusou） logo" width="96" align="left">

# 聚搜GO（Jusou）· 聚合搜索 API / MCP Server

**一个 Key，调 8 个搜索引擎。** 查最新信息、核实事实、多引擎对比，一套接口搞定。给 AI Agent 配联网搜索时不用再逐家注册、逐家对接：
[Exa](https://jusouai.cn/docs/exa)、Tavily、Serper、SerpApi、Brave、博查、百度、AnySearch 共用一套接口、一套计费。

> Looking for a **Tavily / Exa / Serper alternative** with one API key for 8 search engines?
> Jusou is an aggregated search API with a remote **MCP server** — plug it into Claude Code,
> Cursor, Dify, Coze or any MCP / Skill client and your agent can search the web in 3 minutes —
> real-time web search, latest information and fact-checking through one unified search API.

本仓是聚搜GO 的**开源接入壳**：MCP 配置、Skill 包、SDK 示例与平台插件都在这里；
搜索服务本身运行在 [jusouai.cn](https://jusouai.cn)，注册后在控制台拿一个 Key 即可用（按积分计费、失败不扣分）。

## 3 分钟接入（任选一种形态）

### ① MCP（推荐，远程服务、零安装）

Claude Code 一行：

```bash
claude mcp add --transport http jusou https://jusouai.cn/mcp --header "Authorization: Bearer <你的Key>"
```

通用客户端（mcpServers JSON，下例为 Claude Code / VS Code 风格；字段名因客户端而异，如 Windsurf 用 `serverUrl`，不兼容时改用 mcp/ 里的 stdio 桥）：

```json
{
  "mcpServers": {
    "jusou": {
      "type": "http",
      "url": "https://jusouai.cn/mcp",
      "headers": { "Authorization": "Bearer <你的Key>" }
    }
  }
}
```

只支持 stdio 的客户端用仓内桥接：见 [mcp/](mcp/)（一个零依赖 Python 小脚本，把 stdio 转发到远程 MCP）。

接入后有三个工具：`web_search`（指定 engine 或多引擎同时搜）、`list_engines`、`get_balance`。

### ② Skill（给支持 Skill 的 Agent）

把 [skills/jusou-search/](skills/jusou-search/) 目录放进你的 skills 目录，设好环境变量 `JUSOU_API_KEY`，
Agent 会自己读 SKILL.md 并调用随附脚本联网搜索。

### ③ HTTP API（一套统一接口）

```bash
curl -X POST https://jusouai.cn/v1/search \
  -H "Authorization: Bearer <你的Key>" -H "Content-Type: application/json" \
  -d '{"query": "杭州天气", "engine": "baidu"}'
```

不带 `engine` 用默认引擎；带 `engines: ["exa", "baidu"]` 多家同时搜、各自扣分、结果可合并去重。
也提供与各家官方同形的原生接口（`/v1/exa/search`、`/v1/baidu/web-search` …），已有代码换个地址与 Key 即可迁移（字段差异以各引擎文档为准）。
Python / Node 示例见 [sdk/](sdk/)，完整文档在 <https://jusouai.cn/docs>。

## 引擎与计费（统一接口 basic 档）

| 引擎 | 适合 | 积分/次 |
|---|---|---|
| Exa | 英文/语义找资料、找同类网页 | 1 |
| Tavily | 给 AI 的结构化搜索结果 | 1 |
| Serper | Google 全系（网页/新闻/学术/购物…） | 1 |
| SerpApi | 与官方同形的 Google 结果 | 4 |
| Brave | 独立索引、隐私友好 | 2 |
| 博查 | 中文网页、国内覆盖 | 1 |
| 百度 | 中文网页 + AI 生成答案 | 1（AI 搜索 3） |
| AnySearch | 默认引擎、多源聚合 | 1 |

- 深度档（advanced / deep）积分更高：Exa deep 4、Tavily advanced 2、百度 AI 搜索 3，全表见 <https://jusouai.cn/pricing>。
- **失败不扣分**：参数错、上游异常、无可用额度都原样退回；每次调用返回本次扣分与剩余积分。
- 套餐：月卡 ¥19 起（1000 积分），季卡/年卡更划算；卡密兑换、同一 Key 自动叠加。

## 目录

- [mcp/](mcp/) — MCP 配置片段与 stdio 桥接
- [skills/jusou-search/](skills/jusou-search/) — 聚搜 Skill 包（SKILL.md + 调用脚本）
- [sdk/](sdk/) — Python / Node 调用示例
- plugins/ — Dify / Coze / FastGPT 插件（陆续入仓）

## 常见问题

**Key 在哪拿？** [jusouai.cn](https://jusouai.cn) 注册/兑换卡密后，控制台里就是你的 Key（永久可见、可重置）。

**和直接用各家官方 API 比，差别在哪？** 一套接口调 8 家、一个账本扣分、哪家临时不可用换参数即切换；
价格按积分统一结算，小用量不用在每家各充一笔最低充值。

**服务开源吗？** 本仓的接入壳（配置、Skill、示例、插件）MIT 开源；搜索中继服务本身闭源运行。

## License

MIT，见 [LICENSE](LICENSE)。
