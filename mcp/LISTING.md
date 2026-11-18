# MCP 目录上架材料与状态（Foxe 维护）

远程服务：`https://jusouai.cn/mcp`（Streamable HTTP，Bearer Key）。提交文案统一用仓 README 首段。

| 目录 | 提交物 | 方式 | 状态 |
|---|---|---|---|
| Official MCP Registry | `server.json`（本目录） | `mcp-publisher` CLI + GitHub 登录 | ✅ 2026-11-18 已发布 io.github.laomao-ai/jusou@1.0.0，Registry API 可查 |
| Glama | 托管端点表单 | 网站提交、人工审核 | ✅ 2026-11-18 已上线（连接器形态）：https://glama.ai/mcp/connectors/cn.jusouai/go-jusou |
| Smithery | — | — | ❌ 通道关闭（2026-11-18 实查）：已并入 Arcade、自助发布入口取消、代理服务 10-31 停运，现仅精选目录 215 个，不可自投 |
| mcp.so | 远程端点 | 仅付费提交 | ⏸ 唯一通道 $39 一次性，老猫 2026-11-18 定：先不上 |
| 魔搭 ModelScope MCP 广场 | 自定义创建 → StreamableHttp + 请求头参数 | 老猫手机号账号 busycat、免费 | ✅ 2026-11-18 已上线：https://modelscope.cn/mcp/servers/busycat/jusou（公开/搜索工具/仅本地可用；小瑕疵：详情页 README 里 Bearer 后尖括号占位被渲染吞掉，待顺手修） |
| awesome-remote-mcp-servers（GitHub 清单） | PR 收录 | 免费、维护者审核 | 📝 2026-11-18 PR 已提交待合并：https://github.com/punkpeye/awesome-remote-mcp-servers/pull/5129 |

Skill 侧：ClawHub jusou-search@1.0.0 已提交（扫描 CLEAN、待平台转公开）；skills.sh 已可直装（npx skills add laomao-ai/jusou-kit），搜索索引待生效；SkillsMP 待自动收录。find 类发现机制按「索引收录 + 描述任务词匹配 + 安装量排序」运作，描述已中英双语埋词。
