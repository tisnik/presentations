#!/usr/bin/env python
# vim: set fileencoding=utf-8

import sys

# prozatím budeme využívat jen modul QtGui
from PySide import QtGui


# nový widget bude odvozen od standardního návěští
class HelloWorldLabel(QtGui.QLabel):

    def __init__(self):
        # zavoláme konstruktor předka

        # varianta pro Python 2.x i pro Python 3.x
        super(HelloWorldLabel, self).__init__("Hello world!")

        # varianta pro Python 3.x
        # super().__init__("Hello world!")

    def run(self, app):
        # zobrazení okna na obrazovce
        self.show()
        # vstup do smyčky událostí (event loop)
        sys.exit(app.exec_())


def main():
    app = QtGui.QApplication(sys.argv)
    HelloWorldLabel().run(app)


if __name__ == '__main__':
    main()
