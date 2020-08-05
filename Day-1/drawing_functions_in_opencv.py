import cv2
img=r"C:\Users\SHIDHIN\Downloads\PYTHON\OPENCV\image\lena.jpg"
img=cv2.imread(img)
cv2.line(img,(0,0),(300,300),(140,73,105),3)#105, 73, 140
cv2.arrowedLine(img,(0,50),(50,50),(0,0,255),3)
cv2.rectangle(img,(0,70),(100,200),(0,255,0),2)
cv2.circle(img,(150,150),50,(255,0,0),3)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,"OPENCV",(100,500),font,1,(255,255,255),2)
cv2.imshow("FRAME",img)
cv2.waitKey(0)
