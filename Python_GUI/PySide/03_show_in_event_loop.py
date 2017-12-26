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
import time

# prozatím budeme využívat jen modul QtGui
from PySide.QtGui import *


def sleep(seconds):
    print('sleeping')

    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)

    print('waking up')


# konstrukce výchozího tzv. aplikačního objektu
app = QApplication(sys.argv)

# konstrukce obecného widgetu bez předka
window = QWidget()

print('before window.show()')

# zobrazení widgetu na obrazovce
window.show()

print('after window.show()')
sleep(5)


# vstup do smyčky událostí (event loop)
sys.exit(app.exec_())
