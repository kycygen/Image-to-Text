#Install py tesseract first by typing "pip install pytesseract"

import pytesseract as tess
#Insert the file location of "tesseract.exe"
tess.pytesseract.tesseract_cmd = r''
from PIL import Image

#Insert the file name of your image
img = Image.open('sample text.png')
text = tess.image_to_string(img)

print (text)
