#!/usr/bin/env python

import math
import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore, QtGui


# vytvoření štětce z pixmapy
def createBrushFromPixmap(filename):
    pixmap = QtGui.QPixmap(filename)
    return QtGui.QBrush(pixmap)


# nastavení barvy kreslení (pera) na zadanou barvu a šířku stopy
def setColorAndWidth(qPainter, color, width):
    # vytvoření pera a nastavení barvy kreslení
    pen = QtGui.QPen(QtGui.QColor(*color))
    pen.setWidth(width)

    # kreslit se bude právě vytvořeným perem
    qPainter.setPen(pen)


# vytvoření cesty složené z obdélníku
def createPath1():
    path = QtGui.QPainterPath()
    path.addRect(10, 10, 200, 200)
    return path


# vytvoření cesty složené z obdélníku
def createPath2():
    path = QtGui.QPainterPath()
    path.addRect(100, 100, 200, 200)
    return path


# funkce pro vykreslení cesty zadanou barvou a stylem štětce
def drawPath(qPainter, color, width, brush, path):
    # nastavení barvy
    setColorAndWidth(qPainter, color, width)

    # nastavení stylu štětce
    qPainter.setBrush(brush)

    # vykreslení cesty
    qPainter.drawPath(path)


# nový widget bude odvozen od obecného hlavního okna
class MainWindow(QtGui.QMainWindow):

    # rozměry rastrového obrázku
    IMAGE_WIDTH = 640
    IMAGE_HEIGHT = 640

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

        # vytvoření štětce
        brush = createBrushFromPixmap("pixmaps/voronoi.png")

        # vytvoření první cesty
        path1 = createPath1()

        # vytvoření druhé cesty
        path2 = createPath2()

        # SJEDNOCENÍ #

        # vykreslení kombinace obou cest
        drawPath(qp, RED, 4, brush, path1 | path2)

        # posun
        path1.translate(320, 0)
        path2.translate(320, 0)

        # ROZDÍL

        # vykreslení kombinace obou cest
        drawPath(qp, YELLOW, 4, brush, path1 - path2)

        # posun
        path1.translate(-320, 320)
        path2.translate(-320, 320)

        # PRŮNIK

        # vykreslení kombinace obou cest
        drawPath(qp, CYAN, 4, brush, path1 & path2)

        # posun
        path1.translate(320, 0)
        path2.translate(320, 0)

        # SYMETRICKÁ DIFERENCE

        # vykreslení kombinace obou cest
        drawPath(qp, MAGENTA, 4, brush, (path1 | path2) - (path1 & path2))
        # drawPath(qp, MAGENTA, 4, brush, path1.united(path2).subtracted(path1.intersected(path2)))

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
