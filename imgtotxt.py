#Install py tesseract first by typing "pip install pytesseract"
#If you are getting an error regarding pytesseract, download pytesseract manually on this link "https://github.com/UB-Mannheim/tesseract/wiki"

import pytesseract as tess
#Insert the file location of "tesseract.exe"
tess.pytesseract.tesseract_cmd = r'C:\Users\Your_User\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

#Insert the file name of your image
img = Image.open('sample text.png')
text = tess.image_to_string(img)

print (text)
