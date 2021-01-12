import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('photos/demoimg.jpg')
#cv2.imshow("my image",img)

#printing an image over graph for dimention recognition
print(img.shape)
print(img.shape[1])
print(img.shape[0])
plt.imshow(img)
#| (x=0)
#|
#|
#|
#x
#(y=0)--------->y
plt.show()
#-------------------------------------performing resize------------------

def rescaleFrame(frame,scale=0.75):
    width= int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(height,width)

    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
frame_resize=rescaleFrame(img,scale=0.4)
plt.imshow(frame_resize)
plt.show()
print("new dimention")
print(frame_resize.shape)

cv2.waitKey()
cv2.destroyAllWindows()
