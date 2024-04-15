#!/usr/bin/env python

from PySide import QtCore, QtGui, QtSvg

# vytvoření instance třídy QSvgGenerator
generator = QtSvg.QSvgGenerator()

# určení typu výstupu a nastavení
# jména výsledného souboru
generator.setFileName("test3.svg")

# specifikace rozměrů SVG obrázku
generator.setSize(QtCore.QSize(320, 240))

# viditelný výřez
generator.setViewBox(QtCore.QRect(0, 0, 320, 240))

# nastavení titulku SVG obrázku
generator.setTitle("SVG: test 3")

# popis SVG obrázku
generator.setDescription("third SVG example")

# inicializace instance třídy QPainter
painter = QtGui.QPainter()

# začátek kreslení
painter.begin(generator)

# ihned poté ukončíme kreslení
painter.end()
