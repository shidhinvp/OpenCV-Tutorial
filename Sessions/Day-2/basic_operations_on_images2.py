import cv2
img=r"C:\Users\SHIDHIN\Downloads\PYTHON\OPENCV\session\OpenCV-Tutorial\Images\star-1-300x168.jpg"
img=cv2.imread(img)
print(img.shape)
img2=r"C:\Users\SHIDHIN\Downloads\PYTHON\OPENCV\session\OpenCV-Tutorial\Images\star-2.jpg"
img2=cv2.imread(img2)
print(img2.shape)
img=cv2.resize(img,(300,300))
img2=cv2.resize(img2,(300,300))
add=cv2.add(img,img2)
wadd=cv2.addWeighted(img,0.1,img2,0.9,100)
sub=cv2.subtract(img,img2)
cv2.imshow("SUB",sub)
cv2.imshow("ADDW",wadd)
cv2.imshow("img1",img)
cv2.imshow("IMG2",img2)
cv2.imshow("operations",add)
if cv2.waitKey(0)==ord("q"):
    cv2.destroyAllWindows()
