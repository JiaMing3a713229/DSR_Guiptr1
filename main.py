from pyModbusTCP.client import ModbusClient
import time
import cv2
import  numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from pyqt5.pyqt5first import Ui_MainWindow
import sys

SERVER_HOST = "127.0.1.1"
SERVER_U_ID = 2
c = ModbusClient(auto_open=True)


c.host(SERVER_HOST)
c.unit_id(SERVER_U_ID)
c.open()

class MainWindow(QtWidgets.QMainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #set icon
        self.setWindowIcon(QtGui.QIcon('icon/ncuticon.png'))
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QColor(79, 79, 79))
        self.setPalette(palette)

        # MainWindow Title
        self.setWindowTitle('台達電SCARA人機介面')





        #seting progressBar
        self.ui.progressBar_speed.setMinimum(0)
        self.ui.progressBar_speed.setMaximum(99)
        self.ui.progressBar_speed.setValue(0)

        #display speed & distance value
        self.ui.horizontalSlider_speed.valueChanged.connect(self.sliderValue_speed)


        # Dial_speed
        self.ui.dial_speed.setRange(0, 100)
        self.ui.dial_speed.setNotchesVisible(True)
        self.ui.dial_speed.valueChanged.connect(self.dialValue_speed)


        #start_button

        self.ui.pushButton_start.setText('OFF')
        self.ui.pushButton_start.setCheckable(True)
        self.ui.pushButton_start.clicked[bool].connect(self.pushButton_start)
        self.ui.pushButton_start.setStyleSheet('background-color:#1AFD9C')
        self.ui.pushButton_start.setStyleSheet('font-size:25px')

        #pushButton_forword
        self.ui.pushButton_forword.setText('forword')
        self.ui.pushButton_forword.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_forword.setStyleSheet('font-size:18px')
        #action
        #self.ui.pushButton_start.clicked.connect(self.pushButton_start)

        # pushButton_left
        self.ui.pushButton_left.setText('left')
        self.ui.pushButton_left.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_left.setStyleSheet('font-size:18px')
        # action
        # self.ui.pushButton_start.clicked.connect(self.pushButton_start)

        #pushButton_right
        self.ui.pushButton_right.setText('right')
        self.ui.pushButton_right.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_right.setStyleSheet('font-size:18px')

        # action
        # self.ui.pushButton_start.clicked.connect(self.pushButton_start)


        #pushButton_back
        self.ui.pushButton_back.setText('back')
        self.ui.pushButton_back.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_back.setStyleSheet('font-size:18px')
        # action
        # self.ui.pushButton_start.clicked.connect(self.pushButton_start)

        #pushButton_up
        self.ui.pushButton_up.setText('up')
        self.ui.pushButton_up.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_up.setStyleSheet('font-size:18px')
        # action
        # self.ui.pushButton_start.clicked.connect(self.pushButton_start)

        #pushButton_down
        self.ui.pushButton_down.setText('down')
        self.ui.pushButton_down.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_down.setStyleSheet('font-size:18px')
        # action
        # self.ui.pushButton_start.clicked.connect(self.pushButton_start)

        #pushButton_rz1
        self.ui.pushButton_rz1.setText('-')
        self.ui.pushButton_rz1.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_rz1.setStyleSheet('font-size:30px')
        # action
        # self.ui.pushButton_start.clicked.connect(self.pushButton_start)

        #pushButton_rz2
        self.ui.pushButton_rz2.setText('+')
        self.ui.pushButton_rz2.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_rz2.setStyleSheet('font-size:30px')
        #self.ui.pushButton_rz2.setStyleSheet('border-radius:10px;')
        # action
        # self.ui.pushButton_start.clicked.connect(self.pushButton_start)

        # pushButton_reset
        self.ui.pushButton_reset.setText('reset')
        self.ui.pushButton_reset.setStyleSheet("background-color:#02C874;")
        self.ui.pushButton_reset.setStyleSheet('font-size:25px')

        self.ui.pushButton_reset.clicked.connect(self.butten_reset)
        # action
        # self.ui.pushButton_start.clicked.connect(self.pushButton_start)

        #label_Z
        self.ui.label_Z.setText('     Z')
        self.ui.label_Z.setStyleSheet('font-size:25px')
        self.ui.label_Z.setStyleSheet("background-color:#E0E0E0;")

        #label_rz
        self.ui.label_rz.setText('    RZ')
        self.ui.label_rz.setStyleSheet('font-size:25px')
        self.ui.label_rz.setStyleSheet("background-color:#E0E0E0;")

        #self.ui.timeEdit.date()

        '''label x axis'''
        self.ui.label_xo.setText('')
        self.ui.label_xo.setStyleSheet('font-size:30px')
        self.ui.label_xo.setStyleSheet("color:#FFFFFF;")
        self.ui.label_xo.setFont(QtGui.QFont('Arial', 15))

        self.ui.label_x.setText('X:')
        self.ui.label_x.setStyleSheet('font-size:30px')
        self.ui.label_x.setStyleSheet("color:#FFFFFF;")
        self.ui.label_x.setFont(QtGui.QFont('Arial', 15))

        '''label y axis'''
        self.ui.label_yo.setText('')
        self.ui.label_yo.setStyleSheet('font-size:30px')
        self.ui.label_yo.setStyleSheet("color:#FFFFFF;")
        self.ui.label_yo.setFont(QtGui.QFont('Arial', 15))

        self.ui.label_y.setText('y:')
        self.ui.label_y.setStyleSheet('font-size:30px')
        self.ui.label_y.setStyleSheet("color:#FFFFFF;")
        self.ui.label_y.setFont(QtGui.QFont('Arial', 18))

        '''label z axis'''
        self.ui.label_zo.setText('')
        self.ui.label_zo.setStyleSheet('font-size:30px')
        self.ui.label_zo.setStyleSheet("color:#FFFFFF;")
        self.ui.label_zo.setFont(QtGui.QFont('Arial', 15))

        self.ui.label_z.setText('Z:')
        self.ui.label_z.setStyleSheet('font-size:30px')
        self.ui.label_z.setStyleSheet("color:#FFFFFF;")
        self.ui.label_z.setFont(QtGui.QFont('Arial', 15))

        '''label RX axis'''
        self.ui.label_rxo.setText('')
        self.ui.label_rxo.setStyleSheet('font-size:30px')
        self.ui.label_rxo.setStyleSheet("color:#FFFFFF;")
        self.ui.label_rxo.setFont(QtGui.QFont('Arial', 15))

        self.ui.label_rx.setText('RX:')
        self.ui.label_rx.setStyleSheet('font-size:30px')
        self.ui.label_rx.setStyleSheet("color:#FFFFFF;")
        self.ui.label_rx.setFont(QtGui.QFont('Arial', 15))

        '''label RY axis'''
        self.ui.label_ryo.setText('')
        self.ui.label_ryo.setStyleSheet('font-size:30px')
        self.ui.label_ryo.setStyleSheet("color:#FFFFFF;")
        self.ui.label_ryo.setFont(QtGui.QFont('Arial', 15))

        self.ui.label_ry.setText('RY:')
        self.ui.label_ry.setStyleSheet('font-size:30px')
        self.ui.label_ry.setStyleSheet("color:#FFFFFF;")
        self.ui.label_ry.setFont(QtGui.QFont('Arial', 15))

        '''label RZ axis'''
        self.ui.label_rz2.setText('')
        self.ui.label_rz2.setStyleSheet('font-size:30px')
        self.ui.label_rz2.setStyleSheet("color:#FFFFFF;")
        self.ui.label_rz2.setFont(QtGui.QFont('Arial', 15))

        self.ui.label_rzi.setText('RX:')
        self.ui.label_rzi.setStyleSheet('font-size:30px')
        self.ui.label_rzi.setStyleSheet("color:#FFFFFF;")
        self.ui.label_rzi.setFont(QtGui.QFont('Arial', 15))

    def sliderValue_speed(self):
        self.ui.progressBar_speed.setValue(self.ui.horizontalSlider_speed.value())

    def sliderValue_distance(self):
        self.ui.progressBar_distance.setValue(self.ui.horizontalSlider_distance.value())

    def dialValue_speed(self):
        self.ui.progressBar_speed.setValue(self.ui.dial_speed.value())

    def dialValue_distance(self):
        self.ui.progressBar_distance.setValue(self.ui.dial_distance.value())

    def pushButton_start(self,pressed):
        source=self.sender()
        result=str(123456)
        if pressed:
            self.ui.pushButton_start.setText('ON')
            self.ui.label_xo.setText(result)
        else:
            self.ui.pushButton_start.setText('OFF')




    def butten_reset(self):
        print("reset!")

def runrobot():
    rc=c.write_single_register(0x6,0x101)
    print(rc)
    rc = c.write_single_register(0x7, 0x101)
    print(rc)

    time.sleep(1)
    print('start 425')
    rc = c.write_single_register(0x300,425)
    time.sleep(10)
    print('stop!')
    rc = c.write_single_register(0x300,1000)
    time.sleep(1)
    print('start 426')
    rc = c.write_single_register(0x300, 426)
    time.sleep(10)
    print('stop!')
    rc = c.write_single_register(0x300, 1000)
    time.sleep(1)






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    runrobot()
