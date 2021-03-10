# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hello.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class myImgLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(myImgLabel, self).__init__(parent)
        f = QFont("ZYSong18030",10)                                            # 设置字体,字号
        self.setFont(f)                                                        # 未来自定义事件后，该两句删掉或注释掉
    
    def mousePressEvent(self, event):
        if event.buttons () == QtCore.Qt.LeftButton:                           # 左键按下
            print("单击鼠标左键")  # 响应测试语句
   

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1317, 823)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = myImgLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 510, 72, 16))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(820, 180, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action2_2 = QtWidgets.QAction(MainWindow)
        self.action2_2.setObjectName("action2_2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    '''重载一下鼠标按下事件(单击)'''


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hello"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.action2.setText(_translate("MainWindow", "2"))
        self.action2_2.setText(_translate("MainWindow", "2"))
        self.action3.setText(_translate("MainWindow", "3"))
