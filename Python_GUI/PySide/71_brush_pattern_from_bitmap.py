#!/usr/bin/env python

import sys
import math

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore
from PySide import QtGui


# vytvoření štětce z bitmapy
def createBrushFromBitmap(color, filename):
    bitmap = QtGui.QBitmap(filename)
    c = QtGui.QColor(*color)
    return QtGui.QBrush(c, bitmap)


# funkce pro vykreslení obdélníku zadanou barvou a se specifikovaným štětcem
def drawRectangleUsingCustomBrush(
    qPainter, color, x, y, width, height, brush, pen_width=0
):
    # vytvoření pera a nastavení barvy kreslení
    pen = QtGui.QPen(QtGui.QColor(*color))

    # změna šířky pera
    pen.setWidth(pen_width)
    qPainter.setPen(pen)

    # změna tvaru štětce
    qPainter.setBrush(brush)

    # vykreslení obdélníku
    qPainter.drawRect(x, y, width, height)


# nový widget bude odvozen od obecného hlavního okna
class MainWindow(QtGui.QMainWindow):

    # rozměry rastrového obrázku
    IMAGE_WIDTH = 330
    IMAGE_HEIGHT = 240

    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindow, self).__init__()

        self.prepareImage()
        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareImage(self):
        # vytvoření instance třídy QImage
        self.image = QtGui.QImage(
            MainWindow.IMAGE_WIDTH, MainWindow.IMAGE_HEIGHT, QtGui.QImage.Format_RGB32
        )

        # vymazání obrázku
        self.image.fill(0)

        # vytvoření objektu typu QPainter s předáním
        # reference na "pokreslovaný" objekt
        qp = QtGui.QPainter(self.image)

        # konstanty s n-ticemi představujícími základní barvy
        BLACK = (0, 0, 0)
        BLUE = (0, 0, 255)
        CYAN = (0, 255, 255)
        GREEN = (0, 255, 0)
        YELLOW = (255, 255, 0)
        RED = (255, 0, 0)
        MAGENTA = (255, 0, 255)
        WHITE = (255, 255, 255)

        brush = createBrushFromBitmap(WHITE, "bitmaps/test.xbm")

        # Vykreslení obdélníků různým stylem
        drawRectangleUsingCustomBrush(qp, YELLOW, 10, 10, 70, 70, brush)
        drawRectangleUsingCustomBrush(qp, RED, 90, 10, 70, 70, brush)
        drawRectangleUsingCustomBrush(qp, BLUE, 170, 10, 70, 70, brush)
        drawRectangleUsingCustomBrush(qp, MAGENTA, 250, 10, 70, 70, brush)

        drawRectangleUsingCustomBrush(qp, WHITE, 10, 90, 70, 70, brush)
        drawRectangleUsingCustomBrush(qp, WHITE, 90, 90, 70, 70, brush)
        drawRectangleUsingCustomBrush(qp, WHITE, 170, 90, 70, 70, brush)
        drawRectangleUsingCustomBrush(qp, WHITE, 250, 90, 70, 70, brush)

        drawRectangleUsingCustomBrush(qp, BLACK, 10, 170, 70, 70, brush)
        drawRectangleUsingCustomBrush(qp, BLACK, 90, 170, 70, 70, brush)
        drawRectangleUsingCustomBrush(qp, BLACK, 170, 170, 70, 70, brush)
        drawRectangleUsingCustomBrush(qp, BLACK, 250, 170, 70, 70, brush)

        # vytvoření instance třídy QPixmap z objektu QImage
        self.pixmap = QtGui.QPixmap.fromImage(self.image)

    def prepareGUI(self):
        # velikost okna nezadávejte ručně - špatně se počítá kvůli toolbaru
        # self.resize(256, 300)
        self.setWindowTitle("QPainter")

        # tlačítko Quit
        quitAction = QtGui.QAction(
            QtGui.QIcon("icons/application-exit.png"), "&Quit", self
        )
        quitAction.triggered.connect(self.close)
        quitAction.setStatusTip("Quit the application")
        quitAction.setShortcut("Ctrl+Q")

        # nástrojový pruh
        self.toolbar = self.addToolBar("title")
        self.toolbar.setMovable(False)

        # přidání tlačítka na nástrojový pruh
        self.toolbar.addAction(quitAction)

        # doprostřed okna přidáme návěští s rastrovým obrázkem
        self.addLabelWithPixmap()

        # zobrazení hlavního okna
        self.show()

    def addLabelWithPixmap(self):
        # vytvoření návěští
        label = QtGui.QLabel("test")
        # přiřazení rastrového obrázku k návěští
        label.setPixmap(self.pixmap)
        # vložení návěští do hlavního okna
        self.setCentralWidget(label)

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
