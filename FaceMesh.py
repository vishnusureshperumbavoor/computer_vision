import cv2 
import HandTrackingModule as htm
import mediapipe as mp 

cap = cv2.VideoCapture(0)
detector = htm.handDetector()
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

while True:
    success, img = cap.read()
    results = faceMesh.process(img)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img,faceLms,mpFaceMesh.FACEMESH_CONTOURS,drawSpec,drawSpec)
            for id,lm in enumerate(faceLms.landmark):
                #print(lm)
                ih, iw, ic = img.shape 
                x,y = int(lm.x*iw),int(lm.y*ih) 
                print(id,x,y)

    
    cv2.imshow("Image",img)
    cv2.waitKey(1)