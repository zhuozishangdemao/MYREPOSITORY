REACT
具有特殊功能的智能体需要一些提示词模板来实现特殊功能
此时的THOUGHT and ACTION就需要特殊提示词来实现
DEFAULT_REACT_PROMPT = """你是一个具备推理和行动能力的AI助手。你可以通过思考分析问题，然后调用合适的工具来获取信息，最终给出准确的答案。
## 可用工具
{tools}
## 工作流程
请严格按照以下格式进行回应，每次只能执行一个步骤：
Thought: 分析问题，确定需要什么信息，制定研究策略。
Action: 选择合适的工具获取信息，格式为：
- `{{tool_name}}[{{tool_input}}]`：调用工具获取信息。
- `Finish[研究结论]`：当你有足够信息得出结论时。
## 重要提醒
1. 每次回应必须包含Thought和Action两部分
2. 工具调用的格式必须严格遵循：工具名[参数]
3. 只有当你确信有足够信息回答问题时，才使用Finish
4. 如果工具返回的信息不够，继续使用其他工具或相同工具的不同参数
## 当前任务
**Question:** {question}
## 执行历史
{history}
现在开始你的推理和行动："""
class ReActAgent(Agent):
def __init__(
self,name:str,llm:HelloAgentsLLM,tool_registry,system_prompt,conifg,max_steps,custom_prompt
＃增加了最大步骤以及custo_prompt
self.max_steps = max_steps
self.current_history:List[str] = []
#为了react架构加入history
self.prompt_template = custom_prompt if custom_prompt else DEFAULT_REACT_PROMPT
＃这里可以加入对custom_prompt的审查或者警告机制
＊＊
 def add_tool(self,tool):Mcp工具特殊，单独检查，可以尝试手动补充到tool_registry.register_tool的逻辑中
＊＊
if hasattr(tool, 'auto_expand') and tool.auto_expand:
            # MCP工具会自动展开为多个工具
            if hasattr(tool, '_available_tools') and tool._available_tools:
                for mcp_tool in tool._available_tools:
                    # 创建包装工具
                    from ..tools.base import Tool
                    wrapped_tool = Tool(
                        name=f"{tool.name}_{mcp_tool['name']}",
                        description=mcp_tool.get('description', ''),
                        func=lambda input_text, t=tool, tn=mcp_tool['name']: t.run({
                            "action": "call_tool",
                            "tool_name": tn,
                            "arguments": {"input": input_text}
                        })
                    )
                    self.tool_registry.register_tool(wrapped_tool)
                print(f"✅ MCP工具 '{tool.name}' 已展开为 {len(tool._available_tools)} 个独立工具")
            else:
                self.tool_registry.register_tool(tool)
        else:
            self.tool_registry.register_tool(tool)
def run(self,input_text:str,**kargs)->str:
#ReAct特点，每次调用重置一次历史数据
self.curretn_history=[]
current_step=0
print(f'{self.name}start solve problem}
while currentz_step<self.max_steps:
＃构建提示词
＃调用LLM
＃根据Action和Tought解析输出
thought,action = self._parse_ouput(response_text)
#检查任务是否完成
if action.startswith("Finish"):
    final_answer = self._parse_action_input(action)
    print(final_answer)
#区分自身的历史和ReAct过程历史
    self.add_message(Message(input_text,"user")
    self.add_message(Message(final_answer,"assistant")
   return final_answer
#要有三个解析函数，LLM输出解析出Action和Thought，提取工具名称和参数，Action输出文本
def _parse_output(self,text:str)->Tuple(Optional[str],Optional[str[):
    action_match = re.search(r'Action:(.*)",text)
    Thought_match = re.search(r'Thought:(.*),text)
     thought = Thought_match.group(1).strip() if Thought_match else None
    action = action_match.group(1).strip() if action_match else None
    return thought,action
def _parse_action(self,action_text:str)->Tuple(Optional[str],Optional[str]]:
    match = re.match(r'(\w+)\[(.*)\]",action_text)
if match:
    return match.group(1),match.group(2)
def _parse_action_input(self,action_text:str)->str:
    match = re.match(f'\w+\[(.*)\]",action_text)
    return match.group(1) if match else""