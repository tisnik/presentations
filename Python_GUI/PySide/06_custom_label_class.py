#!/usr/bin/env python

import sys

from PySide.QtGui import *


app = QApplication(sys.argv)


class HelloWorldLabel(QLabel):
    def __init__(self):
        QLabel.__init__(self, "Hello world!")

    def run(self):
        self.show()
        app.exec_()


HelloWorldLabel().run()
