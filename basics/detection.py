import cv2 as cv
old_img = cv.imread(r'C:\CS\openCV\Data\images\img11.jpeg')
old_img=cv.resize(old_img,(500,500))

new_img=cv.line(img= old_img,
pt1= (120,145),
pt2= (320,110),
color=(0,255,0),
thickness= 3,
lineType= 4)

cv.imshow('img',new_img)
cv.waitKey(0)
cv.destroyAllWindows()
