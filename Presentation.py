import cv2 
import mediapipe as mp
import pyautogui
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width,screen_height = pyautogui.size()
index_y = 0
i=1
detector = HandDetector(detectionCon=0.8,maxHands=1)
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    frame_height, frame_width , _ = frame.shape 
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks 
    hands,img = detector.findHands(frame)
    if hands:
        for hand in hands :
            fingers = detector.fingersUp(hand)
            print(fingers)
            drawing_utils.draw_landmarks(frame,hand)
            landmarks = hand.landmark 
            for id, landmark in enumerate(landmarks):
                x , y = int(landmark.x*frame_width) , int(landmark.y*frame_height) 
                if fingers == [0,1,0,0,0]:
                    cv2.circle(img=frame,center=(x,y),radius=20,color=(0,255,255))
                    print('left')
                    pyautogui.press('left')
                    #pyautogui.sleep(3)
                if fingers == [0,0,0,0,1]:
                    cv2.circle(img=frame,center=(x,y),radius=20,color=(0,255,255))
                    print("right")
                    #pyautogui.press('right')
                    #pyautogui.sleep(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.imshow("Hologram Economics",frame)
    #cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break