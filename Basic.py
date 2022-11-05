import cv2 
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    _, frame = cap.read()
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame)

    cv2.imshow("Hologramic Economic Paradigm",frame)
    cv2.waitKey(1)