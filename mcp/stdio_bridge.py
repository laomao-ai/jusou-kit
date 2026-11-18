#!/usr/bin/env python3
"""聚搜GO MCP 的 stdio 桥（零依赖）：给只支持 stdio 的 MCP 客户端用。

原理：把 stdin 的逐行 JSON-RPC 原样转发到远程 MCP（https://jusouai.cn/mcp，
Streamable HTTP、无状态），响应按 JSON / SSE 规范拆成逐行 JSON-RPC 写回 stdout。业务逻辑全在远程，本脚本只是管道。

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
    """返回要写回 stdout 的行列表（通知类无返回时为空列表）。"""
    def synth(msg):
        try:
            req_id = json.loads(line).get("id")
        except Exception:
            req_id = None
        if req_id is None:
            return []
        return [json.dumps({"jsonrpc": "2.0", "id": req_id,
                            "error": {"code": -32000, "message": msg}})]
    req = urllib.request.Request(
        URL, method="POST", data=line.encode(),
        headers={"Authorization": "Bearer " + KEY,
                 "Content-Type": "application/json",
                 "Accept": "application/json, text/event-stream"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            ctype = r.headers.get_content_type() or ""
            text = r.read().decode()
    except urllib.error.HTTPError as e:
        try:
            body = e.read().decode()
            json.loads(body)
            return [json.dumps(json.loads(body), ensure_ascii=False, separators=(",", ":"))]
        except Exception:
            return synth(f"upstream HTTP {e.code}")
    except Exception as e:
        return synth(f"bridge: {e}")
    if not text.strip():
        return []
    if ctype == "text/event-stream" or text.lstrip().startswith("data:") or "\ndata:" in text:
        msgs = []
        for event in text.replace("\r\n", "\n").split("\n\n"):
            data = "\n".join(l[5:].lstrip() for l in event.split("\n") if l.startswith("data:"))
            if data.strip():
                msgs.append(data)
        return msgs
    try:
        return [json.dumps(json.loads(text), ensure_ascii=False, separators=(",", ":"))]
    except Exception:
        return [text.strip()]


def main() -> int:
    if not KEY:
        print("缺少环境变量 JUSOU_API_KEY", file=sys.stderr)
        return 2
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        for out in forward(line):
            sys.stdout.write(out + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
