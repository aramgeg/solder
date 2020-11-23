# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solder.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(706, 338)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-image: url(\"/workspace/solder/gui_soft/soft/image/background.png\"); background-repeat: no-repeat; \n"
"background-position: center")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 681, 321))
        self.tabWidget.setStyleSheet("gridline-color: rgba(13, 13, 15, 128);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.hot_gun_on_off = QtWidgets.QPushButton(self.tab_4)
        self.hot_gun_on_off.setGeometry(QtCore.QRect(540, 10, 121, 41))
        self.hot_gun_on_off.setStyleSheet("  border-radius: 10px;")
        self.hot_gun_on_off.setObjectName("hot_gun_on_off")
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 221, 201))
        self.groupBox.setObjectName("groupBox")
        self.set_temp_slider = QtWidgets.QSlider(self.groupBox)
        self.set_temp_slider.setGeometry(QtCore.QRect(10, 140, 201, 16))
        self.set_temp_slider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #999999;\n"
"height: 18px;\n"
"\n"
"border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 18px;\n"
" background-image: url(:/slider-knob.png)\n"
"}\n"
"\n"
"QSlider::add-page:qlineargradient {\n"
"background: lightgrey;\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QSlider::sub-page:qlineargradient {\n"
"background: blue;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top-left-radius: 9px;\n"
"border-bottom-left-radius: 9px;\n"
"}")
        self.set_temp_slider.setOrientation(QtCore.Qt.Horizontal)
        self.set_temp_slider.setObjectName("set_temp_slider")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_2.setGeometry(QtCore.QRect(10, 30, 161, 41))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.set_temp = QtWidgets.QLCDNumber(self.splitter_2)
        self.set_temp.setStyleSheet("QLCDNumber{\n"
"  background-color: rgb(217, 214, 28);\n"
"  border: 2px solid rgb(113, 113, 113);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.set_temp.setObjectName("set_temp")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(10, 80, 191, 41))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.real_temp = QtWidgets.QLCDNumber(self.splitter)
        self.real_temp.setStyleSheet("QLCDNumber{\n"
"  background-color: rgb(217, 214, 28);\n"
"  border: 2px solid rgb(113, 113, 113);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.real_temp.setObjectName("real_temp")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.tab_4)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 101, 25))
        self.comboBox.setStyleSheet("border-radius: 10px;")
        self.comboBox.setObjectName("comboBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 50, 231, 201))
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.fan_speed_slider = QtWidgets.QSlider(self.groupBox_2)
        self.fan_speed_slider.setGeometry(QtCore.QRect(10, 140, 211, 16))
        self.fan_speed_slider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #999999;\n"
"height: 18px;\n"
"\n"
"border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 18px;\n"
" background-image: url(:/slider-knob.png)\n"
"}\n"
"\n"
"QSlider::add-page:qlineargradient {\n"
"background: lightgrey;\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QSlider::sub-page:qlineargradient {\n"
"background: blue;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top-left-radius: 9px;\n"
"border-bottom-left-radius: 9px;\n"
"}")
        self.fan_speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.fan_speed_slider.setObjectName("fan_speed_slider")
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_3.setGeometry(QtCore.QRect(10, 30, 151, 41))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.fan_speed = QtWidgets.QLCDNumber(self.splitter_3)
        self.fan_speed.setStyleSheet("QLCDNumber{\n"
"  background-color: rgb(217, 214, 28);\n"
"  border: 2px solid rgb(113, 113, 113);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.fan_speed.setObjectName("fan_speed")
        self.label_3 = QtWidgets.QLabel(self.splitter_3)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.tab_4)
        self.pushButton.setGeometry(QtCore.QRect(120, 20, 71, 25))
        self.pushButton.setStyleSheet("  border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget = QtWidgets.QWidget(self.tab_3)
        self.widget.setGeometry(QtCore.QRect(0, 10, 361, 271))
        self.widget.setObjectName("widget")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(370, 10, 301, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 281, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pid_p_splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.pid_p_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.pid_p_splitter.setObjectName("pid_p_splitter")
        self.pid_p_slider = QtWidgets.QSlider(self.pid_p_splitter)
        self.pid_p_slider.setMaximum(10)
        self.pid_p_slider.setOrientation(QtCore.Qt.Horizontal)
        self.pid_p_slider.setObjectName("pid_p_slider")
        self.pid_p_lcd = QtWidgets.QLCDNumber(self.pid_p_splitter)
        self.pid_p_lcd.setStyleSheet("QLCDNumber{\n"
"  background-color: rgb(217, 214, 28);\n"
"  border: 2px solid rgb(113, 113, 113);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pid_p_lcd.setObjectName("pid_p_lcd")
        self.label_4 = QtWidgets.QLabel(self.pid_p_splitter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.pid_p_splitter, 1, 0, 1, 1)
        self.pid_i_splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.pid_i_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.pid_i_splitter.setObjectName("pid_i_splitter")
        self.pid_i_slider = QtWidgets.QSlider(self.pid_i_splitter)
        self.pid_i_slider.setMouseTracking(True)
        self.pid_i_slider.setOrientation(QtCore.Qt.Horizontal)
        self.pid_i_slider.setObjectName("pid_i_slider")
        self.pid_i_lcd = QtWidgets.QLCDNumber(self.pid_i_splitter)
        self.pid_i_lcd.setStyleSheet("QLCDNumber{\n"
"  background-color: rgb(217, 214, 28);\n"
"  border: 2px solid rgb(113, 113, 113);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pid_i_lcd.setObjectName("pid_i_lcd")
        self.label_5 = QtWidgets.QLabel(self.pid_i_splitter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.pid_i_splitter, 2, 0, 1, 1)
        self.pid_d_splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.pid_d_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.pid_d_splitter.setObjectName("pid_d_splitter")
        self.pid_d_slider = QtWidgets.QSlider(self.pid_d_splitter)
        self.pid_d_slider.setOrientation(QtCore.Qt.Horizontal)
        self.pid_d_slider.setObjectName("pid_d_slider")
        self.pid_d_lcd = QtWidgets.QLCDNumber(self.pid_d_splitter)
        self.pid_d_lcd.setStyleSheet("QLCDNumber{\n"
"  background-color: rgb(217, 214, 28);\n"
"  border: 2px solid rgb(113, 113, 113);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pid_d_lcd.setObjectName("pid_d_lcd")
        self.label_6 = QtWidgets.QLabel(self.pid_d_splitter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.pid_d_splitter, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Soldering Station"))
        self.hot_gun_on_off.setText(_translate("Dialog", "On"))
        self.groupBox.setTitle(_translate("Dialog", "Hot Air"))
        self.label_2.setText(_translate("Dialog", "Set Temp"))
        self.label.setText(_translate("Dialog", "Real Temp"))
        self.groupBox_2.setTitle(_translate("Dialog", "Air Speed"))
        self.label_3.setText(_translate("Dialog", "Fan Speed"))
        self.pushButton.setText(_translate("Dialog", "Connect"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Main"))
        self.groupBox_3.setTitle(_translate("Dialog", "PID Correction"))
        self.label_4.setText(_translate("Dialog", "Proportional"))
        self.label_5.setText(_translate("Dialog", "Integral"))
        self.label_6.setText(_translate("Dialog", "derivative"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
