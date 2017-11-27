#!/usr/bin/env python
# vim: set fileencoding=utf-8

import sys

# prozatím budeme využívat jen modul QtGui
from PySide.QtGui import *

# konstrukce výchozího tzv. aplikačního objektu
app = QApplication(sys.argv)

# konstrukce návěští bez předka
label = QLabel('Hello world!')

# zobrazení widgetu na obrazovce
label.show()

# vstup do smyčky událostí (event loop)
sys.exit(app.exec_())
