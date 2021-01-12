import cv2
import matplotlib.pyplot as plt
import numpy as np


img=cv2.imread("photos/lena.jpg")

#gray scale image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('image',gray)

#blur an image

blur=cv2.GaussianBlur(img,(11,11),cv2.BORDER_DEFAULT)
#cv2.imshow('blur',blur)

#edge cascade
#canny edge detection
canny=cv2.Canny(img,125,134)
#cv2.imshow('canny',canny)

#dilating the image

dilated=cv2.dilate(canny,(3,3),iterations=4)
#cv2.imshow('dilated',dilated)

#erodded

erod=cv2.erode(dilated,(7,7),iterations=4)
cv2.imshow("eroded",erod)

#resize

resize=cv2.resize(img,(500,500))
cv2.imshow("resize",resize)

#resizing an image

plt.imshow(img)
plt.show()

crop=img[240:300,240:400]
plt.imshow(crop)
plt.show()
eyecanny=cv2.Canny(crop,125,144)
cv2.imshow("crop",eyecanny)

cv2.waitKey(0)
cv2.destroyAllWindows()