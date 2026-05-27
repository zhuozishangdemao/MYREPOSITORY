"""格式管理"""
import os
from typing import Optional,Dict,Any
from pydantic import BaseModel
class Config(BaseModel):
    """HelloAgents配置类"""
    #LLM config
    default_model :str = "gpt-3.5-turbo"
    default_provider:str = "openai"
    temperature:float = 0.7
    max_tokens:Optional[int] =None
    
    #SYSTEM config
    debug:bool=False
    log_levwl:str ='INFO'

    #other config
    max_history_length :int = 100
    
    @classmethod
    def from_env(cls)->"Config":#以类作为变量，返回config实例，这里会对"config"自动解析
        """从环境变量创建配置"""
        return cls(
            debug=os.getenv("DEBUG","false").lower =="true",
            log_level=os.getenv("LOGLEVEL","INFO"),
            temperature=float(os.getenv("TEMPERATURE","0.7")),
            max_tokens = int(os.getenv("MAX_TOKENS")) if os.getenv("MAX_TOKENS")else None,
        )
    def to_dict(self)->Dict[str,Any]:
        """transfer to a dict"""
        return self.model_dump()#config perameters Dict