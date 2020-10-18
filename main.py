from pyModbusTCP.client import ModbusClient
import time
import cv2
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from pyqt5.pyqt5first import Ui_MainWindow
import sys


#SERVER_HOST = "127.0.1.1"
SERVER_HOST = "192.168.1.1"
SERVER_U_ID = 2
a = np.array(65536)
c = ModbusClient(auto_open=True)


c.host(SERVER_HOST)
c.unit_id(SERVER_U_ID)
c.open()


class MainWindow(QtWidgets.QMainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()
        '''設定carema'''

        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture(1)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        '''set icon'''
        self.setWindowIcon(QtGui.QIcon('icon/ncuticon.png'))
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QColor(79, 79, 79))
        self.setPalette(palette)

        '''MainWindow Title'''
        self.setWindowTitle('台達電SCARA人機介面')
        #設定計時器動作show_camera
        self.timer_camera.timeout.connect(self.show_camera)

        #seting progressBar
        self.ui.progressBar_speed.setMinimum(0)
        self.ui.progressBar_speed.setMaximum(99)
        self.ui.progressBar_speed.setValue(0)
        '''顯示速度的數值'''
        #display speed  value
        self.ui.horizontalSlider_speed.valueChanged.connect(self.sliderValue_speed)

        '''旋鈕調整伺服速度'''
        # Dial_speed
        #self.ui.dial_speed.setRange(0, 100)
        #self.ui.dial_speed.setNotchesVisible(True)
        #self.ui.dial_speed.valueChanged.connect(self.dialValue_speed)

        '''伺服異警重置'''
        #reAlarm_button

        self.ui.pushButton_reAlarm.setText('REALARM')
        self.ui.pushButton_reAlarm.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_reAlarm.setStyleSheet('font-size:12px')
        self.ui.pushButton_reAlarm.clicked.connect(self.button_reAlarm)


        #start_button
        '''伺服啟動'''
        self.ui.pushButton_start.setText('OFF')
        self.ui.pushButton_start.setCheckable(True)
        self.ui.pushButton_start.clicked[bool].connect(self.pushButton_start)
        self.ui.pushButton_start.setStyleSheet('background-color:#1AFD9C')
        self.ui.pushButton_start.setStyleSheet('font-size:25px')
        '''伺服停止'''
        #Stop_button
        self.ui.pushButton_stop.setText('stop')
        self.ui.pushButton_stop.clicked.connect(self.pushButton_stop)
        self.ui.pushButton_stop.setStyleSheet('background-color:#1AFD9C')
        self.ui.pushButton_stop.setStyleSheet('font-size:25px')
        '''X座標+'''
        #pushButton_forword
        self.ui.pushButton_forword.setCheckable(True)
        self.ui.pushButton_forword.clicked[bool].connect(self.button_forword)
        self.ui.pushButton_forword.setText('X+')
        self.ui.pushButton_forword.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_forword.setStyleSheet('font-size:18px')

        '''Y座標+'''
        # pushButton_left
        self.ui.pushButton_left.setCheckable(True)
        self.ui.pushButton_left.clicked[bool].connect(self.button_left)
        self.ui.pushButton_left.setText('Y+')
        self.ui.pushButton_left.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_left.setStyleSheet('font-size:18px')

        '''Y座標-'''
        self.ui.pushButton_right.setText('Y-')
        self.ui.pushButton_right.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_right.setStyleSheet('font-size:18px')
        self.ui.pushButton_right.setCheckable(True)
        self.ui.pushButton_right.clicked[bool].connect(self.button_rigth)


        '''X座標+'''
        #pushButton_back
        self.ui.pushButton_back.setText('X-')
        self.ui.pushButton_back.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_back.setStyleSheet('font-size:18px')
        self.ui.pushButton_back.setCheckable(True)
        self.ui.pushButton_back.clicked[bool].connect(self.button_back)


        '''Z座標+'''
        #pushButton_up
        self.ui.pushButton_up.setText('Z+')
        self.ui.pushButton_up.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_up.setStyleSheet('font-size:18px')
        self.ui.pushButton_up.setCheckable(True)
        self.ui.pushButton_up.clicked[bool].connect(self.button_up)


        ''' Z座標-'''
        #pushButton_down
        self.ui.pushButton_down.setText('Z-')
        self.ui.pushButton_down.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_down.setStyleSheet('font-size:18px')
        self.ui.pushButton_down.setCheckable(True)
        self.ui.pushButton_down.clicked[bool].connect(self.button_down)
        # action
        # self.ui.pushButton_start.clicked.connect(self.pushButton_start)

        '''Z旋轉-'''
        #pushButton_rz1
        self.ui.pushButton_rz1.setText('-')
        self.ui.pushButton_rz1.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_rz1.setStyleSheet('font-size:30px')
        self.ui.pushButton_rz1.setCheckable(True)
        self.ui.pushButton_rz1.clicked[bool].connect(self.pushButton_rz1)
        # action
        # self.ui.pushButton_start.clicked.connect(self.pushButton_start)
        '''Z旋轉+'''
        #pushButton_rz2
        self.ui.pushButton_rz2.setText('+')
        self.ui.pushButton_rz2.setStyleSheet("background-color:#ADADAD;")
        self.ui.pushButton_rz2.setStyleSheet('font-size:30px')
        self.ui.pushButton_rz2.setCheckable(True)
        self.ui.pushButton_rz2.clicked[bool].connect(self.pushButton_rz2)

        '''伺服重置'''
        # pushButton_reset
        self.ui.pushButton_reset.setText('reset')
        self.ui.pushButton_reset.setStyleSheet("background-color:#02C874;")
        self.ui.pushButton_reset.setStyleSheet('font-size:25px')

        self.ui.pushButton_reset.clicked.connect(self.butten_reset)


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

        self.ui.label_rx.setText('RZ:')
        self.ui.label_rx.setStyleSheet('font-size:30px')
        self.ui.label_rx.setStyleSheet("color:#FFFFFF;")
        self.ui.label_rx.setFont(QtGui.QFont('Arial', 15))



        '''更新座標數據'''
        #pushbutton_dispos
        self.ui.pushButton_dispos.setText('更新')
        self.ui.pushButton_dispos.setStyleSheet('font-size:25px')
        self.ui.pushButton_dispos.setStyleSheet("background-color:#E0E0E0;")
        self.ui.pushButton_dispos.clicked.connect(self.pushbutton_dispos)
        '''開啟相機'''
        #open button
        self.ui.open_button.setText('open')
        self.ui.open_button.setStyleSheet('font-size:25px')
        self.ui.open_button.setStyleSheet("background-color:#E0E0E0;")
        self.ui.open_button.clicked.connect(self.button_open_camera_clicked)
        '''關閉相機'''
        #close button
        self.ui.close_button.setText('close')
        self.ui.close_button.setStyleSheet('font-size:25px')
        self.ui.close_button.setStyleSheet("background-color:#E0E0E0;")
        #若該按鍵被按，則調用close()，請注意這個close弒父類Qtwidght.QWidget自帶的，會關閉程序
        self.ui.close_button.clicked.connect(self.close)

        #speed_confirm button
        self.ui.confirm.setText('確認')
        self.ui.confirm.setStyleSheet('font-size:25px')
        self.ui.confirm.setStyleSheet("background-color:#E0E0E0;")
        self.ui.confirm.clicked.connect(self.speed_confirm)

    def sliderValue_speed(self):
        velocity = self.ui.horizontalSlider_speed.value()
        self.ui.progressBar_speed.setValue(velocity)
        #rc = c.write_single_register(0x0324,velocity)
        print(velocity)
    def speed_confirm(self):
        velocity = self.ui.horizontalSlider_speed.value()
        rc = c.write_single_register(0x0324, velocity)
        print(velocity)
    #def dialValue_speed(self):
    #    velocity1 = self.ui.dial_speed.value()
    #    self.ui.progressBar_speed.setValue(velocity1)
    #    print(velocity1)
    #    rc = c.write_single_register(0x0324,velocity1)

    #def dialValue_distance(self):
    #    self.ui.progressBar_distance.setValue(self.ui.dial_distance.value())

    def pushButton_start(self,pressed):

        #source=self.sender()
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
            #self.ui.pushButton_right.setText('')
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



    '''9/29更改'''
    def show_camera(self):
        '''從視頻中讀取'''
        flag, self.image = self.cap.read()
        '''把讀取到的大小重新設置為481*351'''
        show = cv2.resize(self.image, (481, 351))
        '''視頻色彩轉回RGB'''
        show = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
        '''把讀取到的視頻數據變成QImage形式'''
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)
        '''往Label顯示視頻'''
        self.ui.Capture.setPixmap(QtGui.QPixmap.fromImage(showImage))
        '''-------------------------------------------------------'''
        x, y, z, rz = read_position()
        '''將X、Y、Z、RZ數據顯示在Label上'''
        self.ui.label_xo.setText(str(x)+'mm')
        self.ui.label_yo.setText(str(y)+'mm')
        self.ui.label_zo.setText(str(z)+'mm')
        self.ui.label_rxo.setText(str(rz)+'deg')

    def button_open_camera_clicked(self):
        '''若定時器未啟動'''
        if self.timer_camera.isActive() == False:
            '''參數0，表示打開USB的鏡頭'''
            '''參數1，表示打開筆電的鏡頭'''
            flag = self.cap.open(0)
            if flag == False:  # flag表示open()成不成功
                msg = QtWidgets.QMessageBox.warning(self, 'warning', "請檢查相機是否連接正確", buttons=QtWidgets.QMessageBox.Ok)
            else:
                '''定時器設置為100ms，每300ms更新一次'''
                self.timer_camera.start(300)
                self.ui.open_button.setText('關閉相機')
        else:
            '''關閉定時器'''
            self.timer_camera.stop()
            '''釋放視頻流'''
            self.cap.release()
            '''清空視頻顯示區域'''
            self.ui.Capture.clear()

            self.ui.open_button.setText('打開相機')

    def pushbutton_dispos(self):

        #read_position()
        x,y,z,rz=read_position()
        '''將X、Y、Z、RZ數據顯示在Label上'''
        self.ui.label_xo.setText(str(x)+'mm')
        self.ui.label_yo.setText(str(y)+'mm')
        self.ui.label_zo.setText(str(z)+'mm')
        self.ui.label_rxo.setText(str(rz)+' deg ')

        print(x)
        print(y)
        print(z)
        print(rz)

