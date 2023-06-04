#Automation program for Photo Editing

#Step 1: Import Pillow Library
from PIL import Image, ImageEnhance, ImageFilter
import os

#Step 2: Create path for Original and Edited photos

path = r'C:\Users\TowfNguyenx\Desktop\TheRoot\Work\Coding\Anhkisu\PythonPracticeProjects\Automation1\OG-img' 
pathEdited = r'C:\Users\TowfNguyenx\Desktop\TheRoot\Work\Coding\Anhkisu\PythonPracticeProjects\Automation1\Edited-img'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L') #Turn to B&W

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathEdited}/{clean_name}_edited.jpg')

