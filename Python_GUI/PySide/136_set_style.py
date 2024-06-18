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
        openFileButton = self.prepareOpenFileButton()
        colorDialogButton = self.prepareColorDialogButton()
        messageBoxButton = self.prepareMessageBoxButton()

        # vytvoření testovacích widgetů vkládaných do okna
        tree = self.prepareTree()
        slider = self.prepareSlider()
        lineEdit = self.prepareLineEdit()
        textEdit = self.prepareTextEdit()
        dial = self.prepareDial()

        # různě ostylovaná návěští
        testLabel1 = QtGui.QLabel("Normal/Default")
        testLabel2 = QtGui.QLabel("Box")
        testLabel3 = QtGui.QLabel("Panel")
        testLabel4 = QtGui.QLabel("Win Panel")
        testLabel5 = QtGui.QLabel("HLine")
        testLabel6 = QtGui.QLabel("VLine")
        testLabel7 = QtGui.QLabel("StyledPanel")

        testLabel2.setFrameStyle(QtGui.QFrame.Box)
        testLabel3.setFrameStyle(QtGui.QFrame.Panel)
        testLabel4.setFrameStyle(QtGui.QFrame.WinPanel)
        testLabel5.setFrameStyle(QtGui.QFrame.HLine)
        testLabel6.setFrameStyle(QtGui.QFrame.VLine)
        testLabel7.setFrameStyle(QtGui.QFrame.StyledPanel)

        # testovací přepínací tlačítka
        testRadioButton1 = QtGui.QRadioButton("radio button #1")
        testRadioButton2 = QtGui.QRadioButton("radio button #2")
        testRadioButton3 = QtGui.QRadioButton("radio button #3")

        # testovací zaškrtávací tlačítka
        testCheckBox1 = QtGui.QCheckBox("check box 1")
        testCheckBox2 = QtGui.QCheckBox("check box 2")

        # které tlačítko bude vybráno
        testRadioButton3.setChecked(True)
        testCheckBox2.setChecked(True)

        # vytvoření správců geometrie
        topLayout = QtGui.QHBoxLayout()
        leftLayout = QtGui.QVBoxLayout()
        centerLayout = QtGui.QVBoxLayout()
        rightLayout = QtGui.QVBoxLayout()

        # umístění widgetů do okna - levý sloupec
        leftLayout.addWidget(tree)
        leftLayout.addWidget(slider)

        # umístění widgetů do okna - prostřední sloupec
        centerLayout.addWidget(lineEdit)
        centerLayout.addWidget(textEdit)
        centerLayout.addWidget(openFileButton)
        centerLayout.addWidget(colorDialogButton)
        centerLayout.addWidget(messageBoxButton)
        centerLayout.addWidget(quitButton)

        # umístění widgetů do okna - pravý sloupec
        rightLayout.addWidget(testRadioButton1)
        rightLayout.addWidget(testRadioButton2)
        rightLayout.addWidget(testRadioButton3)
        rightLayout.addWidget(testCheckBox1)
        rightLayout.addWidget(testCheckBox2)

        rightLayout.addWidget(testLabel1)
        rightLayout.addWidget(testLabel2)
        rightLayout.addWidget(testLabel3)
        rightLayout.addWidget(testLabel4)
        rightLayout.addWidget(testLabel5)
        rightLayout.addWidget(testLabel6)
        rightLayout.addWidget(testLabel7)
        rightLayout.addWidget(dial)

        # umístění layoutů do hlavního layoutu
        topLayout.addLayout(leftLayout)
        topLayout.addLayout(centerLayout)
        topLayout.addLayout(rightLayout)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(topLayout)

    def prepareOpenFileButton(self):
        # tlačítko
        openFileButton = QtGui.QPushButton("Open file...", self)
        openFileButton.resize(openFileButton.sizeHint())

        # navázání akce na signál
        openFileButton.clicked.connect(self.showOpenFileDialog)
        return openFileButton

    def prepareMessageBoxButton(self):
        # tlačítko
        messageBoxButton = QtGui.QPushButton("Message Box", self)
        messageBoxButton.resize(messageBoxButton.sizeHint())

        # navázání akce na signál
        messageBoxButton.clicked.connect(self.showCustomMessageBox)
        return messageBoxButton

    def prepareLineEdit(self):
        # jednořádkové vstupní textové pole
        lineEdit = QtGui.QLineEdit(self)
        # naplnění textového pole textem
        lineEdit.setText(u"příliš žluťoučký kůň úpěl ďábelské ódy")
        return lineEdit

    def prepareTextEdit(self):
        # víceřádkové vstupní textové pole
        textEdit = QtGui.QTextEdit(self)

        # nastavení základních vlastností textového pole
        textEdit.setAcceptRichText(False)
        textEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)

        # vložení obsahu souboru do víceřádkového textového pole
        with open("01_empty_window.py", "r") as fin:
            content = fin.read().decode("utf8")
            textEdit.insertPlainText(content)

        return textEdit

    def prepareColorDialogButton(self):
        # tlačítko s popisem
        colorDialogButton = QtGui.QPushButton("Select color", self)
        colorDialogButton.resize(colorDialogButton.sizeHint())

        # navázání akce na signál
        colorDialogButton.clicked.connect(self.showColorDialog)
        return colorDialogButton

    def prepareQuitButton(self):
        # tlačítko s popisem
        quitButton = QtGui.QPushButton("Quit", self)
        quitButton.resize(quitButton.sizeHint())

        # navázání akce na signál
        quitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        return quitButton

    def showOpenFileDialog(self):
        # handler po stlačení tlačítka "Open file..."
        fileName = QtGui.QFileDialog.getOpenFileName(self, "Open file", u".")

        self.showMessageBox(u"Vybraný soubor\n{f}".format(f=fileName))

    def showColorDialog(self):
        # handler po stlačení tlačítka "Select color"
        colorDialog = QtGui.QColorDialog()
        colorDialog.setCurrentColor(QtGui.QColor("#aabbcc"))
        result = colorDialog.exec_()

        selected = colorDialog.selectedColor()
        message = "Selected color: {r} {g} {b}\nClicked on: {c}".format(
            r=selected.red(),
            g=selected.green(),
            b=selected.blue(),
            c="Ok" if result == 1 else "Cancel",
        )

        self.showMessageBox(message)

    def showMessageBox(self, text):
        msgBox = QtGui.QMessageBox()
        msgBox.setText(text)
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.exec_()

    def showCustomMessageBox(self):
        # handler po stlačení tlačítka "Message Box"
        # vytvoření dialogu
        msgBox = QtGui.QMessageBox()

        # nastavení zprávy a ikony, která se má zobrazit vedle zprávy
        msgBox.setText(u"Zpráva")
        msgBox.setIcon(QtGui.QMessageBox.Critical)

        # nastavení tlačítek, které mají být součástí dialogu
        msgBox.addButton("Help", QtGui.QMessageBox.HelpRole)
        msgBox.addButton("Accept", QtGui.QMessageBox.AcceptRole)
        msgBox.addButton("Reject", QtGui.QMessageBox.RejectRole)

        # zobrazení dialogu
        msgBox.exec_()

    def prepareTree(self):
        # vytvoření stromu
        tree = QtGui.QTreeWidget(self)
        tree.setHeaderLabel("strom")
        tree.setColumnCount(1)

        # naplnění stromu daty
        items = []
        for i in range(1, 11):
            item = QtGui.QTreeWidgetItem(None, ["prvek #{i}".format(i=i)])
            items.append(item)
            QtGui.QTreeWidgetItem(item, ["podprvek A"])
            QtGui.QTreeWidgetItem(item, ["podprvek B"])
            QtGui.QTreeWidgetItem(item, ["podprvek C"])
        tree.insertTopLevelItems(0, items)

        # po vložení všech prvků do stromu je můžeme rozbalit
        skip = False
        for item in items:
            if not skip:
                item.setExpanded(True)
            skip = not skip

        return tree

    def prepareSlider(self):
        # vytvoření slideru
        slider = QtGui.QSlider(QtCore.Qt.Horizontal)

        return slider

    def prepareDial(self):
        # vytvoření widgetu
        dial = QtGui.QDial()

        return dial


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
        self.setWindowTitle("Styles")

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
