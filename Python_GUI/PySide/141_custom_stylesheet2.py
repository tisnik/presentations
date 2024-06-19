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
        # tlačítka, na které je navázán handler
        quitButton = self.prepareQuitButton()

        # další tlačítka
        button1 = self.prepareButtonWithBackground("#e08080")
        button2 = self.prepareButtonWithBackground("lightblue")
        button3 = self.prepareButtonWithBackground("yellow")

        # ostatní widgety
        lineEdit = self.prepareLineEdit()

        # vytvoření správců geometrie
        topLayout = QtGui.QVBoxLayout()

        # vložení widgetů do okna
        topLayout.addWidget(button1)
        topLayout.addWidget(button2)
        topLayout.addWidget(button3)
        topLayout.addWidget(QtGui.QLabel(""))
        topLayout.addWidget(lineEdit)
        topLayout.addWidget(QtGui.QLabel(""))
        topLayout.addWidget(quitButton)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(topLayout)

    def prepareLineEdit(self):
        # jednořádkové vstupní textové pole
        lineEdit = QtGui.QLineEdit(self)
        # naplnění textového pole textem
        lineEdit.setText(u"příliš žluťoučký kůň úpěl ďábelské ódy")
        return lineEdit

    def prepareButtonWithBackground(self, background):
        # tlačítko s popisem
        button = QtGui.QPushButton(background, self)

        # nastavení stylu
        styleSheet = "background-color: {background}".format(background=background)
        button.setStyleSheet(styleSheet)

        button.resize(button.sizeHint())

        return button

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
        self.resize(400, 300)
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

        # položka Style v hlavním menu
        styleMenu = menubar.addMenu("&Style")

        # jednotlivé položky menu s nabízenými styly
        for key in QtGui.QStyleFactory.keys():
            styleMenuItem = QtGui.QAction(key, self)
            styleMenuItem.triggered.connect(lambda key=key: self.setStyle(key))
            styleMenu.addAction(styleMenuItem)

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

        styleSheet = """
            QWidget {border-radius: 10px;
                     border: 1px solid gray;}
            QPushButton { color: #404040;
                          background-color: rgba(188, 188, 188, 50);
                          font-size: 18px;
                          border: 1px solid black;
                          outline-color: red;
                        }
            QLabel { color: #404040;
                     background-color: rgba(255, 188, 20, 0);
                     border: 0px;
                     font-size: 14px;
                   }
            QToolBar { margin: 10px; }
            QLineEdit { background-color: #c0ffc0;
                        selection-background-color:  red;
                        selection-color:  white;
                        font-size: 24px;}
        """
        self.setStyleSheet(styleSheet)

    def setStyle(self, styleName):
        # nastavení vybraného stylu
        QtGui.QApplication.setStyle(styleName)

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
    # QtGui.QApplication.setStyle("plastique")
    # QtGui.QApplication.setStyleSheet("background-color: #407040; color: white")
    app = QtGui.QApplication(sys.argv)
    MainWindow().run(app)


if __name__ == "__main__":
    main()
