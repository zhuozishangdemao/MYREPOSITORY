import torch
from transformers import AutoModelForCausalLM,AutoTokenizer
model_name = 'Qwen/Qwen3-0.6B'

print(f'正在加载分词器和模型')

tokenizer = AutoTokenizer.from_pretrained(model_name,trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype ='auto',
    trust_remote_code = True
)
model = model.to("cuda" if torch.cuda.is_available() else "cpu")
print('模型加载完成')

prompt = 'Datawhale agent learns'

message = [{'role':'user',"content":prompt}]
text = f"<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"
model_inputs = tokenizer([text],return_tensors='pt').to(model.device)
sampling_configs = [
    # 1. 贪婪解码 (默认，确定性)
    {"do_sample": False, "name": "Greedy (do_sample=False)"},
    
    # 2. 纯粹随机采样 (基准)
    {"do_sample": True, "temperature": 1.0, "top_k": 0, "top_p": 1.0, "name": "Pure Sampling (T=1.0)"},
    
    # 3. 低温度，更确定性
    {"do_sample": True, "temperature": 0.2, "top_p": 1.0, "name": "Low Temperature (T=0.2)"},
    
    # 4. 高温度，更具创造性
    {"do_sample": True, "temperature": 1.5, "top_p": 1.0, "name": "High Temperature (T=1.5)"},
    
    # 5. 启用Top-k采样
    {"do_sample": True, "temperature": 1.0, "top_k": 20, "top_p": 1.0, "name": "Top-k (k=20)"},
    
    # 6. 启用Top-p采样 (核采样)
    {"do_sample": True, "temperature": 1.0, "top_p": 0.9, "name": "Top-p (p=0.9)"},
    
    # 7. 组合使用低温度与Top-p
    {"do_sample": True, "temperature": 0.6, "top_p": 0.9, "name": "Low T + Top-p (T=0.6, p=0.9)"},
]
fixed_params = {
    "max_new_tokens": 50,
    "repetition_penalty": 1.1, # 轻微惩罚重复，使输出更流畅
    "pad_token_id": tokenizer.eos_token_id
}
print(f"\n{'='*50}")
print(f"提示语 (Prompt): '{prompt}'")
print(f"{'='*50}")

for config in sampling_configs:
    config_name = config.pop('name')
    gen_params = {**fixed_params,**config}
    with torch.no_grad():
        ouput_ids = model.generate(**model_inputs,**gen_params)

    output_text = tokenizer.decoder(
        ouput_ids[0][len(model_inputs.inputs.id[0])],
        skip_special_tokens = True
    )
    print(f"\n>>> 参数配置: {config_name}")
    print(f"    参数详情: {gen_params}")
    print(f"    模型输出: {output_text}")

print(f"\n{'='*50}")
