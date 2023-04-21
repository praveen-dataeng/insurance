# !sudo apt-get install poppler-utils
# !sudo apt install tesseract-ocr
# Importing libraries

import pandas as pd
import numpy as np
import re

# pdf2image
from pdf2image import convert_from_path, convert_from_bytes
# from IPython.display import display, Image

# openCV
import cv2 as cv
# from PIL import Image

# pyTesseract
import pytesseract
import shutil
import os
# import random
# try:
#     from PIL import Image
# except ImportError:
#     import Image

# Open cv to process the image
def preprocesing_img(img):
  gray_img = cv.cvtColor(np.array(img), cv.COLOR_BGR2GRAY)
  resized_img = cv.resize(gray_img, None, fx=1.5, fy=1.5, interpolation=cv.INTER_LINEAR)
  processed_img = cv.adaptiveThreshold(
      resized_img,
      255,
      cv.ADAPTIVE_THRESH_GAUSSIAN_C,
      cv.THRESH_BINARY,
      61,
      11
      )  
  return processed_img