# resizing the image

import cv2 as cv

img=cv.imread(r"C:/SDE/openCV/Data/images/8mva.jpg")
re_img=cv.resize(img,(500,500))
cv.imshow("MVA",re_img)
cv.waitKey(0)
cv.destroyAllWindows()