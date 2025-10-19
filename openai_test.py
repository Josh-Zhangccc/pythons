from openai import OpenAI
client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="not-needed",
)
response = client.chat.completions.create(
    model="qwen3:8b",
    messages=[
        {'role':'system','content':'你是一个6岁小朋友'},
        {'role':'user','content':'小朋友你几岁了'}
    ],
    stream=False,
    temperature=0.7,  #越高越随机
    max_tokens=150,#最大输出长度
    top_p=0.95,#核采样
    frequency_penalty=0.0,#避免重复
    presence_penalty=0.0#新话题鼓励x

)

#for chunk in response:
#    if chunk.choices[0].delta.content:  # 有新内容时输出
#       print(chunk.choices[0].delta.content, end="", flush=True)
print(response.choices[0].message.content)
print("📌 使用统计：")
print(f"  输入 token: {response.usage.prompt_tokens}")
print(f"  输出 token: {response.usage.completion_tokens}")