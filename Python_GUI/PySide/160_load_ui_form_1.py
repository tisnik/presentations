#!/usr/bin/env python

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore
from PySide import QtGui

# třída pro načtení formuláře
from PySide import QtUiTools

import sys


def load_ui_form(filename):
    ui_loader = QtUiTools.QUiLoader()
    form = ui_loader.load(filename)
    return form


def main():
    QtGui.QApplication.setStyle("plastique")
    app = QtGui.QApplication(sys.argv)
    mainWindow = load_ui_form("mainwindow.ui")
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
