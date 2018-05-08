#!/usr/bin/env python
# vim: set fileencoding=utf-8

from PySide import QtGui, QtSvg

# vytvoření instance třídy QSvgGenerator
generator = QtSvg.QSvgGenerator()

# určení typu výstupu a nastavení
# jména výsledného souboru
generator.setFileName("test2.svg")

# inicializace instance třídy QPainter
painter = QtGui.QPainter()

# začátek kreslení
painter.begin(generator)

# ihned poté ukončíme kreslení
painter.end()
