# Imports 
from PIL import Image
import numpy as np
import time
import cv2
import pickle
from keras.models import load_model

# Face Recognition Application
def face_recognition_app():
  
    # initialize global name var
    global name 

    # face detection
    face_cascade = cv2.CascadeClassifier('data/cascades/haarcascade_frontalface_default.xml')

    # resolution of the webcam
    screen_width = 1280       
    screen_height = 720

    # size of the image to predict
    image_width = 224
    image_height = 224

    # load the trained model
    model = load_model('transfer_learning_vggface_cnn_model')

    # the labels for the trained model
    with open("face-labels.pickle", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {key: value for key, value in og_labels.items()}
        print(f' labes: {labels}')

    # default webcam
    stream = cv2.VideoCapture(0)

    last_detection_time = time.time()
    person_identified = False
    identified_person = None

    # threshold for classifying unknown persons
    confidence_threshold = 68 # threshhold = confidence von 68, da dieser für unsere Klassifikation die beste Güte erzeugt hat
    print(f' threshhold: {confidence_threshold}')

    while True:
        # Capture frame-by-frame
        (grabbed, frame) = stream.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # try to detect faces in the webcam
        faces = face_cascade.detectMultiScale(rgb, scaleFactor=1.3, minNeighbors=5)

        # for each face found
        for (x, y, w, h) in faces:
            roi_rgb = rgb[y:y+h, x:x+w]

            # Draw a rectangle around the face
            color = (255, 0, 0)
            stroke = 2
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, stroke)

            # resize the image
            size = (image_width, image_height)
            resized_image = cv2.resize(roi_rgb, size)
            image_array = np.array(resized_image, "uint8")
            img = image_array.reshape(1, image_width, image_height, 3) 
            img = img.astype('float32')
            img /= 255

            # predict the image
            predicted_prob = model.predict(img)
            confidence = round(predicted_prob[0].max() * 100, 2)
        
            # Display the label
            font = cv2.FONT_HERSHEY_SIMPLEX
            if confidence >= confidence_threshold:
                name = labels[predicted_prob[0].argmax()]
            else:
                name = "unknown"
            
            color = (255, 0, 0)
            stroke = 2
            cv2.putText(frame, f'{name}', (x+5, y-5), font, 1, color,  stroke, cv2.LINE_AA)
            cv2.putText(frame, f'{confidence}', (x+5, y+h-5), font, 1, color, stroke, cv2.LINE_AA)

            if confidence >= confidence_threshold:
                if not person_identified:
                    # If a person is newly detected, update the timer and set the person_identified flag
                    last_detection_time = time.time()
                    person_identified = True
                    identified_person = name

                # Check if the person has been detected for 5 seconds
                if time.time() - last_detection_time >= 5:
                    if identified_person == 'luis':
                        # Display "Access Granted" when the person is identified as 'joshua'
                        cv2.putText(frame, "Access Granted", (x - 20, y + h + 30), font, 1, (0, 255, 0), stroke, cv2.LINE_AA)
                        '''
                        Could input a break statement here in order to break the application once the person is identified. Afterwards our motion controll
                        application could be startet as well. 
                        For preview purposes we decided that we will keep a manual break statement for our project.

                        '''
                        last_identified_person = identified_person
                    else:
                        # Display "Access Not Granted" for other identified persons and 'unknown'
                        cv2.putText(frame, "Access Not Granted", (x - 20, y + h + 30), font, 1, (0, 0, 255), stroke, cv2.LINE_AA)            
            
            else:
                # Reset the person_identified flag when no person is detected
                person_identified = False
                identified_person = None

                
        # Show the frame
        cv2.imshow("Image", frame)
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting 
        if k == 27:
            break
        
    # Cleanup
    stream.release()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    
    print(identified_person)
    return identified_person


# if __name__ == "__main__":
    
#     face_recognition_app()    


