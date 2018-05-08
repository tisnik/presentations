#!/usr/bin/env python
# vim: set fileencoding=utf-8

from PySide import QtSvg

# vytvoření instance třídy QSvgGenerator
generator = QtSvg.QSvgGenerator()

# určení typu výstupu a nastavení
# jména výsledného souboru
generator.setFileName("test1.svg")
