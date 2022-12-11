import cv2 
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import pyautogui

folderpath = "C:/Users/LENOVO/Desktop/vsp-computer-vision/vsp-computer-vison/powerpoint/Presentation"
pathimages = os.listdir(folderpath)
#print(pathimages)

width, height = 1280,720
imgNumber = 0
hs,ws = int(120),int(213)
gestureThreshold = 300
buttonPressed = False
buttonCounter = 0
buttonDelay = 30

# handdetector
detector = HandDetector(detectionCon=0.8,maxHands=1)

cap = cv2.VideoCapture(0)
while True:
    # import images
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    pathFullImage = os.path.join(folderpath,pathimages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    hands,img = detector.findHands(frame)
    #cv2.line(img,(0,gestureThreshold),(width,gestureThreshold),(0,255,0),10)

    # adding webcam image on the slides
    imgSmall = cv2.resize(frame,(ws,hs))
    h,w,_ = imgCurrent.shape 
    imgCurrent[0:hs,w-ws:w] = imgSmall

    if hands and buttonPressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx,cy = hand['center']
        lmList = hand['lmList']

        # constrain values for easier drawing
        xVal = int(np.interp(lmList[8][0],[width//2,w],[0,width]))
        yVal = int(np.interp(lmList[8][1],[150,height-150],[0,height]))
        indexFinger = xVal,yVal
        

        #if cy <= gestureThreshold:  # if hand is at the height of the face
            # gesture 1 - left
        if fingers == [0,1,1,0,0]:
            print('move right')
            pyautogui.press('right')
            #pyautogui.sleep(1)
        # gesture 3 - show pointer 
        #if fingers == [0,1,1,0,0]:
            #cv2.circle(imgCurrent,indexFinger,12,(0,0,255),cv2.FILLED)
            

    # button pressed iterations
    if buttonPressed:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPressed = False 


    cv2.imshow("Images",frame)
    cv2.imshow("Slides",imgCurrent)
    cv2.waitKey(1)