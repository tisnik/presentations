#!/usr/bin/env python

import sys

from PySide import QtGui


class HelloWorldLabel(QtGui.QLabel):
    def __init__(self):
        super(HelloWorldLabel, self).__init__("Hello world!")

    def run(self, app):
        self.show()
        app.exec_()


def main():
    app = QtGui.QApplication(sys.argv)
    HelloWorldLabel().run(app)


if __name__ == '__main__':
    main()
