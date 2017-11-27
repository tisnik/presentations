#!/usr/bin/env python
# vim: set fileencoding=utf-8

import sys

# prozatím budeme využívat jen modul QtGui
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
        self.setWindowTitle("Window and label")

        # návěští
        label = QtGui.QLabel("Hello world!", self)
        # posun v rámci nadřazeného widgetu
        label.move(100, 100)

    def run(self, app):
        # zobrazení okna na obrazovce
        self.show()
        # vstup do smyčky událostí (event loop)
        sys.exit(app.exec_())


def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow().run(app)


if __name__ == '__main__':
    main()
