import PIL
import os
import os.path
from PIL import Image

f = r'**your directory location**'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((64,64))
    width, height = img.size
    print(width, height)
    img.save(f_img)
