#!/usr/bin/env python

from PySide import QtCore, QtGui, QtSvg


# nastavení barvy kreslení (pera) na zadanou barvu
def setColor(qPainter, color):
    # vytvoření pera a nastavení barvy kreslení
    pen = QtGui.QPen(QtGui.QColor(*color))

    # kreslit se bude právě vytvořeným perem
    qPainter.setPen(pen)


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


def drawScene(painter, width, height):
    # konstanty s n-ticemi představujícími základní barvy
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    CYAN = (0, 255, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    MAGENTA = (255, 0, 255)
    WHITE = (255, 255, 255)

    # okraje
    drawRectangle(painter, WHITE, 0, 0, width, height)

    # Vykreslení různých 2D entit
    drawLine(painter, GREEN, 10, 10, 80, 80)

    drawRectangle(painter, YELLOW, 10, 90, 70, 70)
    drawCircle(painter, RED, 125, 125, 35)
    drawEllipse(painter, CYAN, 170, 30 + 80, 70, 35)
    drawEllipse(painter, BLUE, 268, 10 + 80, 35, 70)

    drawRoundedRectangle(painter, MAGENTA, 10, 170, 70, 70, 1)
    drawRoundedRectangle(painter, MAGENTA, 90, 170, 70, 70, 10)
    drawRoundedRectangle(painter, MAGENTA, 170, 170, 70, 70, 20)
    drawRoundedRectangle(painter, MAGENTA, 250, 170, 70, 70, 1000)

    drawArc(painter, CYAN, 10 + 35, 260 + 35, 35, 0, 90)
    drawArc(painter, CYAN, 90 + 35, 260 + 35, 35, 45, 90)
    drawArc(painter, CYAN, 170 + 35, 260 + 35, 35, 45, 180)
    drawArc(painter, CYAN, 250 + 35, 260 + 35, 35, 45, 270)

    drawPie(painter, YELLOW, 10 + 35, 350 + 35, 35, 0, 90)
    drawPie(painter, YELLOW, 90 + 35, 350 + 35, 35, 45, 90)
    drawPie(painter, YELLOW, 170 + 35, 350 + 35, 35, 45, 180)
    drawPie(painter, YELLOW, 250 + 35, 350 + 35, 35, 45, 270)

    drawChord(painter, GREEN, 10 + 35, 440 + 35, 35, 0, 90)
    drawChord(painter, GREEN, 90 + 35, 440 + 35, 35, 45, 90)
    drawChord(painter, GREEN, 170 + 35, 440 + 35, 35, 45, 180)
    drawChord(painter, GREEN, 250 + 35, 440 + 35, 35, 45, 270)


def create_svg(name, width, height):
    VBOX_WIDTH = 330
    VBOX_HEIGHT = 520

    # vytvoření instance třídy QSvgGenerator
    generator = QtSvg.QSvgGenerator()

    # určení typu výstupu a nastavení
    # jména výsledného souboru
    generator.setFileName(name)

    # specifikace rozměrů SVG obrázku
    generator.setSize(QtCore.QSize(width, height))

    # viditelný výřez
    generator.setViewBox(QtCore.QRect(0, 0, VBOX_WIDTH, VBOX_HEIGHT))

    # nastavení titulku SVG obrázku
    generator.setTitle("SVG: test 7")

    # popis SVG obrázku
    generator.setDescription("fifth SVG example")

    # inicializace instance třídy QPainter
    painter = QtGui.QPainter()

    # začátek kreslení
    painter.begin(generator)

    drawScene(painter, VBOX_WIDTH, VBOX_HEIGHT)

    # konec kreslení
    painter.end()


def main():
    create_svg("test7.svg", 320, 320)


if __name__ == "__main__":
    main()
