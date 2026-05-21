REPLECTIONAGENT
#relection的操作可以理解为三步进行
init，refect，refine的循环进行
DEFAULT_PROMPTS = {
    "initial": """
请根据以下要求完成任务：
任务: {task}
请提供一个完整、准确的回答。
""",
    "reflect": """
请仔细审查以下回答，并找出可能的问题或改进空间：
# 原始任务:
{task}
# 当前回答:
{content}
请分析这个回答的质量，指出不足之处，并提出具体的改进建议。
如果回答已经很好，请回答"无需改进"。
""",
    "refine": """
请根据反馈意见改进你的回答：
# 原始任务:
{task}
# 上一轮回答:
{last_attempt}
# 反馈意见:
{feedback}
请提供一个改进后的回答。
"""
#reflection对于记忆存在需要，构建一个短期记忆的类
＃包含execution和reflection的记录
＃区分message：为长期的历史记录，Memory类：短期的记忆
class Memory:
     def __init__(self):
         self.records:List[Dict[str,Any]]  = []
    def add_memory(self,record_type:str,content:str):
        self.records.append({record_type:content})
     #Memory的对外反馈需要以字符串进行交互，加入到反馈的过程
     def get_tarajectory(self):
     trajectory = ""
     for record in self.records:
        #为了交互中让llm理解意图，处理输出还要为输出加入时间顺序
         if record['type'] == 'execution':
             trajectory+=f'---last turn trial (code)----\n{record['content']}\n\n"
         elif record['type'] === 'reflection'
             trajectory+=f'---reviwerer feedback---\n{record['content']}\n\n'
      return trajectory.strip()
    def get_last_execution(self)->str:
     for record in reversed(self.records):
        if record['type'] == 'execturion':
            return recrord['content']
     return ""
class ReflactionAgent(Agent):
    def run(self,input_text:str,**args)->str:
        #每次记忆重置
        self.memory = Memory()
＃初始化结果
        init_result = self.prompts["inittial"].format(task= input_text)
        self.memory.add_record("execution",initial_result)
        ＃步骤1反思
        last_result = self.memory.get_last_execution()
        relect_prompt = self.promps['reflect'].format(
            task = input_text,
            content=last_result
        )
        feedback = self._get_llm_response(reflect_prompt,**kargs)
        self.memory.add_record('reflection',feedback)
        #步骤2检查是否需要停止
        if '无需改进' in feedback or in feedback.lower():
         break
        #步骤3优化
        refine_prompt = self.prompts['refine'].format(
            task = input_textm
            last_attempt=last_result,
            feedback=feedback
        )
        refined_result = self._get_llm_response(refine_prompt,**kargs)
        self.memory.add_record("execution",refined_result)
    
    fine_result = self.memory.get_last_execution()

    self.add_message(Message(input_text,"user"))
    self.add_message(Message(final_result,"assistant"))

    return final_result
def _get__llm_reponse(self,prompt:str,**kargs)->str:


