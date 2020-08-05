import cv2
img=(r"C:\Users\SHIDHIN\Downloads\PYTHON\OPENCV\image\lena.jpg")
img=cv2.imread(img)
cv2.imshow("IMG",img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
if k==ord("s"):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("OUTPUT_IMAGE.png",gray)
    print("SAVED")
    cv2.destroyAllWindows()
