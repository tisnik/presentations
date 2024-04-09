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

    @staticmethod
    def prepareStyles():
        # vytvoření sekvence se všemi dostupnými styly
        style_names = QtGui.QStyleFactory.keys()
        styles = [QtGui.QStyleFactory.create(style_name) for style_name in style_names]
        return styles

    def prepareGUI(self):
        styles = MainWindowContent.prepareStyles()

        # tlačítka, na které je navázán handler
        quitButton = self.prepareQuitButton()

        # vytvoření správců geometrie
        topLayout = QtGui.QHBoxLayout()
        leftLayout = QtGui.QVBoxLayout()
        centerLayout = QtGui.QVBoxLayout()
        rightLayout = QtGui.QVBoxLayout()

        # umístění widgetů do okna - levý sloupec
        for style in styles:
            lineEdit = self.prepareLineEdit(style)
            leftLayout.addWidget(lineEdit)

        for style in styles:
            slider = self.prepareSlider(style)
            leftLayout.addWidget(slider)

        leftLayout.addWidget(QtGui.QLabel(""))
        leftLayout.addWidget(quitButton)

        # umístění widgetů do okna - prostřední sloupec
        for style in styles:
            # testovací přepínací tlačítka
            testRadioButton1 = self.prepareRadioButton(style, "radio button #1", False)
            testRadioButton2 = self.prepareRadioButton(style, "radio button #2", True)
            # vložení přepínacích tlačítek na plochu okna
            centerLayout.addWidget(testRadioButton1)
            centerLayout.addWidget(testRadioButton2)
            centerLayout.addWidget(QtGui.QLabel(""))

        # umístění widgetů do okna - pravý sloupec
        for style in styles:
            # testovací zaškrtávací tlačítka
            testCheckBox1 = self.prepareCheckBox(style, "check box #1", False)
            testCheckBox2 = self.prepareCheckBox(style, "check box #2", True)
            # vložení widgetů tlačítek na plochu okna
            rightLayout.addWidget(testCheckBox1)
            rightLayout.addWidget(testCheckBox2)
            rightLayout.addWidget(QtGui.QLabel(""))

        # umístění layoutů do hlavního layoutu
        topLayout.addLayout(leftLayout)
        topLayout.addLayout(centerLayout)
        topLayout.addLayout(rightLayout)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(topLayout)

    def prepareLineEdit(self, style):
        # jednořádkové vstupní textové pole
        lineEdit = QtGui.QLineEdit(self)
        # naplnění textového pole textem
        lineEdit.setText(u"příliš žluťoučký kůň úpěl ďábelské ódy")
        lineEdit.setStyle(style)
        return lineEdit

    def prepareSlider(self, style):
        # vytvoření slideru
        slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        slider.setStyle(style)
        return slider

    def prepareRadioButton(self, style, text, checked):
        # vytvoření přepínacího tlačítka
        radioButton = QtGui.QRadioButton(text)
        radioButton.setStyle(style)
        radioButton.setChecked(checked)
        return radioButton

    def prepareCheckBox(self, style, text, checked):
        # vytvoření zaškrtávacího tlačítka
        checkBox = QtGui.QCheckBox(text)
        checkBox.setStyle(style)
        checkBox.setChecked(checked)
        return checkBox

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
        # self.resize(320, 240)
        self.setWindowTitle("Individual styles")

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
    app = QtGui.QApplication(sys.argv)
    MainWindow().run(app)


if __name__ == "__main__":
    main()
