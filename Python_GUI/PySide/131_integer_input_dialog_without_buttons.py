#!/usr/bin/env python

import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore, QtGui


# nový widget bude odvozen od obecného widgetu
class MainWindowContent(QtGui.QWidget):
    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindowContent, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        quitButton = self.prepareQuitButton()

        integerInputDialogButton = self.prepareButton(
            "Integer value input", self.integerInputDialogHandler
        )

        # vytvoření správce geometrie
        topLayout = QtGui.QVBoxLayout()

        # umístění widgetů do okna
        topLayout.addWidget(integerInputDialogButton)
        topLayout.addWidget(quitButton)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(topLayout)

    def integerInputDialogHandler(self):
        # vytvoření a konfigurace vstupního dialogu
        dialog = QtGui.QInputDialog(self)
        dialog.setInputMode(QtGui.QInputDialog.IntInput)

        # nastavení výchozího stavu dialogu
        dialog.setLabelText("Integer input:")
        dialog.setIntMinimum(10)
        dialog.setIntMaximum(20)

        # dialog bude zobrazen bez tlačítek
        dialog.setOption(QtGui.QInputDialog.NoButtons, True)

        # zobrazení dialogu a čekání na uživatelský vstup
        result = dialog.exec_()

        # zpracování a zobrazení výsledků
        value = dialog.intValue()
        message = "Entered value: '{v}'\nClicked on: {c}".format(
            v=value, c="Ok" if result == 1 else "Cancel"
        )

        # zobrazení dialogu s informací o vstupu od uživatele
        self.showMessageBox(message)

    def prepareButton(self, label, handler):
        # tlačítko
        button = QtGui.QPushButton(label, self)
        button.resize(button.sizeHint())

        # navázání akce na signál
        button.clicked.connect(handler)
        return button

    def prepareQuitButton(self):
        # tlačítko
        quitButton = QtGui.QPushButton("Quit", self)
        quitButton.resize(quitButton.sizeHint())

        # navázání akce na signál
        quitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        return quitButton

    def showMessageBox(self, text):
        # vytvoření dialogu
        msgBox = QtGui.QMessageBox()

        # nastavení textu a ikony, které se mají zobrazit
        msgBox.setText(text)
        msgBox.setIcon(QtGui.QMessageBox.Information)

        # zobrazení dialogu
        msgBox.exec_()


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
        self.setWindowTitle("QInputDialog")

        # vložení komponenty do okna
        self.setCentralWidget(MainWindowContent())

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
