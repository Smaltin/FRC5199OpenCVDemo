import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read() #Read camera by frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Convert camera to grayscale
    cv2.imshow('frame',gray) #Show grayscale frame on computer
    if cv2.waitKey(1) & 0xFF == ord('q'): #If q is pressed
        break #Exit the loop

cap.release() #Turn off camera
cv2.destroyAllWindows() #Turn off OpenCV
