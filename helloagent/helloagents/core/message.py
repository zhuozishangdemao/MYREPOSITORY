"""消息系统"""
from typing import Optional,Dict,Any,Literal
from datetime import datetime
from pydantic import BaseModel
MessageRole = Literal["user","assistant","system","tool"]#定义消息的角色类型/是否可添加消息类型作为扩展

class Message(BaseModel):#basemodel限制了消息的格式严格，否则会抛出错误
    """消息类"""
    content:str
    role:MessageRole
    timestamp:datetime =None
    metadata:Optional[Dict[str,Any]] = None
    def __init__(self,content:str,role:MessageRole,**kwargs):
        super().__init__(
            content = content,
            role = role,
            timestamp = kwargs.get("timestamp",datetime.now()),
            metadata = kwargs.get('metadata',{})
        )
    def to_dict(self)->Dict[str,Any]:
        """转换为字典格式（openai api格式）"""
        return {
            "role":self.role,
            "content":self.content
        }
    def __str__(self)->str:
        return f'[{self.role}]{self.content}'