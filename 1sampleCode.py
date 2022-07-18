"""
Tesseract is an OCR
OCR is an abbreviation of Optical character recognition.




"""


from PIL import Image
from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'     # r in front of the path is for making sure
                    #that the string literal is a raw string-> omitting this will lead to a code not running

                #below is an example of why you need a raw string. 
                    # >>> mystring = "hello\tworld\nI'm Kim"
                    # >>> print(mystring)
                    # hello	world
                    # I'm Kim
                    # >>> mystring_raw = r"hello\tworld\nI'm Kim"
                    # >>> print(mystring_raw)
                    # hello\tworld\nI'm Kim

#Define path to image
path_to_image = 'sampletext1-ocr.png'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
img = Image.open(path_to_image)

#Extract text from image
text = pytesseract.image_to_string(img)

print(text)


