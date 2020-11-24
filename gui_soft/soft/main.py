import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from solder import Ui_Dialog
import time

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
        self.ser= serial.Serial(prog.uart_port,9600)
        self.set_temp_slider_prev= 0
        self.set_air_speed_slider_prev= 0
        self.set_air_speed_slider_value=0
        self.set_temp_slider_value=0
        self.data_len_prev= 0
        self.prev_set_temp= 0
        prog.hot_gun_on_off.clicked.connect(self.button)
        self.on_off_state = 1
        self.set_temp_plot=[]
        self.real_temp_plot=[]
        #Connect PID sliders response
        prog.pid_p_slider.valueChanged.connect(self.pid_p_slider)
        prog.pid_i_slider.valueChanged.connect(self.pid_i_slider)
        prog.pid_d_slider.valueChanged.connect(self.pid_d_slider)
        prog.pid_write_settings_btn.clicked.connect(self.write_pid_settings)
        #Pid_values
        self.pid_p_value=0
        self.pid_i_value=0
        self.pid_d_value=0
        self.get_init_values()

    def get_init_values(self):
        print("Get values inital values ")
        try:
            self.init_data = self.ser.readline().decode('utf-8')
            pass
        except Exception as e:
            exit()
            pass
        else:
            pass
        finally:
            pass
        self.init_values = self.init_data.split(",")
        #Set temperature display
        prog.set_temp_slider.setValue(float(self.init_values[0]))
        #Set air speed value
        prog.fan_speed_slider.setValue(float(self.init_values[2]))
        #Set PID values
        prog.pid_p_slider.setValue(float(self.init_values[4])*10)
        prog.pid_i_slider.setValue(float(self.init_values[5])*10)
        prog.pid_d_slider.setValue(float(self.init_values[6])*10)

    def pid_p_slider(self):
        self.pid_p_value = prog.pid_p_slider.value()/10
        prog.pid_p_lcd.display(self.pid_p_value)
        #print(self.pid_p_value,",",self.pid_i_value,",",self.pid_d_value)
        self.write_pid_value()

    def pid_i_slider(self):
        self.pid_i_value = prog.pid_i_slider.value()/10
        prog.pid_i_lcd.display(self.pid_i_value)
        #print(self.pid_p_value,",",self.pid_i_value,",",self.pid_d_value)
        self.write_pid_value()

    def pid_d_slider(self):
        self.pid_d_value = prog.pid_d_slider.value()/10
        prog.pid_d_lcd.display(self.pid_d_value)
        #print(self.pid_p_value,",",self.pid_i_value,",",self.pid_d_value)
        self.write_pid_value()
    
    def write_pid_settings(self):
        print("Save button")
        self.write_pid_value("write")

    def write_pid_value(self,write=""):
        #print("Writing pid value")
        self.ser.write(str.encode("pid,"+str(self.pid_p_value)+','+str(self.pid_i_value)+','+ str(self.pid_d_value)\
            +','+str(write)+'\r\n'))


    def work(self):
        while self.working:
            self.read_data()
            self.display_data()
            self._update_canvas()

        self.finished.emit()

    def read_data(self):
        #Reading Serial Data from Arduino
        self.data = self.ser.readline().decode('utf-8')
        #print(self.data)
        #Getting sliders current postition value
        self.set_temp_slider=str(prog.set_temp_slider.value())
        self.set_air_speed_slider=str(prog.fan_speed_slider.value())

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
        #print(self.set_on_off_uart)
        self.ser.write(str.encode(self.set_temp_uart+','+self.set_air_speed_uart+','+ self.set_on_off_uart+'\r\n'))
        #self.ser.write(str.encode(self.set_temp_uart+','+self.set_air_speed_uart+','+ '0' +'\r\n'))
        #print("Updating values")
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
        prog._dynamic_ax.clear()
        #ax = self.figure.add_subplot(111)
        prog._dynamic_ax.plot(self.set_temp_plot, '*-')
        prog._dynamic_ax.plot(self.real_temp_plot, '*-')
        prog._dynamic_ax.figure.canvas.draw()
        


    def display_data(self):
        self.values = self.data.split(",")

        #print(int(self.values[3]))
        """        
        if(self.prev_set_temp != float(self.values[0])):
            #prog.set_temp.display(int(self.values[0]))
            prog.set_temp_slider.setValue(float(self.values[0]))
            print("set temp slider changed")
            print(self.values[0])
            time.sleep(2)
            self.prev_set_temp=float(self.values[0])
        """
        if(int(self.values[3]) == 1):
            prog.hot_gun_on_off.setText("On")
            prog.hot_gun_on_off.setStyleSheet("background-color: green")
        else:
            prog.hot_gun_on_off.setText("Off")
            prog.hot_gun_on_off.setStyleSheet("background-color: red")

        prog.set_temp.display(float(self.values[0]))
        prog.real_temp.display(float(self.values[1]))
        prog.fan_speed.display(float(self.values[2]))

    def button(self):
        print("Button pressed")
        print(int(self.values[3]))
        if(int(self.values[3]) == 1):
            self.on_off_state = 0
        else:
            self.on_off_state = 1
        self.update_data()
        print(self.on_off_state)

class MyFirstGuiProgram(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        ports=self.available_serial_ports()
        for port in ports:
            self.comboBox.addItem(port)
        self.pushButton.clicked.connect(self.connect_serial_port)
        
        self.widget = QtWidgets.QWidget(self.widget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 351, 261))
        self.widget.setObjectName("widget")
        layout = QtWidgets.QVBoxLayout(self.widget)
        dynamic_canvas = FigureCanvas(Figure(figsize=(1, 1)))
        layout.addWidget(dynamic_canvas)
        self._dynamic_ax = dynamic_canvas.figure.subplots()
        
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
        self.worker.finished.connect(self.loop_finished)  # do something in the gui when the worker loop ends
        self.worker.finished.connect(self.thread.quit)  # tell the thread it's time to stop running
        self.worker.finished.connect(self.worker.deleteLater)  # have worker mark itself for deletion
        self.thread.finished.connect(self.thread.deleteLater)  # have thread mark itself for deletion
        # make sure those last two are connected to themselves or you will get random crashes
        self.thread.start()

    def stop_loop(self):
        self.worker.working = False

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = MyFirstGuiProgram(dialog)

    dialog.show()
    sys.exit(app.exec_())