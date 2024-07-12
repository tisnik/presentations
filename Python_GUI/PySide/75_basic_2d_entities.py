#!/usr/bin/env python

import math
import random
import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore, QtGui


# nastavení barvy kreslení (pera) na zadanou barvu
def setColor(qPainter, color):
    # vytvoření pera a nastavení barvy kreslení
    pen = QtGui.QPen(QtGui.QColor(*color))

    # kreslit se bude právě vytvořeným perem
    qPainter.setPen(pen)


# funkce pro vykreslení bodu zadanou barvou
def drawPoint(qPainter, color, x, y):
    setColor(qPainter, color)

    # vykreslení jediného bodu
    qPainter.drawPoint(x, y)


# funkce pro vykreslení úsečky zadanou barvou
def drawLine(qPainter, color, x1, y1, x2, y2):
    setColor(qPainter, color)

    # vykreslení úsečky
    qPainter.drawLine(x1, y1, x2, y2)


# funkce pro vykreslení obdélníku zadanou barvou
def drawRectangle(qPainter, color, x, y, width, height):
    setColor(qPainter, color)

    # vykreslení obdélníku
    qPainter.drawRect(x, y, width, height)


# funkce pro vykreslení obdélníku zadanou barvou a se zaoblenými rohy
def drawRoundedRectangle(qPainter, color, x, y, width, height, r):
    setColor(qPainter, color)

    # vykreslení obdélníku
    qPainter.drawRoundedRect(x, y, width, height, r, r)


# funkce pro vykreslení elipsy zadanou barvou
def drawEllipse(qPainter, color, x, y, width, height):
    # vytvoření pera a nastavení barvy kreslení
    pen = QtGui.QPen(QtGui.QColor(*color))
    qPainter.setPen(pen)

    # vykreslení elipsy
    qPainter.drawEllipse(x, y, width, height)


# funkce pro vykreslení kružnice zadanou barvou
def drawCircle(qPainter, color, cx, cy, radius):
    setColor(qPainter, color)

    # vykreslení kružnice
    qPainter.drawEllipse(cx - radius, cy - radius, 2 * radius, 2 * radius)


# funkce pro vykreslení oblouku zadanou barvou
def drawArc(qPainter, color, cx, cy, radius, angle, span):
    setColor(qPainter, color)

    # vykreslení kružnice
    qPainter.drawArc(
        cx - radius, cy - radius, 2 * radius, 2 * radius, 16 * angle, 16 * span
    )


# funkce pro vykreslení kruhové výseče zadanou barvou
def drawPie(qPainter, color, cx, cy, radius, angle, span):
    setColor(qPainter, color)

    # vykreslení kruhové výseče
    qPainter.drawPie(
        cx - radius, cy - radius, 2 * radius, 2 * radius, 16 * angle, 16 * span
    )


# funkce pro vykreslení kruhové úseče zadanou barvou
def drawChord(qPainter, color, cx, cy, radius, angle, span):
    setColor(qPainter, color)

    # vykreslení kruhové úseče
    qPainter.drawChord(
        cx - radius, cy - radius, 2 * radius, 2 * radius, 16 * angle, 16 * span
    )


# nový widget bude odvozen od obecného hlavního okna
class MainWindow(QtGui.QMainWindow):

    # rozměry rastrového obrázku
    IMAGE_WIDTH = 330
    IMAGE_HEIGHT = 520

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
        drawLine(qp, GREEN, 10, 10, 80, 80)

        for _ in range(250):
            x = random.uniform(90, 160)
            y = random.uniform(10, 80)
            drawPoint(qp, WHITE, x, y)

        drawRectangle(qp, YELLOW, 10, 90, 70, 70)
        drawCircle(qp, RED, 125, 125, 35)
        drawEllipse(qp, CYAN, 170, 30 + 80, 70, 35)
        drawEllipse(qp, BLUE, 268, 10 + 80, 35, 70)

        drawRoundedRectangle(qp, MAGENTA, 10, 170, 70, 70, 1)
        drawRoundedRectangle(qp, MAGENTA, 90, 170, 70, 70, 10)
        drawRoundedRectangle(qp, MAGENTA, 170, 170, 70, 70, 20)
        drawRoundedRectangle(qp, MAGENTA, 250, 170, 70, 70, 1000)

        drawArc(qp, CYAN, 10 + 35, 260 + 35, 35, 0, 90)
        drawArc(qp, CYAN, 90 + 35, 260 + 35, 35, 45, 90)
        drawArc(qp, CYAN, 170 + 35, 260 + 35, 35, 45, 180)
        drawArc(qp, CYAN, 250 + 35, 260 + 35, 35, 45, 270)

        drawPie(qp, YELLOW, 10 + 35, 350 + 35, 35, 0, 90)
        drawPie(qp, YELLOW, 90 + 35, 350 + 35, 35, 45, 90)
        drawPie(qp, YELLOW, 170 + 35, 350 + 35, 35, 45, 180)
        drawPie(qp, YELLOW, 250 + 35, 350 + 35, 35, 45, 270)

        drawChord(qp, GREEN, 10 + 35, 440 + 35, 35, 0, 90)
        drawChord(qp, GREEN, 90 + 35, 440 + 35, 35, 45, 90)
        drawChord(qp, GREEN, 170 + 35, 440 + 35, 35, 45, 180)
        drawChord(qp, GREEN, 250 + 35, 440 + 35, 35, 45, 270)

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
