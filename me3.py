import face_recognition
import cv2
import numpy as np
from datetime import datetime
video_capture = cv2.VideoCapture(0)

img0 = face_recognition.load_image_file("images/adith.jpg")
img0 = face_recognition.face_encodings(img0)[0]

img1 = face_recognition.load_image_file("images/akhilendran.jpg")
img1 = face_recognition.face_encodings(img1)[0]

img2 = face_recognition.load_image_file("images/althafoj.jpg")
img2 = face_recognition.face_encodings(img2)[0]

img3 = face_recognition.load_image_file("images/aravindmanoj.jpg")
img3 = face_recognition.face_encodings(img3)[0]

img4 = face_recognition.load_image_file("images/arjun.jpg")
img4 = face_recognition.face_encodings(img4)[0]

img5 = face_recognition.load_image_file("images/Grigor.jpg")
img5 = face_recognition.face_encodings(img5)[0]

img6 = face_recognition.load_image_file("images/Hari.jpg")
img6 = face_recognition.face_encodings(img6)[0]

img7 = face_recognition.load_image_file("images/Mechqueen.jpg")
img7 = face_recognition.face_encodings(img7)[0]

img8 = face_recognition.load_image_file("images/antony.jpg")
img8 = face_recognition.face_encodings(img8)[0]

known_face_encodings = [
    img0,
    img1,
    img2,
    img3,
    img4,
    img5,
    img6,
    img7,
    img8,
]
known_face_names = [
    "Adith Ashokan",
    "Akhilendran P",
    "Althaf OJ",
    "Aravind Manoj",
    "Arjun Jayakumar",
    "Grigor Sabu",
    "Hari",
    "Mech Queen",
    "Vadakkan"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

def markAttendance(name):
        with open('attendance.csv','r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')


while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            print(best_match_index)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                markAttendance(name)

            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()