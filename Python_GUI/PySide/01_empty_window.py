#!/usr/bin/env python
# vim: set fileencoding=utf-8

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
