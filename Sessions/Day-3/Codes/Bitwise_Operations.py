import cv2
import numpy as np
img1=np.zeros((250,500,3),np.uint8)#2^8-1=255
print(img1.shape)
cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2=np.ones((250,500,3),np.uint8)
cv2.rectangle(img2,(0,0),(250,500),(255,255,255),-1)
bitwise_and=cv2.bitwise_and(img1,img2)
bitwise_or=cv2.bitwise_or(img1,img2)
bitwise_xor=cv2.bitwise_xor(img1,img2)
bitwise_not=cv2.bitwise_not(img1)
cv2.imshow("BIT_NOT",bitwise_not)
"""
cv2.imshow("BIT_XOR",bitwise_xor)
cv2.imshow("BIT_OR",bitwise_or)
cv2.imshow("BIT_AND",bitwise_and)
"""
cv2.imshow("IMAGE2",img2)
cv2.imshow("IMG1",img1)
cv2.waitKey(0)
