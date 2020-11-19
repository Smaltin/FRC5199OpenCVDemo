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
    ret, thresh = cv2.threshold(blur, 127, 255, 0)
    contours, hierarchy = cv2.findContours(blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    traced = cv2.drawContours(frame, contours, -1, (0,0,255), 3)
    cv2.imshow("Pipeline", traced)
    cv2.imshow("Blur", blur)

    if cv2.waitKey(1) & 0xFF == ord('q'): #If q is pressed
        break #Exit the loop

cap.release() #Turn off camera
cv2.destroyAllWindows() #Turn off OpenCV
