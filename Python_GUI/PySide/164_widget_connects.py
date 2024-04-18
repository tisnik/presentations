#!/usr/bin/env python

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore
from PySide import QtGui

# třída pro načtení formuláře
from PySide import QtUiTools

import sys


def load_ui_form(filename):
    ui_loader = QtUiTools.QUiLoader()
    return ui_loader.load(filename)
    return form


def find_button_by_name(window, button_name):
    return window.findChild(QtGui.QPushButton, button_name)


def on_button_press():
    # vytvoření dialogu
    msgBox = QtGui.QMessageBox()

    # nastavení zprávy a ikony, která se má zobrazit vedle zprávy
    msgBox.setText(u"Hello world!")
    msgBox.setIcon(QtGui.QMessageBox.Information)

    # zobrazení dialogu
    msgBox.exec_()


def main():
    QtGui.QApplication.setStyle("plastique")
    app = QtGui.QApplication(sys.argv)
    mainWindow = load_ui_form("form.ui")
    print(mainWindow)

    # získání reference na první tlačítko
    buttonHello = find_button_by_name(mainWindow, "helloButton")
    print(buttonHello)
    # navázání handleru na signál
    buttonHello.clicked.connect(on_button_press)

    # získání reference na druhé tlačítko
    buttonQuit = find_button_by_name(mainWindow, "quitButton")
    print(buttonHello)
    # navázání handleru na signál
    buttonQuit.clicked.connect(QtCore.QCoreApplication.instance().quit)

    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
