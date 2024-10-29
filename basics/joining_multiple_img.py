# Joining multiple images

import cv2 as cv
import numpy as np
img=cv.imread(r"C:\CS\openCV\Data\images\8mva.jpg")
re_img=cv.resize(img,(200,300))


h=np.hstack((re_img,re_img,re_img))    #for horizontal alignment
v=np.vstack((re_img,re_img))    #for vertical alignment

v=np.vstack((h,h)) #for multiple alignment

cv.imshow('pic',v)
cv.waitKey(0)
cv.destroyAllWindows()