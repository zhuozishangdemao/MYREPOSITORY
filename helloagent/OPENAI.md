## Openai
### client
client的作用：创建客户端，配置服务商地址和密钥
```py
# 1. 创建 client，配置服务商地址和密钥
client = OpenAI(
    api_key="你的API密钥",
    base_url="服务商提供的API端点"   # 例如 https://api.openai.com/v1（默认）
)
```
再使用client和带上的信息：如模型名称，信息，自由度
```py
# 2. 使用 client 调用具体功能（如聊天、补全等）
response = client.chat.completions.create(
    model="模型名称",               # 不同厂商模型名可能不同
    messages=[{"role": "user", "content": "你好"}],
    messages=[{"role": "system","content" :"自定义的提示词"},{"role": "user","conten" : "prompt"}]#说明字典是openai规定的api形式，并且可以存储多个字典
    temperature=0.7
    stream = True #规定返回内容是否为流式：流式返回一个迭代器，每次对应一个对象，非流式返回str完整内容
)
```
最后可以对返回结果response进行处理