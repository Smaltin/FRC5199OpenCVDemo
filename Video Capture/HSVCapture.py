import cv2 #OpenCV
import numpy as np
cap = cv2.VideoCapture(0) #Video capture device 0
lower = np.array([50,150,80]) #Lower bound for the HSV Filter
upper = np.array([70,255,255]) #Upper bound for the HSV Filter

while(True):
    ret, frame = cap.read() #Read camera by frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Converts to HSV
    boundmask = cv2.inRange(hsv, lower, upper) #Masks the HSV values to the set range
    blur = cv2.GaussianBlur(boundmask,(9,9),0) #Applies a Gaussian Blur with a width/height of 9
    cv2.imshow('HSV', hsv) #Show HSV frame on computer
    cv2.imshow('Masked',boundmask) #Show HSV-Masked frame on computer
    cv2.imshow('Gaussian Blur',blur) #Show HSV-Masked and Gaussian Blurred frame on computer

    if cv2.waitKey(1) & 0xFF == ord('q'): #If q is pressed
        break #Exit the loop

cap.release() #Turn off camera
cv2.destroyAllWindows() #Turn off OpenCV
