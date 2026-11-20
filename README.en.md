<p align="center">
  <img src="assets/logo.svg" alt="Jusou logo" width="120">
</p>

<h1 align="center">Jusou · 聚搜GO</h1>

<p align="center"><strong>One API key. Eight search engines.</strong><br>
An aggregated search service for AI agents: latest information, fact-checking and
multi-engine comparison through one unified API.</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-1167d8.svg" alt="License: MIT"></a>
  <a href="mcp/"><img src="https://img.shields.io/badge/MCP-Server-22c3a6.svg" alt="MCP Server"></a>
  <a href="skills/jusou-search/SKILL.md"><img src="https://img.shields.io/badge/Skill-1.0.3-1167d8.svg" alt="Skill 1.0.3"></a>
  <a href="#engines--pricing"><img src="https://img.shields.io/badge/Engines-8-22c3a6.svg" alt="8 engines"></a>
</p>

<p align="center">
  <a href="README.md">中文</a> · <a href="https://jusouai.cn/docs">Docs</a> · <a href="https://jusouai.cn">Website</a> · <a href="CHANGELOG.md">Changelog</a> · <a href="CONTRIBUTING.md">Contributing</a>
</p>

Looking for a **Tavily / Exa / Serper alternative** with one API key for 8 search engines?
Jusou is an aggregated search API with a remote **MCP server** — plug it into Claude Code,
Cursor, Dify, Coze or any MCP / Skill client and your agent can search the web in 3 minutes:
real-time web search, latest information and fact-checking through one unified search API.

This repository is Jusou's **open-source integration kit**: MCP configuration, the Agent Skill
package, SDK examples and platform plugins. The search service itself runs at
[jusouai.cn](https://jusouai.cn) — sign up, grab one key from the console, and you are ready
(per-point billing, failed calls are never charged).

## Features

| Feature | What it means |
|---|---|
| 8 engines, one interface | Exa, Tavily, Serper, SerpApi, Brave, Bocha, Baidu, AnySearch — switch by parameter |
| Parallel multi-engine search | Pass `engines` to search several at once; grouped results with optional merge — fact-check across sources instead of trusting one |
| Three depth levels | basic / advanced / deep (per engine support) |
| Native-compatible endpoints | `/v1/exa/search`, `/v1/baidu/web-search`, … mirror each provider's own API shape — migrate by changing the base URL and key |
| One key for every form | HTTP API, MCP and Skill share the same key and the same points ledger |
| Failed calls are free | Parameter errors and upstream failures are refunded automatically; every call returns its charge and your remaining balance |
| 100 free points on sign-up | New accounts get 100 points (valid 7 days) — wire it up first, decide later |

## Quickstart (pick one form)

Sanity-check the service first (no key needed):

```bash
curl https://jusouai.cn/v1/engines   # lists the 8 engines and their per-call points
```

### 1. MCP (recommended — remote, zero install)

Claude Code, one line:

```bash
claude mcp add --transport http jusou https://jusouai.cn/mcp --header "Authorization: Bearer <your-key>"
```

Generic clients (mcpServers JSON, Claude Code / VS Code style; field names vary by client —
Windsurf uses `serverUrl`, and stdio-only clients can use the bridge in `mcp/`):

```json
{
  "mcpServers": {
    "jusou": {
      "type": "http",
      "url": "https://jusouai.cn/mcp",
      "headers": { "Authorization": "Bearer <your-key>" }
    }
  }
}
```

Three tools are exposed: `web_search` (single engine or several in parallel), `list_engines`,
`get_balance`. See [mcp/](mcp/) for details and the zero-dependency stdio bridge.

### 2. Skill (for Skill-capable agents)

One-line install (either channel):

```bash
npx skills add laomao-ai/jusou-kit              # via skills.sh, from this repo
npx skills add @indiv-aiyuancat/jusou-search    # via Tencent SkillHub
```

Or copy [skills/jusou-search/](skills/jusou-search/) into your skills directory manually.
With `JUSOU_API_KEY` set, the agent reads SKILL.md and calls the bundled script itself.

### 3. HTTP API (one unified endpoint)

```bash
curl -X POST https://jusouai.cn/v1/search \
  -H "Authorization: Bearer <your-key>" -H "Content-Type: application/json" \
  -d '{"query": "Hangzhou weather", "engine": "baidu"}'
```

Omit `engine` for the default engine; pass `engines: ["exa", "baidu"]` to search several at
once (charged per engine, results can be merged and deduplicated). Zero-dependency Python /
Node examples live in [sdk/](sdk/); full documentation at <https://jusouai.cn/docs>.

## Engines & pricing

Unified API, basic depth:

| Engine | Best for | Points / call |
|---|---|---|
| Exa | English / semantic research, similar pages | 1 |
| Tavily | Structured results built for AI | 1 |
| Serper | Google family (web / news / scholar / shopping…) | 1 |
| SerpApi | Google results in the official shape | 4 |
| Brave | Independent index, privacy-friendly | 2 |
| Bocha | Chinese web, domestic coverage | 1 |
| Baidu | Chinese web + AI-generated answers | 1 (AI search 3) |
| AnySearch | Default engine, multi-source aggregation | 1 |

- Deeper levels are priced per engine: Exa advanced 2 / deep 4, Tavily advanced 2, Baidu AI
  search 3; for anything else the [production docs](https://jusouai.cn/docs) are authoritative.
- **Failed calls are never charged**: parameter errors, upstream failures and exhausted
  quotas are refunded as-is. A successful call with an empty result set is charged normally —
  the engine did run the search.
- Every call returns its charge and remaining balance (`get_balance` in MCP).

## Repository layout

| Directory | Contents |
|---|---|
| [mcp/](mcp/) | MCP integration: remote-server config, stdio bridge, `server.json` for the MCP Registry, listing status |
| [skills/jusou-search/](skills/jusou-search/) | The Agent Skill package (SKILL.md + script); installable via skills.sh / SkillHub / ClawHub |
| [sdk/](sdk/) | Zero-dependency Python / Node call examples |
| [plugins/](plugins/) | Platform plugins: the Coze OpenAPI spec is in; Dify / FastGPT to follow |
| [assets/](assets/) | Brand assets (`logo.svg` is the master) |

## Listings

Listed on the Official MCP Registry, Glama, ModelScope, Tencent SkillHub, ClawHub,
Skills Directory, mcpservers.org and more — full list and status in
[mcp/LISTING.md](mcp/LISTING.md).

## Design principles

- **Key safety**: your key only ever travels in request headers and environment variables;
  the examples never persist or echo a full key. Never commit a key to a public repository.
- **Transparent billing**: per-engine points in the open, automatic refunds on failure, a
  charge-and-balance receipt on every call.
- **Open kit, hosted service**: configuration, Skill, examples and plugins in this repo are
  MIT-licensed; the search service itself is closed-source and hosted.

## FAQ

**Where do I get a key?** Sign up at [jusouai.cn](https://jusouai.cn) — your key lives in the
console (always visible, resettable). New accounts get 100 free points.

**Why not call each provider directly?** One interface for 8 engines, one points ledger, and
switching engines is a parameter change when one is having a bad day — no per-provider
sign-ups and balances to babysit.

**Is the service open source?** The integration kit in this repo is MIT; the search service
itself is closed-source and hosted (see Design principles above).

## License

MIT — see [LICENSE](LICENSE).
