#!/usr/bin/env python

import sys

from PySide import QtGui


class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.prepareGUI()

    def prepareGUI(self):
        self.resize(320, 240)
        self.setWindowTitle("Simple Button")
        button = QtGui.QPushButton("Button", self)
        button.resize(button.sizeHint())

    def run(self, app):
        self.show()
        app.exec_()


def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow().run(app)


if __name__ == '__main__':
    main()
