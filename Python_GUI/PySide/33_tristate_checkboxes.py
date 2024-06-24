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
from PySide import QtCore, QtGui


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
        self.setWindowTitle("QCheckBox")

        # testovací zaškrtávací tlačítka
        self.testCheckBox1 = QtGui.QCheckBox("check box 1")
        self.testCheckBox2 = QtGui.QCheckBox("check box 2")
        self.testCheckBox3 = QtGui.QCheckBox("check box 3")
        self.testCheckBox4 = QtGui.QCheckBox("check box 4")
        self.testCheckBox5 = QtGui.QCheckBox("check box 5")

        # dvoustavové checkboxy
        self.testCheckBox1.setCheckState(QtCore.Qt.Unchecked)
        self.testCheckBox2.setCheckState(QtCore.Qt.Checked)

        # třístavové checkboxy
        self.testCheckBox3.setTristate(True)
        self.testCheckBox4.setTristate(True)
        self.testCheckBox5.setTristate(True)
        self.testCheckBox3.setCheckState(QtCore.Qt.Unchecked)
        self.testCheckBox4.setCheckState(QtCore.Qt.PartiallyChecked)
        self.testCheckBox5.setCheckState(QtCore.Qt.Checked)

        # horizontální oddělovač
        horizontalLine = QtGui.QLabel()
        horizontalLine.setFrameStyle(QtGui.QFrame.HLine)

        # tlačítko pro zjištění stavů checkboxů
        testButton = QtGui.QPushButton("Print state")

        # tlačítko pro ukončení aplikace
        quitButton = QtGui.QPushButton("Quit")

        # vytvoření správce geometrie
        layout = QtGui.QVBoxLayout()

        # umístění widgetů do okna
        layout.addWidget(self.testCheckBox1)
        layout.addWidget(self.testCheckBox2)
        layout.addWidget(horizontalLine)
        layout.addWidget(self.testCheckBox3)
        layout.addWidget(self.testCheckBox4)
        layout.addWidget(self.testCheckBox5)
        layout.addWidget(testButton)
        layout.addWidget(quitButton)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(layout)

        # po stisku testovacího tlačítka se zavolá metoda
        testButton.clicked.connect(self.printState)

        # navázání akce na stisk tlačítka pro ukončení aplikace
        quitButton.clicked.connect(self.quit)

    def printState(self):
        print("-" * 50)
        MainWindow.printStateForCheckbox("#1", self.testCheckBox1)
        MainWindow.printStateForCheckbox("#2", self.testCheckBox2)
        MainWindow.printStateForCheckbox("#3", self.testCheckBox3)
        MainWindow.printStateForCheckbox("#4", self.testCheckBox4)
        MainWindow.printStateForCheckbox("#5", self.testCheckBox5)

    @staticmethod
    def printStateForCheckbox(name, checkbox):
        state = checkbox.checkState()
        print("Checkbox {name} is in state {state}".format(name=name, state=state))

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
