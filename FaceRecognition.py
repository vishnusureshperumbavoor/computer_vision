import face_recognition
import cv2
import numpy as np
from datetime import datetime
video_capture = cv2.VideoCapture(0)

elon_image = face_recognition.load_image_file("images/Elon.jpg")
elon_face_encoding = face_recognition.face_encodings(elon_image)[0]

latheef_image = face_recognition.load_image_file("images/Latheef.jpg")
latheef_face_encoding = face_recognition.face_encodings(latheef_image)[0]

abhai_image = face_recognition.load_image_file("images/Abhai.jpg")
abhai_face_encoding = face_recognition.face_encodings(abhai_image)[0]

abhijith_image = face_recognition.load_image_file("images/Abhijith.jpg")
abhijith_face_encoding = face_recognition.face_encodings(abhijith_image)[0]

abhinav_image = face_recognition.load_image_file("images/Abhinav.jpg")
abhinav_face_encoding = face_recognition.face_encodings(abhinav_image)[0]

abhishek_image = face_recognition.load_image_file("images/Abhishek.jpg")
abhishek_face_encoding = face_recognition.face_encodings(abhishek_image)[0]

afil_image = face_recognition.load_image_file("images/Afil.jpg")
afil_face_encoding = face_recognition.face_encodings(afil_image)[0]

#ajayjose_image = face_recognition.load_image_file("images/Ajayjose.jpg")
#ajayjose_face_encoding = face_recognition.face_encodings(ajayjose_image)[0]

#ajayna_image = face_recognition.load_image_file("images/Ajayna.jpg")
#ajayna_face_encoding = face_recognition.face_encodings(ajayna_image)[0]

#ajith_image = face_recognition.load_image_file("images/Ajith.jpg")
#ajith_face_encoding = face_recognition.face_encodings(ajith_image)[0]

#martin_image = face_recognition.load_image_file("images/Martin.jpg")
#martin_face_encoding = face_recognition.face_encodings(martin_image)[0]

akshaykumar_image = face_recognition.load_image_file("images/Akshaykumar.jpg")
akshaykumar_face_encoding = face_recognition.face_encodings(akshaykumar_image)[0]

alshitha_image = face_recognition.load_image_file("images/Alshitha.jpg")
alshitha_face_encoding = face_recognition.face_encodings(alshitha_image)[0]

althaf_image = face_recognition.load_image_file("images/Althaf.jpg")
althaf_face_encoding = face_recognition.face_encodings(althaf_image)[0]

#sigma_image = face_recognition.load_image_file("images/Sigma.jpg")
#sigma_face_encoding = face_recognition.face_encodings(sigma_image)[0]

dinesh_image = face_recognition.load_image_file("images/Dinesh.jpg")
dinesh_face_encoding = face_recognition.face_encodings(dinesh_image)[0]

snair_image = face_recognition.load_image_file("images/Snair.jpg")
snair_face_encoding = face_recognition.face_encodings(snair_image)[0]

sajan_image = face_recognition.load_image_file("images/Sajan.jpg")
sajan_face_encoding = face_recognition.face_encodings(sajan_image)[0]

anju_image = face_recognition.load_image_file("images/Anju.jpg")
anju_face_encoding = face_recognition.face_encodings(anju_image)[0]

aravind_image = face_recognition.load_image_file("images/Aravind.jpg")
aravind_face_encoding = face_recognition.face_encodings(aravind_image)[0]

ashwell_image = face_recognition.load_image_file("images/Ashwell.jpg")
ashwell_face_encoding = face_recognition.face_encodings(ashwell_image)[0]

apk_image = face_recognition.load_image_file("images/Apk.jpg")
apk_face_encoding = face_recognition.face_encodings(apk_image)[0]

athul_image = face_recognition.load_image_file("images/Athul.jpg")
athul_face_encoding = face_recognition.face_encodings(athul_image)[0]

basil_image = face_recognition.load_image_file("images/Basil.jpg")
basil_face_encoding = face_recognition.face_encodings(basil_image)[0]

