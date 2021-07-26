import sys
import os
from PIL import Image

#run as cmd line tool with two arguments, folder with pics and folder to deposit converted pics

img_fldr = sys.argv[1]
output_fldr = sys.argv[2]

#if new folder to deposit converted pics does not exist, create it

if not os.path.exists(output_fldr):
    os.mkdir(output_fldr)

#loop through image folder

for pic in os.listdir(img_fldr):
    img = Image.open(pic)
    img.save(f"{output_fldr}/{pic}.png", "png")

#convert to png

#save to new folder