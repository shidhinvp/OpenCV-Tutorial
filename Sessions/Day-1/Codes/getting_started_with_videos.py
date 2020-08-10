#Links For More Prop_Id Are In The Notes Folder
import cv2
name=input("VID/MOVIE:")
if name=="MOVIE":
  #A VIDEO FILE FROM YOUR FILE LOCATION
  cap=cv2.VideoCapture(r"C:\Users\SHIDHIN\Downloads\Telegram Desktop\DVDWap - Kappela (2019) Mlylm HD AAC.mkv")
  print("WIDTH",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  print("HEIGHT",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
  fourcc=cv2.VideoWriter_fourcc(*"XVID")
  #For Size I Have Inseted (3000,3000) But While Printing Shape The Shape Will Be Changed To Maximum
  out=cv2.VideoWriter(r"C:\Users\SHIDHIN\Downloads\PYTHON\OPENCV\session\OpenCV-Tutorial\Video_Handling.mp4",fourcc,24,(3000,3000))
  print("WIDTH_USING_INT",cap.get(3))
  print("HEIGHT_USING_INT",cap.get(4))
  while True:
    ret,frame=cap.read()
    print(ret)
    cv2.imshow("LIVE",frame)
    if cv2.waitKey(1)==ord("q"):
      cv2.destroyAllWindows()
      break
    if cv2.waitKey(1)==ord("s"):
      #To Save A Video
      out.write(frame)
else:
  #Open Your System's Camera
  cap=cv2.VideoCapture(0)
  #Getting Video Frame Width & Height
  print("WIDTH",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  print("HEIGHT",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
  fourcc=cv2.VideoWriter_fourcc(*"XVID")
  out=cv2.VideoWriter(r"C:\Users\SHIDHIN\Downloads\PYTHON\OPENCV\session\OpenCV-Tutorial\Video_Handling.mp4",fourcc,24,(int(cap.get(3)),int(cap.get(4))))
  #Getting Video Frame Width & Height As Befor But Simple 
  print("WIDTH_USING_INT",cap.get(3))
  print("HEIGHT_USING_INT",cap.get(4))
  while True:
    ret,frame=cap.read()
    #I Have An issue So I Have Add Flip Method
    frame=cv2.flip(frame,-1)
    print(ret)
    cv2.imshow("LIVE",frame)
    if cv2.waitKey(1)==ord("q"):
      cv2.destroyAllWindows()
      break
#Background Cam Will Be Closed
cap.release()
out.release()
