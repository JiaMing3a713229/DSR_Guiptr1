# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt5first.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(10, 10, 91, 81))
        self.pushButton_start.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";\n"
"border-radius: 10px; \n"
"border: 2px groove gray;")
        self.pushButton_start.setObjectName("pushButton_start")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(640, 470, 371, 102))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.speedtext = QtWidgets.QLabel(self.layoutWidget)
        self.speedtext.setStyleSheet("font: 75 italic 10pt \"3ds\";")
        self.speedtext.setObjectName("speedtext")
        self.gridLayout_2.addWidget(self.speedtext, 0, 0, 1, 1)
        self.dial_speed = QtWidgets.QDial(self.layoutWidget)
        self.dial_speed.setObjectName("dial_speed")
        self.gridLayout_2.addWidget(self.dial_speed, 0, 1, 3, 1)
        self.progressBar_speed = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar_speed.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";")
        self.progressBar_speed.setProperty("value", 24)
        self.progressBar_speed.setObjectName("progressBar_speed")
        self.gridLayout_2.addWidget(self.progressBar_speed, 1, 0, 1, 1)
        self.horizontalSlider_speed = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider_speed.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_speed.setObjectName("horizontalSlider_speed")
        self.gridLayout_2.addWidget(self.horizontalSlider_speed, 2, 0, 1, 1)
        self.pushButton_forword = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_forword.setGeometry(QtCore.QRect(160, 140, 71, 61))
        self.pushButton_forword.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";\n"
"border-radius: 10px;  border: 2px groove gray;")
        self.pushButton_forword.setObjectName("pushButton_forword")
        self.pushButton_left = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_left.setGeometry(QtCore.QRect(70, 220, 71, 61))
        self.pushButton_left.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";")
        self.pushButton_left.setObjectName("pushButton_left")
        self.pushButton_right = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_right.setGeometry(QtCore.QRect(250, 220, 71, 61))
        self.pushButton_right.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";")
        self.pushButton_right.setObjectName("pushButton_right")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(160, 300, 71, 61))
        self.pushButton_back.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";")
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_up = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_up.setGeometry(QtCore.QRect(70, 420, 71, 61))
        self.pushButton_up.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";")
        self.pushButton_up.setObjectName("pushButton_up")
        self.pushButton_down = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_down.setGeometry(QtCore.QRect(250, 420, 71, 61))
        self.pushButton_down.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";")
        self.pushButton_down.setObjectName("pushButton_down")
        self.pushButton_rz1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rz1.setGeometry(QtCore.QRect(70, 520, 71, 61))
        self.pushButton_rz1.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";")
        self.pushButton_rz1.setObjectName("pushButton_rz1")
        self.pushButton_rz2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rz2.setGeometry(QtCore.QRect(250, 520, 71, 61))
        self.pushButton_rz2.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";")
        self.pushButton_rz2.setObjectName("pushButton_rz2")
        self.label_Z = QtWidgets.QLabel(self.centralwidget)
        self.label_Z.setGeometry(QtCore.QRect(170, 430, 51, 41))
        self.label_Z.setObjectName("label_Z")
        self.label_rz = QtWidgets.QLabel(self.centralwidget)
        self.label_rz.setGeometry(QtCore.QRect(170, 530, 51, 41))
        self.label_rz.setObjectName("label_rz")
        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setGeometry(QtCore.QRect(950, 400, 61, 61))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(350, 90, 191, 51))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_y = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_y.setObjectName("label_y")
        self.horizontalLayout_2.addWidget(self.label_y)
        self.label_yo = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_yo.setObjectName("label_yo")
        self.horizontalLayout_2.addWidget(self.label_yo)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(350, 150, 191, 51))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_z = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_z.setObjectName("label_z")
        self.horizontalLayout_3.addWidget(self.label_z)
        self.label_zo = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_zo.setObjectName("label_zo")
        self.horizontalLayout_3.addWidget(self.label_zo)
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(350, 210, 191, 51))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_rx = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_rx.setObjectName("label_rx")
        self.horizontalLayout_4.addWidget(self.label_rx)
        self.label_rxo = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_rxo.setObjectName("label_rxo")
        self.horizontalLayout_4.addWidget(self.label_rxo)
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(350, 270, 191, 51))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_ryo = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_ryo.setObjectName("label_ryo")
        self.horizontalLayout_5.addWidget(self.label_ryo)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(350, 30, 191, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_x = QtWidgets.QLabel(self.layoutWidget1)
        self.label_x.setObjectName("label_x")
        self.horizontalLayout.addWidget(self.label_x)
        self.label_xo = QtWidgets.QLabel(self.layoutWidget1)
        self.label_xo.setObjectName("label_xo")
        self.horizontalLayout.addWidget(self.label_xo)
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(160, 220, 71, 61))
        self.pushButton_stop.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushButton_reAlarm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reAlarm.setGeometry(QtCore.QRect(870, 400, 71, 61))
        self.pushButton_reAlarm.setStyleSheet("font: 75 10pt \"Microsoft YaHei\";")
        self.pushButton_reAlarm.setObjectName("pushButton_reAlarm")
        self.Capture = QtWidgets.QLabel(self.centralwidget)
        self.Capture.setGeometry(QtCore.QRect(550, 30, 481, 351))
        self.Capture.setFrameShape(QtWidgets.QFrame.Box)
        self.Capture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Capture.setLineWidth(7)
        self.Capture.setObjectName("Capture")
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setGeometry(QtCore.QRect(550, 390, 101, 31))
        self.open_button.setObjectName("open_button")
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(670, 390, 101, 31))
        self.close_button.setObjectName("close_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1036, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_start.setText(_translate("MainWindow", "PushButton"))
        self.speedtext.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">speed</span></p></body></html>"))
        self.pushButton_forword.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_left.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_right.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_back.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_up.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_down.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_rz1.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_rz2.setText(_translate("MainWindow", "PushButton"))
        self.label_Z.setText(_translate("MainWindow", "TextLabel"))
        self.label_rz.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_reset.setText(_translate("MainWindow", "PushButton"))
        self.label_y.setText(_translate("MainWindow", "TextLabel"))
        self.label_yo.setText(_translate("MainWindow", "TextLabel"))
        self.label_z.setText(_translate("MainWindow", "TextLabel"))
        self.label_zo.setText(_translate("MainWindow", "TextLabel"))
        self.label_rx.setText(_translate("MainWindow", "TextLabel"))
        self.label_rxo.setText(_translate("MainWindow", "TextLabel"))
        self.label_ryo.setText(_translate("MainWindow", "TextLabel"))
        self.label_x.setText(_translate("MainWindow", "TextLabel"))
        self.label_xo.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_stop.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_reAlarm.setText(_translate("MainWindow", "PushButton"))
        self.Capture.setText(_translate("MainWindow", "TextLabel"))
        self.open_button.setText(_translate("MainWindow", "PushButton"))
        self.close_button.setText(_translate("MainWindow", "PushButton"))


