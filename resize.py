
from PIL import Image
import os, sys
import glob
"""This script resizes jpg images in the folder specified and makes them less heavy"""

root_dir = "/Users/gsole/Documents/Web-Work/between/between_app/static/between_app/images"


for filename in glob.iglob(root_dir + '**/*.jpg', recursive=True):
    print(filename)
    im = Image.open(filename)
    imResize = im.resize((600,850), Image.Resampling.LANCZOS)
    imResize.save(filename , 'JPEG', quality=90)

