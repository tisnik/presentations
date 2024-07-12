#!/usr/bin/env python

import math
import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore, QtGui


# výpočet souřadnic n-tého vrcholu hvězdy
def starVertex(cx, cy, radius, n):
    angle = math.radians(n * 144)
    return cx + radius * math.sin(angle), cy - radius * math.cos(angle)


# vytvoření štětce z gradientního přechodu
def createBrushFromRadialGradient(color1, color2):
    gradient = QtGui.QRadialGradient(140, 140, 10)
    gradient.setColorAt(0.2, QtGui.QColor(*color1))
    gradient.setColorAt(1.0, QtGui.QColor(*color2))
    gradient.setSpread(QtGui.QGradient.Spread.ReflectSpread)
    return QtGui.QBrush(gradient)


# nastavení barvy kreslení (pera) na zadanou barvu
def setColor(qPainter, color):
    # vytvoření pera a nastavení barvy kreslení
    pen = QtGui.QPen(QtGui.QColor(*color))
    pen.setWidth(5)

    # kreslit se bude právě vytvořeným perem
    qPainter.setPen(pen)


# vytvoření cesty
def createPath():
    path = QtGui.QPainterPath()
    path.moveTo(*starVertex(140, 140, 120, 0))
    path.lineTo(*starVertex(140, 140, 120, 1))
    path.lineTo(*starVertex(140, 140, 120, 2))
    path.lineTo(*starVertex(140, 140, 120, 3))
    path.lineTo(*starVertex(140, 140, 120, 4))
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

        # vytvoření štětce
        brush = createBrushFromRadialGradient(BLUE, WHITE)

        # vytvoření cesty
        path = createPath()

        # vykreslení cesty
        drawPath(qp, WHITE, brush, path)

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
