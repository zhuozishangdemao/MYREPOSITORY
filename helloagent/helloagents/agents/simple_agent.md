def run(self,input_text:str,max_tool_iterations:int =3,**kargs) ->str:
#构建agent时已经传入base_prompt,llm,tool_registry,enable_tool,config,name基于base_prompt and tool_registry 生成了enhanced_prompt规范了Agent调用工具时的格式
run的同时需要构建Message列表保存
message = []
messages.append{"role":"system","content":enhanced_system_prompt})
在agent基类中包含_history:包含了Agent实例从创建到每次调用的所有history,更准确的是装入一些用户反馈，可以让当前agent返回增加参考
for msg in self._history:
    messages.appned({"role":"msg.role,"content":msg.content})将历史记录加入当前对话
messages.append({"role":"user","content":input_text])
#对于不可工具调用的场景使用原有逻辑
if not self.enable_tool_calling:
    response - llm.invoke(message,**kargs)#一些关非流式输出的参数
    self.add_message(Message(input_text,"user")
    self.add_message(Message(response,'assistant')
＃message具体格式的意义在于llm调用时读取message要求格式确定
＃在每次调用的过程中都要将run运行的结果记录在llm中
    return reponse
#以下为多次迭代工具调用的情形
current_iteration = 0
final_response = ""
while current_iteration<max_tool_iterations:
    response = self.llm.invoke(messages,**kwargs)
    tool_calls = self._parse_tool_calls(response)
    if tool_calls:
        tool_result = []
        clean_response = reponse
        message.append("role":"assistant","content":clean_response})
#需要进行提取工具调用列表和提取工具参数列表
        for call in tool_calls:
            result = self._execute_tool_call(call['tool_name'],call['parameters'])
            tool_results.append(result)
            clean_response = cleanreposne.replace[call['original',""]#这一步有什么意义
        tool_results_text = "\n\n".join(tool_results)
        messages.append("role":"user","content":f"工具执行结果:\n{tool_results_text}\n\n请基于这些结果给出完整的答案。‘})
        current_iteratioin+=1
        continue
    final_response = response
    break
#最大循环次数处理
 if current_iteration >= max_tool_iterations and not final_response:
            final_response = self.llm.invoke(messages, **kwargs)
self.add_message(Message(input_text,"user")
self.add_message(Message(final_response,"assistant")
return final_response
#把工具看做agent自身的属性，通过调用tool库进行简便工具注册和删除服务
def add_tool(self,tool,autp_expend:bool=True) ->None:
 def stream_run(self, input_text: str, **kwargs) -> Iterator[str]:
        """
        流式运行Agent
        Args:
            input_text: 用户输入
            **kwargs: 其他参数
        Yields:
          Agent响应片段
        """
        # 构建消息列表
        messages = []
        if self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})
        for msg in self._history:
            messages.append({"role": msg.role, "content": msg.content})
        messages.append({"role": "user", "content": input_text})
        # 流式调用LLM
        full_response = ""
        for chunk in self.llm.stream_invoke(messages, **kwargs):
            full_response += chunk
            yield chunk
        # 保存完整对话到历史记录
        self.add_message(Message(input_text, "user"))
        self.add_message(Message(full_response, "assistant"))