import cv2 #OpenCV
import numpy as np
import os
import math

if __name__ == '__main__':
    lower = np.array([50,150,80]) #Lower bound for the HSV Filter
    upper = np.array([90,255,255]) #Upper bound for the HSV Filter
    dir_path = os.path.dirname(os.path.realpath(__file__))
    while(True):
        hull = []
        img = cv2.imread(dir_path + "/Dark Images/BlueGoal-330in-ProtectedZone.jpg") #Reads the image provided
        cv2.imshow("Image", img) #Displays the image

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Converts to HSV
        boundmask = cv2.inRange(hsv, lower, upper) #Masks to bright green
        contours, hierarchy = cv2.findContours(boundmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #Determine contours
        traced = cv2.drawContours(img, contours, -1, (0,0,255), 1) #Draw the contours in BGR (0,0,255) (Red) with a thickness of 1

        for i in range(len(contours)): #For every contour:
            hull.append(cv2.convexHull(contours[i], False)) #Generate a convex hull
            cv2.drawContours(img, hull, i, (255, 0, 0),2) #Draw the convex hull in BGR (255,0,0) (Blue) with a thickness of 2

        for c in hull:
            M = cv2.moments(c)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
            cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
            cv2.putText(img, "Centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        cv2.imshow("Final", traced)
        cv2.imshow("Mask", boundmask)

        if cv2.waitKey(1) & 0xFF == ord('q'): #If q is pressed
            break #Exit the loop

    cv2.destroyAllWindows() #Turn off OpenCV
