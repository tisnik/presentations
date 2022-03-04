#!/usr/bin/env python
# vim: set fileencoding=utf-8

import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore
from PySide import QtGui


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
        self.setWindowTitle("QMainWindow + statusBar + mainMenu")

        # stavový řádek
        self.statusBar().showMessage("QMainWindow")

        # hlavní menu
        menubar = self.menuBar()

        # příkaz File/Quit
        fileQuitItem = QtGui.QAction("&Quit", self)
        fileQuitItem.triggered.connect(self.close)
        fileQuitItem.setStatusTip("Quit the application")

        # položka File v hlavním menu
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(fileQuitItem)

        # příkaz Help/About
        helpAboutItem = QtGui.QAction("&About", self)
        helpAboutItem.triggered.connect(self.aboutDialog)
        helpAboutItem.setStatusTip("About this application")

        # položka Help v hlavním menu
        helpMenu = menubar.addMenu("&Help")
        helpMenu.addAction(helpAboutItem)

        # zobrazení hlavního okna
        self.show()

    def aboutDialog(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setText("About:\n...\n...\n...")
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.exec_()

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
