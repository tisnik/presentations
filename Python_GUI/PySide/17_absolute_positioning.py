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

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore
from PySide import QtGui


# nový widget bude odvozen od obecného widgetu
class MainWindow(QtGui.QWidget):
    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindow, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        self.resize(320, 240)
        self.setWindowTitle("Quit Button")

        # tlačítka
        button1 = QtGui.QPushButton("One", self)
        button2 = QtGui.QPushButton("Two", self)
        button3 = QtGui.QPushButton("Three", self)
        button4 = QtGui.QPushButton("Four", self)
        button5 = QtGui.QPushButton("Five", self)

        # přesun tlačítek na absolutní pozice
        button2.move(30, 30)
        button3.move(60, 60)
        button4.move(90, 90)
        button5.move(120, 120)

        # navázání akce na signál
        button1.clicked.connect(self.quit)
        button2.clicked.connect(self.quit)
        button3.clicked.connect(self.quit)
        button4.clicked.connect(self.quit)
        button5.clicked.connect(self.quit)

    def run(self, app):
        # zobrazení okna na obrazovce
        self.show()
        # vstup do smyčky událostí (event loop)
        app.exec_()

    def quit(self):
        print("Closing...")
        self.close()


def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow().run(app)


if __name__ == "__main__":
    main()
