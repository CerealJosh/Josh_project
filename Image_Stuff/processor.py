import glob
import os,sys 
import cv2
import random


## Get all the png image in the PATH_TO_IMAGES
imgnames = sorted(glob.glob("/Users/Josh/Desktop/Image_Data/orange_fire/Resized/*jpg"))
def process(imgname):
    temp = cv2.imread(imgname)
    resized = cv2.resize(temp,(224,224))
    imgname2 = "/Resized/".join(os.path.split(imgname))
    print(imgname2)
    cv2.imwrite(imgname2, resized)

def rotateprocess(imagename):
    temp= cv2.imread(imagename)
    rot = random.randint(1,3)
    if rot == 1:
        rotated = cv2.rotate(temp,cv2.ROTATE_90_CLOCKWISE)
    elif rot ==2:
        rotated = cv2.rotate(temp, cv2.ROTATE_180)
    else:
        rotated =cv2.rotate(temp, cv2.ROTATE_90_COUNTERCLOCKWISE)
    imgname2 = "/Rotated/".join(os.path.split(imgname))
    print(imgname2)
    cv2.imwrite(imgname2,rotated )

def zoomprocess(imgname):
    temp = cv2.imread(imgname);
    

for imgname in imgnames:
    ## Your core processing code 
    res = rotateprocess(imgname)
    #res = process(imgname)

    ## rename and write back to the disk
    #name, ext = os.path.splitext(imgname)
    #imgname2 = name+"_res"+ext
    #imgname2 = "_res".join(os.path.splitext(imgname))
    #cv2.imwrite(imgname2, res)



