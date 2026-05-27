"""工具注册表 -Helloagen原生工作系统"""
from typing import Optional,Any,Callable
from .base import Tool
class ToolRegistry:
    """
    HelloAgent工具注册表

    提供工具的注册、管理和执行功能。
    支持两种注册方式：
    1.Tool对象注册
    2.函数直接注册
    """

    def __init__(self):
        self._tools:dict[str,Tool] = {}
        self._functions:dict[str,dict[str,Any]]={}
    
    def register_tool(sefl,tool:Tool,auto_expand:bool =True):
        """
        注册Tool对象

        Args：
        tool：Tool实例
        auto_expand:是否自动展开可展开的工具
        """
    def register_tool(self,tool:Tool,auto_expand:bool =True):
        """
        注册Tool对象
        
        Args:
            tool:Tool实例
            auto_expand:是否自动展开可展开的工具(default = True)"""
        #检查是否可以展开
        if auto_expand and hasattr(tool,'expandable') and tool.expandable:
            expanded_tools = tool.get_expaned_tools()
            if expanded_tools:
                #注册所有展开后的子工具
                for sub_tool in expanded_tools:
                    if sub_tool.name in self._tools:
                        print(f'警告：工具{sub_tool.name}已经存在，将被覆盖')
                    self._tools[sub_tool.name] = sub_tool
                print(f'工具{tool.name}已经展开为{len(expanded_tools)}个独立工具')
                return
        if tool.name in self._tools:
             print(f"⚠️ 警告：工具 '{tool.name}' 已存在，将被覆盖。")

        self._tools[tool.name] = tool
        print(f"✅ 工具 '{tool.name}' 已注册。")
                    
    def register_function(self,name:str,description:str,func:Callable[[str],str]):
        """
        直接注册函数作为工具
        
        Args:
            name:工具名称
            deescription:工具描述
            func:工具函数，接受字符串参数，返回字符串结果
        """
        #通过getattr(self.tool_registry,'_funuctions')可以提取由函数定义的工具
        if name in self._functions:
            print(f'警告，工具{name}已存在，将被覆盖')
        self._functions[name]={
            "description":description,
            "func":func
        }
        print(f'工具{name}已注册')
    def unregister(self,name:str):
        """注销工具"""
        if name in self._tools:
            del self._tools[name]
            print(f"🗑️ 工具 '{name}' 已注销。")
        elif name in self._functions:
            del self._functions[name]
            print(f"🗑️ 工具 '{name}' 已注销。")
        else:
            print(f"⚠️ 工具 '{name}' 不存在。")
    def get_tool(self,name:str)->Optional[Tool]:
        """获取tool对象"""
        return self._tools.get(name)
    def get_function(self,name:str)->Optional[Callable]:
        """获取函数工具"""
        func_info = self._function.get(name)
        return func_info['func'] if func_info else None
    def execute_tool(self,name:str,input_text:str)->str:
        """
        执行工具
        
        ArgsL
            name:工具名称
            input_text输入参数
            
        Returns:
            工具执行结果
        """
        if name in self._tools:
            tool = self._tools.get(name)
            try:
                return tool.run({"input":input_text})
            except Exception as e:
                return f'错误：执行工具{name}发生异常:{str(e)}'
            
        elif name in self._functions:
            func = self._functions[name]['func']
            try:
                return func(input_text)
            except Exception as e:
                return f'错误：执行工具{name}发生异常:{str(e)}'
        else:
            return f'错误： 未找到名为{name}的工具'
    def get_tools_description(self)->str:
        """
        获取所有可用工具的格式化描述字符串
        
        Returns:
            工具描述字符串，用于构建提示词
        """
        descriptions = []

        #Tool对象描述
        for tool in self._tools.values():
            descriptions.append(f"Tool-{tool.name}:{tool.description}")
        
        #函数工具描述
        for name,info in self._functions.items():
            descriptions.append(f'Func-{name}:{info['description']}')
        
        return '\n'.join(descriptions) if descriptions else "暂无可用工具"
    
    def list_tools(self)->list[str]:
        """列出所有工具名称"""
        return list(self._tools.keys())+list(self._functions.keys())
    
    def get_all_tools(self)->list[Tool]:
        """获取所有Tool对象"""
        return list(self._tools.vlaues())
    def clean(self):
        """清空所有工具"""
        confirm = input("你确定要清空所有工具吗(Y/N)").strip().upper()
        if confirm == "Y":
            self._tools.clear()
            self._functions.clear()
            print("工具已经清空")
        else :
            print("已经撤销清空操作")
global_registry = ToolRegistry()