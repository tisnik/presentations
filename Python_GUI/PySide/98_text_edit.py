#!/usr/bin/env python

import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore
from PySide import QtGui


# nový widget bude odvozen od obecného widgetu
class MainWindowContent(QtGui.QWidget):
    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindowContent, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        quitButton = self.prepareQuitButton()
        showTextButton = self.prepareShowTextButton()
        self.textEdit = self.prepareTextEdit()

        # vytvoření prvního správce geometrie
        topLayout = QtGui.QVBoxLayout()

        # vytvoření druhého správce geometrie
        subLayout = QtGui.QHBoxLayout()

        # umístění widgetů do okna
        topLayout.addWidget(self.textEdit)
        topLayout.addLayout(subLayout)

        # tlačítka vložíme do druhého správce geometrie
        subLayout.addWidget(showTextButton)
        subLayout.addWidget(quitButton)

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
        # víceřádkové vstupní textové pole
        textEdit = QtGui.QTextEdit(self)
        textEdit.setAcceptRichText(False)
        return textEdit

    def showTextDialog(self):
        msgBox = QtGui.QMessageBox()
        text = self.textEdit.toPlainText()
        msgBox.setText(u"Text:\n----------------\n{t}\n----------------".format(t=text))
        msgBox.setIcon(QtGui.QMessageBox.Information)
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
