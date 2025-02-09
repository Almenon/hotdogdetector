This repository contains a python script that runs a multimodal, state-of-the-art AI model for detecting hotdogs. It can run on multiple operating systems and even on old hardware.

# But WHY?

You go to Costco. You are about to buy the legendary $1.5 hotdog, but a stranger in a trenchcoat approaches you and offers a blackmarket 50¢ hotdog. 

You pause. The stranger is trustworthy, but this deal seems too good to be true. You whip out your computer, manuever it around to take a picture of the hotdog, save it, run `python main.py`, and wait 20 seconds. The AI says it's not a hotdog! You scream and smack the fake hotdog out of their hands. 

The authorities are alerted and the stranger is arrested. You're a hero!

## But seriously, why?

I was curious if

A) I could run a LLM on old hardware and 

B) how fast it would run

The answer was "yes, but not very fast" 🐢. 



I was also curious what the elctricity usage would be. It turns out it's very small. The max draw of a GTX 1060 is 120 watts, and where I live electricity is .14 cents for an hour of 1000 watts. You could detect hotdogs non-stop for an hour and still not even pay 14 cents. Newer graphics cards, despite using more watts, use less electricity per image because they are so much faster.

# Requirements
Python 3.10 or 3.11 (higher versions may work too)

You need a graphics card at least on par with the GTX 1060, preferably better. In other words, you need a graphics card with at least 6GB memory.

# Setup
Run `python -m pip install -r install_first.txt` to download Pytorch.
Then run `python -m pip install -r install_second.txt` to download the other libraries.
The requirements use pre-compiled wheels compiled with CUDA 12. Be prepared for a large download.

# Usage
On first run be prepared for another large download (~2.5GB). Run `python main.py`. It takes around ~20s on a GTX 1060, or just ~1s on a GTX 3090

## How does this work?
This uses https://huggingface.co/OPEA/Phi-3.5-vision-instruct-qvision-int4-sym-inc, which is a quantized (smaller) version of the LLM https://huggingface.co/microsoft/Phi-3.5-vision-instruct

## Flash attention (optional)

FLash attention can give you a slight speedup. If you want to use flash attention, I recommend using WSL or Linux. If you *reallly* want to use Windows you can use the prebuilt wheel from https://github.com/oobabooga/flash-attention/releases.

Generally speaking for Python it's good to use WSL or Linux because there's a lot of tools out there that are a pain to install on windows or simply not able to run on Windows. Speaking from experience.

To use Flash attention uncomment `# _attn_implementation='flash_attention_2'`
