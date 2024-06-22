#!/usr/bin/env python

# import "jádra" frameworku Qt i modulu pro GUI
import sys

# třída pro načtení formuláře
from PySide import QtCore, QtGui, QtUiTools


def main():
    app = QtGui.QApplication(sys.argv)
    ui_loader = QtUiTools.QUiLoader()
    working_directory = ui_loader.workingDirectory()
    print(working_directory.path())
    print(working_directory.absolutePath())
    sys.exit(0)


if __name__ == "__main__":
    main()
