#!/usr/bin/env python

import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore
from PySide import QtGui

# modul pro práci s QML
from PySide import QtDeclarative

QML_FILE = "169_load_qml_5.qml"


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
