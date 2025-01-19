# Requirements
Linux or Windows should both work... theoretically. I know it works on WSL.

I used python 3.10, other versions may or may not work.

You need a graphics card at least on par with the GTX 1060

# Setup
Run `python -m pip install -r install_first.txt` to download Pytorch.
Then run Run `python -m pip install -r install_second.txt` to download the other libraries.
The requirements use pre-compiled wheels compiled with CUDA 12. Be prepared for a large download.

# Usage
On first run be prepared for another large download (~2.5GB)
Run `python main.py`
It takes around ~20s on a GTX 1060

## How does this work?
This uses https://huggingface.co/OPEA/Phi-3.5-vision-instruct-qvision-int4-sym-inc, which is a quantized (smaller) version of the LLM https://huggingface.co/microsoft/Phi-3.5-vision-instruct

## Flash attention (optional)

If you want to use flash attention, I recommend using WSL or Linux. If you *reallly* want to use Windows you can use the prebuilt wheel from https://github.com/oobabooga/flash-attention/releases. 

Generally speaking for Python it's good to use WSL or Linux because there's a lot of tools out there that are a pain to install on windows or simply not able to run on Windows. Speaking from experience.