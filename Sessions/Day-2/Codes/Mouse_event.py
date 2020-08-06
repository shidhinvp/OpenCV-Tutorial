import cv2
import numpy as np
#events=[i for i in dir(cv2) if "EVENT" in i]
#print(events)
def click_event(event,x,y,flags,param):
    if event ==cv2.EVENT_LBUTTONDOWN:
        print("FLAGS",flags)
        print("PARAM",param)
        font=cv2.FONT_HERSHEY_SIMPLEX
        text=str(x)+" ,"+ str(y)
        cv2.putText(img,text,(x,y),font,1,(0,0,255),3)
        cv2.imshow("IMAGE",img)
    if event==cv2.EVENT_RBUTTONDOWN:
        mycolorimage=np.zeros((512,512,3),np.uint8)
        b=img[x,y,0]
        g=img[x,y,1]
        r=img[x,y,2]
        mycolorimage=np.zeros((342,548,3),np.uint8)#2^8-1
        mycolorimage=[b,g,r]
        cv2.imshow("NUMPY",mycolorimage)
img=r"C:\Users\SHIDHIN\Downloads\PYTHON\OPENCV\session\OpenCV-Tutorial\Images\lena.jpg"
img=cv2.imread(img)
print(img.shape)
#numimg=np.zeros((342,548),np.uint8)#2^8-1
#cv2.imshow("NUMPY",numimg)
cv2.imshow("IMAGE",img)
cv2.setMouseCallback("IMAGE",click_event)
