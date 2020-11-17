import cv2 #OpenCV
import numpy as np
cap = cv2.VideoCapture(0) #Video capture device 0
lower = np.array([50,150,80]) #Lower bound for the HSV Filter
upper = np.array([70,255,255]) #Upper bound for the HSV Filter

while(True):
    ret, frame = cap.read() #Read camera by frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Converts to Grayscale
    cv2.imshow("Grayscale", gray)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    traced = cv2.drawContours(frame, contours, -1, (0,0,255), 3)
    cv2.imshow("Pipeline", traced)

    if cv2.waitKey(1) & 0xFF == ord('q'): #If q is pressed
        break #Exit the loop

cap.release() #Turn off camera
cv2.destroyAllWindows() #Turn off OpenCV
