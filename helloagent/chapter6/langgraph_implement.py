##写完之后记录一份md，描述代码各部分操作的思路和注意点

from typing import TypedDict,Annotated
from langgraph.graph.message import add_messages

class SearchState(TypedDict):
    messages:Annotated[list,add_messages]
    user_query:str
    search_query:str#fined by llm from users' inputs
    search_results:str#consequence that Tavily researched
    final_answer:str
    step:str#signal current steps
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from tavily import TavilyClient

load_dotenv()

print(os.getenv("LLM_MODEL_ID"))

llm = ChatOpenAI(
    model = os.getenv("LLM_MODEL_ID"),
    api_key = os.getenv("LLM_API_KEY"),
    base_url = os.getenv("LLM_BASE_URL"),
    temperature=0.7
)   
tavily_client =TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def undersatnd_query_node(state:SearchState)->dict:
    """步骤1：理解用户查询并生成搜索关键词"""
    user_message = state["messages"][-1].content
    
    understand_prompt = f"""分析用户的查询："{user_message}"
请完成两个任务：
1. 简洁总结用户想要了解什么
2. 生成最适合搜索引擎的关键词（中英文均可，要精准）

格式：
理解：[用户需求总结]
搜索词：[最佳搜索关键词]"""
    response=llm.invoke([SystemMessage(content=understand_prompt)])
    response_text = response.content
    search_query = user_message
    if "搜索词：" in response_text:
        search_query = response_text.split("搜索词：")[1].strip()
    return {
        "user_query":response_text,
        "search_query":search_query,
        "step":"understand",
        "messages":[AIMessage(content=f'我将为您搜索：{search_query}')]
    }

def tavily_search_node(state:SearchState)->dict:
    """步骤二：使用Tavilu API进行真实搜索"""
    search_query = state["search_query"]
    try:
        print(f"searching now:{search_query}")
        response=tavily_client.search(
            query=search_query,search_depth="basic",max_results = 5,include_answer=True
        )
        search_results = ""
        if response.get("answer"):
            search_results = f'综合答案：\n{response['answer']}\n\n'
        if response.get("results"):
            search_results+="相关信息：\n"
            for i,result in enumerate(response["results"][:3],1):
                title = result.get("title","")
                content=result.get("content","")
                url = result.get("url","")
                search_results+=f'{i}.{title}\n{content}\n来源:{url}\n\n'
        if not search_results:
            search_results = "抱歉，没找到相关信息"
        
        return {
            "search_results":search_results,
            "step":"searched",
            "messages":[AIMessage(content=f'搜索完成找到了相关信息，正为您整理答案')]
        }
    except Exception as e:
        erro_msg= f'search error{str(e)}'
        print(f'{erro_msg}')
        return {
            "search_results":f'搜索失败：{erro_msg}',
            "step":"seaerch_fialed",
            "messages":[AIMessage(content = '搜索时出现问题，我将基于已有知识为您回答')]

        }
def generate_answer_node(state:SearchState)->dict:
    """步骤3:基于搜索结果生成最终答案"""
    if state['step'] == 'search_fialed':
        fallback_prompt = f'搜索api暂时不可用，请基于您的知识回答用户问题：\n用户问题：{state["user_query"]}'
        response = llm.invoke([SystemMessage(content=fallback_prompt)])
    else:
        answer_prompt = f"""基于以下搜索结果为用户提供完整、准确的答案：
用户问题：{state['user_query']}
搜索结果：\n{state['search_results']}
请综合搜索结果，提供准确、有用的回答..."""
        response = llm.invoke([SystemMessage(content=answer_prompt)])
    return {
        "final_answer":response.content,
        "step":"completed",
        "messages":[AIMessage(content=response.content)]
    }
from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.memory import InMemorySaver

def create_search_assistant():
    workflow = StateGraph(SearchState)

    workflow.add_node("understand",undersatnd_query_node)
    workflow.add_node("search",tavily_search_node)
    workflow.add_node("answer",generate_answer_node)

    workflow.add_edge(START,"understand")
    workflow.add_edge(START, "understand")
    workflow.add_edge("understand", "search")
    workflow.add_edge("search", "answer")
    workflow.add_edge("answer", END)

    memory = InMemorySaver()
    app=workflow.compile(checkpointer=memory)
    return app
import asyncio 
async def main():

    if not os.getenv("TAVILY_API_KEY"):
        print("未配置tavilyapikey")
        return
    
    app=create_search_assistant()