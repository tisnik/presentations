#!/usr/bin/env python
# vim: set fileencoding=utf-8

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
