#!/usr/bin/env python

import sys
from PySide import QtCore, QtGui, QtSvg


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


def drawScene(painter, width, height):
    # konstanty s n-ticemi představujícími základní barvy
    WHITE = (255, 255, 255)

    # okraje
    drawRectangle(painter, WHITE, 0, 0, width, height)

    image = QtGui.QImage("pixmaps/pysidelogo.png")

    rect1 = QtCore.QRectF(10, 10, 199, 102)
    painter.drawImage(rect1, image)

    rect2 = QtCore.QRectF(10, 120, 199 * 3, 102 * 3)
    painter.drawImage(rect2, image)


def create_svg(name, width, height):
    VBOX_WIDTH = 600
    VBOX_HEIGHT = 440

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
    generator.setTitle("SVG: test 10")

    # popis SVG obrázku
    generator.setDescription("eight SVG example")

    # inicializace instance třídy QPainter
    painter = QtGui.QPainter()

    # začátek kreslení
    painter.begin(generator)

    drawScene(painter, VBOX_WIDTH, VBOX_HEIGHT)

    # konec kreslení
    painter.end()


def main():
    create_svg("test10.svg", 320, 320)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main()
