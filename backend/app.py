# -*- coding: utf-8 -*-
"""58同城开放平台应用 - 后端服务骨架 (Flask)

粗胚模板：包含 58 API 调用封装（签名 + 城市检索），可替换真实密钥后运行。
"""
import hashlib
import time
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# ===== 配置（请替换为真实凭证，勿提交到公开仓库）=====
APP_KEY = ""        # 58 开放平台 appKey
APP_SECRET = ""     # 58 开放平台 appSecret
API_BASE = "https://openapi.58.com"  # 官方网关


def sign(params: dict, secret: str) -> str:
    """58 官方签名规则：除 sig 外所有参数按 key 字典升序，拼接 key=value，末尾加 app_secret，UTF-8 编码后 MD5，转小写。"""
    keys = sorted(params.keys())
    raw = "".join(f"{k}={params[k]}" for k in keys) + secret
    return hashlib.md5(raw.encode("utf-8")).hexdigest()


def build_params(api_name: str, biz: dict, access_token: str = "", openid: str = "") -> dict:
    """组装公共参数 + 业务参数 + 签名。"""
    params = {
        "app_key": APP_KEY,
        "timestamp": str(int(time.time() * 1000)),  # 13 位毫秒
    }
    if access_token:
        params["access_token"] = access_token
    if openid:
        params["openid"] = openid
    params.update(biz)
    params["sig"] = sign(params, APP_SECRET)
    return params


@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "app": "58-local-life"})


@app.route("/api/userinfo")
def userinfo():
    """示例：调用 /v2/user/getuserinfo 获取用户基本信息（需先 OAuth 授权拿 access_token + openid）。"""
    at = request.args.get("access_token", "")
    oid = request.args.get("openid", "")
    params = build_params("/v2/user/getuserinfo", {}, at, oid)
    resp = requests.post(f"{API_BASE}/v2/user/getuserinfo", params=params, timeout=10)
    return jsonify(resp.json())


@app.route("/api/search")
def search():
    """示例接口：按城市 + 分类检索 58 信息（待对应检索类接口开通后接入）。
    参数: city_id, cate_id, q, page, page_size
    """
    biz = {
        "city_id": request.args.get("city_id", ""),
        "cate_id": request.args.get("cate_id", ""),
        "q": request.args.get("q", ""),
        "page_num": request.args.get("page", "1"),
        "page_size": request.args.get("page_size", "20"),
    }
    # TODO: 对应检索接口开通后替换 apiPath
    params = build_params("/v2/info/search", biz)
    # resp = requests.get(f"{API_BASE}/v2/info/search", params=params, timeout=10)
    # return jsonify(resp.json())
    return jsonify({"code": 0, "message": "骨架就绪，接入官方接口后返回真实数据", "params": params})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
