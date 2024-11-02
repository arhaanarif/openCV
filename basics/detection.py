import cv2 as cv
old_img = cv.imread(r'C:\CS\openCV\Data\images\img11.jpeg')
old_img=cv.resize(old_img,(500,500))

#creatin line over the image
new_img=cv.line(img= old_img,
pt1= (120,145),
pt2= (320,110),
color=(0,255,0),
thickness= 3,
lineType= 4)

txt=cv.putText(img= old_img,
text= "Nikola Tesla",
org= (90,120),
fontFace= cv.FONT_HERSHEY_PLAIN,
fontScale= 3,
color= (15,2,155),
thickness= 3,
lineType= cv.LINE_4,
bottomLeftOrigin= False)

#creating rectangle over the image
new_img=cv.rectangle(img= old_img,
pt1= (120,145),
pt2= (320,400),
color=(0,255,0),
thickness= 3,
lineType= 4)


cv.imshow('img',new_img)
cv.waitKey(0)
cv.destroyAllWindows()
