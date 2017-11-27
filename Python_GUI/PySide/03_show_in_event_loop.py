#!/usr/bin/env python
# vim: set fileencoding=utf-8

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
