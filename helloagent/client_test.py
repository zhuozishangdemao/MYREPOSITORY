from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from autogen_core.models import ModelInfo
from dotenv import load_dotenv
load_dotenv()
print(repr(os.getenv('LLM_MODEL_ID')))
print(repr(os.getenv('LLM_API_KEY')))
print(repr(os.getenv('LLM_BASE_URL')))
def create_openai_model_client():
    """创建并配置OpenAI模型客户端"""
    model_info = ModelInfo(
        vision=False,
        function_calling=True,
        json_output=True,
        family="deepseek"
    )
    return OpenAIChatCompletionClient(
        model=os.getenv("LLM_MODEL_ID"),
        api_key=os.getenv("LLM_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL"),\
        model_info = model_info 
    )
client = create_openai_model_client()