#!/usr/bin/env python

import math
import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore, QtGui


# funkce pro vykreslení obdélníku zadanou barvou a se specifikovaným štětcem
def drawRectangleUsingBrush(
    qPainter, color, x, y, width, height, brush_style, pen_width=0
):
    # vytvoření pera a nastavení barvy kreslení
    pen = QtGui.QPen(QtGui.QColor(*color))

    # změna šířky pera
    pen.setWidth(pen_width)
    qPainter.setPen(pen)

    # změna tvaru štětce
    brush = QtGui.QBrush(QtGui.QColor(*color))
    brush.setStyle(brush_style)
    qPainter.setBrush(brush)

    # vykreslení obdélníku
    qPainter.drawRect(x, y, width, height)


def twoOverlappingSquares(qPainter, color1, color2, x, y, compositionMode):
    # nastavení výchozího režimu míchání barev
    qPainter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceOver)

    # první čtverec
    drawRectangleUsingBrush(qPainter, color1, x, y, 100, 100, QtCore.Qt.SolidPattern)

    # nastavení režimu míchání barev
    qPainter.setCompositionMode(compositionMode)

    # druhý čtverec
    drawRectangleUsingBrush(
        qPainter, color2, x + 50, y + 50, 100, 100, QtCore.Qt.SolidPattern
    )


# nový widget bude odvozen od obecného hlavního okna
class MainWindow(QtGui.QMainWindow):

    # rozměry rastrového obrázku
    IMAGE_WIDTH = 600
    IMAGE_HEIGHT = 800

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

        # vykreslení sady překrývajících se čtverců
        self.drawOverlappingSquares(qp)

        # vytvoření instance třídy QPixmap z objektu QImage
        self.pixmap = QtGui.QPixmap.fromImage(self.image)

    def drawOverlappingSquares(self, qPainter):
        # konstanty s n-ticemi představujícími základní barvy
        BLACK = (0, 0, 0)
        BLUE = (0, 0, 255)
        CYAN = (0, 255, 255)
        GREEN = (0, 255, 0)
        YELLOW = (255, 255, 0)
        RED = (255, 0, 0)
        MAGENTA = (255, 0, 255)
        WHITE = (255, 255, 255)

        # umístění čtverců na kreslicí ploše
        HORIZONTAL_DISTANCE = 200
        VERTICAL_DISTANCE = 200

        COLUMN_1 = 10
        COLUMN_2 = COLUMN_1 + HORIZONTAL_DISTANCE
        COLUMN_3 = COLUMN_2 + HORIZONTAL_DISTANCE

        ROW_1 = 10
        ROW_2 = ROW_1 + HORIZONTAL_DISTANCE
        ROW_3 = ROW_2 + HORIZONTAL_DISTANCE
        ROW_4 = ROW_3 + HORIZONTAL_DISTANCE

        # vykreslení sady překrývajících se čtverců
        twoOverlappingSquares(
            qPainter,
            GREEN,
            BLUE,
            COLUMN_1,
            ROW_1,
            QtGui.QPainter.CompositionMode_SourceOver,
        )

        twoOverlappingSquares(
            qPainter,
            GREEN,
            BLUE,
            COLUMN_1,
            ROW_2,
            QtGui.QPainter.RasterOp_SourceOrDestination,
        )

        twoOverlappingSquares(
            qPainter,
            GREEN,
            BLUE,
            COLUMN_2,
            ROW_2,
            QtGui.QPainter.RasterOp_SourceAndDestination,
        )

        twoOverlappingSquares(
            qPainter,
            GREEN,
            BLUE,
            COLUMN_3,
            ROW_2,
            QtGui.QPainter.RasterOp_SourceXorDestination,
        )

        twoOverlappingSquares(
            qPainter,
            GREEN,
            BLUE,
            COLUMN_1,
            ROW_3,
            QtGui.QPainter.RasterOp_NotSourceAndNotDestination,
        )

        twoOverlappingSquares(
            qPainter,
            GREEN,
            BLUE,
            COLUMN_2,
            ROW_3,
            QtGui.QPainter.RasterOp_NotSourceOrNotDestination,
        )

        twoOverlappingSquares(
            qPainter,
            GREEN,
            BLUE,
            COLUMN_3,
            ROW_3,
            QtGui.QPainter.RasterOp_NotSourceXorDestination,
        )

        twoOverlappingSquares(
            qPainter, GREEN, BLUE, COLUMN_1, ROW_4, QtGui.QPainter.RasterOp_NotSource
        )

        twoOverlappingSquares(
            qPainter,
            GREEN,
            BLUE,
            COLUMN_2,
            ROW_4,
            QtGui.QPainter.RasterOp_NotSourceAndDestination,
        )

        twoOverlappingSquares(
            qPainter,
            GREEN,
            BLUE,
            COLUMN_3,
            ROW_4,
            QtGui.QPainter.RasterOp_SourceAndNotDestination,
        )

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
