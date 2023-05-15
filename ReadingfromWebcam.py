import cv2 as cv
#Webcam
video=cv.VideoCapture(0)    #'0' is for Default Webcam
video.set(3,640)   #Width
video.set(4,480)   #Height
video.set(10,80)   #Brightness

while True:
    Success, img = video.read()    
    img=cv.resize(img,(350,500))
    cv.imshow('Videos',img)      
    if cv.waitKey(1) & 0xFF==ord('q'):
        break