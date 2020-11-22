# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solder.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys, serial, serial.tools.list_ports, warnings
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import glob
import datetime
#from serial import Serial
import sys
import time
import numpy as np
import random

class Worker(QObject):
    finished = pyqtSignal()
    intReady = pyqtSignal(str)

    @pyqtSlot()
    def __init__(self):
        super(Worker, self).__init__()
        self.working= True
        self.ser= serial.Serial(ui.uart_port,9600)
        self.set_temp_slider_prev= 0
        self.set_air_speed_slider_prev= 0
        self.set_air_speed_slider_value=0
        self.set_temp_slider_value=0
        self.data_len_prev= 0
        self.prev_set_temp= 0
        ui.hot_gun_on_off.clicked.connect(self.button)
        self.on_off_state = 1
        self.set_temp_plot=[]
        self.real_temp_plot=[]
    def work(self):
        while self.working:
            self.read_data()
            self.display_data()
            self._update_canvas()

        self.finished.emit()

    def read_data(self):
        #Reading Serial Data from Arduino
        self.data = self.ser.readline().decode('utf-8')
        #Getting sliders current postition value
        self.set_temp_slider=str(ui.set_temp_slider.value())
        self.set_air_speed_slider=str(ui.fan_speed_slider.value())

        #If sliders value changed do update
        if(self.set_temp_slider != self.set_temp_slider_prev):
            self.set_temp_slider_prev = self.set_temp_slider
            self.set_temp_slider_value = int(self.set_temp_slider[0:2]+"0")
            self.update_data()
        
        if(self.set_air_speed_slider != self.set_air_speed_slider_prev):
            self.set_air_speed_slider_prev = self.set_air_speed_slider
            self.set_air_speed_slider_value = int(self.set_air_speed_slider[0:1]+"0")
            if(self.set_air_speed_slider_value == 10):
                self.set_air_speed_slider_value = 100
            self.update_data()
           #print(self.set_air_speed_slider_value)

    def update_data(self):
        self.set_temp_uart=str(self.set_temp_slider_value)
        self.set_air_speed_uart=str(self.set_air_speed_slider_value)
        self.set_on_off_uart=str(self.on_off_state)
        print(self.set_on_off_uart)
        self.ser.write(str.encode(self.set_temp_uart+','+self.set_air_speed_uart+','+ self.set_on_off_uart+'\r\n'))
        #self.ser.write(str.encode(self.set_temp_uart+','+self.set_air_speed_uart+','+ '0' +'\r\n'))
        print("Updating values")
            #self.ser.write(str.encode('200,100,1\r\n'))
            #print(self.set_temp_slider_value)
        #time.sleep(0.2)

    def _update_canvas(self):
        self.set_temp_plot.append(float(self.values[0]))
        self.real_temp_plot.append(float(self.values[1]))
        plt.pause(0.002)
        #global cnt
        cnt=0
        cnt+=1
        if (cnt>50):
            self.set_temp_plot.pop(0)
            self.real_temp_plot.pop(0)
        ui._dynamic_ax.clear()
        #ax = self.figure.add_subplot(111)
        ui._dynamic_ax.plot(self.set_temp_plot, '*-')
        ui._dynamic_ax.plot(self.real_temp_plot, '*-')
        ui._dynamic_ax.figure.canvas.draw()
        


    def display_data(self):
        self.values = self.data.split(",")

        #print(int(self.values[3]))
        """
        if(self.prev_set_temp != float(self.values[0])):
            self.prev_set_temp=float(self.values[0])
            ui.set_temp.display(float(self.values[0]))
            #ui.set_temp_slider.setValue(float(self.values[0]))
            print("Update set temp")
        """
        if(int(self.values[3]) == 1):
            ui.hot_gun_on_off.setText("On")
            ui.hot_gun_on_off.setStyleSheet("background-color: green")
        else:
            ui.hot_gun_on_off.setText("Off")
            ui.hot_gun_on_off.setStyleSheet("background-color: red")

        ui.set_temp.display(float(self.values[0]))
        ui.real_temp.display(float(self.values[1]))
        ui.fan_speed.display(float(self.values[2]))

    def button(self):
        print("Button pressed")
        print(int(self.values[3]))
        if(int(self.values[3]) == 1):
            self.on_off_state = 0
        else:
            self.on_off_state = 1
        self.update_data()
        print(self.on_off_state)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(575, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Pictures/Webcam/2020-07-01-203153.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(156, 155, 96);")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 101, 25))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 10, 71, 25))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 221, 201))
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
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 40, 231, 201))
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

        #self._main = QtWidgets.QWidget()
        #self.setCentralWidget(self._main)
        #layout = QtWidgets.QVBoxLayout(Dialog)

        #static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        #layout.addWidget(static_canvas)
        #self.addToolBar(NavigationToolbar(static_canvas, self))

        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 250, 700, 500))
        self.widget.setObjectName("widget")
        layout = QtWidgets.QVBoxLayout(self.widget)
        dynamic_canvas = FigureCanvas(Figure(figsize=(1, 1)))
        #dynamic_canvas.setGeometry(QtCore.QRect(440, 10, 121, 41))
        layout.addWidget(dynamic_canvas)

        #self.addToolBar(QtCore.Qt.BottomToolBarArea,
        #                NavigationToolbar(dynamic_canvas, self))

        #self._static_ax = static_canvas.figure.subplots()
        #t = np.linspace(0, 10, 501)
        #self._static_ax.plot(t, np.tan(t), ".")

        self._dynamic_ax = dynamic_canvas.figure.subplots()
        #self._dynamic_ax_2 = dynamic_canvas.figure.subplots()
        #self._timer = dynamic_canvas.new_timer(
        #    100, [(self._update_canvas, (), {})])
        #self._timer.start()


        self.fan_speed.setObjectName("fan_speed")
        self.label_3 = QtWidgets.QLabel(self.splitter_3)
        self.label_3.setObjectName("label_3")        
        self.hot_gun_on_off = QtWidgets.QPushButton(Dialog)
        self.hot_gun_on_off.setGeometry(QtCore.QRect(440, 10, 121, 41))
        self.hot_gun_on_off.setObjectName("hot_gun_on_off")

        ports=self.available_serial_ports()
        for port in ports:
            self.comboBox.addItem(port)


        self.set_temp_slider.setRange(150, 480)
        self.set_temp_slider.setTickPosition(QSlider.TicksBelow)
        self.set_temp_slider.setTickInterval(10)
        self.pushButton.clicked.connect(self.connect_serial_port)
        #self.hot_gun_on_off.clicked.connect(self.on_off_button)
        self.fan_speed_slider.setRange(20, 100)
        self.fan_speed_slider.setTickPosition(QSlider.TicksBelow)
        self.fan_speed_slider.setTickInterval(5)
        """
        #self.timer = QTimer()
        #self.timer.setInterval(100)
        #self.timer.timeout.connect(self.recurring_timer)
        #self.timer.start()
        """
        # print(self.comboBox_1.itemText(index1))
        #self.label_11.setText(ports[0])

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.counter = 1
        self.datastring= ""
        self.serial_connected = False
        self.uart_port = ""

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Dialog", "Connect"))
        self.groupBox.setTitle(_translate("Dialog", "Hot Air"))
        self.label.setText(_translate("Dialog", "Real Temp"))
        self.label_2.setText(_translate("Dialog", "Set Temp"))
        self.groupBox_2.setTitle(_translate("Dialog", "Air Speed"))
        self.label_3.setText(_translate("Dialog", "Fan Speed"))
        self.hot_gun_on_off.setText(_translate("Dialog", "On"))

    def connect_serial_port(self):
        #print(self.comboBox.currentText())
        self.uart_port = self.comboBox.currentText()
        self.pushButton.setStyleSheet("background-color: green")
        self.thread = None
        self.worker = None
        self.start_loop()


    def loop_finished(self):
        print('Looped Finished')

    def start_loop(self):

        self.worker = Worker()  # a new worker to perform those tasks
        self.thread = QThread()  # a new thread to run our background tasks in
        self.worker.moveToThread(
        self.thread)  # move the worker into the thread, do this first before connecting the signals

        self.thread.started.connect(self.worker.work)
        # begin our worker object's loop when the thread starts running

        #self.worker.intReady.connect(self.onIntReady)

        #self.pushButton_2.clicked.connect(self.stop_loop)  # stop the loop on the stop button click

        self.worker.finished.connect(self.loop_finished)  # do something in the gui when the worker loop ends
        self.worker.finished.connect(self.thread.quit)  # tell the thread it's time to stop running
        self.worker.finished.connect(self.worker.deleteLater)  # have worker mark itself for deletion
        self.thread.finished.connect(self.thread.deleteLater)  # have thread mark itself for deletion
        # make sure those last two are connected to themselves or you will get random crashes
        self.thread.start()

    def stop_loop(self):
        self.worker.working = False

    
    """    
    def onIntReady(self, i):
        self.values = i.split(",")
        print(self.values)
        #self.set_temp.display(float(self.values[0]))
        #self.real_temp.display(float(self.values[1]))
        #self.fan_speed.display(float(self.values[2]))
        #self.textEdit_3.append("{}".format(i))
        #print(self.values[0])
    """
    def available_serial_ports(self):
        """ Lists serial port names
    
            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
    
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
