import cv2
import datetime
cap=cv2.VideoCapture(0)
while True:
  ret,frame=cap.read()
  frame=cv2.flip(frame,-1)
  text=str(datetime.datetime.now())
  font=cv2.FONT_HERSHEY_COMPLEX
  cv2.putText(frame,text,(10,20),font,0.5,(255,218,255),2)
  cv2.imshow("LIVE",frame)
  if cv2.waitKey(1)==ord("q"):
    cv2.destroyAllWindows()
    break
cap.release()
