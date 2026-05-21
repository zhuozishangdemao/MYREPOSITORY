import os
from typing import Optional,Dict,List
from openai import OpenAI
#这里还没有引入HelloAgentLLM这部分，所以后面的myllm并不完整
from .llm import HelloAgentsLLM
class MyLLM(HelloAgentsLLM):
     def __init__(
               self,
               model:Optional[str] = None,
               api_key:Optional[str] = None,
               base_url:Optional[str] = None,
               provider:Optional[str] = 'auto',
               **kwargs
     ):
          if provider == "modelscope":
               print("正在使用自定义的ModelScopeProvider")
               self.provider = 'modelscope'

               self.api_key = api_key or os.getenv("MODELSCOPE_API_KEY")
               self.base_url = base_url or "https://api-inference.modelscope.cn/v1/"

               if not self.api_key:
                    raise ValueError("MODELSCOPE_API_KEY not found,please set api_key")
               self.model = model or os.getenv("LLM_MODEL_ID") 
               self.temperature = kwargs.get('temperature',0.7)
               self.timeout = kwargs.get('timeout',60)
               self.max_tokens = kwargs.get('max_tokens')

               self._client = OpenAI(api_key = self.api_key,base_url=base_url,timeout=self.timeout)
          else:
               super().__init__(model=model,api_key=api_key,base_Url=base_url,provider=provider,**kwargs)