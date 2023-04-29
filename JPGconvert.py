import sys
import os
from PIL import Image

# grab first two arguments, [1] input folder and [2]output folder
image_folder = sys.argv[1]
converted_folder = sys.argv[2]

# if converted folder doesn't exist in curent directory, make one
if not os.path.exists(converted_folder):
    os.makedirs(converted_folder)

# loop through files in desired folder
for filename in os.listdir(image_folder):
    image = Image.open(f"{image_folder}{filename}")  # open file

    # split the file into its name and type (grab the name)
    clean_name = os.path.splitext(filename)[0]
    print(f"{clean_name} converted to JPG form")
    image.save(f'{converted_folder}{clean_name}.jpg',
               "jpeg")  # save images i new folder

print(f"Complete: images saved in {converted_folder} folder")
