## Tavily
### 作用介绍
执行实时搜索，返回json文件，不需要开发者自行到网站向https发送request

### 基本调用方式
```py
from tavily import TavilyClient

# 初始化客户端（用你的 API Key）
client = TavilyClient(api_key="your-api-key-here")

# 执行搜索
result = client.search(query="最新人工智能发展")

# 打印结果（返回的是 JSON 格式的字典）
print(result)
```
打印结果
>{
>  "query": "最新人工智能发展",
>  "results": [
>    {
>      "title": "OpenAI 发布 GPT-5 预览版",
>      "url": "https://...",
>      "content": "...",
>      "score": 0.95,
>      "published_date": "2026-03-30"
>    },
>    ...
>  ],
>  "answer": "...", 
>  "response_time": 1.23
>}

### 常用参数
query 搜索关键词
search_depth  basic or advanced
max_results  返回结果数量
time_range  限制时间范围

事实上api_key应当通过环境变量的形式获取