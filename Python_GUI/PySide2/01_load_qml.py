#!/usr/bin/env python

import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide2 import QtCore
from PySide2 import QtGui

# modul pro práci s QML
from PySide2 import QtQuick

QML_FILE = "01.qml"


# nový widget bude odvozen od QDeclarativeView
class MainWindow(QtQuick.QQuickView):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setTitle("QML Example @ PySide2")
        # načtení souboru QML
        self.setSource(QtCore.QUrl.fromLocalFile(QML_FILE))
        # necháme QML změnit velikost okna
        self.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)


def main():
    # vytvoření Qt aplikace
    app = QtGui.QGuiApplication(sys.argv)

    # vytvoření hlavního okna
    window = MainWindow()

    # zobrazení hlavního okna
    window.show()

    # spuštění aplikace
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
