import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
device = "mps" # the device to load the model onto

model_id = "mistralai/Mixtral-8x7B-v0.1"
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, attn_implementation="flash_attention_2")
tokenizer = AutoTokenizer.from_pretrained(model_id)

prompt = "My favourite condiment is"

model_inputs = tokenizer([prompt], return_tensors="pt").to(device)
model.to(device)

generated_ids = model.generate(**model_inputs, max_new_tokens=100, do_sample=True)
tokenizer.batch_decode(generated_ids)[0]
print(tokenizer.batch_decode(generated_ids)[0])
