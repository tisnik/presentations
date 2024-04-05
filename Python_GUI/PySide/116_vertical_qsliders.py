#!/usr/bin/env python

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

        # vytvoření prvního správce geometrie
        topLayout = QtGui.QVBoxLayout()

        # vytvoření druhého správce geometrie
        subLayout = QtGui.QHBoxLayout()

        # umístění widgetů do okna

        tickPositions = (
            QtGui.QSlider.NoTicks,
            QtGui.QSlider.TicksBothSides,
            QtGui.QSlider.TicksAbove,
            QtGui.QSlider.TicksBelow,
            QtGui.QSlider.TicksLeft,
            QtGui.QSlider.TicksRight,
        )

        for tickPosition in tickPositions:
            subLayout.addWidget(self.prepareSlider(tickPosition))

        topLayout.addLayout(subLayout)
        topLayout.addWidget(quitButton)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(topLayout)

    def prepareQuitButton(self):
        # tlačítko
        quitButton = QtGui.QPushButton("Quit", self)
        quitButton.resize(quitButton.sizeHint())

        # navázání akce na signál
        quitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        return quitButton

    def prepareSlider(self, tickPosition):
        # vytvoření slideru
        slider = QtGui.QSlider(QtCore.Qt.Vertical)
        slider.setTickInterval(4)
        slider.setValue(1)
        slider.setTickPosition(tickPosition)

        return slider


# nový widget bude odvozen od obecného hlavního okna
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindow, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        self.resize(450, 300)
        self.setWindowTitle("QSlider")

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
