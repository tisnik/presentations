#!/usr/bin/env python

#
#  (C) Copyright 2017, 2018  Pavel Tisnovsky
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
from PySide.QtGui import *

# konstrukce výchozího tzv. aplikačního objektu
app = QApplication(sys.argv)

# konstrukce obecného widgetu bez předka
window = QWidget()

# zobrazení widgetu na obrazovce
window.show()

# vstup do smyčky událostí (event loop)
sys.exit(app.exec_())

# do tohoto místa se program teoreticky dostane až PO uzavření
# hlavního okna, ve skutečnosti však skončí už na sys.exit()
print("Finishing")
