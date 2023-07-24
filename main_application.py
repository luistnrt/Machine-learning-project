from face_recognition_application import face_recognition_app
from gesture_control_application import gesture_control_app

if __name__ == '__main__':

    name = face_recognition_app()
    
    if name == 'joshua':
        gesture_control_app()

        
    
    

