#!/usr/bin/env python

import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore, QtGui, QtSvg


# nový widget bude odvozen od obecného widgetu
class MainWindowContent(QtGui.QWidget):
    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindowContent, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        # tlačítka, na které je navázán handler
        quitButton = self.prepareQuitButton()

        # widget s vektorovým obrázkem
        svgWidget = self.prepareSVGWidget()

        # vytvoření správců geometrie
        topLayout = QtGui.QVBoxLayout()

        # vložení widgetů do okna
        topLayout.addWidget(svgWidget)
        topLayout.addWidget(QtGui.QLabel(""))
        topLayout.addWidget(quitButton)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(topLayout)

    def prepareSVGWidget(self):
        svgWidget = QtSvg.QSvgWidget()
        content = QtCore.QByteArray(
            """
            <svg xmlns='http://www.w3.org/2000/svg' version='1.1' width='480' height='480'>
            <circle cx='320.0' cy='240.0' r='128' fill='rgb(0, 255, 255)' style='fill-opacity:.25'/>
            <circle cx='320.0' cy='240.0' r='128' fill='none' stroke='black'/>
            <circle cx='254.891453105' cy='335.850115412' r='111' fill='rgb(221, 34, 255)' style='fill-opacity:.25'/>
            <circle cx='254.891453105' cy='335.850115412' r='111' fill='none' stroke='black'/>
            <circle cx='140.39542436' cy='291.214534183' r='96' fill='rgb(255, 191, 64)' style='fill-opacity:.25'/>
            <circle cx='140.39542436' cy='291.214534183' r='96' fill='none' stroke='black'/>
            </svg>
        """
        )
        svgWidget.load(content)
        return svgWidget

    def prepareQuitButton(self):
        # tlačítko s popisem
        quitButton = QtGui.QPushButton("Quit", self)
        quitButton.resize(quitButton.sizeHint())

        # navázání akce na signál
        quitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        return quitButton


# nový widget bude odvozen od obecného hlavního okna
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindow, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        # velikost není potřeba specifikovat
        # self.resize(400, 300)
        self.setWindowTitle("Custom Stylesheets")

        # hlavní menu
        menubar = self.menuBar()

        # příkaz File/Quit
        fileQuitItem = QtGui.QAction(
            QtGui.QIcon("icons/application-exit.png"), "&Quit", self
        )
        fileQuitItem.triggered.connect(self.close)
        fileQuitItem.setStatusTip("Quit the application")
        fileQuitItem.setShortcut("Ctrl+Q")

        # položka File v hlavním menu
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(fileQuitItem)

        # tlačítko Quit
        quitAction = QtGui.QAction(
            QtGui.QIcon("icons/application-exit.png"), "&Quit", self
        )
        quitAction.triggered.connect(self.close)
        quitAction.setStatusTip("Quit the application")

        # tlačítko About
        aboutAction = QtGui.QAction(
            QtGui.QIcon("icons/dialog-information.png"), "&About", self
        )
        aboutAction.triggered.connect(self.aboutDialog)
        aboutAction.setStatusTip("About this application")

        # nástrojový pruh
        self.toolbar = self.addToolBar("title")

        # přidání tlačítek na nástrojový pruh
        self.toolbar.addAction(quitAction)
        self.toolbar.addAction(aboutAction)

        # vložení komponenty do okna
        self.setCentralWidget(MainWindowContent())

    def aboutDialog(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setText("About:\n...\n...\n...")
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.exec_()

    def run(self, app):
        # zobrazení okna na obrazovce
        self.show()
        # vstup do smyčky událostí (event loop)
        app.exec_()


def main():
    QtGui.QApplication.setStyle("plastique")
    app = QtGui.QApplication(sys.argv)
    MainWindow().run(app)


if __name__ == "__main__":
    main()