def read_servo_speed():
    rc =c.read_holding_registers(0x0324,1)
    print('speed:'+rc)
'''開啟伺服'''
def start_servo():
    rc = c.write_single_register(0x6,0x0101)
    rc = c.write_single_register(0x6,0x0101)
    rc = c.write_single_register(0x7,0x0101)
    rc = c.write_single_register(0x7,0x0101)
'''關閉伺服'''
def close_servo():
    rc = c.write_single_register(0x6,0x0000)
    print(rc)
    rc = c.write_single_register(0x7,0x0000)
    print(rc)

'''動作指令'''
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
'''預警重置'''
def reset_Alarm():

    #rc = c.write_single_register(0x0180,0x01)
    rc = c.write_single_register(0x0026, 0x001)
    rc = c.write_single_register(0x0026, 0x100)
    rc = c.write_single_register(0x0027, 0x001)
    rc = c.write_single_register(0x0027, 0x100)

'''取得座標位置'''
def read_position():

    x2 = c.read_holding_registers(0xf0, 2)
    if x2 == None:
        x2 = c.read_holding_registers(0xf0, 2)

    y2 = c.read_holding_registers(0xf2, 2)
    if y2 == None:
        y2 = c.read_holding_registers(0xf2, 2)

    z2 = c.read_holding_registers(0xf4, 2)
    if z2 == None:
        z2 = c.read_holding_registers(0xf4, 2)

    rz2 = c.read_holding_registers(0xfa, 2)
    if rz2 == None:
        rz2 = c.read_holding_registers(0xfa, 2)

    x = ((a * x2[1]) + x2[0]) / 1000
    y = ((a * y2[1]) + y2[0]) / 1000
    z = ((a * z2[1]) + z2[0]) / 1000
    rz = ((a * rz2[1]) + rz2[0]) / 1000
    return x,y,z,rz










if __name__ == "__main__":
    a = np.array(65536)
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()






    sys.exit(app.exec_())
