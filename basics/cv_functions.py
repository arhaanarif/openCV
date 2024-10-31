import cv2 as cv
import numpy as np

img=cv.imread(r'C:\CS\openCV\data\images\25mva.jpg',0)   # 1 means rgb & 0 means greyscale

print(img.shape)
'''
if flags= 1 or -1 img.shape will give output as (577,1024,3) where 577|1024 means pixels of image
and 3 means channels of image -rgb 
in case of flags= 0 this will generate greyscale image, img.shape giving output of only pixels as 
(577,1024) no channels because of greyscale image
'''

print(img.dtype)
print(img.size)
# print(img)

img=cv.resize(img,(500,500))
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()