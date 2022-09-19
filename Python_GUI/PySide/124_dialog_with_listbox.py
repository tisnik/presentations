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

        textInputDialogButton = self.prepareButton(
            "Text Input", self.textInputDialogHandler
        )

        # vytvoření správce geometrie
        topLayout = QtGui.QVBoxLayout()

        # umístění widgetů do okna
        topLayout.addWidget(textInputDialogButton)
        topLayout.addWidget(quitButton)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(topLayout)

    def textInputDialogHandler(self):
        # vytvoření a konfigurace vstupního dialogu
        dialog = QtGui.QInputDialog(self)
        dialog.setLabelText("Your choice:")
        dialog.setOption(QtGui.QInputDialog.UseListViewForComboBoxItems, True)
        dialog.setComboBoxItems(["Assembler", "Bash", "C", "C++", "Clojure", "Python"])

        # zobrazení dialogu a čekání na uživatelský vstup
        result = dialog.exec_()

        # zpracování a zobrazení výsledků
        text = dialog.textValue()
        message = "Entered text: '{t}'\nClicked on: {c}".format(
            t=text, c="Ok" if result == 1 else "Cancel"
        )

        self.showMessageBox(message)

    def prepareButton(self, label, handler):
        # tlačítko
        button = QtGui.QPushButton(label, self)
        button.resize(button.sizeHint())

        # navázání akce na signál
        button.clicked.connect(handler)
        return button

    def prepareQuitButton(self):
        # tlačítko
        quitButton = QtGui.QPushButton("Quit", self)
        quitButton.resize(quitButton.sizeHint())

        # navázání akce na signál
        quitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        return quitButton

    def showMessageBox(self, text):
        msgBox = QtGui.QMessageBox()
        msgBox.setText(text)
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.exec_()


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
        self.setWindowTitle("QInputDialog")

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
