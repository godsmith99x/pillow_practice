import sys
import os
from PIL import Image

'''
Run as cmd line tool with two arguments, folder with pics and folder to deposit converted pics
'''

img_fldr = sys.argv[1]
output_fldr = sys.argv[2]

if not os.path.exists(output_fldr):
    os.mkdir(output_fldr)
'''
If new folder to deposit converted pics does not exist, create it
'''

for pic in os.listdir(img_fldr):
    img = Image.open(f"{img_fldr}/{pic}")
    pic_name = pic.replace(".jpg", ".png")
    img.save(f"{output_fldr}/{pic_name}", "png")
    '''
    Loop through image folder
    Convert to png
    Save to new folder
    '''
