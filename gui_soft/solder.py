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
        Dialog.resize(706, 414)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QDialog{\n"
"background: rgb(85, 87, 83)\n"
"}\n"
"/*\n"
"background-image: url(\"/workspace/solder/gui_soft/soft/image/background.png\"); \n"
"background-repeat: no-repeat; \n"
"background-position: center\n"
"*/")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 681, 381))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 78, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 65, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 34, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 121, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 78, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 65, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 34, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 121, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 78, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 65, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 34, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 121, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setStyleSheet("QTabWidget{\n"
"background-color: rgb(85, 87, 83);\n"
"    selection-color: rgb(245, 121, 0);\n"
"    border-left-color: rgb(193, 125, 17);\n"
"    border-color: rgb(237, 212, 0);\n"
"    alternate-background-color: rgb(114, 159, 207);\n"
"    /*background-color: rgb(238, 238, 236);*/\n"
"    color: rgb(164, 0, 0);\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setStyleSheet("")
        self.tab_4.setObjectName("tab_4")
        self.hot_gun_on_off = QtWidgets.QPushButton(self.tab_4)
        self.hot_gun_on_off.setGeometry(QtCore.QRect(540, 10, 91, 41))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setBold(True)
        font.setWeight(75)
        self.hot_gun_on_off.setFont(font)
        self.hot_gun_on_off.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"background-color: rgb(67, 203, 209)\n"
"}")
        self.hot_gun_on_off.setObjectName("hot_gun_on_off")
        self.layoutWidget = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 60, 571, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"border-radius: 10px;")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.fan_speed_slider = QtWidgets.QSlider(self.groupBox_2)
        self.fan_speed_slider.setGeometry(QtCore.QRect(10, 145, 211, 21))
        self.fan_speed_slider.setStyleSheet("QSlider{\n"
"border-color: rgb(204, 0, 0);\n"
"}")
        self.fan_speed_slider.setMinimum(20)
        self.fan_speed_slider.setMaximum(100)
        self.fan_speed_slider.setPageStep(5)
        self.fan_speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.fan_speed_slider.setObjectName("fan_speed_slider")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 30, 201, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fan_speed = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.fan_speed.setStyleSheet("QLCDNumber{\n"
"  background-color: rgb(67, 203, 209);\n"
"  border: 2px solid rgb(113, 113, 113);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.fan_speed.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.fan_speed.setObjectName("fan_speed")
        self.horizontalLayout_3.addWidget(self.fan_speed)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setStyleSheet("selection-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_8.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"border-radius: 10px;")
        self.groupBox.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox.setObjectName("groupBox")
        self.set_temp_slider = QtWidgets.QSlider(self.groupBox)
        self.set_temp_slider.setGeometry(QtCore.QRect(10, 140, 201, 31))
        self.set_temp_slider.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.set_temp_slider.setStyleSheet("")
        self.set_temp_slider.setMinimum(140)
        self.set_temp_slider.setMaximum(480)
        self.set_temp_slider.setSingleStep(10)
        self.set_temp_slider.setOrientation(QtCore.Qt.Horizontal)
        self.set_temp_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.set_temp_slider.setTickInterval(10)
        self.set_temp_slider.setObjectName("set_temp_slider")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 30, 201, 111))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.set_temp = QtWidgets.QLCDNumber(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setBold(True)
        font.setWeight(75)
        self.set_temp.setFont(font)
        self.set_temp.setStyleSheet("QLCDNumber{\n"
"  background-color: rgb(67, 203, 209);\n"
"  border: 2px solid rgb(113, 113, 113);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.set_temp.setObjectName("set_temp")
        self.horizontalLayout.addWidget(self.set_temp)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.real_temp = QtWidgets.QLCDNumber(self.layoutWidget2)
        self.real_temp.setStyleSheet("QLCDNumber{\n"
"  background-color: rgb(67, 203, 209);\n"
"  border: 2px solid rgb(113, 113, 113);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.real_temp.setObjectName("real_temp")
        self.horizontalLayout_2.addWidget(self.real_temp)
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8.addWidget(self.groupBox)
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 10, 281, 31))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setStyleSheet("QComboBox{\n"
"border-radius: 10px;\n"
"background-color: rgb(85, 87, 83);\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"background-color: rgb(67, 203, 209)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(370, 10, 301, 271))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"border-radius: 10px;")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 20, 291, 191))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pid_p_slider = QtWidgets.QSlider(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(123)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pid_p_slider.sizePolicy().hasHeightForWidth())
        self.pid_p_slider.setSizePolicy(sizePolicy)
        self.pid_p_slider.setMaximum(100)
        self.pid_p_slider.setSingleStep(1)
        self.pid_p_slider.setSliderPosition(0)
        self.pid_p_slider.setOrientation(QtCore.Qt.Horizontal)
        self.pid_p_slider.setObjectName("pid_p_slider")
        self.horizontalLayout_5.addWidget(self.pid_p_slider)
        self.pid_p_lcd = QtWidgets.QLCDNumber(self.layoutWidget4)
        self.pid_p_lcd.setStyleSheet("QLCDNumber{\n"
"  background-color: rgb(67, 203, 209);\n"
"  border: 2px solid rgb(113, 113, 113);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pid_p_lcd.setObjectName("pid_p_lcd")
        self.horizontalLayout_5.addWidget(self.pid_p_lcd)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pid_i_slider = QtWidgets.QSlider(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(123)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pid_i_slider.sizePolicy().hasHeightForWidth())
        self.pid_i_slider.setSizePolicy(sizePolicy)
        self.pid_i_slider.setMouseTracking(True)
        self.pid_i_slider.setMaximum(100)
        self.pid_i_slider.setSliderPosition(0)
        self.pid_i_slider.setOrientation(QtCore.Qt.Horizontal)
        self.pid_i_slider.setObjectName("pid_i_slider")
        self.horizontalLayout_6.addWidget(self.pid_i_slider)
        self.pid_i_lcd = QtWidgets.QLCDNumber(self.layoutWidget4)
        self.pid_i_lcd.setStyleSheet("QLCDNumber{\n"
"  background-color: rgb(67, 203, 209);\n"
"  border: 2px solid rgb(113, 113, 113);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pid_i_lcd.setObjectName("pid_i_lcd")
        self.horizontalLayout_6.addWidget(self.pid_i_lcd)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pid_d_slider = QtWidgets.QSlider(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(123)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pid_d_slider.sizePolicy().hasHeightForWidth())
        self.pid_d_slider.setSizePolicy(sizePolicy)
        self.pid_d_slider.setMaximum(100)
        self.pid_d_slider.setSliderPosition(0)
        self.pid_d_slider.setOrientation(QtCore.Qt.Horizontal)
        self.pid_d_slider.setObjectName("pid_d_slider")
        self.horizontalLayout_7.addWidget(self.pid_d_slider)
        self.pid_d_lcd = QtWidgets.QLCDNumber(self.layoutWidget4)
        self.pid_d_lcd.setStyleSheet("QLCDNumber{\n"
"  background-color: rgb(67, 203, 209);\n"
"  border: 2px solid rgb(113, 113, 113);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pid_d_lcd.setObjectName("pid_d_lcd")
        self.horizontalLayout_7.addWidget(self.pid_d_lcd)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.pid_write_settings_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.pid_write_settings_btn.setGeometry(QtCore.QRect(110, 220, 111, 31))
        self.pid_write_settings_btn.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"background-color: rgb(67, 203, 209)\n"
"}")
        self.pid_write_settings_btn.setObjectName("pid_write_settings_btn")
        self.plot_widget = QtWidgets.QWidget(self.tab_3)
        self.plot_widget.setGeometry(QtCore.QRect(10, 10, 351, 271))
        self.plot_widget.setObjectName("plot_widget")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Soldering Station"))
        self.hot_gun_on_off.setText(_translate("Dialog", "On"))
        self.groupBox_2.setTitle(_translate("Dialog", "Air Speed"))
        self.label_3.setText(_translate("Dialog", "Fan Speed"))
        self.groupBox.setTitle(_translate("Dialog", "Hot Air"))
        self.label_2.setText(_translate("Dialog", "Set Temp"))
        self.label.setText(_translate("Dialog", "Real Temp"))
        self.pushButton.setText(_translate("Dialog", "Connect"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Main"))
        self.groupBox_3.setTitle(_translate("Dialog", "PID Correction"))
        self.label_4.setText(_translate("Dialog", "Proportional"))
        self.label_5.setText(_translate("Dialog", "Integral"))
        self.label_6.setText(_translate("Dialog", "derivative"))
        self.pid_write_settings_btn.setText(_translate("Dialog", "Write Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())