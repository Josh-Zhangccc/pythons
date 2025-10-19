import requests

# 基础配置
OLLAMA_HOST = "http://localhost:11434"
MODEL_NAME = "llama3.1:8b"

# 生成文本
def generate_text(prompt):
    response = requests.post(
        f"{OLLAMA_HOST}/api/generate",
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()

# 使用示例
result = generate_text("请用中文介绍一下你自己")
print(result['response'])