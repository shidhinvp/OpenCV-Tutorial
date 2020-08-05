import cv2
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
#get cap width and height using cap.get(3) for width, cap.get(4) for height and
#insert in into VideoWriter
out=cv2.VideoWriter("OUTPUT.avi",fourcc,9,(int(cap.get(3)),int(cap.get(4))))
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,-1)
    out.write(frame)
    cv2.imshow("LIVE",frame)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
