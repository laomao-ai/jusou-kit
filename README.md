<p align="center">
  <img src="assets/logo.svg" alt="聚搜GO（Jusou） logo" width="120">
</p>

<h1 align="center">聚搜GO · Jusou</h1>

<p align="center"><strong>一个 Key，调 8 个搜索引擎。</strong><br>
给 AI Agent 的聚合搜索服务：查最新信息、核实事实、多引擎对比，一套接口搞定。</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-1167d8.svg" alt="License: MIT"></a>
  <a href="mcp/"><img src="https://img.shields.io/badge/MCP-Server-22c3a6.svg" alt="MCP Server"></a>
  <a href="skills/jusou-search/SKILL.md"><img src="https://img.shields.io/badge/Skill-1.0.3-1167d8.svg" alt="Skill 1.0.3"></a>
  <a href="#引擎与计费"><img src="https://img.shields.io/badge/Engines-8-22c3a6.svg" alt="8 engines"></a>
  <a href="https://glama.ai/mcp/connectors/cn.jusouai/go-jusou"><img src="https://glama.ai/mcp/connectors/cn.jusouai/go-jusou/badges/score.svg" alt="Jusou MCP connector on Glama"></a>
</p>

<p align="center">
  <a href="README.en.md">English</a> · <a href="https://jusouai.cn/docs">开发文档</a> · <a href="https://jusouai.cn">官网</a> · <a href="CHANGELOG.md">更新日志</a> · <a href="CONTRIBUTING.md">参与贡献</a>
</p>

> Looking for a **Tavily / Exa / Serper alternative** with one API key for 8 search engines?
> Jusou is an aggregated search API with a remote **MCP server** — plug it into Claude Code,
> Cursor, Dify, Coze or any MCP / Skill client and your agent can search the web in 3 minutes:
> real-time web search, latest information and fact-checking through one unified search API.
> Full English version: [README.en.md](README.en.md).

本仓是聚搜GO 的**开源接入壳**：MCP 配置、Skill 包、SDK 示例与平台插件都在这里；
搜索服务本身运行在 [jusouai.cn](https://jusouai.cn)，注册后在控制台拿一个 Key 即可用（按积分计费、失败不扣分）。

## 特性

| 特性 | 说明 |
|---|---|
| 8 家引擎，一套接口 | Exa、Tavily、Serper、SerpApi、Brave、博查、百度、AnySearch，改参数即切换 |
| 多引擎并行 | `engines` 一次搜多家，结果分组返回，可选合并对照——核实事实不用只听一家 |
| 三种深度 | basic / advanced / deep（按各引擎支持情况），浅查深挖自己定 |
| 原生接口兼容 | `/v1/exa/search`、`/v1/baidu/web-search` 等与各家官方同形，已有代码换地址与 Key 即可迁移 |
| 一个 Key 全形态通用 | HTTP API、MCP、Skill 共用同一个 Key 与同一本积分账 |
| 失败不扣分 | 参数错误、上游异常自动退回；每次调用都返回本次扣分与剩余积分 |
| 注册赠 100 分 | 新用户注册即得（7 天有效），先跑通接入再决定用不用 |

## 快速开始（任选一种形态）

先验证服务可达（无需 Key）：

```bash
curl https://jusouai.cn/v1/engines   # 返回 8 家引擎清单与各自计费
```

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

一行安装（任选其一）：

```bash
npx skills add laomao-ai/jusou-kit              # 经 skills.sh，从本仓安装
npx skills add @indiv-aiyuancat/jusou-search    # 经腾讯 SkillHub
```

或手动把 [skills/jusou-search/](skills/jusou-search/) 目录放进你的 skills 目录。
设好环境变量 `JUSOU_API_KEY` 后，Agent 会自己读 SKILL.md 并调用随附脚本联网搜索。

### ③ HTTP API（一套统一接口）

```bash
curl -X POST https://jusouai.cn/v1/search \
  -H "Authorization: Bearer <你的Key>" -H "Content-Type: application/json" \
  -d '{"query": "杭州天气", "engine": "baidu"}'
```

不带 `engine` 用默认引擎；带 `engines: ["exa", "baidu"]` 多家同时搜、各自扣分、结果可合并去重。
Python / Node 零依赖示例见 [sdk/](sdk/)，完整文档在 <https://jusouai.cn/docs>。

## 引擎与计费

统一接口 basic 档：

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

- 深度档（advanced / deep）按引擎计：Exa advanced 2 / deep 4、Tavily advanced 2、百度 AI 搜索 3；其余以 [生产文档](https://jusouai.cn/docs) 为准。
- **失败不扣分**：参数错、上游异常、无可用额度都原样退回；引擎正常返回但结果为空的，算成功调用、照常计分。
- 每次调用返回本次扣分与剩余积分，账目随时可查（MCP 里就是 `get_balance`）。

## 目录结构

| 目录 | 内容 |
|---|---|
| [mcp/](mcp/) | MCP 接入：远程服务配置、stdio 桥、Registry 用的 server.json、上架状态 |
| [skills/jusou-search/](skills/jusou-search/) | Agent Skill 包（SKILL.md + 调用脚本），可经 skills.sh / SkillHub / ClawHub 安装 |
| [sdk/](sdk/) | Python / Node 零依赖调用示例 |
| [plugins/](plugins/) | 平台插件：Coze 的 OpenAPI 规格已入仓，Dify / FastGPT 陆续补 |
| [assets/](assets/) | 品牌资产（logo.svg 为母版） |

## 上架渠道

MCP Registry、Glama、魔搭 ModelScope、腾讯 SkillHub、ClawHub、Skills Directory、mcpservers.org 等渠道均已上架，完整清单与状态见 [mcp/LISTING.md](mcp/LISTING.md)。

## 设计原则

- **Key 安全**：Key 只出现在请求头与环境变量里；示例代码不落盘、不回显完整 Key；不要把 Key 提交进任何公开仓库。
- **计费透明**：按引擎明码积分，失败自动退回，每次调用回执扣分与余额。
- **接入壳开源、服务闭源**：本仓的配置、Skill、示例与插件 MIT 开源；搜索服务本身闭源运行。

## 常见问题

**Key 在哪拿？** [jusouai.cn](https://jusouai.cn) 注册后，控制台里就是你的 Key（永久可见、可重置）；新用户注册赠 100 分。

**和直接用各家官方 API 比，差别在哪？** 一套接口调 8 家、一个账本扣分、哪家临时不可用换参数即切换；不用逐家注册、逐家维护余额。

**服务开源吗？** 本仓的接入壳（配置、Skill、示例、插件）MIT 开源；搜索服务本身闭源运行，见上方「设计原则」。

## License

MIT，见 [LICENSE](LICENSE)。
