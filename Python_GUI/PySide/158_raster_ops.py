#!/usr/bin/env python

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

    BLUE_50_ALPHA = (0, 0, 255, 128)
    GREEN_50_ALPHA = (0, 255, 0, 128)

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
        painter,
        GREEN_50_ALPHA,
        BLUE_50_ALPHA,
        COLUMN_1,
        ROW_1,
        QtGui.QPainter.CompositionMode_SourceOver,
    )

    twoOverlappingSquares(
        painter,
        GREEN_50_ALPHA,
        BLUE_50_ALPHA,
        COLUMN_1,
        ROW_2,
        QtGui.QPainter.RasterOp_SourceOrDestination,
    )

    twoOverlappingSquares(
        painter,
        GREEN_50_ALPHA,
        BLUE_50_ALPHA,
        COLUMN_2,
        ROW_2,
        QtGui.QPainter.RasterOp_SourceAndDestination,
    )

    twoOverlappingSquares(
        painter,
        GREEN_50_ALPHA,
        BLUE_50_ALPHA,
        COLUMN_3,
        ROW_2,
        QtGui.QPainter.RasterOp_SourceXorDestination,
    )

    twoOverlappingSquares(
        painter,
        GREEN_50_ALPHA,
        BLUE_50_ALPHA,
        COLUMN_1,
        ROW_3,
        QtGui.QPainter.RasterOp_NotSourceAndNotDestination,
    )

    twoOverlappingSquares(
        painter,
        GREEN_50_ALPHA,
        BLUE_50_ALPHA,
        COLUMN_2,
        ROW_3,
        QtGui.QPainter.RasterOp_NotSourceOrNotDestination,
    )

    twoOverlappingSquares(
        painter,
        GREEN_50_ALPHA,
        BLUE_50_ALPHA,
        COLUMN_3,
        ROW_3,
        QtGui.QPainter.RasterOp_NotSourceXorDestination,
    )

    twoOverlappingSquares(
        painter,
        GREEN_50_ALPHA,
        BLUE_50_ALPHA,
        COLUMN_1,
        ROW_4,
        QtGui.QPainter.RasterOp_NotSource,
    )

    twoOverlappingSquares(
        painter,
        GREEN_50_ALPHA,
        BLUE_50_ALPHA,
        COLUMN_2,
        ROW_4,
        QtGui.QPainter.RasterOp_NotSourceAndDestination,
    )

    twoOverlappingSquares(
        painter,
        GREEN_50_ALPHA,
        BLUE_50_ALPHA,
        COLUMN_3,
        ROW_4,
        QtGui.QPainter.RasterOp_SourceAndNotDestination,
    )


def create_svg(name, width, height):
    VBOX_WIDTH = 600
    VBOX_HEIGHT = 800
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
    generator.setTitle("SVG: test 9")

    # popis SVG obrázku
    generator.setDescription("seventh SVG example")

    # inicializace instance třídy QPainter
    painter = QtGui.QPainter()

    # začátek kreslení
    painter.begin(generator)

    drawScene(painter, VBOX_WIDTH, VBOX_HEIGHT)

    # konec kreslení
    painter.end()


def main():
    create_svg("test9.svg", 320, 320)


if __name__ == "__main__":
    main()
