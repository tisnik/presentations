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
        testLabel1 = QtGui.QLabel("Normal/Default")
        testLabel2 = QtGui.QLabel("Box")
        testLabel3 = QtGui.QLabel("Panel")
        testLabel4 = QtGui.QLabel("WinPanel")
        testLabel5 = QtGui.QLabel("HLine")
        testLabel6 = QtGui.QLabel("VLine")
        testLabel7 = QtGui.QLabel("StyledPanel")

        testLabel2.setFrameStyle(QtGui.QFrame.Box)
        testLabel3.setFrameStyle(QtGui.QFrame.Panel)
        testLabel4.setFrameStyle(QtGui.QFrame.WinPanel)
        testLabel5.setFrameStyle(QtGui.QFrame.HLine)
        testLabel6.setFrameStyle(QtGui.QFrame.VLine)
        testLabel7.setFrameStyle(QtGui.QFrame.StyledPanel)

        # horizontální oddělovač
        horizontalLine = QtGui.QLabel()
        horizontalLine.setFrameStyle(QtGui.QFrame.HLine)

        # tlačítko pro ukončení aplikace
        quitButton = QtGui.QPushButton("Quit")

        # vytvoření správce geometrie
        layout = QtGui.QVBoxLayout()

        # umístění widgetů do okna
        layout.addWidget(testLabel1)
        layout.addWidget(testLabel2)
        layout.addWidget(testLabel3)
        layout.addWidget(testLabel4)
        layout.addWidget(testLabel5)
        layout.addWidget(testLabel6)
        layout.addWidget(testLabel7)

        layout.addWidget(horizontalLine)

        layout.addWidget(quitButton)

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
