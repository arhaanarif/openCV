# Destory multiple windows or single
import cv2 as cv

img=cv.imread('C:/SDE/openCV/Data/images/1000.jpg')
cv.imshow("1MVA",img)
cv.imshow("1000KVA",img)
cv.waitKey(0)       #image wait time (ms) 0-stay forever
# cv.destroyAllWindows()  #closes all windows
cv.destroyWindow('1000KVA')      #closes one window