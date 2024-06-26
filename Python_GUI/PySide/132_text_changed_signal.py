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

        textInputDialogButton = self.prepareButton(
            "Text Input", self.textInputDialogHandler
        )

        self.enteredTextLabel = QtGui.QLabel("")

        # vytvoření správce geometrie
        topLayout = QtGui.QVBoxLayout()

        # umístění widgetů do okna
        topLayout.addWidget(self.enteredTextLabel)
        topLayout.addWidget(textInputDialogButton)
        topLayout.addWidget(quitButton)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(topLayout)

    def onTextValueChanged(self, text):
        """Handler zavolaný při změně textu ve vstupním dialogu."""
        self.enteredTextLabel.setText(text)

    def textInputDialogHandler(self):
        # vytvoření a konfigurace vstupního dialogu
        dialog = QtGui.QInputDialog(self)
        dialog.setInputMode(QtGui.QInputDialog.TextInput)

        # nastavení výchozího stavu dialogu
        dialog.setLabelText("Text input:")
        dialog.setTextValue("")

        # dialog bude zobrazen bez tlačítek
        dialog.setOption(QtGui.QInputDialog.NoButtons, True)

        # při změně textu se zavolá handler
        dialog.textValueChanged.connect(self.onTextValueChanged)

        # zobrazení dialogu a čekání na uživatelský vstup
        result = dialog.exec_()

        # zpracování a zobrazení výsledků
        text = dialog.textValue()
        message = "Entered text: '{t}'\nClicked on: {c}".format(
            t=text, c="Ok" if result == 1 else "Cancel"
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
