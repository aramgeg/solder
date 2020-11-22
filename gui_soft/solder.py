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
import glob
import datetime
#from serial import Serial
import sys
import time

class Worker(QObject):
    finished = pyqtSignal()
    intReady = pyqtSignal(str)

    @pyqtSlot()
    def __init__(self):
        super(Worker, self).__init__()
        self.working = True
        self.ser = serial.Serial(ui.uart_port,9600)
        self.set_temp_slider_prev =0
        self.data_len_prev =0

    def work(self):
        while self.working:
            self.read_data()
            self.update_data()
            self.display_data()

        self.finished.emit()

    def read_data(self):
        self.data = self.ser.readline().decode('utf-8')
        self.set_temp_slider=ui.set_temp_slider.value()
        time.sleep(0.1)

    def update_data(self):
        if(self.set_temp_slider != self.set_temp_slider_prev):
            self.set_temp_slider_prev = self.set_temp_slider
            self.ser.write(str.encode('200,100,1\r\n'))
            print(self.set_temp_slider)
        #time.sleep(0.2)

    def display_data(self):
        self.values = self.data.split(",")
        self.values_len = (float(self.values[0])+float(self.values[1])+float(self.values[2]))
        
        if(self.values_len != self.data_len_prev):
            self.data_len_prev = self.values_len 
            ui.set_temp.display(float(self.values[0]))
            #ui.set_temp_slider.setValue(float(self.values[0]));
            ui.real_temp.display(float(self.values[1]))
            ui.fan_speed.display(float(self.values[2]))
            #self.textEdit_3.append("{}".format(i))
            #print(self.values[0])
            #print(ui.set_temp_slider.value())


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        self.real_temp = QtWidgets.QLCDNumber(Dialog)
        self.real_temp.setGeometry(QtCore.QRect(20, 110, 81, 41))
        self.real_temp.setObjectName("real_temp")

        self.fan_speed = QtWidgets.QLCDNumber(Dialog)
        self.fan_speed.setGeometry(QtCore.QRect(20, 200, 81, 41))
        self.fan_speed.setObjectName("fan_speed")

        self.set_temp = QtWidgets.QLCDNumber(Dialog)
        self.set_temp.setGeometry(QtCore.QRect(200, 110, 71, 41))
        self.set_temp.setObjectName("set_temp")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 120, 81, 17))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 120, 67, 17))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 210, 81, 17))
        self.label_3.setObjectName("label_3")

        self.fan_speed_slider = QtWidgets.QSlider(Dialog)
        self.fan_speed_slider.setGeometry(QtCore.QRect(20, 260, 160, 16))
        self.fan_speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.fan_speed_slider.setObjectName("fan_speed_slider")

        self.set_temp_slider = QtWidgets.QSlider(Dialog)
        self.set_temp_slider.setGeometry(QtCore.QRect(200, 160, 160, 16))
        self.set_temp_slider.setOrientation(QtCore.Qt.Horizontal)
        self.set_temp_slider.setObjectName("set_temp_slider")
        self.set_temp_slider.setRange(150, 480)
        self.set_temp_slider.setTickInterval(10)
        self.set_temp_slider.setSingleStep(1)

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 111, 25))
        self.comboBox.setObjectName("comboBox")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 10, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.connect_serial_port)

        ports=self.available_serial_ports()
        for port in ports:
            self.comboBox.addItem(port)


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

    def updateLabel(self, value):
        self.fan_speed.display(value)
        print(value)


    def recurring_timer(self):
        if self.serial_connected:
            #self.counter+=1
            self.values=[]
            if self.ser.isOpen():
                self.c = self.ser.read(size=1).decode("ASCII") #better ASCII
                if(self.c =='\n'):
                    self.values = self.datastring.split(",")
                    self.datastring=""
                else:
                    self.datastring=self.datastring+self.c#.decode('utf-8')                
                    #    datastring=""
                print(self.values)
                self.values=[]

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Real Temp"))
        self.label_2.setText(_translate("Dialog", "Set Temp"))
        self.label_3.setText(_translate("Dialog", "Fan Speed"))
        self.pushButton.setText(_translate("Dialog", "Connect"))

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
