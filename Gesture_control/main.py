# main file to execute the gesture control application

import sys

from PyQt5.QtWidgets import QApplication
from Gesture_control.GUI.MainWindow import MainWindow


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()


