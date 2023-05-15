import cv2  #import cv2 module from python library

path = 'OpenCV_Videos/Puppy.mp4'    #We are assigning the Video location to a varaible path

video=cv2.VideoCapture(path)    #VedioCapture('Vedio location')

#Vedio is a Sequence of Images
#While loop will access images one by one 
while True:
    Success, img = video.read()     
    img=cv2.resize(img,(350,500))
    cv2.imshow('Videos',img)      
    if cv2.waitKey(1) & 0xFF==ord('q'):    #Adds a delay and if 'q' is prepared then window exits
        break