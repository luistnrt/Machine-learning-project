# mirror of Gesture_control/main.py to keep folder structure of the project consistent


import sys

from PyQt5.QtWidgets import QApplication
from Gesture_control.GUI.MainWindow import MainWindow


def gesture_control_app():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

# if __name__ == "__main__":
#     gesture_control_app()