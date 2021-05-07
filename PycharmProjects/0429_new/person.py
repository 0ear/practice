from imutils.face_utils import FaceAligner
from imutils.video import count_frames
import imutils
import numpy as np
import dlib
import cv2

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
fa = FaceAligner(predictor, desiredFaceWidth=64)

face_filename = 1


def detect(img, idx, totle):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 1)

    for face in faces:
        faceAligned = fa.align(gray, gray, face)
        global face_filename
        cv2.imwrite('./face/{0}.png'.format(face_filename), faceAligned)
        face_filename += 1
    print('Working with {0} frame. completed {1:.2f} %'.format(idx, idx / float(totle) * 100))


detect_video = '0612.mp4'
videoCapture = cv2.VideoCapture(detect_video)
success, frame = videoCapture.read()
frame_counter = 1
frame_totle = count_frames(detect_video)
while success:
    detect(frame, frame_counter, frame_totle)
    success, frame = videoCapture.read()
    frame_counter += 1

print("Done!!")