from datetime import datetime

from auto_round import AutoRoundConfig ##must import for auto-round format
import requests
from PIL import Image
from transformers import AutoModelForCausalLM, AutoProcessor

startdownload = datetime.now()

model_id = "OPEA/Phi-3.5-vision-instruct-qvision-int4-sym-inc" 

model = AutoModelForCausalLM.from_pretrained(
  model_id, 
  device_map="auto", 
  trust_remote_code=True, 
  torch_dtype="auto",
  # _attn_implementation='flash_attention_2' # FlashAttention only supports Ampere GPUs or newer :(
)
processor = AutoProcessor.from_pretrained(model_id, 
  trust_remote_code=True, 
  num_crops=16
)

print(f'download done in {datetime.now()-startdownload} seconds')

image_url = "https://images.pexels.com/photos/4676409/pexels-photo-4676409.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
content = "Is this a hotdog? Just answer yes or no. "
messages = [
    {"role": "user", 
     "content": "<|image_1|>\n"+content},
]

prompt = processor.tokenizer.apply_chat_template(
  messages, 
  tokenize=False, 
  add_generation_prompt=True
)

image_inputs = Image.open(requests.get(image_url, stream=True).raw)
aistart = datetime.now()
inputs = processor(prompt, image_inputs, return_tensors="pt").to(model.device) 

generation_args = { 
    "max_new_tokens": 1000, 
    "temperature": 0.0, 
    "do_sample": False, 
} 

generate_ids = model.generate(**inputs, 
  eos_token_id=processor.tokenizer.eos_token_id, 
  **generation_args
)

# remove input tokens 
generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]
response = processor.batch_decode(generate_ids, 
  skip_special_tokens=True, 
  clean_up_tokenization_spaces=False)[0] 

print(response)
print(f'ai thinking complete in {datetime.now()-aistart} seconds')