bazith_image = face_recognition.load_image_file("images/Bazith.jpg")
bazith_face_encoding = face_recognition.face_encodings(bazith_image)[0]

bhavana_image = face_recognition.load_image_file("images/Bhavana.jpg")
bhavana_face_encoding = face_recognition.face_encodings(bhavana_image)[0]

binil_image = face_recognition.load_image_file("images/Binil.jpg")
binil_face_encoding = face_recognition.face_encodings(binil_image)[0]

devika_image = face_recognition.load_image_file("images/Devika.jpg")
devika_face_encoding = face_recognition.face_encodings(devika_image)[0]

aboo_image = face_recognition.load_image_file("images/Aboobakkar.jpg")
aboo_face_encoding = face_recognition.face_encodings(aboo_image)[0]

sulu_image = face_recognition.load_image_file("images/Sulaiman.jpg")
sulu_face_encoding = face_recognition.face_encodings(sulu_image)[0]

gokul_image = face_recognition.load_image_file("images/Gokul.jpg")
gokul_face_encoding = face_recognition.face_encodings(gokul_image)[0]

jerrin_image = face_recognition.load_image_file("images/Jerrin.jpg")
jerrin_face_encoding = face_recognition.face_encodings(jerrin_image)[0]

kvenu_image = face_recognition.load_image_file("images/Venugopal.jpg")
kvenu_face_encoding = face_recognition.face_encodings(kvenu_image)[0]

skumar_image = face_recognition.load_image_file("images/Skumar.jpg")
skumar_face_encoding = face_recognition.face_encodings(skumar_image)[0]

#manu_image = face_recognition.load_image_file("images/Manu.jpg")
#manu_face_encoding = face_recognition.face_encodings(manu_image)[0]

masoom_image = face_recognition.load_image_file("images/Masoom.jpg")
masoom_face_encoding = face_recognition.face_encodings(masoom_image)[0]

lahan_image = face_recognition.load_image_file("images/Lahan.jpg")
lahan_face_encoding = face_recognition.face_encodings(lahan_image)[0]

minhaj_image = face_recognition.load_image_file("images/Minhaj.jpg")
minhaj_face_encoding = face_recognition.face_encodings(minhaj_image)[0]

sadikh_image = face_recognition.load_image_file("images/Sadikh.jpg")
sadikh_face_encoding = face_recognition.face_encodings(sadikh_image)[0]

muhassin_image = face_recognition.load_image_file("images/Muhassin.jpg")
muhassin_face_encoding = face_recognition.face_encodings(muhassin_image)[0]

adhil_image = face_recognition.load_image_file("images/Adhil.jpg")
adhil_face_encoding = face_recognition.face_encodings(adhil_image)[0]

aslamka_image = face_recognition.load_image_file("images/Aslamka.jpg")
aslamka_face_encoding = face_recognition.face_encodings(aslamka_image)[0]

fayiz_image = face_recognition.load_image_file("images/Fayiz.jpg")
fayiz_face_encoding = face_recognition.face_encodings(fayiz_image)[0]

suhail_image = face_recognition.load_image_file("images/Suhail.jpg")
suhail_face_encoding = face_recognition.face_encodings(suhail_image)[0]

#nandhakumar_image = face_recognition.load_image_file("images/Nandhakumar.jpg")
#nandhakumar_face_encoding = face_recognition.face_encodings(nandhakumar_image)[0]

nelvin_image = face_recognition.load_image_file("images/Nelvin.jpg")
nelvin_face_encoding = face_recognition.face_encodings(nelvin_image)[0]

reshma_image = face_recognition.load_image_file("images/Reshma.jpg")
reshma_face_encoding = face_recognition.face_encodings(reshma_image)[0]

sahil_image = face_recognition.load_image_file("images/Sahil.jpg")
sahil_face_encoding = face_recognition.face_encodings(sahil_image)[0]

#stj_image = face_recognition.load_image_file("images/Stj.jpg")
#stj_face_encoding = face_recognition.face_encodings(stj_image)[0]

