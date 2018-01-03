#!/usr/bin/env python
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2017  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

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
