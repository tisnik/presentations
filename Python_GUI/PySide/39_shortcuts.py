#!/usr/bin/env python

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
        self.setWindowTitle("Shortcuts")

        # testovací zaškrtávací tlačítka
        self.testCheckBox1 = QtGui.QCheckBox("check box &x")
        self.testCheckBox2 = QtGui.QCheckBox("check box &y")
        self.testCheckBox3 = QtGui.QCheckBox("check box &z")
        self.testCheckBox1.setCheckState(QtCore.Qt.Unchecked)
        self.testCheckBox2.setCheckState(QtCore.Qt.Checked)
        self.testCheckBox3.setCheckState(QtCore.Qt.Unchecked)

        # testovací přepínací tlačítka
        self.testRadioButton1 = QtGui.QRadioButton("radio button &a")
        self.testRadioButton2 = QtGui.QRadioButton("radio button &b")
        self.testRadioButton3 = QtGui.QRadioButton("radio button &c")
        self.testRadioButton2.setChecked(True)

        # tlačítko pro zjištění stavů přepínačů
        testButton = QtGui.QPushButton("&Print state")

        # tlačítko pro ukončení aplikace
        quitButton = QtGui.QPushButton("&Quit")

        # horizontální oddělovače
        horizontalLine1 = QtGui.QLabel()
        horizontalLine1.setFrameStyle(QtGui.QFrame.HLine)
        horizontalLine2 = QtGui.QLabel()
        horizontalLine2.setFrameStyle(QtGui.QFrame.HLine)

        # vytvoření správce geometrie
        layout = QtGui.QVBoxLayout()

        # umístění widgetů do okna
        layout.addWidget(self.testRadioButton1)
        layout.addWidget(self.testRadioButton2)
        layout.addWidget(self.testRadioButton3)
        layout.addWidget(horizontalLine1)
        layout.addWidget(self.testCheckBox1)
        layout.addWidget(self.testCheckBox2)
        layout.addWidget(self.testCheckBox3)
        layout.addWidget(horizontalLine2)
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
        MainWindow.printStateForCheckbox("#1", self.testCheckBox1)
        MainWindow.printStateForCheckbox("#2", self.testCheckBox2)
        MainWindow.printStateForCheckbox("#3", self.testCheckBox3)

    @staticmethod
    def printStateForCheckbox(name, checkbox):
        state = "checked" if checkbox.isChecked() else "unchecked"
        print("Checkbox {name} is {state}".format(name=name, state=state))

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


if __name__ == "__main__":
    main()
