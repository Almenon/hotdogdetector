from datetime import datetime

from auto_round import AutoRoundConfig ##must import for auto-round format
from transformers import AutoModelForCausalLM, AutoProcessor

class AI:
    def __init__(self, object_to_detect: str):
        """
        Note first-time initialization will have side-effect of downloading model
        """
        startdownload = datetime.now()

        MODEL_ID = "OPEA/Phi-3.5-vision-instruct-qvision-int4-sym-inc" 

        self.model = AutoModelForCausalLM.from_pretrained(
            MODEL_ID, 
            device_map="auto", 
            trust_remote_code=True, 
            torch_dtype="auto",
            # _attn_implementation='flash_attention_2' # FlashAttention only supports Ampere GPUs or newer :(
        )

        self.processor = AutoProcessor.from_pretrained(MODEL_ID, 
            trust_remote_code=True, 
            num_crops=16
        )

        content = f"Is this a {object_to_detect}? Just answer yes or no. "
        messages = [
            {"role": "user", 
            "content": "<|image_1|>\n"+content},
        ]

        self.prompt = self.processor.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        print(f'AI initialized in {datetime.now()-startdownload} seconds')


    def detect_object(self, image) -> str:
        inputs = self.processor(self.prompt, image, return_tensors="pt").to(self.model.device) 

        generation_args = {
            "max_new_tokens": 1000,
            "temperature": 0.0,
            "do_sample": False,
        } 

        generate_ids = self.model.generate(**inputs,
            eos_token_id=self.processor.tokenizer.eos_token_id,
            **generation_args
        )

        # remove input tokens 
        generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]
        response = self.processor.batch_decode(generate_ids,
            skip_special_tokens=True,
            clean_up_tokenization_spaces=False
        )[0]

        return response
