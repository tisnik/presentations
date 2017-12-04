#!/usr/bin/env python
# vim: set fileencoding=utf-8

import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore
from PySide import QtGui


# callback funkce
def closeApplication():
    print("Closing...")
    sys.exit(0)


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

        # tlačítko
        button = QtGui.QPushButton("Quit", self)
        button.resize(button.sizeHint())
        button.setToolTip("Immediately quit this application")

        # starý způsob navázání signálu, který není příliš Python-friendly
        QtCore.QObject.connect(button, QtCore.SIGNAL ('clicked()'), closeApplication)

    def run(self, app):
        # zobrazení okna na obrazovce
        self.show()
        # vstup do smyčky událostí (event loop)
        app.exec_()


def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow().run(app)


if __name__ == '__main__':
    main()
