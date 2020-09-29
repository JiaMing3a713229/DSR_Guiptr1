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
cap = cv2.VideoCapture(1)

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

        '''伺服異警重置'''
        #reAlarm_button
        self.ui.pushButton_reAlarm.clicked.connect(self.button_reAlarm)
        self.ui.pushButton_reAlarm.setText('REALARM')
        self.ui.pushButton_reAlarm.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_reAlarm.setStyleSheet('font-size:12px')


        #start_button

        self.ui.pushButton_start.setText('OFF')
        self.ui.pushButton_start.setCheckable(True)
        self.ui.pushButton_start.clicked[bool].connect(self.pushButton_start)
        self.ui.pushButton_start.setStyleSheet('background-color:#1AFD9C')
        self.ui.pushButton_start.setStyleSheet('font-size:25px')

        #Stop_button
        self.ui.pushButton_stop.setText('stop')
        self.ui.pushButton_stop.clicked.connect(self.pushButton_stop)
        self.ui.pushButton_stop.setStyleSheet('background-color:#1AFD9C')
        self.ui.pushButton_stop.setStyleSheet('font-size:25px')

        #pushButton_forword
        self.ui.pushButton_forword.setCheckable(True)
        self.ui.pushButton_forword.clicked[bool].connect(self.button_forword)
        self.ui.pushButton_forword.setText('X+')
        self.ui.pushButton_forword.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_forword.setStyleSheet('font-size:18px')

        #action
        #self.ui.pushButton_start.clicked.connect(self.pushButton_start)

        # pushButton_left
        self.ui.pushButton_left.setCheckable(True)
        self.ui.pushButton_left.clicked[bool].connect(self.button_left)
        self.ui.pushButton_left.setText('Y+')
        self.ui.pushButton_left.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_left.setStyleSheet('font-size:18px')
        # action
        # self.ui.pushButton_start.clicked.connect(self.pushButton_start)

        #pushButton_right
        self.ui.pushButton_right.setText('Y-')
        self.ui.pushButton_right.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_right.setStyleSheet('font-size:18px')
        self.ui.pushButton_right.setCheckable(True)
        self.ui.pushButton_right.clicked[bool].connect(self.button_rigth)

        # action
        # self.ui.pushButton_start.clicked.connect(self.pushButton_start)


        #pushButton_back
        self.ui.pushButton_back.setText('X-')
        self.ui.pushButton_back.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_back.setStyleSheet('font-size:18px')
        self.ui.pushButton_back.setCheckable(True)
        self.ui.pushButton_back.clicked[bool].connect(self.button_back)
        # action
        # self.ui.pushButton_start.clicked.connect(self.pushButton_start)

        #pushButton_up

        self.ui.pushButton_up.setText('Z+')
        self.ui.pushButton_up.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_up.setStyleSheet('font-size:18px')
        self.ui.pushButton_up.setCheckable(True)
        self.ui.pushButton_up.clicked[bool].connect(self.button_up)
        # action
        # self.ui.pushButton_start.clicked.connect(self.pushButton_start)

        #pushButton_down
        self.ui.pushButton_down.setText('Z-')
        self.ui.pushButton_down.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_down.setStyleSheet('font-size:18px')
        self.ui.pushButton_down.setCheckable(True)
        self.ui.pushButton_down.clicked[bool].connect(self.button_down)
        # action
        # self.ui.pushButton_start.clicked.connect(self.pushButton_start)

        #pushButton_rz1
        self.ui.pushButton_rz1.setText('-')
        self.ui.pushButton_rz1.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_rz1.setStyleSheet('font-size:30px')
        self.ui.pushButton_rz1.setCheckable(True)
        self.ui.pushButton_rz1.clicked[bool].connect(self.pushButton_rz1)
        # action
        # self.ui.pushButton_start.clicked.connect(self.pushButton_start)

        #pushButton_rz2
        self.ui.pushButton_rz2.setText('+')
        self.ui.pushButton_rz2.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_rz2.setStyleSheet('font-size:30px')
        self.ui.pushButton_rz2.setCheckable(True)
        self.ui.pushButton_rz2.clicked[bool].connect(self.pushButton_rz2)
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
        velocity = self.ui.horizontalSlider_speed.value()
        self.ui.progressBar_speed.setValue(velocity)
        rc = c.write_single_register(0x0324,velocity)
        print(velocity)

    def dialValue_speed(self):
        velocity1 = self.ui.dial_speed.value()
        self.ui.progressBar_speed.setValue(velocity1)
        print(velocity1)
        rc = c.write_single_register(0x0324,velocity1)

    def dialValue_distance(self):
        self.ui.progressBar_distance.setValue(self.ui.dial_distance.value())

    def pushButton_start(self,pressed):

        source=self.sender()
        #result=str(123456)
        if pressed:
            self.ui.pushButton_start.setText('ON')
            start_servo()
            print('ON')

        else:
            self.ui.pushButton_start.setText('OFF')
            close_servo()
            print('OFF')



    def pushButton_stop(self):
        stoping_jog()

    def butten_reset(self):
        print('homing')
        homing_orgin()

    def button_forword(self,pressed):
        if pressed:
            X_JOG()
            self.ui.pushButton_forword.setText('X+')
            print('X+')
        else:
            stoping_jog()
            #self.ui.pushButton_forword.setText('J1-')
            print('stoping')

    def button_left(self,pressed):
        if pressed:
            Y_JOG()
            print('Y+')
            self.ui.pushButton_left.setText('Y+')
        else:
            stoping_jog()
            print('stoping')
            #self.ui.pushButton_left.setText('J2-')

    def button_rigth(self,pressed):
        if pressed:
            Y_GOJC()
            print('Y-')
            self.ui.pushButton_right.setText('J3+')
        else:
            stoping_jog()
            print('stoping')
            #self.ui.pushButton_right.setText('J3+')

    def button_back(self,pressed):
        if pressed:
            X_GOJC()
            print('X-')
            self.ui.pushButton_right.setText('X-')
        else:
            stoping_jog()
            print('stoping')

    def button_up(self,pressed):
        if pressed:
            Z_JOG()
            print('RX+')
        else:
            stoping_jog()
            print('stoping')

    def button_down(self,pressed):

        if pressed:
            Z_GOJC()
        else:
            stoping_jog()

    def pushButton_rz1(self,pressed):
        if pressed:
            RZ_GOJC()
        else:
            stoping_jog()

    def pushButton_rz2(self,pressed):

        if pressed:
            RZ_JOG()
        else:
            stoping_jog()

    def button_reAlarm(self):
            reset_Alarm()







