import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('cow1.jpeg',1)

img = cv2.imread('cow1.jpeg',0)

# gray = cv2.cv2tColor(img, cv2.COLOR_BGR2GRAY)

row , col = img.shape

print(row,col)
# retval, threshold = cv2.threshold(gray, 60 , 255, cv2.THRESH_BINARY)
# ret,th=cv2.threshold(gray,127,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# cv2.imshow("DSSDDSD",th)
# #while(True):
# cv2.imshow('img', th)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# img = cv2.imread('gradient.png',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
ret,thresh6 = cv2.threshold(img,127,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV', 'binary + otsu ' ]
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5, thresh6]

rowt , colt = thresh1.shape
number_of_whitePixels= []
print(rowt,colt)

"""
   following block determines the position of leg from a segmented image
"""
for i in range (0,col-1):
    cnt=0
    for j in range(0,row-1):
        if(thresh1[j][i]==255):
            cnt=cnt+1
            # print (cnt)
    number_of_whitePixels.append(cnt)

print(max(number_of_whitePixels)) 
position_of_max_val = number_of_whitePixels.index(max(number_of_whitePixels))
print(position_of_max_val)

"""
    following block visualises different threshold
"""

print(len(images))
for i in range(len(images)):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


cv2.waitKey(1) & 0xFF == ord('q')
cv2.destroyAllWindows()