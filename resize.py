
from PIL import Image
import os, sys
import glob

root_dir = "/Users/gsole/Library/CloudStorage/OneDrive-Personal/2_Programing/2_Django/between/between_app/static/between_app/images"


for filename in glob.iglob(root_dir + '**/*.jpg', recursive=True):
    print(filename)
    im = Image.open(filename)
    imResize = im.resize((400,850), Image.Resampling.LANCZOS)
    imResize.save(filename , 'JPEG', quality=90)

