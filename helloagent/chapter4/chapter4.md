### 4.1客户端实现
1. 生成client对象，可以调用已有的函数，代替requests.post:  
self.client = OpenAI(api_key=apikey,base_url=baseUrl,timeout=timeout)
    requests.post(
        url=...,
        headers={"Authorization": f"Bearer {key}"},
        json={...}
    )的过程
2. 调用模型得到输出的结果，stream影响是否为流式输出response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                stream=True,
            )：  
    这里message格式如下  
    messages = [
    {"role": "system", "content": "你是一个乐于助人的助手。"},
    {"role": "user", "content": "你好，请问今天天气如何？"},
    {"role": "assistant", "content": "很抱歉，我无法获取实时天气。"},
    {"role": "user", "content": "那你帮我写一首关于阳光的诗吧。"}
]
    assitant表示模型之前的回答，多轮对话需要把前几轮assistant的回复也放进messages
    system：设定助手的整体行为，风格，规则，通常在来头，让模型更受控制
    user：用户的指令
3. 解析结果  
* stream条件下：
response对象形式  
response为一个generator，每次生成一个ChatCompletionChunk
ChatCompletionChunk(
    id="chatcmpl-xxx",
    choices=[
        ChoiceDelta(
            delta=ChoiceDelta(      # 注意是 delta，不是 message
                content="营销",      # 这一小段增量文本（可能是单个字或多个字）#在pythonprint中呈现流式输出的结果，就可以使用print(flush= True)参数，可以让输出不暂时保存在缓存区域，直接输出
                role="assistant"
            ),
            finish_reason=None,      # 生成没结束前为 None，最后一个 chunk 会是 "stop"
            index=0
        )
    ],
    created=1712345678,
    model="coding-glm-5.1-free"
)  
* 非流式条件：
response = ChatCompletion(
    id="chatcmpl-xxx",#本次请求的唯一标识
    choices=[
        Choice(
            finish_reason="stop",#停止原因，stop：正常结束或者遇到停止词，length: 达到最大长度
            index=0,
            message=ChatCompletionMessage(
                content="营销口号...",    # 完整的回答文
                role="assistant"
                #可能由tool_calls使用的工具
            )#完整的回复消息
        )
    ],#choices数组中包含choice对象
    
    created=1712345678,#生成时间戳
    model="coding-glm-5.1-free",
    usage=CompletionUsage(
        completion_tokens=50,
        prompt_tokens=30,
        total_tokens=80
    )#token用量统计
)
### 4.2REACT架构实现
#### TOOL实现
需要  
1. 核心工具功能：函数
2. 构建通用工具管理器:注册，读取目录，调用
#### React核心逻辑实现
##### 系统提示词设计
规范智能体与llm之间的交互规范：
* 角色规范
* 工具清单
* 格式规范：强制LLM输出由结构性，能从代码解析意图
* 动态上下文：question&&history
##### 核心循环实现
*  每次循环格式化提示词：包含history，question，tools
* 调用llm思考
##### 输出解析器的实现
* _parse_ouput:分理出Thought和Action两个部分
* _parse_action:处理Action字段，得到tool_name 和tool_input
##### 工具调用与执行
* 先检查是否为final，若不是，则对tool_funtion,tool_inputs进行调用，以observation保存调用工具的结果
##### 观察结果的整合
* 将action本身和工具执行后的observation添加回历史记录，作为下一轮循环的上下

### 4.3Plan and solve架构
设计完整蓝图，再执行
通过只输出结果控制输出