import cv2
img=r"C:\Users\SHIDHIN\Downloads\PYTHON\OPENCV\image\lena.jpg"
img=cv2.imread(img)
cv2.imshow("ORI_IMG",img)
k=cv2.waitKey(0)&0XFF
if k==27:
  cv2.destroyAllWindows()
if k==ord("s"):
  cv2.imwrite(r"C:\Users\SHIDHIN\Downloads\PYTHON\OPENCV\session\OpenCV-Tutorial\LENA_COPY.jpg",img)
  print("SAVED")
  cv2.destroyAllWindows()
  
  

