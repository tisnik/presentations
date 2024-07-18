#!/usr/bin/env python

import io
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
        self.textEdit = self.prepareTextEdit()

        # vytvoření správce geometrie
        topLayout = QtGui.QVBoxLayout()

        # umístění widgetů do okna
        topLayout.addWidget(self.textEdit)
        topLayout.addWidget(quitButton)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(topLayout)

    def prepareShowTextButton(self):
        # druhé tlačítko
        showTextButton = QtGui.QPushButton("Show text", self)
        showTextButton.resize(showTextButton.sizeHint())

        # navázání akce na signál
        showTextButton.clicked.connect(self.showTextDialog)
        return showTextButton

    def prepareQuitButton(self):
        # tlačítko
        quitButton = QtGui.QPushButton("Quit", self)
        quitButton.resize(quitButton.sizeHint())

        # navázání akce na signál
        quitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        return quitButton

    def prepareTextEdit(self):
        # jednořádkové vstupní textové pole
        textEdit = QtGui.QTextEdit(self)
        textEdit.setAcceptRichText(True)
        textEdit.setReadOnly(True)
        with io.open("test.html", encoding="utf-8") as fin:
            textEdit.setHtml(fin.read())
        return textEdit


# nový widget bude odvozen od obecného hlavního okna
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindow, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        self.resize(640, 480)
        self.setWindowTitle("QMainWindow + QListWidget")

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
