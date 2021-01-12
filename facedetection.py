import cv2
import matplotlib.pyplot as plt
import numpy as np

cascade=cv2.CascadeClassifier("haarcascade_smile.xml")

img=cv2.imread("photos/smileface.jpg")
body=cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=22)

for (x,y,w,h) in body:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("img",img)

print(body)
cv2.waitKey(0)
cv2.destroyAllWindows()
