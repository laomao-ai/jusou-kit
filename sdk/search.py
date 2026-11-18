#!/usr/bin/env python3
"""聚搜GO 统一搜索示例（Python，零依赖）。
运行：JUSOU_API_KEY=jsk_xxx python3 search.py"""
import json
import os
import urllib.request

KEY = os.environ["JUSOU_API_KEY"]

body = {"query": "杭州天气", "engine": "baidu", "num_results": 3}
req = urllib.request.Request(
    "https://jusouai.cn/v1/search", method="POST",
    data=json.dumps(body).encode(),
    headers={"Authorization": "Bearer " + KEY, "Content-Type": "application/json"})
with urllib.request.urlopen(req, timeout=60) as r:
    out = json.loads(r.read())

for i, x in enumerate(out.get("results") or [], 1):
    print(f"{i}. {x.get('title')}\n   {x.get('url')}")
print((out.get("billing") or {}).get("summary", ""))
