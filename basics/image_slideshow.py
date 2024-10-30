import cv2 as cv
import numpy as np
import os

list_name = os.listdir(r'C:\CS\openCV\Data\images')
print(list_name)

for name in list_name:
    path = 'C:\\CS\\openCV\\Data\\images'
    img_name = path + '\\' + name
    img = cv.imread(img_name)
    img = cv.resize(img, (300, 400))
    cv.imshow('pic', img)
    cv.waitKey(1000)
cv.destroyAllWindows()
