# Changelog

本仓（聚搜GO 开源接入壳）的变更记录，格式参考 [Keep a Changelog](https://keepachangelog.com/)。
版本号与 Skill 包版本对齐；搜索服务本身的更新日志见官网。

## [Unreleased]

### Added

- README 首屏升级：居中品牌区、徽章行、特性表、上架渠道与设计原则小节
- 英文版 README（README.en.md），与中文版互链
- CONTRIBUTING.md、GitHub Issue 模板、.gitignore

### Removed

- README 中的套餐价格信息（对外文档只保留引擎积分表，口径与生产文档对齐）

### Fixed

- README 深度档计费口径与生产文档对齐（补 Exa advanced 2）

## [1.0.3] - 2026-11-19

### Added

- SKILL.md 选引擎表新增 4 个垂直场景配方：公众号（博查/百度 + `site:mp.weixin.qq.com`）、知乎、排错（Stack Overflow）、官方文档
- SKILL.md 新增「事实核查模式」：多引擎并行 + 合并对照的使用说明（服务端既有能力）
- 两个生产实测示例：单引擎查天气（1 分）、双引擎核查珠峰高程（2 分，多源互证）

### Changed

- SkillHub 命名空间迁移为 `indiv-aiyuancat`，安装命令更新为 `npx skills add @indiv-aiyuancat/jusou-search`
- 品牌 logo 入仓（assets/logo.svg），README 顶部嵌图

## [1.0.2] - 2026-11-19

### Added

- SKILL.md 中英双语：description 与 Setup 段覆盖中英文任务词
- 接入说明补「注册赠 100 分（7 天有效）」口径

## [1.0.0] - 2026-11-18

### Added

- 首发：MCP 配置片段与零依赖 stdio 桥（mcp/，含 MCP Registry 用的 server.json）
- Agent Skill 包（skills/jusou-search/：SKILL.md + 调用脚本）
- Python / Node 零依赖 SDK 示例（sdk/）
- Coze 插件 OpenAPI 规格（plugins/coze/openapi.json）
- README（接入三形态、引擎计费表、常见问题）与 MIT 许可证
