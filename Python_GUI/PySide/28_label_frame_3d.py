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
        # velikost není potřeba specifikovat
        # self.resize(320, 240)
        self.setWindowTitle("QLabel widget")

        # textová návěští
        testLabel11 = QtGui.QLabel("Plain Box")
        testLabel21 = QtGui.QLabel("Plain Panel")
        testLabel31 = QtGui.QLabel("Plain WinPanel")

        testLabel12 = QtGui.QLabel("Raised Box")
        testLabel22 = QtGui.QLabel("Raised Panel")
        testLabel32 = QtGui.QLabel("Raised WinPanel")

        testLabel13 = QtGui.QLabel("Sunken Box")
        testLabel23 = QtGui.QLabel("Sunken Panel")
        testLabel33 = QtGui.QLabel("Sunken WinPanel")

        testLabel11.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        testLabel21.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Plain)
        testLabel31.setFrameStyle(QtGui.QFrame.WinPanel | QtGui.QFrame.Plain)

        testLabel12.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Raised)
        testLabel22.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        testLabel32.setFrameStyle(QtGui.QFrame.WinPanel | QtGui.QFrame.Raised)

        testLabel13.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Sunken)
        testLabel23.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Sunken)
        testLabel33.setFrameStyle(QtGui.QFrame.WinPanel | QtGui.QFrame.Sunken)

        # horizontální oddělovač
        horizontalLine = QtGui.QLabel()
        horizontalLine.setFrameStyle(QtGui.QFrame.HLine)

        # tlačítko pro ukončení aplikace
        quitButton = QtGui.QPushButton("Quit")

        # vytvoření správce geometrie
        layout = QtGui.QGridLayout()

        # umístění widgetů do okna
        layout.addWidget(testLabel11, 1, 1)
        layout.addWidget(testLabel21, 2, 1)
        layout.addWidget(testLabel31, 3, 1)

        layout.addWidget(testLabel12, 1, 2)
        layout.addWidget(testLabel22, 2, 2)
        layout.addWidget(testLabel32, 3, 2)

        layout.addWidget(testLabel13, 1, 3)
        layout.addWidget(testLabel23, 2, 3)
        layout.addWidget(testLabel33, 3, 3)

        layout.addWidget(horizontalLine, 4, 2)

        layout.addWidget(quitButton, 5, 2)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(layout)

        # navázání akce na stisk tlačítka pro ukončení aplikace
        quitButton.clicked.connect(self.quit)

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
