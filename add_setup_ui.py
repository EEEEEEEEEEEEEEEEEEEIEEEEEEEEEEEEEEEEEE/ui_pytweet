# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_setup.ui'
#
# Created: Mon Jun 13 14:06:53 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore
from PyQt4 import QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(424, 399)
        self.label_username = QtGui.QLabel(Dialog)
        self.label_username.setGeometry(QtCore.QRect(30, 70, 131, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_username.setFont(font)
        self.label_username.setObjectName(_fromUtf8("label_username"))
        self.edit_email = QtGui.QLineEdit(Dialog)
        self.edit_email.setGeometry(QtCore.QRect(160, 70, 191, 27))
        self.edit_email.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.edit_email.setText(_fromUtf8(""))
        self.edit_email.setObjectName(_fromUtf8("edit_email"))
        self.label_password = QtGui.QLabel(Dialog)
        self.label_password.setGeometry(QtCore.QRect(80, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_password.setFont(font)
        self.label_password.setObjectName(_fromUtf8("label_password"))
        self.edit_password = QtGui.QLineEdit(Dialog)
        self.edit_password.setGeometry(QtCore.QRect(160, 100, 191, 27))
        self.edit_password.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.edit_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.edit_password.setText(_fromUtf8(""))
        self.edit_password.setEchoMode(QtGui.QLineEdit.Password)
        self.edit_password.setObjectName(_fromUtf8("edit_password"))
        self.label_setAcc = QtGui.QLabel(Dialog)
        self.label_setAcc.setGeometry(QtCore.QRect(150, 40, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_setAcc.setFont(font)
        self.label_setAcc.setObjectName(_fromUtf8("label_setAcc"))
        self.list_active_acc = QtGui.QTextBrowser(Dialog)
        self.list_active_acc.setGeometry(QtCore.QRect(20, 180, 381, 201))
        self.list_active_acc.setObjectName(_fromUtf8("list_active_acc"))
        self.push_setup = QtGui.QPushButton(Dialog)
        self.push_setup.setGeometry(QtCore.QRect(250, 140, 98, 27))
        self.push_setup.setObjectName(_fromUtf8("push_setup"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_username.setText(_translate("Dialog", "Username/Email :", None))
        self.label_password.setText(_translate("Dialog", "Password :", None))
        self.label_setAcc.setText(_translate("Dialog", "Setup Your Account", None))
        self.list_active_acc.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.push_setup.setText(_translate("Dialog", "Setup", None))