from PIL import Image

import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r'/Users/home_dada/Library/Python/3.9/bin'

print(pytesseract.image_to_string(Image.open('/Users/home_dada/BobbyProgramming/KRBV0723-1/MachineLearning/ImageLibrary/trystwithdestiny.png')))

# print(pytesseract.image_to_string(Image.open('/Users/home_dada/BobbyProgramming/KRBV0723-1/MachineLearning/ImageLibrary/jose-11-2022.png')))

# print(pytesseract.image_to_string(Image.open('/Users/home_dada/BobbyProgramming/KRBV0723-1/MachineLearning/ImageLibrary/mini-test.png')))