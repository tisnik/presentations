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

        # widgety s vektorovým obrázkem
        vimButton = self.prepareButtonWithIcon("Vim", "editors/vim.svg")
        emacsButton = self.prepareButtonWithIcon("Emacs", "editors/emacs.svg")
        atomButton = self.prepareButtonWithIcon("Atom", "editors/atom.svg")

        # vytvoření správců geometrie
        topLayout = QtGui.QVBoxLayout()

        # vložení widgetů do okna
        topLayout.addWidget(QtGui.QLabel("Select editor:"))
        topLayout.addWidget(vimButton)
        topLayout.addWidget(emacsButton)
        topLayout.addWidget(atomButton)
        topLayout.addWidget(QtGui.QLabel(""))
        topLayout.addWidget(quitButton)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(topLayout)

    def prepareButtonWithIcon(self, label, filename):
        icon = QtGui.QIcon(filename)
        button = QtGui.QPushButton(label)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(40, 40))

        # navázání akce na signál
        button.clicked.connect(lambda: self.showMessageBox(filename))
        return button

    def prepareQuitButton(self):
        # tlačítko s popisem
        quitButton = QtGui.QPushButton("Quit", self)
        quitButton.resize(quitButton.sizeHint())

        # navázání akce na signál
        quitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        return quitButton

    def showMessageBox(self, filename):
        # tlačítko, která mají být součástí dialogu
        buttons = QtGui.QMessageBox.Ok

        # vytvoření dialogu
        msgBox = QtGui.QMessageBox()

        # nastavení zprávy a ikony, která se má zobrazit vedle zprávy
        msgBox.setStandardButtons(buttons)
        msgBox.setText(u"")

        # načtení ikony
        icon = QtGui.QIcon(filename)

        # vytvoření pixmapy a její nastavení jako ikony pro dialog
        pixmap = icon.pixmap(200, 200)
        msgBox.setIconPixmap(pixmap)

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
