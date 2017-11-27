#!/usr/bin/env python
# vim: set fileencoding=utf-8

import sys

# prozatím budeme využívat jen modul QtGui
from PySide.QtGui import *

# konstrukce výchozího tzv. aplikačního objektu
app = QApplication(sys.argv)


# nový widget bude odvozen od standardního návěští
class HelloWorldLabel(QLabel):

    def __init__(self):
        # zavoláme konstruktor předka (nedoporučovaná varianta)
        QLabel.__init__(self, "Hello world!")

    def run(self):
        # zobrazení okna na obrazovce
        self.show()
        # vstup do smyčky událostí (event loop)
        sys.exit(app.exec_())


HelloWorldLabel().run()
