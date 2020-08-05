import cv2
cap=cv2.VideoCapture(r"C:\Users\SHIDHIN\Downloads\Telegram Desktop\DVDWap - Kappela (2019) Mlylm HD AAC.mkv")
fourcc=cv2.VideoWriter_fourcc(*"XVID")
print(cap.get(3))
print(cap.get(4))
out=cv2.VideoWriter("OUTPUT.mkv",fourcc,9,(int(cap.get(3)),int(cap.get(4))))
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
