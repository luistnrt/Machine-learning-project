# Final script 
## Run this script to start the webcam and recognize faces that where created in the dataset of script 01.

import cv2
import numpy as np
import os 


def webcam_face_recognizer():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('Evaluation/Facial_Recognition_Vortrainiert/trainer/trainer.yml')
    cascadePath = "data/cascades/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 0

    names = ['None', 'Luis', 'Test1', 'Test2', 'Test3', 'Test4'] 

    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    while True:
        ret, img =cam.read()
        img = cv2.flip(img, 1) 
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            print(id)
            # If confidence is less them 100 ==> "0" : perfect match 
            if (confidence < 100):
                id = names[id]
                print(confidence)
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
            
            cv2.putText(
                        img, 
                        str(id), 
                        (x+5,y-5), 
                        font, 
                        1, 
                        (255,255,255), 
                        2
                    )
            cv2.putText(
                        img, 
                        str(confidence), 
                        (x+5,y+h-5), 
                        font, 
                        1, 
                        (255,255,0), 
                        1
                    )  
        
        cv2.imshow('camera',img) 
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting 
        if k == 27:
            break
    # Cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

webcam_face_recognizer()