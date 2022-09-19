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

import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore
from PySide import QtGui

# používáme jen pro import funkce sleep
import time


# uspání hlavního vlákna aplikace na zadaný počet sekund
def sleep(app, seconds):
    print("sleeping")

    for i in range(0, 10 * seconds):
        print(i)
        app.processEvents()
        time.sleep(1 / 10.0)

    print("waking up")


# nový widget bude odvozen od obecného widgetu
class MainWindowContent(QtGui.QWidget):
    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindowContent, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        # vytvoření widgetů vkládaných do okna
        quitButton = self.prepareQuitButton()

        # vytvoření správce geometrie
        layout = QtGui.QVBoxLayout()

        # umístění widgetů do okna
        layout.addWidget(quitButton)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(layout)

    def prepareQuitButton(self):
        # tlačítko
        quitButton = QtGui.QPushButton("Quit", self)
        quitButton.resize(quitButton.sizeHint())

        # navázání akce na signál
        quitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        return quitButton


# nový widget bude odvozen od obecného hlavního okna
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindow, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        # self.resize(450, 450)
        self.setWindowTitle("QSplashScreen")

        # vložení komponenty do okna
        self.setCentralWidget(MainWindowContent())

    def showMainWindow(self, app):
        sleep(app, 2)
        # zobrazení okna na obrazovce
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)

    # splashscreen
    pixmap = QtGui.QPixmap("pixmaps/pysidelogo.png")
    splash = QtGui.QSplashScreen(pixmap)
    splash.show()

    # vytvoření a zobrazení hlavního okna
    window = MainWindow()
    window.showMainWindow(app)

    splash.finish(window)

    # vstup do smyčky událostí (event loop)
    app.exec_()


if __name__ == "__main__":
    main()
