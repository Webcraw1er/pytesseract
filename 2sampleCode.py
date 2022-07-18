from PIL import Image
from pytesseract import pytesseract
import os
#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#Define path to image
path_to_images = r'D:\Python\pytesseract\'         # you can also write " ./ ", which indicates "current folder".
#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract
for root, dirs, file_names in os.walk(path_to_images):
    #Iterate over each file_name in the folder
    for file_name in file_names:
        if file_name.endswith(".png"):
        #Open image with PIL
            print(path_to_images+ file_name)
            img = Image.open(path_to_images + file_name)
        #Extract text from image
            text = pytesseract.image_to_string(img)
            print(text)

print(os.getcwd())