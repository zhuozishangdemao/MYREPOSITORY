import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import List,Dict,Any,Optional
from pathlib import Path
import re
load_dotenv()
#自动查找当前根目录下.env文件，把key=value形式读入到os.environ
print(repr(os.getenv('LLM_MODEL_ID')))
print(repr(os.getenv('LLM_API_KEY')))
print(repr(os.getenv('LLM_BASE_URL')))
class HelloAgentsLLM:
    """
    为本书‘helloagent’定制的LLM客户端
    用于调用任何兼容Openai接口的服务，默认使用流式响应
    """
    def __init__(self,model : str =None,apikey :str =None,baseUrl : str =None,timeout:int =None):
        self.model = model or os.getenv('LLM_MODEL_ID')#or返回第一个真值对象，都为假返回第二个
        apikey = apikey or os.getenv('LLM_API_KEY')
        baseUrl = baseUrl or os.getenv("LLM_BASE_URL")
        timeout = timeout or int(os.getenv("LLM_TIMEOUT",60))
        if not all([self.model,apikey,baseUrl]):
            raise ValueError("模型ID，API密钥和服务器地址必须被提供或在.env文件中")
        self.client = OpenAI(api_key=apikey,base_url=baseUrl,timeout=timeout)
    def think(self,messages :List[Dict[str,str]],temperature :float =0 ) ->str :
        '''
        调用大语言模型进行思考，返回响应
        '''
        print(f'正在调用{self.model}模型...')
        try:
            response = self.client.chat.completions.create(
                model = self.model,
                messages=messages,
                temperature=temperature,
                stream=True
            )   
            #处理流式响应
            print('大模型响应成功')
            collectied_content = []
            for chunk in response:
                content = chunk.choices[0].delta.content or ""
                print(content,end = '',flush=True)#flush=True
                collectied_content.append(content)
            print()
            return "".join(collectied_content)
        except Exception as e:
                print(f'调用llmapi时出错{e}')
                return None
# if __name__ == '__main__':
#     try:
#         llmClient = HelloAgentsLLM()

#         exampleMessage = [
#         {'role':'system','content':'you are a helpful assistant that write Python code.'},
#         {'role':'user','content':'写一个快速排序算法'}
#         ]
#         print("----调用llm---")
#         responseText = llmClient.think(exampleMessage)
#         if responseText:
#             print('\n\n---完整模型响应---')
#             print(responseText)
#         new_Message=exampleMessage.copy()
#         new_Message.append({'role':'assistant','content':responseText})
#         new_Message.append({'role':'user','content':'尝试自己构成一个微型编程语言实现上述算法'})
#         new_response_Text = llmClient.think(new_Message)
#         if new_response_Text:
#             print('\n\n\n_____新的模型响应____')
#             print(new_response_Text)
#     except ValueError as e:
#         print(e)
from serpapi import SerpApiClient

def search(query: str) -> str :
    """
    一个基于SerpApi的实战网页搜索引擎工具。
    它会只能的解析搜索解雇哦，优先返回直接答案或知识图谱信息。
    """
    print(f'正在执行[SerpApi]网页搜索：{query}')
    try:
        api_key=os.getenv("SERPAPI_API_KEY")
        if not api_key:
            return  "错误:SEROPAPI_API_KEY未在.env文件配置"
        
        params = {
            'engine':'google',
            'q':query,
            'api_key':api_key,
            'gl':'cn',
            'hl':'zh-cn',
        }

        client = SerpApiClient(params)
        results = client.get_json()

        #智能解析：优先寻找最直接的答案
        if 'answer_box_list' in results:
            return '\n'.join(results['answer_box_list'])
        if 'answer_box'in results and 'answer'in results['answer_box']:
            return results['answer_box']['answer']
        if 'knowledge_graph' in results and 'description'in results['knowledge_graph']:
            return results['knowledge_graph']['description']
        if 'organic_results'in results and results['organic_results']:
            snippets = [
                f'[{i+1}]{res.get('title','')}\n{res.get('snippet','')}'for i ,res in enumerate(results['organic_results'][:3])
            ]
            return '\n\n'.join(snippets)
        return f'未找到关于{query}的信息'
    except Exception as e:
        return f'搜索时发生错误：{e}'
class ToolExecutor:
    """
    一个工具执行器，负责管理和执行工具
    """
    def __init__(self):
        self.tools:Dict[str,Dict[str,Any]] = {}
    def registerTool(self,name:str,description:str,func:callable):#callable声明可调用对象
        """
        向工具箱中注册一个新工具
        """
        if name in self.tools:
            print(f'警告：工具{name}已经存在，将被覆盖')
        self.tools[name]={"description":description,'func':func}
        print(f'工具{name}已经注册')
    def getTool(self, name: str) -> callable:
        """
        根据名称获取一个工具的执行函数。
        """
        return self.tools.get(name, {}).get("func")
    def getAvailableTools(self) ->str:
        """
        获取所有可用工具的格式化描述字符串
        """
        return '\n'.join([f'- {name}:{info['description']}' for name,info in self.tools.items()])
