# 58同城开放平台接入资料

<p align="center">
  <img src="https://raw.githubusercontent.com/giguber/58tongcheng-open-platform/main/logo.png" width="120" alt="58开放平台接入">
</p>

本仓库用于整理 58同城开放平台（open.58.com）官方应用注册与 API 接入的相关资料、配置清单和示例代码。

## 当前进度

- [x] 注册 58同城开放平台官方应用（进行中）
- [ ] 获取 App Key / App Secret
- [ ] 对接 API 签名与鉴权
- [ ] 编写接入示例代码

## 应用配置

### Logo 链接

- 仓库内：`logo.png`（512×512，蓝色 58 图标）
- 直链：https://raw.githubusercontent.com/giguber/58tongcheng-open-platform/main/logo.png

### 回调地址（Callback URL）

> 用于 OAuth 授权登录/授权回调，注册应用时按需填写。

- 本地开发：`http://localhost:8080/callback`
- 正式环境：待定（部署后填写）

### ⚠️ 回调地址格式要求

58 开放平台要求回调地址为**完整的公网 HTTP/HTTPS URL**：

- ✅ `https://api.example.com/callback`（公网域名）
- ✅ `http://api.example.com/callback`（公网域名，HTTP 也可）
- ❌ `http://localhost:8080/callback`（本地地址，带端口，通常不被接受）

## 相关链接

- 开放平台官网：https://open.58.com
- API 文档：https://open.58.com/docs

## 目录规划

- `docs/` — 官方文档整理与接入笔记
- `examples/` — 各接口调用示例代码

## 说明

> 本仓库为个人接入 58同城开放平台的资料库，非官方仓库。
