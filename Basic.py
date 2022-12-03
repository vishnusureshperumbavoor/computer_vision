import cv2 

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()

    cv2.imshow("Webcam basics",frame)
    cv2.waitKey(1)