# if __name__=='__main__':
#     toolExecutor=ToolExecutor()
#     search_description = "一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。"
#     toolExecutor.registerTool("Search", search_description, search)
#     print('\n---可用的工具---')
#     print(toolExecutor.getAvailableTools())

#     print("\n---执行Action: Search['英伟达最最新的GPU型号是什么']---")
#     tool_name = 'Search'
#     tool_input = '英伟达最新的GPU型号是什么'
#     tool_function = toolExecutor.getTool(tool_name)
#     if tool_function:
#         observation = tool_function(tool_input)
#         print("-----观察(observation)-----")
#         print(observation)
#     else:
#         print(f'错误：未找到名为{tool_name}的工具')
REACT_PROMPT_TEMPLATE = """
请注意，你是一个有能力调用外部工具的智能助手,现在的时间是2026.4.27。

可用工具属下如下：
{tools}

请严格按照以下格式进行回应：

Thought:你的思考过程，用于分析问题、拆解任务和规划下一步的行动。
Action:你决定采取的行动，必须是以下格式之一:
- '{{toll_name}}[{{tool_input}}]':调用一个可用工具。
- 'Finish[最终答案]':当你认为已经获得最终答案时。
- 当你收集到足够的信息,能够回答用户的最终问题时,你必须在Action:字段后面使用Finish[最终答案]来输出答案

现在，请开始解决以下问题：
Question:{question}
History:{history}
Left_tool_use_time{left_tool_use_time}
"""

class ReActAgent:
    def __init__(self,llm_client:HelloAgentsLLM,tool_executor:ToolExecutor,max_steps:int = 5):
        self.llm_client = llm_client
        self.tool_executor = tool_executor
        self.max_steps = max_steps
        self.history = []
    def run(self,question:str):
        """
        运行ReAct智能体回答一个问题
        """
        self.history = []#每次运行重置历史记录
        current_step=0

        while current_step<self.max_steps:
            current_step+=1
            print(f'---第{current_step}步---')
            tool_desc = self.tool_executor.getAvailableTools()
            history_str = '\n'.join(self.history)
            prompt = REACT_PROMPT_TEMPLATE.format(
                tools=tool_desc,
                question=question,
                history=history_str,
                left_tool_use_time = self.max_steps-current_step
            )
            messages = [{"role":"user","content":prompt}]
            response_text = self.llm_client.think(messages=messages)

            if not response_text:
                print("错误：LLM未能返回有效响应")
                return None

            thought,action = self._parse_output(response_text)

            if thought:
                print(f'思考:{thought}')

            if not action:
                print("警告：未能解析出有效的Action，流程终止")
                break
            if action.startswith("Finish"):
                final_answer = re.match(r'Finish\[(.*)\]',action,re.DOTALL).group(1)
                print(f'最终答案:{final_answer}')
                return final_answer
            
            tool_name,tool_input = self._parse_action(action)
            if not tool_name or not tool_input:
                print("注意：此步没有进行任何action!")
                continue

            print(f'行动:{tool_name}[{tool_input}]')

            tool_function = self.tool_executor.getTool(tool_name)
            if not tool_function:
                observatioin = f'错误：未找到名为{tool_name}的工具。'
            else :
                observatioin = tool_function(tool_input)
            
            print(f'观察:{observatioin}')

            self.history.append(f'Action:{action}')
            self.history.append(f'Observation:{observatioin}')

        print('已经达到最大步数，流程终止')
        return None
    def _parse_output(self,text:str):
        """
        解析llm的输出,提取thought和action
        """
        thought_match =re.search(r'Thought:\s*(.*?)(?=\nAction:|$)',text,re.DOTALL)
        action_match = re.search(r'Action:\s*(.*?)$',text,re.DOTALL)
        thought = thought_match.group(1).strip() if thought_match else None
        action = action_match.group(1).strip() if action_match else None
        return thought,action
    def _parse_action(self,action_text:str):
        """
        解析Action字段，提取工具名称和输入
        """
        match = re.match(r'(\w+)\[(.*)\]',action_text,re.DOTALL)#- '{{toll_name}}[{{tool_input}}]':调用一个可用工具。对应提示词中的这部分
        if match:
            return match.group(1),match.group(2)
        return None,None
    
