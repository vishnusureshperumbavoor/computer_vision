import cv2 
import HandTrackingModule as htm
import numpy as np 

cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.85)
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if lmList != None:
        # tip of index finger 
        x1,y1 = lmList[8][1:]
        # tip of middle finger 
        x2,y2 = lmList[12][1:]
        fingers = detector.fingersUp()
        print(fingers)

    cv2.imshow("Image",img)
    cv2.waitKey(1)