#!/usr/bin/env python

import math
import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore, QtGui


# vytvoření štětce z pixmapy
def createBrushFromPixmap(filename):
    pixmap = QtGui.QPixmap(filename)
    return QtGui.QBrush(pixmap)


# vytvoření štětce z gradientního přechodu
def createBrushFromLinearGradient(color1, color2):
    gradient = QtGui.QLinearGradient(100, 100, 100, 140)
    gradient.setColorAt(0.2, QtGui.QColor(*color1))
    gradient.setColorAt(1.0, QtGui.QColor(*color2))
    gradient.setSpread(QtGui.QGradient.Spread.ReflectSpread)
    return QtGui.QBrush(gradient)


# vytvoření štětce z gradientního přechodu
def createBrushFromRadialGradient(color1, color2):
    gradient = QtGui.QRadialGradient(225, 200, 10)
    gradient.setColorAt(0.2, QtGui.QColor(*color1))
    gradient.setColorAt(1.0, QtGui.QColor(*color2))
    gradient.setSpread(QtGui.QGradient.Spread.ReflectSpread)
    return QtGui.QBrush(gradient)


# nastavení barvy kreslení (pera) na zadanou barvu
def setColor(qPainter, color):
    # vytvoření pera a nastavení barvy kreslení
    pen = QtGui.QPen(QtGui.QColor(*color))

    # kreslit se bude právě vytvořeným perem
    qPainter.setPen(pen)


# vytvoření cesty složené z kvadratických křivek
def createPath1():
    path = QtGui.QPainterPath()
    path.moveTo(10, 100)
    path.quadTo(50, 10, 90, 100)
    path.quadTo(130, 190, 170, 100)
    path.quadTo(210, 10, 250, 100)
    path.quadTo(290, 190, 330, 100)
    return path


# vytvoření cesty z kubických křivek
def createPath2():
    path = QtGui.QPainterPath()
    path.moveTo(10, 250)
    path.cubicTo(120, 100, -20, 100, 90, 250)
    return path


# vytvoření cesty z kubických křivek
def createPath3():
    path = QtGui.QPainterPath()
    path.moveTo(150, 200)
    path.cubicTo(225, 50, 225, 350, 300, 200)
    return path


# funkce pro vykreslení cesty zadanou barvou a stylem štětce
def drawPath(qPainter, color, brush, path):
    # nastavení barvy
    setColor(qPainter, color)

    # nastavení stylu štětce
    qPainter.setBrush(brush)

    # vykreslení cesty
    qPainter.drawPath(path)


# nový widget bude odvozen od obecného hlavního okna
class MainWindow(QtGui.QMainWindow):

    # rozměry rastrového obrázku
    IMAGE_WIDTH = 340
    IMAGE_HEIGHT = 300

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

        # vytvoření štětců
        brush1 = createBrushFromLinearGradient(WHITE, BLUE)
        brush2 = createBrushFromPixmap("pixmaps/voronoi.png")
        brush3 = createBrushFromRadialGradient(YELLOW, BLACK)

        # vytvoření cesty
        path1 = createPath1()

        # vykreslení cesty
        drawPath(qp, GREEN, brush1, path1)

        # vytvoření cesty
        path2 = createPath2()

        # vykreslení cesty
        drawPath(qp, YELLOW, brush2, path2)

        # vytvoření cesty
        path3 = createPath3()

        # vykreslení cesty
        drawPath(qp, MAGENTA, brush3, path3)

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
