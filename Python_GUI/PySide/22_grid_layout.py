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
        self.setWindowTitle("Quit Button")

        # tlačítka
        button1 = QtGui.QPushButton("One")
        button2 = QtGui.QPushButton("Two")
        button3 = QtGui.QPushButton("Three")
        button4 = QtGui.QPushButton("Four")
        button5 = QtGui.QPushButton("Five")
        button6 = QtGui.QPushButton("Six")

        # vytvoření správce geometrie a umístění widgetů
        layout = QtGui.QGridLayout()
        layout.addWidget(button1, 1, 1)
        layout.addWidget(button2, 2, 2)
        layout.addWidget(button3, 2, 3)
        layout.addWidget(button4, 3, 2)
        layout.addWidget(button5, 4, 1)
        layout.addWidget(button6, 4, 2)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(layout)

        # navázání akce na signál
        button1.clicked.connect(self.quit)
        button2.clicked.connect(self.quit)
        button3.clicked.connect(self.quit)
        button4.clicked.connect(self.quit)
        button5.clicked.connect(self.quit)
        button6.clicked.connect(self.quit)

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
