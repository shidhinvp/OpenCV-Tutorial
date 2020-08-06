import cv2
img=r"C:\Users\SHIDHIN\Downloads\PYTHON\OPENCV\session\OpenCV-Tutorial\Images\messi.jpg"
img=cv2.imread(img)
b,g,r=cv2.split(img)
mimg=cv2.merge((b,g,r))
ball=img[280:340,330:390]
img[273:333,100:160]=ball
cv2.imshow("IMAGE",img)
cv2.waitKey(0)
