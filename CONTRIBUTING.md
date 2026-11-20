# 参与贡献

欢迎提 Issue 与 PR。本仓是聚搜GO 的**开源接入壳**——MCP 配置、Skill 包、SDK 示例与平台插件；
搜索服务本身闭源运行，服务端行为问题请开 Issue 描述现象，维护者会在服务端排查。

## 提 Issue

先选模板（接入问题 / 功能建议），尽量写全：

- **接入问题**：注明客户端与版本（Claude Code / Cursor / Dify …）、接入形态（MCP / Skill / HTTP API）、
  报错原文——**贴之前先删掉你的 Key**。
- **搜索结果问题**：注明引擎、查询词、大致时间，方便对账。
- **文档问题**：指出文件与段落，给出你认为正确的表述与依据。

## 提 PR

- 改动尽量小而完整：一个 PR 只做一件事，标题说清动了什么。
- **计费与引擎口径以生产文档为准**：动 SKILL.md / README 的计费表、引擎清单前，
  先核对 <https://jusouai.cn/docs> 与 `curl https://jusouai.cn/v1/engines` 的实读结果，
  不一致时以生产为准、并在 PR 里注明核对时间。
- **对外文档口径**：不写套餐价格与购买链接（只保留引擎积分表）；不写内部实现细节。
- 示例代码保持**零依赖、可直接运行**：提交前自己跑通一遍，命令与输出对得上。
- Markdown 内的相对链接逐个点通；新增目录时同步更新 README 的「目录结构」表。

## 版本与发布

- 版本号与 Skill 包版本对齐，变更记入 [CHANGELOG.md](CHANGELOG.md) 的 Unreleased 段。
- Skill 包发版走各渠道货架（SkillHub / ClawHub / skills.sh），状态见 [mcp/LISTING.md](mcp/LISTING.md)。

## 行为准则

友善、就事论事。涉及他人 Key、账号与订单的信息一律不要贴进 Issue / PR。
