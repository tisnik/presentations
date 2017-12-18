#!/usr/bin/env python
# vim: set fileencoding=utf-8

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
        self.setWindowTitle("Non exclusive selection")

        # testovací přepínací tlačítka
        self.testRadioButton1 = QtGui.QRadioButton("radio button #1")
        self.testRadioButton2 = QtGui.QRadioButton("radio button #2")
        self.testRadioButton3 = QtGui.QRadioButton("radio button #3")
        self.testRadioButton4 = QtGui.QRadioButton("radio button #4")
        self.testRadioButton5 = QtGui.QRadioButton("radio button #5")
        self.testRadioButton6 = QtGui.QRadioButton("radio button #6")

        # první tři tlačítka nebudou automaticky přidána do společné skupiny
        self.testRadioButton1.setAutoExclusive(False)
        self.testRadioButton2.setAutoExclusive(False)
        self.testRadioButton3.setAutoExclusive(False)

        # tlačítko pro zjištění stavů přepínačů
        testButton = QtGui.QPushButton("Print state")

        # tlačítko pro ukončení aplikace
        quitButton = QtGui.QPushButton("Quit")

        # horizontální oddělovač
        horizontalLine = QtGui.QLabel()
        horizontalLine.setFrameStyle(QtGui.QFrame.HLine)

        # vytvoření správce geometrie
        layout = QtGui.QVBoxLayout()

        # umístění widgetů do okna
        layout.addWidget(self.testRadioButton1)
        layout.addWidget(self.testRadioButton2)
        layout.addWidget(self.testRadioButton3)
        layout.addWidget(horizontalLine)
        layout.addWidget(self.testRadioButton4)
        layout.addWidget(self.testRadioButton5)
        layout.addWidget(self.testRadioButton6)
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
        MainWindow.printStateForRadioButton("#1", self.testRadioButton1)
        MainWindow.printStateForRadioButton("#2", self.testRadioButton2)
        MainWindow.printStateForRadioButton("#3", self.testRadioButton3)
        MainWindow.printStateForRadioButton("#4", self.testRadioButton4)
        MainWindow.printStateForRadioButton("#5", self.testRadioButton5)
        MainWindow.printStateForRadioButton("#6", self.testRadioButton6)

    @staticmethod
    def printStateForRadioButton(name, radioButton):
        state = "checked" if radioButton.isChecked() else "unchecked"
        print("Radio button {name} is {state}".format(name=name, state=state))

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


if __name__ == '__main__':
    main()
