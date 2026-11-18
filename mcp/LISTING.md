# MCP 目录上架材料与状态（Foxe 维护）

远程服务：`https://jusouai.cn/mcp`（Streamable HTTP，Bearer Key）。提交文案统一用仓 README 首段。

| 目录 | 提交物 | 方式 | 状态 |
|---|---|---|---|
| Official MCP Registry | `server.json`（本目录） | `mcp-publisher` CLI + GitHub 登录 | ✅ 2026-11-18 已发布 io.github.laomao-ai/jusou@1.0.0，Registry API 可查 |
| Glama | 托管端点表单 | 网站提交、人工审核 | ✅ 2026-11-18 已上线（连接器形态）：https://glama.ai/mcp/connectors/cn.jusouai/go-jusou |
| Smithery | — | — | ❌ 通道关闭（2026-11-18 实查）：已并入 Arcade、自助发布入口取消、代理服务 10-31 停运，现仅精选目录 215 个，不可自投 |
| mcp.so | GitHub 仓 | 网站提交 | 待公开仓 |
| 魔搭 MCP 广场 | 远程服务 | 平台提交（账号门槛待隔壁调研确认） | 待调研 |
| awesome-mcp-servers | 一行条目 PR | GitHub PR | 待公开仓 |

Skill 侧：ClawHub jusou-search@1.0.0 已提交（扫描 CLEAN、待平台转公开）；skills.sh 已可直装（npx skills add laomao-ai/jusou-kit），搜索索引待生效；SkillsMP 待自动收录。find 类发现机制按「索引收录 + 描述任务词匹配 + 安装量排序」运作，描述已中英双语埋词。
