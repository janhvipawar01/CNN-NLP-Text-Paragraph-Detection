# -*- coding: utf-8 -*-
"""CHOICE 1 CNN/NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qs99pXVSnfIkzBUQOZxjcXa06jcnKy3u
"""

!apt-get install poppler-utils

!pip install pdf2image
!pip install easyocr

from pdf2image import convert_from_path
import easyocr
import numpy as np
import PIL
from PIL import ImageDraw
import spacy

reader = easyocr.Reader(['en'])

images = convert_from_path("/content/ineuron offer letter.pdf")

from IPython.display import display, Image
display(images[0])

bounds = reader.readtext(np.array(images[0]))

def draw_boxes(image, bounds, color='red',width=2):
  draw = ImageDraw.Draw(image)
  for bound in bounds:
    p0, p1, p2, p3 = bound[0]
    draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
  return image
draw_boxes(images[0], bounds)

bounds[1][1]

text=''
for i in range(len(bounds)):
  text=text+bounds[i][1]+'\n'
print(text)