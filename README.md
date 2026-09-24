# 58同城开放平台接入资料

<p align="center">
  <img src="https://raw.githubusercontent.com/giguber/58tongcheng-open-platform/main/logo.png" width="120" alt="logo">
</p>

<p align="center">
  <b>58本地生活</b> —— 基于 58同城开放平台的本地生活信息服务应用模板
</p>

<p align="center">
  <a href="https://github.com/giguber/58tongcheng-open-platform"><img src="https://img.shields.io/badge/GitHub-仓库-blue" alt="GitHub"></a>
  <a href="https://giguber.github.io/58tongcheng-open-platform/"><img src="https://img.shields.io/badge/官网-落地页-brightgreen" alt="官网"></a>
</p>

---

## 项目简介

本仓库是个人接入 58同城开放平台（[open.58.com](https://open.58.com)）的资料库与应用模板，非官方仓库。

- 已注册 58 开放平台官方应用，获取 appKey/appSecret
- 已整理官方文档要点（签名规则、OAuth2.0 授权、SDK 用法）
- 提供前后端模板骨架（Flask + Web）
- 规划能力：按城市（衡阳优先）聚合招聘 / 房产 / 二手车 / 本地服务信息

## 目录结构

```
58tongcheng-open-platform/
├── README.md            # 本文件
├── docs/
│   └── PRODUCT.md       # 产品说明（审核材料）
├── backend/
│   ├── app.py           # Flask 后端骨架（含 58 官方签名算法）
│   └── requirements.txt # 依赖
├── frontend/
│   └── index.html       # 前端模板页
├── database/
│   └── schema.sql       # 数据库设计
├── logo.png             # 应用 Logo
├── LICENSE              # MIT License
└── .gitignore
```

## 快速开始

```bash
# 后端
cd backend
pip install -r requirements.txt
# 在 app.py 中填入你的 appKey/appSecret 后运行
python app.py

# 前端
# 直接打开 frontend/index.html 即可预览模板页
```

## 58 开放平台接入要点（官方文档）

### 1. 签名规则

将除 `sig` 外的所有参数按 key 字典升序排列，按 `key=value` 拼接后末尾加上 `app_secret`，UTF-8 编码后做 MD5，结果转小写。

```python
keys = sorted(params.keys())
raw = "".join(f"{k}={params[k]}" for k in keys) + secret
sig = hashlib.md5(raw.encode("utf-8")).hexdigest()
```

### 2. 授权模式（OAuth2.0）

- 授权登录页：`GET https://openapi.58.com/v2/auth/show?app_key={app_key}&redirect_uri={redirect_uri}`
- 换取令牌：`POST https://openapi.58.com/v2/auth/access_token`（参数 code / timestamp / app_key / sig）
- 刷新令牌：`POST https://openapi.58.com/v2/auth/refresh_token`

### 3. 已见接口

| 接口 | 说明 |
|------|------|
| `/v2/user/getuserinfo` | 获取用户基本信息（需 access_token + openid） |
| `/v4/callcenter/callrecord` | 呼叫中心通话记录（需厂商授权） |

## 应用配置

| 字段 | 值 |
|------|----|
| 应用官网链接 | `https://giguber.github.io/` |
| 回调地址（Callback URL） | `https://giguber.github.io/58tongcheng-open-platform/` |
| Logo | `https://raw.githubusercontent.com/giguber/58tongcheng-open-platform/main/logo.png` |

## 回调地址格式要求（官方规范）

- ✅ 完整公网 HTTP/HTTPS URL（如 `https://giguber.github.io/58tongcheng-open-platform/`）
- ❌ 不接受本地地址（如 `http://localhost:8080/callback`）
- ❌ 不接受带端口的形式

## 说明

- 本仓库为个人学习/接入用途，与 58 同城官方无关联
- 接口权限以开发者中心实际开通为准，部分接口需企业资质或授权码
- 密钥请通过环境变量或本地配置管理，勿提交到公开仓库

---

© 2026 giguber · MIT License
