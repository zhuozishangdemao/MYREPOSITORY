类SearchState：传递运行中的信息
{
    messages使用annotated方法，使得后续的message以添加的方式进行调用
    这里messaged的内容都是langgraph的特定类
    HumanMessage，SystemMessage，AiMessage，按照输出顺序被保存在Message中
}  
初始化llm模型：llm.invoke([SystemMessage(content=)])用于生成understand和finalresult  
初始化tavily客户端  
undersyand_query_node函数：
1. state作为输入输出
2. llm.invoke调用初始化的llm，以SystenMessage的形式发送
3. 返回state：userquery，searchquery,step更新，message以aimessage类添加 

tavily_search_node函数：
1. 处理搜索结果，是否有comprehensive result：answer，若无考虑results部分（实际更多应用要看api接口文档）
2. 更新step，添加AIMessage

generate_answer_node函数：
1. 对step中search状态成功与否分类
2. 返回AIMessage结果

create_seaerch_assistant函数：
1. 创造工作流图对象：workflow=StateGraph(SearchState)
2. 添加节点add_node
3. 设置线性流程START除法END结束
4. 编译图，设置checkpoint