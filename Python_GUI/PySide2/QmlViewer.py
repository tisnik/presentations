
# univerzální prohlížeč QML souborů

import sys

# import "jádra" frameworku Qt i modulu pro GUI
# modul pro práci s QML
from PySide2 import QtCore, QtGui, QtQuick


# nový widget bude odvozen od QDeclarativeView
class MainWindow(QtQuick.QQuickView):
    def __init__(self, qml_file, parent=None):
        super(MainWindow, self).__init__(parent)
        # nastavení titulku hlavního okna aplikace
        self.setTitle("QML Example @ PySide2: " + qml_file)
        # načtení souboru QML
        self.setSource(QtCore.QUrl.fromLocalFile(qml_file))
        # necháme QML změnit velikost okna
        self.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)


def main(qml_file):
    # vytvoření Qt aplikace
    app = QtGui.QGuiApplication(sys.argv)

    # vytvoření hlavního okna
    window = MainWindow(qml_file)

    # zobrazení hlavního okna na desktopu
    window.show()

    # spuštění aplikace
    sys.exit(app.exec_())
