#!/usr/bin/env python
# vim: set fileencoding=utf-8

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
        self.setWindowTitle("QCheckBox")

        # testovací zaškrtávací tlačítka
        self.testCheckBox1 = QtGui.QCheckBox("check box 1")
        self.testCheckBox2 = QtGui.QCheckBox("check box 2")
        self.testCheckBox1.setCheckState(QtCore.Qt.Unchecked)
        self.testCheckBox2.setCheckState(QtCore.Qt.Checked)

        # tlačítko pro zjištění stavů checkboxů
        testButton = QtGui.QPushButton("Print state")

        # tlačítko pro ukončení aplikace
        quitButton = QtGui.QPushButton("Quit")

        # vytvoření správce geometrie
        layout = QtGui.QVBoxLayout()

        # umístění widgetů do okna
        layout.addWidget(self.testCheckBox1)
        layout.addWidget(self.testCheckBox2)
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

    @staticmethod
    def printStateForCheckbox(name, checkbox):
        state = "checked" if checkbox.isChecked() else "unchecked"
        print("Checkbox {name} is {state}".format(name=name, state=state))

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
