# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Tue May 15 20:52:00 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(271, 89)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.helloButton = QtGui.QPushButton(Form)
        self.helloButton.setDefault(True)
        self.helloButton.setObjectName("helloButton")
        self.verticalLayout.addWidget(self.helloButton)
        self.quitButton = QtGui.QPushButton(Form)
        self.quitButton.setObjectName("quitButton")
        self.verticalLayout.addWidget(self.quitButton)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QtGui.QApplication.translate(
                "Form", "Form", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.helloButton.setText(
            QtGui.QApplication.translate(
                "Form", "Hello!", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.quitButton.setText(
            QtGui.QApplication.translate(
                "Form", "Quit", None, QtGui.QApplication.UnicodeUTF8
            )
        )
