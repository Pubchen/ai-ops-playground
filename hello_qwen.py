# -*- coding: utf-8 -*-
"""
调用阿里云百炼（Model Studio）千问大模型的最小示例
方式：DashScope Python SDK (v2)
文档：https://help.aliyun.com/zh/model-studio/first-api-call-to-qwen

运行前请先设置环境变量 DASHSCOPE_API_KEY（你 sk- 开头的密钥）。
"""
import os
import warnings

# 未配置 workspace 时 SDK 会打印一条“回退到共享网关”的提示，属正常现象，这里屏蔽掉以免干扰
warnings.filterwarnings("ignore", message=r"no workspace configured")

import dashscope
from dashscope.v2 import DashScopeError

# ========== 你可能需要修改的配置 ==========
MODEL = "qwen3.8-max"  # 想换模型改这里，例如 "qwen-plus"、"qwen-turbo"
REGION = "cn-beijing"    # 地域，中国站一般就是 cn-beijing

# 业务空间ID（WorkspaceId）：已填入你的空间 ws-70symd67rsy9kdw6。
# 如需临时改用别的空间，可设置环境变量 DASHSCOPE_WORKSPACE 覆盖。
WORKSPACE = os.getenv("DASHSCOPE_WORKSPACE", "ws-70symd67rsy9kdw6")
# ===========================================

# 从环境变量读取 API Key（不要把 sk-xxx 明文写进代码，避免泄露）
api_key = os.getenv("DASHSCOPE_API_KEY")
if not api_key:
    raise SystemExit(
        "未检测到环境变量 DASHSCOPE_API_KEY。\n"
        "请先执行（把 sk-xxx 换成你真实的 Key）：\n"
        "  echo \"export DASHSCOPE_API_KEY='sk-xxx'\" >> ~/.zshrc && source ~/.zshrc"
    )

# 组装 Client 参数（workspace 只有在设置了的时候才传）
client_kwargs = {"api_key": api_key, "region": REGION}
if WORKSPACE:
    client_kwargs["workspace"] = WORKSPACE

client = dashscope.Client(**client_kwargs)

# 对话内容：system 设定助手身份，user 是你的提问
messages = [
    {"role": "system", "content": [{"text": "You are a helpful assistant."}]},
    {"role": "user", "content": [{"text": "你有什么功能？"}]},
]

try:
    response = client.multimodal.chat.create(
        model=MODEL,
        messages=messages,
    )
    # 打印模型回答
    text = getattr(response, "output_text", None)
    print(text if text is not None else response)
except DashScopeError as e:
    print(f"HTTP返回码：{e.status_code}")
    print(f"错误码：{e.code}")
    print(f"错误信息：{e.message}")
    print("请参考文档：https://help.aliyun.com/model-studio/developer-reference/error-code")
