from datetime import datetime

import requests
from PIL import Image

print('WELCOME TO HOTDOG DETECTOR AI - THE MOST HIGH TECH WAY TO DETECT A HOTDOG, GUARANTEED')
print('initializing AI... this might take a while\n')
from ai import AI
ai = AI("hotdog")
print('AI initialized 🧠')

def analyze_and_print_result(image_url):

  image_url = image_url.strip()

  # download image
  image = Image.open(requests.get(image_url, stream=True).raw)

  # pass image to AI for analysis
  aistart = datetime.now()
  print('Thinking...')
  response = ai.detect_object(image)

  if 'yes' in response.lower():
    response = "\n\n🌭🌭🌭🌭🌭 HOTDOG DETECTED 🌭🌭🌭🌭🌭\n"
  else:
    response = "\n\n🤚🛑🌭 NOT HOTDOG! 🌭🛑🤚\n"
  print(response)

  print(f'AI thinking complete in {datetime.now()-aistart} seconds')


while True:
  image_url = input("Paste in a link to the image you want to analyze > ")
  analyze_and_print_result(image_url)
