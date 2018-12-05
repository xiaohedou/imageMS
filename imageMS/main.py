# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'main.ui'
# Created by: PyQt5 UI code generator 5.11.3,PyCharm
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2018/11/22  17:35
# 文件名称   ：main.py

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QBrush,QPixmap
from imageMS import imageRename,imageMark # 导入模块

class Ui_MainWindow(QtWidgets.QWidget):

    # 自动生成的代码，用来对窗体进行设置
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600) #设置窗体大小
        # 设置菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 23))
        self.menubar.setObjectName("menubar")
        # 添加“主菜单”菜单
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        # 添加“关于”菜单
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        # 添加“添加水印”子菜单
        self.actionMark = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon() # 创建图标对象
        # 设置图标文件
        icon.addPixmap(QtGui.QPixmap("img/mark.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMark.setIcon(icon) # 为“添加水印”子菜单设置图标
        self.actionMark.setObjectName("actionMark")
        # 添加“批量重命名”子菜单
        self.actionRename = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon() # 创建图标对象
        # 设置图标文件
        icon1.addPixmap(QtGui.QPixmap("img/rename.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRename.setIcon(icon1) # 为“批量重命名”子菜单设置图标
        self.actionRename.setObjectName("actionRename")
        # 将“添加水印”子菜单添加到“主菜单”菜单中
        self.menu.addAction(self.actionMark)
        # 将“批量重命名”子菜单添加到“主菜单”菜单中
        self.menu.addAction(self.actionRename)
        # 菜单栏中添加“主菜单”
        self.menubar.addAction(self.menu.menuAction())
        # 添加“关于本软件”子菜单
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon() # 创建图标对象
        # 设置图标文件
        icon.addPixmap(QtGui.QPixmap("img/about.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon) # 为“关于本软件”子菜单设置图标
        self.actionAbout.setObjectName("actionAbout")
        # 将“关于本软件”子菜单添加到“关于”菜单中
        self.menu_2.addAction(self.actionAbout)
        # 菜单栏中添加“关于”菜单
        self.menubar.addAction(self.menu_2.menuAction())
        # 设置窗体背景
        palette = QtGui.QPalette()
        # 设置窗体背景自适应
        palette.setBrush(MainWindow.backgroundRole(),QBrush(QPixmap("img/back.png").scaled(MainWindow.size(),QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.SmoothTransformation)))
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(True) # 设置自动填充背景
        # 禁止显示最大化按钮及调整窗体大小
        MainWindow.setFixedSize(800, 600);
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 自动生成的代码，用来设置窗体中控件的默认值
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图片批量处理器"))
        self.menu.setTitle(_translate("MainWindow", "主菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "|| 关于"))
        self.actionMark.setText(_translate("MainWindow", "添加水印"))
        self.actionRename.setText(_translate("MainWindow", "批量重命名"))
        self.actionAbout.setText(_translate("MainWindow", "关于本软件"))
        # 关联“添加水印”菜单的方法
        self.actionMark.triggered.connect(self.openMark)
        # 关联“批量重命名”菜单的方法
        self.actionRename.triggered.connect(self.openRename)
        # 关联“关于本软件”菜单的方法
        self.actionAbout.triggered.connect(self.about)

    # 打开水印窗体
    def openMark(self):
        self.another = imageMark.Ui_MarkWindow()  # 创建水印窗体对象
        self.another.show()  # 显示窗体

    # 打开重命名窗体
    def openRename(self):
        self.another = imageRename.Ui_RenameWindow()  # 创建重命名窗体对象
        self.another.show()  # 显示窗体

    # 关于本软件
    def about(self):
        QMessageBox.information(None, '关于本软件', '图片批量处理器是一款提供日常工作的工具软件，'
                                               '通过该软件，您可以方便的为图片添加文字水印和图片水印，'
                                               '而且可以自定义添加位置，以及透明度；另外，您还可以通过'
                                               '该软件对图片文件进行重命名，支持文件名大写、小写，以及'
                                               '根据自定义模板对图片文件进行编号。', QMessageBox.Ok)

# 主方法
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程