import cv2
img=r"C:\Users\SHIDHIN\Downloads\PYTHON\OPENCV\session\OpenCV-Tutorial\Images\lena.jpg"
img=cv2.imread(img)
print("IMAGE",img.shape)
#Converting Image's Color_Space BGR2GRAY
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print("GRAY",gray.shape)
#Spliting Images
b,g,r=cv2.split(img)
#Merge Images
Merge_image=cv2.merge((b,g,r))
#Showing All The Images
cv2.imshow("MERGE",Merge_image)
cv2.imshow("B",b)
cv2.imshow("G",g)
cv2.imshow("R",r)
cv2.imshow("GRAY",gray)
cv2.imshow("ORG_IMG",img)
if cv2.waitKey(0)==ord("q"):
  cv2.destroyAllWindows()
#Drawing Function's In Opencv
cv2.line(img,(0,100),(100,100),(0,0,255),3)
cv2.imshow("EDITED_IMG",img)
if cv2.waitKey(0)==27:
  cv2.destroyAllWindows()




