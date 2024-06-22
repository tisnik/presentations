#!/usr/bin/env python

# import "jádra" frameworku Qt i modulu pro GUI
import sys

# třída pro načtení formuláře
from PySide import QtCore, QtGui, QtUiTools


def load_ui_form(filename):
    ui_loader = QtUiTools.QUiLoader()
    return ui_loader.load(filename)
    return form


def main():
    QtGui.QApplication.setStyle("plastique")
    app = QtGui.QApplication(sys.argv)
    mainWindow = load_ui_form("form.ui")
    print(mainWindow)

    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