# if __name__ == '__main__':
#     llm = HelloAgentsLLM()
#     tool_executor = ToolExecutor()
#     search_desc = "一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。"
#     tool_executor.registerTool("Search", search_desc, search)
#     agent = ReActAgent(llm_client=llm, tool_executor=tool_executor,max_steps=6)
#     question = "华为最新的手机是哪一款？它的主要卖点是什么？"
#     agent.run(question)
PLANNER_PROMPT_TEMPLATE = """
你是一个顶级的AI规划专家。你的任务是将用户提出的复杂问题分解成一个由多个简单步骤组成的行动计划。
请确保计划中的每个步骤都是一个独立的、可执行的子任务，并且严格按照逻辑顺序排列。
你的输出必须是一个Python列表，其中每个元素都是一个描述子任务的字符串。

问题: {question}

请严格按照以下格式输出你的计划,```python与```作为前后缀是必要的:
```python
["步骤1", "步骤2", "步骤3", ...]
```
"""
import ast

class Planner:
    def __init__(self,llm_client:HelloAgentsLLM):
        self.llm_client = llm_client
    def plan(self,question:str)->list[str]:
        """
        根据用户问题生成一个行动计划
        """
        prompt = PLANNER_PROMPT_TEMPLATE.format(question=question)
        messages = [{'role':'user','content':prompt}]
        print("---正在生成计划---")
        response_text = self.llm_client.think(messages=messages) or ""
        print(f'计划已经生成：\n{response_text}')

        try:
            plan_str = response_text.split("```python")[1].split("```")[0].strip()
            plan = ast.literal_eval(plan_str)
            return plan if isinstance(plan,list) else []
        except (ValueError,SyntaxError,IndexError) as e:
            print(f'解析计划时出现错误:{e}')
            print(f'原始响应为{response_text}')
        except Exception as e:
            print(f"解析式发生未知错误{e}")
            return []
EXECUTOR_PROMPT_TEMPLATE = """
你是一位顶级的AI执行专家。你的任务是严格按照给定的计划，一步步地解决问题。
你将收到原始问题、完整的计划、以及到目前为止已经完成的步骤和结果。
请你专注于解决“当前步骤”，**并仅输出该步骤的最终答案**，不要输出任何额外的解释或对话。

# 原始问题:
{question}

# 完整计划:
{plan}

# 历史步骤与结果:
{history}

# 当前步骤:
{current_step}

请仅输出针对“当前步骤”的回答:
"""
class Executor:
    def __init__(self,llm_client:HelloAgentsLLM):
        self.llm_client = llm_client
    def execute(self,question:str,plan:list[str])->str:
        """
        根据计划，逐步执行并解决问题
        """
        history = ''
        print("\n---正在执行计划---")
        for i,step in enumerate(plan):
            print(f'\n->正在执行步骤{i+1}/{len(plan)};{step}')

            prompt = EXECUTOR_PROMPT_TEMPLATE.format(
                question= question, 
                plan= plan,
                history=history if history else"无",
                current_step= step
            )
            messages = [{"role":"user","content":prompt}]
            response_text = self.llm_client.think(messages=messages) or ""
            history+=f'步骤{i+1}:{step}\n结果:{response_text}\n\n'
            print(f'步骤{i+1}已完成，结果：{response_text}')

        final_answer = response_text
        return final_answer
class PlanAndSolveAgent:
    def __init__(self,llm_client):
        """
        初始化智能体，同时创建规划器和执行器实例
        """
        self.llm_client = llm_client
        self.planner = Planner(self.llm_client)
        self.executor = Executor(self.llm_client)
    def run(self,question:str):
        """
        运行智能体的完整流程：先规划，后执行
        """
        plan = self.planner.plan(question)

        if not plan:
            print("\n---任务终止---\n无法有效生成行动计划")
            return
        
        final_answer = self.executor.execute(question,plan)

        print(f'\n---任务完成---\n最终答案:{final_answer}')
# if __name__ == '__main__':
#     try:
#         llm_client = HelloAgentsLLM()
#         agent = PlanAndSolveAgent(llm_client)
#         question = "一个水果店周一卖出了15个苹果。周二卖出的苹果数量是周一的两倍。周三卖出的数量比周二少了5个。请问这三天总共卖出了多少个苹果？"
#         agent.run(question)
#     except ValueError as e:
#         print(e)

