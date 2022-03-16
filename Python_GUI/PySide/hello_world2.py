import sys

from PySide.QtCore import *
from PySide.QtGui import *

qt_application = QApplication(sys.argv)


class HelloWorldLabel(QLabel):
    def __init__(self):
        QLabel.__init__(self, "Hello world!")

        self.setMinimumSize(QSize(600, 400))
        self.setAlignment(Qt.AlignCenter)
        self.setWindowTitle("Hello world!")

    def run(self):
        self.show()
        qt_application.exec_()


HelloWorldLabel().run()
