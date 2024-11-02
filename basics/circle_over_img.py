import cv2 as cv

old_img=cv.imread(r"C:\CS\openCV\Data\images\img12.jpeg")
old_img=cv.resize(old_img,(500,500))

#circle
new_img=cv.circle(img= old_img,
center= (300,250),
radius= 175,
color=  (0,255,0),
thickness= -4,  #-1 it will fill the circle
lineType= 16,)

#ellipse
new_img=cv.ellipse(img= old_img,
center=(300,250),
axes= (50,100),
angle=30,
startAngle=0,
endAngle=360 ,
color= (255,0,0),
thickness=4,
lineType= 16)



cv.imshow('img',new_img)
cv.waitKey(0)
cv.destroyAllWindows()
