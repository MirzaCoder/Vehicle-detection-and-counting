#WEBCAM REALTIME READ
import cv2
import  numpy as np
#cap = cv2.VideoCapture(0)
cap=cv2.VideoCapture('Traffic.mp4');

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,5.0,(640,480))#vary fps depending on th required speed

car_cascade = cv2.CascadeClassifier('cars.xml')

#eye_cascade = cv2.CascadeClassifier('p1.xml')
count=0
#0=webcam1
#1=webcam2

while True:
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#creates a frame with gray layer)
    car = car_cascade.detectMultiScale(gray, 1.3, 10)
  #  eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in car:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        count+=1
        
        
   #for (ex,ey,ew,eh) in eyes:
   # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.putText(frame, str(count),(10,400), cv2.FONT_ITALIC, 2,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    out.write(frame)#opens the gray frame declared earlier with title gray
    
    
    if cv2.waitKey(10) & 0xFF==ord('q'):#if wait key is not declared the frame is opened but not seen.
        break

cap.release()
out.release()
cv2.destroyAllWindows()
count=len(rects)
 