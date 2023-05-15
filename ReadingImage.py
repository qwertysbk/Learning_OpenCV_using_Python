import cv2
#import cv2 module from python library

path = "OpenCV_Images/Dog.jpg" #We are assigning the image location to a varaible path

img =cv2.imread(path)
#imread('Image location')
#this method reads the image and saves it variable 'img'

cv2.imshow("Dog",img)
#imshow('Window_Name',variable_name)
#this method creates a new window where the image is displayed
#If image size is large/is highly pixalated, then it will fill the window completely

cv2.waitKey(0)
#Waitkey is simply used for the new window to remain open and (0) will keep it open till closed