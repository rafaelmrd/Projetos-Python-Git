
# Identificando letras em imagem de maneira automatica.

import time

import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\garci\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

time.sleep(1)

img = Image.open('lendo1.png')
text = tess.image_to_string(img)

print(text)