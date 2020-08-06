import cv2
import numpy as np
def position(x):
    pass
img=np.zeros((500,500,3),np.uint8)
cv2.namedWindow("CONTROLLER")
cv2.createTrackbar("B","CONTROLLER",0,255,position)
cv2.createTrackbar("G","CONTROLLER",0,255,position)
cv2.createTrackbar("R","CONTROLLER",0,255,position)
s="DON'T CHANGE"
cv2.createTrackbar(s,"CONTROLLER",0,1,position)
while True:
    b=cv2.getTrackbarPos("B","CONTROLLER")
    g=cv2.getTrackbarPos("G","CONTROLLER")
    r=cv2.getTrackbarPos("R","CONTROLLER")
    t=cv2.getTrackbarPos(s,"CONTROLLER")
    if t==0:
        img[:]=[0,0,0]
    else:
        img[:]=[b,g,r]
    cv2.imshow("IMG",img)
    if cv2.waitKey(1)==ord("q"):
        cv2.destroyAllWindows()
        break
cv2.imshow("IMG",img)
if cv2.waitKey(0)==ord("q"):
    cv2.destroyAllWindows()
