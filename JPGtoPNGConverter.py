import sys 
import os
from PIL import Image

#grab frist and second arguement 
image_folder = sys.argv[1]
new_folder = sys.argv[2]
default_folder = 'DEFAULT_IMAGE_FOLDER'

#check if new folder exists, if not create
if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    print('Folder created')
#if folder exisits, create the default folder
else: 
    os.mkdir(default_folder)
    print(f'{default_folder} was created as {new_folder} already exisits')
    new_folder = default_folder
    pass
#loop through images, convert, and save
for file in os.listdir(image_folder):
    img = Image.open(f'{image_folder}/{file}')
    clean_name = os.path.splitext(file)[0]
    img.save(f'{new_folder}/{clean_name}.png', 'png')
    print('Image(s) saved')