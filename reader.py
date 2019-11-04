###RUN FIRST BEFORE RUNNING THE SCRIPT!###
#export TESSDATA_PREFIX='/usr/local/share/'
import sys
import os
import re
import cv2
import PIL
import pandas as pd
import pytesseract
from tqdm import tqdm_notebook
from PIL import Image
import numpy as np
from os import listdir,makedirs
from os.path import isfile,join

#Image cropper

path = 'RawImg' #Source Folder
path2 = 'IMAGES' #Destination Folder

try:
    makedirs(path2)
except:
    print ("Destination path is good!")

image_list = []

files = [f for f in listdir(path) if isfile(join(path,f))] 

print ("Cropping images...")

for item in files:
    fullpath = os.path.join(path, item)
    im=Image.open(fullpath)
    f2, e = os.path.splitext(fullpath)
    imCrop = im.crop((0, 50, 700, 300))
    open_cv_image = np.array(imCrop)
    toSaveImg = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
    dstPath = join(path2,item)
    cv2.imwrite(dstPath,toSaveImg)


print ("Image successfully cropped")

#Cropped image to Grayscale conversion

path = 'IMAGES' # Source Folder
dstpath = 'grayscaleresult' # Destination Folder

try:
    makedirs(dstpath)
except:
    print ("Destination path is good!")

# Folder won't used
files = [f for f in listdir(path) if isfile(join(path,f))]

print ("Converting images to Grayscale...")

for image in files:
    try:
        img = cv2.imread(os.path.join(path,image))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        dstPath = join(dstpath,image)
        cv2.imwrite(dstPath,gray)
    except:
        print ("{} is not converted".format(image))


#Grayscale image to CSV conversion

image_dir = 'IMAGES' #Source folder 
ocr_dir = 'csvresult' #Destination folder 

image_files = os.listdir(image_dir)
if not os.path.isdir(ocr_dir):
    os.mkdir(ocr_dir)
print('Writing output of OCR to directory %s' % ocr_dir)
for f in image_files:
    image_file = os.path.join(image_dir, f)
    #img = Image.open('spt3Cropped.jpg').convert('L')
    #ret,image = cv2.threshold(np.array(image_file), 125, 255, cv2.THRESH_BINARY)
    #img = Image.fromarray(image_file.astype(np.uint8))
    #info = pytesseract.image_to_string(image_file)
    info = pytesseract.image_to_string(image_file)
    csv_file = os.path.join(ocr_dir, os.path.splitext(f)[0]+'.csv')
    with open(csv_file, 'wt') as file:
        file.write(info)

print("DONE!")
