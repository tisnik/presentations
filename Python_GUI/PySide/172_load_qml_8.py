#!/usr/bin/env python

import sys

# import "jádra" frameworku Qt i modulu pro GUI
# modul pro práci s QML
from PySide import QtCore, QtDeclarative, QtGui

QML_FILE = "172_load_qml_8.qml"


# nový widget bude odvozen od QDeclarativeView
class MainWindow(QtDeclarative.QDeclarativeView):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("QML Example")
        # načtení souboru QML
        self.setSource(QtCore.QUrl.fromLocalFile(QML_FILE))
        # necháme QML změnit velikost okna
        self.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)


def main():
    # vytvoření Qt aplikace
    app = QtGui.QApplication(sys.argv)

    # vytvoření hlavního okna
    window = MainWindow()

    # zobrazení hlavního okna
    window.show()

    # spuštění aplikace
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
