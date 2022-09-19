# vim: set fileencoding=utf-8

#
#  (C) Copyright Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import sys

# zajisteni importu noveho rozhrani
import sip

sip.setapi("QDate", 2)
sip.setapi("QDateTime", 2)
sip.setapi("QString", 2)
sip.setapi("QTextStream", 2)
sip.setapi("QTime", 2)
sip.setapi("QUrl", 2)
sip.setapi("QVariant", 2)

from PyQt4.Qt import *

qt_application = QApplication(sys.argv)

label = QLabel("Hello world!")

label.show()

qt_application.exec_()