shahul_image = face_recognition.load_image_file("images/Shahul.jpg")
shahul_face_encoding = face_recognition.face_encodings(shahul_image)[0]

sreekumar_image = face_recognition.load_image_file("images/Sreekumar.jpg")
sreekumar_face_encoding = face_recognition.face_encodings(sreekumar_image)[0]

#sreeraj_image = face_recognition.load_image_file("images/Sreeraj.jpg")
#sreeraj_face_encoding = face_recognition.face_encodings(sreeraj_image)[0]

#vinu_image = face_recognition.load_image_file("images/Vinu.jpg")
#vinu_face_encoding = face_recognition.face_encodings(vinu_image)[0]

#vipin_image = face_recognition.load_image_file("images/Vipin.jpg")
#vipin_face_encoding = face_recognition.face_encodings(vipin_image)[0]

vkb_image = face_recognition.load_image_file("images/Vkb.jpg")
vkb_face_encoding = face_recognition.face_encodings(vkb_image)[0]

vsp_image = face_recognition.load_image_file("images/VSP.jpg")
vsp_face_encoding = face_recognition.face_encodings(vsp_image)[0]

mani_image = face_recognition.load_image_file("images/Mani.jpg")
mani_face_encoding = face_recognition.face_encodings(mani_image)[0]

fazeen_image = face_recognition.load_image_file("images/Fazeen.jpg")
fazeen_face_encoding = face_recognition.face_encodings(fazeen_image)[0]

abin_image = face_recognition.load_image_file("images/Abin.jpg")
abin_face_encoding = face_recognition.face_encodings(abin_image)[0]

sahad_image = face_recognition.load_image_file("images/Sahad.jpg")
sahad_face_encoding = face_recognition.face_encodings(sahad_image)[0]

akshaynath_image = face_recognition.load_image_file("images/Akshaynath.jpg")
akshaynath_face_encoding = face_recognition.face_encodings(akshaynath_image)[0]

aleena_image = face_recognition.load_image_file("images/Aleena.jpg")
aleena_face_encoding = face_recognition.face_encodings(aleena_image)[0]

suneer_image = face_recognition.load_image_file("images/Suneer.jpg")
suneer_face_encoding = face_recognition.face_encodings(suneer_image)[0]

#athulkrishna_image = face_recognition.load_image_file("images/Athulkrishna.jpg")
#athulkrishna_face_encoding = face_recognition.face_encodings(athulkrishna_image)[0]

#krishna_image = face_recognition.load_image_file("images/Krishna.jpg")
#krishna_face_encoding = face_recognition.face_encodings(krishna_image)[0]

mowfaq_image = face_recognition.load_image_file("images/Mowfaq.jpg")
mowfaq_face_encoding = face_recognition.face_encodings(mowfaq_image)[0]

#saneesh_image = face_recognition.load_image_file("images/Saneesh.jpg")
#saneesh_face_encoding = face_recognition.face_encodings(saneesh_image)[0]

shehin_image = face_recognition.load_image_file("images/Shehin.jpg")
shehin_face_encoding = face_recognition.face_encodings(shehin_image)[0]

vinayak_image = face_recognition.load_image_file("images/Vinayak.jpg")
vinayak_face_encoding = face_recognition.face_encodings(vinayak_image)[0]

vyshak_image = face_recognition.load_image_file("images/Vyshak.jpg")
vyshak_face_encoding = face_recognition.face_encodings(vyshak_image)[0]

biju_image = face_recognition.load_image_file("images/Biju.jpeg")
biju_face_encoding = face_recognition.face_encodings(biju_image)[0]

