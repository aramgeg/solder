import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from solder import Ui_Dialog
import time

class MyFirstGuiProgram(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        # Connect "add" button with a custom function (addInputTextToListbox)
        #self.label_2.setText("Hello")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = MyFirstGuiProgram(dialog)

    dialog.show()
    sys.exit(app.exec_())