class Memory :
    """
    一个简单的短期记忆模块，用于储存智能体的行动和反思轨迹
    """

    def __init__(self):
        """
        初始化一个空列表来存储所有记录
        """
        self.records:list[Dict[str,Any]] = []

    def add_record(self,record_type:str,content:str):
        """
        向记忆中添加一条新记录

        参数；
        - record_type(str): 记录的类型('execution'或者'reflection')。
        - content(str):记录具体的内容(例如，生成的代码或反思的反馈)。
        """
        record = {"type":record_type,"content":content}
        self.records.append(record)
        print(f"记忆已经更新，新增一条'{record_type}:{content}'记录。")
    def get_trajectory(self)->str:
        """
        将所有记忆记录格式化为一个连贯的字符串文本，用于构建提示词
        """
        trajectory_parts = []
        for record in self.records:
            if record['type'] == 'execution':
                trajectory_parts.append(f"---上一轮尝试(代码)---\n{record['content']}")
            elif record['type'] == 'reflection':
                trajectory_parts.apppend(f"---评审员反馈---\n{record['content']}")
            
        return "\n\n".join(trajectory_parts)
    def get_last_execution(self)->Optional[str] :
        """
        获取最近的一次执行结果(例如，最新生成的代码)。
        如果不存在，则返回None。
        """
        for record in reversed(self.records):
            if record['type'] == 'execution':
                return record['content']
        return None

INITIAL_PROMPT_TEMPLATE = """
你是一位资深的python程序员。请根据以下要求，编写一个python函数。
你的代码必须包含完整的函数签名，文档字符串，并遵循PEP 8编码规范。

要求：{task}

请直接输出代码，不要包含任何额外的解释。
"""

REFLECT_PROMPT_TEMPLATE = """
你是一位极其严格的代码评审专家和资深算法工程师，对代码的性能有极致的要求。
你的任务时审查以下Python代码，并专注于找出其在<strong>算法效率</strong>上的主要瓶颈。

#原始任务：
{task}

#待审查的代码：
```python
{code}
```

请分析该代码的时间复杂度，并思考是否存在一种<strong>算法上更优</strong>的解决方案来显著提升性能。
如果存在，请清晰地指出当前算法的不足，并提出具体的、可用改进算法建议（例如，使用筛法替代除法）。
如果代码在算法层面已经达到最优，才能回答“无需改进”。

请直接输出你的反馈，不要包含任何额外的解释。
"""

REFINE_PROMPT_TEMPLATE = """
你是一位资深的python程序员，你正在根据一位代码评审专家的反馈来优化你的代码。

#原始任务：
{task}

#你上一轮尝试的代码：
{last_code_attempt}
评审员的反馈：
{feedback}

请根据评审员的反馈，生成一个优化后的新版本代码。
你的代码必须包含完整的函数前面、文档字符串，并遵循PEP 8编码规范。
请直接输出优化后的代码，不要包含任何额外的解释。
"""

class ReflectionAgent:
    def __init__(self,llm_client,max_iterations=3):
        self.llm_client = llm_client
        self.memory = Memory()
        self.max_ierations = max_iterations
    def run(self,task:str):
        print(f"\n----开始处理任务----\n任务{task}")

        print("\n---正在尝试初始化---")
        initial_prompt = INITIAL_PROMPT_TEMPLATE.format(task =task)
        iniital_code = self._get_llm_response(initial_prompt)
        self.memory.add_record('execution',iniital_code)

        for i in range(self.max_ierations):
            print(f'\n---第{i+1}/{self.max_ierations}轮迭代---')
            print("\n->正在进行反思...")
            last_code = self.memory.get_last_execution()
            reflect_prompt = REFLECT_PROMPT_TEMPLATE.format(task=task,code = last_code)
            feedback = self._get_llm_response(reflect_prompt)
            self.memory.add_record('reflection',feedback)

            if "无需改进" in feedback :
                print("\n反思认为代码已经无需改进，任务完成")
                break
            print("\n正在进行优化...")
            refine_prompt = REFINE_PROMPT_TEMPLATE.format(
                task= task,
                last_code_attempt = last_code,
                feedback = feedback   
            )
            refine_code = self._get_llm_response(refine_prompt)
            self.memory.add_record("execution",refine_code)
        
        final_code = self.memory.get_last_execution()
        print(f"\n---任务完成---\n最终生成代码\n```python\n{final_code}\n```")
        return final_code
    def _get_llm_response(self,prompt:str)->str:
        """
        一个辅助方法，用于调用LLM获取完整的流式响应
        """
        message = [{"role":"user","content":prompt}]
        response_text = self.llm_client.think(messages = message) or ""
        return response_text

if __name__ == '__main__':
    # 1. 初始化LLM客户端 (请确保你的 .env 和 llm_client.py 文件配置正确)
    try:
        llm_client = HelloAgentsLLM()
    except Exception as e:
        print(f"初始化LLM客户端时出错: {e}")
        exit()

    # 2. 初始化 Reflection 智能体，设置最多迭代2轮
    agent = ReflectionAgent(llm_client, max_iterations=2)

    # 3. 定义任务并运行智能体
    task = "编写一个Python函数，找出1到n之间所有的素数 (prime numbers)。"
    agent.run(task)
