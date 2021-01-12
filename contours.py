import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("photos/mycat.jpg")
#cv2.imshow("my cat",img)

#resize
resize=cv2.resize(img,(700,500))
cv2.imshow("resize",resize)

#gray scale

gray=cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

#blur
blur=cv2.GaussianBlur(gray,(7,7),cv2.BORDER_DEFAULT)
cv2.imshow("blur",blur)

#canny
canny=cv2.Canny(gray,125,175)
cv2.imshow("canny",canny)

#contours

contour,_=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(resize,contour,-1,(0,255,0),2)
cv2.imshow("contours",resize)

cv2.waitKey(0)
cv2.destroyAllWindows()
