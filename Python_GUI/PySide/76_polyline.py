#!/usr/bin/env python

import sys
import math

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore
from PySide import QtGui


# nastavení barvy kreslení (pera) na zadanou barvu
def setColor(qPainter, color):
    # vytvoření pera a nastavení barvy kreslení
    pen = QtGui.QPen(QtGui.QColor(*color))

    # kreslit se bude právě vytvořeným perem
    qPainter.setPen(pen)


# vytvoření polygonu ze sekvence koordinát [x,y]
def createPolygon(coordinatesSequence):
    polygon = QtGui.QPolygon()
    for coordinates in coordinatesSequence:
        p = QtCore.QPoint(coordinates[0], coordinates[1])
        polygon.append(p)
    return polygon


# funkce pro vykreslení lomené čáry zadanou barvou
def drawPolyline(qPainter, color, polygon):
    setColor(qPainter, color)

    # vykreslení lomené čáry
    qPainter.drawPolyline(polygon)


# nový widget bude odvozen od obecného hlavního okna
class MainWindow(QtGui.QMainWindow):

    # rozměry rastrového obrázku
    IMAGE_WIDTH = 300
    IMAGE_HEIGHT = 250

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

        # Vykreslení různých 2D entit
        polygon = createPolygon(
            [
                [100, 200],
                [200, 200],
                [100, 100],
                [100, 200],
                [200, 100],
                [100, 100],
                [150, 50],
                [200, 100],
                [200, 200],
            ]
        )
        drawPolyline(qp, YELLOW, polygon)

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
