import cv2
import numpy as np
import matplotlib.pyplot as plt

#draw rectangle
blank= np.zeros((500,500,3),dtype='uint8')
blank[250,:]=0,0,255
blank[:,250]=0,255,0
blank[100:250,250:300]=0,0,255
blank[250:300,100:250]=0,255,0
plt.imshow(blank)
plt.show()
#writr textin image

cv2.putText(blank,"hello",(100,100),cv2.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv2.imshow('blank',blank)

cv2.waitKey(0)
cv2.destroyAllWindows()