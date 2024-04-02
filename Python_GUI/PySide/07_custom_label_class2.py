#!/usr/bin/env python

#
#  (C) Copyright 2017, 2018  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

# tento import je zapotřebí kvůli nutnosti zpracování parametrů
# předávaných přes příkazový řádek
import sys

# prozatím budeme využívat jen modul QtGui
from PySide import QtGui


# nový widget bude odvozen od standardního návěští
class HelloWorldLabel(QtGui.QLabel):
    def __init__(self):
        # zavoláme konstruktor předka

        # varianta pro Python 2.x i pro Python 3.x
        super(HelloWorldLabel, self).__init__("Hello world!")

        # varianta pro Python 3.x
        # super().__init__("Hello world!")

    def run(self, app):
        # zobrazení okna na obrazovce
        self.show()
        # vstup do smyčky událostí (event loop)
        sys.exit(app.exec_())


def main():
    app = QtGui.QApplication(sys.argv)
    HelloWorldLabel().run(app)


if __name__ == "__main__":
    main()
