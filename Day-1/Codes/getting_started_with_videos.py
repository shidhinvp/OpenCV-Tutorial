import cv2
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("OUTPUT.mkv",fourcc,9,(640,480))
while True:
    ret,frame=cap.read()
    #frame=cv2.flip(frame)
    print("RET:",ret)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(gray)
    cv2.imshow("MOVIE",frame)
    if cv2.waitKey(1)==ord("q"):
        cv2.destroyAllWindows()
        break
cap.release()
out.release()
