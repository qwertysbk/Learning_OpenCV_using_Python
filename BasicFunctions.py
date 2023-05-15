###### RESIZING IMAGE ######
import cv2
path = "OpenCV_Images/Dog.jpg"
img=cv2.imread(path)
img=cv2.resize(img,(300,250))
#resizes the image to given parameters
cv2.waitKey(0)

###### SAVING IMAGE ######
import cv2
path = "OpenCV_Images/Dog.jpg"
img=cv2.imread(path)
img=cv2.resize(img,(300,250))
#Save the new image
cv2.imwrite('Saved Image.jpg',img)
#cv.imwrite('Image Name and extension', variable name used for image)
cv2.waitKey(0)

###### GREY IMAGE ######
import cv2
path = "OpenCV_Images/Dog.jpg"
img=cv2.imread(path)
img=cv2.resize(img,(300,250))
imGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cvtColor is a package that converts image into any color
cv2.imshow("GREY IMAGE",imGray)
cv2.waitKey(0)

###### BLUR IMAGE ######
import cv2
path = "OpenCV_Images/Dog.jpg"
img=cv2.imread(path)
img=cv2.resize(img,(300,250))
imBlur=cv2.GaussianBlur(img,(27,37),0)
#GaussianBlur is one method of blurring the image
cv2.imshow("BLUR IMAGE",imBlur)
cv2.waitKey(0)

###### CANNY IMAGE ######
import cv2
path = "OpenCV_Images/Dog.jpg"
img=cv2.imread(path)
img=cv2.resize(img,(300,250))
imCanny=cv2.Canny(img,100,100)
#Canny method of creating a canny image
cv2.imshow("CANNY IMAGE",imCanny)
cv2.waitKey(0)

###### DIALATED IMAGE #######
import cv2
import numpy as np      #importing numpy 
path = "OpenCV_Images/Dog.jpg"
img=cv2.imread(path)
img=cv2.resize(img,(300,250))
kernel=np.ones((5,5),np.uint8)
imDialation=cv2.dilate(img,kernel,iterations=3)
#is used to increase image edges
cv2.imshow("DIALATED IMAGE",imDialation)
cv2.waitKey(0)

###### ERODED IMAGE ######
import cv2
import numpy as np
path = "OpenCV_Images/Dog.jpg"
img=cv2.imread(path)
img=cv2.resize(img,(300,250))
kernel=np.ones((5,5),np.uint8)
imEroded=cv2.erode(img,kernel,iterations=3)
#is used to decrease image edges
cv2.imshow("ERODED IMAGE",imEroded)
cv2.waitKey(0)