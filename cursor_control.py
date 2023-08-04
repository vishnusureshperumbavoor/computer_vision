import cv2 
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
width = 1280  # Set the desired width
height = 720  # Set the desired height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width,screen_height = pyautogui.size()
index_y = 0

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    frame_height, frame_width , _ = frame.shape 
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks 
    if hands:
        for hand in hands :
            drawing_utils.draw_landmarks(frame,hand)
            landmarks = hand.landmark 
            for id, landmark in enumerate(landmarks):
                x , y = int(landmark.x*frame_width) , int(landmark.y*frame_height) 
                #print(id)
                #print(x,y)
                if id == 8:
                    cv2.circle(img=frame,center=(x,y),radius=20,color=(0,255,255))
                    index_x = screen_width/frame_width*x 
                    index_y = screen_height/frame_height*y 
                    pyautogui.moveTo(index_x,index_y)
                if id == 12:
                    cv2.circle(img=frame,center=(x,y),radius=20,color=(0,255,255))
                    thumb_x = screen_width/frame_width*x 
                    thumb_y = screen_height/frame_height*y 
                    #print(abs(thumb_y-index_y))
                    if abs(thumb_y - index_y < 50):
                        # print("click")
                        pyautogui.click()
                        #pyautogui.press('right')
                        pyautogui.sleep(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.imshow("Hologram Economics",frame)
    #cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break