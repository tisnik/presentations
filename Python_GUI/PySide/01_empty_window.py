#!/usr/bin/env python
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2017  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

# tento import je zapotřebí kvůli nutnosti zpracování parametrů
# předávaných přes příkazový řádek
import sys

# prozatím budeme využívat jen modul QtGui
import PySide.QtGui

# konstrukce výchozího tzv. aplikačního objektu
app = PySide.QtGui.QApplication(sys.argv)

# konstrukce obecného widgetu bez předka
window = PySide.QtGui.QWidget()

# zobrazení widgetu na obrazovce
window.show()

# vstup do smyčky událostí (event loop)
app.exec_()

# do tohoto místa se program dostane až po uzavření hlavního okna
print("Finishing")
