import cv2
import numpy as np
def position(x):
    pass
#img=r"C:\Users\SHIDHIN\Downloads\PYTHON\OPENCV\image\balls.jpg"
#img=cv2.imread(img)
cap=cv2.VideoCapture(0)
#hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.namedWindow("CONTROLLER")
cv2.createTrackbar("LH","CONTROLLER",0,255,position)
cv2.createTrackbar("LS","CONTROLLER",0,255,position)
cv2.createTrackbar("LV","CONTROLLER",0,255,position)
cv2.createTrackbar("DH","CONTROLLER",255,255,position)
cv2.createTrackbar("DS","CONTROLLER",255,255,position)
cv2.createTrackbar("DV","CONTROLLER",255,255,position)
while True:
    ret,frame=cap.read()
    img=cv2.flip(frame,-1)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lh=cv2.getTrackbarPos("LH","CONTROLLER")
    ls=cv2.getTrackbarPos("LS","CONTROLLER")
    lv=cv2.getTrackbarPos("LV","CONTROLLER")
    dh=cv2.getTrackbarPos("DH","CONTROLLER")
    ds=cv2.getTrackbarPos("DS","CONTROLLER")
    dv=cv2.getTrackbarPos("DV","CONTROLLER")
    l_c=np.array([lh,ls,lv])
    d_c=np.array([dh,ds,dv])
    mask=cv2.inRange(hsv,l_c,d_c)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("LIVE",img)
    cv2.imshow("MASK",mask)
    cv2.imshow("RES",res)
    if cv2.waitKey(1)==ord("q"):
        cv2.destroyAllWindows()
        break
cap.release()
    

