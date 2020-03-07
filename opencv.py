import numpy as np
import cv2
from pyimagesearch.shapedetector import ShapeDetector
import imutils
from Design.Design import Design
from Tambou.tambou import Tambou 
from HandleCollision.HandleCollision import HandleCollision
import simpleaudio as sa

#image1=cv2.imread('test.jpg')
#image2=cv2.imread('tt.png')

#dd=Design()
#image2=dd.resizeImage(200,image2)
#dd.addImage(20,20,image1,image2)
#cv2.imshow('image1',image1)


#define variable
"""dd=Design()

image2=dd.resizeImage(75,image2)
"""
HC=HandleCollision()
dd=Design()
wave_obj = sa.WaveObject.from_wave_file("crash.wav")

image2=cv2.imread('tt.png')
image2=dd.resizeImage(75,image2)

cap = cv2.VideoCapture(0)
tanb = Tambou(image2,20,300,wave_obj)
HC.registerObject(tanb)

#lo = np.array([110,50,50])
#hi = np.array([130,255,255])
color_infos = (0,0,255)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.namedWindow("Camera",cv2.WND_PROP_FULLSCREEN)
#cv2.setWindowProperty("Camera", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.namedWindow("image2",cv2.WND_PROP_FULLSCREEN)



def nothing(x):
    pass

cv2.createTrackbar('H','image2',0,255,nothing)
cv2.createTrackbar('S','image2',53,255,nothing)
cv2.createTrackbar('V','image2',0,255,nothing)
cv2.createTrackbar('H1','image2',91,255,nothing)
cv2.createTrackbar('S1','image2',255,255,nothing)
cv2.createTrackbar('V1','image2',194,255,nothing)

while(True):
    #open the window in fullscreen
   
    

    #capture ecran
    ret, frame = cap.read()
    #effet miroir camera
    frame = cv2.flip(frame,1)
   
    #changement d'espace colorimetrique pour mieux segmenter la couleur
    image = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #affinement de l'image
    #image = cv2.blur(image,(7,7))
    #filtrage couleur to track avec valeur min et max
    lo=np.array([cv2.getTrackbarPos('H','image2'),cv2.getTrackbarPos('S','image2'),cv2.getTrackbarPos('V','image2')])
    hi=np.array([cv2.getTrackbarPos('H1','image2'),cv2.getTrackbarPos('S1','image2'),cv2.getTrackbarPos('V1','image2')])
    
    mask = cv2.inRange(image,lo,hi)
    mask = cv2.erode(mask , None, iterations = 4)
    mask = cv2.dilate(mask , None, iterations = 4)
    image3= cv2.bitwise_and(frame,frame, mask = mask) 

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    
    sd = ShapeDetector()
    for c in cnts:
        #print(c)

        # compute the center of the contour, then detect the name of the
        # shape using only the contour
       
        shape = sd.isCircle(c)

        if(shape):
            M = cv2.moments(c)
            cX = int((M["m10"] / M["m00"]) )
            cY = int((M["m01"] / M["m00"]) )
            HC.Handle((cX,cY))


            cv2.circle(frame,(cX,cY), 5,color_infos,10 )
            
            #img = cv2.imread('test.jpg',1)
    cv2.rectangle(frame,(20,300),(20+image2.shape[1],300+image2.shape[0]),color_infos)

    

    tanb.draw(frame)           
    cv2.imshow('image2',image3)
    cv2.imshow('Camera',frame)


    if cv2.waitKey(1)  == ord('v'):
        break

cap.release()
cv2.destroyAllWindows()

#img = cv2.imread('test.jpg',1)
#cv2.imshow('Image',img)
#cv2.waitKey(0)
#cv2.destroyAllwindows()
