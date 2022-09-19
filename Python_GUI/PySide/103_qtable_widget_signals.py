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
        # vytvoření widgetů vkládaných do okna
        self.table = self.prepareTable()
        self.textEdit = self.prepareTextEdit()
        quitButton = self.prepareQuitButton()

        # vytvoření správce geometrie
        layout = QtGui.QVBoxLayout()

        # umístění widgetů do okna
        layout.addWidget(self.table)
        layout.addWidget(self.textEdit)
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

    def prepareTextEdit(self):
        # víceřádkové vstupní textové pole
        textEdit = QtGui.QPlainTextEdit(self)
        textEdit.setReadOnly(True)
        return textEdit

    def prepareTable(self):
        # vytvoření tabulky
        table = QtGui.QTableWidget(self)
        table.setColumnCount(10)
        table.setRowCount(10)

        # naplnění tabulky
        for j in range(1, 11):
            for i in range(1, 11):
                item = QtGui.QTableWidgetItem(str(i * j))
                tooltip = u"výsledek součinu {x}×{y}".format(x=i, y=j)
                item.setToolTip(tooltip)
                table.setItem(j - 1, i - 1, item)

        # registrace callback funkcí
        table.cellClicked.connect(self.onCellClicked)
        table.currentCellChanged.connect(self.onCurrentCellChanged)
        table.cellChanged.connect(self.onCellChanged)

        return table

    def onCellClicked(self, row, column):
        message = u"kliknuto na buňku [{x}, {y}]".format(x=column, y=row)
        self.textEdit.appendPlainText(message)

    def onCurrentCellChanged(self, row1, column1, row2, column2):
        message = u"změna fokusu z buňky [{x2}, {y2}] na buňku [{x1}, {y1}]".format(
            x1=column1, y1=row1, x2=column2, y2=row2
        )
        self.textEdit.appendPlainText(message)

    def onCellChanged(self, row, column):
        value = self.table.item(row, column).text()
        message = u"změna obsahu buňky [{x}, {y}] na hodnotu {v}".format(
            x=column, y=row, v=value
        )
        self.textEdit.appendPlainText(message)


# nový widget bude odvozen od obecného hlavního okna
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindow, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        self.resize(450, 450)
        self.setWindowTitle("QTableWidget")

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
