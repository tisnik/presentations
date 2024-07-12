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


# nový widget bude odvozen od obecného hlavního okna
class MainWindow(QtGui.QMainWindow):

    # rozměry rastrového obrázku
    IMAGE_WIDTH = 440
    IMAGE_HEIGHT = 140

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

        # nastavení oblasti omezující vykreslování
        region = QtGui.QRegion(
            QtCore.QRect(
                20, 20, MainWindow.IMAGE_WIDTH - 40, MainWindow.IMAGE_HEIGHT - 50
            )
        )
        qp.setClipRegion(region)

        # vykreslení obdélníků různým stylem
        drawRectangleUsingBrush(qp, YELLOW, 10, 10, 50, 50, QtCore.Qt.SolidPattern)
        drawRectangleUsingBrush(qp, YELLOW, 70, 10, 50, 50, QtCore.Qt.HorPattern)
        drawRectangleUsingBrush(qp, YELLOW, 130, 10, 50, 50, QtCore.Qt.VerPattern)
        drawRectangleUsingBrush(qp, YELLOW, 190, 10, 50, 50, QtCore.Qt.CrossPattern)
        drawRectangleUsingBrush(qp, YELLOW, 250, 10, 50, 50, QtCore.Qt.BDiagPattern)
        drawRectangleUsingBrush(qp, YELLOW, 310, 10, 50, 50, QtCore.Qt.FDiagPattern)
        drawRectangleUsingBrush(qp, YELLOW, 370, 10, 50, 50, QtCore.Qt.DiagCrossPattern)

        drawRectangleUsingBrush(qp, WHITE, 10, 70, 50, 50, QtCore.Qt.Dense1Pattern)
        drawRectangleUsingBrush(qp, WHITE, 70, 70, 50, 50, QtCore.Qt.Dense2Pattern)
        drawRectangleUsingBrush(qp, WHITE, 130, 70, 50, 50, QtCore.Qt.Dense3Pattern)
        drawRectangleUsingBrush(qp, WHITE, 190, 70, 50, 50, QtCore.Qt.Dense4Pattern)
        drawRectangleUsingBrush(qp, WHITE, 250, 70, 50, 50, QtCore.Qt.Dense5Pattern)
        drawRectangleUsingBrush(qp, WHITE, 310, 70, 50, 50, QtCore.Qt.Dense6Pattern)
        drawRectangleUsingBrush(qp, WHITE, 370, 70, 50, 50, QtCore.Qt.Dense7Pattern)

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
