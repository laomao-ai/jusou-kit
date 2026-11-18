# MCP 接入（聚搜GO 远程 MCP Server）

服务地址：`https://jusouai.cn/mcp`（Streamable HTTP、无状态、Bearer Key 鉴权）。
工具：`web_search`（指定 engine / 多引擎同时搜）、`list_engines`、`get_balance`。计费与 HTTP API 一致，失败不扣分。

## Claude Code

```bash
claude mcp add --transport http jusou https://jusouai.cn/mcp --header "Authorization: Bearer <你的Key>"
```

## 通用 mcpServers JSON（Cursor / Windsurf / 通义灵码等）

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

## 只支持 stdio 的客户端

用本目录的 `stdio_bridge.py`（零依赖 Python 3）：

```json
{
  "mcpServers": {
    "jusou": {
      "command": "python3",
      "args": ["/path/to/mcp/stdio_bridge.py"],
      "env": { "JUSOU_API_KEY": "jsk_你的Key" }
    }
  }
}
```

## Key

在 https://jusouai.cn 注册/兑换卡密后，控制台里复制你的 Key（形如 `jsk_...`）。不要把 Key 提交进任何公开仓库。
