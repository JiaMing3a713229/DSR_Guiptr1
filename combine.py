from pyModbusTCP.client import ModbusClient
import time
import cv2
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import  QPixmap
from pyqt5.pyqt5first import Ui_MainWindow
import sys
import time


#SERVER_HOST = "127.0.1.1"
SERVER_HOST = "192.168.1.1"
SERVER_U_ID = 2
a = np.array(65536)
c = ModbusClient(auto_open=True)


c.host(SERVER_HOST)
c.unit_id(SERVER_U_ID)
c.open()

cap = cv2.VideoCapture(0)
time.sleep(2)


class MainWindow(QtWidgets.QMainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()
        '''設定carema'''

        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture(0)



        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #set icon
        self.setWindowIcon(QtGui.QIcon('icon/ncuticon.png'))
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QColor(79, 79, 79))
        self.setPalette(palette)

        # MainWindow Title
        self.setWindowTitle('台達電SCARA人機介面')
        ##
        self.ui.Capture.setScaledContents(True)


        #計時

        #GUI內部程式開始
        self.timer_camera.timeout.connect(self.change_pic)
        self.timer_camera.start(1000)  # 啟動 Timer .. 每隔1000ms 會觸發 run
        #self.ui.Capture.setPixmap(QPixmap("D:/Desktop/result/red.jpg"))

        #QtWidgets.QApplication.processEvents()
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

        self.ui.label_rx.setText('RZ:')
        self.ui.label_rx.setStyleSheet('font-size:30px')
        self.ui.label_rx.setStyleSheet("color:#FFFFFF;")
        self.ui.label_rx.setFont(QtGui.QFont('Arial', 15))




        #pushbutton_dispos
        self.ui.pushButton_dispos.setText('更新')
        self.ui.pushButton_dispos.setStyleSheet('font-size:25px')
        self.ui.pushButton_dispos.setStyleSheet("background-color:#E0E0E0;")
        self.ui.pushButton_dispos.clicked.connect(self.pushbutton_dispos)



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

    def change_pic(self):
        self.ui.Capture.setPixmap(QPixmap("D:/Desktop/result/red.jpg"))

    '''
    def show_camera(self):
        flag, self.image = self.cap.read()  # 从视频流中读取

        show = cv2.resize(self.image, (481, 351))  # 把读到的帧的大小重新设置为 481*351

        show = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)  # 视频色彩转换回RGB，这样才是现实的颜色

        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        self.ui.Capture.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage

    def button_open_camera_clicked(self):
        if self.timer_camera.isActive() == False:  # 若定时器未启动
            flag = self.cap.open(1)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            if flag == False:  # flag表示open()成不成功
                msg = QtWidgets.QMessageBox.warning(self, 'warning', "請檢查相機是否連接正確", buttons=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(100)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
                self.ui.open_button.setText('關閉相機')
        else:
            self.timer_camera.stop()  # 关闭定时器
            self.cap.release()  # 释放视频流
            self.ui.Capture.clear()  # 清空视频显示区域
            self.ui.open_button.setText('打開相機')
    '''
    def pushbutton_dispos(self):
        #read_position()
        x,y,z,rz=read_position()
        self.ui.label_xo.setText(str(x))
        self.ui.label_yo.setText(str(y))
        self.ui.label_zo.setText(str(z))
        self.ui.label_rxo.setText(str(rz))

        print(x)
        print(y)
        print(z)
        print(rz)

    def show_pic(self):
        self.ui.Capture.setPixmap(QPixmap("D:/Desktop/result/red.jpg"))

def start_servo():
    rc = c.write_single_register(0x6,0x0101)
    rc = c.write_single_register(0x6,0x0101)
    rc = c.write_single_register(0x7,0x0101)
    rc = c.write_single_register(0x7,0x0101)
def close_servo():
    rc = c.write_single_register(0x6,0x0000)
    print(rc)
    rc = c.write_single_register(0x7,0x0000)
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

def get_picture(width,heigth):


    rat,frame=cap.read()
    frame = cv2.resize(frame, (width, heigth))
    frame = cv2.flip(frame, 1)

    #cv2.imwrite('D:/Desktop/result/imperson.jpg',frame)
    print("get picture")

    return frame
def improve_brightness(img):

    rows, cols, channels = img.shape
    dst = img.copy()
    a = 1
    b = 30
    for i in range(rows):
        for j in range(cols):
            for c in range(3):
                dst[i,j,c] = np.clip(a*img[i,j,c] + b, 0, 255)
    return dst

def roiarea(frame):
    return frame[top:bottom,left:right]

def replaceroi(frame,roi):
    frame[top:bottom,left:right]=roi
    return frame











if __name__ == "__main__":
    a = np.array(65536)
    #cap = cv2.VideoCapture(1)

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    #紅色
    #color = ((156, 43, 46), (180, 255, 255))
    #黃色
    color = ((26, 43, 46), (34, 255, 255))

    lower = np.array(color[0], dtype='uint8')
    upper = np.array(color[1], dtype='uint8')
    '''1為外接'''



    frame=get_picture(400,300)
    #frame=cv2.imread('D:/Desktop/result/test10.jpg')


    #frame=improve_brightness(frame)

    #frame = cv2.resize(frame, (400, 300))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.GaussianBlur(hsv, (11, 11), 0)

    '''hsv 二值化'''
    mask = cv2.inRange(hsv, lower, upper)

    cv2.imshow('inrange',mask)
    #cv2.imwrite("D:/Desktop/result/red.jpg", mask)
    #cv2.imshow('inrange', mask)
    kernel = np.ones((5, 5), np.uint8)
    '''二值化侵蝕'''
    mask = cv2.erode(mask, kernel, iterations=2)
    #cv2.imshow('erode', mask)

    kernel = np.ones((5, 5), np.uint8)
    '''二值化膨脹'''
    mask = cv2.dilate(mask, kernel, iterations=2)

    cv2.imshow('mask',mask)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        cnt = max(contours, key=cv2.contourArea)

        if cv2.contourArea(cnt) > 300:
            x, y, w, h = cv2.boundingRect(cnt)
            x1, y1, x2, y2 = x, y, x + w , y + h

            #dst=frame.copy()
            dst=mask.copy()
            img = cv2.rectangle(frame, (x1-35, y1-35), (x2+20, y2+20), (0, 0, 255), 2)
            cv2.putText(frame, "Red color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))
            #cv2.drawContours(frame, cnt, -1, (0, 0, 255), 2)

            RECT = ((x1-35,y1-35),(x2+20,y2+20))

            (left,top),(right,bottom)=RECT

            roi = roiarea(dst)
            #roi = cv2.resize(roi,(400,300))
            #gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

            ret, binary = cv2.threshold(roi, 127, 255, cv2.THRESH_BINARY)
            #binary = cv2.bitwise_not(binary)
            #cv2.imshow('binary',binary)
            #edged = cv2.Canny(binary, 50, 150)

            #edged = cv2.dilate(edged, None, iterations=1)

            contours1, hierarchy1 = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            approx_result = cv2.approxPolyDP(contours1[0], 30, True)
            cv2.drawContours(roi, contours1, -1, (0, 255, 0), 3)
            cv2.drawContours(roi, [approx_result], -1, (0, 255, 0), 3)


            length = (len(approx_result))
            print(length)
            if length == 5:

                #動作
                print(length)
            if length == 4:

                print(length)

            if length == 3:

                print(length)

            cv2.imshow('roi',roi)


    cv2.imshow("frame", frame)
    cv2.imwrite("D:/Desktop/result/red.jpg", frame)






    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    

    sys.exit(app.exec_())
