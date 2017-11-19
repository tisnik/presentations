#!/usr/bin/env python

import sys

from PySide.QtGui import *


app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle('Hello world!')
window.resize(320, 240)
window.show()

app.exec_()
