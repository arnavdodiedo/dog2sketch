import os 
import cv2 as cv

os.chdir("C:\\Users\\ARKARMAR\\cyclegan\\datasets\\trainB") # directory of original images
l = os.listdir()

for i in range(len(l)):
    img = cv.imread(l[i])
    #print(l[i])
    img = cv.resize(img, (128,128))
    cv.imwrite("C:\\Users\\ARKARMAR\\cyclegan\\datasets\\resized\\trainB\\%d.jpg"%i,img) # save resized images
