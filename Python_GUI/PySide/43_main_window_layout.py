#!/usr/bin/env python

import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore
from PySide import QtGui


# nový widget bude odvozen od obecného widgetu
class MainWindowContent(QtGui.QWidget):
    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindowContent, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        # tlačítko
        button = QtGui.QPushButton("Quit", self)
        button.resize(button.sizeHint())

        # navázání akce na signál
        button.clicked.connect(QtCore.QCoreApplication.instance().quit)


# nový widget bude odvozen od obecného hlavního okna
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindow, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        # velikost není potřeba specifikovat
        # self.resize(320, 240)
        self.setWindowTitle("QMainWindow")

        # vložení komponenty do okna
        self.setCentralWidget(MainWindowContent())

    def run(self, app):
        # zobrazení okna na obrazovce
        self.show()
        # vstup do smyčky událostí (event loop)
        app.exec_()


def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow().run(app)


if __name__ == "__main__":
    main()
