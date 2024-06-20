#!/usr/bin/env python

from PySide import QtCore, QtGui, QtSvg

# konstanty s n-ticemi představujícími základní barvy
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)


# nastavení barvy kreslení (pera) na zadanou barvu
def setColor(qPainter, color):
    # vytvoření pera a nastavení barvy kreslení
    pen = QtGui.QPen(QtGui.QColor(*color))

    # kreslit se bude právě vytvořeným perem
    qPainter.setPen(pen)


# funkce pro vykreslení obdélníku zadanou barvou
def drawRectangle(qPainter, color, x, y, width, height):
    setColor(qPainter, color)

    # vykreslení obdélníku
    qPainter.drawRect(x, y, width, height)


def create_svg(name, width, height):
    VBOX_WIDTH = 100
    VBOX_HEIGHT = 100

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
    generator.setTitle("SVG: test 4")

    # popis SVG obrázku
    generator.setDescription("fourth SVG example")

    # inicializace instance třídy QPainter
    painter = QtGui.QPainter()

    # začátek kreslení
    painter.begin(generator)

    drawRectangle(painter, WHITE, 1, 1, VBOX_WIDTH - 1, VBOX_HEIGHT - 1)

    # konec kreslení
    painter.end()


def main():
    create_svg("test4.svg", 10, 10)
    create_svg("test5.svg", 100, 100)
    create_svg("test6.svg", 1000, 1000)


if __name__ == "__main__":
    main()