known_face_encodings = [
    elon_face_encoding,
    latheef_face_encoding,
    abhai_face_encoding,
    abhijith_face_encoding,
    abhinav_face_encoding,
    abhishek_face_encoding,
    afil_face_encoding,
    #ajayjose_face_encoding,
    #ajayna_face_encoding,
    #ajithmvijayan_face_encoding,
    #akshaymartin_face_encoding,
    akshaykumar_face_encoding,
    alshitha_face_encoding,
    althaf_face_encoding,
    #amal_face_encoding,
    dinesh_face_encoding,
    snair_face_encoding,
    sajan_face_encoding,
    anju_face_encoding,
    aravind_face_encoding,
    ashwell_face_encoding,
    apk_face_encoding,
    athul_face_encoding,
    basil_face_encoding,
    bazith_face_encoding,
    bhavana_face_encoding,
    binil_face_encoding,
    devika_face_encoding,
    aboo_face_encoding,
    sulu_face_encoding,
    gokul_face_encoding,
    jerrin_face_encoding,
    kvenu_face_encoding,
    skumar_face_encoding,
    #manu_face_encoding,
    masoom_face_encoding,
    lahan_face_encoding,
    minhaj_face_encoding,
    sadikh_face_encoding,
    muhassin_face_encoding,
    adhil_face_encoding,
    aslamka_face_encoding,
    fayiz_face_encoding,
    suhail_face_encoding,
    #nandakumar_face_encoding,
    nelvin_face_encoding,
    reshma_face_encoding,
    sahil_face_encoding,
    #stj_face_encoding,
    shahul_face_encoding,
    sreekumar_face_encoding,
    #sreeraj_face_encoding,
    #vinu_face_encoding,
    #vipin_face_encoding,
    vkb_face_encoding,
    vsp_face_encoding,
    mani_face_encoding,
    fazeen_face_encoding,
    abin_face_encoding,
    sahad_face_encoding,
    akshaynath_face_encoding,
    aleena_face_encoding,
    suneer_face_encoding,
    #athulkrishna_face_encoding,
    #krishna_face_encoding,
    mowfaq_face_encoding,
    #saneesh_face_encoding,
    shehin_face_encoding,
    vinayak_face_encoding,
    vyshak_face_encoding,
    biju_face_encoding,
]
known_face_names = [
    "Elon",
    "Abdul Latheef",
    "Abhai Sajeevan",
    "Abhijith Saju",
    "Abhinav K",
    "Abhishek US",
    "Afil KA",
    #"Ajay Jose",
    #"Ajay NA",
    #"Ajith M Vijayan",
    #"Akshay Martin",
    "Akshaykumar PA",
    "Alshitha UM",
    "Althaf PS",
    #"Amal Francis",
    "Anandhu Dinesh",
    "Anandhu S Nair",
    "Anandhu Sajan",
    "Anju Babu",
    "Aravind Aji",
    "Ashwell Babu",
    "APK Nedumbassery",
    "Athul Vinod",
    "Basil Roy",
    "Bazith Mehrab",
    "Bhavana Joshy",
    "Binil Binoy",
    "Devika Shibu",
    "Fathima Aboobakkar",
    "Fathima Sulaiman",
    "Gokulkrishna KU",
    "Jerrin Kochuvarkey",
    "Madhav K Venugopal",
    "Madhav S Kumar",
    #"Manu Mohan",
    "Masoom Raza",
    "Lahan PS",
    "Minhaj CS",
    "Sadikh KR",
    "Muhassin",
    "Adhil NA",
    "Aslam KA",
    "Fraternity Uyir",
    "Suhail RH",
    #"Nandhakumar PK",
    "Nelvin Francis",
    "Reshma Babu India",
    "Sahil Khan",
    #"Sajin TJ",
    "Shahul Shibu",
    "Sreekumar P",
    #"Sreeraj TS",
    #"Vinu Jayakumar",
    #"Vipin Prasad",
    "Vishnu KB",
    "VSP",
    "Anandhu Mani",
    "Fazeen Aboo",
    "Abin Alias",
    "Sahad Ibrahim",
    "Akshaynath MR",
    "Aleena Babu",
    "Aslam Suneer",
    #"Athulkrishna VD",
    #"Krishna Remesh P",
    "Mowfaq Rahman",
    #"Saneesh Sahadevan",
    "Shehin T Shaji",
    "Vinayak Prakash",
    "Vyshak Anand",
    "Biju Peter Sir",
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