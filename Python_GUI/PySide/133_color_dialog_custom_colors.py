#!/usr/bin/env python

import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore, QtGui


# funkce pro vykreslení obdélníku zadanou barvou
def drawRectangleUsingBrush(qPainter, color, x, y, width, height):
    # změna barvy štětce
    brush = QtGui.QBrush(QtGui.QColor(color))
    brush.setStyle(QtCore.Qt.SolidPattern)
    qPainter.setBrush(brush)

    # vykreslení obdélníku
    qPainter.drawRect(x, y, width, height)


# nový widget bude odvozen od obecného widgetu
class MainWindowContent(QtGui.QWidget):

    # rozměry rastrového obrázku
    IMAGE_WIDTH = 330
    IMAGE_HEIGHT = 90

    SQUARE_SIZE = 30

    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindowContent, self).__init__()

        self.prepareImage()
        self.redrawColorBoxes()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareImage(self):
        # vytvoření instance třídy QImage
        self.image = QtGui.QImage(
            MainWindowContent.IMAGE_WIDTH,
            MainWindowContent.IMAGE_HEIGHT,
            QtGui.QImage.Format_RGB32,
        )
        # vymazání obrázku
        self.image.fill(0)

    def redrawColorBoxes(self):
        # vytvoření objektu typu QPainter s předáním
        # reference na "pokreslovaný" objekt
        qp = QtGui.QPainter(self.image)

        # vykreslení čtverců s barvami získanými z dialogu
        index = 0
        for row in range(0, 2):
            for column in range(0, 8):
                color = QtGui.QColorDialog.customColor(index)
                x = 10 + column * (MainWindowContent.SQUARE_SIZE + 10)
                y = 10 + row * (MainWindowContent.SQUARE_SIZE + 10)
                drawRectangleUsingBrush(
                    qp,
                    color,
                    x,
                    y,
                    MainWindowContent.SQUARE_SIZE,
                    MainWindowContent.SQUARE_SIZE,
                )
                index += 1

        # vytvoření instance třídy QPixmap z objektu QImage
        self.pixmap = QtGui.QPixmap.fromImage(self.image)

    def prepareGUI(self):
        quitButton = self.prepareQuitButton()
        colorDialogButton = self.prepareColorDialogButton()

        # vytvoření správce geometrie
        topLayout = QtGui.QVBoxLayout()

        # vytvoření návěští
        self.colorPalette = QtGui.QLabel("test")
        # přiřazení rastrového obrázku k návěští
        self.colorPalette.setPixmap(self.pixmap)

        # umístění widgetů do okna
        topLayout.addWidget(self.colorPalette)
        topLayout.addWidget(colorDialogButton)
        topLayout.addWidget(quitButton)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(topLayout)

    def prepareColorDialogButton(self):
        # tlačítko
        colorDialogButton = QtGui.QPushButton("Select color", self)
        colorDialogButton.resize(colorDialogButton.sizeHint())

        # navázání akce na signál
        colorDialogButton.clicked.connect(self.showColorDialog)
        return colorDialogButton

    def prepareQuitButton(self):
        # tlačítko
        quitButton = QtGui.QPushButton("Quit", self)
        quitButton.resize(quitButton.sizeHint())

        # navázání akce na signál
        quitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        return quitButton

    def showColorDialog(self):
        colorDialog = QtGui.QColorDialog()
        colorDialog.setCurrentColor(QtGui.QColor("#aabbcc"))
        result = colorDialog.exec_()
        self.redrawColorBoxes()
        self.colorPalette.setPixmap(self.pixmap)


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
        self.setWindowTitle("QColorDialog colors")

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
