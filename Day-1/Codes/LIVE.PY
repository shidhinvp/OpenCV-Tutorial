import cv2
from datetime import datetime
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,-1)
    text=str(datetime.now())
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,text,(10,20),font,0.5,(255,0,255),3)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("LIVE",gray)
    if cv2.waitKey(1)==ord("q"):
        cv2.destroyAllWindows()
        break
cap.release()
