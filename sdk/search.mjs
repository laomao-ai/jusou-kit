// 聚搜GO 统一搜索示例（Node 18+，内置 fetch）。
// 运行：JUSOU_API_KEY=jsk_xxx node search.mjs
const KEY = (process.env.JUSOU_API_KEY || "").trim();
if (!KEY) {
  console.error("缺少环境变量 JUSOU_API_KEY（在 https://jusouai.cn 控制台获取）");
  process.exit(2);
}

const res = await fetch("https://jusouai.cn/v1/search", {
  method: "POST",
  headers: { Authorization: `Bearer ${KEY}`, "Content-Type": "application/json" },
  body: JSON.stringify({ query: "杭州天气", engine: "baidu", num_results: 3 }),
});
if (!res.ok) {
  console.error(`调用失败 HTTP ${res.status}：${(await res.text()).slice(0, 200)}`);
  process.exit(2);
}
const out = await res.json();

(out.results || []).forEach((x, i) => console.log(`${i + 1}. ${x.title}\n   ${x.url}`));
console.error(out.billing?.summary ?? "");
