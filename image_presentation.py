import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np

folderpath = "bolt_mocobot"
pathimages = os.listdir(folderpath)

width, height = 1280, 650
imgNumber = 0
hs, ws = int(120), int(180)
gestureThreshold = 300
buttonPressed = False
buttonCounter = 0
buttonDelay = 30

# handdetector
detector = HandDetector(detectionCon=0.8, maxHands=1)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cv2.namedWindow("Presentation", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Presentation", width, height)

while True:
    # import images
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    pathFullImage = os.path.join(folderpath, pathimages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    hands, img = detector.findHands(frame)
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 10)

    # adding webcam image on the slides
    imgSmall = cv2.resize(frame, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w - ws:w] = imgSmall

    if hands and buttonPressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand['center']
        lmList = hand['lmList']

        # constrain values for easier drawing
        xVal = int(np.interp(lmList[8][0], [width // 2, w], [0, width]))
        yVal = int(np.interp(lmList[8][1], [150, height - 150], [0, height]))
        indexFinger = xVal, yVal

        if cy <= gestureThreshold:  # if hand is at the height of the face
            # gesture 1 - left
            if fingers == [1, 0, 0, 0, 0]:
                print("left")
                buttonPressed = True
                if imgNumber > 0:
                    buttonPressed = True
                    imgNumber -= 1

            # gesture 2 - right
            if fingers == [0, 0, 0, 0, 1]:
                print("right")
                if imgNumber < len(pathimages) - 1:
                    buttonPressed = True
                    imgNumber += 1

        # gesture 3 - show pointer
        if fingers == [0, 1, 1, 0, 0]:
            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)

    # button pressed iterations
    if buttonPressed:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPressed = False

    cv2.imshow("Presentation", imgCurrent)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
