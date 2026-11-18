#!/usr/bin/env python3
"""聚搜GO MCP 的 stdio 桥（零依赖）：给只支持 stdio 的 MCP 客户端用。

原理：把 stdin 的逐行 JSON-RPC 原样转发到远程 MCP（https://jusouai.cn/mcp，
Streamable HTTP、无状态），响应逐行写回 stdout。业务逻辑全在远程，本脚本只是管道。

客户端配置示例（Claude Desktop / Cursor 等 stdio 型）：
  {
    "mcpServers": {
      "jusou": {
        "command": "python3",
        "args": ["/path/to/stdio_bridge.py"],
        "env": { "JUSOU_API_KEY": "jsk_你的Key" }
      }
    }
  }

可选环境变量：JUSOU_MCP_URL 覆盖远程地址（默认 https://jusouai.cn/mcp）。
"""
import json
import os
import sys
import urllib.error
import urllib.request

URL = os.environ.get("JUSOU_MCP_URL", "https://jusouai.cn/mcp")
KEY = os.environ.get("JUSOU_API_KEY", "").strip()


def forward(line: str):
    """返回要写回 stdout 的一行（通知类无返回时返回 None）。"""
    req = urllib.request.Request(
        URL, method="POST", data=line.encode(),
        headers={"Authorization": "Bearer " + KEY,
                 "Content-Type": "application/json",
                 "Accept": "application/json, text/event-stream"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            text = r.read().decode()
    except urllib.error.HTTPError as e:
        try:
            req_id = json.loads(line).get("id")
        except Exception:
            req_id = None
        if req_id is None:
            return None
        return json.dumps({"jsonrpc": "2.0", "id": req_id,
                           "error": {"code": -32000, "message": f"upstream HTTP {e.code}"}})
    except Exception as e:
        try:
            req_id = json.loads(line).get("id")
        except Exception:
            req_id = None
        if req_id is None:
            return None
        return json.dumps({"jsonrpc": "2.0", "id": req_id,
                           "error": {"code": -32000, "message": f"bridge: {e}"}})
    if not text.strip():
        return None
    if "data:" in text[:64]:                       # SSE 包装时取最后一条 data
        parts = [l[5:].strip() for l in text.splitlines() if l.startswith("data:")]
        return parts[-1] if parts else None
    return text.strip()


def main() -> int:
    if not KEY:
        print("缺少环境变量 JUSOU_API_KEY", file=sys.stderr)
        return 2
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        out = forward(line)
        if out:
            sys.stdout.write(out + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
