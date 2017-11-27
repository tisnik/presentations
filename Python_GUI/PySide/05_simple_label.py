#!/usr/bin/env python

import sys

from PySide.QtGui import *


app = QApplication(sys.argv)

label = QLabel('Hello world!')

label.show()

app.exec_()