def start_servo():
    rc = c.write_single_register(0x6,0x101)
    rc = c.write_single_register(0x7,0x101)
    print(rc)
def close_servo():
    rc = c.write_single_register(0x6,0x00)
    rc = c.write_single_register(0x7,0x00)
    print(rc)
def X_JOG():
    rc = c.write_single_register(0x0300,601)
def X_GOJC():
    rc = c.write_single_register(0x0300,602)
def Y_JOG():
    rc = c.write_single_register(0x0300,603)
def Y_GOJC():
    rc = c.write_single_register(0x0300,604)
def Z_JOG():
    rc = c.write_single_register(0x0300,605)
def Z_GOJC():
    rc = c.write_single_register(0x0300,606)
def RX_JOG():
    rc = c.write_single_register(0x0300,607)
def RX_GOJC():
    rc = c.write_single_register(0x0300,608)
def RY_JOG():
    rc = c.write_single_register(0x0300,609)
def RY_GOJC():
    rc = c.write_single_register(0x0300,610)
def RZ_JOG():
    rc = c.write_single_register(0x0300,611)
def RZ_GOJC():
    rc = c.write_single_register(0x0300,612)

'''1405全軸回到機械原點'''
def homing_orgin():
    rc = c.write_single_register(0x0300,1405)
'''0停止運作'''
def stoping_jog():

    rc = c.write_single_register(0x0300,0x0000)

def reset_Alarm():

    rc = c.write_single_register(0x0180,0x01)










if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    #runrobot()
