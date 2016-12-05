# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Mon Jun 13 14:09:20 2016
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 491)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.main_window_widget = QtGui.QTabWidget(self.centralwidget)
        self.main_window_widget.setGeometry(QtCore.QRect(10, 20, 621, 421))
        self.main_window_widget.setObjectName(_fromUtf8("main_window_widget"))
        self.status = QtGui.QWidget()
        self.status.setObjectName(_fromUtf8("status"))
        self.Status_text = QtGui.QPlainTextEdit(self.status)
        self.Status_text.setGeometry(QtCore.QRect(10, 10, 341, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        self.Status_text.setFont(font)
        self.Status_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Status_text.setLocale(QtCore.QLocale(QtCore.QLocale.Indonesian, QtCore.QLocale.Indonesia))
        self.Status_text.setFrameShape(QtGui.QFrame.Panel)
        self.Status_text.setObjectName(_fromUtf8("Status_text"))
        self.Push_date_savelist = QtGui.QDateTimeEdit(self.status)
        self.Push_date_savelist.setGeometry(QtCore.QRect(10, 120, 141, 31))
        self.Push_date_savelist.setObjectName(_fromUtf8("Push_date_savelist"))
        self.Push_saveList = QtGui.QCommandLinkButton(self.status)
        self.Push_saveList.setGeometry(QtCore.QRect(150, 120, 98, 31))
        self.Push_saveList.setObjectName(_fromUtf8("Push_saveList"))
        self.Push_SendNow = QtGui.QCommandLinkButton(self.status)
        self.Push_SendNow.setGeometry(QtCore.QRect(250, 120, 98, 31))
        self.Push_SendNow.setObjectName(_fromUtf8("Push_SendNow"))
        self.list_tweet = QtGui.QTextBrowser(self.status)
        self.list_tweet.setGeometry(QtCore.QRect(10, 160, 341, 191))
        self.list_tweet.setObjectName(_fromUtf8("list_tweet"))
        self.push_export = QtGui.QCommandLinkButton(self.status)
        self.push_export.setGeometry(QtCore.QRect(180, 350, 81, 31))
        self.push_export.setObjectName(_fromUtf8("push_export"))
        self.push_import = QtGui.QCommandLinkButton(self.status)
        self.push_import.setGeometry(QtCore.QRect(270, 350, 81, 31))
        self.push_import.setObjectName(_fromUtf8("push_import"))
        self.progressBar = QtGui.QProgressBar(self.status)
        self.progressBar.setGeometry(QtCore.QRect(10, 360, 151, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.list_active_account = QtGui.QTextBrowser(self.status)
        self.list_active_account.setGeometry(QtCore.QRect(360, 10, 251, 341))
        self.list_active_account.setObjectName(_fromUtf8("list_active_account"))
        self.setup_account = QtGui.QCommandLinkButton(self.status)
        self.setup_account.setGeometry(QtCore.QRect(490, 350, 121, 31))
        self.setup_account.setObjectName(_fromUtf8("setup_account"))
        self.main_window_widget.addTab(self.status, _fromUtf8(""))
        self.bot_retweet = QtGui.QWidget()
        self.bot_retweet.setObjectName(_fromUtf8("bot_retweet"))
        self.Active_reetweet = QtGui.QCheckBox(self.bot_retweet)
        self.Active_reetweet.setGeometry(QtCore.QRect(20, 11, 97, 31))
        self.Active_reetweet.setObjectName(_fromUtf8("Active_reetweet"))
        self.Save_run_retweet = QtGui.QCommandLinkButton(self.bot_retweet)
        self.Save_run_retweet.setGeometry(QtCore.QRect(120, 10, 111, 31))
        self.Save_run_retweet.setObjectName(_fromUtf8("Save_run_retweet"))
        self.text_retweet = QtGui.QPlainTextEdit(self.bot_retweet)
        self.text_retweet.setGeometry(QtCore.QRect(20, 50, 211, 81))
        self.text_retweet.setObjectName(_fromUtf8("text_retweet"))
        self.active_acc_retweet = QtGui.QTextBrowser(self.bot_retweet)
        self.active_acc_retweet.setGeometry(QtCore.QRect(20, 140, 211, 241))
        self.active_acc_retweet.setObjectName(_fromUtf8("active_acc_retweet"))
        self.info_retweet = QtGui.QTextBrowser(self.bot_retweet)
        self.info_retweet.setGeometry(QtCore.QRect(250, 40, 361, 341))
        self.info_retweet.setObjectName(_fromUtf8("info_retweet"))
        self.main_window_widget.addTab(self.bot_retweet, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.main_window_widget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar_mw = QtGui.QMenuBar(MainWindow)
        self.menubar_mw.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar_mw.setObjectName(_fromUtf8("menubar_mw"))
        self.menuFile = QtGui.QMenu(self.menubar_mw)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAccount = QtGui.QMenu(self.menubar_mw)
        self.menuAccount.setObjectName(_fromUtf8("menuAccount"))
        self.menuHelp = QtGui.QMenu(self.menubar_mw)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar_mw)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.file_Openlist = QtGui.QAction(MainWindow)
        self.file_Openlist.setObjectName(_fromUtf8("file_Openlist"))
        self.file_Save = QtGui.QAction(MainWindow)
        self.file_Save.setObjectName(_fromUtf8("file_Save"))
        self.file_Save_As = QtGui.QAction(MainWindow)
        self.file_Save_As.setObjectName(_fromUtf8("file_Save_As"))
        self.add_remove_Setup = QtGui.QAction(MainWindow)
        self.add_remove_Setup.setObjectName(_fromUtf8("add_remove_Setup"))
        self.file_Exit = QtGui.QAction(MainWindow)
        self.file_Exit.setObjectName(_fromUtf8("file_Exit"))
        self.Faq = QtGui.QAction(MainWindow)
        self.Faq.setObjectName(_fromUtf8("Faq"))
        self.About_Author = QtGui.QAction(MainWindow)
        self.About_Author.setObjectName(_fromUtf8("About_Author"))
        self.About_Qt = QtGui.QAction(MainWindow)
        self.About_Qt.setObjectName(_fromUtf8("About_Qt"))
        self.menuFile.addAction(self.file_Openlist)
        self.menuFile.addAction(self.file_Save)
        self.menuFile.addAction(self.file_Save_As)
        self.menuFile.addAction(self.file_Exit)
        self.menuAccount.addSeparator()
        self.menuAccount.addAction(self.add_remove_Setup)
        self.menuHelp.addAction(self.Faq)
        self.menuHelp.addAction(self.About_Author)
        self.menuHelp.addAction(self.About_Qt)
        self.menubar_mw.addAction(self.menuFile.menuAction())
        self.menubar_mw.addAction(self.menuAccount.menuAction())
        self.menubar_mw.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.main_window_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Status_text.setPlainText(_translate("MainWindow", "Lorem Rensum", None))
        self.Push_saveList.setText(_translate("MainWindow", "Save List", None))
        self.Push_SendNow.setText(_translate("MainWindow", "Send Now", None))
        self.list_tweet.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.push_export.setText(_translate("MainWindow", "Export", None))
        self.push_import.setText(_translate("MainWindow", "Import", None))
        self.list_active_account.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.setup_account.setText(_translate("MainWindow", "Setup Account", None))
        self.main_window_widget.setTabText(self.main_window_widget.indexOf(self.status), _translate("MainWindow", "Status", None))
        self.Active_reetweet.setText(_translate("MainWindow", "Active", None))
        self.Save_run_retweet.setText(_translate("MainWindow", "Save and Run", None))
        self.text_retweet.setPlainText(_translate("MainWindow", "Retweet, Retwet", None))
        self.active_acc_retweet.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_retweet.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.main_window_widget.setTabText(self.main_window_widget.indexOf(self.bot_retweet), _translate("MainWindow", "Bot Retweet", None))
        self.main_window_widget.setTabText(self.main_window_widget.indexOf(self.tab_2), _translate("MainWindow", "Advance", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAccount.setTitle(_translate("MainWindow", "Setup Account", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.file_Openlist.setText(_translate("MainWindow", "Open List", None))
        self.file_Save.setText(_translate("MainWindow", "Save", None))
        self.file_Save_As.setText(_translate("MainWindow", "Save As", None))
        self.add_remove_Setup.setText(_translate("MainWindow", "Add/Remove", None))
        self.file_Exit.setText(_translate("MainWindow", "Exit", None))
        self.Faq.setText(_translate("MainWindow", "F.A.Q", None))
        self.About_Author.setText(_translate("MainWindow", "About Author", None))
        self.About_Qt.setText(_translate("MainWindow", "About License", None))
