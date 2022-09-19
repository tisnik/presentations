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


# nový widget bude odvozen od obecného widgetu
class MainWindowContent(QtGui.QWidget):
    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindowContent, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        quitButton = self.prepareQuitButton()
        messageBoxButton = self.prepareMessageBoxButton()

        # vytvoření správce geometrie
        topLayout = QtGui.QVBoxLayout()

        # umístění widgetů do okna
        topLayout.addWidget(messageBoxButton)
        topLayout.addWidget(quitButton)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(topLayout)

    def prepareMessageBoxButton(self):
        # tlačítko
        messageBoxButton = QtGui.QPushButton("Message Box", self)
        messageBoxButton.resize(messageBoxButton.sizeHint())

        # navázání akce na signál
        messageBoxButton.clicked.connect(self.showMessageBox)
        return messageBoxButton

    def prepareQuitButton(self):
        # tlačítko
        quitButton = QtGui.QPushButton("Quit", self)
        quitButton.resize(quitButton.sizeHint())

        # navázání akce na signál
        quitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        return quitButton

    def showMessageBox(self):
        # tlačítka, která mají být součástí dialogu
        buttons = (
            QtGui.QMessageBox.Yes
            | QtGui.QMessageBox.YesToAll
            | QtGui.QMessageBox.No
            | QtGui.QMessageBox.NoToAll
            | QtGui.QMessageBox.Help
        )
        # vytvoření dialogu
        msgBox = QtGui.QMessageBox()

        # nastavení zprávy a ikony, která se má zobrazit vedle zprávy
        msgBox.setStandardButtons(buttons)
        msgBox.setText(u"Zpráva")
        msgBox.setIcon(QtGui.QMessageBox.Question)
        # msgBox.setIcon(QtGui.QMessageBox.Question)
        # msgBox.setIcon(QtGui.QMessageBox.Warning)
        # msgBox.setIcon(QtGui.QMessageBox.Critical)

        # zobrazení dialogu
        print(msgBox.exec_())


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
        self.setWindowTitle("QMessageBox")

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
