import cv2
import numpy as np
import boto3
import time
from picamera2 import Picamera2


#initialize vvariables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
face_detected = False


#initialize camera
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={format: 'XRGB8888', "size" : (640,480)}))
picam2.start()

#initialize face recognition
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cv2.startWindowThread()


while True:
    #if process frame to save time
    if process_this_frame:
        face_detected = False
    # Capture frame-by-frame
        frame = picam2.capture_array()
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv2.imshow('frame',gray)
        #detect faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        #determine if face is detected
        if len(faces) > 0:
            face_detected = True

        else:
            face_detected = False

        if face_detected:
            for (x,y,w,h) in faces:
                cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = gray[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    process_this_frame = not process_this_frame
    # Display the resulting frame
    cv2.imshow('frame',gray)



# When everything done, release the capture
picam2.stop()
cv2.destroyAllWindows()







