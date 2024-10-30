# image reading
import cv2 as cv

img=cv.imread('C:/SDE/openCV/Data/images/1000.jpg')
cv.imshow("1MVA",img)
cv.waitKey(10000)       #image wait time (ms) 0-stay forever
cv.destroyAllWindows()  #closes all windows
cv.destroyWindow()      #closes one window