import cv2 
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
detector = htm.handDetector()
tipIds = [4,8,12,16,20]
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if lmList != None :
        # number of fingers
        fingers = detector.fingersUp()
        print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)
        cv2.putText(img,str(totalFingers),(45,375),cv2.FONT_HERSHEY_COMPLEX_SMALL,8,(127,255,0),12)

    cv2.imshow("Image",img)
    cv2.waitKey(1)