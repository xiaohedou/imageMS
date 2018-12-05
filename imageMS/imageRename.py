# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'imageRename.ui'
# Created by: PyQt5 UI code generator 5.11.3,PyCharm
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2018/11/17  18:07
# 文件名称   ：imageRename.py

import os
import os.path
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QMessageBox
from imageMS import imageMark # 导入模块

class Ui_RenameWindow(QMainWindow):

    # 构造方法
    def __init__(self):
        super(Ui_RenameWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)  # 只显示关闭按钮
        self.setupUi(self) # 初始化窗体设置

    # 自动生成的代码，用来对窗体进行设置
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(507, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 重命名设置区域
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 491, 141))
        self.groupBox.setObjectName("groupBox")
        # 文件名大写单选按钮
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 30, 89, 16))
        self.radioButton.setChecked(True) # 默认选中
        self.radioButton.setObjectName("radioButton")
        # 文件名小写单选按钮
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 30, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        # 文件名编号单选按钮
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 60, 89, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        # 设置模板标签
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 90, 54, 21))
        self.label.setObjectName("label")
        # 起始编号标签
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(220, 90, 54, 21))
        self.label_2.setObjectName("label_2")
        # 设置起始编号的文本框
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 90, 61, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        # 编号增量标签
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(360, 90, 54, 21))
        self.label_3.setObjectName("label_3")
        # 设置编号增量的文本框
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 90, 61, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        # 模板下拉列表
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(90, 90, 101, 22))
        self.comboBox.setObjectName("comboBox")
        # 模板中默认提供3种模板
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        # 图片设置区域
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 491, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        # 选择图片路径标签
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 91, 21))
        self.label_4.setObjectName("label_4")
        # 图片路径文本框
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 20, 201, 21))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        # 选择按钮
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(320, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        # 重命名按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        # 显示图片及路径的表格
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 210, 491, 191))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2) # 表格中添加两列
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(0, 130)# 设置第一列宽度
        self.tableWidget.horizontalHeader().setStretchLastSection(True) # 设置自动填充容器
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)  # 垂直滚动条
        MainWindow.setCentralWidget(self.centralwidget)

        # 设置状态栏
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage('准备就绪…… ')  # 设置状态栏默认值
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(0) # 模板下拉列表中默认选择第一项
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 自动生成的代码，用来设置窗体中控件的默认值
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图片批量重命名"))
        self.groupBox.setTitle(_translate("MainWindow", "重命名设置"))
        self.radioButton.setText(_translate("MainWindow", "文件名大写"))
        self.radioButton_2.setText(_translate("MainWindow", "文件名小写"))
        self.radioButton_3.setText(_translate("MainWindow", "文件名编号"))
        self.label.setText(_translate("MainWindow", "设置模板："))
        self.label_2.setText(_translate("MainWindow", "起始编号："))
        self.lineEdit_2.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "编号增量："))
        self.lineEdit_3.setText(_translate("MainWindow", "1"))
        self.comboBox.setItemText(0, _translate("MainWindow", "img_***"))
        self.comboBox.setItemText(1, _translate("MainWindow", "fil_***"))
        self.comboBox.setItemText(2, _translate("MainWindow", "pic_***"))
        self.groupBox_2.setTitle(_translate("MainWindow", "图片设置"))
        self.label_4.setText(_translate("MainWindow", "选择图片路径："))
        self.pushButton.setText(_translate("MainWindow", "选择"))
        self.pushButton_2.setText(_translate("MainWindow", "重命名"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "图片名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "图片路径"))
        # 关联“选择”按钮的方法，用来选择并显示图片列表
        self.pushButton.clicked.connect(self.getFiles)
        # 关联“重命名”按钮的方法，用来执行批量重命名操作
        self.pushButton_2.clicked.connect(self.reName)

    # 获取所有文件
    def getFiles(self):
        try:
            # 选择图片文件夹路径
            self.img_path = QFileDialog.getExistingDirectory(None, "选择图片文件夹路径", os.getcwd())
            self.lineEdit_4.setText(self.img_path) # 显示选择的图片路径
            self.list = os.listdir(self.img_path) # 遍历选择的文件夹
            num=0   # 记录图片数量
            self.tableWidget.setRowCount(0)   # 设置行数为0，以便清除所有行
            self.tableWidget.clearContents()   # 清除所有内容
            for i in range(0, len(self.list)): # 遍历图片列表
                filepath = os.path.join(self.img_path, self.list[i]) # 记录遍历到的文件名
                if os.path.isfile(filepath): # 判断是否为文件
                    imgType = os.path.splitext(filepath)[1]# 获取扩展名
                    if imageMark.Ui_MarkWindow().isImg(imgType): # 判断是否为图片
                        num += 1 # 数量加1
                        self.tableWidget.insertRow(i)  # 添加新行
                        # 设置第一列的值为文件名
                        self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(self.list[i]))
                        # 设置第二列的值为文件路径
                        self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(self.img_path))
            self.statusbar.showMessage('共有图片 '+str(num)+' 张')# 显示图片总数
        except Exception:
            QMessageBox.warning(None, '警告', '请选择一个有效路径……', QMessageBox.Ok)

    # 批量重命名
    def reName(self):
        num = 0  # 记录图片数量
        filename = "" # 记录原文件名
        newfilename = "" # 记录新文件名
        try:
            for i in range(self.tableWidget.rowCount()):  # 遍历图片列表
                filename = self.tableWidget.item(i,0).text()  # 记录遍历到的文件名
                filepath = os.path.join(self.img_path, filename)  # 记录遍历到的文件名(包括路径)
                if os.path.isfile(filepath):  # 判断是否为文件
                    imgType = os.path.splitext(filepath)[1]  # 获取扩展名
                    if imageMark.Ui_MarkWindow().isImg(imgType):  # 判断是否为图片
                        if self.radioButton.isChecked():  # 文件名大写
                            newfilename=str(filename).upper() # 将文件名转换为大写
                            newfilepath = os.path.join(self.img_path, newfilename)  # 新文件名（包括路径）
                            os.rename(filepath,newfilepath) # 重命名文件
                        elif self.radioButton_2.isChecked():  # 文件名小写
                            newfilename = str(filename).lower() # 将文件名转换为小写
                            newfilepath = os.path.join(self.img_path, newfilename)  # 新文件名（包括路径）
                            os.rename(filepath, newfilepath) # 重命名文件
                        elif self.radioButton_3.isChecked():  # 文件名编号
                            strid=self.comboBox.currentText() # 记录当前选择的模板
                            id=int(self.lineEdit_2.text())  # 记录开始编号
                            step=int(self.lineEdit_3.text()) # 记录增量值
                            template='{:0>3d}' # 设置编号格式化为3位
                            # 根据模板、起始编号和增量值生成新文件名
                            newfilename = strid[0:4]+template.format(id+step*i)+imgType
                            newfilepath = os.path.join(self.img_path, newfilename)   # 新文件名（包括路径）
                            os.rename(filepath, newfilepath) # 重命名文件
                        num += 1  # 数量加1
                        # 更新第一列的值为重命名之后的图片文件名
                        self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(newfilename))
            self.statusbar.showMessage('批量重命名完成，共处理图片 ' + str(num) + ' 张')  # 状态栏中显示处理图片总数
        except Exception as e:
            print(e)
            QMessageBox.warning(None, '警告', '请选择正确的重命名方式！', QMessageBox.Ok)
