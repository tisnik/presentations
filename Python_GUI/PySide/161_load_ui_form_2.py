#!/usr/bin/env python

# import "jádra" frameworku Qt i modulu pro GUI
import sys

# třída pro načtení formuláře
from PySide import QtCore, QtGui, QtUiTools


def load_ui_form(filename):
    ui_loader = QtUiTools.QUiLoader()
    q_file = QtCore.QFile(filename)
    q_file.open(QtCore.QFile.ReadOnly)
    form = ui_loader.load(q_file)
    q_file.close()
    return form


def main():
    QtGui.QApplication.setStyle("plastique")
    app = QtGui.QApplication(sys.argv)
    mainWindow = load_ui_form("mainwindow.ui")
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
