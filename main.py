from datetime import datetime

import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer

startdownload = datetime.now()
# load omni model default, the default init_vision/init_audio/init_tts is True
# if load vision-only model, please set init_audio=False and init_tts=False
# if load audio-only model, please set init_vision=False
model = AutoModel.from_pretrained(
    'openbmb/MiniCPM-o-2_6',
    trust_remote_code=True,
    attn_implementation='sdpa', # sdpa or flash_attention_2
    torch_dtype=torch.bfloat16,
    init_vision=True,
    init_audio=False,
    init_tts=False
)
print(f'download done in {datetime.now()-startdownload} seconds')

modelinitialized = datetime.now()
model = model.eval().cuda()
tokenizer = AutoTokenizer.from_pretrained('openbmb/MiniCPM-o-2_6', trust_remote_code=True)
print(f'model initialized in {datetime.now()-modelinitialized} seconds')

msgs = [{
    "role": "user",
    "content": ["What is one plus one?"]
}]

aistart = datetime.now()
answer = model.chat(msgs=msgs, tokenizer=tokenizer)
print(f'ai thinking complete in {datetime.now()-aistart} seconds')
print(answer)