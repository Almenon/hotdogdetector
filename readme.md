# Requirements
Linux or Windows should both work, but if you use Windows make sure to use WSL.
If you're dead set on using native Windows then you either need to compile flash attention 2 yourself (which takes a very long time unless you have a powerful CPU)
or you need to use a prebuilt wheel from https://github.com/oobabooga/flash-attention/releases. I recommend using WSL instead because there's a lot of tools out there that are a pain to install on windows or simply not able to run on Windows. Speaking from experience.

You need to use python 3.10

# Setup
Run `python -m pip install -r install_first.txt` to download Pytorch.
Then run Run `python -m pip install -r install_second.txt` to download the other libraries.
The requirements use pre-compiled wheels compiled with CUDA 12. Be prepare for a large download (~3GB).

# Usage
On first run be prepared for another large download (~16GB)