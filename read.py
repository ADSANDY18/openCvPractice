import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('photos/lena.jpg')
print(img)
cv2.imshow('picture',img)
cv2.waitKey()
cv2.destroyAllWindows()