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
from PySide import QtCore, QtGui


# nový widget bude odvozen od obecného widgetu
class MainWindowContent(QtGui.QWidget):
    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindowContent, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        # vytvoření widgetů vkládaných do okna
        self.label = QtGui.QLabel("")
        scrollBar = self.prepareScrollbar()
        quitButton = self.prepareQuitButton()

        # vytvoření správce geometrie
        layout = QtGui.QVBoxLayout()

        # umístění widgetů do okna
        layout.addWidget(self.label)
        layout.addWidget(scrollBar)
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

    def prepareScrollbar(self):
        # vytvoření scrollbaru
        scrollbar = QtGui.QScrollBar(QtCore.Qt.Horizontal)
        scrollbar.valueChanged.connect(self.onScrollBarValueChanged)

        scrollbar.setMinimum(-100)
        scrollbar.setMaximum(100)
        scrollbar.setSingleStep(1)
        scrollbar.setPageStep(10)
        scrollbar.setValue(1)

        return scrollbar

    def onScrollBarValueChanged(self, value):
        text = "Scrollbar value: {v}".format(v=value)
        self.label.setText(text)


# nový widget bude odvozen od obecného hlavního okna
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindow, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        self.resize(450, 300)
        self.setWindowTitle("QScrollBar")

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
