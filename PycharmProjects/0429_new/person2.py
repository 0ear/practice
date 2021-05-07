import face_recognition
from sklearn import svm
import os
encodings = []
names = []
train_dir = os.listdir('./lfw/')
print("train_dir:",train_dir)
for person in train_dir:
    pix = os.listdir("./lfw/" + person)
    for person_img in pix:
        face = face_recognition.load_image_file("./lfw/" + person + "/" + person_img)
        face_locations=face_recognition.face_locations(face)
        print(face_locations)
        if len(face_locations)==1:
                    face_enc = face_recognition.face_encodings(face)[0]
                    print("person：",person)
                    print("face_enc:",face_enc)
                    encodings.append(face_enc)
                    names.append(person)
        else:
            print(person+"can not used for tarining")
clf = svm.SVC(gamma='scale')
clf.fit(encodings, names)
test_image = face_recognition.load_image_file('Aaron_peirsol-2.jpg')
face_locations = face_recognition.face_locations(test_image)
no = len(face_locations)

print("Number of faces detected: ", no)
print("Found: \n")
for i in range(no):
    test_image_enc = face_recognition.face_encodings(test_image)[i]
    name = clf.predict([test_image_enc])
    print(*name)
