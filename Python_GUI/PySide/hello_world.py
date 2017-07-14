import sys

from PySide.QtCore import *
from PySide.QtGui import *

qt_application = QApplication(sys.argv)

label = QLabel('Hello world!')

label.show()

qt_application.exec_()
