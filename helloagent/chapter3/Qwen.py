#pip install transformers torch在transformer库中调用
#使用AutoModelForCasualLM,AutoTOkenizer自动加载和模型匹配的权重和分词器配置
import torch
from transformers import AutoModelForCausalLM,AutoTokenizer
model_id='Qwen/Qwen1.5-0.5B-Chat'

device = 'cuda' if torch.cuda.is_available else 'cpu'
print(f'using device:{device}')

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(model_id).to(device)

print('模型和分词加载完毕')
messages = [
    {'role':'system','content':'you are a helpfull assistant.'},
    {'role':'user','content':"你好，请你介绍你自己"}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize = False,
    add_generation_prompt = True
)
#编码输入文本
model_inputs = tokenizer([text],return_tensors="pt").to(device)
print("编码后的输入文本：")
print(model_inputs)
#使用模型生成回答
#max_new_token控制了模型最多的新token数量
generate_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens = 512
)

#截取生成的TOkeniD的部分
#只解码模型新生成的部分
generate_ids = [
    output_ids[len(input_ids):] for input_ids,output_ids in zip(model_inputs.input_ids,generate_ids)
]

#解码生成的TokenId
response =tokenizer.batch_decode(generate_ids,skip_special_tokens=True)[0]

print('\n模型的回答：')
print(response)