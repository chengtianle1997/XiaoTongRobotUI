import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from functools import partial
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

import scene0
import scene1
import scene2
import scene3
import scene4

timer = QTimer()  #按钮长按计时器
timer2 = QTimer() #页面重置计时器 


#鼠标任意按下触发事件
def OnAnywhereChicked():
  s0.hide()
  s1.show()
  timer2.timeout.connect(RefreshPage)
  timer2.start(30000)

#页面重置事件
def RefreshPage():
  s1.hide()
  s0.show()
  timer2.stop()

#显示地图界面
def ShowMap():
  s4.show()
  s0.hide()

#返回主界面（从导航导览）
def BackToMain():
  s0.show()
  s4.hide()


#隐藏按钮的鼠标长按事件
def On_pushButton_pressed():
    timer.timeout.connect(PressEvent)
    timer.start(5000)

def PressEvent():
    s2.show()
    timer.stop()

def On_pushButton_release():
    timer.stop()

#关闭程序
def Destroy():
    s0.close()
    s1.close()
    s2.close()

#重启程序
def Restart():
    print("重启成功")

#保存配置文件
def SaveConfig():
    print("保存成功")

#点击对话按钮事件
def StartTalk():
    print("开始对话")



#主运行函数
if __name__ == '__main__':
    #页面1
    app = QApplication(sys.argv)
    s0 = QWidget()
    ui0 = scene0.Ui_Form()
    ui0.setupUi(s0)
    #页面1信号与槽
    ui0.label.button_clicked_signal.connect(OnAnywhereChicked)
    ui0.textBrowser.button_clicked_signal.connect(OnAnywhereChicked)
    ui0.pushButton_2.clicked.connect(OnAnywhereChicked)
    ui0.pushButton_3.clicked.connect(ShowMap)
    ui0.pushButton.pressed.connect(On_pushButton_pressed)
    ui0.pushButton.released.connect(On_pushButton_release)
    s0.show()
    #页面2
    app1 = QApplication(sys.argv) 
    s1 = QWidget()
    ui1 = scene1.Ui_Form()
    ui1.setupUi(s1)
    #页面2信号与槽
    ui1.pushButton_2.pressed.connect(On_pushButton_pressed)
    ui1.pushButton_2.released.connect(On_pushButton_release)
    s1.hide()
    #管理员界面
    app2 = QApplication(sys.argv) 
    s2 = QWidget()
    ui2 = scene2.Ui_Form()
    ui2.setupUi(s2)
    ui2.pushButton_2.clicked.connect(Destroy)
    s2.hide()
    #修改配置界面
    app3 = QApplication(sys.argv) 
    s3 = QWidget()
    ui3 = scene3.Ui_Form()
    ui3.setupUi(s3)
    ui3.pushButton.clicked.connect(SaveConfig)
    ui3.pushButton_2.clicked.connect(s3.hide)
    ui2.pushButton_3.clicked.connect(s3.show)
    s3.hide()
    #导航导览界面
    app4 = QApplication(sys.argv) 
    s4 = QWidget()
    ui4 = scene4.Ui_Form()
    ui4.setupUi(s4)
    ui4.pushButton.clicked.connect(BackToMain)
    s4.hide()
    sys.exit(app.exec_())




        

