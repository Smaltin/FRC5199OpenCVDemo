import cv2 #OpenCV
import numpy as np
import os
import math
lower = np.array([50,150,80]) #Lower bound for the HSV Filter
upper = np.array([70,255,255]) #Upper bound for the HSV Filter
cap = cv2.VideoCapture(0) #Video capture device 0

if __name__ == '__main__':
    while(True):
        ret, frame = cap.read() #Read camera by frame
        cv2.imshow('Capture', frame) #Show HSV frame on computer
        if cv2.waitKey(1) & 0xFF == ord('q'): #If q is pressed
            break #Exit the loop

cap.release() #Turn off camera
cv2.destroyAllWindows() #Turn off OpenCV
