import cv2 as cv

img_get=cv.imread(r'C:\CS\openCV\Data\images\25mva.jpg')
img_get=cv.resize(img_get,(500,500))

txt=cv.putText(img= img_get,
text= "arhaan arif",
org= (50,80),
fontFace= cv.FONT_HERSHEY_PLAIN,
fontScale= 3,
color= (0,0,255),
thickness= 3,
lineType= cv.LINE_4,
bottomLeftOrigin= True) # it creates the mirror img of the text


cv.imshow('img',txt)
cv.waitKey(0)
cv.destroyAllWindows()