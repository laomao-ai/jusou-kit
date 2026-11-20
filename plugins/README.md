# 平台插件

全部是调 https://jusouai.cn 公开接口的薄包装，用户填自己的 Key：

- **coze/** — Coze 插件的 OpenAPI 规格（`openapi.json`），含 `search` / `engines` 两个工具，
  已在 Coze 平台调试通过。Coze 的授权方式暂不支持「用户自填 Key」，公开发布会变成
  平台方 Key 裸奔，故未上架；这份规格可直接导入你自己的 Coze 空间自用。
- **dify/** — Dify 工具插件（规划中）：manifest + provider + 工具定义，用户在插件里填自己的 Key。
- **fastgpt/** — FastGPT 工具集（规划中）：走 OpenAPI 导入，可先用 coze/ 的同一份规格顶替。
