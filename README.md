# Machine-learning-project
Machine learning project repository (Portfolioabgabe: Joshua Brenzinger, Pascal Breucker, Constantin Rech und Luis Steinert)

Combination of facial recognition as a tool for authentification and mediapipe gesture detection to control a spotify music player

--- 
## Folderstructure:

Face_recognition/
  - `data/cascades`: contains the haarcascade_frontal_face_default classifier used for face detection
  - `transfer_learning_vggface_cnn_model`: contains the save trained cnn model which is used for the classification of our faces
  - `face-labels.pickle`: contains the labels (classes)
  - `face_recognition_CNN_training.ipynb`: this jupyter notebook contains the code which was used to train and evaluate the face recognition model
  - `Evaluation und Tests/` -> Documentation of implementation which were not used in the final product 
      - `Facial_Recognition_Vortrainiert`: previous tries to create a face recognizer using LBPHFaceRecognizer class of OpenCV. Was dismissed due to bad evaluation
      - `Other Files`: e.g. above. other implementation of face recognizers which we dismissed due to their performance

Gesture_control/

  - `models/`: contains the trained model and .py file for the dataset creation and landmark connection
  - `pyui/ui/`: contains the ui files for the gesture control application
  - `pyui/`: compiled ui documents as python files
  - `constants.py`: contains the constants for the training of LSTM
  - `GestureRecognitionThread.py`: contains the code for the gesture recognition thread, including preprocessing steps and mediapipe library for landmarks
  - `Spotify.py`: contains the code for the spotify api



## Files:

1. `face_recognition_application.py`: 
   - This python script contains the code for the created application. 
2. `gesture_control_application.py`:
   - ** HOSHUA ** HAHAOK
3. `main_application.py`:
   - This python script contains the code of the combination of face recog and gesture control
   - It runs the face recognition app and evaluates the output in order to start the gesture control app


## Bibliography and Sources

1. Brownlee, J. (2020). How to perform face recognition with VGGFACE2 in Keras. MachineLearningMastery.com. https://machinelearningmastery.com/how-to-perform-face-recognition-with-vggface2-convolutional-neural-network-in-keras/
2. CODE Magazine, EPS Software Corp., Wei-Meng Lee. (o. D.). Implementing face recognition using deep learning and support vector machines. https://www.codemag.com/Article/2205081/Implementing-Face-Recognition-Using-Deep-Learning-and-Support-Vector-Machines
3. Singh, A. (2021, 13. Dezember). How to implement Face recognition using VGG Face in Python 3.7 and Tensorflow 2.0. Medium. https://medium.com/analytics-vidhya/how-to-implement-face-recognition-using-vgg-face-in-python-3-8-and-tensorflow-2-0-a0593f8c95c3
4. https://github.com/kzaleskaa/spotify-gesture-controller as basis for motion control
5. https://mudgalvaibhav.medium.com/real-time-gesture-recognition-using-googles-mediapipe-hands-add-your-own-gestures-tutorial-1-dd7f14169c19
6. https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer
7. https://developer.spotify.com/documentation/web-api spotify documentation
8. https://www.riverbankcomputing.com/software/pyqt/ pyqt documentation for frontend changes

### if you want to run this project do those steps:

#### venv setup
1. create virtual environment
2. install requirements.txt
   
### get spotify api data (spotify premium account needed)

3. login at https://developer.spotify.com/
4. create app and set url: http://localhost:8888/spotify-api/callback/
5. create .env in root 
6. set `CLIENT_ID=<client_id>` 
   `CLIENT_SECRET=<client_secret>`

### start application
7. run `python main_application.py`

