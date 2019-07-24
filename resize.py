import os 
import cv2 as cv

os.chdir("D:\\codes\\python\\dog2sketch\\dataset\\trainB") # directory of original images
l = os.listdir()

for i in range(len(l)):
    img = cv.imread(l[i])
    print(l[i])
    img = cv.resize(img, (128,128))
    cv.imwrite("D:\\codes\\python\\dog2sketch\\dataset\\resized\\trainB\\%d.jpg"%i,img) # save resized images
